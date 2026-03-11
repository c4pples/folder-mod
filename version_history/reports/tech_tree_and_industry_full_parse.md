# AOTA Full Tech Tree and Industry Parse

## A. Executive summary

- **Nations audited:** 41 country history entries in `history/countries/`.
- **Primary finding:** Several countries had no explicit starting technologies, and three had no explicit research slot value.
- **Tech profile status:**
  - Healthy/defined starts: core majors and key secondary powers (GER, SOV, ENG, FRA, ITA, JAP, TUR, AUS, CAN, RAJ, etc.).
  - Inconsistent/underdefined starts (fixed): ACC, ACG, ALG, ANA, APF, ASL, AWU, BEL, BUL, CCW, COG, FIN, GRE, HOL, HUN, IRE, LIT, POL, ROM, SER, UKR.
- **Industry profile status:**
  - Strong industrial cores remain concentrated in USA/GER/SOV/ENG/FRA/ITA/JAP.
  - Fragmented/contingent actors (American splinters, Serbia/Ukraine, colonial tags) intentionally have little or no start industry in owned states at scenario start.
- **World-level pacing concerns addressed:**
  1. "No-start-tech" countries causing AI and player dead-ends after release/collapse transitions.
  2. Missing research slot definitions in GRE/HUN/LIT causing incoherent progression pacing.
- **Biggest fixes applied:**
  - Added lore-safe baseline military/industrial starter tech packages to 21 underdefined countries.
  - Added explicit `set_research_slots = 2` to GRE, HUN, LIT.

---

## B. Nation-by-nation review

Legend:
- **Tech profile** = starting military/industry research readiness.
- **Industry profile** = owned-state starting factory footprint (civ/mil/dock).
- **Identity** = intended economic-industrial archetype.
- **Action** = fixed now / monitor.

### American fracture cluster

| Tag | Tech profile | Industry profile | Identity | Action |
|---|---|---|---|---|
| ACC | Previously empty; now baseline modern militia-state tech | 0/0/0 at start ownership | Constitutional successor in emergency mobilization | **Fixed:** baseline tech package added |
| ACG | Previously empty; now baseline with logistics support | 0/0/0 | Corporate-managerial successor | **Fixed:** baseline tech package added |
| ANA | Previously empty; now baseline army-led starter package | 0/0/0 | Authoritarian mobilization bloc | **Fixed:** baseline tech package added |
| APF | Previously empty; now baseline with truck logistics | 0/0/0 | Pacific federal-commercial successor | **Fixed:** baseline tech package added |
| ASL | Previously empty; now lighter agrarian package | 0/0/0 | Agrarian low-industrial regime | **Fixed:** reduced baseline tech package added |
| AWU | Previously empty; now baseline infantry/support package | 0/0/0 | Revolutionary workers coalition | **Fixed:** baseline tech package added |
| CCW | Previously empty; now modest low-mobilization baseline | 0/0/0 | Communal/Christian low-industrial polity | **Fixed:** light baseline tech package added |
| USA | Defined start, high industry, moderate military-tech emphasis | 174/12/35 | Huge civilian-industrial superstate with uneven militarization | Monitor (coherent for pacing) |

### European majors and powers

| Tag | Tech profile | Industry profile | Identity | Action |
|---|---|---|---|---|
| GER | Strong defined military-industrial base | 85/76/23 | Revanchist-industrial continental core | Monitor |
| SOV | Strong broad land-industrial baseline | 89/77/10 | Heavy continental war-industry state | Monitor |
| ENG | Strong defined mixed naval/industrial setup | 54/27/36 | Maritime-industrial empire core | Monitor |
| FRA | Strong defined but relatively brittle military scaling | 53/14/19 | Recovering continental-industrial state | Monitor |
| ITA | Strong defined mixed force profile | 41/43/25 | Mediterranean arsenal + fleet economy | Monitor |
| JAP | Highest specialization spread in starting tech package | 43/27/26 | Naval-air-industrial militarized power | Monitor |
| AUS | Strong central-European industrial start | 45/20/1 | Regional industrial core | Monitor |
| SPR | Defined start, middling industry | 16/7/4 | Recovering fractured Iberian state | Monitor |
| TUR | Defined broad baseline, moderate industry | 15/5/2 | Regional imperial reconsolidation power | Monitor |
| YUG | Defined start with lower industry depth | 7/3/0 | Fragment-prone regional state | Monitor |

