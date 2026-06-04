# Memory Architecture And Update Rules

Last updated: 2026-05-27

## Goal

Make psychological reflection memory readable, editable, and accumulative over time, rather than a pile of ordinary chat logs.

After each session, material should be saved in layers. When the next automation starts, it should not mechanically read and repeat everything. It should extract the most relevant clues from the long-term archive and form one opening question for the current session.

## Design Principles

This system borrows useful ideas from several open-source knowledge and memory workflows:

- Obsidian as long-term memory: memory should be stored in Markdown files that the user can read and edit directly.
- Memory blocks: long-term memory should be broken into maintainable units rather than placed into one huge file.
- Time-layered memory: preserve single-session notes, monthly summaries, and yearly reports so short-term events can gradually settle into long-term patterns.
- User-profile memory: the focus is not to remember the assistant, but to gradually form a useful profile of the user.
- Progressive assessment: early sessions should understand the user through continuous questions rather than asking everything at once or reaching conclusions too early.

## Layered Memory

### 1. Fact Layer

Record what the user explicitly said:

- what happened;
- who was involved;
- what choice the user made;
- what the user said they wanted;
- what life context the user clearly described.

Do not write speculation as fact.

### 2. Emotion Layer

Record the user's expressed emotions and intensity:

- anxiety, anger, shame, loneliness, helplessness, suppression, numbness, excitement, hope;
- emotional shifts;
- bodily feelings;
- whether the user ends the session clearer or more confused.

### 3. Interpretation Layer

Record psychological understanding formed during the session, but keep it hypothetical:

- "may be related to...";
- "provisionally appears to be...";
- "needs later verification."

Do not turn one session's interpretation into a final conclusion.

### 4. Pattern Layer

Write something into long-term patterns only after it appears repeatedly:

- repeated interpersonal conflicts;
- repeated self-criticism;
- similar avoidance styles;
- stable defense mechanisms;
- long-term core needs or fears.

### 5. Profile Layer

The psychological profile should contain only relatively stable information:

- communication preferences;
- relationship patterns;
- sources of self-worth;
- common defenses;
- deeper needs;
- growth direction.

Whenever the profile is updated, record the reason for the update.

### 6. Question Layer

Each automation start should ask only one question. Question sources, in priority order:

1. the core unfinished theme from the previous session;
2. the hypothesis in the profile most in need of verification;
3. the most important open question in the running case formulation;
4. emotional residue from the latest session note;
5. long-term themes from monthly or yearly reports.

The question should be specific, answerable, and able to open the current session. Do not ask multiple directions at once.

### 7. Continuity Index Layer

`09_Continuity_Index.md` is the fast routing layer. It should remain short and point to source files instead of duplicating them.

Use it to track:

- active themes;
- confirmed stable patterns;
- provisional hypotheses;
- retired or weakened hypotheses;
- latest source files;
- the next opening question.

This layer protects the user experience by reducing startup time in a long-running vault.

### 8. Risk Layer

If self-harm, suicidal intent, intent to harm others, severe loss of control, or real-world safety problems appear, stop ordinary psychological analysis and prioritize safety.

## Update Rules

- Save a single-session note after every session.
- The running case formulation may be updated after every session, but it must distinguish hypotheses from relatively stable patterns.
- The psychological profile should be updated only when information is stable or repeated.
- The continuity index should be updated after each completed session so the next session can start quickly.
- Monthly reports compress several sessions into monthly themes.
- Yearly reports summarize long-term changes.
- Do not label the user's personality based on one intense emotion.
- Do not write the assistant's interpretation as a user fact.

## Opening Question Generation Rules

When an automation starts, work in this order:

1. Read the rule files and latest session note.
2. Read `09_Continuity_Index.md` before older notes.
3. Identify the unfinished theme from the previous session.
4. Compare the psychological profile and running case formulation, then choose the most worthwhile thread to continue.
5. Decide whether this session should lean toward understanding emotion, tracking relationships, exploring defenses, handling a practical problem, or integrating meaning.
6. Generate one question in the user's language.
7. Stop after the question and wait for the user's answer instead of producing a long analysis.
