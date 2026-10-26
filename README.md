# SUBSUELO — Santiago, 2005 →

An immersive, long-form, realistic roleplay for **Claude Code**, set in **Santiago de Chile**
in our world with one secret difference: beneath the city centre, old men with money built
doomsday bunkers near the tunnels around La Moneda.

- **Era I — Los Cimientos (2005 → ~2025).** You play an emergency physician and prepper who
  builds and runs a private network of small **stabilization units** and ambulances across
  Santiago: get the patient, stabilize, transfer. It's a management game first: partners,
  banks, permits, staff, rivals, money. Beneath it, funded by frightened old men, he prepares
  for nuclear war. Ordinary life for years: love, children, the city's real disasters.
- **Era II — La Herencia (~2025 →).** You play a young emergency physician who discovers the
  Network's depths and keeps it going.
- **Era III — El Fin.** The end of the world, when it comes.

Claude is the Dungeon Master. It runs the world, voices everyone, rolls real dice, keeps the
history, the money and the medicine accurate, and remembers everything between sessions.

> Graphic medicine and violence, explicit adult content, drugs and despair are enabled (see
> `config.md` for the settings and the two hard lines).

## How to play

1. Open a Claude Code session in this repository. `CLAUDE.md` loads automatically and makes
   Claude the DM.
2. The setup decisions are recorded in `config.md`; the founder is in `characters/player.md`.
3. Say **`begin`** and the first scene opens in Santiago, March 2005.
4. Play by writing what your character says and does. At decision points you'll get options
   (A–D), but you can always do something else.
5. Say **`save`** when you stop. Everything is written to files, committed and pushed. Next
   time, say **`resume`**.

**Commands:** `begin` · `resume` · `save` · `status` · `sheet` · `network` · `recap` ·
`autopilot` · `slow down` · `fast forward [time]` · `shift` · `fade` · `more/less detail` ·
`more/less medicine` · `hide dice` · `new arc` · `(( out of character ))`

## What's in here

| Folder | Contents |
|---|---|
| `research/` | The compendium: Santiago's history and the dictatorship, Chile 2005–2026, underground Santiago, the health system and the Ley de Urgencia, emergency medicine and disaster medicine in Chile, hospitals and neighbourhoods, infrastructure and catastrophe science, daily life and slang |
| `mechanics/` | The rules (d20 roll-under), medicine (patients, beats, outcomes), the enterprise, preparedness and bunkers, the Turn, character creation |
| `world/` | State, lore, timeline, places, the company sheet, the bunkers as known |
| `characters/` | Player sheet, NPC roster (and secrets — don't read those) |
| `dm/` | **Spoilers.** The Dungeon Master's bibles. Don't read |
| `arcs/` | What your character has learned, arc by arc |
| `sessions/` | Session logs and the dice log |
| `tools/dice.py` | Dice, checks, injuries, money by year (CLP/UF/USD), dates and holidays |

The architecture is adapted from the *Claude Code Immersive Roleplay System* and from
`crusaderp1` (OUTREMER).
