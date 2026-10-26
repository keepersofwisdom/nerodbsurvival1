# CORE RULES — "HORA DORADA" (d20 roll-under)

Narrative first. **Roll only when the outcome is uncertain and failure would matter.** The DM
rolls every die with `tools/dice.py` (real randomness, logged in `sessions/dice.log`) and shows
the result in one compact line. The engine is the same "blackjack" d20 as the crusader game
(`crusaderp1`), rewritten for a modern doctor, a business and the end of the world.

> *La hora dorada*: the golden hour, trauma medicine's first sixty minutes, when what you do
> decides whether the patient lives.

---

## 1. The roll

Every check compares **1d20** with a **Value** (skill, trait, drive or attribute, usually 1–20)
adjusted by modifiers. This is the **Effective Value (EV)**.

| Die | Outcome |
|---|---|
| **= EV** | **Critical success.** The best possible result, and something extra happens |
| **< EV** | **Success.** Higher rolls are better successes (this matters in opposed rolls) |
| **> EV** | **Failure** |
| **natural 20** (EV < 20) | **Fumble.** A failure with a cost: a complication, an injury, a word said that can't be unsaid |

- **EV above 20:** add the excess to the die (EV 23 → roll + 3). A total **≥ 20 is a critical**,
  and no fumble is possible.
- **EV 0 or less:** only a **natural 1** succeeds, and never critically.
- **Margin** = EV − roll on a success. Some systems use it (injury, business, persuasion).

```
python3 tools/dice.py check 14            # plain check vs 14
python3 tools/dice.py check 14 -3 Airway  # with a modifier and a label
```

## 2. Opposed rolls

Both sides roll. **Critical > success > failure > fumble.** If both succeed, **the higher roll
wins**, narrowly. Equal rolls are a stalemate. If both fail, neither gets what they want and the
situation shifts.

```
python3 tools/dice.py opposed 13 15 --labels "Negotiation" "Isapre manager" --mods 2 0
```

## 3. Modifiers

| Situation | Mod |
|---|---|
| Routine for someone of this training | **don't roll** |
| Easy / strongly favourable | **+5** |
| Favourable (good team, good light, time to prepare) | **+2 to +3** |
| Hard (back of a moving ambulance, darkness, smoke, hostile crowd) | **−5** |
| Desperate / nearly impossible | **−10** |
| Inspired by a Drive (§7) | **+5** (critical: **+10**) |
| Hurt / Injured (§9) | **−2 / −5** |
| Fatigue (per level above Tired, §9.2) | **−1** |
| Stress at 12+ (§8) | **−2** on fine work and social rolls |
| Language: conversational / broken | **−2 / −5** (social rolls) |
| The NPC's **Regard** for you (−5…+5) | **± Regard** (social rolls) |
| Equipment: improvised / standard / excellent | **−3 / 0 / +2** |
| Each extra opponent beyond the first | **−2** |

## 4. When to roll, when not

- **Don't roll** for what a professional does routinely: an EM specialist intubating a calm
  patient in a resus room, a driver driving, a manager reading a balance sheet. **The player
  chooses; dice decide whether hands, bodies and the world obey.**
- **The player's medicine is the character's medicine** (see `medicine.md §2`). If the player
  orders the right thing, it happens. The dice judge execution under pressure, biology and
  luck, not whether the player knows the answer.
- **The player's moral choices are never rolled.** Trials of character (§6.1) are rare and
  reserved for extreme moments.
- **Hidden rolls:** the DM rolls secretly for perception, lies, ambushes, a patient's hidden
  problem, an inspector's mood, and reports only what the character notices.
- **One roll per stake.** Don't reroll the same attempt unless circumstances change.

---

## 5. Attributes (3–18)

| Attribute | Covers | Notes |
|---|---|---|
| **Body** | Strength, endurance, health, resisting illness, carrying a patient down four flights | Recovery from wounds and illness; sleep deprivation |
| **Hands** | Dexterity, fine motor control, reflexes, steadiness | The procedural attribute. Tremor from fatigue, fear or drink lowers it for the scene |
| **Nerve** | Composure, courage, focus when everything is screaming | Resisting panic, freezing, shock. Also used vs Stress |
| **Presence** | Charisma, authority, looks, voice | First impressions, commanding a room, seduction |
| **Wits** | Perception, memory, reasoning, learning | Noticing, recalling, puzzles, learning skills and languages |

