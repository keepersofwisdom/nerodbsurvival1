# THE NETWORK — RUNNING THE ENTERPRISE

The founder's idea: **get the patient, stabilize, do what must be done now, transfer.** A
flagship clinic in a central position, small **stabilization units** spread across Santiago, and
a fleet of ambulances tying them together. Underneath, quietly, the bunkers.

This file turns that into play: what it costs, what it earns, how it grows, how it fails. The
company's name, structure and money sources are decided in character creation.

> **Numbers** are order-of-magnitude estimates, in UF so they survive inflation, drawn from
> `research/04_chile_health_system.md §2, §5` and `research/06_gazetteer_central_santiago.md §6`
> (both mostly tagged [E]). Use ranges, not midpoints. Convert with `tools/dice.py money`
> (in 2005, 1 UF ≈ CLP 17,300 ≈ US$31; in 2025, 1 UF ≈ CLP 38,400 ≈ US$40).

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

| Type | What it has | Capital (2005, approx.) | Staff (FTE) | Monthly running cost (2005, approx.) |
|---|---|---|---|---|
| **Flagship clinic** | ED with 3–4 resus bays and 10–15 boxes; 2 ORs; 6–10 ICU/intermediate beds; X-ray, ultrasound, CT (or a deal for one); lab; blood bank; pharmacy; ambulance base; HQ; possibly a helipad | 100,000–250,000 UF (building + fit-out + equipment; a 2,000 m² Providencia building alone ≈ 50,000–64,000 UF) | 150–300 | 12,000–25,000 UF |
| **Stabilization unit** | 2 resus bays, 1 damage-control OR (on call), 4 ICU beds, 6 observation chairs, X-ray + ultrasound, point-of-care lab, O-negative in a fridge, 2 advanced ambulances | 29,000–48,000 UF all-in for a converted casona near Plaza Italia (house 6,000–8,400 + fit-out 9,500–15,200 + equipment 13,000–26,000) | 70–100 | 5,500–9,500 UF (payroll ≈ 70–80%) |
| **Small resus post** | 2 resus bays and 4 boxes, no OR, no ICU: stabilize and transfer within hours | 8,000–15,000 UF | 30–40 | 2,000–3,500 UF |
| **Ambulance post** | A garage, a room, a radio | 1,000–3,000 UF | crews only | 300–700 UF + crews |

*2025 equivalents:* property ×2.5, construction ×1.6–1.9, salaries roughly ×1.3 in real terms (UF).

Staff dominate costs. A 24/7 post needs **4–5 people per seat** (shifts, holidays, sick leave):
one doctor on duty every hour of the year is 4–5 doctors on the payroll.

**Quality (1–20)** measures a unit's equipment, protocols and team. It starts at 10 + the
founder's Management/4 (round down) + money spent above minimum, and changes through play
(good hires, training, a disaster handled well, a scandal, cost-cutting). It's the **Care**
baseline for that unit's patients (`medicine.md §7`) and the target for its incident rolls.

---

## 3. Ambulances

| Type | Chilean name | Crew | Capital, equipped (2005) | Running cost of one 24/7 unit incl. crew (2005) | Use |
|---|---|---|---|---|---|
| **Basic** | AEB (básica) | driver + TENS | 800–1,250 UF (US$45–70k) | 230–350 UF/month | Non-critical transfers, events |
| **Advanced** | AEA (avanzada), nurse-led | driver + TENS + nurse/reanimador | 1,450–2,200 UF (US$80–120k) | 460–700 UF/month | Emergencies, the core fleet |
| **Advanced with physician** | AEA "M3" / UCI móvil | + doctor; transport ventilator, pumps | 1,800–2,700 UF | 700–1,050 UF/month | Inter-hospital transfer of ICU patients; the founder's signature |
| **Special** | rescue 4×4, motorcycle, later a helicopter contract | varies | varies | varies | Disasters, traffic, the cordillera |

One 24/7 seat needs **≈4.2 full-time people**; an advanced unit is ~12–13 people. A van does
150–300 km per 24 h in Santiago and is replaced every 5–7 years.

## 4. Revenue

| Line | How it works | Notes |
|---|---|---|
| **Emergency care billed to Fonasa / Isapres / mutuales** | Every patient treated is billed. **Ley de Urgencia** cases are paid until the patient is stabilized | The core income; slow to collect (60–180 days), disputed, and sometimes unpaid |
| **Rebase** (from 2015) | A stabilized Fonasa patient with no public bed stays in the unit's ICU and **Fonasa pays the days** | Lucrative, reliable, blocks the bed the next trauma needs, and a press target ("living off the rebase") |
| **UGCC bed purchase** (from 2009) | The state's bed-management unit buys critical beds from private providers | Spikes in winter, H1N1, COVID |
| **Transfers** | Charged per transfer, per km and per level of care | Clinics and Isapres outsource transfers |
| **Rescue subscriptions** (*planes de rescate*) | Households and companies pay monthly for emergency response at home, at work | Chile's private "rescate" market already exists (see research); it's competitive |
| **Contracts** | Mutuales (work accidents), Isapres, municipalities, events (stadiums, concerts, Fiestas Patrias), mines and construction sites, embassies | Big, steady, political |
| **Private patients** | Out-of-pocket | Small but profitable |
| **Training** | Courses (ATLS-style, disaster, first aid) for companies and staff | Prestige, recruitment, cover for odd purchases |
| **The state** | In a disaster or an epidemic, the state buys beds, transfers and staff | 27F, H1N1, COVID: crisis can be profitable, and that has a moral weight |

