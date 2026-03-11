# Faction Audit and Evolution Pass

## A. Executive summary

- **Total formal faction concepts audited:** 14 (`common/factions/AOTA_factions.txt` + `common/factions/AOTA_v13_factions.txt`) plus 2 previously ad-hoc faction strings now formalized (`AOTA_MITTELEUROPA_PACT`, `AOTA_EASTERN_ACCORD`).
- **Game-start formal factions discovered in mod-start scripts:** **0**. Current diplomatic architecture is largely latent and path-driven rather than pre-locked.
- **Factions acceptable as post-start formations:** Concert of Stability, Republican Security Pact, Danubian Compact, Charter of Restoration, Night Pact, Eastern Accord.
- **Factions likely too early if forced at game start:** all major formal blocs (especially Night Pact, Charter, Danubian, and Continental systems) because lore emphasizes unstable treaty scaffolding and unresolved legitimacy.
- **Factions recommended for delayed formation:** Continental Accord, Republican Security Pact, Danubian Compact, Mitteleuropa Pact, Eastern Accord (all now tied to focus/decision/event pathways).
- **Factions recommended for split/realignment support (design recommendation, partial implementation):** Continental Accord, Danubian Compact, Republican Security Pact, Night Pact vs Charter bipolarity.
- **Biggest lore concern:** informal pre-war alignments are strong in prose but under-mechanized in gameplay, causing diplomacy to feel under-reactive until hard faction creation moments.
- **Biggest gameplay concern:** several faction creation paths existed without built-in growth tooling, leaving blocs either single-tag placeholders or dependent on vanilla AI drift.

## B. Gamestart faction review

### Global finding
AOTA currently avoids hard formal bloc lock-in at day one in mod-authored setup files. This is lore-consistent with the setting's "unfinished peace" premise and supports early diplomatic ambiguity.

### Faction-by-faction game-start judgment

1. **AOTA_CONCERT_OF_STABILITY**  
   - **Current state:** not game-start; created later by ENG path.  
   - **Assessment:** correct to delay. Fits reconstruction diplomacy better as a response to crisis, not a pre-existing hard alliance.

2. **AOTA_CONTINENTAL_RECONCILIATION**  
   - **Current state:** defined identity; no direct formation script in audited files.  
   - **Assessment:** keep latent until tied to a specific negotiated turning point.

3. **AOTA_FREE_COMMUNES**  
   - **Current state:** defined identity; no direct formation script in audited files.  
   - **Assessment:** should emerge from revolutionary convergence, not start formalized.

4. **AOTA_LEAGUE_OF_FREE_MARKETS**  
   - **Current state:** defined identity; no direct formation script in audited files.  
   - **Assessment:** should remain path-dependent and post-crisis.

5. **AOTA_NIGHT_PACT**  
   - **Current state:** created by late-arc villain path eventing.  
   - **Assessment:** correctly delayed; should remain an escalation bloc.

6. **AOTA_CHARTER_OF_RESTORATION**  
   - **Current state:** created in ENG restoration branch.  
   - **Assessment:** correctly delayed and ideologically framed.

7. **AOTA_REPUBLICAN_SECURITY_PACT**  
   - **Current state:** decision-created (FRA democratic path).  
   - **Assessment:** good delayed concept; previously lacked growth scaffolding.

8. **AOTA_CONTINENTAL_ACCORD**  
   - **Current state:** decision-created (GER pathway).  
   - **Assessment:** should not be game-start; now strengthened as a staged growth bloc.

9. **AOTA_DANUBIAN_COMPACT**  
   - **Current state:** decision-created (AUS federal reconciliation).  
   - **Assessment:** correctly delayed; should be fragile and negotiation-driven.

10. **AOTA_RED_INTERNATIONAL**  
   - **Current state:** defined identity; no direct creation in audited pass files.  
   - **Assessment:** should remain contingent on transnational revolutionary success.

11. **AOTA_BLACK_CONCORD**  
   - **Current state:** defined identity; no direct creation in audited pass files.  
   - **Assessment:** best as emergent anti-state alignment.

12. **AOTA_ATLANTIC_MARKET_LEAGUE**  
   - **Current state:** defined identity; no direct creation in audited pass files.  
   - **Assessment:** should be post-crash maritime-economic coalition.

13. **AOTA_MITTELEUROPA_PACT** (new formal key)  
   - **Current state:** created by GER focus; now formalized as keyed faction identity.
   - **Assessment:** delayed timing is correct.

14. **AOTA_EASTERN_ACCORD** (new formal key)  
   - **Current state:** created by TUR event path; now formalized as keyed faction identity.
   - **Assessment:** delayed timing is correct.

## C. Faction creation recommendations

