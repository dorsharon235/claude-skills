---
name: perfect
description: Dor's "do it perfectly" command. Looks at EVERYTHING installed on this machine (own skills, project skills, plugins, account skills), interviews the user in rounds of questions until the brief is complete (as many rounds as it takes), shows the brief and the chosen skills for approval, and only then does the task with the right skill or chain of skills and checks the result against the brief. Use whenever the user types /perfect, or says "תעשה את זה מושלם", "תבחר את הסקיל הנכון", "תשאל אותי עד שתבין", "תראיין אותי ואז תעשה", "מה הסקיל הכי טוב בשביל...", or asks for a video, site, deck, document, game, image or any bigger piece of work and wants the best installed tool chosen for it, even when no skill is named.
---

# perfect — interview first, pick the right skill, then do it perfectly

The user has hundreds of skills installed and does not want to remember which one fits. He wants one command that:
1. knows everything that is installed,
2. asks as many questions as it takes to fully understand the task,
3. only then picks the best skill (or chain) and does the work properly.

The biggest waste is starting too early: a video built on a guess gets thrown away. So the interview is the core of this skill, not a formality. But a bad interview is also a waste: questions whose answer could be found alone, or questions that do not change the result. Every question has to earn its place.

**Language:** talk to Dor in plain Hebrew, short sentences, few English terms (his global rule). Skill names, commands and paths stay as they are.

## Step 1 — Know what is installed (silently, ~1 minute)

Build the live inventory every run (it changes weekly):

```bash
P="<work folder>/perfect"; mkdir -p "$P"; PYTHONIOENCODING=utf-8 python -I ~/.claude/skills/improve-project/scripts/inventory.py --paths --project "$PWD" > "$P/inventory.md"; head -1 "$P/inventory.md"
```

`<work folder>` = the session's scratchpad directory if the system prompt gives one, else `${TMPDIR:-/tmp}`. Call this folder **P**; `brief.md` lives there too. The last column is each skill's folder, so you can read its SKILL.md directly.

If the script is missing, fall back to the skills list in your own system prompt plus `ls ~/.claude/skills`. Either way, also trust the skills list in your system prompt: what you can actually invoke wins over the table.

**Skills are not the only tools.** Also count as candidates (the table does not list them):
- Artifact types (`Artifact` action `quickstart` / list `scope: "types"`): ready-made deck, document, dashboard and design pages. For a deck or document that is not asked as a file, these are often the best choice.
- Connected services (MCP tools in your tool list or deferred list): Gamma (decks, pages), Canva, Figma, Lovable (apps), Google Drive/Sheets/Calendar, Gmail, HeyGen-style video tools, etc. Use `ToolSearch` to check one is really there.

Do not dump the inventory on the user. Grep it by need.

## Step 2 — Understand the request and draw up the candidates

1. Say in one line what kind of task this is (video / site or page / deck / document / game / image or design / sound / data / code fix / other).
2. Search the inventory for EVERY skill that might fit, by description, not only by name (grep several words, in English: e.g. for a video: `video|film|reel|motion|animation|hyperframes|remotion|caption|sound`).
3. Shortlist 2–6 candidates. **Read the full SKILL.md of each finalist** (and its main reference if the SKILL.md points to one for inputs). This is the trick of this skill: each skill says what it needs (a script, a voice, a logo, a length, a format, source files). Those needs become interview questions. Write them down.
4. Look around before asking: the current folder, files the user mentioned, the project's README/HANDOFF, memory. Anything you can find out alone you do not ask. If the task belongs to a known project in memory, read that memory first. If a project in memory looks *close but not the same* as the request (e.g. he asks about guards' shifts and there is a technicians-routing demo), do not assume: make it the first interview question ("זה על הפרויקט X, או משהו חדש?"), with what you found in one line.
5. Note every question or approval the finalists themselves will ask when run (a style choice, an "OK to install/update", a paid-credit confirmation). Pull those into the interview now, so the work later runs without stopping.

`references/question-bank.md` lists what usually needs knowing per task type. Use it as a checklist, not a script: the finalists' own needs come first.

## Step 3 — The interview (as many rounds as needed)

Keep a running brief in `P/brief.md` (sections: goal, audience, where it is used, content, look and feel, length/size/format, materials the user has, must-haves, must-nots, deadline/budget, open points). After each round update it.