Attribute checks use the attribute as the Value (Body 13 vs the night's third ascent of stairs).
An attribute can be checked directly when no skill fits.

---

## 6. Traits (12 opposed pairs; each pair sums to 20)

Traits are temperament. They don't decide what the character does, but they colour how the DM
narrates the pull, and they let the world know who the character is.

| Left | Right | The question it asks |
|---|---|---|
| **Calm** | **Volatile** | Does he keep the lid on? |
| **Compassionate** | **Detached** | Does he feel the patient, or the case? (Detachment protects as much as it harms) |
| **Honest** | **Deceitful** | Does he tell the truth when it costs? |
| **Generous** | **Greedy** | Is the money a tool or the point? |
| **Cautious** | **Reckless** | Does he wait for the scan, or open the chest? |
| **Trusting** | **Paranoid** | Does he believe people, or prepare for them? |
| **Disciplined** | **Indulgent** | Sleep, drink, food, pills, sex: does he keep the rules he sets himself? |
| **Humble** | **Proud** | Can he say "I was wrong" in front of the team? |
| **Merciful** | **Ruthless** | When someone is at his mercy, what does he do? |
| **Loyal** | **Self-serving** | Who comes first, the people or himself? |
| **Faithful** | **Lustful** | To a partner, or to appetite? |
| **Idealist** | **Pragmatist** | The world as it should be, or as it is? (Neither is a vice) |

**Values:** 1–5 rare, 6–9 weak, 10 balanced, 11–15 marked, **16+ famous** (people know him for
it), 19–20 consuming.

### 6.1 Trials of character
When a situation **strongly tests** a trait (a gunman in the waiting room, an Isapre offering a
bribe, a colleague's wife in an empty on-call room, the man who killed his friend bleeding on
his table), the DM may call a **trial** on the trait the situation pulls toward:

| Result | Effect |
|---|---|
| **Critical** | The impulse **overwhelms** him. The player narrates how he acts on it. To resist: take **+4 Stress** and act freely |
| **Success** | A **strong pull**. The player chooses freely, but acting **against** it costs **+2 Stress** |
| **Failure** | No special pull. Free choice |
| **Fumble** | The **opposite** impulse surges instead (fear becomes rage, desire becomes disgust) |

Trials are rare: a few per session at most, at real moments. **Never** use them to take
ordinary choices away from the player.

### 6.2 Trait growth
- When he acts **notably** in line with a trait, the DM marks a **✓** beside it in the sheet.
- At **the Turn** (`campaign_turn.md`), roll d20 for each ✓ trait. **If the roll is higher than
  its current value, it rises by 1** (its opposite falls by 1). Clear the checks.
- **Dramatic acts** (lying to a family about how their son died, leaving a patient to save the
  bunker's secret, shooting a man) may shift a trait by 1–2 immediately, at the DM's call, with
  a note in the decision log.

### 6.3 Reputations (sum of five traits ≥ 80)
| Reputation | Traits summed | Benefit while it holds |
|---|---|---|
| **El Doctor** (the good doctor) | Compassionate, Honest, Calm, Generous, Humble | +3 with patients, families, nurses and the barrio; staff loyalty rolls +2 |
| **El Patrón** (the boss) | Proud, Ruthless, Pragmatist, Calm, Disciplined | +3 Leadership and Negotiation with businessmen and politicians; staff obey, and fear |
| **El Paranoico** (the prepper) | Paranoid, Cautious, Disciplined, Pragmatist, Detached | +2 Awareness and Logistics; once per arc, he *already prepared* for the thing that happens (the DM confirms what's plausible). People think he's odd |
| **El Santo** (the saint) | Idealist, Merciful, Compassionate, Generous, Loyal | Followers. In a crisis, people come to him and do what he asks; enemies find him hard to attack in public |

A reputation can be lost as traits change, and NPCs notice the change.

---

## 7. Drives (1–20+)

Drives are what he'd lose everything for. Typical: **Duty (patients)**, **Love (family)**,
**Preparation** (the conviction that the end is coming), **Ambition (the Network)**, **Faith**,
plus personal ones: **Love (a person)**, **Hate (someone)**, **Fear (something)**, **Guilt (a
death)**, **Vengeance (for someone)**, **Loyalty (a person or a group)**.

**Invoking a drive:** when he acts directly for it, roll it:

| Result | Effect |
|---|---|
| **Critical** | **Inspired: +10** to one skill for the scene. No panic, fatigue or trial can touch him for the scene |
| **Success** | **Inspired: +5** to one skill for the scene |
| **Failure** | No bonus. The drive falters: **−1** (doubt) |
| **Fumble** | **Breaking:** +3 Stress and a Breaking Point (§8.2). The drive −1 |

- **Growth:** a drive rises by 1 when he sacrifices for it, and falls by 1–3 when he betrays it or
  it betrays him.
- **20+:** obsession. He cannot knowingly act against it without a crisis (+4 Stress).
- **0:** gone. Note what killed it.

---

## 8. Skills (0–20)

| Group | Skills |
|---|---|
| **Clinical** | **Resuscitation** (airway, shock, codes, crash induction) · **Procedures** (lines, drains, surgical airway, thoracotomy, splints, sutures, reductions, blocks) · **Diagnosis** (history, exam, reasoning, labs, ECG, imaging, POCUS) · **Critical Care** (ventilators, drips, ICU management, transport of the critical) · **Surgery** (damage-control surgery: an EM doctor's ceiling is low unless trained) · **Special Patients** (children, pregnancy, the very old) · **Prehospital** (scene work, extrication, ambulance medicine) · **Disaster** (triage, mass-casualty command, field hospitals, CBRN) |
| **Command & money** | **Leadership** (a team in a code, a staff, a crisis) · **Management** (budgets, staff, logistics, supply) · **Negotiation** (contracts, Isapres, investors, unions) · **Bureaucracy** (permits, SEREMI inspections, Superintendencia, courts, lawyers) |
| **People** | **Persuasion** · **Deception** · **Empathy** (reading people, breaking bad news, calming a family) · **Intimidation** · **Seduction** · **Streetwise** (barrios, crime, black market, who to pay) · **Investigation** (archives, records, property titles, following a trail) |
| **Practical** | **Driving** · **Engineering** (construction, generators, HVAC, water, power, the bunker's guts) · **Radio & Electronics** · **Firearms** · **Fighting** (unarmed, knife, restraint) · **Athletics** · **Stealth** · **Outdoors** (the cordillera, survival, foraging) · **Awareness** (noticing, situational sense) |
| **Learning** | **Languages** (English, French, Portuguese, Mapudungun…) · **Science** (chemistry, radiation, epidemiology) · **History & Politics** (who's who in Chile, what the old men did) |

**Untrained:** a skill at 0 may be attempted at an attribute/4 EV (rounded down), at the DM's
discretion, or not at all (Surgery, Engineering, Languages).

### 8.1 Skill growth
- **Checks:** a critical, or a success that mattered under real pressure, earns a ✓.
- **The Turn:** for each ✓ skill, roll d20. **Higher than the current value → +1.**
- **Training** (a course, a fellowship, months of practice with a teacher): +1d3 (max 15 without
  real mastery; above 15 only through checks). ATLS, a disaster course, a firearms course, a
  year in a busy trauma centre abroad.
- **Learning by necessity:** a skill used constantly for a period earns an automatic ✓.

### 8.2 Professional benchmarks (to calibrate sheets)
| Value | Clinical meaning |
|---|---|
| 5–8 | Medical student / intern (*interno*) |
| 9–11 | General practitioner, a few years in an ED (*médico de urgencia* without specialty) |
| 12–14 | EM resident (*becado*), senior GP with ten years of night shifts |
| 15–16 | Newly certified EM specialist |
| 17–18 | Experienced specialist; the person others call |
| 19–20 | National reference; teaches the course |

---

## 9. Stress, Conscience, Health

### 9.1 Stress (0–20)
Stress is the weight: dead children, a lawsuit, debt, secrets, no sleep, fear.
| Source | Stress |
|---|---|
| A bad death on his watch; a code lost on a young patient | +1 to +3 |
| Mass-casualty event, being shot at, a colleague dead | +2 to +5 |
| A hard secret kept from a loved one (per arc) | +1 |
| Acting against a trial or drive | +2 / +4 |
| Financial crisis, lawsuit, inspection threatening closure | +1 to +3 |

**Recovery:** sleep and days off (−1 per real rest day, max −3 a week), a holiday (−3 to −6),
family, love, sex, friendship, exercise, faith, therapy (−1 to −3 per scene that truly helps),
drink and pills (−2 now, and the DM notes the debt).

| Stress | Effect |
|---|---|
| 0–5 | Steady |
| 6–11 | Frayed. Short temper, bad sleep; the DM describes it |
| 12–15 | **Strained:** −2 on fine work and social rolls; Nerve check at the start of each crisis or freeze for a beat |
| 16–19 | **Breaking:** as above, and a **Breaking Point** each time Stress rises |
| 20 | **Broken:** a collapse (the DM and player decide what): hospitalisation, a breakdown on shift, a disappearance, a relapse, an affair blown open. Then Stress resets to 12 and he gains a **Scar** |

### 9.2 Breaking Points (d20, or chosen to fit)
| d20 | Breaking point |
|---|---|
| 1–3 | **Freeze:** loses the next beat of the scene |
| 4–6 | **Rage:** shouts at, or strikes, whoever is nearest |
| 7–9 | **Flight:** leaves the room, the shift, the city |
| 10–12 | **Numb:** feels nothing; Detached +1 |
| 13–14 | **Drink / pills:** self-medicates tonight (Disciplined trial to stop at one) |
| 15–16 | **Insomnia:** no real sleep for 1d6 nights (fatigue) |
| 17–18 | **Reckless:** takes a risk he'd never take (Cautious −1) |
| 19 | **Confession:** tells someone something he shouldn't |
| 20 | **Clarity:** the fog lifts. −2 Stress, and he sees something everyone else missed |

### 9.3 Fatigue
| Level | Meaning | Mod |
|---|---|---|
| 0 Rested | Slept | — |
| 1 Tired | 18 h awake, or the end of a normal shift | — |
| 2 Weary | 24 h awake (the end of a *turno de 24*) | −1 |
| 3 Exhausted | 30+ h awake, or three bad nights | −2, Hands −2 |
| 4 Spent | 40+ h, or carrying people for hours | −3, Hands −4; Body check each hour or collapse |

### 9.4 Conscience
A track for what he has done, not felt: **Clear → Uneasy → Burdened → Haunted → Broken.**
It moves one step down when he does something he believes is wrong and can't undo (a lie that
kills, a patient abandoned for money or secrecy, violence beyond need). It moves up through
confession, restitution, real sacrifice, or time and a reason. At **Haunted**, Stress recovers at
half speed. At **Broken**, he becomes a different man, and the player and DM decide who.

### 9.5 Wounds and illness (the character's own body)
| State | Mod | Meaning |
|---|---|---|
| **Hurt** | −2 | Lacerations, sprains, cracked rib, flu |
| **Injured** | −5 | Needs treatment; can't work a shift properly |
| **Critical** | out | Needs resuscitation and surgery; use `medicine.md` with him as the patient |
| **Dying** | out | Clock running |

Injuries are rolled with `tools/dice.py injury` (see `medicine.md §6`). Long-term conditions
(back, hypertension, alcohol, a needlestick hepatitis) are written in the sheet.

### 9.6 Scars
A Scar is a permanent mark of a Breaking or a terrible event: *nightmares of 27F*, *can't enter a
paediatric box*, *flinches at fireworks*, *a missing finger*. Each Scar is a short phrase the DM
uses in narration, and some give −2 in their trigger situation. Scars may also give strength:
*nothing surprises him after the Posta*, +2 Nerve in mass casualties.

---

## 10. Standing, Regard and Money

### 10.1 Standing (−5…+5 per circle)
How each circle of Santiago sees him. It modifies social rolls with that circle, and opens or
closes doors.
| Circle | Who |
|---|---|
| **Medicine** | Colegio Médico, the SOCHIMU, chiefs of service, the universities |
| **Business** | Isapres, clinics, banks, investors, suppliers |
| **State** | MINSAL, SEREMI, Fonasa, the Superintendencia, the municipalities, ministers |
| **Street** | The barrios and poblaciones, the narcos, the barras, the people his ambulances reach |
| **Uniforms** | Carabineros, PDI, the Army, Bomberos |
| **The Old Men** | The circle of old money and old power (see the arc files for what he knows) |
| **Press** | Reporters, TV, later social networks |

### 10.2 Regard (−5…+5 per NPC)
Each major NPC's feeling toward him. It modifies social rolls with that NPC, and changes
through play (saved lives, broken promises, favours, insults, love).

### 10.3 Money
- Personal money in **CLP** (pesos) and savings in **UF** (Unidad de Fomento, the indexed unit
  in which Chileans price houses, rents, debts and contracts). The company's books are in UF.
- Convert with `python3 tools/dice.py money 5000 UF 2005 --to 2025`.
- Rough personal costs, salaries and company economics are in `enterprise.md`. Prices of daily
  life are in `research/08_daily_life_and_flavour.md`.

---

## 11. Progress clocks

Long projects, threats and tensions use **clocks** of 4, 6 or 8 segments, drawn in the state file
as `[■■□□□□]`. A clock fills by events, failed rolls, or the passage of time; it empties by
success. Examples: *Building Bunker 1* (8), *SEREMI inspection* (4), *The journalist's story* (6),
*Cash runs out* (6), *The patient's deterioration* (see `medicine.md`), *Exposure* (the secret's
discovery, see `preparedness.md`).