### European minors / secondary states

| Tag | Tech profile | Industry profile | Identity | Action |
|---|---|---|---|---|
| BEL | Previously no explicit techs; now competent minor baseline | 13/6/0 | Dense trade-manufacturing secondary power | **Fixed:** baseline tech package added |
| BUL | Previously empty; now low-mid Balkan baseline | 11/3/0 | Agrarian-military transition state | **Fixed** |
| FIN | Previously empty; now doctrine-ready defensive baseline | 7/3/1 | Harsh-terrain defensive industrial minor | **Fixed** |
| GRE | Previously empty and no slots; now coherent baseline | 7/2/2 | Maritime-regional defensive state | **Fixed:** tech + slots |
| HOL | Previously empty; now coherent commercial-industrial baseline | 12/4/3 | Trade-shipping industrial node | **Fixed** |
| HUN | Previously empty and no slots; now coherent baseline | 4/2/0 | Revisionist inland rearmament minor | **Fixed:** tech + slots |
| IRE | Previously empty; now low-intensity baseline | 8/1/0 | Peripheral mixed economy | **Fixed** |
| LIT | Previously empty and no slots; now coherent baseline | 5/2/0 | Vulnerable frontier minor | **Fixed:** tech + slots |
| POL | Previously empty; now robust frontline baseline | 14/11/3 | Continental frontline industrial middle power | **Fixed** |
| POR | Already had coherent low-mid baseline | 12/2/3 | Maritime periphery with colonial links | Monitor |
| ROM | Previously empty; now extraction-military baseline | 6/4/2 | Oil-linked regional military economy | **Fixed** |
| SER | Previously empty; now coherent low baseline | 0/0/0 at start ownership | Fragmented/releasable Balkan reconstruction actor | **Fixed** |
| UKR | Previously empty; now coherent low baseline | 0/0/0 at start ownership | Potential agrarian-industrial frontier state | **Fixed** |

### Imperial / colonial / global minors

| Tag | Tech profile | Industry profile | Identity | Action |
|---|---|---|---|---|
| ALG | Previously empty; now low extraction-periphery baseline | 0/0/0 | Colonial/releasable peripheral economy | **Fixed** |
| COG | Previously empty; now low extraction baseline | 0/0/0 | Extractive concession economy | **Fixed** |
| EGY | Defined tech but no owned-state industry at scenario start | 0/0/0 | Occupied/constrained modernization case | Monitor |
| INS | Defined low baseline | 2/0/1 | Resource periphery under weak industrialization | Monitor |
| MAL | Defined low baseline | 1/0/0 | Rubber-tin export economy | Monitor |
| RAJ | Defined broad baseline with low military industry | 13/2/1 | Population-rich but industry-constrained subcontinental regime | Monitor |
| SAF | Defined low-mid baseline | 9/1/0 | Mining-export economy with thin armaments | Monitor |
| AST | Defined low-mid Commonwealth profile | 11/4/2 | Remote resource-industrial dominion | Monitor |
| NZL | Defined low baseline | 4/1/0 | Small agrarian-maritime dominion | Monitor |
| CAN | Defined mid baseline | 13/5/1 | Secondary industrial arsenal with growth potential | Monitor |

---

## C. Global tech spread review

