# AOTA Multi-Batch Standards Pass

## A. Executive summary
This pass starts from the prior repass conclusion that AOTA still needed deeper standards work in three classes: idea token modernization, one-line/structural normalization, and direct Kaiserreich source-side comparative extraction for scripting discipline.

Executed batches:
1. ideas token modernization and schema discipline in high-risk idea files
2. one-line file normalization for parser-sensitive systems (focuses/decisions/events)
3. direct Kaiserreich source-side comparative extraction from a live KR source checkout (`/tmp/KRHOI4`) and application of structural conventions
4. anti-regression hardening with stricter static lint controls
5. residual parser hygiene cleanup (BOM removal and formatting integrity)

Biggest improvements:
- idea files with compressed one-line definitions are now consistently multi-line and parser-legible
- high-risk one-line focus trees and escalation decisions/events are now maintainable and safer for incremental edits
- static lint now enforces additional anti-regression checks for compressed idea blocks, overlong parser-risk lines, and idea-file BOM detection
- UTF-8 BOM contamination in ideas files was removed

Biggest remaining gaps:
- several very large focus files still retain overlong lines and should be normalized in follow-on batches (`AOTA_SOV`, `AOTA_USA`, `AOTA_GER`, `AOTA_AWU`, `AOTA_CHI_warlords`)
- full-mod holistic runtime validation still requires in-engine error.log/game.log replay after this pass
- additional modernization depth is still possible in untouched legacy files

## B. Multi-batch execution plan summary
### Batch order and dependencies
1. **Batch 1 (ideas tokens)** first, because idea tokens are reused by focus/event/decision systems and breakage here cascades.
2. **Batch 2 (one-line normalization)** second, to reduce parser and maintenance risk before broader comparative enforcement.
3. **Batch 3 (direct KR comparison)** third, to map KR structural discipline directly onto now-readable AOTA files.
4. **Batch 4 (anti-regression enforcement)** fourth, so newly adopted standards become enforceable.
5. **Batch 5 (residual cleanup)** last, to remove leftovers surfaced by prior batches.

Sequence rationale: stabilize parser-facing primitives first, then normalize structure, then apply benchmark conventions, then lock the gains via lint.

## C. Batch 1 — ideas token modernization
### Scope
- country-idea definitions with compressed one-line syntax and inconsistent structural discipline
- files previously implicated in historical idea-related parser errors and token drift

### Files/systems touched
- `common/ideas/AOTA_v12_ideas.txt`
- `common/ideas/AOTA_TUR_ideas.txt`
- `common/ideas/AOTA_RUS_ideas.txt`
- `common/ideas/AOTA_china_rework_ideas.txt`

### What was modernized
- normalized idea definitions from dense one-line blocks into stable multiline blocks
- standardized nesting for `allowed` and `modifier` sections
- preserved gameplay values/mechanics while improving parser readability and edit safety

### Anti-patterns removed
- one-line mega-definitions that hide scope boundaries
- mixed brace-density patterns that increase accidental token bleed during edits

### Parser/maintainability gains
- clearer block boundaries reduce accidental key placement and malformed brace risk
- consistency with large-mod multi-line maintenance practice

## D. Batch 2 — one-line file normalization
### Scope
Targeted parser-sensitive files with chronic long-line structural compression.

### Files normalized
- `common/national_focus/AOTA_COG.txt`
- `common/national_focus/AOTA_NZL.txt`
- `common/national_focus/AOTA_MAL.txt`
- `common/national_focus/AOTA_SAF.txt`
- `common/national_focus/AOTA_AST.txt`
- `common/national_focus/AOTA_ALG.txt`
- `common/national_focus/AOTA_CAN.txt`
- `common/national_focus/AOTA_EGY.txt`
- `common/national_focus/AOTA_RAJ.txt`
- `common/national_focus/AOTA_INS.txt`
- `common/decisions/AOTA_v33_escalation_decisions.txt`
- `events/AOTA_TUR_events.txt`

### Improvements achieved
- converted compressed trees/events/decisions into multiline maintainable structure
- improved indentation and block visibility in prerequisite/available/reward logic
- reduced extreme line lengths in touched decisions/events content

