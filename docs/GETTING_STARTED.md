# Getting Started

This guide helps you create a private working workspace from the public template. The workspace can be opened in any local file workflow.

## 1. Create Your Private Workspace

Use this repository as a template or fork it. If you plan to write real personal material, make the new repository private.

Recommended names:

```text
my-therapy-support-workspace
private-psychological-support
personal-ai-therapy-support
```

## 2. Open It Locally

Open the folder in any Markdown editor, local file manager, private repository, or local-first AI workspace.

You do not need plugins to use the basic workflow. Plain Markdown is enough.

## 3. Run First-Contact Onboarding

If this is a new private workspace, use `docs/ONBOARDING_QUESTIONNAIRE.md` to run a brief first-contact setup.

Keep it minimal at first. The user may skip any question. Record only what is useful and appropriate for the private workspace.

If you prefer to set up manually, open `01_Client_Profile.md` and fill in only the information you want your AI assistant to remember.

## 4. Start Your First Session

This project does not run by itself. Use it by asking your AI assistant to read the workspace and treat it as the framework for a structured AI-assisted therapy support conversation.

Use this prompt:

```text
Use this folder as my AI-Assisted Therapy Support workspace for the current conversation.
Read AGENTS.md, 00_Start_Here.md, 01_Client_Profile.md, 02_Therapy_Framework.md,
03_Running_Case_Formulation.md, 05_Psychological_Profile.md,
06_Scheduling_Policy.md, 07_Memory_Architecture.md, 09_Continuity_Index.md,
docs/STRATEGY_ROUTING.md,
and prior notes in Sessions/.
If the archive is large, read 09_Continuity_Index.md and monthly/yearly summaries
first, then the latest and most relevant session notes.
Read this context once at the start unless I explicitly ask you to reread.

If 01_Client_Profile.md is empty or nearly empty, use docs/ONBOARDING_QUESTIONNAIRE.md first.
Use this workspace as the framework for this conversation.
Continue from previous material instead of starting from zero.
Choose the reflective strategy dynamically.
Start with one focused opening question.
```

## 5. Save The Session

After the session:

1. Copy `04_Session_Template.md`.
2. Save it under `Sessions/`.
3. Name it with a date, for example:

```text
2026-01-01-session.md
```

## 6. Update Long-Term Memory Carefully

Update `03_Running_Case_Formulation.md` after each meaningful session.

Review and update the single current `05_Psychological_Profile.md` after every completed session. Do not create a new profile file for each session.

Stable, repeated, or strongly supported material should go into the main profile sections. New but uncertain material should go into items to confirm or provisional observations.

Do not turn one emotional moment into a personality conclusion.

## 7. Record Strategy For The Next Session

At the end of each session, record:

- which reflective strategy was used;
- why it fit the session;
- whether the next session should continue, combine, or shift strategy;
- what prior material should be carried forward.

The next conversation should preserve continuity while allowing the working lens to change when the user's material calls for it.

For the complete decision logic, see `docs/STRATEGY_ROUTING.md`.

## 8. Keep The Privacy Boundary Clear

The workspace itself is local-first. It does not require a hosted backend.

If you use a cloud AI assistant, only share the files or excerpts you intentionally provide. For highly sensitive material, consider using a local AI setup or keeping some notes outside AI workflows entirely.

Do not rely on platform-level memory as the primary archive. The local continuity files should remain the source of truth for durable psychological memory.

## 9. Review The Full Lifecycle

For the full workflow, see:

- `docs/SESSION_LIFECYCLE.md`
- `09_Continuity_Index.md`
- `docs/PROMPT_RECIPES.md`
- `examples/full-session-lifecycle-example.md`
