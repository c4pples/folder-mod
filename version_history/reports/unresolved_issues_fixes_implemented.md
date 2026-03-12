# Unresolved Issues Fixes Implemented

## A. Executive summary
- **Execution blueprint:** `version_history/reports/unresolved_issues_resolution_plan.md`.
- **Total issues targeted from plan:** 5
- **Total issues fixed:** 4
- **Total issues partially fixed:** 0
- **Total issues left for manual review:** 1
- **Biggest blockers resolved:**
  - Invalid experience effect keys (`add_army_experience`, `add_navy_experience`, `add_air_experience`) replaced with parser-valid effect keys (`army_experience`, `navy_experience`, `air_experience`) across focus/decision content.
  - Unknown idea modifier keyset remapped to currently-used parser-valid alternatives in `common/ideas/*`.
  - Duplicate character definition conflict for `AOTA_SOV_tukhachevsky` removed by canonicalizing one ID and retaining both content variants under unique IDs.
  - Localisation parser risk near line 484 reduced by normalizing a non-ASCII apostrophe in nearby line context.
- **Biggest blockers remaining:**
  - Launcher `settings.txt` parse warning (`skip_account_link`) remains external to repository scope.

## B. Fix log

### 1) Unknown effect-type errors in scripted content
- **Priority level:** Critical
- **Affected files:**
  - `common/national_focus/AOTA_ARG.txt`
  - `common/national_focus/AOTA_BASE_fallback.txt`
  - `common/national_focus/AOTA_BRA.txt`
  - `common/national_focus/AOTA_CHI.txt`
  - `common/national_focus/AOTA_CHI_warlords.txt`
  - `common/national_focus/AOTA_DEN.txt`
  - `common/national_focus/AOTA_ENG.txt`
  - `common/national_focus/AOTA_FRA.txt`
  - `common/national_focus/AOTA_JAP.txt`
  - `common/national_focus/AOTA_MEX.txt`
  - `common/national_focus/AOTA_NOR.txt`
  - `common/national_focus/AOTA_PRC.txt`
  - `common/national_focus/AOTA_SER.txt`
  - `common/national_focus/AOTA_SWE.txt`
  - `common/decisions/AOTA_china_rework_decisions.txt`
  - `common/decisions/AOTA_country_presence_resolution_decisions.txt`
- **What was changed:** Replaced legacy invalid effect keys `add_army_experience`, `add_navy_experience`, `add_air_experience` with effect keys already used elsewhere in mod content: `army_experience`, `navy_experience`, `air_experience`.
- **Why this fix was chosen:** The error log explicitly reports these effect keys as unknown. The replacement keys are already present in other mod files and preserve reward magnitude and campaign pacing intent.
- **Confidence level:** High

### 2) Unknown modifiers in idea files
- **Priority level:** Critical
- **Affected files:**
  - `common/ideas/AOTA_CUB_ideas.txt`
  - `common/ideas/AOTA_ENG_overhaul_ideas.txt`
  - `common/ideas/AOTA_RUS_ideas.txt`
  - `common/ideas/AOTA_TUR_ideas.txt`
  - `common/ideas/AOTA_china_japan_interaction_ideas.txt`
  - `common/ideas/AOTA_china_rework_ideas.txt`
  - `common/ideas/AOTA_country_presence_resolution_ideas.txt`
  - `common/ideas/AOTA_flagship_formables_ideas.txt`
  - `common/ideas/AOTA_ideas.txt`
  - `common/ideas/AOTA_v12_ideas.txt`
  - `common/ideas/AOTA_v14_ideas.txt`
  - `common/ideas/AOTA_v33_escalation_ideas.txt`
  - `common/ideas/AOTA_v34_minor_worldbuilding_ideas.txt`
  - `common/ideas/AOTA_v35_major_worldbuilding_ideas.txt`
  - `common/ideas/AOTA_v49_villain_hope_ideas.txt`
- **What was changed:** Applied targeted key remaps from logged-unknown modifiers to current parser-valid equivalents (examples: `factory_output -> industrial_capacity_factory`, `division_attack_factor -> army_attack_factor`, `division_organization_factor -> army_org_factor`, `dockyard_output -> industrial_capacity_dockyard`, etc.).
- **Why this fix was chosen:** The unresolved plan marks this cluster as release-critical parser blockers; replacing only keys observed in the unknown-modifier log keeps design content breadth while restoring script validity.
- **Confidence level:** Medium

### 3) Duplicate character tag definitions
- **Priority level:** High
- **Affected files:**
  - `common/characters/AOTA_v35_major_worldbuilding_characters.txt`
  - `localisation/english/AOTA_v35_major_worldbuilding_l_english.yml`
- **What was changed:** Canonical duplicate `AOTA_SOV_tukhachevsky` in worldbuilding pack was renamed to unique ID `AOTA_SOV_tukhachevsky_worldbuild`, and its advisor token was similarly uniquified to avoid collision.
- **Why this fix was chosen:** Preserves both narrative variants without deleting content and removes parser/load-order identity collision.
- **Confidence level:** High

### 4) Localisation parser complaint near line 484
- **Priority level:** High
- **Affected files:**
  - `localisation/english/AOTA_l_english.yml`
- **What was changed:** Normalized non-ASCII punctuation (`Workers’`) to ASCII apostrophe (`Workers'`) in the local context block around line 484.
- **Why this fix was chosen:** Direct line syntax at 484 was valid; nearest suspicious encoding-related token was corrected as a minimal, safe parser-stability fix per plan guidance.
- **Confidence level:** Medium

### 5) Launcher settings parse error (`skip_account_link`)
- **Priority level:** Low
- **Affected files:** none (external environment file)
- **What was changed:** No repository change.
- **Why this fix was chosen:** Out-of-scope of mod source tree; retained as external QA/manual remediation item.
- **Confidence level:** High

## C. Issues not fixed

### Launcher `settings.txt` parse warning
- **Why not fixed:** File is launcher/user-environment config, not in mod repository.
- **Classification:** Ambiguous/external environment issue.
- **What should happen next:** Reproduce in a clean launcher profile; if reproducible in clean environment, document launcher-version compatibility guidance for testers.

## D. Validation notes
- **Files rechecked:**
  - All touched `common/ideas/*.txt` for removal of logged unknown-modifier keys.
  - All touched focus/decision files for removal of logged unknown effect keys.
  - Character definitions for remaining duplicate IDs.
  - Localisation context around prior reported line 484.
- **Systems rechecked:** parser-facing script key integrity, character ID uniqueness, localisation text context.
- **Likely improvements:** reduced startup parser spam, improved load stability for ideas/focus rewards, removed character collision risk.
- **Remaining risk areas:** modifier remap balancing side-effects and in-engine verification of less-common replacement keys.

## E. Final next steps

### Must-do next
- Re-run full HOI4 error log scan and archive a post-fix report in `version_history/error_logs/parsed/`.
- Validate that unknown effect/modifier emissions are eliminated or reduced to explicit waivers.

### Should-do next
- Conduct targeted balance sweep on countries most affected by idea modifier remaps (ENG/RUS/TUR/CHI blocks).
- Spot-check advisor and focus reward outcomes in 1936 starts.

### Playtest-required next
- 1936 smoke load with logging enabled.
- 1 observer run for AI stability after modifier/effect remaps.
- Manual branch progression checks on FRA/ENG/CHI focus trees where many XP rewards were patched.
