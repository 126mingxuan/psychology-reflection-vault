# Adaptive Scheduling Policy

Last updated: 2026-05-27

## Goal

After each psychological reflection session, do not mechanically fix the next time. Instead, use the session content, the user's state, and any unfinished themes to decide when the next automated reflection prompt should start.

When the automation starts, it should produce one new opening question. The session formally begins when the user has time to answer.

## Default Settings

- Default frequency: once per week.
- Default duration: 45 to 60 minutes.
- Default trigger: Friday evening.
- If the previous session shows that an earlier or later follow-up would be more useful, adjust the next trigger time.

## Next-Time Judgment

### Recommend 2 To 3 Days Later

Use this when:

- emotional intensity in the session was high;
- the user remains clearly anxious, low, suppressed, confused, or insufficiently held;
- an important theme appeared but there was not enough time to explore it;
- the user needs closer psychological continuity;
- waiting a full week could cause the material to fragment or pressure to accumulate.

### Recommend 4 To 5 Days Later

Use this when:

- the session introduced important material that should continue soon;
- emotional intensity is moderate but not acute;
- the user needs a few days to observe real-life reactions;
- a full week feels too long, while 2 to 3 days feels too soon.

### Recommend 7 Days Later

Use this when:

- the current theme has mostly closed;
- the user's emotional state is relatively stable;
- one clear observation point has formed for the coming week;
- the normal counseling-like rhythm is appropriate.

### Recommend 10 To 14 Days Later

Use this when:

- the session has been sufficiently integrated;
- the user needs more time to digest, practice, or observe;
- there is no high-intensity emotion or urgent theme for now;
- overly frequent analysis could become rumination.

## Required End-Of-Session Record

At the end of each session note, include:

- session closure judgment:
- recommended next trigger time:
- scheduling rationale:
- direction for the next opening question:
- continuity index update needed:

## Automation Execution Rules

If the automation can directly update the next run time, adjust it according to the recommendation.

If the current system cannot set an arbitrary next date, keep the default schedule, record the recommended time clearly in the session summary, and wait for user confirmation or manual adjustment.

## Long-Term Operating Rule

For a mature vault, scheduling should consider both emotional need and memory load:

- if the user needs faster support, recommend an earlier check-in;
- if the session is integrated and more processing time would help, recommend a longer interval;
- if many sessions accumulate, update monthly summaries and `09_Continuity_Index.md` so future starts remain fast;
- do not increase contact frequency simply because more files exist.