- **Majors:** retain clear edge via broader start tech packages and stronger slot counts (mostly 4 slots).
- **Regional powers:** mixed 3-slot starts with narrower initial specialization.
- **Minors:** now consistently have minimum viable military-support tech baselines.
- **Weak/releasable states:** remain weak by industry and slots, but no longer mechanically incoherent from zero tech states.
- **Special cases:** American splinters remain contingent actors (no owned-state start industry), but can now research/produce coherently when activated.

## D. Global industrial spread review

- **Industrial cores:** USA, GER, SOV, ENG, FRA, ITA, JAP remain dominant.
- **Secondary cores:** AUS, POL, CAN, BEL/HOL as regionals.
- **Peripheries:** colonial/releasable tags remain low-industry by design.
- **Fractured states:** US splinters/SER/UKR intentionally scenario-contingent with low initial ownership footprints.
- **Specialization pattern:** naval concentration remains in ENG/USA/ITA/JAP/FRA; continental arsenal concentration in GER/SOV.

## E. Path-based differentiation review

- Existing focus trees already provide differentiated industrial/research trajectories (e.g., research-slot and tech-bonus nodes in many AOTA trees).
- This pass focused on startup coherence, not flattening path outcomes.
- Recommendation for future pass: expand path-conditioned industrial institutions for fracture/reconstruction tags once their map ownership and emergence triggers are finalized.

## F. AI and long-run campaign notes

- **AI gains from this pass:** former zero-tech countries can now produce and upgrade conventional force structures after appearance/release.
- **Still watch:** tags with 0 owned states at scenario start (ACC/ANA/etc., SER/UKR, ALG/COG/EGY) to confirm event-driven state assignment works in active campaigns.
- **Pacing risk reduced:** fewer AI dead starts and fewer tags that stall due to absent base military tech.

## G. Technical notes

### Files changed
- `history/countries/ACC - American Constitutional Coalition.txt`
- `history/countries/ACG - American Corporate Commonwealth.txt`
- `history/countries/ALG - Algeria.txt`
- `history/countries/ANA - American National Authority.txt`
- `history/countries/APF - Pacific Federation.txt`
- `history/countries/ASL - Southern Agrarian League.txt`
- `history/countries/AWU - American Workers Union.txt`
- `history/countries/BEL - Belgium.txt`
- `history/countries/BUL - Bulgaria.txt`
- `history/countries/CCW - Christian Commonwealth.txt`
- `history/countries/COG - Congo.txt`
- `history/countries/FIN - Finland.txt`
- `history/countries/GRE - Greece.txt`
- `history/countries/HOL - Netherlands.txt`
- `history/countries/HUN - Hungary.txt`
- `history/countries/IRE - Ireland.txt`
- `history/countries/LIT - Lithuania.txt`
- `history/countries/POL - Poland.txt`
- `history/countries/ROM - Romania.txt`
- `history/countries/SER - Serbia.txt`
- `history/countries/UKR - Ukraine.txt`

### Fix categories
- Added missing baseline `set_technology` blocks where absent.
- Added explicit research slots for GRE/HUN/LIT.
- Preserved all existing focus trees, spirits, and unique national identity hooks.

### Remaining edge cases for follow-up
- Tags with zero owned states at scenario load should be validated against event/spawn logic in active playthroughs.
- Consider future doctrine-specific start tech granularity for some non-major tags after campaign telemetry.

## H. Manual playtest recommendations

1. **American collapse scenario**
   - Trigger emergence of ACC/ANA/AWU/APF/ASL/ACG/CCW and verify they can research and produce infantry/artillery/support immediately.
2. **Balkan and Eastern Europe minors**
   - Observe GRE/HUN/LIT/POL/ROM for AI continuity through 1936–1940.
3. **Colonial/peripheral releasables**
   - Release ALG/COG/UKR/SER and confirm AI no longer deadlocks technologically.
4. **Pacing stress test**
   - Hands-off 10-year run: confirm majors maintain edge without minors being technologically inert.

