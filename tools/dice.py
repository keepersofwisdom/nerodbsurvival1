#!/usr/bin/env python3
"""Dice, injury, money and calendar tool for the SUBSUELO roleplay (Santiago de Chile, 2005 →).

Every roll uses the OS random source and is appended to sessions/dice.log,
so the DM never invents a result.

Usage:
  dice.py roll 2d6+1 [label...]
  dice.py check VALUE [MOD] [label...]
  dice.py opposed A B [--mods MA MB] [--labels LA LB]
  dice.py injury MECHANISM [--margin N] [--armor N] [--crit]
  dice.py money AMOUNT UNIT YEAR [--to YEAR]     (UNIT: CLP, UF, USD)
  dice.py date YYYY-MM-DD                         (weekday, holidays, season, sun, timeline)
  dice.py easter YEAR

Add --nolog to any command to skip the log.
"""

import argparse
import datetime
import math
import random
import re
import sys
from pathlib import Path

RNG = random.SystemRandom()
ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "sessions" / "dice.log"
TIMELINE = ROOT / "world" / "timeline.md"

CRIT, SUCCESS, FAIL, FUMBLE = "CRITICAL", "success", "failure", "FUMBLE"
RANK = {CRIT: 3, SUCCESS: 2, FAIL: 1, FUMBLE: 0}


def log(line, enabled):
    if not enabled:
        return
    LOG.parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"{stamp}  {line}\n")


# --- core resolution -------------------------------------------------------

def resolve(value, mod=0, die=None):
    """d20 roll-under: under the effective value succeeds, exact = critical, 20 = fumble.

    Returns (outcome, die, score). Score is what opposed rolls compare.
    """
    ev = value + mod
    d = die if die is not None else RNG.randint(1, 20)
    if ev > 20:
        score = min(d + ev - 20, 20)
        return (CRIT if d + ev - 20 >= 20 else SUCCESS), d, score
    if ev <= 0:
        if d == 1:
            return SUCCESS, d, 1
        return (FUMBLE if d == 20 else FAIL), d, 0
    if d == ev:
        return CRIT, d, d
    if d < ev:
        return SUCCESS, d, d
    return (FUMBLE if d == 20 else FAIL), d, 0


def fmt_check(label, value, mod, outcome, d):
    ev = value + mod
    modtxt = f"{mod:+d}" if mod else ""
    extra = f" (+{ev - 20} → {min(d + ev - 20, 20)})" if ev > 20 else ""
    name = f"{label} " if label else ""
    return f"{name}{value}{modtxt} (EV {ev}): rolled {d}{extra} → {outcome}"


# --- dice commands ---------------------------------------------------------

DICE_RE = re.compile(r"^(\d*)d(\d+)([+-]\d+)?$", re.IGNORECASE)


def cmd_roll(args):
    m = DICE_RE.match(args.expr.replace(" ", ""))
    if not m:
        sys.exit(f"bad dice expression: {args.expr} (use e.g. 1d20, 2d6+1, d100)")
    n = int(m.group(1) or 1)
    sides = int(m.group(2))
    bonus = int(m.group(3) or 0)
    if n < 1 or n > 100 or sides < 2:
        sys.exit("dice count must be 1-100 and sides at least 2")
    rolls = [RNG.randint(1, sides) for _ in range(n)]
    total = sum(rolls) + bonus
    label = " ".join(args.label)
    detail = "+".join(map(str, rolls)) + (f"{bonus:+d}" if bonus else "")
    line = f"{label + ': ' if label else ''}{args.expr} = [{detail}] = {total}"
    print(line)
    log(line, not args.nolog)


def split_mod(rest):
    """Return (mod, label) from 'check VALUE [MOD] [label...]' trailing words."""
    if rest and re.fullmatch(r"[+-]?\d+", rest[0]):
        return int(rest[0]), " ".join(rest[1:])
    return 0, " ".join(rest)


def cmd_check(args):
    mod, label = split_mod(args.rest)
    outcome, d, _ = resolve(args.value, mod)
    line = fmt_check(label, args.value, mod, outcome, d)
    print(line)
    log(line, not args.nolog)


