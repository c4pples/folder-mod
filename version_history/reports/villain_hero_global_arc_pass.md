# Villain vs Hope Global Arc Pass

## A. Executive summary
- **Primary villain country:** Germany (GER), via a new **Continental Directorate** extension on top of its existing hegemonic path.
- **Hidden secondary villain country:** Cuba (CUB), via a deepened **Ledger Republic** branch behind the existing secret ancap path.
- **Soft villain coalition:** **Night Pact** network (Germany-led, but designed to absorb opportunist major powers and client elites through decisions/events).
- **Main good guy country:** Britain (ENG), via a **Commonwealth Reconstruction Authority** extension to the reform path.
- **Thematic logic:** The mod already frames a world of armistice trauma, fragmented legitimacy, and institutional improvisation. This pass formalizes that into one visible systemic threat, one stranger secondary nightmare, one distributed ecosystem of enablers, and one costly but principled reconstruction alternative.

## B. Why each role was assigned

### 1) Germany as PRIMARY villain
- **Lore evidence:** The GER tree already contains a robust authoritarian-hegemonic axis (`GER_total_hegemonic_directive`) and security-state apparatus themes.
- **Geopolitical evidence:** Germany is structurally positioned to project power into central/eastern Europe and shape wider continental alignments.
- **Institutional evidence:** Existing content emphasizes general staff influence, cartel-state capacity, and covert networks.
- **Why not alternatives:** SOV and ENG both contain multi-directional paths including reconstruction options; GER's hegemonic route most cleanly supports a coherent principal antagonist with global consequences.

### 2) Cuba as HIDDEN secondary villain
- **Lore evidence:** CUB already has a secret ancap branch with extraterritorial contracts, boardroom rule, and private coercion.
- **Geopolitical evidence:** Caribbean chokepoints and exile/capital flows let Cuba punch above normal regional weight.
- **Institutional evidence:** Existing CUB ideas and focuses already model corporate capture.
- **Why not alternatives:** Other minors lack a similarly strong pre-existing “weird state form” to evolve into a distinct nightmare.

### 3) Night Pact as SOFT villain coalition
- **Lore evidence:** The setting repeatedly depicts elite bargaining, proxy coercion, and fragmented postwar order.
- **Geopolitical evidence:** An informal network better fits a fractured world than a monolithic alliance at game start.
- **Institutional evidence:** Decision/event mechanics now model policy convergence via security and finance protocols.
- **Why not a formal start-faction:** Soft-coalition emergence aligns better with the mod's tone of deniable influence and opportunistic alignment.

### 4) Britain as MAIN good path
- **Lore evidence:** ENG has an existing reformist constitutional/commonwealth pathway already framed around compromise and devolution.
- **Geopolitical evidence:** Britain can materially support allies while absorbing domestic tradeoffs, making it a plausible systemic counterweight.
- **Institutional evidence:** Parliamentary, naval, and imperial-administrative capacities are already represented.
- **Why not pure idealist alternatives:** ENG can credibly anchor “hard hope” (expensive, constrained, contested) instead of abstract moralism.

## C. Content added for each arc

### Primary villain (GER): Continental Directorate
- **Focuses added:** `GER_exception_decree_state`, `GER_security_directorate_cabinet`, `GER_tributary_industrial_zones`, `GER_frontier_loyalty_commands`, `GER_black_dossier_diplomacy`, `GER_night_pact_architecture`, `GER_continental_night_order`.
- **Events added:** `aota.5000`, `aota.5001`, plus global news linkage `aota.5005`.
- **Decisions added:** Germany can initiate coalition expansion via `AOTA_invite_to_night_pact`.
- **Spirits added:** `aota_ger_permanent_exception`, `aota_ger_tributary_industry`, `aota_ger_night_order`.
- **Characters/advisors:** Added `AOTA_GER_reinhard_gehlen` and recruited on path entry.
- **Name/cosmetic identity:** `GER_continental_directorate` cosmetic tag.
- **Narrative beats:** crisis normalization -> security cabinet consolidation -> extractive regionalization -> coercive diplomatic network -> systemic “night order.”

### Hidden secondary villain (CUB): Ledger Republic deepening
- **Focuses added:** `CUB_midnight_compliance_ledger`, `CUB_repossess_the_hemisphere` (gated behind existing secret branch capstone).
- **Events added:** `aota.5004` path transformation event.
- **Decisions added:** `AOTA_cub_export_compliance_battalions` in dedicated category.
- **Spirits added:** `aota_cub_ledger_state`, `aota_cub_debt_discipline`.
- **Characters/advisors:** Added `AOTA_CUB_julio_lobo` and recruited upon ledger transition.
- **Name/cosmetic identity:** `CUB_ledger_republic` cosmetic tag.
- **Narrative beats:** boardroom sovereignty -> full contract-enforcement regime -> debt militarization -> hemispheric repossession doctrine.

