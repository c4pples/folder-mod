# China Unification Mechanics-Only Pass (with Japan Interaction Support)

## A. Executive summary
- The previous China setup had strong thematic focus trees but lacked a unified mechanical backbone for legitimacy, staged authority, negotiated submission, and post-reunification instability.
- Added a dedicated China unification framework centered on a **legitimacy variable** (`AOTA_china_legitimacy`) and **intermediate political stages** represented by dynamic ideas and flags.
- Added new unification decision categories for Chinese actors and Japan, supporting:
  - congress/coalition route,
  - negotiated submission,
  - coercive submission,
  - formal reunification proclamation,
  - post-unification reconstruction.
- Added event chain support for key transitions: initialization, congress bargaining, submission offers, force ultimatums, reunification proclamation, stability crisis, reconstruction, and Japanese strategic reaction.
- Added anti-unification pressure through legitimacy decay and a refragmentation-risk track after reunification.
- Added targeted, compatibility-oriented Japanese support:
  - two small Japan focuses,
  - a Japan response decision category,
  - reunified-China monitoring idea,
  - event-driven reaction to Chinese reunification.

## B. Current-state diagnosis
### How unification worked before
- CHI/PRC/warlord trees had strong narrative progression but largely delivered linear stat/focus rewards with limited systemic cross-tag unification logic.
- Existing China-Japan interactions were mostly pressure/accommodation toggles and periodic pulses, not integrated into deeper unification progression.

### Main gaps found
- **Legitimacy gap:** no explicit distinction between territorial control and accepted authority.
- **Pacing gap:** no explicit intermediate stages between fragmentation and “functional national center.”
- **Integration gap:** submission/annexation pathways were not strongly differentiated between negotiation and coercion.
- **Post-win gap:** limited mechanical depth after “winning” the unification struggle.
- **Japan coherence gap:** Japan had pressure tools but limited path-sensitive response to different unification outcomes (e.g. contested hegemon vs reunified state).

## C. New unification framework
### Legitimacy system
- Introduced `AOTA_china_legitimacy` as a central variable for China-region actors.
- Added scripted effects for legitimacy gains/losses and stage refresh.
- Legitimacy now influences political stage, available decisions, and reunification timing.

### Route types
- Negotiation route: congress + negotiated submission.
- Coercive route: demand submission under pressure (risking legitimacy damage).
- Coalition route: congress outcomes reward balanced consolidation.
- Collaboration-linked route: Japanese recognition choices can alter legitimacy dynamics.

### Submission/integration logic
- Negotiated submission event offers autonomy-subject outcomes.
- Ultimatum path can force subject alignment or refusal/escalation pressure.
- Submission no longer feels purely binary conquest-only.

### Intermediate stages
- Added stage ideas reflecting gradual progression:
  - Claimant Regime,
  - Provisional Authority,
  - Recognized Coalition Government,
  - Dominant but Contested Core State,
  - Reunified but Unstable,
  - Post-Unification Reconstruction State.

### Post-unification systems
- Reunification proclamation unlocked only at high legitimacy + reduced rival field + substantial control.
- Follow-up “cost of victory” event introduces refragmentation risk vs costly integration choice.
- Reconstruction compacts decision transitions to longer-term stabilization.

### Failure / partial outcomes
- Legitimacy decay from unresolved rivalry and accommodation pressure can stall consolidation.
- Refragmentation-risk idea models post-victory instability if integration is neglected.
- Contested-hegemon stage allows strong-but-not-fully-stable outcomes.

### Japan reaction framework
- Japan can actively:
  - back fragmentation networks,
  - recognize collaborationist actors,
  - prepare against reunified China.
- A reunified-China event now prompts strategic policy shift in Japan.

## D. Country/tag implications
### CHI
- Gains legitimacy via institutional restoration and settlement-focused focuses.
- Can unify through congress, negotiated submission, or coercive pressure depending on timing.
- Distinctiveness: state-institution and constitutional legitimacy hooks.
- Japan interaction: resistance/accommodation legacy flags now intersect with legitimacy progression and Japanese response decisions.

### PRC
- Gains legitimacy via revolutionary-congress and coalition/federal-social paths.
- Can pursue anti-foreign legitimacy route or negotiated integration route.
- Distinctiveness: revolutionary mandate + coalition option.
- Japan interaction: anti-imperial path and accommodation path now feed into shared legitimacy framework.

### Warlords (GXC/YUN/SHX/XSM/SIK/MEN/MAN)
- Existing path identity preserved; now can enter legitimacy framework and use staged submission/reunification decisions.
- Distinctiveness: stronger role as negotiators, conditional submitters, or regional claimants.
- Japan interaction: holdout/collaboration and pressure dynamics influence legitimacy outcomes.

## E. Japanese support changes
- Added small focus-tree support in Japan tree:
  - `JAP_manage_chinese_claimants`
  - `JAP_recalibrate_against_reunified_china`
- Added Japan decision category to support fragmentation, collaborate recognition, and strategic prep.
- Added Japan idea `AOTA_japan_reunified_china_watch` for late-stage strategic response.
- These changes are narrow and compatibility-oriented, not a full Japan rework.

## F. Technical integration notes
### Files changed / added
- Added scripted triggers for actor/threshold checks.
- Added scripted effects for legitimacy and stage refresh.
- Added new unification ideas (stage/state ideas + Japanese watch idea).
- Added dedicated China unification decisions and Japan response decisions.
- Added dedicated unification events namespace.
- Updated CHI/PRC/warlord focus hooks to grant legitimacy in key milestones.
- Updated Japan focus tree with two small compatibility focuses.
- Updated monthly on_action to tick legitimacy/stage progression.
- Extended AI strategy with reunified-China response and legitimacy-aware posture.

### Remaining manual review items
- Verify exact gameplay balance of legitimacy gain/loss rates in long AI runs.
- Confirm event AI weights for submission choices across all warlord tags.
- Validate that subject/autonomy outcomes align with intended lore branching.

## G. Manual playtest recommendations
### Fast unifier scenarios
- CHI hard-centralization rush with coercive submissions.
- PRC military-heavy route with limited coalition concessions.

### Negotiation-driven scenarios
- CHI congress + negotiated submissions chain.
- PRC coalition-socialist route with selective accommodation.

### Post-unification stability tests
- Reunification then emergency-rule option (test refragmentation pressure).
- Reunification then integration-spend option (test stabilization tempo).

### Foreign intervention edge cases
- Japanese recognition of accommodation governments.
- Japan fragmentation support against contested hegemon.

### Japan-China response consistency
- Japan with new claimant-management focus path vs no path.
- Reunified China trigger response and decision availability.

### AI consistency tests
- 1936-1944 observer runs for variety in outcomes (no single deterministic endpoint).
- Check that AI does not always jump directly to conquest route when legitimacy is low.
