# 07 — Infrastructure and Catastrophe
### How Santiago's lifelines fail, how its catastrophes would unfold, and what a well-prepared group would actually need

> **Reference file for the DM.** Everything except Part D is meant as fact, projection or clearly flagged estimate. Compiled October 2026. Era I runs 2005–2025, Era II from 2025; items dated 2026 are marked so the DM can keep them out of a 2025 scene.

---

## How to read this file

**Confidence tags** (used throughout, per claim or per table row):

| Tag | Meaning |
|---|---|
| **[V]** | Verified during compilation against the source(s) listed in that section or in §Sources (press, official PDF, peer-reviewed abstract). |
| **[K]** | Standard fact from established references (Glasstone & Dolan, Kearny, Chilean statute texts, well-known events). The compiler is confident but did **not** re-open the primary source in this pass. Check exact figures before quoting them as gospel. |
| **[K~]** | As [K], but the compiler is less sure of the exact number. Treat it as approximately right. |
| **[M]** | Model projection from peer-reviewed studies. It is a projection, not an observation. |
| **[E]** | The compiler's own estimate or DM calibration, reasoned from the facts around it. It has no source. |
| **[?]** | Conflicting or unverified. Use it as a range or as an open question. |

**Compilation note.** During compilation, direct access to most Chilean official sites (bcn.cl, sec.cl, coordinador.cl, aguasandinas.cl, senapred.cl), to Wikipedia and to journal websites was blocked. Facts tagged [V] were checked through search retrieval of press reports, official PDFs and abstracts, plus PubMed. The search budget ran out before several checks could be made: the megadrought rainfall figures, the 2022 water-law details, the Diamante caldera, firearms-law ammunition caps, Swiss ventilation rates and bunker prices. Those passages carry [K], [K~] or [?] tags. See "Gaps" at the end.

### Quick reference: the numbers the DM will need most

| Item | Figure | Tag |
|---|---|---|
| Region Metropolitana population (Censo 2024) | 7,400,741, about 40% of Chile's 18,480,432 | [V] |
| Santiago's raw-water reserve against river turbidity | **~34 hours** since the Pirque ponds (about 2019–20); it was 9–11 h before | [V] |
| Turbidity-driven water cuts | 29 extreme episodes and 5 citywide suspensions in 2013–2017; 1.3 million customers cut in June 2023 | [V] |
| Mobile antenna battery autonomy required by law | **4 h** for "Nivel 2" sites (most users); up to 48 h for "Nivel 1" critical sites (DS 60/2012) | [V] |
| 25 Feb 2025 national blackout | Began 15:16; about 80% of the country's customers lost power; curfew 22:00–06:00; about 90% restored by the next morning; 207 detained; 3 deaths of electro-dependent patients investigated | [V] |
| Legal minimum fuel stock | 25 days of average sales per producer or importer (Ley 18.179, 1982) | [V] (whether and how it is enforced today: [?]) |
| Sonacol pipelines | 465 km; carry about **97%** of the liquid fuel sold in Santiago | [V] |
| Lo Valledor wholesale market | About **80%** of Santiago's fruit and vegetables, 50–60% of the national supply | [V] |
| Metro | 149.8 km, 7 lines, 26 comunas (2025); it **stops completely** without grid power | [V] |
| Fallout decay ("7-10 rule") | Each 7× increase in time cuts the dose rate 10×; two weeks after the burst it is about 1/1,000 of the H+1 level | [V] |
| Shielding against fallout gamma | About 9 cm of packed earth or about 6 cm of concrete halves the dose; about 90 cm of earth cuts it about 1,000× | [K] |
| Carabineros headcount | 56,509 total and 44,414 operational ("orden y seguridad"), April 2026 | [V] |
| Large-transformer lead time | 80–210 weeks (2024); 3–6 years for transmission-scale units | [V] |
| Drug shelf life (US SLEP) | 88% of lots tested still good at least 1 year past expiry; mean extension 66 months | [V] |

---

# PART A — Santiago's lifelines and how they break

## A.0 The city as a system

- **People.** The Región Metropolitana (RM) had 7,400,741 inhabitants in the 2024 census, against 7,112,808 in 2017. The comuna of Santiago (the historic centre) had 438,856. About 965,000 RM residents (13%) were born abroad. [V] The continuous built-up area, Gran Santiago, holds roughly 6.5–7 million people. [E]
- **Basin.** Santiago fills a tectonic valley at about 450–850 m. The ground slopes down from the Andean foothills in the east (Lo Barnechea, La Reina, Peñalolén, Puente Alto) to the west (Maipú, Pudahuel). Andean summits of 5–6 km stand within 50–80 km to the east, and the Coastal Range closes the basin to the west. [K] The Mapocho river crosses the centre; the larger Maipo runs along the south edge. [K]
- **Ground.** Most of the city stands on thick river gravels (the "grava de Santiago"). They are excellent foundation soil, easy to excavate and seismically well behaved. In the north-west there are softer fine-grained soils and ash deposits. [K]
- **Air.** A subsidence inversion tied to the South Pacific anticyclone sits over the basin all year, with its base about 1,000 m above the surface. In winter, surface radiative inversions are added to it. The basin ventilates poorly, which is why Santiago has winter smog episodes. [V] Anything burned or released inside the basin (city fires, generator exhaust, industrial chemicals, volcanic ash) tends to stay, especially from May to August. [E]
- **Implication for play.** Gravity is Santiago's friend: water flows west from the eastern plants on its own. Its enemies are the cordillera's mudflows, a single fuel corridor from the coast, a grid that depends on long north–south lines, and a population in which almost no one keeps more than a few days of supplies. [E]

---

## A.1 Water

### Who and what

| Element | Facts | Tag |
|---|---|---|
| Operator | **Aguas Andinas**, together with its sister companies Aguas Cordillera and Aguas Manquehue, serves most of Gran Santiago. A few comunas have their own systems; the best known is SMAPA, the municipal operator of Maipú. Regulator: **SISS** (Superintendencia de Servicios Sanitarios). Controlling shareholder: the Agbar/Suez group, now Veolia, through IAM. | [K~] |
| Main source | The **Maipo river** supplies the bulk of the city's surface water; the Mapocho and its tributaries supply the north-east. | [K] |
| Reservoir | **Embalse El Yeso** in the upper Cajón del Maipo. Capacity is given as 220 or 256 million m³ depending on the source; the usable reserve is about 200 Mm³, roughly one-third of the surface water Aguas Andinas can use. It held 215 Mm³ in 2016 and fell to about 60 Mm³ during the drought. | [V] |
| High-Andean lakes | Laguna Negra and Lo Encañado are additional regulated reserves. | [K] |
| Treatment | The **Complejo Las Vizcachas** (Puente Alto) is the main plant, followed by the **La Florida** plant and smaller ones. All the large plants sit on the eastern and south-eastern edge, upslope of the city. | [K] |
| Emergency raw-water storage | **Estanques de Pirque**: six ponds holding 1.5 million m³ of raw water, about US$120 million. They raised the city's autonomy during turbidity events from about 9–11 h to **~34 h**. | [V] |
| Next step | The El Manzano–Pique catchment aims at **48 h** of autonomy. It was announced for 2024, but one source still had it at design stage, so its status is [?]. | [V]/[?] |
| Wastewater | Since about 2012 essentially all of Santiago's sewage has been treated at the La Farfana and Mapocho-Trebal plants, which Aguas Andinas brands "Biofactorías". | [K] |
| Scale | 1.5 Mm³ lasting 34 h implies a draw of roughly 12 m³/s, which gives the order of magnitude of the city's demand. | [E] |

### How it breaks: turbidity ("turbiedad")

The classic failure has nothing to do with a shortage of water. Warm winter or summer storms arrive with a **high freezing level ("isoterma 0 alta")**, so rain instead of snow falls on bare Andean slopes. That triggers **mudflows ("aluviones")** into the Maipo, and the river's turbidity rises beyond what the plants can treat. Aguas Andinas then stops intake and lives off stored water until the river clears. [K]

| Episode | What happened | Tag |
|---|---|---|
| Jan 2013 | Citywide cut caused by turbidity. Intendente Orrego later called it the first of three in three years. | [V] |
| Apr 2016 | Massive cut. Press reports spoke of "more than four million people" without water. | [V]/[?] (counting method unclear) |
| 25–26 Feb 2017 | Aguas Andinas announced a cut for the **30 comunas** of Gran Santiago in the small hours, hours after saying no massive cuts were planned. SISS fined the company about CLP 797 million for emergency-management failings (the press does not make clear which event the fine covers). | [V] |
| 2013–2017 overall | **29 episodes of extreme turbidity, 5 citywide suspensions** | [V] |
| 23 Jun 2023 | Heavy rain. The Pirque ponds were brought into use and authorities first spoke of about 36 h of autonomy. When turbidity persisted, autonomy fell by about 50% and service was suspended to **1,304,857 customers in 34 comunas**. The river flow had a return period of about 20–25 years. | [V] |

**Lessons for the DM**
- Even with the ponds, Santiago's water buffer against a river problem is about **one and a half days**. [V]
- Cuts are announced with only hours of warning. Supermarkets sell out of bottled water within those hours. [E] (consistent with press accounts of each episode)
- The 2023 event shows that the reserve is not drawn evenly: the operator protects the reserve by cutting some sectors early. [V]/[E]

### How it breaks: power, pressure, high-rises

- **Gravity helps.** Because the plants sit upslope, much of the network keeps flowing for a while even if pumps stop. [E]
- **Pumping is still needed** for the high eastern zones (Lo Barnechea, upper Las Condes, Peñalolén alto), for the wells, and for every building taller than about 4–6 floors. Towers pump water to roof tanks. In a blackout, upper floors lose water when the roof tank empties, usually within **hours to a day**. Many towers have small generators for lifts and pumps, with a few hours of fuel. [E]
- **Sewage lift stations** need power too. Low-lying western areas and any below-grade space (basements, bunkers) are at risk of backflow. [E]
- No public account confirms how the water system behaved during the 25 Feb 2025 blackout. Assume service largely continued in gravity-fed areas, with pressure lost in high zones and towers. [?]/[E]

### Groundwater and water law

