# MEDICINE — PATIENTS, PROCEDURES, OUTCOMES

The heart of the game. Medicine here is **real**: real physiology, real drugs, real timings, real
Chilean institutions, and the practice **of the year in play** (2005 medicine is not 2025
medicine). Patients die when they would die. Good medicine is the best protection there is, and
it is not always enough.

For any clinical fact the DM is unsure of (a dose, a ventilator setting, what a 2005 Chilean ED
had, how a burn evolves at 48 h), ask the **`clinician`** agent.

---

## 1. Running a case

1. The DM writes a **patient card** (§3) *before* the patient arrives, including hidden problems.
2. The patient arrives through narration: the ambulance doors, the smell, the noise, what the
   paramedic shouts, what the eye catches first.
3. The player acts. The DM answers with **findings, vitals, results and the patient's
   evolution**, in real time, beat by beat (§4).
4. The DM rolls only where §5 says so.
5. When the case resolves (admitted, transferred, discharged, dead), the DM rolls the
   **Outcome** (§7) and records it.

Not every patient needs a card. A shift has twenty patients, and three of them are scenes.
The rest are narration (§10).

---

## 2. The player's medicine and the character's medicine

- **If the player orders it, he does it.** "Two large-bore IVs, O-negative, pelvic binder, call
  the OR" happens, at the speed the place and team allow. If it's routine for his skill level,
  there's no roll.
- **The player's knowledge is not limited by the character's**, and the character's isn't
  limited by the player's:
  - If the player misses something the character would notice (his Diagnosis is 16), the DM
    rolls **Diagnosis** secretly and, on a success, gives a **hint** in the character's head
    ("the neck veins are wrong for a man this pale").
  - If the player asks **"what would he think?"**, the DM rolls Diagnosis and answers as the
    character's clinical reasoning, with the uncertainty a real doctor would have.
  - If the player knows something the character couldn't know **in that year** (a 2015 trial
    in 2007), the character may *intuit* it only if it's plausible (he reads, he trained abroad)
    and pays the price of going against the standard of care (colleagues, lawyers, Bureaucracy
    rolls). See §9.
- **The DM never gives the answer away in narration**, but never hides what the character
  would plainly see, hear, smell or measure.
- Vitals and results arrive **when they would**: a capillary glucose in a minute, an ABG in
  five, labs in 45–90 minutes (faster in 2025), a CT when the scanner, the transfer and the
  radiologist allow.

---

## 3. The patient card

```
PATIENT — [name or "NN"], [age], [sex] · [date, time, unit]
Arrival: [how: SAMU / own ambulance / walked in / dumped at the door / police]
Story: [what the paramedic or family says — may be wrong]
Acuity: C1 / C2 / C3 / C4 / C5        Reserve: [1–20]        Insurance: [Fonasa X / Isapre / mutual / none]
Vitals on arrival: HR · BP · RR · SpO2 · T° · GCS · glucose · pain
Problems:
  1. [visible]  — [what kills, how fast] — temporize: [x] — definitive: [y]
  2. [HIDDEN]   — [what reveals it: question / exam / test] — ...
Clock: [■■■■□□] segments, beat = [minutes]
Needs: [blood, OR, ICU bed, CT, cath lab, specialist, transfer]
Complications if mishandled: [list]
People: [family, police, the boyfriend in the waiting room, a reporter]
DM notes: [what the case is *about* — the moral or human weight]
```

### 3.1 Acuity (the Chilean *categorización*)
| Cat. | Meaning | Target time to doctor | Typical |
|---|---|---|---|
| **C1** | Life-threatening now | Immediate | Arrest, shock, airway, GCS ≤ 8, major trauma |
| **C2** | Emergent; can turn C1 | Minutes | Chest pain, stroke, sepsis, high-energy trauma looking well |
| **C3** | Urgent, stable | Within ~1–2 h | Abdominal pain, fractures, asthma, pyelonephritis |
| **C4** | Less urgent | Hours | Sprains, simple cuts, fever in a well child |
| **C5** | Not urgent | When there's time | Prescriptions, colds, certificates |

*(Chilean public EDs categorise C1–C5, ESI-based. The game uses it for every year for
consistency; the research file `05_emergency_medicine_ems_disaster.md` gives the real history.)*

### 3.2 Reserve (1–20)
Physiological reserve: how much the body can take.
| Reserve | Who |
|---|---|
| 17–19 | Young, fit, no disease |
| 13–16 | Healthy adult; healthy child |
| 9–12 | Middle-aged with hypertension or diabetes; heavy drinker; pregnant (two patients!) |
| 5–8 | Elderly; COPD, heart failure, dialysis, cirrhosis, cancer |
| 1–4 | Frail, bedridden, terminal |