def cmd_opposed(args):
    la, lb = args.labels or ("A", "B")
    ma, mb = args.mods or (0, 0)
    oa, da, sa = resolve(args.a, ma)
    ob, db, sb = resolve(args.b, mb)
    lines = [fmt_check(la, args.a, ma, oa, da), fmt_check(lb, args.b, mb, ob, db)]

    if RANK[oa] != RANK[ob]:
        winner, loser = ((la, oa), (lb, ob)) if RANK[oa] > RANK[ob] else ((lb, ob), (la, oa))
        if winner[1] in (CRIT, SUCCESS):
            verdict = f"{winner[0]} WINS"
            if loser[1] in (CRIT, SUCCESS):
                verdict += " (the other resists, but loses ground)"
        else:
            verdict = f"both fail; {loser[0]} FUMBLED and pays for it"
    elif oa in (FAIL, FUMBLE):
        verdict = "both fail — no one gains" + (" (double fumble: chaos)" if oa == FUMBLE else "")
    elif oa == CRIT:
        verdict = "both CRITICAL — spectacular stalemate"
    elif sa == sb:
        verdict = "equal rolls — stalemate"
    else:
        winner = la if sa > sb else lb
        verdict = f"both succeed; {winner} wins on the higher roll, narrowly"
    lines.append("→ " + verdict)
    out = "\n".join(lines)
    print(out)
    log(" | ".join(lines), not args.nolog)


# --- injuries --------------------------------------------------------------
# mechanism: (dice sides, bonus, penetrating?, description)
MECHANISMS = {
    "fist": (4, 0, False, "punch / kick"),
    "blunt": (6, 1, False, "bat, pipe, stone, rifle butt"),
    "knife": (6, 2, True, "stab or slash"),
    "pellet": (4, 0, True, "riot-control pellet / birdshot at range"),
    "handgun": (6, 4, True, "9 mm / .38 class"),
    "shotgun": (6, 6, True, "buckshot at close range"),
    "rifle": (6, 7, True, "rifle / high-velocity round"),
    "vehicle": (6, 5, False, "car vs pedestrian or rollover"),
    "fall": (6, 3, False, "fall of one or two storeys (DM: +1 per extra storey)"),
    "crush": (6, 4, False, "collapse, entrapment, structural debris"),
    "blast": (6, 6, False, "explosion: blast, fragments and burns"),
}

SEVERITY = [
    (1, "GRAZE — bruise or scratch, no penalty"),
    (4, "MINOR — Hurt (−2): laceration, sprain, simple fracture; ED, not resus (C3–C4)"),
    (7, "SERIOUS — Injured (−5): needs urgent care or surgery; can deteriorate (C2, clock 8)"),
    (10, "CRITICAL — down; shock or airway threat; dies without intervention (C1, clock 6)"),
    (13, "MORTAL — dying fast (C1, clock 3); survival needs immediate damage control"),
]

LOCATIONS = [
    (2, "head"), (3, "face / eyes"), (4, "neck"), (9, "chest"),
    (13, "abdomen"), (14, "pelvis"), (16, "arm"), (20, "leg"),
]

HINTS = {
    ("head", True): "penetrating TBI; GCS falls, herniation risk; scalp bleeds hard",
    ("head", False): "concussion → epidural/subdural; lucid interval possible; c-spine",
    ("face / eyes", True): "globe rupture / orbital injury; airway blood",
    ("face / eyes", False): "facial fractures, epistaxis, airway at risk if mid-face unstable",
    ("neck", True): "zone I–III: vessels, airway, oesophagus; expanding haematoma = airway now",
    ("neck", False): "c-spine, laryngeal fracture, carotid dissection",
    ("chest", True): "pneumo/haemothorax; precordial 'box' → tamponade; tension within minutes",
    ("chest", False): "rib fractures, flail, contusion, tension PTX, aortic tear if high energy",
    ("abdomen", True): "bowel, liver, spleen; haemorrhagic shock; laparotomy",
    ("abdomen", False): "spleen/liver laceration; FAST; may look fine for an hour",
    ("pelvis", True): "iliac vessels, bladder, rectum; junctional bleeding hard to compress",
    ("pelvis", False): "pelvic ring fracture; litres into the retroperitoneum; binder",
    ("arm", True): "brachial artery? tourniquet; nerve injury",
    ("arm", False): "fracture, compartment syndrome",
    ("leg", True): "femoral artery = exsanguination in minutes; tourniquet",
    ("leg", False): "femur fracture (1–1.5 L blood), open fracture, crush syndrome",
}


