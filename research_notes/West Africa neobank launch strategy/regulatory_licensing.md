# Regulatory & Licensing Map for a Digital Neobank in Francophone West & Central Africa (as of October 2026)

Scope: WAEMU/UMOA (BCEAO), CEMAC (BEAC/COBAC), DRC (BCC), Guinea (BCRG). Product: accounts, wallets, cards, transfers, multi-currency, lending. Non-crypto. FX: 1 EUR = 655.957 FCFA (EUR figures are rounded).

Research method note: the WAEMU core texts (EME Instruction 008-05-2015 and Payment Services Instruction 001-01-2024) and the BCEAO list of licensed payment institutions were read directly from BCEAO PDFs. Most other figures come from press or law-firm secondary sources and are flagged where relevant. The web-search budget ran out before I could search on bank BaaS APIs, card processors (GIM-UEMOA, HPS, Interswitch), Kori, the AML uniform law or KYC tiers. These are listed under Gaps.

---

## 1. WAEMU: e-money institution (EME) licence under BCEAO Instruction n°008-05-2015

### Takeaway
An EME licence needs 300 M FCFA (about €457k) of fully paid-up capital. It allows wallets, e-money distribution and agent networks. It expressly bans any credit and any interest on float. Balances are capped at 2 M FCFA (about €3,049) per identified customer and 10 M FCFA of reloads per month unless the BCEAO grants an exception. There is no automatic passport: operating in each other WAEMU state needs a separate BCEAO authorisation.

