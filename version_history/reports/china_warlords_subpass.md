# China Warlords-Only Sub-Pass Report

## A. Executive summary
This sub-pass introduces a dedicated warlord gameplay layer for China's non-central actors (GXC, YUN, SHX, XSM, SIK, MEN, MAN) through a new shared-but-differentiated focus tree, expanded statecraft decisions, actor-specific identity spirits, and new narrative events.

The design goal was additive integration: no existing China rework content was removed, and the old generic fallback content remains for other minors. Chinese regional actors now receive distinct identity scaffolding, branching midgame politics, and late-game relevance centered on autonomy, unification bids, or accommodation under pressure.

## B. Warlord / regional actor diagnosis
### Prior diagnosis
- Warlord tags were routed into the universal fallback tree with limited regional specificity.
- Political identity, social base, and institutional logic were under-expressed.
- Progression lacked China-specific turning points and unification bargaining.

### Applied diagnosis-driven changes
- Created a dedicated warlord focus tree with early institutional setup, mutually exclusive political strategy, and late-game synthesis.
- Added tag-specific identity spirits to prevent interchangeability.
- Added regional decision loop for assemblies, patronage reshuffles, logistics crises, border incidents, and unification backchannels.
- Added event prose to convey councils, command politics, and negotiated sovereignty.

## C. Country-by-country summary
### Guangxi (GXC)
- Identity: Southern federal military-commercial machine.
- Signature spirit: **Southern Federal Machine**.
- Best-fit paths: negotiated autonomy, regional unification conference, anti-bandit governance.

### Yunnan (YUN)
- Identity: Mountain arsenal politics with difficult terrain logistics.
- Signature spirit: **Mountain Arsenal Compacts**.
- Best-fit paths: militarized autonomy or selective unification through command integration.

### Shanxi (SHX)
- Identity: Railway garrison state with disciplined interior defense.
- Signature spirit: **Railway Garrison State**.
- Best-fit paths: reconstruction commissions + political guard formations.

### Xibei San Ma (XSM)
- Identity: Frontier commanderies and mobile patronage army.
- Signature spirit: **Frontier Commanderies**.
- Best-fit paths: militia screening + anti-bandit zones + mandate path.

### Sinkiang (SIK)
- Identity: Corridor governorate balancing frontier governance and external commerce.
- Signature spirit: **Governorate of Corridors**.
- Best-fit paths: accommodation channel + bargained security protocols.

### Mengkukuo (MEN)
- Identity: Banner hierarchy and frontier administration under pressure.
- Signature spirit: **Steppe Banner Administration**.
- Best-fit paths: local survival compact or foreign accommodation, depending on strategic pressure.

### Manchukuo (MAN)
- Identity: Concessionary technocratic statecraft under asymmetric patronage.
- Signature spirit: **Concessionary Statecraft**.
- Best-fit paths: concession economy protection + regulated collaboration framework.

## D. Pacing and content spread improvements
- **Early game:** foundations, councils, patronage, grain/revenue institutions.
- **Midgame:** military-logistical development + strategy choice (survival/autonomy vs unifier vs accommodation).
- **Late game:** anti-bandit emergency zones, political guards, regulated collaboration, and a shared capstone asserting regional agency.
- Decision category provides repeatable interaction so actors do not go dormant between focuses.

## E. Character / institution additions
While no direct new portrait characters were added in this pass, institutional depth was expanded through:
- provincial councils,
- revenue and grain bureaus,
- local officer academies,
- frontier security bureaus,
- county reconstruction commissions,
- transport syndicate concessions,
- patronage reshuffle mechanics.

These represent the governing apparatus and factional machinery behind warlord regimes.

## F. Unification / diplomacy logic changes
The tree now explicitly supports divergent projects:
- **Back a unifier / bargain with one:** unification backchannel decision.
- **Become a unifier:** regional unification conference -> mandate -> command integration.
- **Resist unification:** local survival compact -> autonomy statute.
- **Collaborate selectively:** foreign accommodation channel -> concession/security protocol line.
- **Maintain strategic ambivalence:** capstone allows political continuity without immediate full annexation logic.

## G. Technical notes
- Added new focus file for China warlord tags and removed those tags from generic fallback selection list.
- Added new ideas and localization keys for identities and statecraft outcomes.
- Added warlord decision category and event IDs (300-303, 310-312) in the existing China event namespace.
- Kept all changes additive and integrated with current China rework files.

## H. Manual playtest recommendations
1. Start as each of GXC/YUN/SHX/XSM/SIK/MEN/MAN and verify exclusive strategic branch behavior.
2. Confirm each tag receives the correct identity spirit at `Doctrine of Regional Legitimacy` completion.
3. Test interaction with existing CHI/PRC rework (especially opinion modifiers and diplomacy timing).
4. AI observation run: ensure warlords complete at least one full strategic branch and use statecraft decisions periodically.
5. Stress test at war outbreak timing to confirm anti-bandit and command integration rewards remain balanced.
