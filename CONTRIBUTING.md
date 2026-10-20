# Contributing to the LL.B. Study Library

## Golden rule

Never write study-content updates directly to main. Work on a dedicated branch, validate the change, open a pull request, and wait for the repository owner's explicit authorisation before merging. Do not merge PRs or move changes to main unless the owner clearly authorises it.

A successful automated check does not mean a legal note is perfect. It only means the defined checks passed.

## Branch names

Use one branch per logical change:
- content/sem01-bns1-day02-YYYYMMDD — new or expanded lesson
- questions/sem01-bns1-bank-YYYYMMDD — question-bank changes
- correction/sem01-bns1-section-review-YYYYMMDD — legal correction
- process/workflow-improvements-YYYYMMDD — process changes

Keep changes focused. Do not combine unrelated subjects or semesters in one branch.

## Before editing

1. Inspect the current branch, repository tree and existing file.
2. Search for an existing topic or question ID to avoid accidental duplication.
3. Preserve existing material. Add a new file where possible; when editing an existing file, retain useful content and record material changes in the applicable changelog.
4. Verify statutory provisions in enacted legislation and the applicable syllabus against official sources.
5. Check whether a question is a verified PYQ or only predicted/practice material.

## Required pull-request process

1. Create a branch from current main.
2. Make focused changes with clear commit messages.
3. Record the update in the root CHANGELOG.md and, for subject-specific content, that subject's CHANGELOG.md.
4. Run link and repository checks; inspect the results.
5. Open a pull request targeting main. Describe the scope, sources, limitations and files changed.
6. Keep the PR open while the owner reviews it. Do not auto-merge.
7. Wait for the owner to authorise merging in a clear instruction. If changes are requested, revise the feature branch and rerun checks.
8. Only after authorisation, merge the approved PR using the chosen merge method. Do not force-push or rewrite shared history.

## Academic accuracy requirements

- Quote or paraphrase the applicable official CCSU syllabus accurately and record the programme/session to which it applies.
- Verify BNS sections, statutory wording, exceptions and penalties against the official enacted text and applicable amendments.
- Cite cases accurately. If a case or citation has not been verified, label it as a research lead rather than authority.
- Label predicted and original practice questions clearly. Never present them as verified past-paper questions.
- Do not describe an answer as perfect or guaranteed. Use documented review checks and state remaining uncertainty.

## Stable IDs and evidence labels

Use stable IDs where practical: DAY-01, TOPIC-BNS1-001, PREDICTED-BNS1-001, PRACTICE-BNS1-001, PYQ-VERIFIED-BNS1-YYYY-001 and CASE-BNS1-001.

A PYQ-VERIFIED label requires the actual paper to have been inspected and its year/session, subject and source recorded.

## Changes after approval

After a merge, record the merge/PR link and commit in the root changelog. Keep old material in Git history and do not delete question entries merely because new versions exist. For material corrections, explain what changed and why.
