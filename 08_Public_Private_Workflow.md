# Public Template And Private Workspace Workflow

## Purpose

This project is designed to support two separate spaces:

- a public template repository that can be shared on GitHub;
- a private working workspace that contains real personal reflection material.

Never mix these two spaces casually. Psychological notes can contain sensitive emotional, relational, health, identity, or risk material.

## Public Template Repository

The public repository may contain:

- workflow rules;
- blank templates;
- fictional examples;
- installation scripts;
- agent skill instructions;
- documentation for privacy, safety, onboarding, and long-term maintenance.

The public repository should not contain:

- real session notes;
- real client history;
- identity information;
- contact information;
- health details;
- family or relationship details;
- financial details;
- crisis or risk material;
- private messages or private documents.

## Private Working Workspace

The private workspace may contain the user's real continuity files:

- `Sessions/*.md`;
- `Dreams/*.md`;
- monthly and yearly reports;
- user-specific profile details;
- case formulation updates;
- risk notes;
- personal observation tasks.

Keep the private workspace local or in a private repository. Review every file before changing visibility.

## Recommended Setup

1. Keep this repository public-safe.
2. Create a separate private folder for real use, such as `~/Documents/psychology-reflection`.
3. Copy the template files into that private folder.
4. Run first-contact onboarding.
5. Store real session notes only in the private folder.
6. Use fictional examples when documenting the project publicly.

## Publish Checklist

Before pushing or publishing:

- confirm `Sessions/*.md` is ignored unless the file is a public README;
- confirm `Dreams/*.md` is ignored unless the file is a public README;
- confirm monthly and yearly reports are ignored unless they are public READMEs;
- search for private names, addresses, contacts, credentials, tokens, and health details;
- review the diff instead of using a blind upload;
- keep examples fictional and clearly labeled.

## Updating The Template From A Private Workspace

If the private workspace reveals a useful workflow improvement:

1. Extract the general rule.
2. Remove personal details.
3. Rewrite the improvement as a reusable public instruction.
4. Add it to the public template, docs, or fictional examples.
5. Do not copy real session material into the public repository.