- **Continental Accord:** trigger via GER diplomatic conference/focus completion, then invite-wave decisions (implemented) to simulate conference-to-bloc transition.
- **Republican Security Pact:** trigger by democratic French path, then expansion through selective republican invite decisions (implemented).
- **Danubian Compact:** trigger only after internal settlement/reconciliation focus, then incremental invitations to avoid instant hard lock (implemented).
- **Eastern Accord:** keep as Ottoman-sponsored event outcome, with follow-up invitations to regional partners as crisis management matures into alliance structure (implemented).
- **Mitteleuropa Pact:** preserve as focus-gated German route; now converted to keyed faction identity for consistency and future dynamic naming support.

## D. Faction split/growth analysis

### Growth logic (implemented)
- Added a dedicated **Faction Evolution** decision category for leaders of key delayed blocs.
- Added AI-weighted invitation events so joining is probabilistic and ideology/opinion-sensitive rather than automatic.

### Split/fragment logic (design recommendation)
- **Continental Accord:** should fracture between constitutional-cooperative and coercive-security wings if founder radicalizes.
- **Danubian Compact:** should split between imperial reformists and hard national revisionists under severe legitimacy shocks.
- **Republican Security Pact:** should fragment if members drift to authoritarian anti-parliamentary paths.
- **Night Pact vs Charter system:** should pull swing states through pressure events rather than deterministic binary lock-in.

## E. Country alignment review

### Major powers
- **GER:** correctly starts uncommitted in formal bloc terms; should remain capable of either conference-order or hardline coercive alignment (supported).
- **FRA:** should remain a swing-shaper with republican, revolutionary, and reactionary external futures; democratic pact path now has clearer growth tooling.
- **ENG:** correctly positioned as delayed architect of restoration-oriented alignment; should continue to formalize late.
- **AUS/HUN/ROM/YUG space:** should remain unstable and conditional rather than hard pre-baked camp; compact expansion now incremental.
- **TUR and Near East neighbors:** should move from imperial influence network to optional formal bloc over time; Eastern Accord now has staged invitation support.
- **USA:** fragmentation-centric and not over-locked into prewar faction logic; preserve multi-successor diplomatic futures.
- **SOV/Russian project:** should remain path-reactive and potentially cross-cutting, not auto-locked to monolithic bloc behavior.

### Swing-state emphasis
- Belgium, Spain, Romania, Hungary, Iraq, and Egypt are better represented as invitees/conditional aligners than immutable game-start bloc members (implemented for invite-wave behavior in key paths).

## F. Technical implementation notes

### Files changed
1. `common/factions/AOTA_factions.txt`
   - Added formal faction definitions for `AOTA_MITTELEUROPA_PACT` and `AOTA_EASTERN_ACCORD`.
2. `common/decisions/AOTA_v13_decisions.txt`
   - Replaced string faction creation with keyed faction IDs.
   - Added faction-leader flags on creation for follow-up evolution logic.
3. `common/decisions/AOTA_faction_evolution_decisions.txt` (new)
   - Added post-formation invitation decisions for Continental, Danubian, Republican, and Eastern blocs.
4. `events/AOTA_faction_evolution_events.txt` (new)
   - Added acceptance/rejection event chain for invitations with ideology/opinion AI weighting.
5. `events/AOTA_TUR_events.txt`
   - Converted Eastern Accord to keyed faction creation and added leadership flag.
6. `common/national_focus/AOTA_GER.txt`
   - Converted Mitteleuropa creation to keyed faction ID.
7. `common/national_focus/AOTA_ENG.txt`
   - Converted Concert creation to keyed faction ID.
8. `localisation/english/AOTA_faction_evolution_l_english.yml` (new)
   - Added new faction names, decision names/descriptions, and event loc.

### Logic added
- Faction creation now emits leadership flags for subsequent evolution mechanics.
- Faction growth now proceeds through selective invitations with non-deterministic AI response.
- Faction naming consistency improved by moving ad hoc string-created blocs to keyed faction definitions.

## G. Manual review / playtest priorities

1. **Check no vanilla residual game-start faction carryover** in the active mod load order (especially if vanilla diplomacy history remains active).
2. **Observe AI uptake rates** for invitation events over 1936-1939 to ensure neither over-cohesion nor dead blocs.
3. **Test radical ideology pivots** in GER/FRA/AUS/TUR to confirm invite logic still feels plausible and not purely mechanical.
4. **Night Pact / Charter late-arc interactions** should receive dedicated counter-invite pressure events in future pass.
5. **Consider formal split events** once sufficient telemetry confirms where blocs currently over-stabilize.

---

## Audit conclusion

AOTA's core diplomatic direction is strong: formal blocs are generally delayed and aligned with narrative escalation. The main shortfall was not excessive game-start faction lock-in, but underdeveloped bloc maturation after creation. This pass addresses that by formalizing key faction identities, adding staged invitation mechanics, and introducing AI-reactive growth behavior while preserving existing worldbuilding architecture.