### Cited Findings
- **Who must be licensed:** apart from banks and financial institutions authorised by the banking law, no entity may issue e-money without prior BCEAO approval. Banks must notify the BCEAO 2 months before launching e-money. SFDs (microfinance institutions) need prior BCEAO authorisation (art. 8). — [BCEAO Instruction 008-05-2015](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **Capital (art. 11):** the minimum share capital of an EME is **300,000,000 FCFA (about €457,347)**, fully subscribed and paid in cash before approval. An SFD may be authorised to issue e-money if its own funds and customer deposits each reach at least 300 M FCFA at the prior year end. The BCEAO may require more capital depending on the risk profile. — [BCEAO Instruction 008-05-2015](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **Own funds (art. 22):** an EME must hold own funds of at least the minimum capital, and at all times at least **3% of e-money outstanding**. — [BCEAO Instruction 008-05-2015](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **No credit, no interest (art. 5):** issuers may not grant credit "in any form" and may not pay interest on the funds received for e-money. Funds from a loan granted by a **bank or SFD** may be used to issue e-money, which is the legal hook for bank or SFD-funded credit disbursed into wallets. — [BCEAO Instruction 008-05-2015](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **Partners (art. 4):** EMEs may partner with "technical operators" limited to technical processing or distribution under the issuer's responsibility. Partner marketing must name the issuing institution, and responsibility for issuance cannot be outsourced. — [BCEAO Instruction 008-05-2015](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **Permitted activities (art. 16):** EMEs may provide services linked to issuing and distributing e-money, plus electronic data storage for other legal entities. — [BCEAO Instruction 008-05-2015](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **Distribution (art. 17–18):** EMEs may use distributors (principal distributors and sub-distributors) and remain responsible for them, including AML/CFT compliance. — [BCEAO Instruction 008-05-2015](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **Ceilings (art. 31):**
  - Holdings per identified customer at one issuer: **≤ 2,000,000 FCFA (about €3,049)**, cumulated across instruments.
  - Monthly reloads per customer: **≤ 10,000,000 FCFA (about €15,245)**.
  - Unidentified holders: **≤ 200,000 FCFA (about €305) per month**.
  - All three ceilings can be raised with express BCEAO authorisation if the issuer justifies the need and its extra controls. Distributors and merchants are exempt.
  - Source: [BCEAO Instruction 008-05-2015](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **Safeguarding (art. 32–34):**
  - Float must sit in a dedicated account at one or more banks or SFDs in the Union, reconciled daily, and may not fund operations.
  - It may be invested only in sight deposits, term deposits, or securities of governments, regional financial institutions or BRVM-listed companies.
  - **Sight deposits must be at least 75%** of e-money outstanding.
  - Source: [BCEAO Instruction 008-05-2015](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **Review time (art. 13):** the maximum review period is **3 months** from a complete file. Each information request suspends the clock, and the applicant has 2 months to answer or the file is rejected. — [BCEAO Instruction 008-05-2015](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **Cross-border (art. 20):** once licensed in one member state, an EME may operate in other WAEMU states, including through subsidiaries or branches, "subject to requesting the authorisation of the Central Bank". The authorisation is a Governor's decision and must be published in a local legal gazette before launch. — [BCEAO Instruction 008-05-2015](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf); described as "no passport" by [Prifinance](https://prifinance.com/en/payments/cote-divoire-payment-license/)
- **Reload ceiling history:** during COVID-19 the BCEAO temporarily raised the e-wallet reload ceiling from 2 M to 3 M FCFA for identified customers. — [Financial Afrik 2020](https://www.financialafrik.com/2020/04/02/covid-19-la-bceao-annonce-8-nouvelles-mesures-pour-booster-la-transaction-electronique/) (older)
- **Fees and realistic duration:** no application, licence or annual supervision fee is published in the instruction or the BCEAO promoter guide. Prifinance estimates 9–15 months end to end. — [Prifinance](https://prifinance.com/en/payments/cote-divoire-payment-license/) (commercial adviser; treat as indicative)
- **Still in force:** the Commission Bancaire still lists 008-05-2015 as the applicable EME text. In practice it is read together with 001-01-2024. — [Prifinance](https://prifinance.com/en/payments/cote-divoire-payment-license/)
  - The 2024 instruction's final clause repeals only "earlier provisions to the contrary dealing with the same subject" (art. 97). — [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)

### Inferences
- An EME licence cannot carry lending. Lending must come from a bank or SFD partner, with proceeds credited to the wallet (the art. 5 carve-out), or from the startup's own SFD.
- The 2 M FCFA balance cap makes an EME wallet unsuitable as a primary account for salaried middle-class users or SMEs unless the BCEAO grants a waiver. This is why Djamo sought a microfinance licence to offer "uncapped" current accounts (see §3).
- Multi-country rollout under an EME is sequential, one BCEAO authorisation per country, not a passport.

### Gaps
- I found no evidence of a 2024–2026 revision of 008-05-2015, such as new KYC tiers or raised ceilings. The BCEAO may have issued unpublished waivers to individual EMEs.
- No official licence or application fees were found.

---

## 2. WAEMU: payment institution (Établissement de Paiement, EP) under Instruction n°001-01-2024 (23 Jan 2024)

### Takeaway
The EP regime is the cheapest licensed entry: **100 M FCFA (about €152k)** covers any of cash-in/out and account management, transfers, card payments, card/instrument issuing and acquiring. An EP **cannot lend, cannot pay interest, and cannot use e-money-style distributor networks**, but may use BCEAO-registered "agents de services de paiement". It is licensed per country.
Since mid-2025 the BCEAO has enforced it hard: unlicensed fintechs had to stop payment services. 31 EPs were licensed by 28 Feb 2026, including Djamo (CI and SN) and Julaya (CI, SN, BJ).

### Cited Findings
- **Covered services (art. 4):**
  - (i) cash deposit/withdrawal and account management
  - (ii) transfers, direct debits and card payments
  - (iii) money transfer
  - (iv) payments by any means of communication
  - (v) issuing payment instruments
  - (vi) acquiring
  - (vii) payment initiation
  - (viii) account aggregation / account information
  - Source: [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **Who counts as a payment service provider (definitions):** banks, financial credit institutions (EFCs), microfinance institutions, EMEs and EPs. Under art. 6, banks may also provide initiation (vii) and aggregation (viii). — [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **Payment accounts and ancillary services (art. 5):** services (i)–(vi) are attached to a **payment account** opened at the EP. EPs may also offer custody and data processing as ancillary services. — [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **Partnerships (art. 7):** PSPs may form service partnerships subject to outsourcing rules. **Exclusivity clauses are prohibited.** — [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **Prohibited operations (art. 8):** EPs may not:
  1. grant credit "in any manner whatsoever";
  2. pay interest or any remuneration or benefit on payment-account funds;
  3. handle cheques, bills of exchange, promissory notes or documentary credits;
  4. **use distributors** to provide payment services;
  5. invest client funds other than in sight or term deposits at banks or microfinance institutions, or member-state securities of at most 1 year residual maturity. Sight deposits must be **≥ 30%** and government securities **≤ 25%**.
  - Source: [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **Capital (art. 11):** paid in cash, in FCFA:
  - **10 M FCFA (about €15,245)** for aggregation only (a registration, not a licence: art. 9, 22–24)
  - **20 M FCFA (about €30,490)** for initiation only
  - **30 M FCFA (about €45,735)** for initiation plus aggregation
  - **100 M FCFA (about €152,449)** for any of services (i)–(vi)
  - The licensing decision may set a higher amount. A professional liability insurance or financial guarantee is also required (art. 12).
  - Source: [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **Own funds and liquidity (art. 44):** own funds may never fall below the minimum capital, and the EP must hold sufficient liquidity. Calculation methods are left to the BCEAO. — [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **Review time (art. 18–19):** **6 months** from a complete file, and the clock restarts after each information request. The applicant has **30 calendar days** to answer or the application is deemed rejected. Silence after 6 months (9 months if a home-supervisor no-objection is needed) counts as refusal. — [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **Safeguarding (art. 48):** client funds not paid out by the end of the next business day go into ring-fenced accounts (comptes de cantonnement) at banks or microfinance institutions. These accounts are reconciled daily and protected from the EP's creditors in resolution or liquidation. — [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **Agents (art. 38–40):** nobody may act as an "agent de services de paiement" without BCEAO registration. The EP files the agent's identity, contract, AML controls and the fitness of its managers. The EP stays fully liable for its agents. A PSP may also act as agent of other PSPs for distinct services. — [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
  - Definitions: an "agent bancaire" is a person registered with the BCEAO acting for credit institutions. An "intermédiaire mandaté" is an agent bancaire or a payment-services agent. — same source.
- **Industry association and transition (art. 95–96):** EPs must join the Association Professionnelle des Établissements de Paiement et de Monnaie Électronique within 1 month of licensing. The transition period was 6 months. — [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **Deadline timeline (sources conflict on the final date):**
  - Original deadline 23 July 2024, then derogations to 31 Jan 2025 and 30 Apr 2025. The BCEAO suspended non-compliant operators from **2 May 2025**. — [BIE/CCIAD, BCEAO Senegal briefing 9 May 2025](https://bie.cciad.sn/2025/05/09/regulation-des-fintechs-les-precisions-de-la-bceao/)
  - Agence Ecofin reported a deadline of 1 May 2025. — [Agence Ecofin](https://www.agenceecofin.com/actualites-finance/0304-127221-umoa-les-prestataires-de-paiement-ont-jusqu-au-1er-mai-2025-pour-obtenir-un-agrement)
  - Later reporting gave fintechs **until 31 Aug 2025**. — [Digital Mag CI](https://digitalmag.ci/instruction-n001-01-2024-bceao-les-fintech-ont-jusquau-31-aout-2025-pour-obtenir-un-agrement-de-la-bceao/); [Agence Ecofin, June 2025](https://www.agenceecofin.com/actualites-finance/0206-128873-services-de-paiement-umoa-les-fintech-ont-jusqu-au-31-aout-pour-se-regulariser)
  - Prifinance cites BCEAO **Avis n°004-03-2025** making unlicensed payment services unlawful from 1 May 2025. — [Prifinance](https://prifinance.com/en/payments/cote-divoire-payment-license/)
- **Uptake at May 2025:** Senegal had over 100 fintechs, only 2 licensed (PayDunya, Mikaty) and 13 files in advanced review. 9 licences had been granted across WAEMU. — [BIE/CCIAD](https://bie.cciad.sn/2025/05/09/regulation-des-fintechs-les-precisions-de-la-bceao/)
- **Official list at 28 Feb 2026 (31 EPs), with licence number and date:**
  - **Côte d'Ivoire:** SYCA (EP.CI.001/2025, 06/05/25), Touchpoint, Firstcom, Julaya CI (EP.CI.004/2025, 09/05/25), **Djamo CI (EP.CI.005/2025, 04/09/25)**, FeexPay, CinetPay, PayMeTrust, Dunya.
  - **Senegal:** Dunya, Mikaty, Bictorys, **Flutterwave Sénégal** (22/05/25), Samir Money, Versus Finances Tech, Copay, Sesa Digital Finance, Julaya SN, **Djamo SN (EP.SN.010/2025, 03/09/25)**, African Financial Agent.
  - **Benin:** Julaya Bénin, Open SI.
  - **Burkina Faso:** InTouch, Kerry Payments.
  - **Mali:** InTouch, Cauridor.
  - **Niger:** iFutur.
  - **Guinea-Bissau:** InTouch.
  - **Togo:** InTouch, Ollo Africa, Semoa (EP.TG.003/2026, 20/01/26).
  - Sources: [BCEAO list (PDF)](https://www.bceao.int/sites/default/files/2026-03/LISTE%20DES%20ETABLISSEMENTS%20DE%20PAIEMENT%20AGR%C3%89%C3%89S%20DANS%20L%E2%80%99UMOA%20au%2031%20janvier%202026.pdf); [Trésor CI, 19 Mar 2026](https://tresor.gouv.ci/tres/espace-uemoa-monnaie-electronique-la-bceao-agree-31-nouveaux-etablissements-dont-09-en-cote-divoire/)
- **Newer list:** the BCEAO home page announced a list of licensed EPs "as of 31 Aug 2026", published 8 Oct 2026. I could not open it. — [BCEAO](https://www.bceao.int/fr) (via search result only)

### Inferences
- Licence numbers are per country (for example Julaya holds separate EP.CI, EP.SN and EP.BN licences; InTouch holds BF, GB, ML and TG). **In practice there is no single WAEMU passport for EPs.** Each country needs its own entity or licence through the local BCEAO national directorate.
- For Jokko, an EP licence (100 M FCFA) is the minimum compliant vehicle to own the customer account, issue cards (service v) and run transfers. It cannot hold savings that earn interest or extend credit.
- The 2025 crackdown means a "partner first" model in which the startup touches client funds without its own licence is no longer viable in WAEMU. Before licensing, Jokko can only be a technical provider or a registered agent of a licensed PSP.
- Observed licensing time: firms that filed before the 2025 deadlines were licensed between May and September 2025. Six months of review plus file preparation suggests **9–15 months** from company formation to an EP licence.

### Gaps
- No information on how the BCEAO handles EP cross-border extension; the instruction has no explicit chapter on it.
- The EP liquidity and own-funds calculation rules ("specified by the Central Bank") were not found.
- No official application fees found.

---

## 3. WAEMU: microfinance (SFD) licence as the lending and deposit route

### Takeaway
A microfinance (SFD) licence is the only sub-bank WAEMU licence that allows **both deposits (with interest) and credit**. **Djamo Finances SA became the first fintech to get one** (Côte d'Ivoire, announced Sept 2025, after a process of about 3 years). The SFD law sets no fixed minimum capital. The licence is national (Ministry of Finance after a binding BCEAO opinion), and lending is capped by the **24% usury ceiling**. SFDs with outstanding deposits or loans above 2 bn FCFA fall under direct BCEAO and Banking Commission supervision (art. 44).

### Cited Findings
- **Licensing authority:** microfinance activity requires prior approval from the **Ministry of Finance of the host state, after a binding opinion (avis conforme) of the BCEAO**. — [BCEAO SFD regulation compendium, ch. 7](https://www.bceao.int/sites/default/files/inline-files/chapitre_7_-_reglementation_specifique_aux_institutions_de_microfinance.pdf)
- **Capital rules:**
  - Share capital must be fully subscribed before filing, with at least 25% paid up. The rest must be paid before the Minister grants approval. — [BCEAO ch. 7](https://www.bceao.int/sites/default/files/inline-files/chapitre_7_-_reglementation_specifique_aux_institutions_de_microfinance.pdf)
  - The SFD law **sets no minimum entry capital**; capital must match the business plan. — [ANSSFD Benin guide](https://anssfd.bj/wp-content/uploads/2023/12/GUIDE-DINSTRUCTION-DES-DOSSIERS-DE-DMDE-DAGREMENT_Definitif.pdf)
- **Article 44 threshold:** the BCEAO and Banking Commission directly supervise SFDs whose deposits and/or loans exceed **2 bn FCFA (about €3.05 M)**. Some sources add "for two consecutive financial years". — [Trésor CI microfinance](https://microfinance.tresor.gouv.ci/micro/bceao-et-commissions-bancaires/); [BCEAO texts](https://www.bceao.int/sites/default/files/2017-11/-recueil-des-textes-legaux-et-reglementaires-regissant-les-sfd-de-lumoa.pdf)
- **Legal history:** PARMEC (1993) was replaced by the 2007 uniform SFD law, which each state transposes into national law. — [BCEAO ch. 7](https://www.bceao.int/sites/default/files/inline-files/chapitre_7_-_reglementation_specifique_aux_institutions_de_microfinance.pdf)
- **Digital channels:** the BCEAO's 2022 digitalisation guide lets SFDs partner with IT providers or EMEs, issue e-money on their own platform and carry out **digital credit**. — [BCEAO SFD digitalisation guide (June 2022)](https://www.bceao.int/sites/default/files/2022-11/Guide%20pour%20la%20digitalisation%20des%20op%C3%A9rations%20financi%C3%A8res%20des%20SFD%20dans%20l'UEMOA.pdf)
- **SFDs as payment and e-money providers:** SFDs can issue e-money with BCEAO authorisation if own funds and deposits are each ≥ 300 M FCFA (EME Instruction art. 11). They are also recognised PSPs under 001-01-2024. — [EME Instruction](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf); [EP Instruction](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **Djamo case (Côte d'Ivoire):**
  - Djamo Finances SA obtained a microfinance licence, announced 11 Sept 2025. It was granted by the Ivorian Ministry of Economy and Finance with a favourable BCEAO opinion, after about 3 years.
  - It enables uncapped current accounts, a savings account paying **up to 6%/yr**, and cash-flow loans **up to 1 M FCFA (about €1,524)**.
  - Sources: [Ecofin Agency](https://www.ecofinagency.com/finance/1209-48632-ivorian-fintech-djamo-breaks-new-ground-with-bceao-microfinance-approval); [Financial Afrik EN](https://www.financialafrik.com/en/2025/09/16/uemoa-ivorian-fintech-djamo-becomes-the-first-to-obtain-a-microfinance-license); [Digital Mag CI](https://digitalmag.ci/zone-uemoa-la-fintech-djamo-met-sur-le-marche-djamo-finances/?amp=1)
- **Sector size:** 533 active SFDs in the UMOA at 31 Mar 2025, with 4,807 service points and 19.7 M clients. — [AllAfrica](https://fr.allafrica.com/stories/202508250605.html)

### Inferences
- **For a lending neobank, the SFD (SA form) route is the realistic WAEMU path.** It is far cheaper than a bank (no fixed capital floor versus 20 bn FCFA) and Djamo has shown regulators will grant it to a fintech. The cost is a long process (Djamo took about 3 years) and national scope.
- The best-practice structure is a group with an EP (payments and cards) plus an SFD (deposits and credit), as Djamo now has in Côte d'Ivoire. An EME is optional.
- Once outstanding deposits or loans pass 2 bn FCFA, expect BCEAO and Banking Commission supervision and prudential norms comparable to banks.

### Gaps
- No verified figure for the capital the BCEAO expects in practice from an SA-form SFD. Djamo's SFD capital is not public in the sources found.
- The current SFD prudential ratios (capital adequacy, liquidity, credit concentration) were not retrieved.
- I could not determine whether an SFD licence can be extended to other WAEMU states, or whether a new national licence is needed in each.

---

## 4. WAEMU: full banking licence

### Takeaway
New WAEMU bank licences now require **20 bn FCFA (about €30.5 M)** of minimum capital, up from 10 bn (decided 21 Dec 2023, applies immediately to new applications). Existing banks have until about January 2027 to comply. This rules a bank licence out for an early-stage startup.

### Cited Findings
- **Decision:** the UMOA Council of Ministers raised minimum bank capital from 10 bn to **20 bn FCFA** on 21 Dec 2023 (BCEAO notice 5 Jan 2024).
  - Banks licensed before 1 Jan 2024 have **3 years** to comply, and had to file compliance plans by 1 July 2024.
  - The new threshold applies immediately to new licence applications.
  - Sources: [Agence Ecofin](https://www.agenceecofin.com/banque/1001-115087-augmentation-du-capital-social-des-banques-dans-l-uemoa-la-bceao-apporte-des-precisions-sur-le-processus); [Sika Finance](https://www.sikafinance.com/marches/uemoa-un-delai-de-3-ans-accorde-aux-banques-pour-porter-leur-capital-a-20-milliards-fcfa_44294); [EcoMatin](https://ecomatin.net/uemoa-le-capital-social-minimum-des-banques-passe-de-10-milliards-a-20-milliards-de-fcfa)
- **Scale of the raise:** 65 banks needed to raise about 472.8 bn FCFA (about $850 M) in total. — [Agence Ecofin](https://www.agenceecofin.com/banque/0501-114983-hausse-du-capital-social-des-banques-de-l-umoa-les-investisseurs-seront-sollicites-a-hauteur-de-850-millions)
- **No single licence:** under the uniform banking law, licences are granted nationally by the Minister of Finance on a binding opinion of the Banking Commission. A bank licensed in one state needs separate approval to set up in another. — [inferred from the BCEAO texts' structure; not directly verified this session]

### Inferences
- The bank route is relevant only as a long-term (5+ year) option or via acquiring a small bank. The SFD route gives deposits and credit at a fraction of the capital.

### Gaps
- Capital for an "établissement financier de crédit" (EFC) in WAEMU was not verified. It is widely cited as 3 bn FCFA (about €4.57 M) but **unverified this session**.
- No sourced figures for bank licensing timelines (commonly cited as 12+ months), and the single-licence status was not verified.

---

## 5. WAEMU usury caps (taux d'usure) and fee treatment

### Takeaway
From **1 June 2026**, the usury ceiling (on the all-in TEG/TAEG) is **14% for banks**, down from 15%, and **24% for SFDs and financial credit institutions** (Council of Ministers Decision n°19/29-12-2025/CM/UMOA). Fees, commissions and insurance tied to the loan count toward the TEG, so "fee-based" digital lending that pushes the effective rate above the cap is usurious.

### Cited Findings
- **The decision:** Decision n°19/29-12-2025/CM/UMOA (Cotonou, 29 Dec 2025) sets **14% for banks** and **24% for EFCs and SFDs**, effective **1 June 2026**. The BCEAO implementing notice is Avis n°007-12-2025 of 31 Dec 2025. — [BCEAO decision PDF](https://www.bceao.int/sites/default/files/2026-01/Decision-No19-du-29-12-2025_CMUMOA_fixant_le_taux_de_l-usure.pdf); [Financial Afrik, 27 Jul 2026](https://www.financialafrik.com/2026/07/27/taux-dusure-dans-luemoa-le-recalibrage-opere-par-la-decision-n19-29-12-2025-cm-umoa/); [Affaires & Entreprises](https://affairesetentreprises.ci/2026/05/02/uemoa-la-bceao-abaisse-les-plafonds-de-taux-dusure-banques-et-microfinances-sous-pression-reglementaire/)
- **What counts toward the cap:** the TAEG includes nominal interest **plus all fees, commissions and insurance premiums** linked to granting the loan. A loan is usurious if its TEG/TAEG exceeds the ceiling for the lender's category, whatever the contract form or borrower type. Charging multiple ancillary fees outside the TEG is flagged as a circumvention risk. — [Financial Afrik](https://www.financialafrik.com/2026/07/27/taux-dusure-dans-luemoa-le-recalibrage-opere-par-la-decision-n19-29-12-2025-cm-umoa/)
- **Conflict on the previous SFD rate:**
  - Financial Afrik says the 24% SFD ceiling was **unchanged**. — [Financial Afrik](https://www.financialafrik.com/2026/07/27/taux-dusure-dans-luemoa-le-recalibrage-opere-par-la-decision-n19-29-12-2025-cm-umoa/)
  - The BCEAO's SFD page cites 24% from Decision CM/UMOA/011/06/2013 (effective 2014). — [BCEAO](https://www.bceao.int/fr/documents/taux-dusure-pour-les-operations-de-credit-des-sfd-dans-la-zone-umoa)
  - Agence Ecofin's headline ("the microfinance usury rate **passes to** 24% in June") and other press imply it was previously 27%. — [Agence Ecofin](https://www.agenceecofin.com/actualites-finance/3004-138022-umoa-le-taux-de-l-usure-pour-les-institutions-de-microfinance-passe-a-24-en-juin)
  - **Unresolved.** The current figure of 24% is consistent across all sources.
- **Digital lenders and data:** in August 2023 the ARTCI warned online-loan apps in Côte d'Ivoire (for example "Easy Cash") that were collecting personal data without authorisation, and gave them 10 days to comply. — [Osiris](https://osiris.sn/nouvelle-forme-de-pret-en-ligne-en-cote-d-ivoire-l-artci-appel-a-la-vigilance.html)

### Inferences
- A 30-day nano-loan with a flat 5% fee annualises far above 24%. Short-tenor digital credit must be priced so the **annualised** all-in TEG stays at or below 24% (as an SFD) or 14% (if originated by a partner bank).
- Partnering with a bank for credit is therefore *more* constraining on price (14%) than an own SFD (24%). This is another argument for the SFD route.
- The ARTCI action shows digital lenders face data-protection enforcement as well as usury exposure.

### Gaps
- No primary text found on how the BCEAO treats very short-term loans or late fees under the TEG computation.
- No documented enforcement cases against digital lenders for usury.

---

## 6. CEMAC (BEAC / COBAC): payment services, microfinance, banking, FX controls

### Takeaway
In CEMAC, payments run under Règlement n°04/18/CEMAC/UMAC/COBAC (in force 1 Jan 2019). An établissement de paiement (which can issue e-money) needs **500 M FCFA (about €762k)** of capital, is licensed by the national Ministry of Finance after a binding COBAC opinion, and **cannot lend or take deposits**.
Lending requires a microfinance licence: category 2 (deposits plus credit) at **300 M FCFA** or category 3 (credit only, no deposits) at **150 M FCFA**. Bank capital rose to **25 bn FCFA** on 1 Jan 2026.
FX rules (Règlement 02/18) cap card use outside CEMAC at 5 M FCFA per trip and online payments at 1 M FCFA per month without justification. This makes multi-currency and international cards harder than in WAEMU.

### Cited Findings
- **Who may provide payment services:** only credit institutions, microfinance institutions and licensed payment institutions (art. 5). Licensing is by the **national monetary authority after a binding COBAC opinion** (art. 23). — [Lextenso (2019)](https://www.labase-lextenso.fr/l-essentiel-droits-africains-des-affaires/2019-n5/les-conditions-d-exercice-des-services-de-paiement-dans-la-cemac-DAA112d1); [Chazai Wamba commentary](https://cesttoutdroit.com/article-droit-bancaire-et-financier/nouveau-reglement-cemac-relatif-aux-services-de-paiement/)
- **Review times:** the COBAC opinion is due within 6 months, and silence counts as approval. The technical solution goes to the BEAC (2–3 months). — [Lextenso](https://www.labase-lextenso.fr/l-essentiel-droits-africains-des-affaires/2019-n5/les-conditions-d-exercice-des-services-de-paiement-dans-la-cemac-DAA112d1); [Chazai Wamba](https://cesttoutdroit.com/article-droit-bancaire-et-financier/nouveau-reglement-cemac-relatif-aux-services-de-paiement/)
- **What a CEMAC EP can and cannot do:**
  - Issuing and managing e-money is a payment service under the regulation.
  - EPs must be an SA with a board.
  - They **cannot collect deposits, grant credit or pay interest**.
  - Client funds must be ring-fenced at banks by the next business day.
  - FX exchange is allowed only as an ancillary service within FX rules.
  - Services are limited to the CEMAC zone.
  - Source: [Chazai Wamba](https://cesttoutdroit.com/article-droit-bancaire-et-financier/nouveau-reglement-cemac-relatif-aux-services-de-paiement/)
- **EP capital and own funds:** COBAC R-2019/02 (23 Sept 2019) sets minimum paid-up capital at **500 M FCFA**, with core own funds at least 75% net equity. Own-funds requirements include **2% of average daily e-money outstanding** over 6 months. — [COBAC R-2019/02 (copy)](https://cesttoutdroit.com/wp-content/uploads/2023/06/23-septembre-2019-Reglement-COBAC-R-2019-02-normes-prudentielles-etablissements-de-paiement.pdf)
- **Reform under way (unadopted, sources conflict):**
  - A draft would **double EP capital to 1 bn FCFA** and create a fintech status. — [EcoMatin (headline only; page unreachable)](https://ecomatin.net/la-cobac-veut-doubler-le-capital-minimum-des-operateurs-de-mobile-money-et-creer-un-statut-pour-les-fintechs)
  - At Libreville on 22–24 June 2026, consultations on eight draft regulations agreed a **lower** minimum capital for "second-category" payment operators, easier use of distributors, a future **regulatory sandbox**, and rules on deferred payment, international transfers and rural KYC. No figures or adoption date were given. — [Sika Finance, 1 Jul 2026](https://www.sikafinance.com/marches/cemac-la-cobac-affine-les-futures-regles-des-services-bancaires-et-des-paiements_62676)
- **Banks and financial institutions (COBAC R-2025/02, 10 Dec 2025, in force 1 Jan 2026):**
  - Bank capital rises from 10 bn to **25 bn FCFA (about €38.1 M)**.
  - Financial-institution capital rises from 2 bn to **4 bn FCFA (about €6.1 M)**.
  - Existing banks have a step-up path: 14 bn by end-2026, 18 bn end-2027, 22 bn end-2028, 25 bn end-2029.
  - New licences must meet 25 bn or 4 bn immediately.
  - Source: [Droit Médias Finance](https://www.droitmediasfinance.com/index.php/actualites/droit-bancaire/1159-cemac-le-reglement-cobac-r-2025-02-releve-le-capital-social-minimum-des-etablissements-bancaires-a-25-milliards-de-fcfa)
- **Microfinance (Règlement 01/17/CEMAC/UMAC/COBAC, in force 1 Jan 2018; capital set by COBAC EMF R-2017/03):**
  - **Category 1:** members only, cooperative form, at least 100 members, no fixed minimum capital.
  - **Category 2:** collects savings and lends to third parties; **300 M FCFA (about €457k)**, phased in. The final step date was not confirmed.
  - **Category 3:** lends without collecting savings; **150 M FCFA (about €229k)** from 1 Jan 2021.
  - Sources: [Investir au Cameroun](https://www.investiraucameroun.com/microfinance/2706-11019-la-cobac-fixe-de-nouveaux-montants-pour-constituer-le-capital-social-des-microfinances-dans-la-cemac); [LC-Doc R-2017/03](https://lc-doc.com/document/reglement-cobac-emf-r-2017-03-portant-fixation-du-capital-social-minimum-des-etablissements-de-microfinance-des-deuxieme-et-troisieme-categories)
- **Microfinance sector:** CEMAC had 521 microfinance institutions at end-2024 (384 in Cameroon), with a combined balance sheet of 2,061 bn FCFA and NPLs of 177.8 bn FCFA. A draft regulation on microfinance liquidity is pending. — [Sika Finance](https://www.sikafinance.com/marches/cemac-la-cobac-affine-les-futures-regles-des-services-bancaires-et-des-paiements_62676)
- **FX controls:**
  - Règlement n°02/18/CEMAC/UMAC/CM (21 Dec 2018) and Instruction n°008/GR/2019 govern use of electronic payment instruments outside CEMAC; prepaid cards are explicitly covered.
  - Withdrawals and payments abroad are capped at **5 M FCFA (about €7,622) per person per trip**. Remote (online) payments are free up to **1 M FCFA (about €1,524) per month per person**. Above these, supporting documents are required (Lettre circulaire 004/GR/2022).
  - Issuers must report these transactions monthly to the BEAC. Failure to justify can lead to termination of all the customer's e-payment instruments.
  - Sources: [Agence Ecofin](https://www.agenceecofin.com/finances-publiques/2806-67370-la-beac-plafonne-les-retraits-et-paiements-par-carte-bancaire-hors-de-la-cemac); [Lextenso 2022](https://www.labase-lextenso.fr/l-essentiel-droits-africains-des-affaires/2022-n10/beac-nouvelles-conditions-de-reglement-a-distance-des-transactions-et-d-utilisation-a-l-exterieur-des-instruments-de-paiement-electronique-DAA201d4); [BOA Congo 2023](https://boa-cg.com/2023/11/23/nouvelles-dispositions-sur-les-conditions-et-modalites-dutilisation-des-instruments-de-paiement-electronique-hors-zone-cemac/)
  - Sources conflict on the justification window (30 vs 90 days).
- **USD transfers:** in July 2025 the BEAC issued new procedures for USD transfers outside CEMAC to reduce delays. — [Agence Ecofin](https://www.agenceecofin.com/actualites-finance/2307-130330-la-beac-ajuste-ses-procedures-pour-les-transferts-en-dollars-hors-cemac-pour-reduire-les-delais) (search snippet only)
- **Partner-bank model in CEMAC (Wave, Cameroon):**
  - COBAC decision D-2025/122 (11 June 2025) gave **Commercial Bank Cameroun** prior authorisation to offer a "Wave" payment service: cash-in/out, P2P, merchant and bill payments, wallet-to-bank and inbound international transfers. It runs in partnership with Wave Transfer S.A., after a BEAC no-objection on the technical solution.
  - A commentator says this sidestepped a Ministry of Finance rule barring banks from working with fintechs that lack a PSP licence.
  - Source: [Droit Médias Finance, 13 Jul 2025](https://droitmediasfinance.com/index.php/actualites/droit-tech-fintech/1022-cameroun-la-cobac-accorde-lautorisation-prealable-a-commercial-bank-cameroun-pour-son-nouveau-service-de-paiement-wave)
- **Dormant accounts:** 2025 CEMAC rules require banks, microfinance institutions and EPs to identify dormant accounts and transfer the funds to deposit funds or the BEAC. — [Sika Finance](https://www.sikafinance.com/marches/cemac-la-cobac-affine-les-futures-regles-des-services-bancaires-et-des-paiements_62676)

### Inferences
- In CEMAC, a **bank-sponsored service authorisation** (the Wave–CBC model) is a proven "partner first" route. The bank holds the licence, and COBAC and BEAC approve the product and technical solution.
- For lending in CEMAC, a **category 3 microfinance institution (150 M FCFA, credit only)** is the cheapest licensed lender. Category 2 (300 M FCFA) adds deposits.
- FX controls make "multi-currency accounts" for CEMAC residents largely infeasible. Cards will hit the 1 M FCFA/month online cap, and an EP's FX activity is restricted to ancillary conversion.

### Gaps
- The 2025/2026 CEMAC reform texts (EP categories and new capital levels) were not adopted as of the sources found. Check COBAC for adoption after June 2026.
- No passporting mechanism for CEMAC EPs was found; licences appear to be per state.
- The full text of FX Règlement 02/18 on residents holding foreign-currency accounts was not retrieved.

---

## 7. DRC (BCC) and Guinea (BCRG)

### Takeaway
DRC e-money institutions need **USD 2.5 M** paid-up capital (BCC Instruction n°24 of 2011). Guinea's EME capital is **GNF 4 bn** (BCRG Decision D/2018/001). Both are separate central banks with national licences and no link to the WAEMU or CEMAC regimes. These are second-wave markets.

### Cited Findings
- **DRC e-money capital:** Instruction n°24 (11 Nov 2011) on e-money and EMEs, art. 6, requires paid-up capital equivalent in CDF to **USD 2,500,000**. Filing is with the BCC Governor. — [BCC microfinance texts compendium (Aug 2019)](https://legalrdc.com/wp-content/uploads/2020/06/Recueil_des_textes_reglementaires_Microfinance_19_08_2019_12H.pdf); [Maxence Kiyana](https://maxencekiyana.com/la-monnaie-electronique-en-rdc/)
- **Other DRC instruments:** BCC Instruction n°42 (9 Mar 2020) covers cards and acquiring and created an "aggregator" category. Instruction n°58/2024 reportedly mandates interoperability. AML is under Law 04/016 with CENAREF reporting. — [RDC national financial inclusion strategy 2023–2028](https://finances.gouv.cd/uploads/files/Strategie%20nationale%20d'inclusions%20financi%C3%A8res.pdf); [Licentium](https://www.licentium.io/hub/dr-congo) (secondary)
- **DRC microfinance:** BCC Instruction n°010 sets microfinance minimum capital. Figures were not extracted. — [BCC](https://www.bcc.cd/system/files_force/dsif/instruction-n.-010_aux_institutions_de_microfinance_relative_a_la_fixation_du_capital_minimum.pdf/?download=1)
- **Guinea EME capital:** BCRG Decision N°D/2018/001/BCRG/CAM (29 June 2018) sets EME minimum capital at **GNF 4,000,000,000**. EME issuance is framed by Decision D/2015/003/CAM (31 Mar 2015). — [BCRG compendium](https://www.bcrg-guinee.org/wp-content/uploads/2020/02/Recueil-de-textes.pdf); [regalert summary](https://regalert.today/document/5869d682-d351-49ab-8a95-9c0d3eefcc28/text)
- **Guinea market:** 11 licensed EMEs in late 2025, up from 6 in 2024. — [BCRG "BCRG et les EME"](https://www.bcrg-guinee.org/wp-content/uploads/2025/08/BCRG-et-les-EME.pdf)
- **Guinea instant payments:** the BCRG launched the **NimbaPay** instant-payment and interoperability platform on 22 July 2026. — [Guinéenews](https://guineenews.org/2026/07/22/guinee-la-bcrg-lance-nimbapay-la-plateforme-nationale-qui-revolutionne-les-paiements-instantanes-et-linteroperabilite/)
- **Guinea crypto stance:** in August 2026 the BCRG instructed EMEs and PSPs to block and report wallets used in crypto scams, and bars crypto as legal tender. — [Droit Médias Finance](https://droitmediasfinance.com/index.php/actualites/droit-tech-fintech/1362-guinee-cryptoactifs-la-banque-centrale-de-la-republique-de-guinee-bcrg-interdit-lusage-des-cryptomonnaies-comme-monnaie-ayant-cours-legal)

### Inferences
- DRC's USD 2.5 M e-money floor is about 5x the WAEMU EME floor. A partner-bank entry is more capital-efficient there.
- Guinea's crypto hostility reinforces Jokko's non-crypto positioning.

### Gaps
- DRC microfinance capital amounts and any 2023–2026 BCC payment-services law were not verified.
- The GNF-to-EUR equivalent is not given (rate not provided).
- No Guinean payment-institution regime was found.

---

## 8. Partnership / BaaS models: how Djamo, Wave, Julaya and others actually operate

### Takeaway
The proven West African pattern is a three-stage path:
1. Start as a front-end on a **partner bank's** licence, with co-branded Visa prepaid cards issued by the bank.
2. Get **own payment licences** (EP or EME) per country.
3. Add a **microfinance licence** for deposits and credit.

Djamo followed exactly this path: BGFIBank CI and Ecobank cards, then EP licences in CI and SN (2025), then Djamo Finances SA microfinance (2025). Wave started on partner banks and then got an EME licence (Wave Digital Finance) in **April 2022, not 2023**.

### Cited Findings
- **Djamo cards:** the Djamo Visa card is a **co-branded Visa card issued by partner banks BGFIBank Côte d'Ivoire or Ecobank Côte d'Ivoire**. The BCEAO EME page lists Djamo together with BGFI CI and Ecobank Senegal prepaid cards. — [Djamo Visa card page](https://www.djamo.com/fr-ci/carte-visa); [BCEAO EME page](https://www.bceao.int/fr/content/etablissements-de-monnaie-electronique)
- **Visa partnership:** Visa announced a strategic partnership with Djamo in March 2025 (CI and SN first), with Djamo distributing Visa cards issued by its partner banks. — [Sika Finance](https://www.sikafinance.com/marches/visa-et-djamo-unissent-leurs-forces-pour-stimuler-l-innovation-financiere-en-afrique-de-l-ouest_51786)
- **Djamo's licences:** EP licences EP.CI.005/2025 (4 Sept 2025) and EP.SN.010/2025 (3 Sept 2025), plus the microfinance licence for Djamo Finances SA (Sept 2025). — [BCEAO EP list](https://www.bceao.int/sites/default/files/2026-03/LISTE%20DES%20ETABLISSEMENTS%20DE%20PAIEMENT%20AGR%C3%89%C3%89S%20DANS%20L%E2%80%99UMOA%20au%2031%20janvier%202026.pdf); [Ecofin Agency](https://www.ecofinagency.com/finance/1209-48632-ivorian-fintech-djamo-breaks-new-ground-with-bceao-microfinance-approval)
  - Whether Djamo also holds a separate EME licence is **unclear**. Some press describes it as an EME, but the official lists found show EP and microfinance only. — [Classe Export](https://classe-export.com/index.php/pays/afrique/91972-cote-divoire-le-nouvel-exploit-de-la-fintech-djamo/)
- **Wave:** Wave Digital Finance obtained a BCEAO EME licence on **14 April 2022**. It was the first non-bank, non-telco multi-market WAEMU player to do so; before that it operated through partner banks. — [Financial Afrik, 21 Apr 2022](https://www.financialafrik.com/2022/04/21/le-pingouin-wave-mobile-money-devient-etablissement-de-monnaie-electronique/); [Team France Export](https://www.teamfrance-export.fr/infos-sectorielles/16753/16753-la-bceao-accorde-la-licence-detablissement-de-monnaie-electronique-a-wave)
  - In Cameroon (CEMAC), Wave operates through Commercial Bank Cameroun's COBAC-authorised service (see §6).
- **Julaya:** EP licences in CI (EP.CI.004/2025), SN (EP.SN.009/2025) and BJ (EP.BN.001/2025). — [BCEAO EP list](https://www.bceao.int/sites/default/files/2026-03/LISTE%20DES%20ETABLISSEMENTS%20DE%20PAIEMENT%20AGR%C3%89%C3%89S%20DANS%20L%E2%80%99UMOA%20au%2031%20janvier%202026.pdf)
  - Earlier it offered a prepaid **Mastercard** for corporate expenses. — [TechCrunch 2022](https://techcrunch.com/2022/09/21/ivorian-fintech-julaya-gets-5m-to-become-banking-partner-for-businesses-in-francophone-africa/)
  - Bank of Africa CI white-labels "Bulk Payment (Julaya)" to SMEs. — [BOA CI](https://boacoteivoire.com/pme/comptes-services/bulk-payment/)
  - Julaya reportedly partners with Ecobank, SIB and BOA. — search summary of Julaya site; not independently verified
- **Other licensed processors:** Flutterwave Sénégal (EP.SN.004/2025), InTouch (4 countries), CinetPay, PayDunya/Dunya and Touchpoint all hold EPs. These are potential **payment-rail partners** (collections, payouts, acquiring) for a neobank. — [BCEAO EP list](https://www.bceao.int/sites/default/files/2026-03/LISTE%20DES%20ETABLISSEMENTS%20DE%20PAIEMENT%20AGR%C3%89%C3%89S%20DANS%20L%E2%80%99UMOA%20au%2031%20janvier%202026.pdf)
- **No exclusivity:** PSP partnerships may not contain exclusivity clauses (Instr. 001-01-2024 art. 7). This helps a startup negotiate multi-bank set-ups. — [BCEAO Instruction 001-01-2024](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **Bridge Bank vs Bridge:** Bridge Bank Group CI (Ivorian bank) is unrelated to Bridge (the Stripe stablecoin company, which offers Visa card issuing). The latter is crypto-adjacent and inappropriate for Jokko's non-crypto product. — [Stripe newsroom](https://stripe.com/newsroom/news/bridge-partners-with-visa)

### Inferences
- **Card issuing:** in WAEMU, Visa or Mastercard principal-member banks (for example BGFIBank CI, Ecobank, BOA) issue co-branded prepaid cards for fintechs. An EP licensed for service (v), "issuing payment instruments", could in principle issue its own cards via a scheme sponsor or principal membership. Djamo still uses banks.
- **Recommended partner stack before licensing:** a partner bank (card issuing, ring-fenced accounts, possibly credit origination at ≤14% TEG) plus a licensed EP or EME (wallet rails), with Jokko as the technical and marketing layer. Jokko must display the issuer's name (EME Instruction art. 4) and must not hold funds itself.

### Gaps
- **Not researched (search budget exhausted):**
  - Bank BaaS API offerings (Coris, NSIA, Orabank, Société Générale, Afriland, UBA, Access, Banque Atlantique, Baobab, Advans).
  - GIM-UEMOA membership rules.
  - Processors (HPS, Interswitch, Monnet).
  - Kori's legal structure.
  - The founder should get quotes directly; no public BaaS price lists are known.

---

## 9. Agents and sub-agents (distribution)

### Takeaway
The model depends on the licence:
- **EMEs** may run distributor and sub-distributor networks.
- **EPs** may *not* use distributors, but may use **BCEAO-registered payment-services agents**.
- **Banks** use BCEAO-registered "agents bancaires".

A startup acting for a licensed institution before getting its own licence must itself be registered as an agent or intermédiaire mandaté where it handles customers.

### Cited Findings
- **EME distributors:** EMEs may use legal or natural persons as distributors, organised as principal distributors and sub-distributors. The issuer stays responsible, including for AML/CFT (arts. 17–18). — [EME Instruction](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **EP rules:** distributors are banned (art. 8.4). Agents must be registered by the BCEAO before acting (art. 38). The EP remains fully liable (art. 39). — [EP Instruction](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
  - Avocats Houda's summary mentions only the distributor ban, not the agent route. The instruction text shows both rules coexist. — [Avocats Houda](https://www.avocatshouda.com/uemoa-entree-en-vigueur-de-linstruction-n001-01-2024-relative-aux-services-depaiement-dans-les-etats-membres-de-lumoa/)
- **Definitions:** an "agent bancaire" is registered with the BCEAO and acts for one or more credit institutions. An "agent de services de paiement" is registered with the BCEAO. Both are "intermédiaires mandatés". — [EP Instruction, art. 1](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **CEMAC:** COBAC supervises distributors and sub-distributors of PSPs. The June 2026 reform drafts ease conditions for using distributors. — [Chazai Wamba](https://cesttoutdroit.com/article-droit-bancaire-et-financier/nouveau-reglement-cemac-relatif-aux-services-de-paiement/); [Sika Finance](https://www.sikafinance.com/marches/cemac-la-cobac-affine-les-futures-regles-des-services-bancaires-et-des-paiements_62676)

### Inferences
- If Jokko wants a physical cash-in/out network, an EME licence (distributors allowed) or partnership with an EME is more flexible than an EP. Alternatively, rely on PI-SPI interoperability to let users top up from Orange Money or Wave.

### Gaps
- The text of the WAEMU "intermédiaire en opérations de banque" regime (banking law) and the agent-bancaire instruction was not retrieved.

---

## 10. Data protection, AML/CFT and KYC

### Takeaway
Each country has its own data-protection authority and prior-formality regime: Senegal's CDP under Law 2008-12 (still the reference in 2025; a reform is in draft), and Côte d'Ivoire's ARTCI under Law 2013-450, with prior authorisation and the CERTINUM platform launched July 2026. AML/CFT runs under the WAEMU uniform AML/CFT law with national CENTIFs and GIABA oversight. KYC tiers for e-money flow from the EME ceilings (200k FCFA/month unidentified; 2 M FCFA balance identified).

### Cited Findings
- **Senegal:** the CDP's 2025 quarterly opinions still cite **Law n°2008-12 of 25 Jan 2008**. A CDP workshop on 10–11 Oct 2024 was to finalise a revised bill, and I found no evidence it has been adopted. Declarations and authorisation requests rose notably in Q2 2025. — [Osiris](https://osiris.sn/le-senegal-va-reviser-la-loi-sur-la-protection-des-donnees-personnelles.html); [CDP quarterly opinion](https://sppsyrftszniuaicadvk.supabase.co/storage/v1/object/public/public_docs/avis-trimestriels/avis-trimestriel-1752749972939.pdf)
- **Côte d'Ivoire:** all personal-data processing needs prior declaration or **authorisation** from the ARTCI. Authorisation is required for biometrics, geolocation and **transfers abroad** (relevant for cloud hosting and KYC vendors). — [CIO Mag](https://cio-mag.com/cote-divoire-artci-le-traitement-des-donnees-personnelles-desormais-soumis-a-une-autorisation-prealable)
  - The ARTCI launched **CERTINUM**, an online compliance and authorisation platform, in July 2026. — [Droit Médias Finance](https://www.droitmediasfinance.com/index.php/actualites/droit-tech-fintech/1355-cote-divoire-lartci-lance-certinum-la-plateforme-nationale-de-conformite-en-protection-des-donnees-personnelles)
- **Data in the EP Instruction:** EPs must protect user data under the data-protection law of their country of establishment (art. 50). — [EP Instruction](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)
- **AML/CFT basis:** both instructions cite the uniform law on AML/CFT and proliferation financing in UMOA states. EMEs must apply AML/CFT across their distributor networks (art. 26). — [EP Instruction](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf); [EME Instruction](https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **Senegal grey list:** Senegal left the FATF grey list in October 2024. The BCEAO cites this as a reason to tighten fintech oversight. — [BIE/CCIAD](https://bie.cciad.sn/2025/05/09/regulation-des-fintechs-les-precisions-de-la-bceao/)
- **Côte d'Ivoire AML:** Prifinance cites Law n°2016-992 (AML) and Law n°2024-362 (beneficial ownership) for CI. — [Prifinance](https://prifinance.com/en/payments/cote-divoire-payment-license/)
- **Côte d'Ivoire tax on transfers:** a 5% tax on monthly money-transfer turnover (CGI art. 1130), corporate tax at 25% (30% for telecom/ICT), and VAT at 18%. — [Prifinance](https://prifinance.com/en/payments/cote-divoire-payment-license/) (secondary; verify with a tax adviser)

### Inferences
- Budget a separate data-protection filing per country, typically before launch, and get ARTCI authorisation for cross-border data transfers if KYC or cloud vendors sit outside CI.

### Gaps
- **Not verified:**
  - The current WAEMU uniform AML law version (a 2023 revision is reported but was not checked).
  - Formal BCEAO KYC tiers beyond the EME ceilings.
  - Biometric ID integration options.
  - Business onboarding documents (NINEA/RCCM).
  - CENTIF reporting thresholds.
  - Côte d'Ivoire's FATF status.

---

## 11. Recent regulatory developments (2023–2026)

### Takeaway
The main changes:
- **PI-SPI**, the BCEAO instant-payment platform, launched on 30 Sept 2025. By 30 Sept 2026 it had 175 participants authorised to offer it to the public, including Wave, Djamo, Julaya and Orange.
- **EP licensing** was enforced from May 2025.
- **Bank capital** doubled to 20 bn FCFA.
- **Usury** ceilings were recalibrated (banks at 14% from June 2026).
- **No general BCEAO regulatory sandbox** exists yet. Only a PI-SPI API test sandbox (Nov 2025) is live.
- **CEMAC** is reworking its payment and fintech rules and raised bank capital to 25 bn.

### Cited Findings
- **PI-SPI launch:** officially launched **30 Sept 2025** in Dakar. It runs 24/7 across all 8 states, uses QR code or alias, is **free for domestic transfers**, and links banks, EMEs, microfinance institutions and EPs. — [BCEAO launch page](https://www.bceao.int/fr/content/lancement-officiel-de-la-plateforme-interoperable-du-systeme-de-paiement-instantane-pi-spi); [CIO Mag](https://cio-mag.com/paiement-instantane-pi-spi-la-plateforme-de-la-bceao-officiellement-lancee/)
- **PI-SPI connections:** at 2 Apr 2026, 80 institutions were connected (59 banks, 9 EMEs, 11 microfinance institutions, 1 EP) and 42 more were in live testing. The BCEAO set **30 June (2026)** as the adherence deadline. — [search summary of BCEAO/press](https://www.financialafrik.com/2026/03/05/paiements-instantanes-pi-spi-dans-luemoa-liste-actualisee-des-etablissements-autorises-par-la-bceao/); [Togo First](https://www.togofirst.com/fr/finance/0304-18641-la-bceao-fixe-au-30-juin-l-adhesion-des-operateurs-a-sa-plateforme-de-paiement-instantane-pi-spi) (headline only)
- **PI-SPI participants at 30 Sept 2026:** **175** authorised to open services to the public: SN 43, CI 38, BF 20, ML 19, BJ 18, TG 17, NE 13, GB 7. Named participants include Wave Digital Finance, Wave CI, Orange, MTN, Moov, Djamo SN and CI, Julaya, Baobab, Cofina, Mikaty and iFutur. — [Financial Afrik, 1 Oct 2026](https://www.financialafrik.com/2026/10/01/bceao-liste-des-175-participants-autorises-a-ouvrir-les-services-de-pi-spi-au-public-au-30-septembre-2026/)
- **PI-SPI developer sandbox:** a public sandbox for the PI-SPI **API-Business** was opened on 13 Nov 2025. It is a technical test environment, not a regulatory sandbox. — [Droit Médias Finance](https://www.droitmediasfinance.com/index.php/actualites/droit-tech-fintech/1139-uemoa-fintech-un-bac-a-sable-sandbox-public-lance-pour-lapi-business-de-la-plateforme-interoperable-du-systeme-de-paiement-instantane)
- **Regulatory sandbox status:** the BCEAO created a FinTech Committee on 18 Feb 2020 to build an innovation hub and regulatory sandbox. I found no launch of a general regulatory sandbox by Oct 2026. In May 2025 a BCEAO official mentioned the sandbox and "phased licensing" only as options. — [BCEAO fintech framework page](https://www.bceao.int/fr/documents/cadre-reglementaire-des-fintech-dans-lumoa); [Jeune Afrique](https://www.jeuneafrique.com/1683512/economie-entreprises/pourquoi-la-bceao-met-la-pression-sur-les-fintech/) (paywalled; via search summary)
- **Enforcement:** unlicensed fintechs were ordered to stop payment services from May 2025 (see §2). I found no public list of named fintechs sanctioned or suspended. — [BIE/CCIAD](https://bie.cciad.sn/2025/05/09/regulation-des-fintechs-les-precisions-de-la-bceao/)
- **CEMAC:** the 2026 reform consultations (sandbox, EP categories) and bank capital at 25 bn FCFA (see §6). In 2024 CEMAC payment systems handled about 3.92 bn transactions worth 182,962 bn FCFA. — [Sika Finance](https://www.sikafinance.com/marches/cemac-la-cobac-affine-les-futures-regles-des-services-bancaires-et-des-paiements_62676)
- **Guinea:** NimbaPay launched July 2026 (see §7).

### Inferences
- PI-SPI lowers the moat of mobile-money incumbents. A licensed EP, EME or SFD can offer free instant interoperable transfers. The first step for PI-SPI access is holding a licence (EP, EME, SFD or bank) or riding on a participant.
- Open banking: the 2024 instruction creates **payment initiation** (20 M FCFA) and **account aggregation** (10 M FCFA registration) statuses, a PSD2-like foundation. I found no mandatory bank API (open-banking access) rule.

### Gaps
- PI-SPI participation fees and technical certification timelines were not found.
- No WAEMU open-banking API mandate was identified.
- The BCEAO list of licensed EPs at 31 Aug 2026 was not read, so EP licensing after February 2026 is unknown.

---

## 12. Realistic sequencing, timelines, costs and pros/cons

### Takeaway
For a clean, non-crypto lending neobank starting in WAEMU (Côte d'Ivoire or Senegal):
1. **Months 0–12:** launch on partner rails (partner bank for cards and accounts; licensed EP or EME for wallet rails). Jokko is the tech and brand layer and never touches funds. In parallel, file an **EP licence (100 M FCFA, 6-month statutory review)**.
2. **Months 6–18:** obtain the EP and join PI-SPI. Start credit only through a partner bank (≤14% TEG) or partner SFD (≤24% TEG).
3. **Months 12–36:** file for an **SFD (microfinance SA) licence** for deposits and credit (Djamo took about 3 years).
4. **Optional:** an EME (300 M FCFA) if agent networks or e-money are needed.
5. **Long term only:** a bank licence (20 bn FCFA).

Expansion is country by country. CEMAC entry is via a bank-sponsored service (Wave model) or an EP at 500 M FCFA, plus a category 3 microfinance institution for credit.

### Cited Findings (summary table; sources as cited in sections above)

| Path | Licensor | Min. capital | EUR approx. | Deposits? | Lending? | Statutory review | Scope |
|---|---|---|---|---|---|---|---|
| WAEMU EP (services i–vi) | BCEAO | 100 M FCFA | €152k | Payment accounts only; no interest | **No** | 6 months (9 with home-supervisor opinion) | Per country (licence numbers per state) |
| WAEMU EP initiation / aggregation | BCEAO | 20 M / 10 M FCFA | €30k / €15k | No | No | 6 months / 3 months (registration) | Per country |
| WAEMU EME | BCEAO | 300 M FCFA; own funds ≥3% of float | €457k | E-money, no interest; 2 M FCFA balance cap | **No** (but bank/SFD loans can fund wallets) | 3 months (clock stops on queries) | Per-country authorisation (art. 20) |
| WAEMU SFD (microfinance) | National Ministry of Finance + binding BCEAO opinion | No legal minimum; must match plan | n/a | **Yes**, with interest (Djamo: up to 6%) | **Yes**, ≤24% TEG | Not fixed; Djamo took about 3 years | National |
| WAEMU bank | Ministry + Banking Commission | 20 bn FCFA | €30.5 M | Yes | Yes, ≤14% TEG | Not found | National |
| CEMAC EP (incl. e-money) | National monetary authority + binding COBAC opinion | 500 M FCFA (reform pending) | €762k | No | **No** | COBAC opinion ≤6 months | CEMAC-limited; per state |
| CEMAC microfinance cat. 3 / cat. 2 | Ministry + COBAC | 150 M / 300 M FCFA | €229k / €457k | Cat. 2 only | Yes | Not found | National |
| CEMAC bank / financial institution | Ministry + COBAC | 25 bn / 4 bn FCFA | €38.1 M / €6.1 M | Yes | Yes | Not found | National |
| DRC EME | BCC | USD 2.5 M | n/a | E-money | No | Not found | National |
| Guinea EME | BCRG | GNF 4 bn | n/a | E-money | No | Not found | National |

- **Fees:** no published official fees for EP or EME applications; realistic time is 9–15 months. — [Prifinance](https://prifinance.com/en/payments/cote-divoire-payment-license/)
- **Djamo benchmark:**
  - Partner-bank cards (BGFI, Ecobank).
  - EP licences CI and SN in Sept 2025, roughly 20 months after Instruction 001-01-2024 was issued.
  - Microfinance licence Sept 2025 after about 3 years.
  - Sources: [Djamo](https://www.djamo.com/fr-ci/carte-visa); [BCEAO EP list](https://www.bceao.int/sites/default/files/2026-03/LISTE%20DES%20ETABLISSEMENTS%20DE%20PAIEMENT%20AGR%C3%89%C3%89S%20DANS%20L%E2%80%99UMOA%20au%2031%20janvier%202026.pdf); [Ecofin Agency](https://www.ecofinagency.com/finance/1209-48632-ivorian-fintech-djamo-breaks-new-ground-with-bceao-microfinance-approval)

### Inferences
- **Pros and cons by path:**
  - **EP first:** cheapest licensed option (€152k capital) and gives own accounts, cards and transfers plus PI-SPI eligibility. It cannot lend or pay interest, distributors are banned, it is per country, and review is 6+ months.
  - **EME:** gets distributor networks and e-money, with a shorter statutory review (3 months). It needs 3x the EP capital, has a 2 M FCFA balance cap, and allows no credit or interest. It adds little over an EP for an app-first neobank.
  - **SFD:** the only affordable route to deposits and credit (24% cap, better than banks' 14%). It is slow (Djamo took about 3 years), national, prudentially heavier above 2 bn FCFA, and requires governance comparable to a credit institution.
  - **Partner bank only:** fastest go-live. Since May 2025 the startup cannot touch funds or present itself as a payment institution (art. 9 bans the use of the "établissement de paiement" title). Economics are shared, and lending is capped at 14% TEG.
- **Indicative minimum capital stack:** EP CI (100 M FCFA) + EP SN (100 M FCFA) + SFD SA (amount set by plan, likely several hundred million FCFA) = **at least 200 M FCFA (€305k) in regulatory capital before the SFD**. Legal, audit, insurance and IT-security costs come on top and were not sourced.
- **Clean-with-regulators principles:**
  - Do not touch client funds before licensing.
  - Show the issuer name on all product communications.
  - Keep all-in TEG within the cap.
  - File data-protection authorisations before launch.
  - Avoid any crypto or stablecoin rails; the BCRG and BCEAO are hostile.

### Gaps
- No sourced estimates of legal or advisory fees, BCEAO processing statistics, or bank BaaS pricing.
- Not confirmed whether a single holding can obtain SFD licences in several WAEMU states, or how long CEMAC licences take in practice.
