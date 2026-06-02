# Memory Architecture And Update Rules

Last updated:

## Goal

Make psychological reflection memory readable, editable, and cumulative instead of turning it into a pile of unstructured chat logs.

The system follows a session-based memory rhythm: conversation first, documentation after. Do not write durable memory after every user message. During a session, keep temporary working context; after the session closes, write one coherent session note and update long-term files in a batch.

## Layered Memory

### 1. Fact Layer

Record what the user explicitly said: what happened, who was involved, what choices were made, and what needs were clearly expressed.

Do not write interpretations as facts.

### 2. Emotion Layer

Record expressed emotions, intensity, body sensations, and emotional shifts.

### 3. Interpretation Layer

Record psychological understanding from the session, but keep it tentative. Use wording such as "may be related to...", "temporarily appears to...", or "needs further validation."

### 4. Pattern Layer

Write something into long-term patterns only when it appears repeatedly.

### 5. Profile Layer

The psychological profile should include only relatively stable information, such as communication preferences, relational patterns, sources of self-worth, common defenses, deeper needs, and growth direction.

The psychological profile must be reviewed after every session. If the session adds stable or repeated evidence, update the relevant stable section. If the session adds a new but unconfirmed clue, record it under items to confirm or provisional observations rather than treating it as a permanent trait.

### 6. Strategy Layer

Record which reflective strategy was used in the session and what strategy should be tried next. Strategy memory is separate from personality memory: changing the strategy does not mean changing who the user is. It means adapting the working lens to the user's current material.

Strategy choices may include psychodynamic, cognitive-behavioral, family-systems, mindfulness-based, existential, humanistic, safety-first, or an explicit integration of several lenses.

The next session should inherit both continuity and strategy recommendation: read prior notes, preserve the user's history, and then decide whether to continue, combine, or shift the working lens.

### 7. Question Layer

Each session should start with one question only. Priority sources:

1. the unfinished core theme from the previous session;
2. the hypothesis in the profile that most needs validation;
3. the most important open question in the running case formulation;
4. emotional residue from the latest session note;
5. long-term themes in monthly or yearly reports.

### 8. Risk Layer

If self-harm, suicidal intent, harm to others, severe loss of control, or real-world safety issues appear, stop ordinary reflection and prioritize safety.

## Update Rules

- Save a session note after every session.
- Update the running case formulation when the session changes the overall understanding.
- Review and update the psychological profile after every session. Stable material should be integrated into the profile; uncertain material should be recorded as provisional or as an item to confirm.
- Keep one current psychological profile file rather than creating a new profile file for every session.
- Record the strategy used in the session and the recommended strategy for the next session.
- Use monthly reports to integrate themes from a month.
- Use yearly reports to summarize long-term change.
- Do not label personality based on one strong emotion.
- Do not write the assistant's interpretation as the user's fact.

## Continuity Rules

- The next session must continue from prior material rather than starting from zero.
- Read all prior session notes when the vault is small enough to do so.
- When the archive becomes large, read monthly/yearly summaries first, then the latest session note and any earlier notes directly relevant to the current theme.
- Always read the latest `05_Psychological_Profile.md` before opening the session.
- Always read the latest strategy recommendation before choosing the working lens for the session.
- Always end with a recommended next session time or interval based on `06_Scheduling_Policy.md`.
