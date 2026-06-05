# Dream Mini-Session Workflow

## Purpose

Dream mini-sessions are short supplemental reflections that use a remembered dream to open a brief conversation. They are not full weekly sessions, psychological diagnoses, dream dictionaries, or proof of hidden meanings.

The goal is to help the user briefly notice the dream, the waking emotion, and their own associations. The output should match the user's need instead of automatically producing a fixed interpretation or summary.

## Default Shape

- Default duration: 3 to 7 minutes.
- Default dialogue length: 1 to 3 assistant turns.
- Default output: user-selected.
- Default memory status: single dream notes remain private and local.
- Long-term use: repeated dream themes may be carried into full sessions only when the user permits it or when the theme clearly repeats.

## Output Options

At the end of a dream mini-session, ask or infer what output the user wants:

- no summary: stop after the brief reflection;
- one-sentence takeaway: name the emotional center in one sentence;
- brief private note: record a compact dream snapshot and possible theme;
- structured dream note: use the full template below;
- carry-forward note: write only the part that may be useful for the next full session.

Do not save anything under `Dreams/` unless the user asks to record it.

## Boundaries

Do not:

- diagnose the user from a dream;
- treat a single dream as a stable personality pattern;
- impose universal symbolism;
- claim certainty about unconscious meaning;
- request sensitive details that are not needed;
- turn a dream mini-session into a full psychological session unless the user asks.

If a dream contains immediate danger, self-harm, intent to harm others, severe loss of control, or current real-world safety risk, pause ordinary reflection and follow the safety boundary in `docs/PRIVACY_AND_SAFETY.md`.

## Startup Prompt

Use this when the user wants to start from a dream:

```text
Use this as a dream mini-session, not a full therapy-style session.
Keep it brief. Ask at most one or two clarifying questions unless I ask to continue.
Only create a summary if I ask for one, and match the summary length to what I request.
Do not diagnose me or treat the dream as a complete psychological explanation.
```

## Conversation Flow

### 1. Identify The User's Desired Mode

If the user has not specified the output, ask a lightweight preference question:

```text
Do you want a quick reflection only, a one-sentence takeaway, or a short note saved for later?
```

Do not ask this if the user already made the desired output clear.

### 2. Dream Capture

Ask the user to describe the dream in their own words. If they already provided the dream, do not ask them to repeat it.

Useful fields:

- dream date or approximate night;
- dream content;
- strongest scene or image;
- people, places, or objects that stood out;
- emotion during the dream;
- emotion on waking;
- body sensation on waking, if any.

For a micro-session, do not try to collect every field. Use only what the user naturally provides.

### 3. Brief Clarification

Ask one short question at a time. Use no more than two clarification questions unless the user asks to continue.

Prioritize:

1. Which part stayed with you most after waking?
2. What emotion felt strongest in or after the dream?
3. What does the strongest image personally remind you of?

### 4. Personal Association

Use the user's own associations before offering interpretation.

Helpful question:

```text
When you think about the strongest image in the dream, what does it personally remind you of?
```

Skip this question if the user has already provided a clear association.

### 5. Short Reflection

Offer a concise, tentative reflection. Use language such as:

- "One possible theme is..."
- "This may be less about the literal scene and more about..."
- "Based on your associations, the emotional center seems to be..."

Avoid symbolic certainty.

### 6. Optional Summary And Storage

Only produce a summary when the user asks for one, the startup prompt requests one, or the user chose an output mode that includes a summary.

Possible output formats:

#### One-Sentence Takeaway

```text
The emotional center of this dream seems to be [tentative theme], especially around [image/emotion].
```

#### Brief Private Note

Use 3 to 5 bullets:

- dream snapshot;
- emotional tone;
- user associations;
- possible theme;
- optional observation question.

#### Structured Dream Note

Use the template below only when the user wants a fuller record.

If the user wants it saved, create or update a dated note under `Dreams/`.

## Dream Note Template

```markdown
# YYYY-MM-DD Dream Mini-Session

## Dream Metadata

- Dream date:
- Recorded date:
- Sleep context, if relevant:
- User-requested output: one-sentence takeaway / brief private note / structured dream note / carry-forward note
- Mini-session status: draft / completed / not saved

## Dream Content

-

## Strongest Images

-

## Emotions And Bodily State

- During the dream:
- On waking:
- Body sensations:

## User Associations

-

## Brief Dialogue Notes

-

## User-Requested Output

- Dream snapshot:
- Emotional tone:
- Possible theme, stated provisionally:
- What should not be over-interpreted:
- One observation question:

## Continuity Use

- Carry into next full session: yes / no / only if repeated
- Reason:
- Related prior dream or session note:

## Privacy Check

- Sensitive details minimized:
- Suitable for private vault only:
```

## Relationship To Full Sessions

Dream mini-sessions are supplementary. They can help the assistant notice emotional residue, repeated images, avoidance, grief, fear, desire, conflict, or current stress. They should not replace full sessions.

In full weekly sessions, use dream notes only when:

- the user brings up the dream;
- the continuity index points to repeated dream themes;
- a dream theme clearly connects to the current session focus;
- the user previously allowed dream themes to inform full sessions.
