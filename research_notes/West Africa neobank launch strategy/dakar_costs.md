# Dakar (and Abidjan) operating cost research — fintech / neobank launch

*Compiled 8 October 2026. All amounts in FCFA (XOF), 1 EUR = 655.957 FCFA (fixed peg); 1 USD ≈ 560–600 FCFA (2025–26 range; use 580 for planning).*

**Reliability flags used throughout**
- **[A]** = official / primary (government, social-security body, CLEISS, Big-4 tax guide, vendor's own price page)
- **[B]** = credible secondary (recruitment firm survey, established payroll/EOR provider, reputable press citing a survey)
- **[C]** = indicative only (blogs, content-marketing salary pages, aggregators like SalaryExplorer/Paylab/Glassdoor with small samples, AI-written "guides")
- **[E]** = my estimate/derivation from the above

**Headline planning numbers (detail and sources below)**
- Loaded-cost multiplier on gross salary: **×1.09–1.11 statutory** for cadres at 0.8–1.3M gross (×1.16 for 250k staff, ×1.06 for 2.5M execs) → **×1.25 recommended** for a competitive fintech package (13th month, private health top-up, transport). Abidjan statutory ≈ ×1.13.
- Office: Point E / Mermoz / Sacré-Cœur ≈ **8,500 FCFA/m²/month** (Plateau 9–12k; Almadies 6–11k); coworking desk ≈ **70–150k FCFA/month**.
- OTP SMS via Orange API ≈ **4–10 FCFA**; WhatsApp utility ≈ USD 0.0045; KYC ≈ **USD 0.5–1.9 per onboarding**; card delivered ≈ **4–5k FCFA**.

---

## 1. Salaries — Dakar (gross monthly, FCFA)

### 1.1 Source landscape (read this first)
There is **no published 2025–26 recruiter salary survey for Senegal** from Michael Page/Hays/Robert Walters (Michael Page Africa only publishes South Africa/Mauritius guides — [michaelpageafrica.com salary guides](https://www.michaelpageafrica.com/advice/insights/salary-guides)). Available data are:
- **ANSD EERH (official, [A])** — quarterly survey of the modern sector; gives sector payroll and headcount, not role-level pay. Q4 2025: **Information & communication**: payroll 43,124 M FCFA for 7,508 employees → **≈1.9 M FCFA/employee/month** (dominated by Sonatel/Orange & large ICT firms; Q4 includes bonuses; 59% of the payroll goes to "cadres supérieurs"). **Financial & insurance activities**: 66,243 M FCFA for 53,437 employees → **≈410,000 FCFA/employee/month** (includes microfinance & many clerical staff). Whole modern sector (ex-public admin): 413.4 bn for 341,945 → **≈400,000 FCFA/month**. [ANSD EERH note d'analyse T4 2025 (PDF)](https://www.vie-publique.sn/docs/4a49ffef-91b5-47a0-94f5-6004cbc2a304/enquete-emploi-remuneration-heures-travail-eerh-note-analyse-t4-2025-ansd.pdf) — my per-head arithmetic [E].
- **Kolonell tech salary grid (Jun 2026, [C])** — Dakar digital agency blog; claims to use real Dakar offers and agency/startup pay, no sample. Explicitly says figures are "grands comptes" level and **local SMEs/startups pay 25–40% less**. [Grille complète 2026](https://kolonell.com/fr/blog/grille-salaires-metiers-tech-senegal-complete-2026); [web dev grid](https://kolonell.com/fr/blog/salaire-developpeur-web-senegal-grille-2026); [mobile dev](https://kolonell.com/fr/blog/salaire-developpeur-mobile-ios-android-senegal-2026); [by stack](https://kolonell.com/fr/blog/salaire-developpeur-par-stack-langage-senegal-2026).
- **Senego "salaire par métier 2026" ([C])** — media site, "indicative averages from surveys, postings and recruiter feedback", no sample. [Senego calculator](https://senego.com/services/calculateur-salaire-metier).
- **Africarrières grille (updated Aug 2026, [C])** — explicitly AI-assisted, some values "non confirmé"; tends low. [Africarrières grille](https://africarrieres.com/senegal/fr/guide/marche-emploi/grille-salaires).
- **Paylab Senegal ([C], likely understated)** — survey/modelled; e.g. Compliance specialist 107k–272k, AML specialist 82k–204k, Risk specialist 104k–261k, Software engineer ≈116k–451k/month. These are far below every other source and below what banks pay cadres; treat as floor for very small local firms. [Paylab banking SN](https://www.paylab.com/sn/salaryinfo/banking); [Paylab software engineer SN](https://paylab.com/sn/salaryinfo/information-technology/software-engineer?lang=en).
- **Job ads** rarely state pay in Senegal. Examples found: web developer Dakar 400–600k ("selon profil"); field sales/partnerships 100–110k fixed + 5% commission; another sales role 300k net + profit share; call-centre (PCCI, older articles) 120k base + bonuses, ~180k with bonuses. [C]

**Bottom line on reliability:** role-level figures below are triangulated from [C] sources plus ANSD sector averages; confidence is **medium for tech roles, low-medium for compliance/finance/exec roles**. Validate with 2–3 local recruiters (e.g. Africsearch, Grey Search Africa, Emerging Search, Tchad Recrutement/Sen Interim) before fundraising.

### 1.2 Premiums
- **Banks/telcos pay a premium**: ANSD shows ICT-sector average pay ~4.7× the modern-sector average; Senego bank grid (DG/DGA 2–5M, department heads 1.0–1.8M, credit analysts 0.4–0.7M) sits well above Africarrières general grids. Kolonell: SMEs/startups pay 25–40% below "grands comptes". **Fintechs (Wave, Djamo, Orange Money/Max it, Free Money/Mixx, Kalpé etc.) recruit from banks/telcos and must roughly match bank packages for compliance/risk/finance, and pay above banks for engineers.** [E]
- **Remote/foreign-client effect**: real and large for senior engineers. Kolonell: senior local vs remote-international — DevOps 1.7–3.0M vs 2.8–5.0M+; data scientist 1.5–2.8M vs 2.5–4.5M; architect 1.8–3.0M vs 3.0–5.5M; freelancers earn 30–60% more gross than salaried peers; senior mobile freelancers bill 90–180k FCFA/day. Lesafriques: a senior Dakar dev working for foreign clients earns 0.8–1.5M/month [C]. **Wave** (HQ Dakar operations) historically posted remote engineering roles at **USD 96k–178k** (e.g. Technical Lead Risk USD 124–170k + equity, 2021 posting [B, dated]) — i.e. the best Dakar engineers have a global-pay alternative. [concoursn repost of Wave ad](https://concoursn.com/wave-recruits-01-technical-lead-risk/)

### 1.3 Salary table & planning figures (gross monthly FCFA, Dakar, 2026)

| Role | Junior | Mid / confirmé | Senior / head | **Planning figure** | Sources / reliability |
|---|---|---|---|---|---|
| CEO / managing director (startup/SME, market rate, non-founder) | – | 1.5M–2.5M | 2.5M–5M (bank DG/DGA 2–5M) | **2.5M** (founders often take 1–1.5M pre-Series A) | Senego bank DG 2–5M; Africarrières directors 0.8–2.5M [C] |
| CTO / head of engineering | – | 1.5M–2.5M | 2.5M–4M (remote alt. 3–5.5M) | **2.5M** | Senego CTO 1.2–2.5M; Kolonell architect 1.8–3.0M, remote 3–5.5M [C] |
| Senior backend developer | – | – | 1.2M–2.2M (cloud-native/Go/K8s >1.2M; lead >2M) | **1.5M** | Kolonell [C]; Senego senior/lead 0.7–1.5M [C] |
| Mobile developer (Flutter/RN) | 350k–550k | 700k–1.2M | 1.3M–2.4M | **mid 0.9M; senior 1.5M** | Kolonell mobile grid [C] |
| Full-stack / web developer | 300k–500k | 600k–1.1M | 1.2M–2.2M | **mid 0.8M** | Kolonell; Senego 400–800k confirmed; job ad 400–600k [C] |
| Product designer (UI/UX) | 300k–500k | 550k–950k | 1.0M–1.8M | **mid 0.7M** | Kolonell; Senego 250–600k [C] |
| QA tester | 250k–400k | 400k–700k | 700k–1.0M | **0.5M** | No direct source — derived as ~60–70% of dev grid [E] |
| DevOps / cloud engineer | 450k–700k | 900k–1.6M | 1.7M–3.0M | **1.2M** | Kolonell [C] (scarce skill) |
| Head of compliance / AML officer (MLRO, "responsable conformité") | – | 0.9M–1.4M | 1.2M–2.0M | **1.5M** | Bank department-head band 1.0–1.8M (Senego) [C]; no posted salaries found (Djamo, Banque Atlantique ads silent) |
| Compliance / AML analyst | 300k–450k | 450k–750k | – | **0.55M** | Bank analyst band (Senego 0.4–0.7M) [C]; Paylab 107–272k (too low) [C] |
| Credit risk manager | – | 0.9M–1.4M | 1.2M–1.8M | **1.2M** | Senego dept head band [C] [E] |
| Credit analyst | 250k–400k | 400k–700k | – | **0.5M** | Senego 0.4–0.7M (3–7 yrs); Africarrières 0.3–0.45M [C] |
| Collections agent ("agent de recouvrement") | 150k–250k | 300k–450k | team lead 500k–900k | **250k + 10–20% variable** | legrandfrere.africa (West Africa) [C] |
| Customer support / call-centre agent | 120k–200k (+bonuses) | 200k–300k (bilingual/senior) | supervisor 350k–500k | **200k** | PCCI 120k base / ~180k with bonuses (older press) [C]; GoAfrica ads "fixe + prime" |
| KYC / onboarding operations agent | 180k–250k | 250k–400k | – | **275k** | Bank back-office/clientèle junior 180–400k (Africarrières, Senego) [C] |
| B2B sales rep / commercial terrain | fixed 100k–200k + commission | fixed 250k–400k + 20–40% variable | – | **300k fixed + ~100k avg commission** | Ads: 100–110k fixed + 5%; 300k net + intéressement; Senego bank agent 250–400k + 20–30% variable [C] |
| Head of sales / directeur commercial | – | 1.0M–1.5M | 1.5M–2.5M | **1.4M + 20–30% bonus** | Senego dept head band 1.0–1.8M [C] [E] |
| Partnerships manager | – | 600k–1.0M | 1.0M–1.5M | **0.9M** | [E] from PM/sales bands (Kolonell PM 0.7–1.2M) |
| Accountant / finance officer (comptable) | 200k–300k | 300k–550k | chef comptable 600k–1.0M | **0.4M** | Paylab 87–244k (low) [C]; [E] |
| Finance director / CFO | – | 1.5M–2.5M | 2.5M–3.5M | **2.0M** | Bank dept head 1.0–1.8M; DG/DGA 2–5M (Senego) [C] [E] |
| HR / admin assistant | 150k–250k | 250k–400k | – | **0.275M** | [E] (general formal-sector average 250–350k, Senego FAQ) |
| Country manager, Abidjan (Y2) | – | 2.0M–3.0M | 3.0M–4.5M | **2.8M** (+ housing/car if expatriate) | Africarrières CI bank director 2.5–4.0M [C]; Simoon (Orange CI 0.8–2.5M avg) [C]; Abidjan pays ~10–20% above Dakar for equivalent roles (Paylab CI accountant 130–442k vs SN 87–244k) [C] |

Salary inflation: WTW projected West-Africa salary budgets +7.5% in 2025 (vs 5.9% in 2024) [B] [WTW 2025 Africa salary budget trends](https://www.wtwco.com/en-eg/insights/2025/09/africa-2025-salary-budget-trends-regional-realities-and-strategies). In WAEMU (inflation ~1–3%), plan **+5–7%/yr** nominal raises, more for engineers.

---

## 2. Employer social charges & payroll taxes — Senegal (2026)

### 2.1 Statutory rates (valid 1 Jan 2026)

| Item | Employer | Employee | Monthly base / ceiling | Source |
|---|---|---|---|---|
| CSS – prestations familiales | 7% | – | ceiling **63,000** FCFA/month (→ max 4,410 FCFA/month) | [A] [CLEISS, cotisations au 1er janvier 2026](https://www.cleiss.fr/docs/cotisations/senegal.html); [A] [PwC Tax Summaries, Senegal – other taxes (reviewed 7 Aug 2026)](https://taxsummaries.pwc.com/senegal/corporate/other-taxes) |
| CSS – accidents du travail / maladies prof. | 1%, 3% or 5% (risk class set at registration; office/financial services normally 1%) | – | ceiling **63,000** (→ 630 FCFA/month at 1%) | same |
| IPRES – régime général (RG) | 8.4% | 5.6% | ceiling **432,000** (→ max 36,288 employer) | same |
| IPRES – régime complémentaire cadres (RCC) | 3.6% | 2.4% | base = slice **432,000 → 1,296,000** (→ max 31,104 employer) | [A] CLEISS (explicitly states "assiette comprise entre 432 000 et 1 296 000") |
| IPM (institution de prévoyance maladie – mandatory health cover, incl. 2% AMO levy passed to ICAMO) | 2%–7.5% (often ~3% each side, set by the IPM) | 2%–7.5% | ceiling **250,000** | [A] CLEISS; PwC says "6% on a basis between 60,000 and 250,000, shared equally" |
| CFCE (contribution forfaitaire à la charge de l'employeur) | **3%** of total gross salaries + taxable benefits | – | **no ceiling** | [A] PwC ("Employer tax: 3% of total gross salaries paid"); [C] [countrytaxcalc](https://www.countrytaxcalc.com/tax-guides/africa/senegal-paye-guide-2026/) |
| SMIG (minimum wage) | – | – | 371 FCFA/h × 173.33 h ≈ **64,300 FCFA/month** since 1 Jul 2023 | [A] CLEISS |

Notes:
- The CSS ceiling of 63,000 FCFA is very low, so CSS is near-negligible for professional salaries (≈5,040 FCFA/month max at 1% AT). Some blogs (e.g. [Kolonell, Jun 2026](https://kolonell.com/fr/blog/charges-sociales-ipres-css-senegal-calcul-2026) [C]) wrongly apply 7% to the full salary — ignore those worked examples.
- Ceiling history: IPRES ceilings raised 1 Apr 2022 from 360,000→432,000 (RG) and 1,080,000→1,296,000 (RCC). eRegulations still shows stale 256,000/768,000 figures — outdated [C].
- Older EOR guides citing "18%–31.5% employer burden" or "22–27%" are inconsistent with the statutory table above, unless they include private health insurance, 13th month, etc. Treat as [C].


### 2.2 Other employment costs and norms
- **Paid leave:** 24 working days/year (2 days per month of service), +1 day per 5 years' seniority (capped). [B] [WageIndicator Senegal – congé annuel](https://wageindicator.org/fr-sn/travail-au-senegal/droit-du-travail/conge-annuel-et-vacances); [C] [Africarrières – heures et congés](https://africarrieres.com/senegal/fr/guide/droit-du-travail/heures-et-conges). Leave pay is part of the annual salary (no extra cost beyond cover).
- **13th month / prime de fin d'année:** *not* a statutory obligation under the Labour Code or the national inter-professional collective agreement (CCNI) — I found no source saying otherwise. It is customary in banks (bank sector collective agreement) and many large firms; fintechs competing with banks typically offer a 13th month or an equivalent performance bonus. **Plan +8.3% for cadres.** [E]
- **Transport allowance (indemnité de transport):** customary/collective-agreement allowance, typically ~20,800–26,000 FCFA/month in the formal sector; I could not confirm the 2025–26 amount from an official text. [C]
- **IPM (health):** the statutory IPM covers only basic care; tech firms/banks usually add a private health top-up (assurance maladie groupe) — budget **~300,000–600,000 FCFA per employee per year** (family cover) [E – broker quotes not found online; flag as gap].
- **Personal income tax (IR) and TRIMF** are employee-side withholdings (no employer cost) but affect net-to-gross negotiations: candidates in Dakar usually negotiate in **net**. Rough net/gross ratio for an 800k cadre ≈ 0.80–0.83. [E]

### 2.3 Loaded-cost worked example — 800,000 FCFA gross/month, cadre, office risk class (AT 1%)

| Line | Base | Rate | Employer cost/month |
|---|---|---|---|
| IPRES RG | 432,000 | 8.4% | 36,288 |
| IPRES RCC | 800,000 − 432,000 = 368,000 | 3.6% | 13,248 |
| CSS family | 63,000 | 7% | 4,410 |
| CSS work accident | 63,000 | 1% | 630 |
| IPM (assume 3% employer) | 250,000 | 3% | 7,500 |
| CFCE | 800,000 | 3% | 24,000 |
| **Statutory total** | | | **86,076 (= 10.8%)** |
| 13th month (customary, 1/12) | 800,000 | 8.33% | 66,667 |
| Private health top-up (≈450k/yr) | | | 37,500 |
| Transport allowance (customary) | | | ~26,000 |
| **All-in total** | | | **≈216,000 (= 27%)** |

**Multipliers (planning):**
- **Statutory only: ×1.11 at 800k, ×1.09 at 1.3M** gross for a cadre; falls to **×1.06 at 2.5M** (ceilings; only the 3% CFCE is uncapped); **×1.16 at 250k** for non-cadres (IPRES RG 8.4% on the whole salary + CSS 5,040 + IPM + CFCE).
- **Market-competitive package (13th month + private health + transport): ×1.25–1.30.** Recommended planning multiplier for a fintech: **×1.25** on gross, plus ~2–3% for training/equipment/recruitment.
- Compare: Kolonell's example (×1.17 on a 400k non-cadre) over-states CSS by applying it uncapped [C].

### 2.4 Côte d'Ivoire (Abidjan) — employer charges, brief
- CNPS employer (verified [A] [PwC Tax Summaries – Ivory Coast other taxes, reviewed 9 Sep 2026](https://taxsummaries.pwc.com/ivory-coast/corporate/other-taxes)): retirement **7.7%** on ceiling **3,375,000** FCFA/month; family allowance (incl. maternity) **5.75%** on ceiling **70,000**; work injury **2–5%** on 70,000. Employer payroll tax (ITS employer share): **2.8%** of gross for local staff, **12%** for expatriates (20% abatement removed). Not on the PwC page but standard (from memory, verify): employee CNPS retirement 6.3%; FDFP training levies 0.4% (taxe d'apprentissage) + 1.2% (formation continue); CMU 1,000 FCFA/employee/month employer share. → **Statutory employer load ≈ 13–14% for a local cadre at 1–3M FCFA (≈ ×1.13–1.14)**; ≈ ×1.22 for an expatriate. SMIG CI = 75,000 FCFA/month [C, Africarrières/Simoon].

---

## 3. Office, coworking, utilities

### 3.1 Office rent — Dakar (FCFA per m² per month, excl. charges/taxes unless stated)

Best data found: **live listing inventory of a Dakar commercial agency** ([Mon Agent Immobilier – bureaux à louer Dakar](https://www.monagentimmo.net/bureau-a-louer-a-dakar), fetched Oct 2026, ~65 listings, mix of current and already-let; **[B]** — asking rents, not signed leases, listing dates not shown). Per-m² rents computed from listing totals:

| Area | Range observed (FCFA/m²/month) | Typical | Examples |
|---|---|---|---|
| **Plateau** (CBD) | 5,000 – 13,000 | **9,000–12,000** | Immeuble Rivonia 338 m² @ 12,000; 532 m² @ 9,000; 350 m² @ 13,000; 95 m² for 800k (8,400) |
| **Point E** | 4,850 – 10,000 | **7,000–8,500** | FOCUS ONE 465 m² @ 10,000; new building 273 m² @ 8,540; 100 m² @ 7,000 (= 700k/month); 196 m² for 1.0M (5,100) |
| **Mermoz / VDN** | 4,800 – 13,000 | **8,500–9,000** | 738 m² @ 9,000; 210 m² @ 8,570; Mermoz VDN 800 m² @ 13,000 |
| **Sacré-Cœur / VDN** | 3,700 (villa) – 11,700 (new building) | **6,000–9,000** | VDN SC3 300 m² for 3.5M; villa 300 m² for 1.1M |
| **Almadies / Ngor** | 5,000 – 13,500 | **6,000–11,000** | 503 m² @ 5,960; 400 m² @ 7,000; 246 m² @ 13,500; Ngor 260 m² @ 5,770 |
| Fann / Corniche | 5,000 – 12,000 | 7,000–9,000 | Fann Hock 500 m² @ 12,000 |
| Cheaper: Liberté 6, Grand Yoff, Ouest Foire, Cité Keur Gorgui, villas converted to offices | 2,200 – 7,000 | 4,000–5,000 | Ouest Foire 120 m² for 275k |

Corroboration: other agency listings via search — Point E new offices 7,000–10,000/m²; Mermoz–Sacré-Cœur plateau 410 m² for 4.1M (≈10,000/m²); Mermoz 700 m² @ 9,000 HT ([SenHub Immo](https://senhubimmo.com/bien-immobilier/SHI-12653), [A2D Immobilier](https://a2dimmobilier.com/location-bureaux-locaux-commerciaux/page/2/), [Keur-Immo](https://keur-immo.com/en/senegal/real-estate-ad-senegal/dakar-sacre-coeur-office-spaces-for-rent/)) [B, some listings 3–5 years old]. Kolonell (May 2026) estimates an 80 m² office at 700k–1.1M on the Plateau (≈8,750–13,750/m²) and 600–900k in Almadies [C] ([Kolonell Abidjan vs Dakar](https://kolonell.com/fr/blog/abidjan-vs-dakar-startup-cout-comparatif-2026)).

**On top of rent (planning assumptions [E], from standard Senegalese commercial-lease practice):** deposit 2–3 months; agency fee ≈1 month; registration duty **2% of annual rent** [A, PwC]; local economic contribution (CEL, ex-patente) property component ≈ 15% of rental value for leased premises [A, PwC]; fit-out/furniture/AC for 150 m² ≈ 15–30M FCFA one-off; service charges/security/cleaning 500–1,500 FCFA/m²/month. VAT (18%) may apply if landlord is VAT-registered.

**Planning figure:** 150–200 m² for a 20–30 person team in Point E / Mermoz / Sacré-Cœur at **~8,500 FCFA/m²** → **1.3–1.7M FCFA/month** rent + ~20% for charges/security/cleaning ≈ **1.6–2.1M/month**. Plateau premium (~+25%) is justified only for regulator/bank proximity; most Dakar fintechs (Wave, Djamo, PayDunya, InTouch) sit in Mermoz/Sacré-Cœur/Almadies/Ngor.

### 3.2 Coworking — Dakar
| Space | Price | Date / reliability |
|---|---|---|
| Impact Hub Dakar (Mermoz) | day 3,000; monthly 60,000; private office 400,000/month all-in | Nov 2021 [C] ([Au-Sénégal](https://au-senegal.com/ou-trouver-des-espaces-de-coworking-a-dakar,16116.html)) |
| Jokkolabs (Sacré-Cœur 3) | monthly desk 65,000; 10-day pass 30,000 | Nov 2021 [C] (same) |
| Ofisini | day 5,000; monthly 70,000 | Nov 2021 [C] |
| Freepenseur / Cité Keur Gorgui | coworking 65,000; private office from 170,000 | 2021 [C]; Coworkingcafe listing "from 60,000/month, day 4,000" [C] |
| Regus (Plateau, Ngor/Almadies, Point E) | coworking membership 58,500/month; dedicated workstation 111,000/month (2021); 2026 guide: day pass ≈23,900, dedicated desk from ≈4,600/day | [C] |
| 2026 estimate (Impact Hub, Jokkolabs) | **fixed desk 70,000–150,000/month** | May 2026 [C] Kolonell |

**Planning figure (pre-launch team of 5–10):** 100,000 FCFA/desk/month; small private office for 6–8 in a business centre ≈ 600k–1.2M/month all-inclusive [E].

### 3.3 Utilities
- **Electricity (Senelec, CRSE grid effective 1 Jan 2026)** [A] ([CRSE grille tarifaire 2026 PDF](https://www.crse.sn/wp-content/uploads/2025/12/Grilles-tarifaires-Senelec-et-CER-applicables-a-compter-du-1er-janvier-2026.pdf); [Le Soleil](https://lesoleil.sn/actualites/economie/energie-baisse-des-tarifs-delectricite-des-le-1er-janvier-2026/)): professional small-power (PPP) 147.43 / 189.84 / 208.63 FCFA/kWh by tranche; professional medium-power (PMP) 165.01 / 191.01 / 210.81 FCFA/kWh. Kolonell estimate for an 80 m² office: 80–160k/month [C]. For a 150–200 m² air-conditioned office with servers/laptops plan **250–400k/month** [E] (AC dominates). Outages are much rarer than pre-2017 but a generator/UPS is standard: 20–30 kVA diesel genset ≈ 8–15M FCFA one-off + fuel [E — no vendor quote found].
- **Internet**: Orange (Sonatel) residential/SOHO fibre 14,900 (10 Mb/s) → 39,900 FCFA/month (100 Mb/s); Yas (ex-Free) fibre 100 Mb/s unlimited 33,000/month [C] ([Osiris comparison](https://osiris.sn/cout-de-l-internet-quelle-est-la-place-de-la-guinee-par-rapport-a-ses-voisins.html)); Orange satellite pro 44,900/month (Dec 2025) [B]. Kolonell: "professional fibre 100 Mb/s" 65–110k/month [C]. A **dedicated business link with SLA (Orange Business / Sonatel "LS/Internet dédié")** is quote-only; plan **300–800k/month** for 20–50 Mb/s symmetrical dedicated [E] + a second-operator backup fibre (~40k).

### 3.4 Abidjan (year 2)
- Office rent: Property Kro study (2017) 6,000–18,000 FCFA/m²/month across prime communes, new projects >20,000, vacancy <2% [B, dated] ([Fraternité Matin](https://www.fratmat.info/index.php/economie/l-immobilier-de-bureaux-a-abidjan-un-secteur-tres-attractif-selon-une-etude)). Kolonell 2026: 80 m² on the Plateau 1.2–2.0M/month (≈15,000–25,000/m²); Cocody II-Plateaux 600–900k for 80 m² (≈7,500–11,000/m²); Marcory Zone 4 above Dakar's Mermoz [C]. **Planning: Abidjan ≈ 1.3–1.6× Dakar** → Cocody/Marcory Zone 4 ≈ 11,000–14,000/m²; Plateau 15,000–22,000/m².
- Coworking: fixed desk 80,000–180,000/month; shared desk 55–90k; dedicated with services 90–150k; premium Plateau 100–200k (Kolonell 2026 [C]); Regus at Indénie and Koumassi (quote only). **Planning: 150k/desk/month** for a 3–5-person country team in year 2.
- Utilities: pro fibre 100 Mb/s 90–140k/month; electricity 80 m² 90–180k/month [C, Kolonell].

---

## 4. Professional services — Senegal

No official fee scales are published (fees are free, set by engagement letter). Figures below are mostly [C]/[E]; **get 3 written quotes for each**.

| Service | Data found | Planning figure | Reliability |
|---|---|---|---|
| **Company formation (SA)** at APIX one-stop shop | SA minimum capital 10M FCFA (OHADA); APIX/RCCM fees 25–50k; statutes registration ~25k; BOJ publication ~13k; notary (mandatory for SA) 100k–350k (more for larger capital, notary fees are partly proportional to capital); bank blocked-account fee 5–25k. ([Kolonell APIX 2026](https://kolonell.com/fr/blog/creer-entreprise-apix-senegal-etapes-cout-2026), [Kolonell SARL/SUARL costs](https://kolonell.com/fr/blog/cout-creation-entreprise-senegal-sarl-suarl-detail-2026), [Afrotools](https://afrotools.com/blog/creation-entreprise-senegal-couts/)) | **1.5–3M FCFA all-in** for an SA with lawyer-drafted statutes (excl. capital). NB: a BCEAO EME needs **300M FCFA** paid-in capital (Instr. 008-05-2015); capital increase registration duty 1% only above 100M capital (PwC). | [C]/[A] |
| **Business law firm** | Kolonell (unsourced): junior 50–100k/h, senior 100–300k/h, partner 300–500k FCFA/h; monthly retainers for SMEs 200k–2M ([Kolonell avocat d'affaires](https://kolonell.com/fr/blog/avocat-affaires-dakar-contrats-commerciaux-2026)) | Partner-level at top Dakar firms (Geni & Kebe/DLA Piper Africa, Mame Adama Gueye, SCP Kanjo Koita, etc.) ≈ **150–350 €/h (100–230k FCFA)** [E] | [C]/[E] |
| **BCEAO licence file (EP or EME)** | No public fees found. Process takes many months (BCEAO stopped unlicensed fintechs from 1 May 2025; only ~11 fintechs licensed under Instr. 001-01-2024 by mid-2025). | **Legal + regulatory consultants: 30–80M FCFA (≈€45–120k)** for full dossier (business plan, AML/CFT manual, IT security policy, governance docs, Q&A rounds with BCEAO over 9–18 months); plus internal staff time. [E] | [E] — key gap |
| **Statutory auditor (CAC)** | No scale. SA must always appoint a CAC (OHADA); BCEAO-licensed institutions need a CAC approved by the BCEAO/Banking Commission. | Small SA, non-regulated: **3–8M FCFA/yr**; licensed EP/EME with Big-4/mid-tier: **10–25M FCFA/yr** (+ regulatory reports) [E] | [E] |
| **Chartered accountant (expert-comptable) bookkeeping + tax filings** | "Forfait PME 50k–300k FCFA/month" ([Kolonell expert-comptable](https://kolonell.com/fr/blog/expert-comptable-certifie-senegal-syscohada-2026)) | Outsourced pre-launch: **250–500k/month**; post-licence, in-house team + firm for payroll/tax: 200–300k/month | [C] |
| **Payroll outsourcing** | – | 10–20k FCFA/employee/month [E] | [E] |
| **Data protection (CDP)** | Declaration/authorisation forms on cdp.sn; no fee schedule found (believed free of charge). CDP processed 96 files in Q2 2025. Authorisation needed for biometrics and transfers abroad. | Filing itself ≈ 0; **DPO/privacy counsel 2–5M FCFA** one-off for files + transfer authorisations [E] | [B] for procedure, fees gap |
| **Recruitment agency fees** | No Senegal grid found; market practice 15–20% of annual gross for search by ads, 20–25% for cadres, **25–35% for retained executive search**, paid in thirds, 3–6-month guarantee ([Licorne Society](https://www.licornesociety.com/blog/combien-coute-cabinet-recrutement-tarif), memoire on Syntec practice) | **18% of annual gross** for mid roles; **25–30%** for C-level via Africsearch/Grey Search/Odgers | [C] (French benchmarks; Dakar firms similar) |

---

## 5. Technology vendor pricing

| Item | Public price found | Planning figure | Reliability |
|---|---|---|---|
| **eKYC — Smile ID** | No public rate card (pricing page redirects to "talk to an expert"). Third-party: document verification ≈ USD 0.10–0.30, biometric KYC ≈ USD 0.30–1.00, AML screening from USD 0.05 ([HelloDuty](https://helloduty.com/blogs/what-is-smile-identity-and-how-its-revolutionizing-business-practices)); startup programme up to USD 6,000 credits ≈ 30,000 checks ([Fitgap](https://us.fitgap.com/products/smileid)) | **USD 0.50–1.00 per full onboarding** (doc + selfie/liveness) in Senegal; Senegal has no government ID-database lookup comparable to Nigeria's NIN, so doc+biometric is the norm [E] | [C] |
| **eKYC/AML — Sumsub** | Basic **USD 1.35/verification, min USD 149/month**; Compliance (incl. AML screening, ongoing monitoring, address) **USD 1.85/verification, min USD 299/month**; Enterprise custom ([Sumsub pricing](https://sumsub.com/pricing/)) | Negotiable to ~USD 0.8–1.2 at volume [E] | [A] |
| **AML / sanctions screening — ComplyAdvantage** | Starter ≈ **USD 99–119/month** (100–2,000 monitored entities; "Starter Agentic" 149); enterprise/transaction monitoring custom; ComplyLaunch free programme for early startups ([PricingSaaS](https://pricingsaas.com/companies/complyadvantage), [ERP Research](https://erpresearch.com/erp-add-ons/fraud-risk/complyadvantage/pricing)) | Year 1: USD 150–500/month; with transaction monitoring at scale USD 30–80k/yr [E] | [C] |
| **Card issuing processor** (Paymentology, Marqeta, NymCard, local GIM-UEMOA/ HPS / Interswitch / Sesame/ Monetique) | No public pricing. Marqeta anecdote: ~USD 25k set-up ([Blind](https://www.teamblind.com/post/whats-the-pricing-for-the-marqeta-card-issuing-nzlfdmks)) [C]. In WAEMU, Visa/Mastercard issuing requires a sponsor bank (BIN sponsor) and GIM-UEMOA membership for domestic cards. | **Set-up USD 25–75k; monthly minimum USD 3–10k; per active card USD 0.10–0.50/month + per-transaction fees** [E]; sponsor-bank fees on top (often revenue share on interchange) | [E] — gap |
| **Card manufacturing/personalisation** | Sewacard Industrie (Diamniadio) is GIM-UEMOA-certified for EMV CPA cards, claims 1M cards/month and <72h delivery ([Senego](https://senego.com/gim-uemoa-sewacard-industrie-certifiee-pour-produire-des-cartes-bancaires_1150620.html)); no unit price published | **EMV contact card, personalised + PIN mailer: USD 1.5–3 (≈900–1,800 FCFA)** at 10–50k runs; contactless/dual-interface or metal far more; plus card carrier/envelope [E] | [E] |
| **Core banking / ledger** | Mambu: no list price; buyer-reported ≈ **USD 150k+/yr** for small deployments, first-year TCO 2–3× licence ([FintechSpecs](https://fintechspecs.com/?p=1776)); AWS Marketplace listing shows usage-based entry (USD 0.01/account) [C]. Thought Machine: enterprise, multi-million — out of reach. Oradian: subscription by user volume, no public price. Apache Fineract/Mifos: free (Apache 2.0) — cost is hosting + integrator. Formance (open-source ledger): free self-hosted; Formance Cloud contract pricing via AWS Marketplace. | For an EP/EME at launch: **self-hosted open-source ledger (Formance/Fineract) + 2–3 engineers**, or a regional core (e.g. Oradian, Musoni, Temenos Transact SaaS for SFDs) at **USD 30–100k/yr**. Avoid Mambu/TM pre-Series B. [E] | [C]/[E] |
| **Cloud hosting** | No AWS/GCP/Azure region in WAEMU; nearest: AWS af-south-1 (Cape Town), AWS Lagos Local Zone, Paris/Frankfurt. Senegal's state Tier-3 data centre at Diamniadio (2021) and the "New Deal Technologique" sovereign-cloud push (operational phase Mar 2026). Personal-data transfers abroad need CDP authorisation (Law 2008-12); BCEAO licensing reviews outsourcing/hosting arrangements. | Early stage: **USD 2–6k/month** on AWS/GCP (Paris/Frankfurt) for prod + staging; budget for a local/WAEMU replica (Sonatel Orange Business, Senegal Numérique SA, ADC/Rack Centre) **USD 1–3k/month** if the BCEAO/CDP asks for local copy [E] | [E] |
| **SMS** | **Orange SMS API Senegal (official)**: 100 SMS = 2,000 FCFA (20/SMS); 500 = 7,500 (15); 1,000 = 12,000 (12); 5,000 = 50,000 (10); **20,000 = 80,000 (4); 40,000 = 160,000 (4); 60,000 = 200,000 (≈3.3 FCFA/SMS)**; 5 TPS limit; volume discounts on request ([Orange Developer – SMS Senegal pricing](https://developer.orange.com/apis/sms-sn/pricing)) [A]. Twilio to Senegal: **USD 0.5506/segment** ([Twilio](https://www.twilio.com/en-us/sms/pricing/sn)) [A] — ~30× local. | **4–10 FCFA per OTP SMS** via direct operator/local aggregator; avoid global CPaaS for OTP | [A] |
| **WhatsApp Business API** | Meta per-message pricing since Jul 2025; "Rest of Africa" rates (Senegal) ≈ **USD 0.0252 marketing; USD 0.0045 utility/authentication** (reseller copy of Meta rate card, [SleekFlow](https://help.sleekflow.io/en_US/whatsapp/pricing); official: [Meta pricing docs](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)); service (user-initiated) conversations free; BSP markup extra | Utility/OTP ≈ **2.6 FCFA**, marketing ≈ **15 FCFA** per message + BSP fee (USD 0–0.005) | [B] |
| **Back-office (Retool)** | Team: builder USD 10 (annual)/12, internal user 5/7; Business: builder 50/65, internal user 15/18; external users free to 50 then USD 8→4 ([Retool pricing](https://retool.com/pricing)) [A] | 3 builders + 25 ops users on Business ≈ **USD 525/month** | [A] |
| **Google Workspace** | Business Starter ≈ USD 7, Standard ≈ USD 14, Plus ≈ USD 22 per user/month (annual, 2025 list prices incl. Gemini) — from memory, not re-fetched | Standard for 30 users ≈ USD 420/month | [B, verify] |
| **Penetration test** | Fintech web app manual test USD 5–30k; API USD 6–35k; cloud USD 10–40k ([Beagle Security](https://beaglesecurity.com/blog/article/fintech-penetration-testing.html), [ZeroThreat](https://zerothreat.ai/blog/fintech-pentesting-cost-breakdown)) [C]; no Senegal-specific prices — local firms (e.g. in Dakar/Abidjan) likely 30–50% cheaper | **USD 15–30k per annual pentest** (app + API + mobile) [E] | [C] |
| **PCI DSS** | QSA Level-1 assessment USD 15–100k (IXOPAY), 30–100k+ (Scrut 2026), 100–250k for large multi-site (SecurityMetrics) ([Scrut](https://www.scrut.io/post/calculating-your-actual-pci-compliance-cost-expert-guide-for-2026), [SecurityMetrics](https://chat.securitymetrics.com/blog/pci-level-1-audit-costs)); ASV scans quarterly | If you **outsource card data to a PCI-certified processor** you only need SAQ + ASV scans (USD 2–5k/yr). If you store PAN: **USD 40–80k first-year QSA ROC + 50–150k remediation** [E] | [C] |

---

## 6. Other costs

| Item | Data | Planning figure | Reliability |
|---|---|---|---|
| **Insurance (professional liability, cyber, D&O)** | No Senegal premium data found online. | Cyber + PI for a licensed EP: **USD 10–30k/yr** for USD 1–2M cover via Allianz/AXA/Sunu/NSIA brokers; group health top-up see §2.2 [E] | gap |
| **Courier (Dakar)** | Paps: from 1,000 FCFA HT per Dakar delivery (2020) ([Osiris](https://osiris.sn/Achat-et-Livraison-Paps-et-Expat.html)); Yango Delivery (launched Nov 2025): ~1,200 (0–3 km) / 1,800 (3–7 km); city averages 1,500 central / 2,500 suburbs (Pikine/Guédiawaye) ([Kolonell last mile](https://kolonell.com/fr/blog/livraison-last-mile-dakar-zones-tarifs-delais-2026)) [C] | **Card delivery with KYC hand-over: 2,000–3,000 FCFA per card in Dakar**, 3,500–6,000 to regions via partner networks [E] | [C] |
| **Card cost per issued card (all-in)** | plastic+perso 900–1,800 + PIN mailer/carrier 200–400 + delivery 2,000–3,000 | **≈4,000–5,000 FCFA (USD 7–9) per physical card delivered**; virtual cards ≈ processor fee only [E] | [E] |
| **Digital marketing (Meta)** | Facebook feed CPM 800–2,200 FCFA; Instagram Reels CPM 1,400–3,500; CPC 100–350; cost per form lead 600–2,800; cost per WhatsApp conversation start 350–1,100; minimum test budget 150k/14 days ([Kolonell CPM/CPC Senegal 2026](https://kolonell.com/fr/blog/cout-publicite-facebook-google-tiktok-senegal-cpm-cpc-2026)) [C, agency estimates]. LinkedIn: no Senegal data (global B2B CPC typically USD 3–8, CPM USD 10–30) [E]. | Consumer CAC via paid social: **1,500–5,000 FCFA per install / 5,000–15,000 FCFA per funded account** [E] | [C] |
| **Events / sponsorship** | No public rates found for Dakar events (e.g. Africa Fintech Forum, Fintech Week Dakar, Sargal). | Booth/sponsor at a regional fintech event **5–25M FCFA**; local meetups 0.5–2M [E] | gap |
| **Transport allowance for field sales** | Yango taxi Almadies→Plateau ≈ 1,500 FCFA (older); motorbike courier rates above. | Field rep: **50–100k FCFA/month** transport allowance, or scooter lease ~60–90k/month + fuel (regulated pump price, ~1,000 FCFA/l order of magnitude — not verified this session) [E] | [E] |
| **Mobile phone/data** | Orange historical bundles e.g. 4,000 FCFA/month = 600 min + 2 GB (2020) [C]; Free/Yas 15–30% cheaper than Orange (Senego comparator) [C]; no current corporate-fleet price list found. | **10–20k FCFA/employee/month** (voice + 20–40 GB data) + handset 100–250k every 2–3 years [E] | [C]/[E] |
| **Business bank account** | Maintenance fees 8,000–25,000 FCFA/month (Kolonell) [C] | 25k/month | [C] |

---

## 7. Key gaps & uncertainties
1. **Role-level salaries rest on [C] sources.** No recruiter survey exists for Senegal; the biggest uncertainty is for compliance/AML heads, CFO, head of sales and CEO. Paylab figures are 3–5× lower than blog grids and should be disregarded for cadres. Action: 3 recruiter calls (Africsearch, Grey Search Africa, Emerging Search/ Talent2Africa) and 3–5 peer fintech founders (Wave alumni, Djamo SN, PayDunya, Bictorys, Kalpé).
2. **Engineer pay is bimodal**: local-market (Kolonell grid) vs remote/global (Wave-type USD 100k+ bands, freelance 1.6–3.2M+ FCFA). A neobank competing with Wave for top engineers may need to pay at or above the top of the local grid plus equity.
3. **Charges**: statutory rates are firm ([A] CLEISS/PwC 2026). IPM rate (2–7.5%) depends on the chosen IPM; 13th-month and transport-allowance norms come from practice, not law.
4. **Office rents** come from asking prices of one agency's inventory (≈65 listings) plus older corroboration; no transaction-based survey. Fit-out and generator costs are estimates.
5. **Licence-related costs** (BCEAO dossier, CAC for a regulated EP/EME, sponsor-bank/card processor minimums, data-residency requirements) have no public prices — the largest budget risk outside payroll.
6. **Vendor prices** that are firm: Sumsub, Retool, Orange SMS API, Twilio, (Meta WhatsApp via reseller). Others (Smile ID, ComplyAdvantage, card processors, core banking, insurance) are estimates.
7. Abidjan figures are thin: employer charges [A], rents/coworking [C]; country-manager salary [C].
