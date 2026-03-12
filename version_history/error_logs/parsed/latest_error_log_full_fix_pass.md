# Latest HOI4 Error Log Full Fix Pass

## A. Executive summary
- **Newest raw logs scanned:** `version_history/error_logs/raw/error.log` (modified `2026-03-12 18:08:08`), plus directory check for companion logs.
- **Issue clusters identified:** 11 major clusters (launch/parser/reference/content).
- **Safe fixes applied this pass:** 6 clusters fixed directly across 20 files.
- **Biggest blockers resolved:** malformed country tag aliases, invalid DLC trigger token usage, typoed tech key usage, faction trigger typo, scripted trigger token typos, and on_actions BOM parse break.
- **Biggest blockers remaining:** large decision-category parser failures, invalid legacy idea modifiers, invalid event effects (`add_opinion`, `become_subject`), duplicate ideology DB IDs, duplicate character tag.

## B. Top issue clusters

| Cluster | Severity | Source systems/files | Status |
|---|---|---|---|
| Decision category parser failures (`Unknown category`, `Unexpected token`) | High | multiple `common/decisions/*` | Not fixed (ambiguous engine-version/schema mismatch) |
| Malformed `country_tag_aliases` entries causing unknown trigger spam | High | `common/country_tag_aliases/AOTA_country_tag_aliases.txt` | **Fixed** |
| Invalid DLC trigger token `has_dlc_bba` | Medium | multiple `history/countries/*` | **Fixed** |
| Invalid faction trigger `has_faction` | Medium | events + one focus | **Fixed** |
| Scripted trigger key typos (`num_of_owned_states`, `stability`, `war_support`) | Medium | `common/scripted_triggers/AOTA_flagship_formables_triggers.txt` | **Fixed** |
| On-action parse break from BOM/first-token issue | Medium | `common/on_actions/AOTA_v13_on_actions.txt` | **Fixed** |
| Typoed tech key `tech_camelry` | Medium | RAJ/TUR history files | **Fixed** |
| Invalid event effect `add_opinion` | Medium | `events/AOTA_TUR_events.txt` | Not fixed (needs intent-safe redesign to opinion modifier model) |
| Invalid event effect `become_subject` | Medium | `events/AOTA_china_unification_events.txt` | Not fixed (autonomy/subject model unclear) |
| Invalid/legacy idea modifiers | Medium | multiple `common/ideas/*` | Not fixed (needs schema target confirmation) |
| Duplicate ideology DB IDs / duplicate character tag | Medium | ideology + characters files | Not fixed (content ownership conflict, not typo-only) |

## C. Fix log

1. **Issue:** malformed country tag alias definitions generated unknown trigger spam and null alias mapping.
   - **Files changed:** `common/country_tag_aliases/AOTA_country_tag_aliases.txt`
   - **Change:** converted alias entries from `TAG = OTHER` into explicit alias objects using `original_tag`.
   - **Safety rationale:** deterministic format correction; preserves intended semantic mappings without changing geopolitical content.
   - **Confidence:** **high**.

2. **Issue:** BOM/invalid first token in on_actions file produced parse errors.
   - **Files changed:** `common/on_actions/AOTA_v13_on_actions.txt`
   - **Change:** rewrote file UTF-8 cleanly without BOM while preserving event scheduling logic.
   - **Safety rationale:** pure encoding/tokenization repair; no logic redesign.
   - **Confidence:** **high**.

3. **Issue:** invalid DLC trigger token `has_dlc_bba` in country history conditional blocks.
   - **Files changed:**
     - `history/countries/AUS - Austria.txt`
     - `history/countries/CAN - Canada.txt`
     - `history/countries/EGY - Egypt.txt`
     - `history/countries/ENG - Britain.txt`
     - `history/countries/FRA - France.txt`
     - `history/countries/GER - Germany.txt`
     - `history/countries/ITA - Italy.txt`
     - `history/countries/JAP - Japan.txt`
     - `history/countries/RAJ - Dominion of India.txt`
     - `history/countries/SOV - Russia.txt`
     - `history/countries/SPR - Spain.txt`
     - `history/countries/TUR - Ottoman Empire.txt`
     - `history/countries/YUG - Yugoslavia.txt`
   - **Change:** replaced `has_dlc_bba = yes` with `has_dlc = "By Blood Alone"`.
   - **Safety rationale:** straightforward token migration to supported trigger syntax.
   - **Confidence:** **high**.