- **Aquifer.** The Santiago basin sits on productive alluvial aquifers. Aguas Andinas runs wells as a strategic backup, and much of the basin is a declared restriction or prohibition area for new extraction (the DGA's "áreas de restricción/prohibición"). [K~]
- **Water rights** ("derechos de aprovechamiento de aguas"): rights to use water, granted by the **DGA** (Dirección General de Aguas). Under the 1981 **Código de Aguas** they were granted free, in perpetuity, and could be traded separately from land. [K]
- **2022 reform (Ley 21.435).** Water was reaffirmed as a "bien nacional de uso público" (public good). **New** rights are temporary, for 30 years and renewable. Human consumption and sanitation have priority, and unused rights can lapse. [K~]
- **Domestic wells.** The Code has long allowed anyone to dig a well **on their own land** for drinking and domestic use ("bebida y usos domésticos"). That is the legal basis for a household or building well. Registration and flow conditions were tightened after 2022; check the current article 56 and its regulations. [K]/[?]
- **Megadrought ("megasequía").** Central Chile has had a run of dry years since about 2010, documented by the CR2 climate centre. 2019 was exceptionally dry in Santiago. In April 2022 the regional authorities published a drought **rationing protocol** with escalating alert levels and rotating cuts by sector, which was never fully triggered. See B.6. [K~]

---

## A.2 Power

### The grid

| Element | Facts | Tag |
|---|---|---|
| System | **SEN** (Sistema Eléctrico Nacional), formed in **Nov 2017** when the central SIC and the northern SING were joined. It runs about 3,000 km from Arica to Chiloé; Aysén and Magallanes have separate small systems. Operator: **Coordinador Eléctrico Nacional (CEN)**. Regulators: **CNE** for tariffs and planning, **SEC** for enforcement. | [K] |
| Backbone | 500 kV lines run north–south, increasingly carrying northern solar power south to the Santiago load centre. The **HVDC Kimal–Lo Aguirre** link (±600 kV, about 1,342 km, up to 3,000 MW, ending at Lo Aguirre on Santiago's western edge) won environmental approval in Nov 2025 and started construction in **Feb 2026**. It is expected around 2029–30, so it is not available in 2025. | [V] |
| Santiago's main nodes | Polpaico to the north, Lo Aguirre to the west, Alto Jahuel to the south, plus 220 kV substations ringing the city. | [K~] |
| Nearby generation | Maipo hydro plants in the Cajón del Maipo (Alfalfal, Queltehues, Volcán, Maitenes), **Alto Maipo** (531 MW, in service about 2022), the Renca/Nueva Renca gas plant, and the gas plants at Quintero and Quillota. | [K~] |
| Distribution | **Enel Distribución Chile** serves about 2 million customers in roughly 33 comunas (most of the city). **CGE** and smaller companies serve the rest. | [K~] |

### Documented failures

| Date | Event | Tag |
|---|---|---|
| 27 Feb 2010 (27F) | The Mw 8.8 earthquake brought down most of the central grid. Santiago was largely restored within roughly a day, with pockets lasting longer; the south-central regions took days to weeks. | [K~] |
| 14 Mar 2010 | A second SIC-wide blackout, from a transformer failure in the south, while the system was still fragile after 27F. | [K~] |
| 24 Sep 2011 | SIC blackout caused by a fault at Ancoa substation; millions of people lost power for a few hours. | [K~] |
| 15 Jul 2017 | Snowfall in Santiago broke trees and lines. Hundreds of thousands of customers lost power, some for several days. | [K~] |
| 1–2 Aug 2024 | Windstorm with gusts of up to 124 km/h according to Enel. About **700,000 Enel customers** lost power (SEC figure), with a national peak of **1,243,904 customers** on 2 Aug. **Some outages lasted more than two weeks.** SEC classed the cause as internal and fined Enel **280,000 UTM** (about CLP 18.8 billion). Enel paid voluntary compensation to about 800,000 customers. A concession-revocation process was opened and then closed in 2026 without revocation. | [V] |
| **25 Feb 2025** | **National blackout.** Details below. | [V] |
| Sep 2026 | A distribution failure cut power to about 120–130,000 RM customers and **interrupted Metro service**. Outside Era II's start; mentioned for continuity. | [V] (headline only) |

### The 25 February 2025 blackout ("25F"): the best template for any grid-down scene

| Aspect | What happened | Tag |
|---|---|---|
| Trigger | At **15:16** the Nueva Maitencillo–Nueva Pan de Azúcar 2×500 kV line, owned by ISA Interchile and carrying about 1,800 MW between Vallenar and Coquimbo, was disconnected by an "unwanted operation" of its protection and control systems. Press reports say both the main and the backup protection systems misoperated. CEN's failure analysis, about 400 pages long, found that Interchile staff had restarted a communications module and tried to resynchronise the protection **without telling the CEN**, contrary to the manufacturer's procedures. The Cardones–Polpaico 2×500 kV link also tripped, and the system collapsed. | [V] |
| Extent | From **Arica to Los Lagos**. SEC: **~80% of customers** affected (press figures ranged from 80% to 95%). Enel reported about 905,000 of its customers affected; CGE about 3.2 million. | [V] |
| Restoration | By 22:00 only **about a quarter** of demand was back. About 8 hours after the failure, 4.15 million homes had power, a little under half of those affected. By the next morning about **90%** was restored, and the centre-south was fully restored from Valparaíso to Chiloé. | [V] |
| Government | **Estado de excepción constitucional de catástrofe** (constitutional state of catastrophe) and a **curfew from 22:00 to 06:00** in every region from Arica to Los Lagos. The government ruled out an attack. | [V] |
| Order | **207 people detained** nationally during the curfew night. The Interior Minister called the figure low and said most people complied. Drivers were warned that **traffic lights** were out. | [V] |
| Health | **Three deaths of electro-dependent people** (home ventilators or oxygen concentrators) were investigated. | [V] |
| Metro | Trains were **evacuated** and stations closed until power returned. | [V] |
| Mobile networks | About 1% of the network was down 1–2 h after the failure, though with heavy congestion. At **4 h, 10%** was down, as Nivel 2 antennas' batteries ran out. The peak was **23% down at about 23:00**. Recharging batteries and refuelling generators in the dark was difficult. | [V] |
| Aftermath | An academic panel working for the CEN blamed structural weaknesses in the system, **unjustified disconnections of generators**, regulatory non-compliance by companies and omissions by the CEN itself. CEN audited Interchile; the same line failed again on 16 Jun 2025. A congressional investigative commission was set up. | [V] |

**Key point for the DM.** 25F was a *best case*. It happened on a summer afternoon, the hydro plants were intact for black-start, there was no physical damage and the telecom network held for about four hours. Even so, restoring the country took 8–16 hours. Any scenario with **physical damage** to transformers or lines (earthquake, solar storm, sabotage) stretches that to days or weeks. [E]

### Hospitals and the electro-dependent

- **Generator autonomy.** No published Chilean rule (MINSAL or Superintendencia de Salud) setting a minimum number of hours of on-site fuel for hospitals could be found. The accreditation standards require emergency power systems and their testing. [V: none found] / [K~]
- **Realistic range.** On-site tanks typically hold **24–72 hours** at load; after that, everything depends on diesel trucks reaching the hospital through dark, gridlocked streets. [E] For comparison, US hospital emergency-management standards plan around a **96-hour** self-sufficiency horizon. [K]
- **Electro-dependent patients.** A law from about 2021 (Ley 21.304) obliges distribution companies to keep a register of these patients and to provide backup arrangements. 25F showed the gap between the law and reality. [K~]/[V for the deaths]
- **Game implication.** A small emergency-medicine network with its own generators, fuel and oxygen concentrators becomes, within 6–12 hours of any blackout, a magnet for patients on home oxygen and ventilators. [E]

---

## A.3 Fuel and gas

### Oil: an import economy with one corridor into the capital

| Element | Facts | Tag |
|---|---|---|
| Crude | Chile produces almost no oil of its own (only small amounts in Magallanes) and **imports nearly all its crude**. | [K] |
| ENAP | The state company supplies about **60%** of national hydrocarbon demand, combining its own refining with imports: about 90% of gasoline, about 40% of diesel and about 70% of jet fuel (2026 statement). Distributors (Copec, Enex, Esmax and others) **import, store and deliver the remaining ~40% directly**. | [V] |
| Refineries | **Aconcagua** (Concón, opened 1955): **102,000 bbl/day**; with the Quintero marine terminal it supplies most of the centre-north. **Bío Bío** (Hualpén, near Concepción): **116,000 bbl/day**. **Gregorio** (Magallanes): about 17,600 bbl/day. | [V] |
| Pipeline into Santiago | **Sonacol** (Sociedad Nacional de Oleoductos): a **465 km** network in the Valparaíso, O'Higgins and Metropolitana regions, carrying about **97% of liquid fuels sold in the capital**. Shareholders include Copec, Esmax, Enex, Abastible and ENAP. Its core line runs **Concón to the Maipú terminal** in western Santiago; a 134 km Concón–Maipú LPG pipeline is also recorded. A new 26–27 km pipeline from Maipú to the airport was approved in 2019 against local opposition; whether it was built is [?]. | [V] |
| Legal stock | Ley 18.179 (1982) requires each producer or importer to hold average stocks of each product equal to **25 days of its average sales** over the previous six months. | [V] (current enforcement: [?]) |
| Physical reality in Santiago | The 25-day stock sits mostly at **coastal terminals and refineries**, not in the city. Santiago itself holds the Maipú terminal plus service-station tanks, probably **a few days** of normal consumption. Most service stations **cannot pump without grid power**. | [E] |
| 27F precedent | The Bío Bío refinery was damaged and shut for weeks, and the south suffered fuel shortages. | [K~] |

**Failure modes, in order of likelihood:** a blackout (pumps stop) → a Concón–Maipú pipeline break or Sonacol control failure (earthquake, sabotage) → a port or terminal shutdown at Quintero (tsunami, storm swell, strike) → a global supply shock (war, sanctions), against which Chile has about 3–4 weeks of total national stock if the 25-day rule is met. [E]

### Natural gas and LPG

- **The Argentine gas crisis (2004–2008).** In the late 1990s Chile built gas power plants and Santiago's residential gas network on cheap Argentine pipeline gas. From **2004** Argentina restricted exports to protect its own consumption; the cuts worsened in **2007**. Gas plants switched to diesel, which raised power costs and pollution. [V]
- **Response.** In **June 2007** 20-year LNG supply contracts were signed for the central zone, to start in the second half of 2009. **GNL Quintero** (about US$1.1–1.3 billion; financial close June 2008) received its first cargo in mid-2009: the ship left Trinidad on 8 June 2009 carrying about 145,000 m³ of LNG. **GNL Mejillones** in the north followed around 2010. [V]/[K for Mejillones]
- **2025 echo.** In **July 2025** Argentina again interrupted exports during a cold wave. Chilean customers with interruptible contracts were curtailed while Quintero carried the load. [V]
- **Households.** Metrogas distributes natural gas in Santiago. A large share of households cook with **LPG cylinders ("balón de gas")** of 5, 11, 15 or 45 kg from Abastible, Gasco or Lipigas, and many heat with **kerosene ("parafina")** stoves in winter. [K] In a long crisis these cylinders become currency. [E]

---

## A.4 Food

| Element | Facts | Tag |
|---|---|---|
| **Lo Valledor** (Pedro Aguirre Cerda) | The giant wholesale market. In 2026 the Agriculture Minister put its share at **about 80% of Santiago's fruit and vegetables and 50–60% nationally**. A press account describes **2.5 million tonnes a year** (about 6,800 t/day on average [E]), 33 ha, about 1,500 stalls, **30,000+ people and 7,000 vehicles a day**. It works through the night; trucks arrive from the Central Valley around 01:00–05:00. | [V] |
| **La Vega Central** (Recoleta) | The historic market north of the Mapocho (19th century), part wholesale and part retail. In 2020 its spokesman said that as long as Lo Valledor, La Vega and the "ferias libres" (street markets) stayed open, Santiago would not go short. | [V]/[K] |
| Ferias libres | Hundreds of weekly street markets supplied from Lo Valledor, which serve poorer comunas. | [K] |
| Supermarkets | Walmart Chile (Líder, Acuenta, Central Mayorista), Cencosud (Jumbo, Santa Isabel), SMU (Unimarc, Alvi), Tottus (Falabella). Large distribution centres sit on the north-western and western periphery near the motorways (Quilicura, Pudahuel, Lo Aguirre). | [K~] |
| Imports | Chile is a big **exporter** of fruit, salmon and wine but a **net importer of staples**: a large share of its wheat, most feed maize, much of its rice, and most vegetable oils and soy meal. | [K~] |
| Ports | **San Antonio** (Chile's largest container port, linked to Santiago by Ruta 78) and **Valparaíso** (Ruta 68). | [K] |

**How many days of food does Santiago hold?** No official figure exists. [V: none found] As an estimate: shelves hold about **2–4 days** of fast-moving staples under normal demand, and panic buying empties them in **hours**. Distribution centres hold another few days. Households typically have **3–7 days** of food, but little water. Lo Valledor turns over daily, so if trucks stop for 48–72 hours, fresh produce collapses. [E]

**Documented panic buying and looting**
- **27F 2010, Concepción.** After 1–2 days with no communications, no power, no water and no visible authority, crowds looted supermarkets (including Líder stores), pharmacies and shops; some stores were burned. Neighbourhoods formed **armed self-defence barricades** against rumoured looters. The government declared a state of catastrophe and imposed a curfew, and **160 people were detained the first night**. [V for looting, curfew and detentions; K for the barricades]
- **Estallido, Oct 2019.** Supermarkets were looted and burned in Santiago and other cities during the first nights. One Fiscalía (prosecutors') dataset recorded 33 cases filed as "saqueo" within 11,156 property crimes for the period it covered; reporting categories understate the visible damage. [V]/[?]
- **COVID, March 2020.** Supermarkets were the **only** retail line to grow in March (+6% year on year, while in-person retail in the RM fell 19.9%). Demand surged in two waves, first from fear of renewed violence and then from fear of closures. Panic buying rose by about 14% in the week a quarantine of much of the RM was announced. [V]
- **Truckers' strikes ("paros de camioneros").** The 1972 strike against Allende, and later strikes in the 2010s–2020s, show that Santiago is three highways away from hunger. [K]

---

## A.5 Communications

### Mobile and fixed networks

- **27F 2010.** Mobile and fixed networks collapsed, first from congestion and then from loss of power. Radio broadcasting (AM and FM, battery sets) was for many people the only source of news for a day or more. The tsunami warning chain also failed. [K]
- **Ley 20.478 (2010).** After 27F, Congress passed this law on the recovery and continuity of public telecommunications in critical conditions. Its regulation, **DS 60/2012**, classifies sites by criticality and requires backup power of **up to 48 h for Nivel 1 sites and at least 4 h for Nivel 2 sites**, which serve most users. [V]
- **25F 2025** proved the 4-hour rule: 10% of the network was down at 4 h and 23% by about 23:00 (see A.2). In 2025 Subtel was processing a decree raising the Nivel 2 minimum to **6 h**. Whether it was issued is [?]. In Oct 2026 Subtel was still citing 4 h and 48 h. [V]
- **Cell broadcast.** SAE (Sistema de Alerta de Emergencia) pushes alerts to phones. It needs live towers. [K]
- **Fibre and data.** Fibre nodes and street cabinets need power, and home routers die with the grid. International connectivity relies on submarine cables landing on the central coast, including Google's **Curie** cable to Valparaíso (2019). [K~] **Starlink** has been available in Chile since about 2021. In a grid-down scene, a Starlink dish plus a battery or generator is the most capable civilian link, provided the satellites and ground stations are working. [K~]/[E]
- **Antenna sites.** Cerro San Cristóbal and other hills carry broadcast and repeater antennas, which makes them important places in any comms scene. [K~]

### Radio

- **Radio amateurs.** The **Radio Club de Chile** (callsign CE3AA, founded 1922, based in Santiago) had more than 1,500 direct members plus 22 member clubs in 2010. It documented its role in the 27F response. Licences are issued by **Subtel** in categories that in 2010 were Aspirante, Novicio, General and Superior, and are valid for **5 years**. [V] The total number of licensed amateurs is not confirmed; a few thousand active is a fair estimate. [E]
- **Practical HF and VHF.** HF (for example the 40 m and 80 m bands) covers the country at night and needs no infrastructure. VHF and UHF repeaters on the hills give city coverage but need power at the site. A prepared group wants HF transceivers, antennas, batteries and a licensed operator. [K]/[E]
- **Emergency services.** Carabineros, Bomberos and SAMU run their own VHF/UHF and digital networks with hilltop repeaters. They outlast the mobile network but are not built for weeks without power, and repeater sites run on batteries and small generators. [E] Bomberos de Chile are **volunteer** fire brigades; the Santiago brigade was founded in 1863. [K]

---

## A.6 Transport

| Mode | Facts and fragility | Tag |
|---|---|---|
| **Metro de Santiago** | 149.8 km, **7 lines**, 26 comunas (2025); Lines 7, 8 and 9 are under construction (L7 about 2028). It carried about 660 million passengers a year in 2015. **Fully dependent on grid power**: on 25F all trains were evacuated. **2019:** of 136 stations, **118 were damaged**; **7 burned out, 18 partly burned**, 93 suffered other damage and only 18 were untouched; 10 trains were destroyed or badly vandalised. Reconstruction cost **US$255 million** and took about **11 months**. | [V] |
| Buses ("Red") | One of the largest **electric bus fleets** outside China. This is an advance for air quality and a new grid dependence, since charging depots need power. | [K~]/[E] |
| Roads | Ruta 5 (north–south), **Ruta 68** (Valparaíso/Viña), **Ruta 78** (San Antonio port), **Ruta 57** to Los Andes and the **Cristo Redentor / Los Libertadores pass** to Mendoza, which **closes for days at a time in winter snow**. Santiago's urban motorways ("autopistas concesionadas") are tolled electronically by TAG. On 27F the Ruta 5 Sur was cut at four points and urban overpasses collapsed in Santiago. | [V for Ruta 5 cuts]/[K] |
| Airport | **Arturo Merino Benítez (AMB)** at Pudahuel. On 27F it was **closed for at least 24 hours** after the passenger terminal structure partly collapsed. International departures resumed about a week later, with check-in in **tents** and only a few boarding bridges working. Fuel tanks were also damaged. | [V] |
| Rail | EFE runs passenger services to Chillán and suburban trains (Metrotren Nos, 2017); freight is limited. Rail is marginal for feeding Santiago. | [K~] |
| Traffic lights | They fail in a blackout, causing **gridlock** within an hour at rush hour. Ambulances and fuel trucks get stuck. | [V for the 25F warnings]/[E] |

---

## A.7 Health system notes (for an emergency-medicine protagonist)

- **Ley de Urgencia (Ley 19.650, 1999).** Health providers may not demand a cheque or guarantee before treating a life-threatening emergency. [K] This matters to a private emergency network: in a crisis it will be legally and morally obliged to treat whoever comes through the door. [E]
- **SAMU** (public ambulance service, telephone **131**). Public urgent-care points include the SAPU, SAR and SUAPS, plus hospital emergency departments. The trauma reference hospital is the **Hospital de Urgencia Asistencia Pública (HUAP, the "Posta Central")** in the city centre. [K]
- The public network is organised into six **Servicios de Salud** for the RM (Norte, Sur, Oriente, Occidente, Central, Sur-Oriente). The big private clinics (Alemana, Las Condes, Santa María, Indisa, the UC Christus network) are concentrated in the east and north-east. [K]
- **COVID precedent.** Central management of ICU beds across public and private hospitals, aeromedical transfers between regions, and a rapid expansion of critical beds. Hospitals saturated twice, in mid-2020 and in April–June 2021. [K~]
- **Hidden dependencies.** Medical oxygen (from Linde/Indura and Air Liquide air-separation plants, delivered by truck), dialysis (power plus large volumes of treated water), sterilisation, the blood bank, the cold chain and laboratory reagents. In any long outage, **dialysis patients** are the first mass casualty group after the electro-dependent. [K]/[E]

---

## A.8 Social order

### What actually happened in four crises

| Crisis | Order and disorder | Tag |
|---|---|---|
| **27F 2010** (Mw 8.8, 03:34) | 521 dead and 56 missing according to Memoria Chilena; early counts were higher. Looting in Concepción on days 1–3. **Estado de catástrofe** in Maule and Biobío, and the **first curfew since the dictatorship**: at first from 21:00, later from 18:00 to 12:00. About 7,000 troops were deployed at first, growing to between 13,000 and 23,000 within the month, depending on the source. The government was criticised for deploying the military late. | [V]/[K for the criticism] |
| **Estallido, 18 Oct 2019 onward** | Fare-evasion protests escalated into riots, arson of Metro stations and looting. A **state of emergency and nightly curfews** in Santiago followed for about the first week and a half. About 30 people died. Hundreds suffered eye injuries from police pellets. The Libertad y Desarrollo think tank estimated the economic cost of the first month at more than **US$6.3 billion**. | [V for Metro and LyD]/[K~ for curfew dates, deaths and eye injuries] |
| **COVID 2020–21** | **Estado de catástrofe from 18 Mar 2020**; a **national night curfew from 22 Mar 2020 to 30 Sep 2021**, about 18 months and among the longest in the Americas. Quarantines were imposed comuna by comuna and movement permits were issued online through the "Comisaría Virtual". | [V]/[K] |
| **25F 2025 blackout** | State of catastrophe and a one-night curfew in 15 regions; **207 detained**; compliance was broadly good. | [V] |

**Patterns the DM can rely on** [E, drawn from the above]
1. In Chile **the state reacts with states of exception, curfews and soldiers**, usually within **6–48 hours**. The legal machinery is well practised.
2. **Looting comes when four things fail at once**: communications, power, supply and visible police. That was Concepción in 2010. With only one or two of them failing, as on 25F, people mostly stay home.
3. **Neighbourhood self-organisation** appears fast: barricades, vigilante patrols in yellow vests (Santiago 2019), shared generators, ollas comunes (community soup kitchens, a Chilean tradition revived in 2020). [K]
4. Disorder is **geographically uneven**. The poorer periphery suffers both looting and police neglect; the wealthy east hires private security.

### States of exception (Constitution, arts. 39–45; Ley Orgánica 18.415)

| State | Trigger | Declared by and duration | What can be restricted | Tag |
|---|---|---|---|---|
| **Estado de asamblea** | External war | President with Congress approval; lasts while the war situation does | Personal liberty, assembly, freedom of work, association; interception of communications; requisition of goods; limits on property | [K] |
| **Estado de sitio** | Internal war or grave internal upheaval ("grave conmoción interior") | President with Congress approval; **15 days**, extendable | Freedom of movement; house arrest or detention in places that are not prisons; assembly | [K] |
| **Estado de catástrofe** | Public calamity | **President alone**, who must inform Congress. Congress may annul it after **180 days** if its causes have entirely ceased; beyond **1 year** it needs Congress's agreement. The zone is placed under a military **Jefe de la Defensa Nacional**. | Freedom of movement and assembly; **requisition of goods**; limits on property; administrative measures, **including curfews** | [K] |
| **Estado de emergencia** | Grave disturbance of public order or danger to national security | President; **15 days**, extendable once, after which Congress's agreement is needed. Also under a Jefe de la Defensa Nacional. | Freedom of movement and assembly | [K] |

- **Ley 21.542 (3 Feb 2023)**, a constitutional reform, lets the President deploy the armed forces to **protect critical infrastructure** by decree **without** declaring a state of exception, for up to **90 days**, extendable with Congress. [V] In an Era II catastrophe, soldiers would guard water plants, substations, the Maipú fuel terminal and hospitals early. [E]
- **Requisition** under catastrophe is the legal tool the state would use against a private stockpile: generators, fuel, medical supplies and vehicles. A bunker owner's greatest legal risk in a declared catastrophe is to be **requisitioned, not raided**. [K]/[E]

### Forces

| Force | Size | Tag |
|---|---|---|
| **Carabineros** (national uniformed police, under the Interior/Security ministry) | **56,509** total in April 2026 (59,894 in 2019); **44,414** in "orden y seguridad"; 12,222 authorised posts unfilled. Numbers are falling by about 1,000 a year. | [V] |
| **PDI** (Policía de Investigaciones, the detective police) | About 12,000–13,000 | [K~] |
| Army | About 35,000–45,000 active, including conscripts; Navy and Air Force on top | [K~] |
| Ratio | About **1 operational carabinero per 400–420 inhabitants** nationally, and far fewer actually on the street at any given hour | [E] |

---

## A.9 The cascade clock: Santiago with the grid down

Assume a total blackout of the RM, with no physical damage to the city itself. Hours 0–16 are calibrated on 25F; everything beyond is extrapolation. **[E]** unless tagged.

| Time | What fails or happens |
|---|---|
| **0–15 min** | Metro trains stop and are evacuated [V]. Traffic lights go dark. Lifts trap people. Hospitals switch to generators (5–15 s for critical circuits). Card terminals and ATMs fail, so **cash only**. |
| **1 h** | Rush-hour gridlock. Mobile networks are congested but up [V]. Petrol stations stop pumping. Water pressure starts to fall in towers above about 5 floors. |
| **4 h** | **Nivel 2 antennas die** as batteries run out [V]. Many home internet links are already dead. Building generators run out of fuel. Home-oxygen and ventilator patients start calling SAMU or arriving at emergency departments. |
| **6–8 h** | Night falls (in summer). A **curfew** is likely [V]. Fridges warm up. Pharmacies close. Lifts in hospitals and towers run on generators or stop. |
| **12 h** | A quarter or more of the mobile network is down [V]. Hospitals start rationing generator load. Sewage lift stations overflow in low areas. Gas cylinders and bottled water sell out. |
| **24 h** | If the grid is still down: towers have no water; supermarket frozen and chilled stock is lost; fuel trucks are prioritised for hospitals and the army; the **first looting** appears where police are thin (the periphery). Ollas comunes start. |
| **48–72 h** | Hospital diesel runs short wherever deliveries failed. Dialysis is cancelled. The water operator's own generators and fuel become the decisive variable. **Estado de catástrofe** with troops. Crime spikes against shops and pharmacies. Rumour runs ahead of truth. |
| **1 week** | Only if the cause is physical damage (see Part B): rolling power for priority circuits; queues for water trucks; a cash economy and barter in cylinders, diesel, medicines and batteries; departures from the city toward family in the countryside. |
| **1 month** | The "new normal" of rationing. Formal economy is half-paralysed. The state controls fuel. The black market is organised. |

---

## A.10 Timeline of documented failures, 2005–2026 (for period colour)

| Year | Event | Tag |
|---|---|---|
| 2004–2008 | Argentine gas cuts; gas plants switched to diesel; 2007 is the worst year | [V] |
| Feb 2007 | Launch of **Transantiago**, the bus system redesign: weeks of transport chaos | [K] |
| May 2008 | **Chaitén** volcano erupts; the town is evacuated | [K] |
| 2009 | First LNG cargo reaches **GNL Quintero** | [V] |
| 27 Feb 2010 | **27F** earthquake and tsunami (Mw 8.8); grid, communications and airport fail; looting and curfew in Concepción | [V] |
| 2010 | Ley 20.478 on telecom resilience | [V] |
| Sep 2011 | Central-grid (SIC) blackout | [K~] |
| Jan 2013 | Turbidity cut of Santiago's water | [V] |
| Apr 2015 / Sep 2015 | **Calbuco** eruption; **Illapel** earthquake (Mw 8.3) and tsunami | [K] |
| Apr 2016 | Massive turbidity water cut | [V] |
| Jan–Feb 2017 | Mega-wildfires in the centre-south; **Feb 2017** citywide water cut | [K]/[V] |
| Jul 2017 | Santiago snowfall blackout | [K~] |
| Nov 2017 | SIC and SING joined to form the SEN | [K] |
| Oct 2019 | **Estallido social**: Metro arson, curfews | [V] |
| 2020–2021 | **COVID** catastrophe state and 18 months of curfew | [V] |
| 2019–2022 | Megadrought peak; **Apr 2022** rationing protocol | [K~] |
| Feb 2023 | Ley 21.542 on critical infrastructure | [V] |
| Jun 2023 | Water cut for 1.3 million customers; Pirque ponds used | [V] |
| Feb 2024 | Wildfire in the **Viña del Mar / Valparaíso** hills, one of Chile's deadliest disasters since 27F (more than 130 dead) | [K~] |
| May 2024 | G5 geomagnetic storm; auroras seen in southern Chile | [V] |
| Aug 2024 | Windstorm blackout: 1.24 million customers at the peak, some outages over 2 weeks | [V] |
| **25 Feb 2025** | **National blackout** | [V] |
| Jul 2025 | Argentina interrupts gas exports again | [V] |

---

# PART B — Scenarios (Chile-specific)

## B.0 Scenario matrix

| Scenario | Plausibility | Warning time | Direct physical damage to Santiago | Main killer in Santiago | Duration of disruption | Value of a deep, stocked bunker | Tag |
|---|---|---|---|---|---|---|---|
| Nuclear war in the Northern Hemisphere (Chile not hit) | Low, but non-zero | Minutes to days | **None** | Hunger, fuel shortage, disorder; later cold and crop failure | **Years** | Low as a fallout shelter; **very high as a stocked, defensible base** | [E] |
| Nuclear strike on Santiago (fiction variant) | Extremely low | Minutes | Total near the targets | Blast, fire, fallout | Years | Decisive for the first 2 weeks | [E] |
| Carrington-class solar storm | About 0.3–12% per decade (estimates disagree) | 15–60 h after the flare is seen | None | Grid and fuel cascade | Days to months; years only in the worst tail | Medium (power, communications, medical continuity) | [V]/[E] |
| Severe pandemic | Moderate per decade | Weeks | None | Disease plus a collapsed health system | 1–3 years | High for isolation and medical stores | [E] |
| San Ramón fault earthquake (Mw 6.5–7.5) | Low per century, but certain eventually | **None** | **Severe in the east** | Collapse, fire, lifelines | Months to years | Mixed: a shallow bunker near the fault trace is at risk; a deep one in gravel is safer | [V]/[E] |
| Subduction megathrust earthquake offshore (Mw 8–9) | Moderate per century | None | Moderate | Lifelines, fuel and port damage | Weeks to months | Medium | [K]/[E] |
| Andean volcanic eruption | Low to moderate | Days to months of unrest | Minor (ash, lahars) | Water turbidity, ash | Days to weeks | Low | [V]/[E] |
| Megadrought | **Ongoing** | Years | None | Rationing, crops, hydro power | Years | Medium (wells, storage) | [K]/[E] |
| Cyberattack on the grid | Moderate | None | None | Blackout cascade | Days to weeks | Medium | [E] |

---

## B.1 Nuclear war

### Would Chile be targeted?

**Probably not.** [K]/[E]
- Chile is a party to the **Treaty of Tlatelolco**, which makes Latin America a nuclear-weapon-free zone. It has **no nuclear weapons**, belongs to **no nuclear alliance**, and **hosts no foreign military bases** or strategic-forces installations of the kind that attract warheads (missile fields, SSBN bases, early-warning radars, major command centres). [K]
- Its **strategic value** is economic and geographic: about a quarter of the world's mined **copper**, second place in **lithium**, the **Strait of Magellan and Drake Passage** (the only sea route between the oceans if the Panama Canal were closed), Antarctic claims, and astronomical and satellite ground stations near Santiago and in the north. None of these is a classic counterforce target, and countervalue targeting of a neutral Southern Hemisphere state would make no strategic sense. [K]/[E]
- **Neighbours.** Neither Argentina nor Brazil has nuclear weapons; their nuclear materials are mutually inspected through ABACC. [K]
- **Residual risks** are a deliberately "spoiler" strike in a total war (doctrinally unlikely), an accident, or **nuclear terrorism**. The last is the only route by which a weapon plausibly reaches Santiago, and it would be a low-yield ground burst. [E]
- **A note for local colour:** Chile operates a small research reactor, RECH-1, at the **CCHEN La Reina** centre in eastern Santiago. It is not a weapons site, but it is the kind of place a rumour mill would seize on. [K~]

### Fallout in the Southern Hemisphere

- **Local fallout** from ground bursts in the Northern Hemisphere falls out within hours to days, mostly within hundreds of kilometres downwind of the targets. **None reaches Chile.** [K]
- **Global (stratospheric) fallout** spreads over months to years. Air in the lower atmosphere takes about **a year** to mix between hemispheres, because the tropical circulation acts as a barrier. During the atmospheric-testing era (almost all of it in the north), Northern Hemisphere stratospheric concentrations ran **2–3 times** those in the south, and for the 1959 US tests Northern Hemisphere fallout was about twice the southern figure. [K]/[V]
- **Precedent.** The French atmospheric tests at Moruroa and Fangataufa (1966–74) gave measurable fallout in South America and drew protests from Chile and Peru. [K~]
- **Expected effect on Santiago.** A **chronic, low-dose problem** through the food chain (caesium-137, strontium-90), not an acute shelter problem. Iodine-131 (half-life 8 days) mostly decays before it arrives. **There is no realistic need for a two-week fallout sheltering period in Santiago after a Northern Hemisphere war.** [E] The DM may run Geiger-counter anxiety scenes and real anxiety over milk and vegetables, but radiation will not kill people in Santiago. [E]

### Nuclear winter and nuclear famine: what the models say

| Study | Scenario | Projection | Tag |
|---|---|---|---|
| Robock, Oman & Stenchikov (2007), *J. Geophys. Res.* | US–Russia war injecting 150 Tg of soot | Global mean surface cooling of roughly 7–8 °C for years; growing seasons collapse in the northern mid-latitudes; cooling is strongest over land. | [K~] |
| Coupe et al. (2019), *JGR Atmospheres* | 150 Tg, modelled with the WACCM4 climate model | **Larger** drops in temperature and precipitation than the older model in the first years. | [V] |
| **Jägermeyr et al. (2020), PNAS** 117:7071, doi:10.1073/pnas.1919049117 | India–Pakistan war, 5 Tg | Global mean −1.8 °C and **−8% precipitation for at least 5 years**. Calories from maize fall 13%, wheat 11%, rice 3% and soy 17% over 5 years; single-year losses of about 12%, which is 4× the worst recorded anomaly. Stocks and trade buffer **year 1**; multi-year losses then pass to food-insecure countries. | [V] |
| **Xia et al. (2022), *Nature Food*** 3:586–596, doi:10.1038/s43016-022-00573-0 | Six scenarios, 5–150 Tg | **Any injection above 5 Tg leads to mass food shortage in almost all countries.** More than **2 billion deaths** from an India–Pakistan war and more than **5 billion** from a US–Russia war. Livestock and fisheries cannot compensate, and adaptation such as cutting food waste helps little. **Northern countries (Canada, much of Europe) suffer worst; Argentina and Australia least**, because they grow hardy wheat at scale and have small populations. | [V] |
| Scherrer et al. (2020), *PNAS* 117(47), doi:10.1073/pnas.2008256117 | Six scenarios, effects on fisheries | For a US–Russia war, global fish **biomass falls by up to 18% and catch by up to 29%**. If fishing intensifies, catch rises about 30% in the short term and then falls by **up to ~70%**. Stocks rebuilt before the war provide a buffer. | [V] |
| New Zealand study (2023, *Scientific Reports*), building on Xia | 150 Tg | Major crops and fish in New Zealand fall by about **61%**; sunlight on cropland is lowest in years 1–2. | [V] |
| Coupe et al. (2021, *GRL*), "Nuclear Niño" | 5–150 Tg | An **El Niño-like** state in the Pacific lasting years. That would **weaken the Humboldt Current upwelling** that feeds Chile's anchovy and jack-mackerel fisheries. | [K~] |
| Bardeen et al. (2021, *JGR*) | Large wars | Soot heats the stratosphere and destroys **ozone**, so surface **ultraviolet** rises sharply for several years after the soot clears. | [K~] |
| ALLFED | 150 Tg | Country-level response studies and national preparedness reports for Argentina and others; work on "resilient foods" such as seaweed and relocating crops. **No Chile-specific study was found.** | [V] |

### What this means for Chile (reasoned) [E] unless tagged

- **Climate.** Central Chile has a Mediterranean climate buffered by the cold Pacific, and ocean inertia means **less cooling than continental interiors**. Expect the Central Valley to lose roughly 1–3 °C in a 5–16 Tg war and several degrees in a 150 Tg war. Frosts would come earlier and later in the season, and summers would be shorter and cloudier. On top of the existing **megadrought**, any drop in rainfall cuts hydro power, irrigation and Santiago's El Yeso reserve. [M]/[E]
- **Food.** Chile's export economy (cherries, grapes, avocados, wine, salmon) **loses its buyers and its shipping** within weeks. Meanwhile Chile must **import staples it cannot pay for or cannot get**. Argentina, next door, is projected to be one of the **least affected** food producers on Earth [V], which makes the **Los Libertadores pass, cross-Andes trade and Argentine politics** existential for Santiago. The pass closes in winter snow, and more often if the climate cools. [K]/[E]
- **Fisheries.** These are a key Chilean protein source. A "nuclear Niño" plus global overfishing pressure suggests a short boom followed by a crash. [M]/[E]
- **Energy.** Chile **imports nearly all its oil**, and stocks cover about a month (A.3). Within 2–6 weeks the state rations diesel to food, health, water and the military. **Electricity is Chile's relative strength:** more than half comes from hydro, solar and wind. But soot cuts Atacama **solar** output substantially in years 1–2, reduced rainfall cuts hydro, and LNG cargoes stop. Expect **rolling power cuts** rather than total darkness. [K~]/[E]
- **UV.** Chile already lives with high UV and ozone-hole episodes in the south; after the soot clears, UV gets worse. Expect skin and eye damage and crop stress. [M]/[E]
- **Refugees and politics.** Wealthy Northern Hemisphere survivors with planes and boats would try to reach the Southern Cone, New Zealand and Australia. Chile and Argentina would close their borders. [E]

### EMP

- A **high-altitude EMP (HEMP)** requires a detonation 30–400 km up and affects only the area under the burst's line of sight. A war in the Northern Hemisphere does **not** produce an EMP over Chile. [K]
- Use HEMP only if the DM deliberately chooses a burst over South America, for example in a terrorism or "rogue state" plot. Its slow E3 component acts like a solar storm on the grid (B.2); its fast E1 component damages unprotected electronics. [K]

### Sheltering mechanics (for the "Santiago hit" variant)

**7-10 rule.** Every 7-fold increase in time after the burst cuts the fallout dose rate 10-fold. [V]

| Time after burst | Relative dose rate |
|---|---|
| H+1 hour | 1,000 |
| H+7 hours | 100 |
| H+49 hours (about 2 days) | 10 |
| H+343 hours (about 2 weeks) | 1 |
| About 14 weeks | 0.1 |

[V] (the rule is an approximation; real decay depends on the weapon, burst height and weather)

- **Dose estimate** (Way–Wigner t⁻¹·² decay, integrated from H+1 to H+2 weeks): about **3.4 × the H+1 dose rate**. An outdoor field of 1,000 R/h at H+1 gives about 3,400 R over two weeks (certainly lethal). Inside a shelter with a protection factor of 1,000 the occupant receives about **3–4 R**. [E] (calculation)
- **Halving thicknesses for fallout gamma** (Kearny, *Nuclear War Survival Skills*): steel about 1.8 cm, **concrete about 5.6–6 cm**, **packed earth about 8.4–9 cm**, water about 12 cm, wood about 22 cm. **Ten halvings ≈ a 1,000-fold reduction**, so about 90 cm of earth or about 56–60 cm of concrete. [K]
- **Shelter duration.** Stay continuously sheltered for at least 24–48 h. After that, brief exits become survivable; after about **2 weeks** most areas allow longer outdoor work. [V]/[K]
- **Santiago's geography.** Winds in the basin are weak and follow a daily cycle: south-westerly up-valley breezes in the afternoon, down-slope drainage at night, and occasionally the dry easterly **"puelche"**. A plume would meander rather than blow straight away, and smoke from burning city districts would sit under the inversion for days. [K~]/[E]

### Phases for the realistic case: Northern Hemisphere war, Chile untouched [E]

**First 72 hours**
- News arrives by television, radio, phones and social media; the internet slows down as transatlantic and Pacific routes degrade or fail. Markets collapse and the peso crashes. Banks freeze withdrawals or ration cash.
- **Panic buying** empties every supermarket in Santiago within **24 hours** (compare the March 2020 pattern). Fuel queues form. The government declares an **estado de catástrofe**, a curfew, price controls and a fuel allocation.
- Flights stop: the airport becomes a stranded-tourist camp. Northern Hemisphere expatriates crowd their embassies.
- No physical damage; electricity and water are normal.

**First month**
- Fuel rationing (diesel kept for food, water, health and the military). Imports of finished products stop and refineries run down their crude stocks. Food prices triple or more. Food is distributed by ration card or in-kind boxes, as Chile did with pandemic food boxes in 2020.
- Northern Hemisphere governments are paralysed; no ships arrive. Chile negotiates bilaterally with Argentina for wheat and with Peru. The armed forces guard ports, Lo Valledor, fuel terminals and silos.
- Cooling has not yet hit Chile (soot takes weeks to spread). Mass layoffs; tens of thousands of cherry and fruit workers lose their jobs.

**First year**
- The climate signal arrives in the following growing season (spring 2 in the Southern Hemisphere): a cooler, drier, dimmer summer and a shorter season in the Central Valley. Chile reorients farmland from export fruit to **staples** (wheat, potatoes, legumes); orchards are cut down for firewood.
- Fishing is militarised. Rolling power cuts, with periodic gas and kerosene crises in winter.
- Malnutrition appears in the periphery. Measles and tuberculosis resurge. The health system runs out of imported drugs (insulin, antibiotics, chemotherapy, anaesthetic gases).
- Politically: emergency government, possibly by decree; extended states of exception; a growing role for the military. Social unrest is likely around food distribution.
- **This is the scenario where a bunker matters least as a bunker and most as a granary, pharmacy, clinic and fortified base.**

---

## B.2 Carrington-class solar storm

### Chile's exposure

- **Geomagnetic latitude** (dipole approximation, compiler's calculation): **Arica about −9°, Santiago about −24°, Punta Arenas about −44°.** Chile is at **low to middle geomagnetic latitudes**, lower in magnitude than its geographic latitude, which puts it at lower risk than Canada, Scandinavia or the northern US. [E] (calculation)
- The magnetic **dip equator** runs through Peru; the Jicamarca observatory near Lima sits on it. The far north of Chile lies a few degrees from it. [K]
- **South Atlantic Anomaly (SAA).** The geomagnetic field over South America and the South Atlantic is among the **weakest on Earth**. Satellites in low orbit take far more radiation hits when they pass over it, which causes electronics upsets; Hubble suspends observations there. [K] Brazilian studies of the 2015 storms found **larger ground magnetic disturbances within the SAA and equatorial-electrojet regions**, so geomagnetically induced currents (GIC) should be larger there too. Measured and modelled values were modest, though: about 8 A in 2015, and about 30 A in one Brazilian transformer during the 2003 "Halloween storm", with most values below 10 A. [V]
- **What raises Chile's risk** [K]/[E]:
  1. **Very long lines.** The 500 kV backbone runs about 3,000 km north–south, and the HVDC link adds about 1,342 km (from about 2029). Induced voltage grows with line length. HVDC links are less exposed to GIC on the line itself, but their converter transformers are not immune.
  2. **The coast effect.** Geoelectric fields are enhanced where conductive ocean meets resistive land, and the whole Chilean grid runs parallel to the Pacific coast within about 100–200 km.
  3. **Large autotransformers** at a few nodes (Polpaico, Lo Aguirre, Alto Jahuel, Cardones, Nueva Pan de Azúcar) concentrate the risk.
- **What lowers it:** low geomagnetic latitude, a grid that is used to big tripping events, and plenty of hydro for black-start. [E]
- **No Chile-specific GIC study was found.** This is a real gap in the public literature and a useful hook for play. [V: none found]

### Precedents

- **1859.** Auroras were recorded in Chile during the Carrington event. [V] (mentioned in the 2024 reports)
- **10–11 May 2024 (G5, the first "extreme" storm since 2003).** Auroras were seen and photographed from **Punta Arenas, Puerto Natales, Puerto Williams and Chiloé**, possibly Aysén, around 19:00. Press called it the first such sighting at those latitudes in about 165 years. **No damage to the Chilean grid was reported.** [V]
- **Feb 2022.** A minor storm increased atmospheric drag enough to destroy about **38 newly launched Starlink satellites** in low orbit. [K]

### Probability and impact estimates

- **Probability of a Carrington-class event:** about **12% per decade** (Riley 2012) or about 10% (Riley & Love), using a power-law fit. Extreme-value analyses give **0.33–0.70% per decade**, with an upper 95% bound around 4%. **The disagreement is real.** [V]
- **Lloyd's/AER (2013), for North America:** damages up to about **US$2.5 trillion**, with parts of the grid down for **up to 1–2 years** in the worst case. This is a high-latitude, US-centred estimate. [V]/[K]
- **Transformer replacement:** lead times averaged about **120 weeks** in 2024 (80–210 weeks for large units). Transmission-scale units take **3–6 years**, and prices have risen to more than double. Chile imports all its large power transformers. [V]/[K]

### Effects

| System | Effect | Tag |
|---|---|---|
| Grid | Half-cycle saturation of transformers causes reactive-power demand, harmonics and protection misoperation; voltage collapse leads to a **national blackout like 25F**. Hotspot heating may permanently damage a few large transformers. | [K]/[E] |
| GPS and GNSS | Positioning errors and outages for hours to a day or two, plus scintillation at low latitudes. **Timing** is also lost, which hurts telecom, banking and grid synchrophasors. | [K] |
| Satellites | Anomalies, losses in low orbit from drag, and degraded Starlink and communications satellites. | [K] |
| HF radio | Blackout on the sunlit side for hours; absorption for days. Ironically, HF is the amateur's backup. | [K] |
| Hospitals | Run on generators; GPS-dependent ambulance dispatch and navigation are degraded. Medical electronics themselves are not affected by GIC. | [K]/[E] |
| Pipelines | Accelerated corrosion over the long term; no immediate failure. | [K] |

### Realistic duration in Santiago [E]

- **Most likely (about 70%):** a **national blackout of 8–48 hours**, as on 25F but at night and with protection-system chaos, then a degraded grid with rolling cuts for **days**. GPS and satellite problems last 1–3 days.
- **Bad (about 25%):** **several 500/220 kV transformers damaged.** The SEN is split into islands. Santiago gets **rotating rationing for weeks to months**, because the north's solar power cannot reach the city and local hydro, Nueva Renca and Quintero gas cannot cover demand. Mobile networks run on generators at a few sites. Fuel becomes the master resource.
- **Tail (under 5%):** a cascading loss of many transformers across the Americas, with **global** supply chains for transformers and electronics swamped. Chile waits years in the queue. Partial electricity from hydro and isolated plants, but no "Mad Max". This is a slow, poor, rationed country.

### Phases [E]

**First 72 hours**
- **Warning.** The flare is seen 15–60 h before the coronal mass ejection arrives. Space-weather agencies alert grid operators, and the CEN may reconfigure the grid. Most citizens hear nothing, or a garbled news item.
- **Impact,** say at night. Brilliant auroras are visible even from Santiago. The grid goes down within minutes, followed by the 25F cascade (A.9) plus GPS failure, which hits apps, ride-hailing and dispatch.
- **Restoration attempts** fail repeatedly because the storm lasts 1–3 days. Hospitals run on generators; the curfew is repeated.

**First month**
- Depending on transformer damage: either normality within about a week, or rationing by sector (for example 8 h on and 8 h off), as was planned during drought crises.
- Imports of spare parts are slow because the whole world is short. Mobile coverage is patchy. Banking runs on cash. Industry and mining (copper) cut demand to free power for the cities.

**First year**
- If transformers were damaged: an emergency procurement programme; mobile substations; diesel generation at large nodes (which needs imported diesel). The HVDC project is accelerated. Political crisis over the grid's fragility (compare the Interchile debates in 2025).
- Medical: chronic patients (dialysis, home oxygen) are migrated to powered facilities.

---

## B.3 Pandemic

### COVID lessons from Chile [V]/[K]

- Chile used the **estado de catástrofe** and an **18-month night curfew** (22 Mar 2020 to 30 Sep 2021). [V]
- Quarantines were imposed **comuna by comuna**, which was socially uneven: wealthy eastern comunas were locked down first, poor ones later and for longer. Online movement permits ("Comisaría Virtual"), a five-step reopening plan ("Paso a Paso"), centralised ICU-bed management and aeromedical evacuations followed. [K]
- The ICU network **expanded several-fold** and saturated in June 2020 and April–June 2021. **Vaccination was among the fastest in the world** in early 2021 (CoronaVac, then Pfizer). [K~]
- Deaths: about 60,000+ confirmed and probable by 2022–23. [K~]
- **Supply**: supermarket demand surged and staff got sick, but **food never ran out**. **Lo Valledor and the ferias kept working**, and ollas comunes reappeared in poor comunas. [V]/[K]
- **Social**: 2020 began with the estallido still smouldering, and the pandemic suppressed it.

### A severe pandemic for the game (for example an influenza with 2–5% case fatality and fast spread) [E]

**First 72 hours** (after the first local cases): rumour and denial; runs on masks, alcohol gel and paracetamol; schools close; the ministry activates its plans. The clinic network is overwhelmed by worried patients.

**First month**: an estado de catástrofe, **curfew**, city quarantine and cordons around Santiago (as in 2020). Absenteeism of 20–40% among health workers, truckers, water and power operators. **The lifelines fail through staffing, not through damage.** Hospitals triage ventilators. Funeral services are overwhelmed. Shortages of oxygen, antivirals and antibiotics follow.

**First year**: waves; vaccines months away. The poorest comunas carry the worst mortality. The economy contracts 10–20%. Unrest over aid and lockdown fatigue. A bunker's value lies in **isolation** (positive-pressure filtered air, quarantine airlocks), **staff housing** and **medical stores**. Its danger is that a single infected entrant can contaminate a sealed community.

---

## B.4 Earthquake: the San Ramón fault (and the subduction zone)

### The San Ramón fault (Falla San Ramón)

| Item | Facts | Tag |
|---|---|---|
| Location | A thrust fault along Santiago's **Andean front**, the boundary between the foothills and the flat city, through Lo Barnechea, Las Condes, La Reina, Peñalolén, La Florida and Puente Alto. The trace is commonly given as **about 25–30 km long, about 55% of it urbanised**, and it may continue about 20 km further south. | [V] |
| Key studies | Armijo et al. (2010, *Tectonics*), with the IPGP and Universidad de Chile; Vargas et al. (2014, *Geology*), trench paleoseismology; Estay et al. (2016, *NHESS*); a 2020 review in *NHESS*. | [V] (titles not re-checked: [K]) |
| Past events | Trenching shows **two large events about 17–19 thousand and about 8 thousand years ago**, each with **about 5 m of displacement**, consistent with **Mw about 7.5**. The 1575 and 1647 historical earthquakes are not clearly attributable to this fault. | [V] |
| Slip rate and recurrence | About **0.1–0.5 mm/yr**; recurrence **about 9,000 years**. With the last event about 8,000 years ago, Armijo, Vargas and colleagues call the fault "ripe" for a Mw 7.5. | [V] |
| Alternative view | Estay et al. (2016) argue that the fault is split into **four segments** that rupture separately, at **Mw 6.2–6.7**. They do not rule out a combined rupture. | [V] |
| Damage studies | Simulations show **eastern Santiago would feel much stronger shaking** than in subduction earthquakes. A 2026 Universidad de los Andes study modelled Mw 6.7 effects on 10-storey buildings. | [V] |

**Why it matters more than its magnitude.** It would be a **shallow crustal quake directly beneath the wealthy east**: near-fault pulses, strong vertical acceleration, and a **surface rupture of up to a few metres** across streets, pipes, the Metro and Costanera Norte, water mains, gas lines and the Maipo aqueducts that feed the city from Las Vizcachas. [E] Chilean building codes (NCh 433) proved excellent in 27F, but they were designed for **subduction-type** shaking. [K]

**Analogues** [K]: Christchurch 2011 (Mw 6.2, shallow, under the city): 185 dead and a city centre demolished. Kobe 1995 (Mw 6.9, crustal): about 6,400 dead. Northridge 1994 (Mw 6.7): about 60 dead with good codes. **For Santiago, assume hundreds to a few thousand dead**, depending on hour and magnitude; tens of thousands of damaged homes; and **months** of service disruption in the east. [E]

### Other quakes that shake Santiago

- **Subduction megathrust** offshore central Chile: the 1730 Valparaíso earthquake (estimated about Mw 9), 1906 Valparaíso (about Mw 8.2), 3 Mar 1985 Algarrobo (Mw 8.0, about 180 dead). [K~]
- **Intraslab** earthquakes deep under the city. Both types shake Santiago less violently than San Ramón would, but over a larger area, and they **damage ports, the Concón refinery, Ruta 68 and the coastal fuel infrastructure.** [K]/[E]

### Phases (San Ramón, Mw 7.2, 03:00 in winter) [E]

**First 72 hours**: power is out across the city (substations and lines along the foothills are damaged). Mobile networks are congested and then dead. Building collapses are concentrated in older masonry (Ñuñoa, older La Reina) and in some modern towers near the trace. **Fires** break out from gas leaks. Water mains in the east are broken; the gravity system loses pressure. Hospitals in the east (Clínica Alemana, Clínica Las Condes, Hospital del Salvador, Hospital Luis Tisné) are damaged or evacuated, and casualties flow to the centre and west (Posta Central, Hospital San Juan de Dios). Highways are cut by collapsed overpasses. The state of catastrophe arrives within hours, with the army in the street on day 1–2 (the post-27F lesson).

**First month**: the west and centre recover power within days; the east within weeks. Water tankers serve the east. Thousands are displaced into tent camps ("aldeas") in parks. Debris removal. The **Metro** is partly closed (inspections; tunnels crossing the fault are damaged). The economic heart of Las Condes and Providencia is paralysed. Looting is limited if the state is visible.

**First year**: reconstruction; political argument over permits that allowed building on the fault trace; a property-market crisis in the east. Aftershocks, and fear of a second segment rupturing.

---

## B.5 Volcanic

- **The nearest volcanoes**, all in the Cajón del Maipo and on the Argentine border: **Tupungatito** (about 75 km from Santiago), **San José** and **Maipo**. [V]
- **Tupungatito** ranks about 29th–31st in SERNAGEOMIN's national volcanic-risk ranking, depending on the edition (category 2). Experts expect any eruption to be **small**. The ash would reach the Cajón del Maipo and could reach Santiago only with a favourable wind. The main hazard is **lahars**: volcanic mudflows from melting glacier ice. A seismic swarm in March 2025 left the alert at **green**. [V]
- **San José** erupted between 1822 and 1960, without highly explosive events. SERNAGEOMIN says neither San José nor Maipo should seriously affect Santiago except under unusual winds. [V]
- **Prevailing westerlies** carry ash **east toward Argentina**: Puyehue 2011 and Calbuco 2015 dropped ash on Bariloche and beyond, not on Chile's cities. Santiago is mostly **upwind** of its own volcanoes, and only easterly ("puelche") episodes would bring ash west. [K]/[E]
- **The real Santiago link is water.** A lahar or ash-laden runoff in the Maipo basin means **turbidity**, which means a citywide water cut (A.1) and possibly weeks of trouble for the Las Vizcachas intake. [E] **This is the most game-relevant volcanic consequence.**
- **Deep time.** Western Santiago's subsoil contains a large ignimbrite (the "Ignimbrita Pudahuel"), attributed to a caldera eruption at the Maipo/Diamante complex hundreds of thousands of years ago. Age and volume [?]; check before quoting.

**Phases (Tupungatito, moderate eruption with lahar) [E].** First 72 h: alert raised to orange or red; San José de Maipo and El Volcán evacuated; ashfall in the Cajón; a lahar in the Maipo leads to a water cut for Santiago within hours. First month: rotating water service; tanker trucks; hydro plants in the Cajón shut down; tourism collapses. First year: monitoring; repeated turbidity in the summer melt; disputes over relocating villages.

---

## B.6 Megadrought ("megasequía")

- **Context.** Central Chile has had persistent rainfall deficits since about 2010 (CR2 "La megasequía 2010–2015" and later reports). 2019 was exceptionally dry in Santiago. El Yeso fell to about **60 Mm³**, against a capacity of 220–256 Mm³. [K~]/[V for El Yeso]
- **Response.** In **April 2022** the RM published a drought-alert protocol (green, yellow, orange/red preventive, red) foreseeing **rotating 24-hour cuts by sector** in its last stage. Wetter years (2023 El Niño) refilled the reservoirs, and the protocol was never fully used. [K~]
- **Cascade.** Less hydro power means more gas and diesel generation, higher prices and import dependence. Agriculture dies (Petorca valley precedent: villages supplied by tanker truck), and rural migration to Santiago follows. [K]/[E]
- **Phases [E].** First 72 h: not applicable, since this is a slow crisis. First month of "red": nightly pressure reduction, then 24-hour rotating cuts by sector; buckets, tanks, and a black market in water trucks. First year: wells become political; water theft from canals; urban gardens banned; fights between agriculture and the city; mass purchase of household tanks ("estanques") and well-drilling, much of it illegal.

---

## B.7 Others, briefly

| Scenario | Notes | Tag |
|---|---|---|
| **Cyberattack on the grid or water utility** | Chile passed a **framework cybersecurity law (Ley 21.663, 2024)** creating a national cybersecurity agency (ANCI). There are precedents of attacks on Chilean state bodies (ransomware against public agencies, and a 2022 leak of military emails). The physical effect equals a 25F-type blackout, but restoration is slower if control systems are corrupted: days to weeks. | [K~]/[E] |
| **Deliberate HEMP over South America** | See B.1. Combines a fast electronics kill (E1) with grid damage (E3). Vehicles mostly keep running; many electronics fail. | [K]/[E] |
| **Asteroid** | A Chelyabinsk-type airburst (about 0.5 Mt) over a city breaks windows across tens of km². A Tunguska-type (about 10–15 Mt) flattens a city. A 1 km object is a global climate event like a nuclear winter. Ocean impacts cause tsunamis on the Chilean coast. | [K] |
| **Supervolcano / VEI 7** (for example Yellowstone, or a Tambora-class eruption anywhere) | A "year without a summer": a 0.5–1 °C global drop for 1–3 years, harvest failures in the Northern Hemisphere, and Chile affected through trade and climate. Behaves like a mild nuclear winter without the war. | [K]/[E] |
| **Wildfire at the urban edge** | The Feb 2024 Valparaíso and Viña fires killed more than 130 people. Santiago's eastern and western hills are exposed in dry, hot, windy summers. | [K~] |
| **Aluvión (mudflow) in the city** | The 3 May 1993 **Quebrada de Macul** aluvión killed about 26 people in Peñalolén and La Florida. Eastern quebradas (ravines) remain a hazard during warm storms, the same mechanism as turbidity. | [K] |
| **Compound events** | The realistic catastrophe is often two at once: a winter frontal storm plus a quake; drought plus a heatwave plus wildfires; a blackout during a pandemic. | [E] |

---

# PART C — Prepping and bunkers in Chile

## C.1 Design basis: what is the bunker for?

| Threat | Protection needed | Depth and structure | Duration of occupancy |
|---|---|---|---|
| **Fallout** (Santiago in a downwind plume) | Mass shielding (protection factor ≥ 100–1,000) plus filtered air | About 1 m of earth or 60 cm of concrete overhead; can be a basement | **2 weeks** of continuous occupancy, then intermittent use |
| **Blast** (direct targeting) | Hardened structure, blast doors and blast valves | Deep (more than 10 m) or reinforced to a rated overpressure | Hours to weeks |
| **Chemical / biological** (pandemic, industrial accident) | **Positive-pressure filtered air**, airlock, decontamination | Any depth | Days to months |
| **Civil disorder** | Concealment, access control, hardened entrance | Any depth; **discretion** matters more | Indefinite |
| **Long collapse** (famine, rationing) | Storage, power, water, security, **community** | Large volume, not necessarily deep | Months to years |
| **Earthquake** | Seismic design; flexible connections at utility entries | Underground structures in gravel perform well | Not applicable |

**Key judgement for Santiago [E].** The threats that actually happen here are **earthquakes, blackouts, water cuts, disorder and long economic collapse**. A Santiago bunker should be built **first as a seismically robust, self-powered, self-watered, secure storehouse and clinic**, and **second** as an NBC shelter (nuclear, biological, chemical). Blast protection is a luxury, justified only by fiction or by the owner's paranoia, which is itself a good character note.

## C.2 Structure

- **Overpressure reference values (Glasstone & Dolan)** [K]: about 1 psi (7 kPa) breaks windows; about 5 psi (35 kPa) destroys most houses; about 10–20 psi destroys reinforced-concrete buildings. **Swiss shelters are designed for 1 bar (100 kPa, about 14.5 psi)**, which is enough for a well-built shelter to survive outside the immediate fireball zone of a large weapon. [K]
- **Fallout shielding**: see the halving thicknesses in B.1. **A third or fourth basement level under a Santiago office tower** (several floor slabs of 15–25 cm reinforced concrete overhead plus earth on the sides) easily gives a **protection factor in the thousands**. [E] Santiago's thousands of deep underground car parks in Las Condes, Providencia and the centre are therefore excellent ready-made fallout shelters, though not stocked, ventilated or defensible. [E]
- **Concrete and codes.** Chile designs reinforced concrete under NCh 430 and seismic loads under **NCh 433** (buildings) and NCh 2369 (industrial). Structural concrete grades are typically G25–G40 (25–40 MPa); a blast-rated shelter would use G35–G50 with heavy two-way reinforcement and confinement. [K~]/[E]
- **Seismic behaviour.** Buried structures move with the ground and suffer far less amplification than buildings. Weak points are **connections**: entrances, ventilation shafts, utility penetrations and the interface with the building above. Use flexible couplings and seismic joints. [K]
- **Gravel.** The "grava de Santiago" is stable for deep excavation with anchored retaining walls ("pilas y anclajes", soldier piles and anchors), as in every deep car park. The **water table** varies across the basin, deeper in the east and shallower in the north-west; get a geotechnical study ("mecánica de suelos"). [K]/[E]
- **Blast doors and blast valves** are Swiss and German specialities; Chile has no known domestic maker. A Swiss-style steel-and-concrete shelter door, imported, is a five-figure-USD item. [?]/[E]

## C.3 Air: NBC filtration, carbon dioxide, ventilation

- **Swiss system** (the reference model; the regulator is the Federal Office for Civil Protection, BABS/FOCP). Shelters have a **ventilation unit** that can run electrically or be hand-cranked, a **pre-filter and an activated-carbon gas filter** for NBC protection, **blast valves** that slam shut on the pressure wave, and an **overpressure valve** that keeps the shelter slightly pressurised so contaminated air cannot seep in. **Andair AG** and similar Swiss firms make the ventilation units, gas filters and valves. [K] Swiss standards also set minimum space, roughly **1 m² of floor and 2.5 m³ of volume per person**. [K~]
- **Fresh-air rates** in filtered mode are of the order of a few m³/h per person; check the current BABS technical directives before quoting exact numbers. [?] Normal ventilation for comfort and humidity needs far more, about 15–30 m³/h per person. [K]/[E]
- **Carbon dioxide budget** [K]/[E]:
  - A resting adult produces about **1 kg of CO₂ a day** (about 20 L/h) and uses about 0.84 kg of O₂.
  - **Rising CO₂ kills before falling oxygen does.** About 0.5% (5,000 ppm) is the 8-hour occupational limit; at about 3% people get headaches and pant; above about 5% it is dangerous.
  - A **sealed** room with 2.5 m³ per person reaches 3% CO₂ in about **3–4 hours**. **A sealed shelter is a death trap without forced ventilation or CO₂ scrubbing.** [E] (calculation)
  - **Chemical scrubbing** for "sealed mode" (an external fire, a gas cloud): lithium hydroxide absorbs about 0.9 kg of CO₂ per kg; soda lime about 0.2–0.25 kg/kg. For 50 people that is about 55 kg of LiOH or about 200–250 kg of soda lime **per day**. Sealed mode is practical only for **hours to a couple of days**. [K]/[E]
  - **Cheap CO₂ meters** (NDIR sensors) should be everywhere; they are a classic tension device in play. [E]
- **Fire and smoke.** A firestorm or burning city can make the outside air toxic (carbon monoxide, very hot gases) for hours to days. The air intake should be remote and protected, and the system should be able to close and go into scrubbing mode. [K]
- **Generator exhaust** must leave **outside the sealed envelope**, and its intake must not draw from the shelter: carbon monoxide is the classic shelter killer. [K]

## C.4 Heat and humidity

- **Each occupant gives off about 100 W** (about 70 W as heat plus moisture). Fifty people produce about **5 kW**, before lights, computers, medical equipment and cooking. [K]
- **Moisture:** each person releases on the order of 1–1.5 L of water vapour a day through breath and sweat, so 50 people add about 50–75 L/day. Condensation, mould and miserable sleep follow. [K~]
- **The ground as a heat sink:** deep soil sits near the local mean annual air temperature, about **14–16 °C in Santiago**. A buried shelter starts cool, but the walls warm up over days to weeks of full occupancy. [K~]/[E]
- **US shelter habitability tests in the 1960s** (groups of dozens to hundreds sheltered for up to two weeks) found **heat and humidity** were the main complaints and limiting factors, more than food or boredom. [K]
- Design: ventilation, dehumidifiers or chillers (which need power), a water-cooled heat exchanger using the well or tank (stored water is also thermal mass), and **light clothing**. In winter the problem reverses for a lightly occupied shelter, though Santiago never gets truly cold underground. [E]

## C.5 Water

- **Quantities** (Sphere humanitarian standards): **2.5–3 L per person per day** for drinking survival; **about 15 L per person per day** as a basic total for drinking, cooking and minimal hygiene. [K] Realistic shelter planning: **4–6 L per person per day** for drinking and cooking, plus whatever hygiene allows. [E]
- **Storage**: food-grade polyethylene tanks (cheap and common in Chile; rural houses use "estanques" of 1,000–10,000 L), stainless steel, or lined concrete cisterns. Keep stored water away from light. [K]
- **Treatment**: chlorine (household bleach loses strength within months; **calcium hypochlorite granules keep for years**), ceramic or hollow-fibre filters, UV (needs power), reverse osmosis (needs power and wastes water), boiling (needs fuel). [K]
- **Well**: legal for domestic use on one's own land under the Water Code, subject to registration (C.13). Santiago groundwater is generally good but **depth varies, from tens of metres to more than 100 m**. A well needs a pump and power, and in fallout scenarios it is a **protected** water source because the aquifer is shielded. [K]/[E]
- **Water is the tightest constraint for large groups.** 100 people × 5 L × 90 days = **45,000 L** (45 m³), already a large cistern. [E] (calculation)

## C.6 Sewage and waste

- A bunker below sewer level needs **ejector pumps** with a holding sump, **backflow valves** (Santiago's sewers back up in heavy rain and in blackouts) and a bypass. [K]
- **Without power or sewer:** chemical toilets, composting or bag-and-lime systems, storage of sealed waste. Smell and disease (gastroenteritis, hepatitis A) are the real enemies. [K]
- **Solid waste:** compactable storage; incineration is impossible without exhaust. Plan about **0.5–1 kg per person per day** of packaging if eating stored food. [E]

## C.7 Power

| Element | Facts | Tag |
|---|---|---|
| Diesel generator | Uses about **0.25–0.3 L of diesel per kWh** at a good load and worse at light loads. A 100 kVA set at full load burns roughly 20–25 L/h. **Size two smaller units** rather than one large, so one can be maintained while the other runs. | [K] |
| Fuel degradation | **Diesel**: 6–12 months untreated (oxidation, water, microbial "diesel bug"); several years with stabiliser, biocide, a dry and cool tank, and regular **fuel polishing** (filtering and recirculating). **Gasoline**: 3–6 months. Rotating the stock is the professional answer. | [K] |
| Solar | Santiago receives roughly 4.5–5.5 kWh/m²/day averaged over the year, with much less in winter and in smog. Panels must be **outside** the bunker, vulnerable and visible. | [K~] |
| Batteries | LiFePO₄ lasts about 3,000–6,000 cycles; lead-acid about 300–1,500. Lithium batteries need **ventilation and fire safety**: a lithium fire in a sealed bunker is lethal. | [K] |
| Lighting | LED: a whole shelter for dozens of people can be lit with a few hundred watts. | [K] |
| Load estimate | Ventilation plus lights plus refrigeration plus medical plus communications for 50 people: about **5–20 kW** on average, which means **30–150 L of diesel a day** and **1,000–4,500 L a month**. | [E] (calculation) |

## C.8 Food storage

| Food | Shelf life (cool, dry, dark) | Tag |
|---|---|---|
| White rice, wheat berries, dried beans and lentils, sugar, salt, in sealed Mylar or cans with oxygen absorbers | **20–30+ years** (Brigham Young University storage studies) | [K] |
| Commercial freeze-dried meals (pouches or #10 cans) | Manufacturers claim **up to 25–30 years** | [K] |
| Military MREs | About **3–5 years at 27 °C**, much less in heat | [K] |
| Ordinary canned goods | 2–5 years for good quality; longer for safety if the cans are intact | [K] |
| Cooking oil | 1–2 years (rancidity); ghee and lard are similar | [K] |
| Powdered milk (Chilean "leche en polvo") | 1–2 years at retail; longer when nitrogen-packed | [K~] |
| Honey | Indefinite | [K] |

- **Calories:** about 2,000–2,500 kcal per person per day (more for heavy labour). Dry staples hold about **3,500 kcal/kg**, so about **0.6–0.7 kg per person per day**. [K]/[E]
- **Chilean pantry flavour** (cheap, culturally right): arroz, porotos, lentejas, garbanzos, harina, **harina tostada** (toasted flour), **mote** (husked wheat), **charqui** (jerky), leche en polvo, té, azúcar, aceite, sal, plus canned jurel (jack mackerel, very Chilean), canned tuna and machas. [K]/[E]
- **Enemies of stored food:** heat, moisture, oxygen, light and **rodents**. Santiago's rats are formidable. [K]

## C.9 Medical stores

- **Drug shelf life.** The US **Shelf Life Extension Program (SLEP)**, run by the FDA for the Defense Department, tested 122 drug products (3,005 lots): **88% of lots were extended at least 1 year past their labelled expiry, by an average of 66 months**, but with **high lot-to-lot variability**. Many properly stored drugs outlast their dates. (Lyon et al., *J Pharm Sci* 2006, doi:10.1002/jps.20636; retrieved via PubMed.) [V]
  - A separate analysis (Cantrell et al., *Arch Intern Med*, 2012) found most active ingredients in drugs decades past expiry still at or near full potency. [K~]
  - **Exceptions:** liquids and suspensions; **insulin** (refrigerate; once opened, about 4 weeks at room temperature); **epinephrine** (loses potency); nitroglycerin; some antibiotics in liquid form; vaccines and biologics; eye drops. [K]
- **Oxygen: concentrator or cylinders?** [K]

| | Oxygen concentrator | Cylinders |
|---|---|---|
| Output | About 5–10 L/min at 90–95% O₂ | Up to 15+ L/min, at 99%+ O₂ |
| Needs | **Power** (about 300–600 W) | **Resupply** |
| Endurance | As long as power lasts | A large ("H/K") cylinder of about 6,000–8,000 L lasts about 2 days at 2 L/min and a few hours at 15 L/min |
| Risks | Fails in a blackout | Fire and explosion risk; heavy |
| Bunker answer | Several concentrators **plus** generator or battery | Cylinders as a reserve for high flow; a small hospital-style oxygen generator (PSA plant) for a serious network |

- **The emergency-physician list** [E]: airway kit, oxygen, IV fluids (crystalloids for 1–2 years), sutures and staplers, splints, tourniquets, chest drains; antibiotics (oral and IV, broad coverage); analgesia (ketamine is stable and versatile; opioids under controlled-drug rules, see C.13); local anaesthetics; antiemetics; steroids; antihypertensives, antidiabetics and insulin for chronic patients; anticonvulsants; obstetric kit; a portable ultrasound and a defibrillator (both need power); rapid tests; oral rehydration salts. **Blood:** no long-term storage, so plan a "walking blood bank" of typed donors. [K]
- **What a bunker cannot do long-term:** dialysis, most chemotherapy, complex surgery without staff and supplies, intensive care for more than a few patients. [E]

## C.10 Psychology and governance of confinement

- **Evidence** [K]: the **Mars-500** isolation (520 days, Moscow, 2010–11) showed sleep disruption, inactivity and depression in some crew members; Antarctic winter-over crews show "third-quarter" mood dips; submarine patrols of 60–90 days work thanks to routine, hierarchy and purpose; US 1960s shelter tests found **heat, crowding and lack of leadership** were the stressors.
- **Practical rules** [K]/[E]: fixed daily schedules and work rotation; an artificial day–night cycle with light; exercise; some **privacy** (curtains, bunks); a clear **command structure accepted before entry**; transparent rationing; written rules on alcohol, weapons storage and conflict; mental-health surveillance (the doctor is also the psychiatrist); information discipline (rumour is corrosive); **contact with the outside** (radio) for morale; burial and death protocols.
- **Selection** (who gets in) is the real moral core, and a natural driver for the campaign. [E]

## C.11 Capacity planning worksheet [E] (calculation)

Example: **50 people for 30 days** of full occupancy.

| Resource | Rule of thumb | Total |
|---|---|---|
| Drinking and cooking water | 5 L per person per day | 7,500 L |
| Minimal hygiene water | 5–10 L per person per day | 7,500–15,000 L |
| Food (dry staples) | 0.65 kg per person per day | about 1 t |
| Freeze-dried alternative | about 0.5 kg per person per day | about 750 kg, much more volume |
| Filtered fresh air | a few m³/h per person in filter mode; 15–30 m³/h per person for comfort | 150–1,500 m³/h |
| CO₂ produced | 1 kg per person per day | 50 kg/day |
| Heat released | 100 W per person | 5 kW continuous |
| Diesel | 10–15 kW average load | about 2,500–4,000 L |
| Floor area | at least 1 m² per person (Swiss minimum), comfortably 3–5 m² | 50–250 m² plus storage |
| Waste | 0.5–1 kg per person per day | 750–1,500 kg |

Scale linearly. **100 people for 1 year** needs about 180 m³ of drinking and cooking water, about 24 t of dry food and 40–60 m³ of diesel. At that point the "bunker" is really a **logistics base with a well, a fuel farm and a supply chain**. [E]

## C.12 Costs

### Real private bunkers abroad (for scale and character)

| Example | Price | Tag |
|---|---|---|
| **Vivos xPoint** (South Dakota): about 575 former army munitions bunkers sold as long leases | A few tens of thousands of USD up front plus about US$1,000 a year in ground rent | [K~] |
| **Survival Condo Project** (Kansas): a converted Atlas missile silo with about 15 floors, built for a few dozen people for years | Half-floor units about **US$1.5 million**, full floors about **US$3 million**, penthouse about **US$4.5 million** (2017 reporting) | [K~] |
| **Rising S**, **Atlas Survival Shelters** (US) | Steel shelters from tens of thousands of USD to multi-million custom installations | [K~] |
| **New Zealand "billionaire bunkers"** | Peter Thiel's NZ citizenship (granted 2011, revealed 2017). Evan Osnos's 2017 *New Yorker* piece "Doomsday Prep for the Super-Rich" shaped the image of Silicon Valley money buying refuges in NZ. | [K] |
| **Mark Zuckerberg's Kauai compound** | Reportedly includes a large underground shelter (*Wired*, 2023) | [K~] |
| **Switzerland** | Shelters are mandatory: about **9 million places**, more than the population. Owners who build none pay a replacement contribution of the order of CHF hundreds per place. | [K]/[?] |

### Chile: rough costs, 2005 and 2025 [E]

Reference values [K~]: US$1 ≈ CLP 560 (2005) and ≈ CLP 940–960 (2025). UF (Unidad de Fomento, the inflation-indexed unit used for property and construction) ≈ CLP 17,300 (Jan 2005) and ≈ CLP 38,500–39,500 (2025). Chilean prices roughly doubled in pesos between 2005 and 2025.

| Item | 2005 | 2025 | Notes |
|---|---|---|---|
| Normal deep basement (car-park grade) in Santiago | About US$400–700/m² | About US$700–1,200/m² | Includes excavation, retaining walls and slabs |
| Hardened shelter structure (thick slabs, blast-rated, seismic) | About US$900–1,600/m² | About US$1,500–3,000/m² | Engineering, imported doors and valves extra |
| Swiss-type NBC ventilation set (fan, gas filter, blast valves) for 50 people | About US$10–25k | About US$20–50k | Imported (CIF); add customs and installation |
| Blast door (imported) | About US$8–20k | About US$15–50k | Each |
| Diesel generator, 100 kVA, with sound enclosure | About US$15–25k | About US$25–45k | Plus tank and permits |
| Diesel fuel per litre | About CLP 400–450 | About CLP 950–1,100 | Prices vary weekly |
| A year of dry staples for one person | About US$150–250 | About US$300–500 | Rice, beans, flour, oil, sugar |
| A year of freeze-dried food for one person | About US$2,000–3,500 | About US$4,000–7,500 | Imported |
| Household water tank, 5,000 L | About CLP 300–400k | About CLP 600–900k | |
| Well, 80–120 m, with pump (Santiago) | About CLP 8–15 million | About CLP 20–45 million | Depends on depth, permits and casing |
| **A 300 m² hardened shelter for 50 people, fully fitted (structure, air, power, water, 1 year of stores)** | **About US$0.6–1.2 million** | **About US$1.2–3 million** | Excluding land; much higher if built under an existing building in the centre |

The DM should treat these as order-of-magnitude figures. The founder's real cost driver is **secrecy**: building in central Santiago without the DOM, neighbours, the SEC or the press noticing. [E]

## C.13 Chilean law

### Building underground

- **Permits.** Any construction, including underground levels, needs a **"permiso de edificación"** from the municipality's **Dirección de Obras Municipales (DOM)** under the **Ley General de Urbanismo y Construcciones (LGUC, DFL 458/1975)** and its **Ordenanza (OGUC)**. That requires plans signed by an architect, a structural engineer's calculations (seismic code NCh 433), a soil-mechanics study and a final reception certificate ("recepción final"). [K]
- **Ownership of the subsoil.** Under the Civil Code a landowner owns the subsoil beneath the land, but **minerals belong to the state**. **Building under a street, square or other public property ("bien nacional de uso público")** needs a **concession**, as Santiago's underground car parks under squares and avenues have. [K~]
- **Metro, utilities and heritage.** Building near Metro tunnels requires coordination with Metro S.A. (there are protection corridors). Utility easements must be respected. In the historic centre, **heritage zones and national monuments** (Consejo de Monumentos Nacionales) restrict excavation; archaeological finds stop work. [K~]/[E]
- **Concealment in fiction.** A "basement extension", "archive", "server room", "parking expansion" or "water-storage tank" filed under a legitimate permit is the plausible cover. Old structures can be "regularised" later through periodic **regularisation laws** ("leyes del mono"). [K~]/[E]

### Fuel and electrical installations

- **Liquid fuels** are regulated by **DS 160/2008**, the safety regulation for production, storage and supply of liquid fuels, enforced by the **SEC** (Superintendencia de Electricidad y Combustibles). Tanks above certain sizes must be **declared or registered with the SEC** and built and inspected to its rules, with special requirements for buried tanks (double walls, leak detection). Fire codes and Bomberos also apply. [K~]
- **Large diesel stocks in a city basement** (thousands of litres) are legally very difficult; they are usually placed in a separate vault or outside. [E]
- **Electrical installations**, including generators and transfer switches, must be declared to the SEC by an **authorised electrician (the "TE1" declaration)** and comply with the **RIC** consumer-installation rules (DS 8/2019 and its technical annexes). [K~]
- **LPG** has its own SEC safety regulations; large tanks need permits. [K~]

### Firearms: Ley 17.798 (Control de Armas)

- **Framework.** **Ley 17.798 (1972)**, with a consolidated text in DS 400/1978 and its regulations. The supervising authority is the **DGMN** (Dirección General de Movilización Nacional, part of the Defence Ministry), operating through local **Autoridades Fiscalizadoras**, mostly Carabineros units and garrisons. [K]
- **Ownership.** Adults with a clean record, residence, and certificates of **physical and psychological fitness** plus knowledge of firearms may **register ("inscribir")** permitted weapons for specific purposes: personal defence or security, hunting, sport shooting or collecting. **Registration allows keeping the weapon only at the registered address ("tenencia").** **Carrying ("porte")** needs a separate, exceptional permit, which has become very rare. **Automatic weapons, modified or home-made firearms and many military-pattern items are prohibited.** [K]
- **The 2005 reform (Ley 20.014)** tightened registration and increased penalties. **The 2015 reform (Ley 20.813)** further toughened penalties (illegal possession, firing in public), required periodic aptitude checks and strengthened the registry. **The 2022 reform (Ley 21.412)** capped the number of firearms per person for defence purposes (with broader allowances for registered sport shooters, hunters and collectors), tightened **ammunition control** with purchase limits tied to each registered weapon and purpose, added renewal requirements, and created tracing obligations. [K~] **Exact ammunition caps and renewal intervals should be checked in the current text** at bcn.cl/leychile and in the latest regulation. [?]
- **Game implication.** A legally armed bunker in Santiago has **a few registered handguns and shotguns, kept at the registered address, with modest ammunition**. Anything more is a felony with heavy prison terms, and the DGMN registry is exactly what a state-of-catastrophe requisition or police raid would consult. [E]

### Radio

- Amateur licences are issued by **Subtel**, in categories from entry level ("Aspirante/Novicio") to General and Superior, valid **5 years**. Foreigners resident in Chile with a licence from a country that has a reciprocity agreement can obtain temporary licences. Repeaters and higher power need higher categories and specific authorisations. [V]/[K~]
- Commercial and private radio networks (VHF/UHF business radio) need Subtel concessions or permits. Unlicensed HF use is illegal but practically undetectable in a collapse. [K]/[E]

### Water wells

- Domestic wells on one's own land are allowed by the Water Code for drinking and domestic use (C.5, A.1). Larger extraction needs **DGA water rights**, and much of the Santiago basin restricts new rights. After the 2022 reform, new rights are temporary (30 years). Drilling companies and well registration are regulated; check current rules. [K]/[?]

### Other relevant law

- **Controlled drugs.** Ley 20.000 and the **ISP** (Instituto de Salud Pública) regulations govern opioids, benzodiazepines and other controlled drugs (special prescription forms, the "receta cheque"). A private emergency network can hold them only under its ISP and health-authority authorisations, which makes a hidden stockpile of controlled drugs a legal liability. [K]
- **Medical oxygen** is a medicine regulated by the ISP, and its supply chain is concentrated in a few companies. [K~]
- **The Ley de Urgencia (19.650)** obliges any provider to treat life-threatening emergencies (A.7). [K]
- **Requisition under an estado de catástrofe** (A.8). [K]

## C.14 Prepper culture in Chile

- **The driver is earthquakes.** Chile has had a national culture of seismic preparedness since 1960 (Valdivia, Mw 9.5, the largest earthquake ever recorded), reinforced by 1985, 2010, 2014 and 2015. School drills ("operación Deyse"), building codes and tsunami evacuation signs are part of daily life. [K]
- **SENAPRED** (Servicio Nacional de Prevención y Respuesta ante Desastres) replaced ONEMI in 2023 under Ley 21.364 (2021). Its public messaging promotes a household **"kit de emergencia" / "mochila de emergencia"** for about **72 hours**: water, non-perishable food, a battery radio, a torch, a first-aid kit, documents, cash, medicines, warm clothes and a whistle. [K~]
- **Reality:** most households keep little beyond a torch and some water, and panic buying in every crisis (2010, 2019, 2020) shows it. [E]
- **No organised Chilean prepper movement or domestic bunker industry could be documented** in this pass. [V: none found] Chile has survivalist interest online, and outdoor and trekking culture (the Andes, Patagonia) supplies skills and gear. [E] This gap is useful for the game: the protagonist's network can be genuinely unique.
- **Patagonia and foreign land buyers.** Douglas and Kristine Tompkins bought vast areas of Chilean Patagonia from the 1990s and donated them to create national parks (Pumalín, Patagonia), handed over around 2017–18. Sebastián Piñera's Parque Tantauco in Chiloé. In Argentina, Joe Lewis's estate at Lago Escondido. Patagonian land purchases by foreigners have been a recurrent sovereignty controversy. [K]
- **The "Argentina survives" meme.** After Xia et al. (2022), Argentine and international press ran headlines calling **Argentina "the best country to survive a nuclear war"**, alongside Australia. [V] In a Santiago game, that framing becomes a political and migratory pull **across the Andes**.
- **The New Zealand narrative.** Since 2017, NZ has been the global shorthand for the billionaire bolt-hole. In fiction, a Chilean elite would plausibly have hedged with Patagonian estances, Uruguay or NZ passports, and **private underground space in Santiago's wealthy east**. [K]/[E]

---

# PART D — Hooks for play (FICTION IDEAS, not facts)

1. **The 34-hour clock.** A warm storm hits the Cajón del Maipo while the network is busy with something else. Aguas Andinas' raw-water reserve starts counting down. The bunker has a well; the building above does not. Who gets water, and who learns that you have it?
2. **Nivel 2.** Four hours after the grid fails, the antennas begin to die. The network's ambulances carry HF radios; SAMU does not. A Carabineros officer asks to "borrow" the channel and never gives it back.
3. **The 25-day lie.** The fuel law says 25 days, but the Maipú terminal holds three. A Sonacol engineer on the network's patient list knows exactly how much diesel sits in which tank, and what it would take to open a valve.
4. **Requisition order.** On day 3 of an estado de catástrofe, the Jefe de la Defensa Nacional's staff arrive with a list: generators, oxygen concentrators and ambulances registered with the SEC and the ISP. The founder hid nothing from the paperwork and everything from the press. Now the paperwork is the threat.
5. **The fault under the vault.** A geotechnical report commissioned in 2008 for the founder's deepest bunker, under a private clinic in the east, sits 400 m from the mapped San Ramón trace. The engineer who signed it is still alive and remembers.
6. **The electro-dependent list.** A distribution company's register of home-ventilator patients leaks during a blackout. Families start arriving at the unit's door with oxygen tubing in their hands. There are more patients than concentrators.
7. **Argentina's wheat.** In a nuclear-winter year, a shipment of Argentine wheat is held at the Los Libertadores pass by snow and politics. A mining-company convoy, private security and a sympathetic customs officer could get some of it through, for a price.
8. **The curfew pass.** A movement permit (the old "Comisaría Virtual" logic, now on paper because the servers are down) is the most valuable document in Santiago. The founder's network has a medical exemption, and someone is forging copies.
9. **Ghost auroras.** During a solar storm, the sky above Santiago glows red. Old men in the network tell the heir about the 1859 auroras recorded in Chile. Within a day the CEN has lost three transformers at Polpaico, and the waiting list for replacements is longer than the war that caused it.
10. **The cellar beneath the cellar.** Under a 1920s building in the centre, the inherited plans show a "colonial canal". It is real, and it links two of the old men's bunkers. One of them was never sealed from the Mapocho side.
11. **Sealed mode.** A fire above (a looted supermarket, a burning tower) forces the bunker to close its intakes. The CO₂ meters start climbing. The lithium hydroxide stock is enough for 18 hours. The fire department's estimate is 30.
12. **The quarantine airlock.** In a pandemic, a nurse from the network arrives feverish at the bunker door with the only person who knows the generator's maintenance codes.
13. **Jurel and harina tostada.** Month four of rationing: the bunker's stores are good, but the neighbours can smell cooking through the ventilation exhaust. The ollas comunes outside are running dry.
14. **The DGMN registry.** The founder's legally registered weapons are exactly three. The bunker holds forty. A former army officer on the payroll knows both numbers.
15. **The CCHEN rumour.** A false rumour spreads that the research reactor in La Reina is "leaking" after an earthquake. Panic sends the eastern comunas into the streets, and toward the clinic network, at the worst possible hour.

---

## Sources

**Retrieved and used during compilation** (press, official documents and abstracts, via search retrieval or PubMed):

*Water*
- Chilevisión, "Inauguran seis megaestanques en Pirque…": https://www.chilevision.cl/noticias/reportajes/cronicas/inauguran-seis-megaestanques-en-pirque-para-enfrentar-futuros-cortes-de
- Diario Financiero via Infraestructura Pública, "La estrategia de Aguas Andinas…": https://www.infraestructurapublica.cl/wp-content/uploads/2021/02/La-estrategia-de-Aguas-Andinas-para-respaldar-el-abastecimiento-de-Santiago-Diario-Financiero.pdf
- Pauta (23 Jun 2023): https://www.pauta.cl/actualidad/2023/06/23/cortes-de-agua-aguas-andinas-reporta-cortes-y-uso-de-estanque-de.html
- Emol (23 Jun 2023): https://www.emol.com/noticias/Nacional/2023/06/23/1099060/confirman-suspension-agua-34-comunas.html
- The Clinic (27 Feb 2017): https://www.theclinic.cl/2017/02/27/pregunta-existencial-por-que-chucha-tanto-corte-de-agua-potable-en-santiago/
- El Dínamo (2017): https://www.eldinamo.cl/tendencias/2017/04/21/tuit-de-aguas-andinas-deja-en-evidencia-que-la-empresa-no-tiene-idea-donde-esta-parada/
- Meteored, El Yeso: https://www.meteored.cl/noticias/ciencia/embalse-el-yeso-descargas-controladas-para-proteger-comunidades-y-optimizar-recursos-hidricos.html
- Chilevisión, El Yeso in drought: https://www.chilevision.cl/noticias/reportajes/cronicas/embalse-el-yeso-en-crisis-zona-central-registro-la-decada-mas-seca-de-la-historia/
- MCH, El Yeso 2016: https://www.mch.cl/aguas-andinas-llenado-del-embalse-el-yeso-asegura-agua-para-2016/

*Power and the 25F blackout*
- Ex-Ante (25 Feb 2025): https://www.ex-ante.cl/?p=272580
- Ex-Ante, final report to the investigative commission: https://www.ex-ante.cl/economia/la-cadena-de-errores-que-evidencio-el-informe-final-enviado-a-la-comision-investigadora-sobre-el-apagon-del-25f/
- CNN Chile (7 Mar 2025): https://www.cnnchile.com/pais/informe-isa-intervencion-reporte-cen_20250307/
- Reporte Minero: https://www.reporteminero.cl/noticia/noticias/2025/02/apagon-chile-acera-autoridades-sectoriales-investigacion
- La Tercera, CEN audit of Interchile: https://www.latercera.com/pulso/noticia/cordinador-electrico-nacional-anuncia-auditoria-contra-interchile-por-posibles-infracciones-en-linea-que-causo-el-apagon/
- Infobae (25 Feb 2025): https://www.infobae.com/america/america-latina/2025/02/25/masivo-corte-de-luz-en-chile-cientos-de-miles-de-personas-estan-sin-electricidad-y-varios-servicios-basicos-estan-afectados/
- Interferencia: https://interferencia.cl/articulos/masivo-apagon-electrico-deriva-en-toque-de-queda-y-despliegue-de-militares-la-espera-de
- Diario de Cuyo (207 detained, 3 deaths): https://www.diariodecuyo.com.ar/argentina/tras-el-toque-de-queda-en-chile-investigan-la-muerte-de-tres-personas-durante-el-apagon-y-hay-207-detenidos-1707701.html
- Primicias: https://primicias.ec/internacional/causas-apagon-masivo-chile-empresas-sistema-90654
- Emol, SEC fine on Enel (Jan 2025): https://www.emol.com/noticias/Nacional/2025/01/22/1155004/sec-multa-enel-corte-luz.html
- Enel, Sernac compensation (Feb 2025): https://enel.cl/content/dam/enel-cl/prensa/comunicados-enel-distribucion/2025/20250204-CP-Enel-Distribucion-PVC-Sernac.pdf
- Radio U. de Chile (Sep 2026 outage): https://radio.uchile.cl/2026/09/26/masivo-apagon-afecta-a-casi-130-mil-clientes-en-la-capital-e-interrumpe-el-servicio-de-metro/

*Telecommunications and radio*
- Ex-Ante, why mobile phones failed: https://www.ex-ante.cl/por-que-fallaron-los-celulares-durante-el-masivo-corte-de-luz/
- DF, Subtel 6-hour decree: https://www.df.cl/empresas/telecom-tecnologia/subtel-ya-tramita-decreto-que-aumenta-a-6-horas-el-respaldo-electrico-para
- TeleSemana (Feb 2025): https://www.telesemana.com/blog/2025/02/28/el-apagon-de-chile-obliga-a-acelerar-cambios-para-extender-la-autonomia-de-las-baterias-de-las-antenas/
- TeleSemana (Oct 2026): https://www.telesemana.com/blog/2026/10/20/subtel-oficia-a-las-operadoras-para-reforzar-redes-y-energia-ante-lluvias-en-chile/
- DPL News: https://dplnews.com/chile-apagon-electrico-y-la-autonomia-de-las-baterias-de-las-antenas-celulares/
- Radio Club de Chile, 27F presentation (2010): https://www.ce3aa.cl/wp-content/uploads/2010/10/descargas_garec2010cch.pdf
- ChileAtiende, amateur licences: https://chileatiende.gob.cl/fichas/16934-licencia-temporal-para-radioaficionados-extranjeros

*Fuel and gas*
- Valora Analitik (Sonacol): https://www.valoraanalitik.com/?p=62177
- Global Energy Monitor, Concón–Maipú LPG pipeline: https://gem.wiki/Conc%C3%B3n-Maip%C3%BA_LPG_Pipeline
- The Clinic, Maipú–airport pipeline (2020): https://www.theclinic.cl/2020/01/22/vecinos-de-maipu-se-preparan-para-enfrentar-cuestionado-oleoducto-que-pasaria-a-metros-de-sus-casas/
- Meganoticias, ENAP's supply share (Mar 2026): https://www.meganoticias.cl/nacional/517895-alza-combustibles-enap-problemas-abastec-opera-sin-interrupciones-24-03-2026.html
- Ley 18.179 (CNE PDF): https://www.cne.cl/wp-content/uploads/2015/07/Ley18179_xDoc_7x.pdf
- Portal Minero, Aconcagua 70 years: https://www.portalminero.com/refineria-aconcagua-de-enap-cumple-70-anos-de-operaciones
- Diario Concepción, ENAP supplement (2023): https://assets.diarioconcepcion.cl/2023/07/EE-ENAP.pdf
- Cooperativa (2007, LNG contracts): https://cooperativa.cl/noticias/pais/energia/gas-natural/empresas-firmaron-contratos-para-asegurar-suministro-de-gnl-a-planta-de-quintero/2007-06-02/173753.html
- EJU (2009, first LNG cargo): https://eju.tv/2009/06/chile-recibe-gnl-por-mar-y-se-cierra-al-gas-boliviano/
- CAI Law, "LNG in Chile" (2014): https://www.cailaw.org/media/files/IEL/Publications/2014/ela-lng-chile-vol8-no4.pdf
- Emol, Argentine gas cut (Jul 2025): https://www.emol.com/noticias/Economia/2025/07/03/1171145/gas-empresas-chile-argentina.html

*Food*
- BioBioChile (Apr 2026, Lo Valledor share): https://www.biobiochile.cl/noticias/economia/actualidad-economica/2026/04/16/llamando-a-cotizar-precios-gobierno-recibe-la-temporada-otono-invierno-de-frutas-y-verduras.shtml
- Ex-Ante, Lo Valledor chronicle: https://www.ex-ante.cl/nacional/cronica-amanecer-en-el-mercado-lo-valledor-el-pulmon-agricola-de-santiago-que-nunca-duerme/
- Radio Agricultura, La Vega spokesman (2020): https://www.radioagricultura.cl/noticias/nacional/vocero-de-la-vega-central-y-posible-desabastecimiento-en-santiago-teniendo-abierto-lo-valledor-nosotros-y-las-ferias-libres-no-deberia-pasar_20200505/
- BioBioChile, CNC March 2020 sales: https://www.biobiochile.cl/noticias/economia/actualidad-economica/2020/04/27/solo-se-salvaron-los-supermercados-ventas-presenciales-en-el-comercio-se-desplomaron-en-marzo.shtml
- Portal Innova / Teamcore: https://portalinnova.cl/?p=10551

*Social order, population, transport*
- Memoria Chilena, 27F: https://www.memoriachilena.gob.cl/602/w3-article-93853.html
- El Universo (1 Mar 2010, Concepción curfew): https://www.eluniverso.com/2010/03/01/1/1361/160-detenidos-concepcion-primera-noche-toque-queda.html
- Cooperativa (7 Mar 2010): https://cooperativa.cl/alcaldesa-de-concepcion-que-por-ningun-motivo-se-vayan-los-militares/prontus_nots/2010-03-07/184940.html
- La Izquierda Diario (troop numbers): https://www.laizquierdadiario.com/Militares-en-las-calles-una-vez-mas
- Pauta fact-check, Metro US$255m: https://www.pauta.cl/factchecking/el-contestadog/metro-costos-estaciones-estallido-social-18-octubre-255-millones-dolares
- DF / LyD, cost of the first month (2019): https://infraestructurapublica.cl/wp-content/uploads/2019/11/Balance-de-LyD_-ms-de-US-6300-millones-suma-costo-econmico-del-primer-mes-de-disturbios-Diario-Financiero.pdf
- Ex-Ante, Fiscalía figures: https://www.ex-ante.cl/hubo-violencia-pero-contenida-las-cifras-que-desbaratan-los-dichos-de-bassa-sobre-el-18-o/
- Ex-Ante, curfew comparison: https://www.ex-ante.cl/internacional/coronavirus-chile-esta-entre-los-5-paises-con-los-toques-de-queda-mas-largos-del-continente/
- Montevideo Portal, end of curfew: https://www.montevideo.com.uy/Archivo/Finaliza-el-toque-de-queda-en-Chile-despues-de-un-ano-y-medio-uc799838
- BioBioChile, Carabineros headcount (Apr 2026): https://www.biobiochile.cl/especial/bbcl-investiga/noticias/articulos/2026/04/23/carabineros-opera-con-12-222-vacantes-y-perdio-cerca-de-5-mil-policias-de-calle-desde-2019.shtml
- Diario Oficial, Ley 21.542 (2023): https://www.diariooficial.interior.gob.cl/publicaciones/2023/02/03/43468/01/2266620.pdf
- El Dínamo, Censo 2024: https://www.eldinamo.cl/pais/2025/03/27/se-acabo-la-incognita-censo-2024-contabilizo-18-480-432-habitantes-en-chile/
- Emol, Metro at 50 (2025): https://www.emol.com/noticias/Nacional/2025/09/15/1177890/desafios-metro-santiago-50-anos.html
- El Universo, airport after 27F: https://www.eluniverso.com/2010/02/27/1/1361/aeropuerto-santiago-cerrado-menos-24-horas.html
- DF, airport reopening: https://www.df.cl/empresas/aeropuerto-de-santiago-restablecera-el-viernes-salidas-internacionales
- El Mercurio (28 Feb 2010, scan): https://ucolick.org/~plynam/DOCUMENTS/ARTICLES/2010-02-28--El_Mercurio.pdf
- CEP, Santiago air-pollution chapter: https://static.cepchile.cl/uploads/cepchile/2022/09/12_cap3escudero_libromambiente.pdf
- Meteored, thermal inversions: https://www.meteored.cl/noticias/ciencia/inversiones-termicas-y-su-influencia-en-la-contaminacion-del-aire.html

*Nuclear war, fallout, food*
- Xia L. et al. (2022), *Nature Food* 3:586–596, doi:[10.1038/s43016-022-00573-0](https://doi.org/10.1038/s43016-022-00573-0) (abstract retrieved via PubMed)
- University of Colorado press release (2022): https://www.colorado.edu/today/2022/08/15/nuclear-war-would-cause-global-famine-and-kill-billions-study-finds
- El Economista (Argentina), "mejor lugar para sobrevivir": https://eleconomista.com.ar/actualidad/argentina-mejor-lugar-mundo-sobrevivir-una-guerra-nuclear-n55491
- Jägermeyr J. et al. (2020), *PNAS* 117:7071–7081, doi:10.1073/pnas.1919049117: https://pure.iiasa.ac.at/16344
- Scherrer K. et al. (2020), *PNAS* 117(47), doi:10.1073/pnas.2008256117: https://data.ucar.edu/dataset/marine-wild-capture-fisheries-after-nuclear-war
- Coupe J. et al. (2019), WACCM 150 Tg dataset: https://data.ucar.edu/dataset/nuclear-winter-responses-to-nuclear-war-between-the-united-states-and-russia-in-the-whole-atmos
- New Zealand nuclear-winter food study (*Sci Rep* 2023): https://pmc.ncbi.nlm.nih.gov/articles/PMC10202904/
- ALLFED 2023 highlights: https://forum.effectivealtruism.org/posts/YzCF2NDLSwKayZXb7/allfed-s-2023-highlights
- DTIC, hemispheric fallout report: https://apps.dtic.mil/sti/pdfs/AD0642279.pdf
- University of Idaho extension, fallout decay: https://objects.lib.uidaho.edu/uiext/uiext18751.pdf

*Solar storms*
- Brazilian GIC study, 2015 storms (*JSWSC*): https://www.swsc-journal.org/articles/swsc/pdf/2015/01/swsc150056.pdf
- Low-latitude GIC estimation (ESSOAr): https://essopenarchive.org/doi/full/10.1002/essoar.10500842.1
- Wood Mackenzie, transformer lead times: https://woodmac.com/news/opinion/supply-shortages-and-an-inflexible-market-give-rise-to-high-power-transformer-lead-times
- Utility Dive: https://www.utilitydive.com/news/electric-transformer-shortage-nrel-niac/738947/
- POWER magazine (2026): https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis
- WAPA, supply chains: https://www.wapa.gov/supply-chains/
- ENR, Carrington probabilities: https://www.enr.com/articles/42151-space-weather-are-solar-storms-oversold-as-a-hazard
- Open Philanthropy, Carrington analysis: https://www.openphilanthropy.org/?p=3282
- BBVA OpenMind (Lloyd's figure): https://www.bbvaopenmind.com/en/science/environment/when-will-the-next-solar-superstorm-occur/
- Emol, auroras in Chile (May 2024): https://www.emol.com/noticias/Nacional/2024/05/10/1130490/aurora-austral-chile-tormenta-solar.html
- BioBioChile, auroras after 165 years: https://www.biobiochile.cl/noticias/ciencia-y-tecnologia/astronomia/2024/05/11/amp/tras-165-anos-se-vieron-auroras-australes-en-el-sur-de-chile-asi-fue-el-ultimo-registro-del-fenomeno.shtml
- Switchgear Magazine, HVDC Kimal–Lo Aguirre: https://switchgear-magazine.com/news/technology/chile-starts-3-gw-hvdc-power-line/

*Earthquakes and volcanoes*
- IPGP, San Ramón trenching: https://www.ipgp.fr/~lacassin/RL-TectoniqueIPGP/Past-earthquakes_San_Ramon_Fault.html
- *NHESS* 2020 review: https://nhess.copernicus.org/articles/20/1533/2020/
- Estay et al., *NHESS* 2016: https://nhess.copernicus.org/articles/16/2511/2016/
- Domínguez & Heresi (SECED): https://www.seced.org.uk/images/newsletters/ID145_Dominguez_Pablo_Heresi.pdf
- La Tercera, San Ramón simulation: https://www.latercera.com/que-pasa/noticia/santiago-oriente-lo-sentiria-mucho-mas-fuerte-simulan-como-seria-un-terremoto-en-la-falla-san-ramon/2E5ESJDWEZBQJD3ZP5UBX53M7Q/
- Meganoticias, 2026 Universidad de los Andes study: https://www.meganoticias.cl/nacional/520686-estudio-terremoto-falla-san-ramon-impacto-edificios-santiago-28-04-2026.html
- Pauta, Tupungatito ranking (2025): https://www.pauta.cl/ciudad/2025/03/27/volcan-tupungatito-numero-31-del-ranking-de-riesgo.html
- La Tercera, volcanoes threatening Santiago: https://www.latercera.com/que-pasa/noticia/columna-de-sismologia-arriba-en-la-cordillera-o-los-desconocidos-volcanes-que-amenazan-a-santiago/C7TNLO3LSZGNTNP3YVM4SPE3EQ/

*Medicine*
- Lyon R.C. et al. (2006), "Stability profiles of drug products extended beyond labeled expiration dates", *J Pharm Sci* 95(7):1549–60, doi:[10.1002/jps.20636](https://doi.org/10.1002/jps.20636) (via PubMed)

**Standard references relied on but not re-opened in this pass** ([K] items): Glasstone & Dolan, *The Effects of Nuclear Weapons* (3rd ed., 1977); Kearny, *Nuclear War Survival Skills* (1987); Robock, Oman & Stenchikov (2007) *JGR*; Coupe et al. (2021) *GRL*; Bardeen et al. (2021) *JGR Atmospheres*; Lloyd's/AER (2013) *Solar Storm Risk to the North American Electric Grid*; Riley (2012) *Space Weather*; Armijo et al. (2010) *Tectonics*; Vargas et al. (2014) *Geology*; Sphere Handbook (2018); Swiss BABS technical directives for shelters (TWP 1984 and successors); CR2 (2015) *La megasequía 2010–2015*; Constitución Política arts. 39–45; Ley 17.798, 20.014, 20.813, 21.412; Ley 20.478 and DS 60/2012; DS 160/2008; LGUC/OGUC; Código de Aguas and Ley 21.435; Ley 19.650; Ley 21.364; Osnos (2017) *The New Yorker*.

## Gaps and things to verify before relying on them

1. **Water system internals**: treatment-plant capacities (m³/s), how the network behaved on 25F, and the status of the El Manzano–Pique project (48 h of autonomy).
2. **Hospital generator autonomy**: no Chilean rule was found. Ask MINSAL or the Superintendencia de Salud, or use the [E] range.
3. **Firearms**: the exact ammunition caps, weapon limits and renewal intervals under Ley 21.412 and its regulation. **Check bcn.cl before writing any scene that depends on them.**
4. **Water law**: the current wording of article 56 (domestic wells) after the 2022 reform.
5. **Megadrought numbers** (Santiago rainfall in 2019, the details of the 2022 rationing protocol) were not re-verified.
6. **Xia et al. 2022, country-level values for Chile** were not extracted (they are in the paper's supplementary data). Argentina's relative resilience is verified; Chile's exact projected calorie change is not.
7. **No Chile-specific study of geomagnetically induced currents** exists in the accessible literature, so the solar-storm duration estimates are reasoned.
8. **Bunker and equipment prices** (Vivos, Survival Condo, Andair, Swiss replacement contributions) and all Chilean cost estimates are approximate.
9. **The Diamante caldera / Pudahuel ignimbrite** age and volume.
10. **PDI and armed-forces headcounts** and the numbers of licensed radio amateurs and registered firearms in Chile.
