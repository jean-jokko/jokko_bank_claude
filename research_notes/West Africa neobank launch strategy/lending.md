# Digital Lending in Francophone West & Central Africa (WAEMU / CEMAC) — Launch Notes for Jokko (as of October 2026)

Conventions: 1 EUR = 655.957 FCFA (fixed peg; XOF and XAF at par). "Flash loans" = instant, very short-term nano-loans/overdrafts (not crypto). Research date: 8 Oct 2026. Items marked **[UNVERIFIED]** or **[DATED]** should be re-checked before use.

---

## 1. Legal: who may lend, usury caps, TEG treatment, disclosure, and lending-as-a-service partnerships

### Takeaway
In WAEMU only licensed credit institutions (banks, financial credit institutions) and SFDs/microfinance institutions may lend. Since 1 June 2026 the all-in cost cap (TEG/TAEG, fees and insurance included) is **14%/yr for banks** and **24%/yr for SFDs and financial credit institutions**. E-money issuers (EMEs) cannot lend on their own account. They can only distribute a bank's or SFD's credit. In CEMAC, lenders are banks and COBAC-licensed EMFs (3 categories). The BEAC's monetary policy committee (CPM) sets the usury rate quarterly by country. The TEG caps are the single biggest constraint on nano-loan economics.

### Cited Findings
**WAEMU usury / TEG**
- Decision n°19/29-12-2025/CM/UMOA (signed Cotonou, 29 Dec 2025) cut the bank usury rate from 15% to **14%**. It kept **24%** for financial credit institutions ("établissements financiers de crédit") and SFDs. It applies **from 1 June 2026**. The UEMOA Council of Ministers alone sets the rate. The BCEAO and Commission bancaire enforce it — [Financial Afrik, 27 Jul 2026](https://www.financialafrik.com/2026/07/27/taux-dusure-dans-luemoa-le-recalibrage-opere-par-la-decision-n19-29-12-2025-cm-umoa/); [BCEAO decision PDF](https://www.bceao.int/sites/default/files/2026-01/Decision-No19-du-29-12-2025_CMUMOA_fixant_le_taux_de_l-usure.pdf); [BCEAO Avis n°007-12-2025](https://www.bceao.int/fr/reglementations/avis-no007-12-2025-aux-etablissements-de-credit-et-aux-institutions-de)
- The cap applies to the **TEG/TAEG**, which includes "l'ensemble des frais, commissions et primes d'assurance liés à l'octroi du crédit". Any credit above the cap is usurious, whatever the contract type or borrower type. Sanctions: a fine, and for repeat offences imprisonment and possible closure. Civil: the clause or the whole contract can be voided and excess amounts refunded. Prudential: Commission bancaire sanctions up to licence withdrawal. The column explicitly flags the risk of lenders circumventing the cap through "frais annexes non intégrés au TEG" — [Financial Afrik](https://www.financialafrik.com/2026/07/27/taux-dusure-dans-luemoa-le-recalibrage-opere-par-la-decision-n19-29-12-2025-cm-umoa/)
- Ecofin says the APR covers "total mandatory borrowing costs relative to the loan amount". It quotes a CI microfinance specialist: any loan above 24% "exposes the institution to direct sanctions from the WAEMU Banking Commission, regardless of management intent" — [Ecofin](https://www.ecofinagency.com/news-finances/3004-55154-bceao-loan-rate-caps-to-take-effect-across-waemu-on-june-1)
- **Conflict:** Ecofin says MFIs "previously used a 27% cap". Other sources say the 24% SFD rate dates from a 2013 Council of Ministers decision in force since 1 Jan 2014 (cap was 27% earlier) — [Ecofin](https://www.ecofinagency.com/news-finances/3004-55154-bceao-loan-rate-caps-to-take-effect-across-waemu-on-june-1) vs [BCEAO SFD usury page](https://www.bceao.int/fr/documents/taux-dusure-pour-les-operations-de-credit-des-sfd-dans-la-zone-umoa) / [droitmediasfinance](https://www.droitmediasfinance.com/index.php/actualites/droit-bancaire/1248-uemoa-credits-bancaires-le-taux-dusure-pour-les-banques-a-14-et-pour-les-etablissements-financiers-a-24-pour-a-partir-1er-juin-20266). Treat 24% (since 2014) as correct; 27% is the pre-2014 figure.
- Disclosure: an older note says the anti-usury law requires credit institutions to state the TEG in every loan contract. Côte d'Ivoire's consumer law (art. 146) reportedly requires consumer-credit advertising to state the TEG. There is no UMOA-wide cooling-off (rétractation) rule. Consumer financial protection is mostly national, and CI and Mali have specific consumer/mortgage credit regimes — [Financial Afrik 2019 (Sanou)](https://www.financialafrik.com/2019/03/12/protection-des-consommateurs-de-luemoa-les-initiatives-nationales/); [CMS on Burkina usury law](https://cms.law/fr/fra/a-la-une/burkina-faso-projets-de-lois-sur-l-usure-et-sur-l-interet-legal) **[DATED]**
- The BCEAO policy rate was held at 3.25% in Dec 2025 — [allAfrica, Dec 2025](https://fr.allafrica.com/stories/202512030599.html)

**WAEMU: who may lend; EME limits; partnerships**
- BCEAO Instruction n°008-05-2015 limits an EME to issuing and managing e-money. Credit from a bank or SFD to a client can be used to issue e-money (art. 5). This is the legal basis for bank/SFD-funded credit disbursed into wallets. A non-bank EME must keep its trust (fiduciary) account at a partner bank — [BCEAO EME page](https://www.bceao.int/fr/documents/etablissements-de-monnaie-electronique); [Instruction 008-05-2015](https://edenpub.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- BCEAO has sanctioned non-banks for doing bank-reserved activities (the Wari case) — [Osiris: BCEAO vs Orange / Wari](https://osiris.sn/BCEAO-vs-Orange-Lost-in-Fintech.html)
- Instruction 001-01-2024 on payment services covers banks, financial credit institutions, payment institutions, MFIs and EMEs. The compliance deadline was around May 2025 (sources differ; one says extended to 31 Aug 2025). Minimum capital ranges from 10m FCFA (€15.2k) for account aggregators to 100m FCFA (€152k) for wallet/transfer services. Unlicensed services were cut off — [Launch Base Africa](https://launchbaseafrica.com/2025/05/02/millions-locked-out-as-west-african-central-bank-blocks-unlicensed-fintechs/?amp=1); [droitmediasfinance](https://droitmediasfinance.com/index.php/actualites/droit-tech-fintech/956-uemoa-services-de-paiement-la-bceao-proroge-la-periode-de-mise-en-conformite-a-mai-2025)
- In Aug 2026 the BCEAO was debating how to supervise telcos and fintechs that want to take deposits and lend on their own account. Options: (1) same activity, same rules (banking licence); (2) a new "digital bank" category with bank-aligned ratios; (3) separating payment, credit and insurance. No decision has been reported. Senegal e-money outstanding was 571bn FCFA (€870m) on 21 Aug 2026: Wave 459bn (€700m), Orange Money 106bn (€162m) — [Senego, 31 Aug 2026](https://senego.com/bceao-telecoms-et-fintechs-avancent-vers-le-credit-le-cadre-prudentiel-en-debat_1998398.html)
- **Licensing precedents for a fintech:**
  - Orange Bank Africa (Orange 85% / NSIA 15%) is a full bank — "first digital bank approved by BCEAO" — [CIO Mag](https://cio-mag.com/orange-bank-africa-revele-les-coulisses-qui-simplifient-lacces-au-microcredit-tik-tak-depuis-5-ans/); [Ecofin](https://www.ecofinagency.com/news-finances/0302-52548-ifc-to-provide-30-6m-guarantee-for-orange-bank-digital-lending-in-cote-d-ivoire-senegal)
  - Djamo obtained a **microfinance (SFD) licence** for Djamo Finances SA. Côte d'Ivoire's Ministry of Finance granted it, with a favourable BCEAO opinion, on 15 Sep 2025. The process took **~3 years**. It is described as the first fintech microfinance licence in the region and enables "instant credit" — [The Condia](https://thecondia.com/djamo-first-microfinance-central-bank-bceao/); [IT Edge](https://www.itedgenews.africa/djamo-gets-regulatory-nod-to-pioneer-digital-microfinance-in-francophone-africa/)
- **Distribution partnerships (examples):**
  - Orange Money + Baobab "M-Baobab" (Senegal, Mar 2022): instant loan up to 500,000 FCFA (€762) and savings at 6% — [Seneweb](https://seneweb.com/fr/news/61/offre-de-credit-et-d-epargne-100-digitale-orange-finances-mobiles-senegal-et-baobab-lancent-m-baobab_n_374618.html) **[DATED]**
  - Orange + Jumo microcredit on Orange Money — [developingtelecoms](https://developingtelecoms.com/telecom-technology/financial-services/18840-orange-money-expands-micro-loan-services.html) **[DATED]**
  - Orange Money/Orange Bank + fintech Ezra (CI) — [FinDev Gateway](https://www.findevgateway.org/fr/actualites/cote-divoire-orange-money-et-orange-bank-sallient-ezra-pour-developper-lacces-au-micro)
  - Orange + Yabx (tech) + Cofina (lender) smartphone financing in CI — [TechCabal](https://techcabal.com/?p=90142) (undated)
  - MTN: group model historically "intermediated partnerships with banks", plus some own-balance-sheet lending; MTN is exploring banking licences — [Ecomatin](https://ecomatin.net/services-financiers-mtn-veut-sa-propre-licence-bancaire-pour-booster-son-activite-de-credit)

**CEMAC**
- Regulation n°04/19/CEMAC/UMAC/CM (TEG, usury, publication of bank conditions; dated 10 Aug 2020 in the source). A loan is usurious if its TEG exceeds the rate set by the **BEAC CPM**, which sets usury rates **per member state**, quarterly (3-month validity, art. 17). National CNEFs compute average TEGs by loan category. For businesses, the cap is generally the prior-quarter national average TEG plus a margin set by the committee. Loans by other persons are subject to the same ceilings where risks are similar — [droitmediasfinance](https://droitmediasfinance.com/index.php/dmf-conseils/protection-du-consommateur-financier/1284-cemac-financement-par-credits-comment-se-determine-le-taux-dusure-en-zone-cemac)
- The BEAC treats the TEG as the real overall cost: all tax-inclusive charges, insurance, fees and commissions. The nominal rate averages ~73% of the TEG. Average TEG: Q1 2025 10.51%; Q2 2025 11.8%. The SME TEG jumped from 11.4% to 23.3% in Q2 2025. Gabon is highest at 24.8% and Cameroon 7.9% — [French Treasury note](https://www.tresor.economie.gouv.fr/Articles/0b783e57-3419-466f-9c5c-e802bad51ca9/files/167120a5-e6ff-44a9-9179-b6b33eb1104b); [Ecomatin](https://ecomatin.net/cemac-les-taux-bancaires-setablissent-entre-8-et-15-au-premier-trimestre-2025); BEAC TEG rules: [Instruction du Gouverneur n°004/2021](https://www.beac.int/wp-content/uploads/2021/12/Instruction-du-Gouverneur-N°004-2021_compressed.pdf)
- BEAC policy rate (TIAO): raised to 4.75% in Dec 2025, then cut back to 4.50% in Jun 2026. Marginal lending facility: 6.25%, then 5.75% — [Tchadinfos, 29 Jun 2026](https://tchadinfos.com/2026/06/29/la-beac-baisse-ses-taux-dinteret/)
- **EMF categories:** Regulation R-01/17/CEMAC/UMAC/COBAC (27 Sep 2017) and COBAC EMF R-2017/03:
  - **Cat. 1:** cooperatives lending only to members. No minimum capital; must join a network.
  - **Cat. 2:** SA that collects savings and lends to third parties. Minimum capital **300m FCFA (€457k)** since 1 Jan 2021.
  - **Cat. 3:** SA that lends to third parties **without collecting savings**. Minimum capital **150m FCFA (€229k)**.
  - Source: [Kalieu-Elongo](https://kalieu-elongo.com/exercice-et-controle-de-lactivite-de-microfinance-en-afrique-centrale-le-cadre-reglementaire-revu-et-corrige/); [CEMAC Reg 2017-01 text](https://www.sgg.cg/txts-droit-reg/cemac-reglement-2017-01-exercice-controle-microfinance.pdf); [Financial Afrik 2021](https://financialafrik.com/2021/04/12/cameroun-les-etablissements-de-microfinance-sommes-de-se-conformer-au-nouveau-dispositif-prudentiel-de-la-cobac)
- COBAC is moving bank minimum capital toward 25bn FCFA (€38.1m) under R-2025/02. This raises the barrier to a CEMAC bank licence — [Ecomatin](https://ecomatin.net/cemac-4-points-pour-comprendre-pourquoi-la-cobac-veut-fixer-a-25-milliards-fcfa-le-capital-minimum-des-banques); [Financial Afrik Dec 2025](https://www.financialafrik.com/2025/12/29/le-relevement-du-capital-bancaire-en-cemac-un-risque-majeur-de-consolidation/)
- Cameroon gave fintechs a 3-month ultimatum to license or stop (2025) — [Launch Base Africa](https://launchbaseafrica.com/2025/05/16/cameroons-fintech-ultimatum-three-months-to-license-or-cease-operations/?amp=1)

### Inferences
- **Usury arithmetic is decisive.** Under a 24% all-in TEG, the most an SFD can charge is about **1.97% for a 30-day loan** and about **0.46% for a 7-day loan**. A bank at 14% gets about 1.15% for 30 days. On a 25,000 FCFA (€38) 30-day loan, the SFD maximum is about 490 FCFA (€0.75) in all interest *and fees*. That does not cover typical digital credit losses of several percent per cycle, plus acquisition, disbursement and collection costs.
- So a pure "flash" nano-loan with flat 5–15% fees, the East African model, is very hard to run legally in WAEMU. Reported offers like MoMoKash's 9–14% fees for 7–30 days (Benin, section 3) look hard to reconcile with a 24% TEG cap. How operators legally structure this (fee categorisation, lender of record, etc.) could not be confirmed. Jokko should get a formal legal opinion and should **not** copy competitor fee grids.
- Jokko's most realistic WAEMU paths:
  - (a) **Distribution/agency model:** Jokko as EME or payment institution plus a partner bank/SFD as lender of record, with risk-sharing.
  - (b) **Own SFD licence** in one country (the Djamo route, which took ~3 years).
  - (c) **Bank licence**, which is the most capital-intensive.

  The partner's licence category sets the cap: 14% for a bank, 24% for an SFD. Partnering with an **SFD or financial credit institution** rather than a bank gives 10 points more pricing headroom.
- In CEMAC, a **Category 3 EMF** (credit without deposit-taking, 150m FCFA / €229k capital) is the lightest licensed route for a pure lender. Usury caps there are country-specific and quarterly, so pricing engines must be parameterised by country and quarter.
- The open BCEAO debate (Aug 2026) creates regulatory risk for EMEs that drift into lending. Partnership structures should keep the regulated lender clearly the lender of record: credit decision ownership, balance sheet, contract and TEG disclosure.

### Gaps
- The full text of WAEMU consumer credit disclosure rules (pre-contract information, cooling-off) by country; only CI art. 146 was found.
- No source confirms whether BCEAO counts mobile-money disbursement/withdrawal fees or "service fees" charged by a distributing EME in the lender's TEG. This is critical for pricing and needs counsel.
- Current CEMAC usury rate values by country and category (Q3/Q4 2026) were not retrieved. Check the BEAC CPM communiqués.
- No BCEAO text explicitly naming "loan distribution by EMEs" as permitted or prohibited was found. The legal basis is inferred from Instruction 008-05-2015 art. 5 and the EME activity limitation.
- Whether WAEMU's 2024 payment-services instruction replaced Instruction 008-05-2015 provisions was not verified.

---

## 2. Credit bureaus and alternative data

### Takeaway
WAEMU has a functioning regional credit bureau (BIC, operated by **Creditinfo West Africa**, ex-Creditinfo VoLo). It holds 40m+ contracts on 18m individuals from 318 institutions. Coverage is regulated lenders, and there is no evidence that mobile money transaction data feeds it. CEMAC's first private bureau, **Creditinfo Central Africa (CICA)**, was licensed in Nov 2025 and launched in Jan 2026; it is still rolling out by country. Alternative data (wallet flows, payroll, telco) remains in the hands of each lender or its partners.

### Cited Findings
- BIC-UEMOA at 30 Jun 2025 (7th annual meeting, Cotonou, Oct 2025): >40m credit contracts, **18m individuals**, 385,000 companies, **318 active financial institutions**, >1.3m report consultations. Clients with good Creditinfo scores were 10x more likely to be good payers. Alternative data and AI are discussed only as future directions — [droitmediasfinance](https://droitmediasfinance.com/index.php/actualites/droit-bancaire/1123-uemoa-bureau-dinformation-sur-le-credit-bilan-dune-decennie-de-transformation-et-perspectives-a-lere-du-digital)
- The BIC covers all 8 UMOA countries under the "Creditinfo West Africa" brand. BIC data can come from financial institutions, public sources and large billers (utilities, mobile telephony), but no source confirms that mobile money transactions are reported — [BCEAO BIC promotion page](https://www.bceao.int/fr/content/promotion-des-bureaux-dinformation-sur-le-credit-dans-lumoa); [Creditinfo Chronicle](https://chronicle.creditinfo.com/tag/volo)
- The BCEAO's PI-SPI instant payment platform launched in Sep 2025. It is expected to generate transaction data usable for scoring, including for mobile money users — [droitmediasfinance](https://droitmediasfinance.com/index.php/actualites/droit-bancaire/1123-uemoa-bureau-dinformation-sur-le-credit-bilan-dune-decennie-de-transformation-et-perspectives-a-lere-du-digital)
- Total e-money outstanding in the UEMOA was 1,923.2bn FCFA (€2.93bn) at end-2025, up 35.2% from 1,422.6bn — [Le Soleil](https://lesoleil.sn/actualites/economie/uemoa-le-senegal-en-tete-sur-la-microfinance-et-la-monnaie-electronique-en-2025/)
- **CEMAC:**
  - BEAC Governor Decision n°142 of 25 Nov 2025 licensed **Creditinfo Central Africa SA (CICA)**, based in Douala, as the CEMAC credit information bureau.
  - It was launched with IFC on **20 Jan 2026** and is rolling out progressively: Cameroon, CAR, Chad, then Congo; Gabon launch on 15 Jul (year not stated).
  - The framework requires supervised institutions to share data, with consumer consent and data protection.
  - Sources: [IFC press release](https://www.ifc.org/fr/pressroom/2026/la-beac-et-la-soci-t-financi-re-internationale-ifc-lancent-officiellement-le-burea0); [Business in Cameroon](https://www.businessincameroon.com/finance/2101-15630-cemac-credit-bureau-goes-live-aiming-to-cut-risk-and-expand-affordable-lending); [droitmediasfinance](https://droitmediasfinance.com/index.php/1317-congo-le-bureau-dinformation-sur-le-credit-sinstalle-a-brazzaville-et-signe-des-accords-avec-les-etablissements-de-credit); [Gabonreview](https://www.gabonreview.com/transformer-linformation-en-confiance-creditinfo-central-africa-demarre-ses-activites-au-gabon/)
- Orange's Tik Tak relies on customer knowledge, data mining and scoring. At launch (2020), an unpaid loan after 30 days led to the Orange Money account being blocked and wallet funds being recovered automatically. A shared bad-payer blacklist with other MNOs was planned — [Osiris / 2020](https://osiris.sn/orange-est-devenu-une-banque-africaine-credit-epargne-carte-bancaire.html) **[DATED]**
- MTN's MoMoKash (CI) uses "alternative credit scoring models and affordability controls", built in-house by MTN teams (product, data science, risk, compliance) — [MTN case study, 28 Apr 2026](https://www.mtn.com/case-study/unlocking-digital-credit-through-mobile-money/)

### Inferences
- Jokko should join the BIC through its regulated lending partner, or directly if it licenses as an SFD. Every loan should be reported so that Jokko borrowers build bureau history. This is also a selling point to customers ("build your credit score").
- Jokko's real scoring edge will be **first-party data**: salary credits into Jokko accounts, wallet inflows, bill payments, savings behaviour, and PI-SPI transfers. Bureau data mainly serves as a negative check: existing debt, defaults at MFIs.
- Wallet auto-debit ("sweep") is a key collections tool that MNO lenders already use. Jokko gets the same lever only for funds held in Jokko accounts, which argues for salary-domiciliation features first.

### Gaps
- Whether EMEs or fintech distributors can consult the BIC directly, and the cost per enquiry, were not found.
- Whether any MNO reports nano-loan repayment data to the BIC was not found.
- Data-protection consent requirements for using telco/MNO data in scoring (national data protection authorities: CDP Senegal, ARTCI CI) were not researched.

---

## 3. Existing digital lending players and their terms

### Takeaway
The market is led by **MNO-linked lenders**: Orange Bank Africa's **Tik Tak** (CI, Senegal, Guinea), with 500bn+ FCFA disbursed in 5 years, and MTN **MoMoKash**. Microfinance groups are digitising: Baobab nano-loans, Cofina. **Djamo** has just obtained a microfinance licence to lend. **Wave** has announced but not launched credit. Salary advance and BNPL are nascent and fragmented. Terms are rarely published, and default data is almost never disclosed.

### Cited Findings
**Orange Bank Africa / Tik Tak**
- Five-year milestone (Jul 2025): **>500bn FCFA (€762m) disbursed** to ~**2 million** customers. 51% of customers are outside the capital. Active in CI, Senegal and Guinea. Women repay "slightly better" than men (no rates given) — [CIO Mag, 24 Jul 2025](https://cio-mag.com/orange-bank-africa-revele-les-coulisses-qui-simplifient-lacces-au-microcredit-tik-tak-depuis-5-ans/)
- A Jun 2025 report gave >450bn FCFA (€686m) to >1.9m Orange Money clients since 2020, a different and unreconciled figure. Orange's 2024 CSR report: **340,000** Tik Tak users in 2024. Standard loans run **5,000–50,000 FCFA (€7.6–€76)**, with higher ceilings for premium tiers — [WeAreTech](https://www.wearetech.africa/fr/fils/actualites/340-000-personnes-ont-utilise-le-service-de-pret-financier-tik-tak-d-orange-en-2024); [allAfrica Jun 2025](https://fr.allafrica.com/stories/202506180164.html)
- OBA 2024 figures (early 2025 event): deposits 301.9bn FCFA (€460m), "credits realised" 359.6bn FCFA (€548m), 1,571,026 clients across CI, SN and GN. The article has internal inconsistencies — [Digitalmag via search](https://digitalmag.ci/?p=28178) **[UNVERIFIED]**
- Loans are short-term, repayable over 1–3 months — [developingtelecoms](https://developingtelecoms.com/telecom-technology/financial-services/18840-orange-money-expands-micro-loan-services.html)
- **IFC support:**
  - 2022: advisory work on digital credit for MoMo agents and merchants.
  - 2023: risk-sharing facility covering **50%** of a short-term loan portfolio up to US$30m equivalent, with IDA PSW first-loss support; target ~300,000 additional loans by 2025.
  - **Feb 2026:** new **17bn FCFA (€25.9m, ~US$30.6m) guarantee** covering up to 50% of a working-capital portfolio of up to **US$60m** via Tik Tak. It targets SMEs (trade, services, women-owned) in CI and Senegal. ~3m Orange Money customers have signed up to Tik Tak.
  - Sources: [Ecofin, 3 Feb 2026](https://www.ecofinagency.com/news-finances/0302-52548-ifc-to-provide-30-6m-guarantee-for-orange-bank-digital-lending-in-cote-d-ivoire-senegal); [IFC 2023](https://ifc.org/en/pressroom/2023/ifc-partners-with-orange-bank-africa-to-increase-digital-lending-for-small-businesses-in-west-africa)
- Tik Tak pricing and NPL are **not publicly disclosed** in any source found.

**MTN MoMoKash**
- MTN Benin FAQ (Apr 2026): terms of 7, 14 or 30 days; **fees 9%–14%** depending on term, MoMo usage and repayment record; one active loan at a time — [MTN Benin FAQ](https://www.mtn.bj/wp-content/uploads/2026/04/FAQ-MOMOKASH.pdf). A consumer site claims 2,000–100,000 FCFA at 2% for 30 days. It is low reliability and the country is unclear.
- MTN CI case study (Apr 2026): MoMoKash built in-house, with alternative scoring. No volumes, pricing or NPL disclosed — [MTN](https://www.mtn.com/case-study/unlocking-digital-credit-through-mobile-money/)
- MTN Cameroon: MoMoKash savings/microcredit was being finalised in 2020 with MTN as intermediary to financial institutions. No 2025 product data was found — [NextBillion](https://nextbillion.net/news/mtn-cameroon-to-soon-offer-mobile-savings-and-loans-services) **[DATED]**

**Djamo (CI, Senegal)**
- Over 1m customers. It raised a US$14m Series A (2022) and US$17m (Apr 2025). The SFD licence (Sep 2025) enables "instant, clear, and responsible credit" with a gradual rollout. Credit/SME is led by Nicolas Berthozat, an ex-FairMoney co-founder. Only 5–10% of users receive their salary through Djamo; the target is 50% — [The Condia](https://thecondia.com/djamo-first-microfinance-central-bank-bceao/); [Launch Base Africa](https://launchbaseafrica.com/2025/02/20/ivorian-fintech-startup-djamo-lands-funding-from-state-owned-investment-fund-post-series-b/)
- No source found describes a Djamo "avance sur salaire" product or its pricing.

**Wave**
- Credit, savings and insurance are "in preparation" (Feb 2026; Wave Digital Finance MD El Hadji Malick Gueye). No launch date. Wave launched a virtual Visa card with Ecobank Senegal in Jan 2026. It raised US$137m in debt in 2025 (RMB-led), which is corporate funding, not consumer credit — [Ndarinfo](https://www.ndarinfo.com/Wave-38-millions-de-comptes-credit-epargne-et-assurance-en-preparation_a42954.html); [Financial Afrik](https://www.financialafrik.com/2026/01/24/senegal-wave-lance-une-carte-virtuelle-avec-visa-et-ecobank/)

**Baobab (microfinance group)**
- End-2025: loan portfolio **€963m (~631.7bn FCFA)**, **PAR30 2.06%** (2.63% in Oct 2024), 1.66m total clients, average loan €3,079. Digital nano-loans are listed as a product — [Baobab press kit 2026](https://baobab.com/wp-content/uploads/2026/08/Kit-Presse_2026_800x600_FR.pdf)
- About 50% of loans are reportedly disbursed digitally, per CB Insights. **[UNVERIFIED]**
- IFC is preparing up to **68bn FCFA (€103.7m)** of support backed by a US$120m guarantee for six subsidiaries — [Ecomatin](https://ecomatin.net/lifc-prepare-un-appui-de-68-milliards-fcfa-au-groupe-de-microfinance-baobab-pour-doper-le-credit-aux-pme)
- Beltone (Egypt) acquired 100% of Baobab for €197.6m, closing Feb 2026 — CB Insights **[UNVERIFIED]**

**Moov Africa**
- Bank-wallet and ATM partnerships only (Banque Atlantique, Ecobank). No Moov nano-loan in West Africa was found — [Digitalmag](https://digitalmag.ci/fintech-la-banque-atlantique-sassocie-avec-moov-africa-pour-renforcer-linclusion-financiere/); [Osiris](https://osiris.sn/togo-moov-et-ecobank-lancent-move-money-gab-pour-faciliter-les-retraits-d.html)

**Salary advance players (francophone)**
- **Fintra** (Orya Technologies, Dakar; pilot Sep 2022): up to **20% of salary at 6%** if repaid within 15 days, paid into Orange Money, Wave or Free Money within an hour, public and private employers — [WeAreTech](https://www.wearetech.africa/fr/fils/solutions/avec-fintra-les-salaries-senegalais-peuvent-obtenir-des-prets-a-de-faibles-taux) **[DATED]**
- **MoneyVerse** (DRC): integrates with HR and payroll; MoneyVerse funds and carries the risk — [WeAreTech](https://www.wearetech.africa/fr/fils/solutions/rdc-moneyverse-facilite-l-acces-aux-avances-sur-salaire)
- **WAGIS** (Burkina Faso) — [Osiris](https://www.osiris.sn/a-21-ans-un-etudiant-du-cesag-veut-revolutionner-l-acces-au-salaire-en-afrique.html)

**BNPL / layaway**
- **Molo Molo Pay** (CI, founded 2021): pay-little-by-little for phones, motorbikes and appliances. It is closer to **layaway** (save first, collect the item at target) and partners with appliance distributor Sociam. 250,000+ users (date unclear) — [APA News](https://fr.apanews.net/cote-divoire/rci-une-application-de-paiement-echelonne-lancee/)
- BNPL is about 1% of CI e-commerce payment methods; mobile money and wallets dominate — [dodopayments](https://dodopayments.com/payments-in/cote-divoire) (low-authority source)

**Names in the brief not verified**
- Kredika, Fiko, Paps, Kix, Kitch, Tranzak, Payline, Yako Africa, Coris Money loans, Julaya credit, Société Générale "Mon salaire": not searched or not found in this pass. Treat as **[UNVERIFIED]**.
- Wari is better known for its BCEAO dispute than for lending — [Osiris](https://osiris.sn/BCEAO-vs-Orange-Lost-in-Fintech.html)

### Inferences
- Tik Tak shows the scale available: about €762m disbursed over 5 years, roughly €150m a year. Its average ticket is very small (5,000–50,000 FCFA), and OBA needed IFC 50% risk-sharing to expand into SME working capital. This suggests even a well-capitalised MNO bank wants credit enhancement for unsecured digital loans in WAEMU.
- Djamo, the closest comparable to Jokko, chose its **own SFD licence** (24% cap) over relying permanently on a partner. That took 3 years, so Jokko needs a partner model in the interim.
- Wave entering credit is the main competitive threat in Senegal and CI. Its 459bn FCFA float in Senegal alone gives it unmatched cash-flow data. Jokko should differentiate on salaried and payroll-linked customers rather than on mass nano-loans.

### Gaps
- No published Tik Tak or MoMoKash pricing (TEG) or NPL/PAR figures for WAEMU.
- No 2025–26 data on Fintra, Molo Molo Pay, or a Cofina/Yabx smartphone programme.
- No verified BNPL player with a real deferred-payment (credit) model in WAEMU/CEMAC.
- Coris Money, Ecobank, Société Générale and NSIA digital salary loans not researched.

---

## 4. Lessons from Kenya and Nigeria (Fuliza, M-Shwari, Tala, Branch, FairMoney; regulatory crackdowns)

### Takeaway
East Africa shows overdraft-style nano-credit can reach huge scale: Fuliza disbursed KES 1.47tn in FY to Mar 2026. It also shows very high default on the smallest tickets, borrower over-indebtedness, and eventual regulation: Kenya's CBK DCP licensing (252 licensed of 800+ applicants) and Nigeria's FCCPC DEON regulations (2025). Key lessons: build in disclosure, minimum ticket sizes, cooling limits, ethical collections and data-privacy compliance from day one.

### Cited Findings
**Fuliza (Safaricom M-Pesa overdraft; NCBA/KCB-funded)**
- FY to Mar 2026: disbursements **+49% to KES 1.47tn**, revenue **+46% to KES 6bn**, 17.7m customers, average loan ~KES 218 — [Capital FM, May 2026](https://www.capitalfm.co.ke/business/2026/05/fuliza-loans-jump-49pc-to-sh1-47tn/)
- FY to Mar 2025: KES 986.1bn disbursed, KES 4.1bn revenue, 7.9m customers — [Mwango Capital](https://mwangocapital.substack.com/p/12-05-2025-safaricom-holds-dividend-for-third)
- H1 FY26 (to Sep 2025): KES 629.2bn borrowed, 9.1m active users. Fuliza is 59% of Safaricom credit revenue — [Business Daily](https://www.businessdailyafrica.com/bd/markets/kenyans-borrow-sh629bn-from-fuliza-as-digital-overdraft-gains-5256022)
- Inference from these numbers: Safaricom's revenue is roughly **0.4% of disbursed volume**, because loans are tiny and revolve within days. Most of the economics sit with the funding banks and in daily fees.

**M-Shwari**
- 7.5% one-off "facilitation fee" (not "interest") per 30-day loan, equivalent to ~91% annualised. A 20% excise duty applies to fees since FY2021/22. Minimum loan raised to KES 2,000, with smaller loans moved to Fuliza to cut defaults. 2024 disbursements KES 98bn (−3.5%) — [Business Daily](https://www.businessdailyafrica.com/bd/corporate/companies/m-shwari-loan-charge-not-interest-cba-tells-customers-2126276); [Business Daily: shifts <2,000 to Fuliza](https://www.businessdailyafrica.com/bd/markets/capital-markets/m-shwari-shifts-loans-of-below-sh2-000-to-fuliza-2298316); [NCBA excise FAQ](https://ke.ncbagroup.com/wp-content/uploads/2024/02/CHANGE-OF-EXCISE-DUTY-COLLECTION-PROCESS-FAQs.pdf); [Daba Finance](https://dabafinance.com/en/news/ncba-disburses-7-7b-in-loans-as-mobile-credit-becomes-lifeline)
- NCBA wrote off KES 11bn of Fuliza/M-Shwari loans. In 2022 it offered 50% forgiveness under a CBK-guided credit repair framework — [Business Daily](https://www.businessdailyafrica.com/bd/markets/capital-markets/ncba-writes-off-sh11bn-digital-loans--4032320); [Citizen](https://www.citizen.digital/business/ncba-to-forgive-ksh55-billion-fuliza-m-shwari-defaulted-loans-n309979)

**Tala / Branch**
- Historically ~15% per month (~180% a year) on 1-month loans. Tala reports risk-based 0.3–0.6% per day — [Business Daily "most expensive mobile loans"](https://www.businessdailyafrica.com/bd/news/revealed-kenya-s-most-expensive-mobile-loans-2264368) **[DATED]**

**Default rates (Kenya / Tanzania)**
- CBK data: **83.1% default on digital loans < KES 1,000**, 69.4% for KES 1,000–5,000, and 16.4% NPL for KES 50,001–100,000. DCP rules bar CRB listing of defaulters under KES 1,000, which may encourage non-repayment — [Business Daily](https://www.businessdailyafrica.com/bd/economy/borrowers-fail-to-repay-83pc-of-digital-loans-below-sh1000-5189888)
- Bank digital loan NPLs averaged 21% (2015–18), versus 10.2% across the banking industry — [Business Daily](https://www.businessdailyafrica.com/bd/news/borrowers-in-default-on-21pc-of-mobile-bank-loans-2264724)
- CGAP surveys: 12% (Kenya) and 31% (Tanzania) of borrowers self-report default. In Tanzanian data, 17% of loans were in default. 16% of Kenyan digital borrowers borrowed to repay another loan — [CGAP](https://cgap.org/node/3401)
- Industry-wide Kenya bank NPL was 15.3% (May 2026) — [paybillke / CBK figures](https://paybillke.com/guides/kenya-borrowing-2026-bank-results-loan-stats) (secondary)

**Kenya regulation**
- CBK Digital Credit Providers Regulations 2022. Licensed DCPs: 126 (Jun 2025), 153 (Sep 2025), 195 (Dec 2025), **252 (Jul 2026)** from **800+ applications** since Mar 2022. Review covers business models, consumer protection, and fit-and-proper owners. Disclosure of fees is required, but not a standardised APR — [CBK press release](https://centralbank.go.ke/uploads/press_releases/711656549_Press%20Release%20-%20Licensing%20of%2027%20Additional%20Digital%20Credit%20Providers.pdf); [Kenyans.co.ke](https://www.kenyans.co.ke/news/119442-cbk-approves-42-new-digital-lenders-bringing-total-195); [People Daily](https://peopledaily.digital/business/cbk-licenses-25-more-digital-lenders-as-applications-top-800-since-2022)

**Nigeria FCCPC DEON Regulations 2025**
- In effect from 21 Jul 2025. They cover all unsecured digital consumer lending, including MMOs. Lenders had to register within 90 days.
- Penalties up to **₦100m or 1% of turnover**, plus director disqualification up to 5 years.
- **Prohibitions:** pre-authorised or automatic lending and unethical marketing. Lender partnerships must be registered jointly.
- No numeric rate cap, but the FCCPC monitors rates and requires transparent pricing.
- Sources: [FCCPC press release](https://www.fccpc.gov.ng/media/press-releases/digital-lending-fccpc-tackles-abuses-issues-landmark-regulations/); [DEON text](https://a.storyblok.com/f/302089/x/ae54c51861/federal-competition-and-consumer-protection-commission-digital-electronic-online-or-non-traditional-consumer-lending-regulations.pdf); [Afriwise](https://www.afriwise.com/blog/predatory-lending-and-unfair-pricing-practices-understanding-the-legal-limits-of-digital-loan-pricing-in-nigeria)

**FairMoney (Nigeria MFB)**
- 2024 revenue **₦121.9bn (+62%)**. Impairments **+30% to ₦59.4bn**, with a policy of provisioning from disbursement. Deposits fund 56% of the loan book per TechCabal (Tekedia says >80%). Figures are unaudited and conflict between sources. GCR rating BBB+(NG) — [TechCabal](https://techcabal.com/2025/04/10/fairmoney-2024-revenue/); [Tekedia](https://www.tekedia.com/fairmoney-revenue-surges-to-n121-9-billion-in-2024-amid-shift-to-customer-deposit-funded-lending/)

### Inferences
- **Lessons for Jokko:**
  1. Sub-€5 tickets default massively. Set a minimum ticket and grow limits gradually.
  2. Never auto-disburse or pre-authorise credit (now illegal in Nigeria and a reputational hazard everywhere).
  3. Show the full cost in FCFA *and* TEG before acceptance.
  4. Collections must not shame customers or contact their phone contacts (the core of the Nigerian crackdown).
  5. Expect regulators to eventually license digital lenders specifically. Building to the Kenya/Nigeria standard now future-proofs Jokko.
- The FairMoney trajectory (credit-led, then deposits funding the book) is the template a neobank can follow. Deposits are the cheapest funding once licensed (the Djamo SFD route).
- East African pricing (7.5–15% per month) is **not transferable** to WAEMU, where the TEG cap is 24% a year. WAEMU digital lending has to work on lower losses (salary-linked, data-rich customers) and lower costs, not on high fees.

### Gaps
- Branch, Carbon, Moniepoint and Kuda overdraft economics were not researched in this pass.
- No current audited NPL for Tala, Branch or M-Shwari.
- The outcome of the FCCPC court case is unknown.

---

## 5. Funding the loan book; cost of funds; yields, default (PAR30), CAC/LTV

### Takeaway
WAEMU digital credit is funded mainly by:
- **Deposits** (bank or SFD licence);
- **DFI risk-sharing guarantees** (IFC 50% cover for OBA and Baobab);
- **Local bonds** and a fast-growing **FCTC securitisation** market (≈419bn FCFA issued in 2025).

FCFA funding costs sit around 6.8–7.5% for rated issuers, against a policy rate of 3.25% (BCEAO) or 4.5% (BEAC). Mature MFIs show PAR30 around 2%. Digital nano-loans elsewhere default at far higher rates.

### Cited Findings
- **IFC risk-sharing:** OBA 2023 (50% of up to US$30m) and Feb 2026 (17bn FCFA guarantee, 50% of up to US$60m) — [Ecofin](https://www.ecofinagency.com/news-finances/0302-52548-ifc-to-provide-30-6m-guarantee-for-orange-bank-digital-lending-in-cote-d-ivoire-senegal). Baobab: up to 68bn FCFA (€103.7m) with a US$120m guarantee across 6 subsidiaries — [Ecomatin](https://ecomatin.net/lifc-prepare-un-appui-de-68-milliards-fcfa-au-groupe-de-microfinance-baobab-pour-doper-le-credit-aux-pme)
- **IFC** has committed US$47.5m to women-focused microfinance in 6 African countries including Senegal — [Senego](https://senego.com/femmes-et-microfinance-lifc-injecte-475-millions-de-dollars-dans-6-pays-africains-dont-le-senegal_1576414.html)
- **Proparco:** first direct fintech investment was Jumo in 2018 (US$3m equity). It operates mainly through credit lines to financial institutions (over half its activity per the 2025 bilan). It has an Abidjan team and Digital Africa for seed-stage startups. No 2025–26 Proparco fintech lending line in West Africa was found — [Osiris](https://osiris.sn/proparco-lance-son-premier-projet-de-developpement-des-prets-digitaux-en.html); [Proparco bilan 2025](https://proparco.fr/sites/proparco/files/2026-06/bilan_proparco_2025_light.pdf); [Proparco Afrique 2025](https://proparco.fr/sites/proparco/files/2026-01/proparco-plaquette-afrique-fr-2025-v2-web.pdf)
- **Securitisation (FCTC):**
  - Legal basis: UEMOA Regulation n°02/2010/CM/UEMOA. The FCTC has no legal personality, is run by a licensed management company, buys receivables and issues notes.
  - 2025 FCTC issuance **418.9bn FCFA (€639m)**.
  - Apr–May 2026: >277bn FCFA (€422m) of bank, agricultural and energy FCTCs listed at **7–10%**.
  - BSIC FCTC: 45bn FCFA (€68.6m) at **7.25%** (Jun–Jul 2026). NSIA Banque Bénin "Keur Samba": 44bn FCFA (€67.1m) (Mar 2026). NSIA CI RMBS: 10bn FCFA (2025).
  - Sources: [droitmediasfinance](https://droitmediasfinance.com/index.php/actualites/finances/1254-uemoa-titrisation-des-creances-zoom-sur-la-premiere-cotation-de-5-fonds-communs-de-titrisation-bancaire-agricole-et-energie-remuneres-entre-7-et-10); [allAfrica BSIC](https://fr.allafrica.com/stories/202607030364.html); [Financial Afrik](https://www.financialafrik.com/2026/03/13/brvm-le-fctc-keur-samba-nsia-banque-benin-fait-son-entree-en-bourse-avec-44-milliards-fcfa); [APA BRVM 2025](https://fr.apanews.net/business/la-brvm-boucle-lannee-2025-avec-un-record-historique/)
- **Microfinance precedent:** Cofina's FCTC (Apr 2018) was 10bn FCFA (€15.2m), with an 18-month maturity at 7.50%, using receivables from its CI and Senegal subsidiaries and rated tAA by WARA — [Financial Afrik](https://www.financialafrik.com/2018/04/12/cofina-lance-sa-premiere-operation-de-titrisation-de-creances-pour-un-montant-de-10-milliards-de-francs-cfa) **[DATED]**
- **Bond precedent:** Baobab Senegal "GSS BAOBAB 6.80% 2024–2029" bond listed on BRVM on 25 Feb 2025 — [allAfrica](https://fr.allafrica.com/stories/202502190233.html)
- **Corporate debt:** Wave raised US$137m in debt (2025, RMB-led) and a €90m syndicated loan in 2022 — [Daba Finance](https://dabafinance.com/fr/nouvelles/Wave-l-ve-137-millions-de-dollars-de-dettes-pour-financer-son-expansion-en-Afrique-en-2025)
- **Policy rates:** BCEAO 3.25% (Dec 2025) — [allAfrica](https://fr.allafrica.com/stories/202512030599.html). BEAC 4.50% (Jun 2026) — [Tchadinfos](https://tchadinfos.com/2026/06/29/la-beac-baisse-ses-taux-dinteret/)
- **Portfolio quality:** Baobab group PAR30 **2.06%** (end-2025) — [Baobab](https://baobab.com/wp-content/uploads/2026/08/Kit-Presse_2026_800x600_FR.pdf). Kenya digital nano-loan defaults of 69–83% on tiny tickets, 16% on larger ones — [Business Daily](https://www.businessdailyafrica.com/bd/economy/borrowers-fail-to-repay-83pc-of-digital-loans-below-sh1000-5189888). FairMoney impairments ₦59.4bn on ₦121.9bn revenue — [TechCabal](https://techcabal.com/2025/04/10/fairmoney-2024-revenue/)

### Inferences
- **Indicative unit economics (inference, not sourced data)**, for an SFD-partnered 30-day salary advance at the 24% cap:
  - Gross yield is at most ~2% per cycle, roughly 24% a year if fully utilised.
  - Cost of funds is ~7–9% a year in FCFA (FCTC/bond benchmarks of 6.8–7.5% plus a spread for a smaller, unrated lender).
  - That leaves ~15–17 points a year for credit losses, operations and margin. It only works if annualised losses stay in **low single digits**, as in salary-linked lending with payroll deduction or MFI-quality books (PAR30 ~2%).
- For the same reason, unsecured nano-loans to unknown wallet users (East African default levels) cannot be profitable under WAEMU caps.
- Funding sequence:
  1. Partner SFD's or bank's balance sheet (zero Jokko capital at risk), with Jokko first-loss of 5–20% of the portfolio to align incentives.
  2. DFI risk-sharing (IFC/IDA PSW, as with OBA) once there is 12–18 months of performance data.
  3. A warehouse line from a local bank.
  4. Deposits, once Jokko holds an SFD or bank licence.
  5. FCTC securitisation once the book reaches ~10bn+ FCFA (€15m+). The precedent minimum is Cofina at 10bn FCFA.

### Gaps
- No public WAEMU-specific CAC/LTV data for digital lenders.
- No published cost of senior debt for unrated WAEMU fintechs.
- BII, FMO, AfDB and debt-fund facilities (e.g., Lendable, Verdant, MCE) for francophone digital lenders were not researched in this pass.
- No public PAR30 for any WAEMU digital-only portfolio (Tik Tak, MoMoKash).

---

## 6. Salary advance / earned wage access (EWA): payroll integration, domiciliation, collections

### Takeaway
Salary-linked credit is the lowest-risk entry point for a neobank in WAEMU. Collection can be via salary domiciliation (the salary is credited to the lender's account), a payroll deduction agreement with the employer, or both. Côte d'Ivoire's decree 2014-370 lets borrowers assign (cession) 35–57% of pay, depending on income, to loan repayments. The francophone EWA market is small and fragmented (Fintra, MoneyVerse, WAGIS), and none has reached scale.

### Cited Findings
- **Côte d'Ivoire Decree n°2014-370 (18 Jun 2014):**
  - The **quotité saisissable** (garnishable share) is capped at 33% of salary, allowances included.
  - The **quotité cessible** (voluntary assignment to a lender) went from 33% to a **sliding 35–57%** scale by income band, to expand borrowing capacity.
  - Base = gross monthly pay with allowances, minus mandatory withholdings, expense allowances, family supplements and non-garnishable allowances.
  - Consolidated text in force at 18 Jul 2023.
  - Sources: [CivLII decree](https://civlii.laws.africa/en/akn/ci/act/decree/2014/370/fra@2023-07-18/source); [Gouv.ci CCM 18 Jun 2014](https://www.gouv.ci/uploads/publications/1403123786CCM_du_18_06_2014_VCDEF.pdf); [Connection Ivoirienne](https://connectionivoirienne.net/2014/06/20/assouplissement-conditions-demprunt-bancaire-en-cote-divoire/)
- **Fintra (Senegal):**
  - Up to 20% of salary at 6% if repaid within 15 days, available from the 15th of the month and paid to a mobile wallet within an hour.
  - Employer-side automated management that doesn't touch company treasury. Public and private employers.
  - Target market: ~350,000 formal employees in Senegal. Banks charge up to 12% on overdrafts.
  - A former HR head noted that the employer is not obliged to accept a salary advance.
  - Source: [WeAreTech](https://www.wearetech.africa/fr/fils/solutions/avec-fintra-les-salaries-senegalais-peuvent-obtenir-des-prets-a-de-faibles-taux); [CIO Mag](https://cio-mag.com/au-senegal-une-startup-se-deploie-dans-lavance-sur-salaire/) **[DATED 2022]**
- **MoneyVerse (DRC):** HR/payroll integration; the fintech funds and carries risk — [WeAreTech](https://www.wearetech.africa/fr/fils/solutions/rdc-moneyverse-facilite-l-acces-aux-avances-sur-salaire)
- **Earnipay (Nigeria):** employers connect payroll; employees draw up to 50% of accrued pay any day, repaid from the next salary; **flat fee** (e.g., ~₦250 on ₦60,000) rather than interest. US$4m seed (Canaan); ~₦100m disbursed in 6 months (2022) — [TechCabal](https://techcabal.com/2023/04/18/earnipay-2-0-earnipay-expands-its-earned-wage-access-platform-to-offer-more-solutions-for-businesses/); [KnowESG](https://knowesg.com/social-governance/company-disburses-n100m-as-salary-advance-to-workers-in-6-months-24062022) **[DATED]**
- **Floatpays (South Africa):** grew from EWA into savings, pension-backed home loans and rewards. Payroll partners include Pepkor, YUM, TransUnion and Yoco — [BusinessDay SA, Apr 2025](https://www.businessday.co.za/bt/business-and-economy/2025-04-06-its-your-money-claim-it-now/)
- **Djamo:** 5–10% of users are paid into Djamo; target 50% — [Launch Base Africa](https://launchbaseafrica.com/2025/02/20/ivorian-fintech-startup-djamo-lands-funding-from-state-owned-investment-fund-post-series-b/)

### Inferences
- **The EWA model needs care under WAEMU law.** A flat fee on an advance of *earned* wages (Earnipay style) may arguably not be "credit" if the employer advances the money. Once a fintech or SFD funds it, it is credit and the 24% TEG cap applies. The fee calculation must include all charges.
  - Example: 6% for 15 days (Fintra) is about 146% annualised, which is clearly above the 24% cap if treated as credit.
  - Jokko needs a legal opinion on structure: employer-funded advance versus lender-funded credit.
- **Recommended mechanism:** a tripartite agreement (employer + Jokko + partner SFD) with:
  - (i) an irrevocable payroll deduction mandate within the quotité cessible;
  - (ii) salary domiciliation to a Jokko account, so the repayment is swept on salary credit;
  - (iii) an employer confirmation of employment status and salary;
  - (iv) caps of 30–50% of net salary earned to date.

  Losses should then be close to zero outside job loss and fraud.
- **Civil servants:** CI and Senegal civil servants are the most stable payroll segment. Payroll domiciliation at banks is the standard prerequisite for public-servant loans. Jokko would need accreditation with the Treasury/payroll systems (e.g., "domiciliation" agreements), which favours partnering with an existing bank or SFD that already has payroll codes.

### Gaps
- The Senegalese equivalent of the CI quotité cessible decree was not found.
- The process and requirements for a fintech or SFD to get payroll deduction codes for civil servants (CI Direction de la Solde; Senegal DSOLDE) were not found.
- No current (2025–26) data on Fintra's or other francophone EWA providers' volumes.
- Legal characterisation of EWA under the BCEAO SFD law was not found.

---

## 7. BNPL, e-commerce and device (phone) financing

### Takeaway
Formal BNPL is negligible in francophone Africa, at about 1% of CI e-commerce payment methods. The demand is for **layaway and device financing**: Molo Molo Pay, Baobab+ PayGo smartphones with Samsung Knox locking, and Orange + Yabx + Cofina. Jumia has *not* exited CI or Senegal; it left South Africa and Tunisia in late 2024. Device financing with remote locking is the strongest-collateral consumer product available.

### Cited Findings
- **Baobab+:** since Mar 2021, Samsung smartphones paid via mobile money over **3–6 months**, with **Knox** remote lock until fully paid. PAYG history is used as a credit history for further products. It has also licensed **PayJoy** Checkout/Lock technology. PAYG solar since 2015 in Senegal, CI, Mali and Madagascar. Norfund invested €10m — [Financial Afrik](https://www.financialafrik.com/2021/03/18/baobab-et-samsung-democratisent-lacces-aux-smartphones/); [CIO Mag](https://cio-mag.com/baobab-cote-divoire-le-smartphone-comme-porte-dentree-a-linclusion-financiere/); [Financial Afrik Norfund](https://www.financialafrik.com/2021/09/23/levee-de-10-millions-deuros-aupres-de-norfund-baobab-enracine-sa-position/) **[DATED]**
- **Orange CI + Yabx (tech/customer journey) + Cofina (lender):** smartphone instalment financing — [TechCabal](https://techcabal.com/?p=90142) (undated)
- **M-KOPA:** profitable (KES 1.2bn profit in 2024). Smartphones, solar and loans in Kenya, Uganda, Nigeria, South Africa and Ghana. **No confirmed francophone presence** — [allAfrica Oct 2025](https://fr.allafrica.com/stories/202510090535.html); [WeAreTech](https://www.wearetech.africa/fr/fils/breves/breves-simple/le-kenyan-m-kopa-realise-un-premier-benefice-de-9-2-millions)
- **Molo Molo Pay (CI):** layaway with appliance distributor Sociam; 250,000+ users — [APA News](https://fr.apanews.net/cote-divoire/rci-une-application-de-paiement-echelonne-lancee/)
- **Jumia** exited South Africa (Zando) and Tunisia at end-2024; those markets were 2.7% of orders and 3% of GMV. It went from 11 to 9 countries — [Jumia Group](https://group.jumia.com/news/african-online-retailer-jumia-to-exit-south-africa-and-tunisia); [TechPoint](https://techpoint.africa/news/jumia-to-exit-south-africa-tunisia/). No source found of a CI/Senegal exit.

### Inferences
- **BNPL at checkout** (merchant-subsidised, 0% to the consumer, 2–4 instalments) is attractive under the usury cap. If the merchant pays the discount, the consumer TEG can be 0%. Whether a merchant discount enters the TEG under BCEAO rules needs legal confirmation.
- Best initial partners: electronics and phone retailers and distributors (Sociam-type), device OEMs with lock tech (Samsung Knox, PayJoy), and MNO device programmes. Jokko should require device locking as collateral.

### Gaps
- Merchant discount rates, default rates and terms for device financing in WAEMU were not found.
- Current (2025–26) status of Baobab+ smartphones and the Orange/Yabx/Cofina programme is unknown.
- CEMAC BNPL players were not researched.

---

## 8. Islamic finance and insurance considerations

### Takeaway
The WAEMU has a dedicated framework for Islamic microfinance. BCEAO Instructions 003-03-2018 and 005-05-2018 allow SFDs to offer Murabaha, Ijara, Istisna, Salam (non-participative) and Mudaraba, Musharaka (participative) products, with internal Sharia compliance certification. In 2023 there were 18 authorisations, including 8 exclusively Islamic MFIs. A **Murabaha-based** salary advance or device financing is a credible differentiator for Senegal, Mali and Niger.

### Cited Findings
- BCEAO **Instruction n°005-05-2018** sets the technical characteristics of Islamic finance operations by SFDs. It builds on Instruction n°003-03-2018 on SFDs practising Islamic finance. All microfinance operations can be carried out if they comply with Islamic finance principles — [BCEAO Instruction 005-05-2018](https://bceao.int/sites/default/files/2018-05/Instruction%20005-05-2018%20Caract%C3%A9ristiques%20techniques%20op%C3%A9ratins%20FI%20par%20les%20SFD-web.pdf). One source cites a different reference number (002-03-2018).
- Contract types: Murabaha, Ijara, Istisna and Salam (non-participative), and Mudaraba and Musharaka (participative). Each must be certified by an internal compliance board (third-party summary) — [regalert](https://regalert.today/document/e7eef74c-8734-4828-945a-90f15b169482) **[verify against official text]**
- Senegal Law n°2019-06 (4 Feb 2019) amending the SFD law integrates Islamic finance into microfinance — [vie-publique.sn](https://www.vie-publique.sn/documents/5471/loi-n201906-du-04-fevrier-2019-modifiant-la-loi-n-2008-47-du-03-septembre-2008)
- **BCEAO 2023 annual report:** 18 authorisations (2 fully Islamic banks, 7 banks with Islamic windows, 8 fully Islamic MFIs, 1 MFI with a window). 3 Islamic MFI licences in 2023 (Burkina, Niger, Senegal). A Sharia governance guide and model contracts were adopted in May 2023. Senegal players: Banque Islamique du Sénégal, CBI Baraka (Coris), PAMECAS (DEFI department) — [droitmediasfinance](https://droitmediasfinance.com/index.php/actualites/droit-bancaire/855-uemoa-finance-islamique-la-bceao-denombre-18-autorisations-delivrees-aux-institutions-financieres-islamiques)
- **Insurance:** credit-life and other insurance premiums linked to granting credit are **included in the TEG** in WAEMU — [Financial Afrik](https://www.financialafrik.com/2026/07/27/taux-dusure-dans-luemoa-le-recalibrage-opere-par-la-decision-n19-29-12-2025-cm-umoa/). In CEMAC, the TEG likewise includes insurance — [French Treasury](https://www.tresor.economie.gouv.fr/Articles/0b783e57-3419-466f-9c5c-e802bad51ca9/files/167120a5-e6ff-44a9-9179-b6b33eb1104b)

### Inferences
- A Murabaha product (Jokko or its partner buys the good or service and resells it at a disclosed mark-up, paid in instalments) fits naturally with **device and merchant financing**. It can also structure salary-linked purchase financing. It probably requires partnering with one of the 8–9 licensed Islamic MFIs or Islamic bank windows, or building an Islamic window in Jokko's own future SFD.
- How the usury cap applies to a Murabaha mark-up is not confirmed in sources; assume the mark-up is treated as a cost of credit within the TEG.
- Credit-life insurance (death or disability cover on the outstanding balance) is standard and useful for salary loans. Because the premium counts in the TEG, it eats into the 24% headroom. Price it inside the cap or have the partner absorb it.

### Gaps
- No post-2023 count of Islamic finance authorisations.
- No examples of *digital* Murabaha nano-financing in WAEMU were found.
- CIMA-zone (insurance) rules for embedded credit insurance were not researched.
- Treatment of the Murabaha mark-up under usury rules is not confirmed.

---

## 9. Recommended lending product sequencing for Jokko (synthesis)

### Takeaway
Launch salary-linked credit first, through a partner SFD with Jokko first-loss. Then add merchant/device financing. Add a small revolving overdraft ("flash") only once there is salary-flow data. Pursue Jokko's own SFD licence in parallel (Djamo took about 3 years), and use DFI guarantees and later FCTC securitisation to scale.

### Cited Findings (anchors for the recommendation)
- Usury caps are 24% for SFDs and 14% for banks, all-in TEG, from 1 Jun 2026 — [Financial Afrik](https://www.financialafrik.com/2026/07/27/taux-dusure-dans-luemoa-le-recalibrage-opere-par-la-decision-n19-29-12-2025-cm-umoa/)
- The SFD licence route took Djamo ~3 years — [The Condia](https://thecondia.com/djamo-first-microfinance-central-bank-bceao/)
- IFC provides 50% portfolio guarantees for digital lending (OBA) — [Ecofin](https://www.ecofinagency.com/news-finances/0302-52548-ifc-to-provide-30-6m-guarantee-for-orange-bank-digital-lending-in-cote-d-ivoire-senegal)
- Tiny tickets default heavily (Kenya: 83% under KES 1,000) — [Business Daily](https://www.businessdailyafrica.com/bd/economy/borrowers-fail-to-repay-83pc-of-digital-loans-below-sh1000-5189888)
- CI quotité cessible is 35–57% of pay — [CivLII](https://civlii.laws.africa/en/akn/ci/act/decree/2014/370/fra@2023-07-18/source)
- Device locking (Knox/PayJoy) is used by Baobab+ — [Financial Afrik](https://www.financialafrik.com/2021/03/18/baobab-et-samsung-democratisent-lacces-aux-smartphones/)
- The CEMAC bureau has existed only since Jan 2026 — [IFC](https://www.ifc.org/fr/pressroom/2026/la-beac-et-la-soci-t-financi-re-internationale-ifc-lancent-officiellement-le-burea0)
- Nigeria bans pre-authorised lending (DEON 2025) — [FCCPC](https://www.fccpc.gov.ng/media/press-releases/digital-lending-fccpc-tackles-abuses-issues-landmark-regulations/)

### Inferences (recommendation)

**Phase 0 (months 0–3): legal and partner set-up**
- Legal opinion on: TEG treatment of wallet/transfer fees, EWA characterisation, merchant-discount BNPL, and Murabaha mark-up.
- Sign a **loan distribution / agency agreement** with an **SFD or financial credit institution** (24% headroom), not a bank (14%). Candidates to approach: Baobab (digital nano-loan capability, IFC-backed); Cofina (prior Orange/Yabx device partnership and securitisation experience); Advans or a large network SFD (e.g., PAMECAS in Senegal, which also has an Islamic window).
- The partner is lender of record and reports to the BIC. Jokko owns the UX, data, scoring model and collections, and provides **first-loss cover of 10–20%** of the portfolio.
- Start the **Jokko SFD licence** file in one market (CI or Senegal) immediately.

**Phase 1 (months 3–9): salary-linked advance in CI first, then Senegal**
- Product: up to 30–50% of net earned salary; 1-month tenor; priced inside the 24% TEG (≈2% max per month all-in).
- Eligibility: only for customers whose salary is **domiciled at Jokko** or covered by an employer payroll deduction agreement.
- Collection: automatic sweep on salary credit, plus employer deduction within the quotité cessible.
- Go-to-market: employer-by-employer B2B2C, starting with mid-size private employers, then civil servants via the partner's payroll codes.
- Target losses: <2% annualised.

**Phase 2 (months 6–15): merchant / device instalments ("BNPL")**
- 3–6 month smartphone and appliance financing with locking tech and electronics retailers (Sociam-type).
- Merchant-subsidised 0% where legal; a Murabaha variant for Senegal, Mali and Niger via an Islamic SFD or window.

**Phase 3 (months 12–24): small revolving overdraft ("flash" credit)**
- Offer only to customers with 3+ months of salary or regular inflows into Jokko.
- Limits start at ~10–20% of average monthly inflow and step up with repayment.
- Minimum ticket around 10,000 FCFA (€15) to avoid the sub-€5 default trap; maximum 30 days; cooling-off between draws; no pre-authorised or auto-disbursed credit.
- The TEG must be shown on every draw.

**Phase 4 (months 18+): SME / merchant working capital**
- For merchants using Jokko acquiring or collections, repaid from a split of receipts.
- Seek IFC/IDA-PSW-style 50% risk-sharing, the OBA precedent.

**Funding path**
1. Partner balance sheet with Jokko first-loss.
2. DFI guarantee or credit line once 12–18 months of vintage data exists.
3. Deposits once the SFD is licensed.
4. FCTC securitisation above ~10bn FCFA (€15m) outstanding.

**CEMAC**
- Defer lending until the CICA bureau is live in the target country and a Category 3 EMF partner (or Jokko's own Cat. 3, 150m FCFA / €229k capital) is in place.
- Usury caps are per country and per quarter, so the pricing engine must be configurable.

**Always-on controls**
- Bureau check and reporting.
- Affordability rule: total debt service ≤ quotité cessible.
- One active loan per product.
- Device and SIM-swap fraud checks; KYC under BCEAO Instruction 003-03-2025.
- Ethical collections: no contact-list harassment.
- Full TEG disclosure in FCFA and %.
- Complaint handling; vintage and PAR monitoring with automatic limit cuts.
- DEON/CBK-grade conduct standards as the internal bar.

### Gaps
- The recommendation depends on unconfirmed legal points (fee inclusion in TEG, EWA characterisation, merchant-discount treatment). These must be validated by WAEMU banking counsel before any launch.
- No partner-specific commercial terms (revenue share, first-loss norms) for WAEMU loan distribution were found publicly. The 10–20% first-loss figure is an industry assumption, not a sourced value.