How to ask:
- Use the `AskUserQuestion` tool: up to 4 questions per round, each with 2–4 concrete options, your recommended option first and marked "(מומלץ)". Options make answering fast. The user can always type "Other". Use `preview` to show a small mock-up or example when choosing between looks/structures. If the tool is deferred, load it with `ToolSearch` ("select:AskUserQuestion"). If it is not available at all, write the round as a numbered list in your message, each question with lettered options (א/ב/ג, recommended first), end the turn, and wait — the user answers like "1א 2ג 3: ...".
- Facts and numbers: never invent figures the user will show to others (market size, revenue, customers, prices). Ask whether he has them, or offer to research them (say if research uses paid credits); mark anything unconfirmed as "להשלמה" in the result.
- Open questions that options cannot cover (the story, a name, a text the user must write) go in plain text, a few at a time.
- Order: big decisions first (goal, audience, where it is shown), then content, then look, then details. An early answer can make later questions irrelevant: drop them.
- Each question in plain Hebrew, standing on its own (the user may see only the dialog).
- Never ask something you could find out, something a sensible default covers without affecting quality, or two things in one question.
- When the user says "תחליט אתה" on a point: decide, write the decision in the brief as "החלטתי: ...", move on.
- When he asks for materials (photos, logo, recording), say exactly what, in what format, and where to put it.

There is no round limit. Stop only when every item that changes the result is either answered, found, or decided by you with a reason. A good self-check: "If I start now, is there anything I would have to guess that the user would likely reject?" If yes, ask another round.

## Step 4 — The brief and plan for approval

Show a short summary, in Hebrew:
- **מה הבנתי** — the brief in 5–10 lines.
- **הסקילים שאשתמש בהם** — in order, each with one line why it beats the other candidates (e.g. "`cinematic-film` ולא `hyperframes`, כי ביקשת סרט עם קריין על תמונות ארכיון"). If a chain: what each one does.
- **מה אני מחליט לבד** — the defaults you took.
- **מה עוד חסר** — if anything; usually nothing.
- If something costs money or credits (paid APIs, avatar video, image generation), say what and roughly how much before running.

Then wait for a clear OK (a button "יאללה, תתחיל" / "יש תיקון"). Corrections → update brief → show again only what changed.

If no installed skill fits well, say so honestly, do the task with general tools, and mention in one line which kind of skill would help (the weekly `skill-scout` can look for it). Do not install anything without asking.

## Step 5 — Do it

1. Invoke each chosen skill with the `Skill` tool, in order, and follow its instructions fully. Its rules win over your habits. Pass it the brief: everything the skill would normally ask is already answered (that is why step 2.5 pulled its questions into the interview), so give it those answers instead of asking again. Ask the user only if the skill hits something truly new, or needs a fresh approval by its own rules (payment, publishing, sending) — those approvals are never skipped.
2. Keep the brief open while working; every decision is checked against it.
3. Big work: show an early checkpoint (a frame, a draft, a structure) before the full build, so a mistake costs minutes, not hours.

## Step 6 — Check before handing over

- Go over the brief line by line: is each item in the result? Write ✓ / ✗ for yourself.
- Look at the real output (render the video and look at frames, open the page in the browser, open the document), not just "the command ended". Fix what is wrong.
- Hand over in Hebrew: what was made, where it is (full path or link), which skills were used, what you decided alone, and what was not checked. Send files with `SendUserFile` when there is a file.

## Example (short)

User: "/perfect תעשה סרטון לאינסטגרם על הקבוצה שלי"
- Step 1–2: a video. Candidates: `hyperframes`, `cinematic-film`, `edit-reel`, `video-shotcraft`, `add-sound`, `brag`. Read them. Found the "Unicorn catchball" memory with source reels and the dark-beats music preference.
- Round 1: what kind (מומלץ: טריילר עונה מקטעים קיימים / סרט עם קריין / הסבר מונפש), length (מומלץ: 30 שניות), vertical 9:16 (מומלץ), with captions?
- Round 2: which clips, music style (offer dark beats first, from memory), text on screen, ending (logo / call to action).
- Round 3: names to show, colours, date of the event...
- Brief + plan: `edit-reel` to cut, then `add-sound` for music, because the material is real footage, not a story with a narrator. OK → do → check frames → hand over.