def cmd_injury(args):
    mech = args.mechanism.lower()
    if mech not in MECHANISMS:
        sys.exit(f"unknown mechanism {mech}; choose from: {', '.join(MECHANISMS)}")
    sides, bonus, penetrating, desc = MECHANISMS[mech]
    d = RNG.randint(1, sides)
    crit = 3 if args.crit else 0
    margin = max(0, args.margin) // 4  # a clean hit (big success margin) hurts more
    total = d + bonus + crit + margin - args.armor
    result = "LETHAL — dead or unsalvageable on scene"
    for limit, text in SEVERITY:
        if total <= limit:
            result = text
            break
    loc_roll = RNG.randint(1, 20)
    location = next(name for limit, name in LOCATIONS if loc_roll <= limit)
    side = ""
    if location in ("arm", "leg"):
        side = "left " if RNG.randint(1, 2) == 1 else "right "
    hint = HINTS[(location, penetrating)]
    parts = [f"d{sides} {d}", f"{mech} {bonus:+d}"]
    if crit:
        parts.append("crit +3")
    if margin:
        parts.append(f"margin +{margin}")
    if args.armor:
        parts.append(f"armour −{args.armor}")
    line = (f"injury ({desc}): {', '.join(parts)} = {total} → {result} | "
            f"location d20 {loc_roll}: {side}{location} — {hint}")
    print(line)
    log(line, not args.nolog)


# --- money -----------------------------------------------------------------
# Approximate values for play. UF on 1 January; USD = annual average CLP per dollar;
# minimum wage = monthly gross in force for most of the year. Reconcile with
# research/02_chile_timeline_2005_2026.md; values after 2025 are estimates.
ECON = {
    2005: (17317, 560, 127500), 2006: (17974, 530, 135000), 2007: (18336, 522, 144000),
    2008: (19622, 522, 159000), 2009: (21452, 560, 165000), 2010: (20942, 510, 172000),
    2011: (21456, 484, 182000), 2012: (22294, 486, 193000), 2013: (22841, 495, 210000),
    2014: (23310, 570, 225000), 2015: (24627, 654, 241000), 2016: (25629, 677, 257500),
    2017: (26348, 649, 270000), 2018: (26799, 641, 288000), 2019: (27565, 703, 301000),
    2020: (28310, 792, 320500), 2021: (29070, 760, 337000), 2022: (30996, 873, 400000),
    2023: (35122, 840, 460000), 2024: (36790, 944, 500000), 2025: (38419, 950, 529000),
    2026: (39700, 950, 539000),
}


def econ(year):
    if year in ECON:
        return ECON[year]
    last = max(ECON)
    if year > last:
        uf, usd, wage = ECON[last]
        growth = 1.035 ** (year - last)  # assume ~3.5% inflation a year
        return int(uf * growth), usd, int(wage * growth)
    sys.exit(f"no economic data before {min(ECON)}")


def fmt_clp(x):
    return "$" + f"{x:,.0f}".replace(",", ".") + " CLP"


def cmd_money(args):
    unit = args.unit.upper()
    uf, usd, wage = econ(args.year)
    if unit == "CLP":
        clp = args.amount
    elif unit == "UF":
        clp = args.amount * uf
    elif unit == "USD":
        clp = args.amount * usd
    else:
        sys.exit("unit must be CLP, UF or USD")
    print(f"{args.amount:,.2f} {unit} in {args.year} = {fmt_clp(clp)} = {clp / uf:,.1f} UF "
          f"= US${clp / usd:,.0f}  (UF {fmt_clp(uf)}, US$1 ≈ {usd} CLP, "
          f"{clp / wage:,.1f}× the minimum wage of {fmt_clp(wage)})")
    if args.to:
        uf2, usd2, wage2 = econ(args.to)
        clp2 = clp / uf * uf2
        print(f"  same real value in {args.to}: {fmt_clp(clp2)} = US${clp2 / usd2:,.0f} "
              f"(indexed by UF)")


# --- calendar --------------------------------------------------------------

