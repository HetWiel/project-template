# Working on this project

This repository is a work on hetwiel.dev: an experiment in how fast an idea can turn into
something that works. You (the machine) build. The maker steers, and learns what you built.
That second half is **The Apprentice**, and it is not optional.

- Talk to the maker in Dutch. Code, comments, commits and docs are in English.
- Read `README.md` for what this project is and how it goes live.
- Never put secrets (tokens, keys, passwords) in the repository.

## The Apprentice

Every work keeps a ledger of the materials (techniques, tools, concepts) it was built with,
and how well the maker understands each one:

| file | what |
|---|---|
| `apprentice.yml` | the ledger: one entry per material, with its level. hetwiel.dev/apprentice/ is built from it, so it is public. |
| `APPRENTICE.md` | one card per material: what it is, where it lives, why this way, questions, a by-hand task. Plus the teach-back log. |
| `.claude/skills/apprentice/SKILL.md` | how to run the loop. Load it with the Skill tool. |

Levels, low to high: `seen` → `understood` → `by-hand` → `taught`.

### The rules

1. **Every session that changes code ends with the loop.** Before the last commit, load the
   `apprentice` skill and follow *After building*: new materials get an entry and a card.
2. **New materials get a teach-back before they go live.** Don't push to `main` until the maker has
   explained the new material back to you, or has explicitly said to postpone it. A postponement is
   written in the teach-back log, so it stays visible.
3. **Levels are earned, never given.** Only raise a level after the maker passed the teach-back or did
   the by-hand task himself. Judge strictly: a half answer stays at the current level. The ledger is
   public; it has to be true.
4. **Leave some work for the hand.** When a small, well-defined change comes up that fits a material
   at `understood`, offer it as a by-hand task instead of doing it: hints and pointers, no code.
5. When the maker says *teach-back*, *apprentice* or `/apprentice`, run a teach-back session
   (see the skill).

## The brake and the clock

A session in a repo whose `apprentice.yml` still has the template's placeholders (`work: My project`,
`opened: 2026-01-01`) is the start of a **new work**. Before building anything:

6. **Check the brake.** The understanding debt is the number of materials at `seen` across all works;
   hetwiel.dev/apprentice/ shows it and whether the brake is on (the rule itself is in the hetwiel
   repo: `brake_threshold` in `site/content/site.yml`). While the brake is on, don't build the new work.
   Tell the maker the debt and the threshold, and offer a teach-back in an existing work instead.
7. **Start the clock.** With the brake off, add an entry to `site/content/clock.yml` in the **hetwiel**
   repo (RQ1: idea to online): `work` (its name as it will appear on the front page), `idea` (the time
   of the maker's request, with the time zone, e.g. `2026-11-02T20:15:00+01:00`), `source: recorded`,
   and commit it right away. If this session can't reach the hetwiel repo, tell the maker the exact
   time and ask him to add the repo to the session, so the moment isn't lost. When the work becomes
   reachable for visitors, set `online` to the hetwiel commit that made it so (usually the one that
   adds its block to the Caddyfile).