---

## 4. Beats and the clock

Each case runs in **beats**. The DM sets the beat length on the card:
| Acuity | Beat | Clock |
|---|---|---|
| C1 | 2–5 min | 3–6 segments |
| C2 | 10–30 min | 6–8 segments |
| C3 | 1–2 h | 8 segments (or none) |

- Each beat in which **a lethal problem is neither temporized nor fixed**, its clock gains a
  segment (two if something done made it worse: a sedative drug in shock, a delay to scan an
  unstable patient, a failed airway).
- **Temporizing** stops the ticking (a needle decompression, a tourniquet, pressure, a binder,
  intubation). Some temporizing measures only buy a few beats (the DM notes how many).
- **Definitive care** removes the problem (the chest drain, the laparotomy, the cath lab, the
  embolisation, antibiotics plus source control). Much definitive care is **not available in a
  stabilization unit**, so the patient must be **transferred** (§8), and that is the business.
- **Clock full:** C1 → cardiac arrest (§6). C2/C3 → becomes C1, or irreversible damage (the
  stroke's lost brain, the dead bowel, the leg that comes off).

---

## 5. When to roll

| Situation | Roll | Mods |
|---|---|---|
| A procedure routine for his skill, in decent conditions | **none** | — |
| The same procedure in hard conditions (moving ambulance, floor of a metro station, dark, smoke, combative patient, difficult anatomy, under fire) | **Procedures** or **Resuscitation** | −2 to −10 |
| A procedure he's rarely or never done (resuscitative thoracotomy, perimortem caesarean, burr hole, lateral canthotomy) | **Procedures** | −3 to −5 (or the Surgery skill if it's surgery) |
| Spotting a hidden problem the player didn't look for | **Diagnosis** (secret) | ± |
| Managing a ventilator, drips and a crashing ICU patient for hours | **Critical Care** | ± |
| Keeping the team working through chaos | **Leadership** | ± |
| A child, a pregnant woman, a 95-year-old | **Special Patients** (instead of, or before, the other roll) | ± |

**Modifiers:** team (none −3, poor −1, good +1, excellent +2), equipment (improvised −3,
standard 0, excellent +2), fatigue, stress, injuries, light and space, the year's technology
(video laryngoscope +2 on a hard airway, ultrasound guidance +2 on lines).

### 5.1 Procedure results
| Result | Effect |
|---|---|
| **Critical** | Perfect and fast: the problem is handled and the beat isn't spent |
| **Success** | Done. The beat is spent |
| **Failure** | Not done this beat. Try again next beat, or change approach (the clock ticks) |
| **Fumble** | A **complication** (§5.2), and the beat is lost |

