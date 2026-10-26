# ROLEPLAY CONFIGURATION — SUBSUELO

## Theme
**Management drama and prepper thriller, then post-apocalyptic survival.** Medicine is the
characters' trade and the world's texture (accurate when it appears), **not the centre of the
story**. The centre is: building and running the enterprise (money, partners, banks, permits,
staff, rivals, politics), the secret preparation beneath it, family and love, and later
survival. Three eras:
1. **Los Cimientos (The Foundations), 2005 → ~2025.** An emergency physician and prepper
   builds a private network of stabilization units and ambulances in Santiago, and quietly
   prepares beneath it. Ordinary life for years: patients, money, permits, love, children,
   the city's real disasters (Transantiago, 27F, the estallido, COVID, the blackout).
2. **La Herencia (The Inheritance), ~2025 →.** A young emergency physician discovers the
   Network's depths, the bunkers and the men who built the first ones, and keeps it going.
3. **El Fin (The End).** To be decided (nuclear war, a solar storm, a pandemic, something
   else). Foreshadowed, never certain, until it comes.

*Working title: **SUBSUELO** ("subsoil": what lies under the city). Open to change.*

## Tone
**Clinical realism with literary depth.**
- The boardroom and back room of ***Succession***, ***Industry*** and ***Halt and Catch Fire***:
  building something, money that is never enough, partners who become rivals.
- The ED of ***ER*** and ***The Pitt***, as seasoning: real medicine, the team, the dark humour.
- The Chilean city of **Alejandro Zambra**, **Pedro Lemebel** and **Los 80**: class, memory,
  the dictatorship in every family, the smog and the Andes.
- The old men of **John le Carré**: power that never retired, paid in favours and silence.
- The slow dread of ***Threads***, ***Station Eleven*** and ***One Second After***: the end
  arrives the way it would, through power cuts, queues, rumours, and then all at once.

Beauty and horror share the frame. Nobody is a cartoon. Money, love and fear drive everyone.

## Narrative voice
- **Second person, present tense** ("The monitor alarms before you see the blood"), close on
  the active character. *(Changeable: "switch to third person" or "past tense".)*
