# HOI4 Error Log Scan + Safe Auto-fix (latest pass)

## A. Executive summary
- **Newest logs scanned:** `version_history/error_logs/raw/error.log` (mtime: 2026-03-12 14:57:02 UTC).
- **Major issue clusters found:** 8.
- **Safe fixes applied automatically:** 4 root-cause fixes across 14 files.
- **Top remaining blockers:**
  1. Unknown effect types (`add_army_experience`, `add_navy_experience`, `add_air_experience`) in multiple scripted effects/decisions.
  2. Unknown modifiers in idea files (likely version/API mismatch names).
  3. Duplicate character tags in character definitions.
  4. One localisation parser complaint at `AOTA_l_english.yml` line 484 (not reproducible from direct line inspection; needs in-game parser validation).

## B. Hard blockers found
1. **Decision schema wrapper errors** (`categories = {}`, `category = { id = ... }`, `decision = { id = ... }`) caused parser/category failures and decision registration failures.
2. **Country tag alias format errors** produced invalid alias warnings and unexpected token errors (`original_tag`, `fallback`, alias tag invalid).
3. **State history malformed token**: `buildings_max_level_factor` triggered parser failures in several state files.

## C. Major errors found
- Massive repeated **unknown effect-type** errors (171) concentrated around old effect names.
- Repeated **unknown modifier** errors (71) concentrated in ideas files.
- **Decision parser spam** (121) from a smaller set of malformed decision files (single root cause).
- **Duplicate character tags** (2 instances).
- One **localisation colon parse error** in `AOTA_l_english.yml` line 484.
- One **launcher-side settings parse error** in `settings.txt` (outside mod content).

## D. Safe fixes applied

### Fix 1: Normalize malformed decisions schema into valid HOI4 decision/category structure
- **Issue summary:** Decision files used wrapper blocks not recognized by HOI4 parser.
- **Likely source files:**
  - `common/decisions/AOTA_CUB_decisions.txt`
  - `common/decisions/AOTA_ENG_overhaul_decisions.txt`
  - `common/decisions/AOTA_RUS_decisions.txt`
  - `common/decisions/AOTA_TUR_decisions.txt`
  - `common/decisions/AOTA_china_japan_interaction_decisions.txt`
  - `common/decisions/AOTA_v10_decisions.txt`
  - `common/decisions/AOTA_systems.txt`
  - `common/decisions/AOTA_country_presence_resolution_decisions.txt`
- **What changed:**
  - Removed invalid top-level wrappers like `categories = { ... }`.
  - Replaced invalid `category = { id = X ... }` with `X = { ... }`.
  - Replaced invalid `decision = { id = Y ... }` with `Y = { ... }`.
- **Why safe:** Pure structural parser repair; content, triggers, effects, and balance logic were preserved.
- **Confidence:** **High**.

### Fix 2: Convert country tag aliases to valid alias assignments
- **Issue summary:** Alias file used unsupported object format (`original_tag`, `fallback`) causing invalid alias parsing.
- **Source file:** `common/country_tag_aliases/AOTA_country_tag_aliases.txt`
- **What changed:** Converted each alias block to canonical `ALIAS = TAG` form.
- **Why safe:** Direct syntax correction preserving existing alias intent.
- **Confidence:** **High**.

### Fix 3: Remove invalid state field triggering malformed token errors
- **Issue summary:** `buildings_max_level_factor` generated malformed token errors in state history files.
- **Source files:**
  - `history/states/471-Northwestern Canada.txt`
  - `history/states/472-Northwest Territories.txt`
  - `history/states/644-state 3.txt`
  - `history/states/876-Udachny.txt`
  - `history/states/967-Deep Amazonas.txt`
- **What changed:** Removed only the invalid `buildings_max_level_factor` line from each impacted state file.
- **Why safe:** Minimal parser-stability fix; no owner/core/VP/political/lore changes.
- **Confidence:** **High**.

### Fix 4: Post-fix structural validation pass
- **Issue summary:** Risk of introducing brace/syntax issues while transforming files.
- **What changed:** Re-scanned touched files for wrapper remnants and verified balanced braces.
- **Why safe:** Validation-only pass, no gameplay changes.
- **Confidence:** **High**.

## E. Issues not auto-fixed
1. **Unknown effect-type spam (171)**
   - **Why not auto-fixed:** Multiple possible replacement APIs depending on HOI4 version and script context; risky bulk substitutions could alter gameplay.
   - **Recommended next step:** Validate target HOI4 version and run controlled replacement matrix (e.g., `add_army_experience` -> expected current effect form where applicable).

2. **Unknown modifiers in ideas (71)**
   - **Why not auto-fixed:** Ambiguous mapping for many modifiers (`division_attack_factor`, `factory_output`, etc.) across versions and systems.
   - **Recommended next step:** Version-aware modifier map + targeted refactor by file with gameplay review.

3. **Duplicate character tags**
   - **Why not auto-fixed:** Could represent intentional overrides or multiple content branches.
   - **Recommended next step:** Resolve by choosing canonical definition per tag and remove/rename duplicates.

4. **Localisation parse error at line 484**
   - **Why not auto-fixed:** Direct file inspection shows syntactically normal line; likely contextual/encoding or upstream malformed-entry interaction.
   - **Recommended next step:** Validate with in-engine load and check adjacent lines for hidden characters/encoding anomalies.

5. **Launcher `settings.txt` parse error (`skip_account_link`)**
   - **Why not auto-fixed:** External user environment file, not mod source.
   - **Recommended next step:** Regenerate launcher settings file outside repo context.

## F. Likely noise / low-priority warnings
- Repeated duplicate emission of the same parser error stack from one malformed file.
- Secondary warnings cascading from primary category/decision schema failures.

## G. Files changed
- `common/decisions/AOTA_CUB_decisions.txt`
- `common/decisions/AOTA_ENG_overhaul_decisions.txt`
- `common/decisions/AOTA_RUS_decisions.txt`
- `common/decisions/AOTA_TUR_decisions.txt`
- `common/decisions/AOTA_china_japan_interaction_decisions.txt`
- `common/decisions/AOTA_v10_decisions.txt`
- `common/decisions/AOTA_systems.txt`
- `common/decisions/AOTA_country_presence_resolution_decisions.txt`
- `common/country_tag_aliases/AOTA_country_tag_aliases.txt`
- `history/states/471-Northwestern Canada.txt`
- `history/states/472-Northwest Territories.txt`
- `history/states/644-state 3.txt`
- `history/states/876-Udachny.txt`
- `history/states/967-Deep Amazonas.txt`

## H. Top priority remaining work
1. Build and apply a **version-accurate effect/modifier compatibility map** for idea/decision scripting.
2. Resolve duplicate character tag definitions.
3. Re-run HOI4 logs after this pass to confirm decision/category and alias error collapse.
4. Investigate localisation parser context around `AOTA_l_english.yml` line 484 with engine-side parser.