4. **Issue:** typoed technology key `tech_camelry` caused invalid database object errors.
   - **Files changed:**
     - `history/countries/RAJ - Dominion of India.txt`
     - `history/countries/TUR - Ottoman Empire.txt`
   - **Change:** corrected to `tech_cavalry`.
   - **Safety rationale:** obvious spelling correction with clear intended tech.
   - **Confidence:** **high**.

5. **Issue:** invalid trigger `has_faction` in event/focus logic.
   - **Files changed:**
     - `events/AOTA_faction_evolution_events.txt`
     - `events/AOTA_v49_villain_hope_events.txt`
     - `common/national_focus/AOTA_ENG.txt`
   - **Change:** replaced `has_faction = yes` with `is_in_faction = yes`.
   - **Safety rationale:** direct API-equivalent trigger replacement.
   - **Confidence:** **high**.

6. **Issue:** invalid scripted trigger keys in flagship formables trigger set.
   - **Files changed:** `common/scripted_triggers/AOTA_flagship_formables_triggers.txt`
   - **Change:** replaced `num_of_owned_states` → `num_owned_states`; `stability >` → `has_stability >`; `war_support >` → `has_war_support >`.
   - **Safety rationale:** token-level parser compatibility fix preserving threshold intent.
   - **Confidence:** **medium-high**.

## D. Issues not fixed (manual review required)

1. **Decision category parser failures across many files**
   - **Why not auto-fixed:** broad cross-file schema mismatch (`allowed` trigger restrictions + category parsing cascade). High chance of accidental behavior changes if forced.
   - **Affects:** `common/decisions/*` frameworks (China rework, crises, systems, etc.).
   - **Recommended next step:** validate against exact target HOI4 version decision-schema; normalize category `allowed/visible` blocks and gated scripted triggers.

2. **Invalid event effects (`add_opinion`, `become_subject`)**
   - **Why not auto-fixed:** several plausible replacements (opinion modifier route vs direct relation changes; subject autonomy models differ).
   - **Affects:** diplomatic and unification event outcomes.
   - **Recommended next step:** choose intended diplomatic model then migrate to valid effects (`add_opinion_modifier`, autonomy/subject effects).

3. **Invalid/legacy idea modifiers**
   - **Why not auto-fixed:** many modifier names could map to multiple modern keys; unsafe to guess at balance-sensitive outcomes.
   - **Affects:** idea power level and country balance.
   - **Recommended next step:** run a modifier dictionary pass against current HOI4 version and map each invalid token explicitly.

4. **Duplicate ideology database IDs / duplicate character template tag**
   - **Why not auto-fixed:** content-level conflicts require canonical ownership choice for ideologies/characters.
   - **Affects:** ideology DB and character identity load order.
   - **Recommended next step:** pick single authority file or unique IDs/tags, then reconcile duplicates.

## E. Files changed
- `common/country_tag_aliases/AOTA_country_tag_aliases.txt`
- `common/national_focus/AOTA_ENG.txt`
- `common/on_actions/AOTA_v13_on_actions.txt`
- `common/scripted_triggers/AOTA_flagship_formables_triggers.txt`
- `events/AOTA_faction_evolution_events.txt`
- `events/AOTA_v49_villain_hope_events.txt`
- `history/countries/AUS - Austria.txt`
- `history/countries/CAN - Canada.txt`
- `history/countries/EGY - Egypt.txt`
- `history/countries/ENG - Britain.txt`
- `history/countries/FRA - France.txt`
- `history/countries/GER - Germany.txt`
- `history/countries/ITA - Italy.txt`
- `history/countries/JAP - Japan.txt`
- `history/countries/RAJ - Dominion of India.txt`
- `history/countries/SOV - Russia.txt`
- `history/countries/SPR - Spain.txt`
- `history/countries/TUR - Ottoman Empire.txt`
- `history/countries/YUG - Yugoslavia.txt`

## F. Remaining top-priority manual issues
1. Decision category parsing failures across the v13/v33/v44/v49 and China decision packs.
2. Invalid idea modifiers in multiple idea files.
3. `add_opinion` and `become_subject` event effect migrations.
4. Duplicate ideology DB IDs in `common/ideologies/AOTA_ideologies.txt`.
5. Duplicate character tag for `ENG_neville_chamberlain`.