### Soft villain coalition: Night Pact
- **Faction identity support:** Added `AOTA_NIGHT_PACT` faction definition.
- **Events:** `aota.5001` proclamation, `aota.5002` invitation/acceptance logic.
- **Decisions/mechanics:** `AOTA_invite_to_night_pact`, `AOTA_night_pact_financial_protocol`, `AOTA_night_pact_security_protocol`.
- **Shared/mirrored spirits:** `aota_soft_villain_finance`, `aota_soft_villain_security_exchange`.
- **Policy convergence logic:** Member flagging (`AOTA_SOFT_VILLAIN_MEMBER`) enables recurring institutional alignment decisions.

### Main good path (ENG): Commonwealth Reconstruction Authority
- **Focuses added:** `ENG_ref_truth_and_reconstruction_congress`, `ENG_ref_reparative_budgeting`, `ENG_ref_citizens_relief_mission`, `ENG_ref_plural_oceanic_charter`, `ENG_ref_solidarity_convoys`, `ENG_ref_the_charter_of_restoration`, `ENG_ref_last_best_argument`.
- **Events added:** `aota.5003` path-defining congress event.
- **Decisions added:** `AOTA_hope_issue_sanctions`, `AOTA_hope_ship_reconstruction_aid`.
- **Spirits added:** `aota_eng_restoration_compact`, `aota_eng_hard_peace_dividend`, `aota_eng_solidarity_convoys`, `aota_hope_international_bastion`.
- **Characters/advisors:** Added `AOTA_ENG_ellen_wilkinson`, recruited at congress.
- **Name/cosmetic identity:** `ENG_commonwealth_reconstruction_authority` cosmetic tag.
- **Narrative beats:** truth/repair congress -> domestic sacrifice budget -> humanitarian logistics -> coalition diplomacy -> defended pluralist order.

## D. Interaction map
- **Main villain pressure:** GER’s new branch raises threat and can actively invite additional states into the Night Pact.
- **Soft coalition reinforcement:** Member states can repeatedly align through finance/security protocol decisions, deepening systemic danger beyond one tag.
- **Hidden villain divergence:** CUB’s ledger-state path is not territorial hegemony first; it is contractual-sovereignty predation and debt-militarized governance.
- **Good path counterplay:** ENG can sanction Night Pact members and pay domestic costs to sustain reconstruction aid, giving active strategic opposition.
- **Shared world framing:** News event `aota.5005` communicates the global ideological faultline once the villain architecture coheres.

## E. Technical integration notes
- **Focus files changed:** `common/national_focus/AOTA_GER.txt`, `common/national_focus/AOTA_ENG.txt`, `common/national_focus/AOTA_CUB.txt`.
- **New script files:**
  - `events/AOTA_v49_villain_hope_events.txt`
  - `common/decisions/AOTA_v49_villain_hope_decisions.txt`
  - `common/ideas/AOTA_v49_villain_hope_ideas.txt`
  - `common/characters/AOTA_v49_villain_hope_characters.txt`
  - `localisation/english/AOTA_v49_villain_hope_l_english.yml`
- **Supporting definitions updated:**
  - `common/factions/AOTA_factions.txt`
  - `common/cosmetic_tags/AOTA_cosmetic_tags.txt`
- **Validation focus:** avoided overwriting/removing existing paths; all additions are additive and wired via focus rewards/events/decisions.

## F. Manual follow-up recommendations
1. **Portrait/art pass:** new advisors currently use generic portraits.
2. **AI tuning:** observer tests should calibrate acceptance weights for `aota.5002` and decision usage frequency.
3. **Balance checks:** verify ENG aid decisions feel costly but worthwhile in long campaigns; ensure GER threat pacing is dangerous but not runaway by 1938.
4. **Flavor expansion:** add country-specific responses for FRA/SOV/USA to Night Pact growth and ENG reconstruction diplomacy.

---

## G. Pacing parity revision (post-review deepening)
Following review feedback, this pass was deepened to better match mature AOTA tree pacing and timing:

- **GER villain branch expanded from 7 to 16 focuses** with explicit late-phase institutionalization (occupation governance, extraction logistics, coalition secretariat, and capstone settlement framing).
- **ENG hope branch expanded from 7 to 16 focuses** with additional social-reform burdens, anti-oligarchy confrontation, sanctions doctrine, and late moral-strategic consolidation.
- **CUB hidden villain branch expanded from 2 to 8 late-stage focuses** with data-state, maritime-insurance coercion, and regional debtor-blacklist systems.
- Added **new decisions** for recurring coalition management and restoration responses, improving campaign persistence beyond one-off focus rewards.
- Added **new events** (`aota.5006`, `5007`, `5008`, `5009`, `5011`) to ensure phase transitions are narratively legible in-world.
- Added **additional spirits** to represent the cost structures of deeper paths (occupation machine, reconstruction levies, auctioned sea regime).

### Timing/pacing intent
- New additions stay on **10-cost late-tree timing** to avoid frontloading power spikes in 1936.
- Mechanical gains are paired with strategic/social costs (stability hits, consumer pressure, political power costs) to preserve AOTA's "earned outcomes" pacing.
- Coalition effects are now more looped and campaign-length, not just single unlocks.
