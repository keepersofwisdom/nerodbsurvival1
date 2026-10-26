# PREPAREDNESS — BUNKERS, STORES AND THE SECRET

The founder is a prepper. The Network is his public face; underneath it he builds (or finds)
places where people can live through the end, and he fills them. This file covers the bunkers,
what they hold, how long they last, and how the secret is kept.

> Engineering numbers here are game approximations. Real figures (shielding, air, water,
> power, costs) are in `research/07_infrastructure_and_catastrophe.md`; check with the
> `researcher` agent before a scene turns on them.

---

## 1. The bunker sheet (kept in `world/bunkers.md`, DM-side truth in `dm/`)

```
BUNKER — [code name] · beneath [unit / building] · depth [m] · [built / found / restored, year]
Access: [entrances, hidden or not; tunnels and where they lead]
Capacity: [people] for [days]          Protection: [fallout PF / blast psi / seismic / EMP]
Systems:   Air [none / filtered / NBC + overpressure] · Power [grid / diesel N days / solar / batteries]
           Water [tank m³ / well / grid] · Sewage [..] · Comms [radio / landline / sat]
           Medical [none / first aid / resus room / OR] · Heat & cooling [..]
Stores:    Food [person-days] · Water [person-days] · Fuel [days] · Medical [tier] · Weapons [..]
Condition: [1–20; systems decay without maintenance]
Who knows: [list]                        Exposure: [clock]
```

### 1.1 Protection, in game terms
| Protection | What it means | Typical construction |
|---|---|---|
| **Basement** | Shelter from a riot, a quake's aftershocks, a short blackout | Ordinary basement, a strong door, stores |
| **Fallout shelter** (PF ~40–100) | Survives fallout if sealed for weeks | ~1 m of earth or ~60 cm of concrete overhead, filtered air |
| **Deep shelter** (PF 1000+) | Survives fallout and a distant blast; EMP-hardened if designed so | Several metres of overburden, blast doors, NBC filtration, its own power and water |
| **Hardened** | Survives near a blast; designed by the military | Rare. Built by the state, or by men who had the state's engineers |

## 2. Getting a bunker

| Route | How | Rolls |
|---|---|---|
| **Build** under a unit | Disguised as basements, parking, archives, a generator room, seismic foundations | Engineering, Management, Bureaucracy; Exposure risk at each step (spoil trucks, contractors, permits) |
| **Find** | Old plans, old men, rumours, the tunnels around the centre | Investigation, History & Politics, Streetwise; danger |
| **Acquire** | Buy the building above it, inherit it, be given it, take it | Negotiation; the price may not be money |
| **Restore** | An old bunker's systems are dead: air, water, power, seals | Engineering per system (each a clock) |
| **Connect** | Link units to bunkers, bunkers to tunnels | Engineering, and a lot of Exposure |

Building a deep shelter under a unit is a long project (clocks of 8, several of them), and the
cost is large (order of magnitude: from a few thousand UF for a reinforced basement to tens of
thousands for a real deep shelter; the research file has real comparisons).

## 3. Stores

Stores are counted in **person-days** (one person, one day).
| Store | Per person-day | Shelf life (rotate!) |
|---|---|---|
| **Water** | 4 litres to live (drinking, cooking, minimal hygiene); more for medicine | Indefinite if sealed and treated; rotate tanks |
| **Food** | ~2,000 kcal | Canned 2–5 years; freeze-dried and rice/beans in mylar 10–25 years |
| **Fuel** | Generator litres per hour × hours | Diesel 1–2 years untreated; longer with stabiliser and rotation |
| **Medical** | By tier (below) | Drugs: most keep potency well past expiry when stored right; insulin, some antibiotics and adrenaline don't |

**Medical tiers:** 0 nothing · 1 first aid · 2 a GP's room · 3 an ED resus room (airway,
fluids, analgesia, antibiotics) · 4 + damage-control OR, blood alternatives, ventilators, oxygen
generation · 5 a small hospital that can run for months.

**Rotation:** stores cost money to keep. At each **Turn**, a **Management** roll per bunker:
failure means a store degrades (−10–30% of one category, the DM picks), a fumble means a
system fails unnoticed (the water's gone bad, the filters are mouldy, the batteries are dead).

## 4. Condition

Each bunker has a **Condition** (1–20). Systems decay at 1 point per year unmaintained (more
in a damp one). When the end comes, roll **Condition** for each system as it's switched on.
Old bunkers found in the 2000s may start at 4–8.

## 5. Exposure (the secret)

A single **Exposure clock** per bunker (and one for the whole project) measures how close the
secret is to coming out. It fills with:
- spoil trucks at night, a contractor's loose talk, a strange line in the accounts, a permit
  that doesn't match the building, a neighbour's cracked wall;
- people told (every person who knows adds risk; some are worth it);
- curiosity: a journalist, an SII auditor, a rival, a cop, an ex-wife.

It empties with care: cover stories, compartmentalisation, loyalty, money, time.

When an Exposure clock fills, **someone finds out**. Who, and what they do, is the DM's call
from the state of the world: blackmail, a story, a raid, an offer to join, a theft.

## 6. Who comes in

The question every prepper avoids: **when the door closes, who is inside?** Capacity is finite.
The founder (and later the heir) will have to keep a list, and lists make enemies, and lists
are moral choices. The DM never decides the list.