### 5.2 Complications (pick to fit, or d20)
| d20 | Complication |
|---|---|
| 1–4 | Lost time: equipment missing, wrong tray, a team member freezes |
| 5–7 | The procedure works but causes something new (iatrogenic pneumothorax, an arterial puncture, broken teeth) |
| 8–10 | Unrecognised failure (oesophageal tube, drain in the wrong space): the DM tells the truth only when the patient shows it |
| 11–13 | Contamination or infection (shows days later) |
| 14–15 | Needlestick, splash or cut to a staff member (HIV, hepatitis B/C: follow-up) |
| 16–17 | A drug error: wrong dose, wrong drug, an allergy |
| 18–19 | Equipment failure (the monitor, the suction, the ventilator's battery, the generator) |
| 20 | Everything at once: the DM chooses two |

---

## 6. Cardiac arrest

When a clock fills on a C1 patient, or the story says so, the patient **arrests**. Run the code
narratively (rhythm, compressions, shocks, drugs, the reversible causes: the 4 H's and 4 T's).
Each **2-minute cycle** is a beat. The DM decides the rhythm from the cause.

**ROSC roll** (return of spontaneous circulation), once the player has done what he can (or every
few cycles), roll d20 against:

| Situation | Base EV |
|---|---|
| Witnessed VF/VT, defibrillated within 3 minutes | 15 |
| VF/VT, delayed shock | 9 |
| PEA with the cause **found and fixed** (tension, tamponade, hyperkalaemia, hypovolaemia corrected) | 10 |
| PEA, cause not found | 4 |
| Asystole | 2 |
| Traumatic arrest, cause fixed (tension released, tamponade opened, bleeding controlled) | 6 |
| Traumatic arrest, exsanguination not controlled | 1 |
| Out-of-hospital, unwitnessed, no bystander CPR | −3 to any of the above |
| Hypothermia, drowning, children: "not dead until warm and dead" | +3 |

Mods: Leadership of the team, quality of CPR (mechanical device +1), ECMO-CPR (where it exists,
2015+, a handful of centres in Chile: +4 for the right patient).

- **Success:** ROSC. Now the post-arrest care, and the **Outcome** roll at Reserve −5.
- **Critical:** ROSC, and the brain may be spared (Outcome at Reserve −2).
- **Failure:** keep going or call it. Each further attempt −2 (cumulative).
- **Fumble:** the code goes badly in a way that will be remembered (a family member in the room,
  a rib through the liver, the staff fight).

*Calling the time of death* is the player's choice, never rolled.

---

## 7. The Outcome roll

When the case resolves, roll d20 against **Reserve + Care + Clock**:

| Factor | Mod |
|---|---|
| **Care** — excellent (everything right, fast) | +5 |
| good | +2 |
| adequate | 0 |
| delays / omissions | −3 |
| serious errors | −6 |
| **Clock** — each empty segment remaining | +1 (max +4) |
| clock full (it reached arrest or irreversible damage) | −5 |
| **Definitive care** obtained in time | +2 |
| **Destination** — the receiving hospital is excellent / overwhelmed | +1 / −3 |

| Result | Outcome |
|---|---|
| **Critical** | Full recovery, and something good: a grateful family with connections, a reporter's story, a nurse who saw it |
| **Success** | Survives; recovers well (with the expected course) |
| **Failure** | Survives with **sequelae** or a long, complicated course; or dies days later if the clock was full or Reserve was ≤ 5 |
| **Fumble** | Dies (or the worst survivable outcome: vegetative state, amputation, a brain injury that changes everything) |

The Outcome is often known **days or weeks later**: through a call, a follow-up, a letter, a
lawsuit, a funeral notice in *El Mercurio*. Use that.

---

## 8. Stabilize and transfer (the business model)

The units of the Network do **what must be done now** and send the patient on. That means:
- **"Stabilized"** is a clinical and a legal word. Under the **Ley de Urgencia** (Ley 19.650,
  1999) the private provider must treat a vital emergency without demanding a guarantee, and
  the payment and transfer rules hinge on **stabilization**. See
  `research/04_chile_health_system.md` for exactly how. The DM tracks it on the card.
- **Finding a bed:** calls to clinics and hospitals, Isapre authorisations, Fonasa's bed
  management, favours (Standing and Regard). A **Negotiation** or **Bureaucracy** roll when the
  system resists; a critical finds the perfect bed, a fumble leaves the patient boarding for
  hours in a unit built for minutes.
- **The transfer itself:** the clock keeps ticking in the ambulance at **half speed** with an
  advanced crew and a ventilator (full speed with a basic crew). A **Critical Care** roll for
  long or unstable transfers; traffic is narration (rush hour on Vicuña Mackenna, the
  Costanera's tunnel, the protests at Baquedano).
- **The receiving hospital** decides part of the Outcome (§7). Knowing which hospital is good at
  what, at which hour, is the founder's real skill.

---

## 9. Medicine by year (what exists, and what is standard)

| Period | Standard practice (as a Chilean EM doctor would know it) |
|---|---|
| **2005–2008** | ATLS 7th ed. (2 L of crystalloid first); FAST exists, POCUS rare; direct laryngoscopy, etomidate/succinylcholine; video laryngoscopes almost unknown in Chile; no TXA in trauma; massive transfusion protocols rare; thrombolysis (streptokinase) for STEMI where no cath lab; stroke thrombolysis rare; troponin I; 16-slice CT in big centres; paper charts; pagers and Nokia phones |
| **2009–2013** | CRASH-2 (2010) brings **TXA**; ATLS 8th (2008) and damage-control resuscitation (permissive hypotension, early blood); video laryngoscopes spread in private clinics; POCUS grows; AHA 2010 "C-A-B"; H1N1 (2009) and ECMO's first Chilean runs; 27F (2010) |
| **2014–2019** | ATLS 9th (2012) and 10th (2018); **1:1:1** transfusion (PROPPR 2015); mechanical **thrombectomy** for stroke (2015 trials); REBOA experimental; ECMO-CPR in a few centres; electronic records spread; WhatsApp runs the hospital; the estallido (2019) and its eye injuries |
| **2020–2022** | COVID: prone positioning, high-flow nasal oxygen, ICU expansion, ECMO; PPE shortages; tele-everything |
| **2023–2026** | ATLS 11th edition rolling out; whole-blood programmes beginning in some systems; REBOA in selected centres; POCUS universal; AI tools appearing; violence-related trauma (gunshot wounds) much more common in Santiago than in 2005 |

*Verify specifics with the `clinician` agent before a scene turns on them.*

**Ahead of his time:** the founder reads, travels and trains. If the player has him adopt a
practice before it's standard in Chile (TXA in 2007, whole blood in 2012, a disaster plan the
city doesn't have), it can work (Care +2) but costs money and politics: a **Bureaucracy** or
**Negotiation** roll with colleagues, the SEREMI or the lawyers, and a lawsuit risk if a patient
dies.

---

## 10. The shift (narration and arrival tables)

Most of a shift is montage. To build it, roll **1d6+2** arrivals per hour for a busy central unit
at night (fewer by day in 2005, more in winter), and roll **d100** on the table for each patient
worth a line:

| d100 | Arrival (adjust by season and hour) |
|---|---|
| 01–10 | Chest pain (C2–C3): one in ten is a real infarct |
| 11–18 | Breathless: asthma, COPD, heart failure, pneumonia (winter ×2) |
| 19–25 | Fall, sprain, fracture (old woman on the stairs; a cyclist) |
| 26–31 | Road trauma (C1–C3): car, motorcycle, pedestrian on the Alameda |
| 32–36 | Assault: fists, bottle, knife (Fri/Sat ×2; after 2018, gunshots more often) |
| 37–41 | Abdominal pain: gastroenteritis, appendicitis, the one that's an aneurysm |
| 42–46 | Intoxication: alcohol, pills, pasta base, cocaine, a teenager's overdose |
| 47–51 | Neuro: stroke, seizure, the headache that's a bleed |
| 52–56 | A child: fever, bronchiolitis (winter ×3), a swallowed coin, a scald |
| 57–60 | Psychiatric crisis: suicide attempt, psychosis, panic |
| 61–64 | Sepsis in an old man from a nursing home |
| 65–67 | Workplace accident (a mutual patient: construction, a fall from scaffolding) |
| 68–70 | Pregnancy: bleeding, labour in the car park, ectopic |
| 71–73 | Allergic reaction / anaphylaxis |
| 74–76 | Burns (Fiestas Patrias, New Year, a gas heater in a *mediagua*) |
| 77–79 | Diabetic emergency, kidney failure, hyperkalaemia |
| 80–82 | Frequent flyer: the drunk, the lonely, the one who wants a certificate |
| 83–85 | VIP: a politician's son, a footballer, a TV face (privacy, press, pressure) |
| 86–88 | A colleague, a nurse, a cop, a firefighter as the patient |
| 89–91 | Dead on arrival, or arrest in the waiting room |
| 92–94 | Something strange: a poisoning nobody can name, an injury that doesn't match the story |
| 95–97 | Violence in the unit: a gang following its wounded, a furious family |
| 98–99 | Mass event: a bus, a fire, a collapse, a protest (go to §11) |
| 00 | A patient tied to the main plot (the DM's choice) |

---

## 11. Mass casualties

When patients outnumber hands, switch to **mass-casualty mode**:
1. **Triage** (START or the era's protocol): the DM gives the patients as a list with
   colour-coded categories and quick descriptions. The player sorts them, and the player's
   **choices** (who gets the ventilator, who's left "expectant") are never rolled.
2. **Command:** a **Disaster** roll (or Leadership) per phase (first 30 minutes, first hours,
   the night). Success means the system works (lines of communication, flow, transfers);
   failure means one problem (a lost patient, a jammed entrance, the press in the resus room);
   fumble means a breakdown.
3. **Groups** of similar patients get one Outcome roll per group, using the group's typical
   Reserve and the Care the system could give them.
4. The DM counts the dead honestly, and names some of them.
5. After it: Stress, a debrief (or not), the press, the inquiry, the bill.

---

## 12. Violence and injuries (who gets hurt, and how badly)

Fights are short, confused and lethal. Resolve an attack with an opposed roll (Firearms,
Fighting or Driving vs Fighting, Awareness, Athletics or cover). The winner's **margin** feeds
the injury roll:

```
python3 tools/dice.py injury handgun --margin 9         # 9 mm, a clean hit
python3 tools/dice.py injury knife --armor 4            # stab vest
python3 tools/dice.py injury blast --crit               # a gas explosion, close
```

The tool gives **severity** (graze → minor → serious → critical → mortal → lethal), a
**location**, and a clinical hint. A serious or worse injury becomes a **patient card** (§3),
whether the patient is a stranger, an NPC or the player character himself.