MONTHS = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# (month, day): (name, first year it was a national holiday or None, note)
FIXED_HOLIDAYS = {
    (1, 1): ("Año Nuevo", None, ""),
    (5, 1): ("Día del Trabajo", None, ""),
    (5, 21): ("Glorias Navales (Iquique, 1879)", None, ""),
    (6, 29): ("San Pedro y San Pablo", None, "moved to the nearest Monday"),
    (7, 16): ("Virgen del Carmen", 2007, ""),
    (8, 15): ("Asunción de la Virgen", None, ""),
    (9, 18): ("Fiestas Patrias — Independencia", None, "the dieciocho: fondas, asado, cueca"),
    (9, 19): ("Glorias del Ejército", None, "military parade in Parque O'Higgins"),
    (10, 12): ("Encuentro de Dos Mundos", None, "moved to the nearest Monday"),
    (10, 31): ("Día de las Iglesias Evangélicas", 2008, "may move to a Friday"),
    (11, 1): ("Todos los Santos", None, ""),
    (12, 8): ("Inmaculada Concepción", None, ""),
    (12, 25): ("Navidad", None, "Christmas in midsummer heat"),
}

# Dates people remember (shown from the year after the event).
ANNIVERSARIES = {
    (9, 11): (1973, "anniversary of the 1973 coup: vigils, barricades in the poblaciones, a tense night"),
    (3, 3): (1985, "anniversary of the 1985 central Chile earthquake (M8.0)"),
    (2, 27): (2010, "anniversary of the 27F earthquake and tsunami (M8.8)"),
    (10, 18): (2019, "anniversary of the estallido social (18-O): crowds at Plaza Baquedano"),
    (2, 25): (2025, "anniversary of the national blackout of 2025"),
}


