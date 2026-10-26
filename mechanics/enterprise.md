# THE NETWORK — RUNNING THE ENTERPRISE

The founder's idea: **get the patient, stabilize, do what must be done now, transfer.** A
flagship clinic in a central position, small **stabilization units** spread across Santiago, and
a fleet of ambulances tying them together. Underneath, quietly, the bunkers.

This file turns that into play: what it costs, what it earns, how it grows, how it fails. The
company's name, structure and money sources are decided in character creation.

> **Numbers are provisional** (order-of-magnitude, in UF so they survive inflation). They will
> be reconciled with `research/04_chile_health_system.md` and checked with the `clinician` and
> `researcher` agents before they matter in play. Convert with `tools/dice.py money`.

---

## 1. The company sheet (kept in `world/network.md`)

```
THE NETWORK — [name] · [legal form: S.A., SpA (2007+), Ltda.] · founded [date]
Owners: [founder %, partners %, investors %]
Cash: [UF] · Debt: [UF, lender, rate, due] · Last quarter: revenue / costs / result [UF]
Standing: Medicine · Business · State · Street · Uniforms · The Old Men · Press   (−5…+5)

UNITS
| Unit | Place | Opened | Type | Beds/boxes | Quality | Staff | Monthly result | Permits | Below |
AMBULANCES
| Call sign | Type | Year | Base | Crew | Condition |
KEY STAFF
| Name | Role | Since | Loyalty (−5…+5) | Notes |
PROJECTS (clocks)
| Project | Clock | Cost so far / total | Next step |
THREATS (clocks)
| Threat | Clock | Trigger |
```

---

## 2. Unit types

| Type | What it has | Capital (2005, approx.) | Staff (24/7) | Monthly running cost (approx.) |
|---|---|---|---|---|
| **Flagship clinic** | ED with 3–4 resus bays and 10–15 boxes; 2 ORs; 6–10 ICU/intermediate beds; X-ray, ultrasound, CT (or a deal for one); lab; blood bank; pharmacy; ambulance base; HQ; possibly a helipad | 80,000–200,000 UF (building + fit-out + equipment) | 60–120 people | 6,000–12,000 UF |
| **Stabilization unit** | 2 resus bays, 4–6 boxes, 1 damage-control OR, 2–4 monitored beds, X-ray + ultrasound, point-of-care lab, O-negative in a fridge, 1–2 ambulances | 15,000–40,000 UF | 25–40 people | 1,800–3,500 UF |
| **Ambulance post** | A garage, a room, a radio | 1,000–3,000 UF | crews only | 300–700 UF + crews |

Staff dominate costs. A 24/7 post needs **about five people per seat** (shifts, holidays, sick
leave): one doctor on duty every hour of the year is ~5 doctors on the payroll.

**Quality (1–20)** measures a unit's equipment, protocols and team. It starts at 10 + the
founder's Management/4 (round down) + money spent above minimum, and changes through play
(good hires, training, a disaster handled well, a scandal, cost-cutting). It's the **Care**
baseline for that unit's patients (`medicine.md §7`) and the target for its incident rolls.

---

## 3. Ambulances

| Type | Chilean name (approx.) | Crew | Capital, equipped (2005, approx.) | Use |
|---|---|---|---|---|
| **Basic** | básica / M1 | driver + TENS/paramedic | 900–1,500 UF | Non-critical transfers, events |
| **Advanced** | avanzada / M2 | driver + nurse or paramedic + (doctor) | 1,800–3,000 UF | Emergencies, the core fleet |
| **Critical care** | UCI móvil / M3 | driver + nurse + doctor; ventilator, pumps, monitor-defib | 2,500–4,000 UF | Inter-hospital transfer of ICU patients |
| **Special** | rescue truck, 4×4, bike, motorcycle; later a helicopter contract | varies | varies | Disasters, traffic, the cordillera |

Running cost: fuel, maintenance, insurance, consumables: roughly **60–150 UF per ambulance per
month** without crew. Ambulances age: after ~6–8 years, or 300,000 km, condition drops.

---

## 4. Revenue

