# Public And Private Vault Workflow

## Core Principle

The public repository stores the system template. A private repository or local folder stores real personal material.

## Recommended Structure

```text
psychology-reflection-vault/
  public templates, instructions, and reusable rules

my-private-psychology-vault/
  real client profile
  real Sessions/
  real Reports/
  real case formulation and psychological profile
```

## What The Public Repository May Include

- General README
- AGENTS.md instructions
- Session templates
- Memory architecture
- Scheduling policy
- Blank psychological profile template
- Blank case formulation template
- Public/private workflow instructions

## What The Public Repository Should Not Include

- Real session notes
- Real names, contact details, addresses, or accounts
- Family, romantic relationship, workplace, school, or other identifying details
- Psychological risk notes, medical history, diagnosis, or medication details
- AI-generated personal psychological profiles
- Anything the user would not want strangers to read

## Updating The Public Project

When a private working vault produces a reusable improvement:

1. Validate the mechanism privately first.
2. Abstract it into a template or rule without personal details.
3. Update the public project.
4. Check for private information before committing and pushing.

## Updating A Private Vault

After each real session:

1. Save the session note in `Sessions/`.
2. Update `03_Running_Case_Formulation.md`.
3. Update `05_Psychological_Profile.md` only if needed.
4. Optionally commit to a private Git repository or keep the vault local only.