def gregorian_easter(y):
    a = y % 19
    b, c = divmod(y, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = (h + l - 7 * m + 114) % 31 + 1
    return datetime.date(y, month, day)


def season(date):
    m, d = date.month, date.day
    md = m * 100 + d
    if md >= 1221 or md < 321:
        return "summer (hot, dry, smoke from fires some years; 30–35°C afternoons)"
    if md < 621:
        return "autumn (cool mornings, first rains from May, smog season begins)"
    if md < 923:
        return "winter (frost at dawn, rain fronts, smog and pre-emergency alerts, snow on the Andes)"
    return "spring (warm days, jacarandá and pollen, snowmelt in the rivers)"


def sun_times(date, lat=-33.45, lon=-70.67, tz=-4):
    """Approximate sunrise/sunset for Santiago in UTC−4 (NOAA-style approximation)."""
    n = date.timetuple().tm_yday
    gamma = 2 * math.pi / 365 * (n - 1)
    eqtime = 229.18 * (0.000075 + 0.001868 * math.cos(gamma) - 0.032077 * math.sin(gamma)
                       - 0.014615 * math.cos(2 * gamma) - 0.040849 * math.sin(2 * gamma))
    decl = (0.006918 - 0.399912 * math.cos(gamma) + 0.070257 * math.sin(gamma)
            - 0.006758 * math.cos(2 * gamma) + 0.000907 * math.sin(2 * gamma)
            - 0.002697 * math.cos(3 * gamma) + 0.00148 * math.sin(3 * gamma))
    rlat = math.radians(lat)
    cos_ha = (math.cos(math.radians(90.833)) / (math.cos(rlat) * math.cos(decl))
              - math.tan(rlat) * math.tan(decl))
    ha = math.degrees(math.acos(max(-1, min(1, cos_ha))))
    noon = 720 - 4 * lon - eqtime + tz * 60
    rise, sett = noon - 4 * ha, noon + 4 * ha

    def hm(minutes):
        minutes %= 1440
        return f"{int(minutes // 60):02d}:{int(minutes % 60):02d}"
    return hm(rise), hm(sett)


def timeline_entries(iso):
    if not TIMELINE.exists():
        return []
    return [line.strip() for line in TIMELINE.read_text(encoding="utf-8").splitlines()
            if iso in line]


def cmd_date(args):
    try:
        date = datetime.date.fromisoformat(args.date)
    except ValueError:
        sys.exit("date must be YYYY-MM-DD (Gregorian)")
    y = date.year
    notes = []
    key = (date.month, date.day)
    if key in FIXED_HOLIDAYS:
        name, since, note = FIXED_HOLIDAYS[key]
        if since is None or y >= since:
            notes.append(f"feriado: {name}" + (f" ({note})" if note else ""))
    easter = gregorian_easter(y)
    offset = (date - easter).days
    movable = {-46: "Miércoles de Ceniza", -7: "Domingo de Ramos", -2: "Viernes Santo (feriado)",
               -1: "Sábado Santo (feriado)", 0: "Domingo de Resurrección (Easter)"}
    if offset in movable:
        notes.append(movable[offset])
    if key == (6, 21) and y >= 2021:
        notes.append("feriado: Día de los Pueblos Indígenas (winter solstice; exact day varies 20–21 Jun)")
    if key in ANNIVERSARIES and y > ANNIVERSARIES[key][0]:
        notes.append(ANNIVERSARIES[key][1])
    if date.month == 9 and 10 <= date.day <= 20:
        notes.append("Fiestas Patrias season: fondas, kites, empanadas, traffic out of the city, ED full of drunks and burns")
    if date.month == 12 and date.day == 31:
        notes.append("Año Nuevo eve: fireworks at Torre Entel / Costanera; trauma and burns peak after midnight")
    if date.month in (1, 2):
        notes.append("summer holidays: the city half-empty, staff on vacation, forest-fire season")
    rise, sett = sun_times(date)
    print(f"{WEEKDAYS[date.weekday()]}, {date.day} {MONTHS[date.month]} {y}")
    print(f"  Season: {season(date)}")
    print(f"  Sun (Santiago, UTC−4; add 1 h when summer time is in force, roughly Sep/Oct–Mar/Apr): "
          f"rise {rise}, set {sett}")
    print(f"  Calendar: {'; '.join(notes) if notes else 'an ordinary day'}")
    entries = timeline_entries(args.date)
    if entries:
        print("  world/timeline.md:")
        for e in entries:
            print(f"    {e}")


def cmd_easter(args):
    e = gregorian_easter(args.year)
    print(f"Easter {args.year}: {e.day} {MONTHS[e.month]} "
          f"(Viernes Santo {(e - datetime.timedelta(days=2)).day} {MONTHS[(e - datetime.timedelta(days=2)).month]})")


# --- entry -----------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="SUBSUELO dice, injury, money and calendar")
    p.add_argument("--nolog", action="store_true", help="do not write to sessions/dice.log")
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("roll", help="roll dice, e.g. 1d20, 2d6+1, d100")
    r.add_argument("expr")
    r.add_argument("label", nargs="*")
    r.set_defaults(func=cmd_roll)

    c = sub.add_parser("check", help="d20 roll-under check")
    c.add_argument("value", type=int)
    c.add_argument("rest", nargs="*", metavar="[MOD] [label]")
    c.set_defaults(func=cmd_check)

    o = sub.add_parser("opposed", help="opposed d20 checks")
    o.add_argument("a", type=int)
    o.add_argument("b", type=int)
    o.add_argument("--mods", type=int, nargs=2, metavar=("MA", "MB"))
    o.add_argument("--labels", nargs=2, metavar=("LA", "LB"))
    o.set_defaults(func=cmd_opposed)

    inj = sub.add_parser("injury", help="wound severity and location for a mechanism")
    inj.add_argument("mechanism", help=", ".join(MECHANISMS))
    inj.add_argument("--margin", type=int, default=0, help="attacker's success margin (EV − roll)")
    inj.add_argument("--armor", type=int, default=0, help="vest 4 (stab) / 6 (ballistic), cover, helmet")
    inj.add_argument("--crit", action="store_true")
    inj.set_defaults(func=cmd_injury)

    mo = sub.add_parser("money", help="convert CLP / UF / USD for a year")
    mo.add_argument("amount", type=float)
    mo.add_argument("unit")
    mo.add_argument("year", type=int)
    mo.add_argument("--to", type=int, help="show the same real value in another year")
    mo.set_defaults(func=cmd_money, nolog=True)

    dt = sub.add_parser("date", help="weekday, holidays, season, sun and timeline for a date")
    dt.add_argument("date")
    dt.set_defaults(func=cmd_date, nolog=True)

    e = sub.add_parser("easter", help="Easter for a year")
    e.add_argument("year", type=int)
    e.set_defaults(func=cmd_easter, nolog=True)

    argv = sys.argv[1:]
    nolog = "--nolog" in argv
    argv = [a for a in argv if a != "--nolog"]
    args = p.parse_args(argv)
    args.nolog = nolog or getattr(args, "nolog", False)
    args.func(args)


if __name__ == "__main__":
    main()