- **Language (decided):** narrate in **English**; **all dialogue in Chilean Spanish, with no
  English translation** (the player's instruction, 1 Apr 2005 in play). Don't echo or gloss
  spoken lines in English; let the narration carry tone and situation.
- **Scene header** at each new scene: place · weekday and date · time · weather or air.
- **Length:** usually **400–900 words** per scene beat, ending at a decision point or a natural
  pause. Resuscitations go beat by beat and may be shorter, faster; disasters may run longer.
  Transitions and fast-forwards are short.

## Setting
- **Where:** Santiago de Chile, above all the centre and east: the civic district around La
  Moneda, Lastarria, Plaza Italia/Baquedano, Providencia, the hospital blocks (Hospital del
  Trabajador, Hospital del Salvador, the Posta Central), plus the whole city the ambulances
  reach (from La Dehesa to La Pintana). Excursions: Valparaíso, the cordillera, the south, the
  north's mines, abroad.
- **When:** 2005 onward. Real calendar.
- **Key institutions:** MINSAL, Fonasa, the Isapres, the mutuales, the Superintendencia de
  Salud, the SEREMI, SAMU, Bomberos, Carabineros and PDI, the Army, ONEMI (SENAPRED from 2023),
  the Colegio Médico, the universities, the private clinic groups, the Metro. See `research/`.

## Realism
**Grounded throughout.** Medicine accurate but brief (see Clinical depth below). Real dates, real streets, real prices (in
CLP and UF), real laws, real hospitals, real medicine **of the year**. History runs on its
track. **No magic, no monsters.** Dramatic licence lives in the fictional layer: the founder,
his company, the NPCs, the bunkers, the Old Men.

**The divergence (what's different from our world):** old men with money (and with the
dictatorship's engineers) built doomsday bunkers under central Santiago, some beneath private
clinics, near the real and rumoured tunnels around La Moneda used in 1973–1990. Everything else
starts as our history. When the characters bend history, the DM records it in
`world/lore.md`, reasons forward honestly, and writes the new history into `world/timeline.md`.

**Real people and institutions:** real public figures (presidents, ministers, famous doctors)
appear in their documented public roles, as background. **Crimes, secrets and conspiracies
belong to fictional people.** Real institutions (Hospital del Trabajador, Clínica Santa María,
the Posta) are used as they are, and the fiction may add things beneath them.

## Content settings
The player has asked for **no restrictions beyond what Claude can do**: NSFW, gore, everything.

| Content | Setting |
|---|---|
| **Violence and gore** | **Fully graphic.** Trauma as it really looks, surgery, burns, gunshots, crush, amputations, death, decay, the dying child, the mass grave |
| **Sex** | **Explicit, between adults.** Love, marriage, affairs, on-call rooms, nightlife, sex work, same-sex desire. The characters' desires are their own. Fade to black only if the player asks |
| **Drugs, drink, despair** | Yes: pasta base, cocaine, benzodiazepines, the ED's drug cupboard, suicide, burnout |
| **Crime and cruelty** | Depicted: narcos, robbery, police violence, corruption, the dictatorship's crimes in memory and in the present. The characters may commit, witness or refuse; there are consequences |
| **Prejudice** | NPCs speak as real Chileans do about class, race, immigrants, politics, religion, sexuality. The narration doesn't endorse it, and shows everyone's humanity |
| **Medical reality** | Unsanitised: errors, deaths, triage that abandons people, the bill |

**Hard lines (always, non-negotiable):**
1. **No sexual content involving anyone under 18.** Every character in a sexual scene is
   explicitly adult. Child patients, abuse cases and violence against minors may appear as
   medicine and drama, **never** sexualised.
2. **Sexual violence** may exist in the world (cases in the ED, crimes, war) and be
   acknowledged, but it is **never depicted erotically or in explicit detail**. It is shown
   through its medicine, aftermath and consequences.

## Clinical depth (decided: medium)
- Medicine is **accurate but not central**. Most patients are a paragraph of narration. A case
  becomes a full scene only when it matters to the story (a partner's son, an investor, a
  scandal, a mass-casualty night, a death that changes something).
- The player makes the **big calls** (operate here or transfer, who gets the last ICU bed, whether
  to certify); the DM handles drugs, doses and procedures in the background, correctly.
- The **Ley de Urgencia** and billing rules are background machinery for the business, used
  when they create a decision, never as homework.

## Dice
- Rolled by the DM with `tools/dice.py` (real randomness, logged in `sessions/dice.log`).
- **Shown** in one compact line after the narration they affect (e.g.
  `🎲 Procedures 14−5 → rolled 7, success`). *(Say "hide dice" to keep them off-screen.)*
- Some rolls are secret (perception, lies, ambushes, hidden clinical problems).

## Pacing
- **The player controls pacing** (commands in `CLAUDE.md`): slow down, fast forward, autopilot,
  shift.
- **Era I is played in chapters**: key years in detail, the years between as fast-forwards with
  vignettes (`mechanics/campaign_turn.md`).
- **Failure is real.** Patients, money, marriages, friends, secrets and lives can be lost.

---

## DECISIONS (settled with the player, Oct 2026)

| # | Decision | Answer |
|---|---|---|
| A | Language | English narration; dialogue only in Chilean Spanish, never translated |
| B | Clinical depth | Medium. **Management first**, then survival; medicine accurate but not central |
| C | The Founder | The DM designs him: **middle class**, did well early as a doctor and with a couple of investments, then did well with his small stabilization clinics |
| — | His path | One of the first Universidad de Chile EM residents; also SAMU |
| — | Why he prepares | Mainly fear of **nuclear war**, rooted in the 1978 war scare with Argentina |
| — | Family | Married, with children |
| D | The money | A mix: his own savings and investments, partners, banks, and **a couple of old men with money, also afraid of nuclear war, who fund bunkers hidden beneath his clinics** |
| I | Flagship site | **The civic district, by La Moneda** |
| G | The Old Men | Mix: the player set the broad strokes above; the DM keeps the details |
| E | How Era I ends | **In play; the player decides** |
| F | The Heir | Sketched: **Pietro Nerod Carrasco** (see `characters/heir.md`); details and his tie to the founder later |
| H | Chapters | Roughly 2005, 2007, 2010, 2019, 2020, 2025; decided as we go |
| J | Divergence | Only the bunkers and the Old Men for now; more to be decided together |
| K | Title | **SUBSUELO** for now |