| Line | How it works | Notes |
|---|---|---|
| **Emergency care billed to Fonasa / Isapres / mutuales** | Every patient treated is billed. **Ley de Urgencia** cases are paid until the patient is stabilized | The core income; slow to collect (60–180 days), disputed, and sometimes unpaid |
| **Transfers** | Charged per transfer, per km and per level of care | Clinics and Isapres outsource transfers |
| **Rescue subscriptions** (*planes de rescate*) | Households and companies pay monthly for emergency response at home, at work | Chile's private "rescate" market already exists (see research); it's competitive |
| **Contracts** | Mutuales (work accidents), Isapres, municipalities, events (stadiums, concerts, Fiestas Patrias), mines and construction sites, embassies | Big, steady, political |
| **Private patients** | Out-of-pocket | Small but profitable |
| **Training** | Courses (ATLS-style, disaster, first aid) for companies and staff | Prestige, recruitment, cover for odd purchases |
| **The state** | In a disaster or an epidemic, the state buys beds, transfers and staff | 27F, H1N1, COVID: crisis can be profitable, and that has a moral weight |

**Unpaid care** is real: patients without coverage, foreigners, Fonasa bills rejected. A unit in
the poorest comunas earns less and matters more.

---

## 5. The quarter (business turn)

At each **Turn** (`campaign_turn.md`), for the company as a whole and for any unit in trouble:

1. **Books:** revenue − costs = result (the DM estimates from the units, fleet and contracts, and
   states it in round UF).
2. **Management roll** (the founder, or his finance chief), modified by:
   | Factor | Mod |
   |---|---|
   | Cash reserve > 3 months of costs | +2 |
   | Cash < 1 month of costs | −3 |
   | A good finance chief (NPC) | +2 |
   | Expansion this quarter | −2 |
   | A crisis in the city (27F, COVID…) | −3 or +3 (the DM judges whether it hurts or pays) |
   | Founder Stress 12+ or absent | −2 |
3. **Result:**
   | Roll | Effect |
   |---|---|
   | **Critical** | A windfall: a new contract, an investor, a debt forgiven, a rival in trouble |
   | **Success** | Plan holds. Results as estimated |
   | **Failure** | One problem (d6): 1 a payer stops paying · 2 a key staff member quits · 3 equipment breaks · 4 an inspection finds faults · 5 a lawsuit · 6 a cost overrun of 10–30% |
   | **Fumble** | A crisis: two problems, or one serious (a death with press, a fraud, a fire, a strike) |
4. **Incidents per unit:** roll d20 vs the unit's **Quality**. Failure: something goes wrong
   (a patient dies badly, a theft of drugs, a robbery of an ambulance, a fight in the waiting
   room). Fumble: it makes the news. A critical: a celebrated save.
5. **Staff:** for each key NPC, d20: 1–2 something happens to them (illness, a rival offer, a
   scandal, pregnancy, burnout, a death in the family, a betrayal); 19–20 something good (they
   bring a contract, save a life, prove loyal, learn a skill).

## 6. Growth

New things are **projects** with clocks:
| Project | Clocks (each segment ≈ a few weeks, or a roll) | Typical rolls |
|---|---|---|
| Buy or lease a site | Find (4) | Investigation, Negotiation |
| Permits (DOM building permit, SEREMI health authorisation) | 4–6 | Bureaucracy (bribery is possible and has consequences) |
| Build / fit out | 6–8 | Management, Engineering |
| Hire and train the team | 4 | Leadership, Standing (Medicine) |
| Win a contract | 4 | Negotiation, Standing (Business / State) |
| Accreditation (from ~2009) | 6 | Management, Bureaucracy |

Failures add segments or cost; fumbles add a threat clock (a corrupt inspector now owns you, a
neighbour sues, a journalist starts asking why you dig so deep for a "parking lot").

## 7. Money from where?

The founder decides in character creation how the first money arrives, and each choice has
strings: **family money**, **bank loans** (and guarantees), **partners** (other doctors), an
**Isapre or a clinic group** (who will want control), **foreign investors**, or **the Old Men**
(see `preparedness.md` and the arc files for what that might mean). Debt is tracked with
lender, rate and due date. Missed payments make clocks.

## 8. Hiding money

Bunkers cost money that must not appear as bunkers. Ways: inflating construction costs of the
units ("deep foundations", "seismic isolation", "underground parking", "archives", "a generator
room"); a separate company; the Old Men's money; cash. Each method has a risk (an audit, the
SII tax service, a partner who reads the books, a contractor who talks), tracked in the
**Exposure** clock (`preparedness.md §5`).
