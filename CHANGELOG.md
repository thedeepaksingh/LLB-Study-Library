# Repository Change Log

This is an append-only summary of meaningful changes to the study library. Detailed subject changes belong in each subject's own CHANGELOG.md. Use PR links and commit hashes wherever available.

## Entry format

For every accepted change, append:
- date in ISO format (YYYY-MM-DD);
- PR number/link and merge commit;
- affected semester, subject and topic;
- files added/changed;
- change type (new content, legal correction, syllabus update, question bank or workflow);
- sources checked;
- review status;
- unresolved limitations or follow-up tasks.

## Entries

### 2026-10-20 — Repository governance workflow proposed

- Branch: process/controlled-updates-and-review
- Status: proposed on a feature branch; not approved or merged to main.
- Purpose: add branch-based change procedure, owner authorisation policy, PR template, internal-link validation and review checklist.
- Accuracy note: checks can detect structural issues and broken internal links, but cannot guarantee legal or academic perfection.
- Merge record: to be completed only after the owner authorises and the PR is merged.

## Preservation rule

Do not rewrite or delete historical entries. If an entry needs correction, append a correction explaining the original statement, corrected information and supporting source.


### 2026-10-20 — Study-first operating agreement and syllabus completeness tracking

- **Branch:** `process/controlled-updates-and-review`
- **Status:** Proposed; not merged to `main`.
- **Files added:** BNS-1 content completeness matrix and study-maintenance agreement.
- **Purpose:** make clear that the assistant handles repository organisation and study-content maintenance, while the owner focuses on learning and retains explicit approval authority for each merge.
- **Preservation:** the BNS-1 collection stays under `Semester-01/BNS-1/`; completeness is tracked by topic instead of treating the existence of a file as proof that it is finished.


### 2026-10-20 — Direct BNS-1 study content proposed
- **Branch:** `content/bns1-direct-learning-pack-2026-10-20`
- **Status:** Draft for review; not merged into `main`.
- **Subject path:** `Semester-01/BNS-1/`
- **Files:** added direct full-syllabus teaching notes, BNS section-wise learning guide, 22-case casebook, and original worked exam problems/answers; updated subject navigation, section finder, case-law dashboard and subject changelog.
- **Purpose:** replace a link-heavy framework with actual study text, statutory ingredients, section numbers, case facts/holdings and application problems in the same BNS-1 location.
- **Limitations:** summaries need continuing legal review; IPC-era cases are not represented as automatic interpretations of BNS. Practice questions are not claimed to be actual CCSU PYQs. The direct-learning pack has not been merged to main.


### 2026-10-23 — Direct-learning packs for remaining Semester 1 subjects proposed
- **Branch:** `content/semester1-other-subjects-2026-10-23`
- **Status:** Draft pull request for owner review; not merged to `main`.
- **Affected area:** Semester 1 — K-1001 Jurisprudence–I, K-1002 Constitutional Law of India–I, K-1003 Law of Torts & Consumer Protection Law, and K-1005 Contract–I.
- **Added:** syllabus/source maps, study plans, complete teaching notes, theory/statute/article guides, case-law casebooks, original worked practice questions and per-subject completeness matrices/changelogs; Semester 1 and master navigation updated.
- **Sources checked:** CCSU-hosted three-year LL.B. syllabus; CCSU January 2026 examination schedule; Government of India Constitution of India edition (2024); India Code Consumer Protection Act, 2019 and Indian Contract Act, 1872; Department of Consumer Affairs 2021 consumer commission jurisdiction rules.
- **Study/content status:** expanded teaching drafts. Current legal and case-law verification, faculty review and the student's batch-specific syllabus confirmation remain pending.
- **Question provenance:** worked problems are original practice, not verified CCSU PYQs.
- **Validation limit:** repository link/structure checks do not guarantee legal correctness. Do not mark as fully verified solely because these files exist.