### Logic-preservation checks
- normalization performed as structural rewrite only (no intentional mechanical rebalance)
- post-pass static lint and legacy token scans were re-run to catch accidental syntax regressions

## E. Batch 3 — KR source-side comparative extraction
### Direct source reference used
A direct source checkout of Kaiserreich code was used in this pass:
- `/tmp/KRHOI4/common/ideas/RUS ideas (Russia).txt`
- `/tmp/KRHOI4/common/national_focus/SER focus (Serbia).txt`

### Practical KR patterns extracted
- strict multiline block formatting for idea and focus entries
- explicit, separated `allow_branch` / `available` / `bypass` / `ai_will_do` sections in focus definitions
- comment-delimited organizational segmentation for high-volume files
- preference for legible structural spacing over compressed token density

### How applied to AOTA
- touched AOTA ideas/focuses/decisions/events were reshaped toward multiline parser-legible blocks
- anti-regression lint gained structural checks to discourage reintroduction of compressed idea blocks

### Where AOTA intentionally differs
- AOTA content identity, mechanics, and lore remain AOTA-authored
- no KR lore/path/content transplantation was performed; only structural discipline was borrowed

## F. Batch 4 — anti-regression enforcement
### Controls added/improved
- expanded `version_history/error_logs/parsed/aota_static_lint.py` with:
  - compressed one-line ideas block detection
  - overlong-line checks in parser-sensitive directories
  - BOM detection for ideas files

### Recurring failure classes hardened
- legacy idea-token regressions
- unreadable compressed idea layouts
- hidden BOM parser contamination in idea files

### Known temporary exclusions
Some high-debt files remain excluded from overlong-line enforcement pending dedicated normalization subpasses:
- `common/national_focus/AOTA_AWU.txt`
- `common/national_focus/AOTA_CHI_warlords.txt`
- `common/national_focus/AOTA_GER.txt`
- `common/national_focus/AOTA_SOV.txt`
- `common/national_focus/AOTA_USA.txt`

## G. Batch 5 — residual cleanup
- removed UTF-8 BOM from:
  - `common/ideas/AOTA_v14_ideas.txt`
  - `common/ideas/AOTA_v17_world_ideas.txt`
  - `common/ideas/AOTA_v34_minor_worldbuilding_ideas.txt`

## H. Files changed
- `common/ideas/AOTA_v12_ideas.txt`
- `common/ideas/AOTA_TUR_ideas.txt`
- `common/ideas/AOTA_RUS_ideas.txt`
- `common/ideas/AOTA_china_rework_ideas.txt`
- `common/ideas/AOTA_v14_ideas.txt`
- `common/ideas/AOTA_v17_world_ideas.txt`
- `common/ideas/AOTA_v34_minor_worldbuilding_ideas.txt`
- `common/national_focus/AOTA_COG.txt`
- `common/national_focus/AOTA_NZL.txt`
- `common/national_focus/AOTA_MAL.txt`
- `common/national_focus/AOTA_SAF.txt`
- `common/national_focus/AOTA_AST.txt`
- `common/national_focus/AOTA_ALG.txt`
- `common/national_focus/AOTA_CAN.txt`
- `common/national_focus/AOTA_EGY.txt`
- `common/national_focus/AOTA_RAJ.txt`
- `common/national_focus/AOTA_INS.txt`
- `common/decisions/AOTA_v33_escalation_decisions.txt`
- `events/AOTA_TUR_events.txt`
- `version_history/error_logs/parsed/aota_static_lint.py`

## I. Validation notes
Validation executed in this pass:
- static lint run after hardening changes
- legacy modifier token scan across ideas
- line-length distribution checks across script categories

Result: current lint gate passes in-repo after this pass.

## J. Remaining issues / manual review
1. perform next normalization batch on excluded high-debt focus files
2. execute in-engine run and archive fresh `error.log` and `game.log` for runtime-only issues
3. extend lint toward cross-file reference checks (focus/event/idea/localisation linkage) in future pass

## K. Final standards assessment
This pass materially reduces the remaining gap from the prior repass by delivering substantial modernization in the three explicitly requested classes and by adding stronger anti-regression enforcement. AOTA is now closer to Kaiserreich-level structural scripting discipline in touched systems, while preserving AOTA-specific content and design identity.
