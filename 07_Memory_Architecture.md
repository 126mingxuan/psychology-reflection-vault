# Memory Architecture And Update Rules

Last updated:

## Goal

Make psychological reflection memory readable, editable, and cumulative instead of turning it into a pile of unstructured chat logs.

The system follows a session-based memory rhythm: conversation first, documentation after. Do not write durable memory after every user message. During a session, keep temporary working context; after the session closes, write one coherent session note and update long-term files in a batch.

Memory should support the session, not interrupt it. File reads should normally happen once at the beginning of a session. Additional reads or mid-session writes should be rare and justified by user request, major topic shift, corrected profile information, or risk material.

## Layered Memory

### 0. Onboarding Layer

Use the first-contact onboarding questionnaire only when a new private workspace has little or no profile context.

Store explicit user preferences, broad goals, privacy boundaries, and initial strategy preferences in `01_Client_Profile.md`. Treat early psychological observations as provisional until they are supported by later sessions.

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

The psychological profile must be reviewed and updated after every completed session. It is one cumulative current portrait of the user, not a new file per session. If the session adds stable or repeated evidence, update the relevant stable section. If the session adds a new but unconfirmed clue, record it under items to confirm or provisional observations rather than treating it as a permanent trait.

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
- Use first-contact onboarding only for a new or empty private workspace. Do not repeat the full questionnaire every session.
- Update the running case formulation when the session changes the overall understanding.
- Review and update the psychological profile after every completed session. Stable material should be integrated into the profile; uncertain material should be recorded as provisional or as an item to confirm.
- Keep one current psychological profile file rather than creating a new profile file for every session.
- Record the strategy used in the session and the recommended strategy for the next session.
- Use monthly reports to integrate themes from a month.
- Use yearly reports to summarize long-term change.
- Do not label personality based on one strong emotion.
- Do not write the assistant's interpretation as the user's fact.

## Continuity Rules

- The next session must continue from prior material rather than starting from zero.
- Read the minimum necessary context once at the beginning of the session.
- Use `09_Continuity_Index.md` as the fast entry point for active themes, relevant source files, latest session pointers, unresolved questions, and compression status.
- Read all prior session notes only when the workspace archive is small enough to do so.
- When the archive becomes large, read `09_Continuity_Index.md`, monthly/yearly summaries, the latest session note, and only the earlier notes directly relevant to the current theme.
- Avoid rereading files repeatedly during the same session unless the user asks, a major new topic requires it, or risk handling requires it.
- Always read the latest `05_Psychological_Profile.md` before opening the session.
- Always read the latest strategy recommendation before choosing the working lens for the session.
- Always end with a recommended next session time or interval based on `06_Scheduling_Policy.md`.

## Scalable Reading Protocol

The project should remain usable after six months, one year, or longer. The assistant should not reread every old session note once the archive becomes large.

### Small Archive

Use this when there are about 12 or fewer session notes.

- Read the core files.
- Read all session notes if they fit comfortably.
- Update the running case formulation, psychological profile, and continuity index after the session.

### Medium Archive

Use this when there are about 13-40 session notes.

- Read the core files.
- Read `09_Continuity_Index.md`.
- Read the latest 2-3 session notes.
- Read the latest monthly report.
- Read older session notes only when the continuity index or current theme points to them.

### Large Archive

Use this when there are more than about 40 session notes or when full reading becomes slow.

- Read the core files.
- Read `09_Continuity_Index.md`.
- Read the latest session note.
- Read the latest monthly report and the latest yearly report if available.
- Read targeted older notes only when needed to verify a claim, trace a recurring pattern, handle risk material, or continue an unresolved theme.

### Anti-Drift Rules

- The psychological profile should contain stable or strongly supported material, not every recent emotion.
- The running case formulation should keep hypotheses tentative and source-aware.
- The continuity index should point to evidence; it should not become a hidden source of unsupported conclusions.
- If a profile claim has no clear source, mark it for verification instead of treating it as stable.
- Monthly reports should compress repeated themes, not rewrite the user's identity.
- Yearly reports should describe change over time, not freeze the user into old patterns.

### Maintenance Rhythm

- After each session: update the session note, running case formulation, psychological profile, strategy recommendation, and continuity index.
- At the end of each month or after enough sessions: create a monthly report and clear the compression backlog in `09_Continuity_Index.md`.
- At the end of each quarter: review whether the psychological profile still reflects the user's current state.
- At the end of each year: create or update a yearly report and mark which old themes are resolved, inactive, or still active.
