# Prompt Recipes

These prompts are starting points. Adapt them to your own private workspace and language.

## Standard AI-Assisted Therapy Support Prompt

Use this when you want the full workflow in a private working workspace.

```text
Use this folder as my AI-Assisted Therapy Support workspace for the current conversation.

First, read AGENTS.md and follow its workflow. Then read the minimum necessary continuity context:
00_Start_Here.md, 01_Client_Profile.md, 02_Therapy_Framework.md,
03_Running_Case_Formulation.md, 05_Psychological_Profile.md,
06_Scheduling_Policy.md, 07_Memory_Architecture.md, 09_Continuity_Index.md,
and the latest relevant notes in Sessions/.
If the archive is large, read 09_Continuity_Index.md and monthly/yearly reports first, then the latest and most relevant session notes.

If 01_Client_Profile.md is empty or nearly empty, begin with the first-contact onboarding workflow in docs/ONBOARDING_QUESTIONNAIRE.md.
Ask only a few setup questions at a time, let me skip any question, and record only what is useful and appropriate for this private workspace.

During the session:
- speak in my language unless I request another language;
- do not claim to be a therapist, doctor, or crisis service;
- use a professional counseling-informed, therapy-oriented support structure;
- read context once at the start unless I ask you to reread or safety requires it;
- do not update durable memory after every message;
- prioritize the live conversation over documentation;
- avoid turning the session into a questionnaire;
- reflect emotional meaning before advice or technique;
- follow docs/CONVERSATION_EXPERIENCE.md for the therapeutic conversation model: contact, assessment, working focus, exploration, tentative formulation, timed intervention, and active closing;
- use docs/STRATEGY_ROUTING.md to choose whether to continue, combine, or shift reflective lenses;
- use external web search only when it genuinely improves the session or I ask for it.

If immediate danger, suicidal intent, self-harm intent, or harm-to-others risk appears, stop ordinary reflection and prioritize real-world safety.

When the session is ready to close:
- summarize the core theme, emotional pattern, and next focus;
- recommend the next check-in time using 06_Scheduling_Policy.md;
- create a dated session note under Sessions/ using 04_Session_Template.md;
- update 03_Running_Case_Formulation.md when the working understanding changes;
- review and update the single current 05_Psychological_Profile.md;
- update 09_Continuity_Index.md so the next session can read efficiently;
- record the strategy used this session and the recommended strategy for next session.

Start now by briefly connecting to the previous material, then ask one focused opening question.
```

## First-Contact Onboarding

```text
Use docs/ONBOARDING_QUESTIONNAIRE.md to run a brief first-contact setup.
Ask only a few questions at a time.
Let me skip any question.
Do not collect more private information than needed.
After the setup, update 01_Client_Profile.md with explicit preferences and basic context.
Mark early psychological observations as provisional.
Then begin the first therapy-support session by establishing contact and a clear working focus.
```

## Start A Weekly Reflection Session

```text
Read AGENTS.md, the core continuity files, the latest psychological profile, the running case formulation,
09_Continuity_Index.md, and prior session notes in Sessions/. If the archive is large,
read the continuity index and monthly/yearly summaries first, then the latest and most relevant session notes.
Read this context once at the start unless I explicitly ask you to reread.
Use this workspace as the framework for this conversation.
Continue from the existing psychological reflection system.
Use docs/STRATEGY_ROUTING.md to decide whether to continue, combine, or shift reflective lenses.
Start with one focused opening question.
```

## Continue From The Previous Session

```text
Read the latest session note.
Read the latest psychological profile and the strategy recommendation from the running case formulation.
Identify the unfinished emotional or relational theme.
Choose whether to continue, combine, or shift the reflective strategy.
Ask one question that continues from the prior material.
```

## Close A Session

```text
Summarize the core theme, the main emotional pattern, and one useful next observation.
Recommend the next check-in time using 06_Scheduling_Policy.md.
Then create a session note using 04_Session_Template.md.
Update 03_Running_Case_Formulation.md.
Review and update 05_Psychological_Profile.md: integrate stable evidence, and record
uncertain clues as provisional observations or items to confirm.
Update 09_Continuity_Index.md with active themes, source pointers, and compression status.
```

## Update Long-Term Memory

```text
Do not update durable memory after every user message.
Avoid repeated file reads during the same session unless the user asks, a major new theme requires it, or safety handling requires it.
During the session, keep temporary working context only.
After the session closes, save one coherent session note.
Update 03_Running_Case_Formulation.md with tentative hypotheses.
Review and update 05_Psychological_Profile.md after every completed session.
Put stable repeated material into profile sections.
Put uncertain material into provisional observations or items to confirm.
Keep one current psychological profile file instead of creating a new profile file every session.
Use local continuity files, not platform-level memory, as the durable archive.
Use 09_Continuity_Index.md as a routing layer, not as a replacement for source notes.
```

## Record Strategy For Next Session

```text
Based on this session and previous notes, record:
1. the primary reflective lens used;
2. supporting lenses used;
3. why this strategy fit;
4. whether the next session should continue, combine, or shift strategy;
5. which prior material should be carried forward.
```

## Strategy Routing Check

```text
Use docs/STRATEGY_ROUTING.md to review the current session strategy.
Check safety first.
Identify the current main theme.
Compare it with the previous strategy recommendation.
Choose one primary lens and, if needed, one supporting lens.
Explain briefly why this lens fits.
At the end of the session, record whether the next session should continue, combine, or shift strategy.
```

## Monthly Review

```text
Read all Sessions notes from this month.
Summarize repeated themes, emotional shifts, relational patterns, useful practices, and next-month focus.
Save the result under Reports/Monthly/.
```

## Privacy Review Before Publishing

```text
Review this repository for private or identifiable information.
Flag any real session notes, names, locations, contact details, health details, relationship details, or risk notes.
Do not publish until those are removed.
```