**Unpaid care** is real: patients without coverage, foreigners, Fonasa bills rejected. A unit in
the poorest comunas earns less and matters more.

---

### 4.1 The Ley de Urgencia, in eight rules (from `research/04 §8`)
1. **Nobody can be refused or asked for money first** in a vital emergency, in any year. From
   Nov 2009, no cheque or cash guarantee for anything.
2. **The doctor's certificate is money:** it decides who pays, and auditors read it months later.
3. **Stabilization is a legal moment:** certified by the treating doctor; only then can the patient
   be moved; for Fonasa patients it triggers the choice of public network or free choice (the
   DOMA, formalised in 2022).
4. **Transfers fail far more than they succeed** (only ~11–14% of Fonasa patients stabilized in
   private clinics were moved to public hospitals). Plan for patients who stay: the Network
   needs ICU beds, or it gets stuck.
5. **From 2015, Fonasa pays the waiting days** (rebase). Before that, every extra day is a fight.
6. **Mutual, SOAP (traffic) and Isapre patients are good business;** Fonasa tramo A walk-ins are a
   mission, not a margin.
7. **From July 2016, accreditation** is the price of being in an Isapre's GES trauma network.
8. **2022–2024:** the Isapres are shaky, the paperwork stricter, the press watching the rebase.

**Break-even (2005):** a stabilization unit needs roughly **6,000–10,000 UF a month collected**,
that is, 8–15 serious stabilizations a day plus ICU days and contracts. Isapre-heavy: comfortable.
Fonasa-heavy without rebase or contracts: it loses money. Insurers pay 60–180 days late, so a
growing network can be profitable **and still run out of cash**.

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

---

## 9. Running the business in play (the core loop)

Management is the **main stage** of Era I. The medicine happens inside the units; the story
happens in the meetings, the books, the deals and the compromises.

### 9.1 The loop
1. **Situation.** The DM puts a real problem on the table, with **numbers** (UF, pesos,
   patients a day, days of cash), **people** (who wants what), and a **clock** if there is one.
2. **Options.** Two to four concrete choices with their trade-offs spelled out (money, time,
   risk, people, the secret), "…or something else."
3. **Scene.** The player plays the meeting, the call, the visit. Social rolls only where an NPC
   resists; the `npc-voice` agent for the big ones.
4. **Consequence.** The DM updates `world/network.md` and narrates what changes, now and later.

### 9.2 The monthly flash (when the player asks, or at a scene's start)
A short dashboard, per unit and for the whole company:
```
[Month YYYY] Patients/day · % serious · payer mix (Isapre / Fonasa / mutual / SOAP / private)
Collections (UF) · receivables (days) · cash (UF, months of runway) · debt service due
ICU occupancy · transfers achieved · deaths / complaints / lawsuits · staff turnover
Projects (clocks) · threats (clocks) · the one thing that keeps him awake
```

### 9.3 Attention (the founder can't be everywhere)
Each quarter the founder has **3 Focuses**: a unit, a project, a negotiation, the bunkers, his
family, his own health. What he focuses on uses **his** skills and gets **+2** on its rolls.
Everything else runs on his staff's skills (key NPCs' values) and the unit's Quality.
- He may take a **4th Focus** by sacrificing rest: **+2 Stress** and a −3 on the quarter's
  family roll (`campaign_turn.md` Step 5).
- **Family is a Focus.** A quarter without it is noticed at home.

### 9.4 Strategy (at each Year)
The player sets the year's priorities in a few lines (grow or consolidate; quality or margin;
which payers; which barrios; how much goes underground). The DM turns them into projects and
clocks, and the world answers.

### 9.5 Partners, board and investors
Equity is power. Track each owner's **stake**, **agenda** and **Regard**. Big decisions
(new debt, a new unit, selling, a new partner) go to a vote by stake, unless the statutes the
player negotiated say otherwise. Partners can sell to strangers, sue, leak, or be bought out.

### 9.6 Rivals
The big clinic groups, the private rescue companies and the Isapres' own networks watch any
newcomer: they copy, undercut, poach staff, lobby the SEREMI, or offer to buy. Real companies
appear in their public roles; **dirty tricks belong to fictional rivals** (`config.md`).

### 9.7 Typical management scenes
The bank's credit committee · the partners' dinner that becomes a fight · poaching a head nurse
from the Posta · the SEREMI inspector who finds the generator room "larger than declared" ·
the Isapre's contract renewal · a union's first strike notice · the old man's lunch at the Club
de la Unión · the competitor's buyout offer · the press call after a death · firing a friend ·
the auditor who reads the construction invoices · choosing which barrio gets the next unit.
