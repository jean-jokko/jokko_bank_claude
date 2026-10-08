# Senegal deep dive: B2B-first neobank launch (research date 8 Oct 2026)

Scope: Senegal-specific facts for Jokko's decision to launch in Senegal first (team in Dakar), B2B first (SME payroll, bulk payouts, collections, invoicing, expense cards, employee salary accounts, salary advance via a partner SFD), with a B2C push in 2–3 years and Côte d'Ivoire second. Non-crypto, regulator-clean.

Method: Part 1 consolidates Senegal content already in this folder (`market_waemu_guinea.md`, `competitors_business.md`, `competitors_consumer.md`, `lending.md`, `regulatory_licensing.md`, `rails_demand_playbooks.md`) and the report `reports/West Africa neobank launch strategy.md`. Part 2 adds about 35 targeted searches and fetches made on 8 Oct 2026. Three primary legal texts were read directly: the Senegal Labour Code, the Senegal Code de procédure civile, and BCEAO Instructions 001-01-2024 and 001-03-2025.

Flags used:
- **[PRIMARY]**: read in the official text.
- **[SECONDARY]**: press or analyst source.
- **[VENDOR]**: a commercial blog with a sales interest (notably Kolonell, a Dakar integration agency).
- **[UNVERIFIED]**: single or weak source.
- **[DATED]**: before 2025.
- **[CONFLICT]**: sources disagree.
- **[NEW]**: found in this round; not in the earlier notes.

---

## 0. Ten things that matter most for a Senegal-first B2B launch

1. **Wages already flow digitally in Senegal, which is unique in WAEMU.** 30.5% of adults receive wages. 12.0% are paid into a bank or FI account and 20.1% through a mobile phone, against only 7.5% cash-only ([Global Findex 2025](https://www.worldbank.org/en/publication/globalfindex)). The 0.5% transfer tax (TTA) exempts salary payments, so payroll is the one flow the new tax leaves untouched.
2. **The formal payroll pool is about 0.75–0.8M people.**
   - IPRES (private-sector pension fund) had **577,171 contributing employees** and **40,300 contributing employers** in 2024 ([Le Soleil, citing ANSD SES 2024](https://lesoleil.sn/actualites/economie/prevoyance-retraite-les-charges-de-lipres-estimees-a-plus-de-153-milliards-de-fcfa-en-2024/)) **[NEW]**.
   - The State paid **≈195,000 agents** at end-March 2026 ([search summary of ANSD/budget execution reports](https://lesoleil.sn/actualites/economie/administration-centrale-les-salaires-du-personnel-estimes-a-1252-milliards-de-fcfa-en-janvier-2026/)) **[NEW]**.
   - The government's own budget document estimates that more than 50% of private-law workers are not affiliated with IPRES.
3. **About 40,000 employers is the realistic B2B universe.** The IPRES count of contributing employers is the best proxy for "formal employers with payroll". APIX registers about 26,000 new companies a year, which is about 40% of all creations ([AllAfrica/APS, Sep 2025](https://fr.allafrica.com/stories/202509230683.html)) **[NEW]**.
4. **Senegal's salary-assignment law is more permissive than Côte d'Ivoire's on paper, but procedurally heavy.** Code de procédure civile art. 381 sets a progressive garnishable/assignable scale (10/20/30/40% up to 200,000 FCFA a month, then 100% above). Total deductions of any kind are capped at **two-thirds of net pay**. A formal *cession volontaire* must be declared in person before the president of the regional court (art. 571-2). The Labour Code says **"acomptes sur salaire déjà acquis ne sont pas considérés comme avances"** (art. L.130), which matters for earned-wage-access design (§11) **[NEW, PRIMARY]**.
5. **Wave holds about 80% of e-money float in Senegal.** Float was 459bn of 571bn FCFA on 21 Aug 2026; Orange Money had 106bn ([Senego citing CB-UMOA](https://senego.com/mobile-money-au-senegal-wave-ecrase-la-concurrence-avec-80-du-marche_1997891.html)). Wave is the default payout rail and price anchor (1% sender-pays). From 2 Nov 2026, PI-SPI makes interoperable P2P free up to 8,000 FCFA a day and at most 0.8% above.
6. **Ecobank Sénégal is the de facto card sponsor for fintechs in Senegal.** It is the issuer for Wave's virtual Visa (Jan 2026), Mixx by Yas's Mastercard (Jun 2025) and Djamo Senegal's cards. Bank BaaS is bilateral: private APIs exist, there is no open-banking regime, and no public price lists ([Kolonell [VENDOR]](https://kolonell.com/fr/blog/open-banking-senegal-etat-2026)).
7. **Bank ownership is reshuffling, which creates new partner appetite.** BICIS became **SUNU Bank Sénégal** (renamed 23 Oct 2025). Société Générale Sénégal (ex-SGBS) is for sale with a State pre-emption claim, and closing is **not confirmed** as of Oct 2026. **Banque Islamique du Sénégal rose to #3** by balance sheet in 2025. Orange Bank Africa went from 11 to 556,852 accounts in Senegal in a year.
8. **E-invoicing is legislated but not scheduled.** The Loi de finances 2025 (loi 2025-02) makes it mandatory for VAT-registered taxpayers. The penalty is 25% of the VAT, capped at 5M FCFA per invoice. DGID has published no official rollout calendar ([Deloitte](https://blog.avocats.deloitte.fr/senegal-les-principales-mesures-importantes-de-la-loi-de-finances-pour-2025?amp=1); [Thomson Reuters/Pagero](https://europe.thomsonreuters.com/compliance/regulatory-updates/senegal)). The invoicing module is therefore a "get ready" feature, not a forcing event as Côte d'Ivoire's FNE is.
9. **Macro is the main risk.** Debt is about 130% of GDP, IMF-projected growth is 2.2% for 2026, and the US$2.2bn ECF is still only a staff-level agreement (1 Sep 2026), awaiting Board approval and a misreporting waiver. Expect tax increases, payment arrears to State suppliers, and pressure on public payroll.
10. **Licensing is per country and the "partner first, touch funds later" window is closed.** Since 1 Sep 2025 only licensed PSPs may provide payment services. Senegal already has about 11 licensed EPs, including Julaya SN, Djamo SN, PayDunya, Bictorys and Flutterwave SN. Jokko must be a technical provider or registered agent of a licensed partner until its own EP is granted.

---

## 1. Macro and politics

From existing notes:
- 2025 population 18.93M, 55.8% urban, about 11.8M adults. GDP US$37.0bn, GDP per capita US$1,955 ([WDI](https://data.worldbank.org/)).
- IMF real growth: 6.1% (2024), 7.9% (2025, hydrocarbons), **2.2% (2026p)**, 2.3% (2027p). Inflation 1.4% (2025), 2.5% (2026p). Government debt **130.2% of GDP** (2025) ([IMF REO Apr 2026 via market notes](https://www.imf.org/-/media/files/publications/reo/afr/2026/april/english/statsappendix.pdf)).
- Hidden-debt scandal: the 2023 deficit was 12.3% of GDP, not the 4.9% reported. The Court of Auditors put end-2023 debt at 99.7% of GDP against 74.4% reported ([France 24](https://www.france24.com/en/live-news/20260901-imf-reaches-agreement-with-senegal-on-new-2-2-bn-loan-programme); [Wikipedia](https://en.wikipedia.org/wiki/Senegal_hidden_debt_scandal)).
- **IMF:** a staff-level agreement on a 36-month ECF of about US$2.2bn was reached on 1 Sep 2026. It is subject to Management and Board approval, "decisive corrective actions" to support a misreporting waiver, and financing assurances ([IMF PR26/282](https://www.imf.org/en/news/articles/2026/09/01/pr26282-senegal-imf-reaches-sla-ecf-arrangement)). As of early Oct 2026 no Board approval was found **[NEW]**.
  - **[CONFLICT]** The earlier notes say external debt would go through an enhanced G20 Common Framework ([Credendo](https://credendo.com/en/knowledge-hub/senegal-debt-restructuring-announced-after-hidden-debt-crisis)). The government frames the deal as "without restructuring" ([Financial Afrik, 1 Sep 2026](https://www.financialafrik.com/en/2026/09/01/senegal-imf-a-2-2-billion-program-without-restructuring/)).
- The State is funding itself domestically. Its first 2026 public bond targeted 200bn FCFA and raised 304bn ([Le Soleil](https://lesoleil.sn/actualites/economie/marche-financier-le-senegal-lance-un-emprunt-obligataire-de-200-milliards-de-fcfa/)) **[NEW]**. That crowds out bank credit to the private sector and keeps UMOA-Titres yields attractive, which helps a future savings/yield product.
- 2026 budget: tax revenue projected at 5,384.8bn FCFA, up 23.5% on 2025 ([search summary of PLF 2026 coverage](https://fr.allafrica.com/stories/202603020570.html)) **[NEW]**. The fiscal squeeze is tax-led, so expect more levies on digital flows.
- **Monetary rhetoric:** PM Sonko criticises the CFA franc. The official line is gradual and regional (ECOWAS "eco", targeted around 2027, flexible exchange rate), and **no unilateral exit has been announced** ([search summary: Seneweb, Le Soleil fact-check Jul 2026](https://lesoleil.sn/le-decodeur/fact-checking/faux-un-euro-ne-vaudra-pas-655-eco-et-le-franc-cfa-ne-disparaitra-pas-automatiquement-en-2027/)) **[NEW]**. This is a low-probability, high-impact tail risk to keep in the risk register.

Implications:
- Austerity raises the risk of arrears on public salary-linked lending and of late State payments to SMEs. That in turn raises SME demand for working capital and invoice finance.
- Prefer private-sector payroll first. Treat civil servants as phase 2, via a bank or SFD that already holds payroll deduction codes.

## 2. Financial inclusion and digital readiness

From existing notes (Findex 2025, survey year 2024):

| Indicator (% of adults) | Senegal |
|---|---|
| Any account | 76.5 |
| Bank/FI account | 48.0 |
| Mobile money account | 66.9 |
| Main phone is a smartphone | 60.8 |
| Daily internet use | 45.0 |
| Saved formally | 58.3 |
| Borrowed from a formal FI | 17.6 |
| Borrowed from a mobile money provider | 11.3 |
| Owns a debit card | **32.7** (highest in WAEMU) |
| Bought something online | 21.7 |

Source: [Global Findex 2025](https://www.worldbank.org/en/publication/globalfindex).

Other indicators:
- BCEAO's broad inclusion rate for Senegal was 85.9% in 2024 ([MADIS Invest citing BCEAO](https://madisinvest.com/actualites/economie/uemoa-le-taux-dinclusion-financiere-atteint-736-en-2024-b3FYEqxr68XRdloFSOMa)).
- Internet users: 60.1% of the population (ITU 2024).
- MicroSave (Jun 2025) counts 48 fintechs in Senegal by 2024 and "83.3% financial inclusion" ([MicroSave infographic](https://www.microsave.net/fr/wp-content/uploads/2025/06/Infographie-Fintech-SENEGAL-FR062025OK.pdf)) **[NEW, SECONDARY]**.
- **eKYC:** onboarding is document plus liveness (OCR on the national ID card plus selfie). No State API for identity verification against the national register was found. The New Deal Technologique (launched 24 Feb 2025, 1,105bn FCFA) lists an e-ID and e-Sign as priority digital public infrastructure, but no rollout date has been published ([AllAfrica](https://fr.allafrica.com/stories/202502250306.html); [Seneweb on eKYC](https://www.seneweb.com/fr/news/Technologie/identite-numerique-pourquoi-labsence-dun-ekyc-regional-coute-cher_n_483400.html)) **[NEW]**.
  - Vendor pages say the ANSD issues the ID card. In fact the national biometric ECOWAS ID card is produced under the Interior Ministry (DAF) **[UNVERIFIED]**.

## 3. Payroll, employment and wages: the B2B and salary-advance base

**Survey-based (Findex 2025):** 30.5% of adults receive wages, which is about **3.6M people**. 4.9% receive public-sector wages, about 0.58M. 12.0% are paid into an FI account and 20.1% by phone; 7.5% are cash-only.

**Administrative counts [NEW]:**
- **IPRES (private-sector pensions):** 577,171 contributing employees in 2024 (567,103 in 2023, +1.8%), and 40,300 contributing employers (38,381 in 2023, +4.9%). Revenue was 170bn FCFA in 2024 and expected contributions are 174bn FCFA in 2026 ([Le Soleil citing ANSD SES 2024](https://lesoleil.sn/actualites/economie/prevoyance-retraite-les-charges-de-lipres-estimees-a-plus-de-153-milliards-de-fcfa-en-2024/); [Le Soleil on IPRES 2026](https://lesoleil.sn/actualites/economie/ipres-174-milliards-fcfa-de-cotisations-a-encaisser-en-2026/)).
  - The DPBEP 2027–2029 budget document estimates social-security evasion at more than 50% of private-law workers (search summary).
- **FNR (civil-service pension fund):** 144,543 contributors and 75,134 pensioners at end-2024 (same source).
- **State payroll:**
  - 195,144 agents at end-March 2026, against 186,205 a year earlier. 191,817 in January 2026 (ANSD).
  - At end-June 2025, 188,576 agents were paid: 183,549 permanent and 5,027 contractual.
  - Q1 2026 wage bill: 375.1bn FCFA (+5.1%). Central-administration salaries were 125.2bn FCFA in January 2026 ([Le Soleil](https://lesoleil.sn/actualites/economie/administration-centrale-les-salaires-du-personnel-estimes-a-1252-milliards-de-fcfa-en-janvier-2026/)).
  - **[SECONDARY]** Figures come from a search summary of ANSD/DGB reports. The headcount definitions differ.
- **Modern formal private sector (ANSD EERH):**
  - About 335,653 salaried employees on average in 2024, with a total wage bill of 1,540.4bn FCFA (+6.9%).
  - Q3 2025: 337,415 employees. Q4 2025 wage bill: 413.4bn FCFA (+3.4%).
  - Permanent staff are 76.6% of employees and take 92.1% of the wage bill ([vie-publique EERH 2024](https://www.vie-publique.sn/documents/10391/enquete-sur-lemploi-la-remuneration-et-les-heures-de-travail-eerh-rapport-annuel-2024-ansd); [Le Soleil Q4 2025](https://lesoleil.sn/actualites/economie/secteur-moderne-4134-milliards-de-fcfa-de-masse-salariale-enregistree-au-4ᵉ-trimestre-2025/)).
  - **Derived average:** about **380,000 FCFA a month per formal modern-sector employee** (wage bill ÷ headcount; my calculation, not an ANSD figure).
  - **[CONFLICT]** Trading Economics shows an "average monthly wage" of about 122–126k FCFA (Q3–Q4 2025, ANSD series with a different scope).
  - The EERH covers a narrower firm universe than IPRES (335k vs 577k).
- **Minimum wage:** the SMIG is **64,223 FCFA a month** under Decree 2023-1710 of 7 Aug 2023 ([PaySpace](https://support.payspace.com/portal/en/kb/articles/senegal-social-security-ceiling-update)) **[SECONDARY, UNVERIFIED against the Journal officiel]**.
  - Older guides cite 47,700 FCFA (2018 decree), which is outdated.
  - The CSS planned to raise its contribution ceiling from 63,000 to 80,000 FCFA from 1 Apr 2025, but this was suspended by a circular of 29 Jan 2025 (same source).
- **How public servants are paid:**
  - UEMOA Directive 08/2002 (transposed by Senegal's Law 2004-15 of 4 Jun 2004) requires State, public and para-public employers to pay salaries **at or above 100,000 FCFA** by cheque or transfer to a bank or postal account. The threshold is set by BCEAO instruction ([CB-UMOA Directive 08/2002](https://www.cb-umoa.org/sites/default/files/2025-03/DIRECTIVE%20N%C2%B0%2008_2002_CM_UEMOA%20PORTANT%20SUR%20LES%20MESURES%20DE%20PROMOTION%20DE%20LA%20BANCARISATION%20ET%20DE%20L%E2%80%99UTILISATION%20DES%20MOYENS%20DE%20PAIEMENT%20SCRIPTURAUX%20%282%29.pdf)) **[NEW]**.
  - The **SenTrésor** mobile payment platform (pilot 28 Mar 2025, launch 2 Jun 2025) pays bursaries, social aid and pensions to wallets. It plans to add salaries and allowances **≤100,000 FCFA** "in line with Community provisions". After the pilot, 44,000+ beneficiaries had been paid more than 4bn FCFA ([APA News](https://fr.apanews.net/technologies/senegal-le-tresor-public-lance-sen-tresor-pour-digitaliser-les-paiements-de-masse/); [Droit Médias Finance](https://droitmediasfinance.com/index.php/actualites/droit-tech-fintech/1016-senegal-sen-tresor-ou-la-digitalisation-des-services-financiers-de-letat)) **[NEW]**.
  - **Implication:** civil servants above 100k FCFA must be paid into a bank (or postal) account. Whether an e-money or SFD account qualifies is untested. A neobank needs a **partner bank or SFD account (RIB)** to capture civil-servant salary domiciliation.
  - The directive's art. 4 targets public employers, so private employers are not clearly bound (my reading).
  - Public-servant loans are typically repaid by payroll deduction, at 0.5–5M FCFA over 12–60 months, offered by BHS, LBA (ex-CNCAS), CBAO, SG and others ([Ndarinfo 2026](https://www.ndarinfo.com/Comment-obtenir-un-pret-personnel-sans-garantie-au-Senegal-en-2026-banques-microfinance-et-credit-fonctionnaire_a43629.html)) **[SECONDARY]**.

Inferences:
- **The B2B payroll serviceable market** is about 40k IPRES-contributing employers plus the informal and under-declared long tail. Jokko's core ICP is likely the 1–5k firms with 10–500 staff in Dakar, Thiès and Saint-Louis.
- **Salary accounts for employees:** about 0.58M declared private employees plus about 0.2M State agents, plus several hundred thousand undeclared salaried workers. Most are already paid digitally, many to Wave. The contestable piece is being the *destination account* with credit attached, not just the rail.

## 4. SME base and business formation

- **ANSD RGE 2016** (the last census): 407,882 economic units, 97.0% informal, 96.8% natural persons. The formal sector produces 83.7% of turnover. 844,268 workers were counted ([ANSD RGE](https://www.ansd.sn/Indicateur/resultats-du-recensement-general-des-entreprises-rge); [Africa Check](https://africacheck.org/fr/fact-checks/articles/senegal-des-donnees-sur-le-secteur-informel-examinees)) **[NEW, DATED]**.
  - **RGE-2** is under way: mapping May–Sep 2026, data collection in H1 2027 ([AllAfrica, Aug 2026](https://fr.allafrica.com/stories/202608130522.html)). Results are expected in 2027–28.
- The employers' federation says only **about 18,000 firms file financial statements** (formal in the full sense). ANSD's ERI-ESI 2017 found 3.6% of the employed work in the formal sector (via [Africa Check](https://africacheck.org/fr/fact-checks/articles/senegal-des-donnees-sur-le-secteur-informel-examinees)) **[NEW]**.
- The State targets halving the share of informal units by 2030 ([Seneweb](https://www.seneweb.com/fr/news/Economie/90-of-businesses-operate-in-the-informal-sector-the-state-is-launching-a-massive-formalization-program-by-2030_n_474153.html)).
- **APIX creations:** about 26,000 in 2024 and 9,200 in H1 2025 (slowed by court clerks' strikes). APIX handles only about 40% of all creations; the rest go through chambers of commerce ([AllAfrica, Sep 2025](https://fr.allafrica.com/stories/202509230683.html)) **[NEW]**. Total creations are therefore plausibly 50–65k a year (calc.), mostly sole proprietorships.
- Formalities: APIX centralises RCCM + NINEA in 48–72h officially (2–5 days in practice). An RCCM is required to invoice or open a business account ([Kolonell [VENDOR]](https://kolonell.com/fr/blog/cepici-vs-apix-comparatif-creation-senegal-cote-ivoire-2026)). Wave Business and Orange Max it merchant APIs require a valid NINEA + RCCM.
- **Merchants:** 218,583 active mobile money merchants and 412,172 registered (2024); 909 merchants accept online payments via mobile money. Only 193 private companies are registered for mobile money bill/collection payments ([BCEAO SFN 2024](https://www.bceao.int/sites/default/files/2026-03/Rapport%20annuel%20sur%20les%20services%20financiers%20num%C3%A9riques%20dans%20l'UEMOA%20-%202024.pdf)).
- **SME credit gap:** 7.2% of GDP; fewer than 25% of MSMEs have bank loans; MSMEs are more than 90% of firms and about 40% of jobs ([IFC 2026](https://www.ifc.org/en/pressroom/2026/ifc-partners-with-soci-t-g-n-rale-to-expand-access-to-finance-for-msmes-create-job)). 63% of MSMEs are credit-constrained ([FinDev Gateway](https://www.findevgateway.org/data/msme-finance-gap)).
- **Bank SME account fees:** UBA SN charges 25,000 FCFA a month for SA/SARL/PME and 10,000 for TPE ([Comparek [UNVERIFIED]](https://comparek.sn/banques/produits/compte-entreprise)). Djamo Business is free.

## 5. Mobile money market

- **2024 (BCEAO):** 42.6M registered and 14.65M active (90-day) accounts, an activity rate of 34.4%. 2.874bn transactions worth 48,488bn FCFA (≈€73.9bn), 30.9% of WAEMU value. Payments 3,113bn FCFA. Bank↔wallet transfers: 16.5M operations worth 1,120.6bn FCFA ([BCEAO SFN 2024](https://www.bceao.int/sites/default/files/2026-03/Rapport%20annuel%20sur%20les%20services%20financiers%20num%C3%A9riques%20dans%20l'UEMOA%20-%202024.pdf)).
- **2025:** the government estimates mobile money transactions at **15,300bn FCFA** ([Osiris](https://osiris.sn/mobile-money-15-300-milliards-f-cfa-de-transactions-en-2025.html)) **[NEW, CONFLICT]**. This is far below BCEAO's 48,488bn for 2024, probably because of a different scope (excluding cash-in/out?).
  - Senegal holds 29.7% of WAEMU e-money outstanding at end-2025 (1,923.2bn union-wide) ([Le Soleil](https://lesoleil.sn/actualites/economie/uemoa-le-senegal-en-tete-sur-la-microfinance-et-la-monnaie-electronique-en-2025/)).
- **Shares:**
  - E-money float on 21 Aug 2026: **Wave 459bn FCFA (≈80%)**, Orange Money 106bn (≈19%; operator-declared), total 571bn ([Senego citing CB-UMOA](https://senego.com/mobile-money-au-senegal-wave-ecrase-la-concurrence-avec-80-du-marche_1997891.html); [Senego, 31 Aug 2026](https://senego.com/bceao-telecoms-et-fintechs-avancent-vers-le-credit-le-cadre-prudentiel-en-debat_1998398.html)).
  - Wave is "commonly reported" at about 70% of active users, with about 90% of adults holding a Wave account ([Substack [SECONDARY]](https://pambossoteriades.substack.com/p/the-price-was-the-product)). It has about 8M monthly users in Senegal ([TechCabal](https://techcabal.com/2025/06/30/wave-raises-137-milion/)).
  - Orange Money SN reports 13.7M users (+9.5%).
  - **Mixx by Yas** (ex-Free Money, Axian group) is small, at about 2% of WAEMU value.
- **Pricing:**
  - Wave: 1% send (cap 5,000 FCFA), free cash-in/out, bulk payouts 1% sender-pays, merchant acceptance free up to 20,000 FCFA a day then 1% ([wave.com/fr/business](https://www.wave.com/fr/business/)).
  - Orange Money SN removed transfer fees and charges 1% withdrawal (cap 5,000).
  - Aggregator collections: Naboopay 1.5–2%, PayDunya 2.5–3.5% ([Kolonell [VENDOR]](https://kolonell.com/en/blog/payment-aggregator-multi-psp-comparison-senegal-2026)).
- **PI-SPI:**
  - Launched in Dakar on 30 Sep 2025. Senegal had **43 authorised participants** of 175 at 30 Sep 2026 (CI had 38).
  - Mandatory for interoperable e-money transfers from **2 Nov 2026**: free up to 8,000 FCFA a day per user per provider, at most 0.8% above, receiving always free. Cross-border UEMOA transfers follow from 1 Jun 2027.
  - Wave connected on 30 Sep 2026.
  - The "API Business" tier had only 24 names in mid-Sep 2026, mostly CI/SN ([Financial Afrik, 4 Oct 2026](https://www.financialafrik.com/2026/10/04/la-bceao-rend-pi-spi-obligatoire-revoit-ses-tarifs-et-pose-enfin-la-question-de-nouveaux-services-financiers-adosses-a-la-plateforme/)).
  - **For B2B payouts this is the key rail to get on via a partner.**
- Wave and the CSS (social security fund) now pay certain social benefits (family allowances, maternity and work-injury daily allowances, and annuities under 100,000 FCFA) into Wave accounts ([Senego](https://senego.com/css-lancement-du-paiement-de-certaines-prestations-sociales-via-wave_2003968.html); [AllAfrica, Sep 2026](https://fr.allafrica.com/stories/202609030297.html)) **[NEW]**. This deepens Wave's B2G/payroll-adjacent position.
- DER/FJ (the State entrepreneurship agency) signed a partnership with Wave Sénégal at VivaTech in June 2026 (LionsTech programme) ([Osiris](https://osiris.sn/vivatech-2026-la-der-fj-et-wave-senegal-signent-un-partenariat-strategique-au.html)) **[NEW]**. Wave is close to the State's startup apparatus.

## 6. Taxes and compliance rails relevant to B2B

**Transfer tax (TTA) and merchant withholding (Law 2025-17 of 27 Sep 2025, JO of 2 Oct 2025):**
- 0.5% per transfer, payment or withdrawal operation, capped at 2,000 FCFA, whatever the channel. Withdrawals are taxed only on amounts above 20,000 FCFA per 24h.
- Plus **0.5% withholding on merchant receipts** via electronic platforms, collected by operators.
- **Exempt:** cash deposits, small withdrawals, **salary and scholarship payments**, State transfers, ordinary bank transfers, same-network transfers, and bank↔operator operations (per the minister).
- Orange applied it from 16–17 Dec 2025 ([Seneweb](https://www.seneweb.com/en/news/Societe/orange-money-la-taxe-sur-les-transferts-dargent-tta-de-05-entre-en-vigueur-des-le-17-decembre_n_477669.html); [Senego](https://senego.com/mobile-money-la-taxe-sur-les-transferts-dargent-entre-en-vigueur-ce-17-decembre-2025_1903513.html)).
- **[CONFLICT, NEW]** An Osiris op-ed (Jan 2026) claims neither Orange nor Wave was actually collecting it on the ground and that technical modalities were unfinished ([Osiris](https://osiris.sn/taxe-sur-les-transferts-mobiles-l-etat-annonce-les-operateurs-silencent-le.html)).
- Revenue target: 230bn FCFA in earlier notes, "220bn over three years" in one source, "€350M a year" in another **[CONFLICT]**.
- GSMA says the 0.5% taxes cut Senegal's tax score from 65 to 31 (via Osiris).
- No 2026 amendment or suspension was found.
- **Implication for Jokko:** payroll is exempt, so lead with payroll. Supplier payouts and merchant collections carry 0.5%; design pricing so the tax is shown separately. Bank-transfer and PI-SPI flows may be advantaged, but confirm with a tax adviser whether PI-SPI transfers between institutions count as "ordinary bank transfers" or "transfers".

**E-invoicing:**
- Legislated by the Loi de finances 2025 (loi 2025-02 of 28 Dec 2024) for VAT-registered taxpayers.
- Penalty: 25% of the VAT that should have been e-invoiced, capped at 5M FCFA per invoice ([Deloitte](https://blog.avocats.deloitte.fr/senegal-les-principales-mesures-importantes-de-la-loi-de-finances-pour-2025?amp=1); [Thomson Reuters/Pagero](https://europe.thomsonreuters.com/compliance/regulatory-updates/senegal)).
- **No official DGID calendar** has been published (Pagero says so). Vendor blogs give contradictory dates: ≥100M FCFA turnover from Jan 2026 and ≥30M from Jul 2026, versus "2027–28", with a 50,000 FCFA penalty per invoice ([Kolonell [VENDOR, CONFLICT]](https://kolonell.com/fr/blog/facturation-electronique-normalisee-dgid-senegal-2026)) **[NEW]**.
- **Implication:** build the invoicing module to be FNE-like and DGID-ready, but do not count on a 2026–27 mandate to force adoption in Senegal.

**Tax and social payments:**
- DGID lets taxpayers pay all taxes, duties and fees through **Orange's Max it** app ("FAY SAMA IMPÔT"), announced Nov 2025 ([DGID communiqué via APS](https://aps.sn/wp-content/uploads/2025/11/Communique-externe-sur-le-lancement-du-paiement-des-impots-taxesdroits-et-redevances-sur-max-it-orange.pdf); [AllAfrica](https://fr.allafrica.com/stories/202511120539.html)) **[NEW]**. No Wave equivalent was found.
- DGID's **SenTimbre** replaced physical tax stamps from 20 Jul 2026 ([SenePlus](https://www.seneplus.com/article/la-dgid-bascule-vers-le-tout-numerique-avec-sentimbre)).
- IPRES supports employer tele-declaration and contributions. A 2026 employee portal is planned ([Dakaractu](https://www.dakaractu.com/IPRES-Vers-une-revolution-digitale-en-2026-avec-le-portail-salarie-et-la-gestion-anticipee-des-retraites_a267681.html)). IPRES/CSS's "Ndamli" one-stop platform launched regionally in 2026 (earlier notes).
- **No evidence that employers can pay IPRES/CSS contributions by mobile money.** eRegulations still describes payment at the cashier by cheque or bank transfer ([eRegulations](https://senegal.eregulations.org/procedure/103/64/step/213?l=fr)).
- **Implication:** "pay salaries + IPRES + CSS + taxes from one account" via bank transfer is a credible B2B feature. It needs an account with a RIB (partner bank) and an integration path to IPRES/CSS/DGID.

## 7. Competitors active in Senegal

| Player | Senegal licence | What it does in SN (B2B relevance) | Gaps / notes |
|---|---|---|---|
| **Wave** (Wave Digital Finance; Wave Business) | BCEAO EME (14 Apr 2022); Wave Bank Africa is CI-only, licence pending as of Apr 2026 | ≈80% of SN e-money float; bulk payouts at 1% sender-pays; agent cash collect; merchant API; free virtual Visa with **Ecobank SN** (23 Jan 2026); CSS benefit payments; credit, savings and insurance "in preparation" (Feb 2026), **no launch confirmed by Oct 2026** ([Financial Afrik interview](https://www.financialafrik.com/2026/02/18/entretien-exclusif-avec-el-hadji-malick-gueye-directeur-general-de-wave-digital-finance/)) | No IBAN; 2M FCFA balance cap; prepaid card refused by Apple; no multi-user approvals or payroll workflow documented |
| **Orange Money / Orange Bank Africa** | EME (OFMS) + OBA bank (SN branch, licensed Sep 2023 per Senego; earlier notes say opened 2024/Feb 2025 **[CONFLICT]**) | OBA SN: 11 → **556,852 accounts** and 5.2 → 31.7bn FCFA balance sheet in 2025, 1 branch, 15 staff ([Senego](https://senego.com/classement-des-banques-au-senegal-la-bis-monte-3e-orange-bank-signe-une-percee-spectaculaire_1996678.html)); Tik Tak nano/SME loans with an IFC 17bn FCFA guarantee (CI+SN); OM Mastercard prepaid launched 28 Nov 2025 with Orange Bank, Mastercard and Network International ([Dakaractu](https://www.dakaractu.com/La-carte-prepayee-Mastercard-Orange-Money-officiellement-lancee-au-Senegal_a267053.html)); tax payments in Max it | Strongest distribution for nano-credit; weak SME workflow |
| **Mixx by Yas** (ex-Free Money) | EME | Mastercard prepaid with **Ecobank SN** (Jun 2025); nano-credit (~30k beneficiaries); earlier "Lebalma" credit with Cofina (2021) | Small share |
| **Djamo Sénégal** | EP.SN.010/2025 (3 Sep 2025); MFI licence is CI (Djamo Finances) | Consumer app plus Djamo Business (bulk payments, employee cards, payroll into Djamo accounts, zero account fee); cards via partner banks (Ecobank; BCEAO page lists Ecobank Senegal prepaid) | Only 5–10% of users salaried; no approvals workflow documented; $40M Series C in progress |
| **Julaya Sénégal** | EP.SN.009/2025 | Closest B2B analogue: payroll to MoMo, approvals, sub-accounts, "RIB Julaya", Cash & Collect; partners with "10 banks in CI and SN" for top-ups and has a "sponsor bank" (unnamed); prepaid business cards with **Mansa Bank + Mastercard** ([Financial Afrik 2022 interview](https://www.financialafrik.com/2022/09/28/entretien-avec-olivier-houben-country-manager-de-julaya-au-senegal/)) **[DATED]** | Pricing unpublished; no credit despite a 2022 promise; SN bank partners unnamed |
| **PayDunya** (DUNYA Digital Payment SA) | EP (May 2025) | Collections and payouts aggregator (MoMo 2.5–3.5%) | Reported Peach Payments acquisition **[UNVERIFIED]** |
| **Bictorys** | EP (May 2025) | Merchant checkout incl. Shopify | No reliable traction data |
| **Naboopay** | Not in EP lists found **[UNVERIFIED]** | Cheapest SN-only MoMo aggregator (1.5–2%) | Check licence status |
| **Flutterwave Sénégal** | EP.SN.004/2025 | Payment links and collections | No local fees published |
| **InTouch** (TouchPay) | EME in SN; EP elsewhere | B2B omnichannel payments | Potential rail partner |
| **Wizall Money** | E-money distributor (Banque Atlantique/BCP group) | B2B2C salaries, scholarships, NGO disbursements | Bank-owned |
| **New Africa Technology (Flash)** | Wallet; Mastercard prepaid card (Nov 2024) with "Flash in Business" | SN/CI/BJ ([IBS Intelligence](https://ibsintelligence.com/ibsi-news/mastercard-and-new-africa-technology-launch-fintech-card-in-senegal-cote-divoire-benin)) **[NEW]** | Small |
| **Kori Tech** | Merchant multi-wallet terminal (KoriPass) | Collections hardware | Not a wallet |
| **Fintra** (Orya) | None found | Salary advance pilot (2022): up to 20% of salary at 6% for 15 days, paid to OM/Wave/Free | **[DATED]**; no 2025–26 activity found. **WAGIS** (Dakar student startup) is building EWA, not yet deployed ([Osiris](https://www.osiris.sn/a-21-ans-un-etudiant-du-cesag-veut-revolutionner-l-acces-au-salaire-en-afrique.html)) |
| **Kopar Express / BNDE** | n/a | Government-backed diaspora neobank planned for Dec 2024 | Launch unconfirmed ([FinDev](https://www.findevgateway.org/fr/actualites/une-neo-banque-au-service-de-la-diaspora-le-senegal-franchit-une-nouvelle-etape-digitale)) |
| **Scale** (South Africa) + Mastercard | Issuing enabler | Single integration covering SN, CI, KE, ZM, ZW; in SN focused on **payout cards and corporate spend cards** (Mar 2026) ([TechCabal](https://techcabal.com/2026/03/26/scale-partners-with-mastercard-to-simplify-card-issuance-across-five-african-markets/)) **[NEW]** | A possible issuer-processor route for Jokko's expense cards; bank sponsor in SN not named |

Gaps no one fills in Senegal:
- A payroll **operating system** that combines declaration-ready payslips (IPRES/CSS/IR exports), multi-operator payouts and PI-SPI with approvals, an employee salary account with an **IBAN/RIB**, and a **salary advance priced inside the usury cap**.
- Expense cards that work on Meta/Google ads and SaaS.
- E-invoicing readiness plus collections reconciliation.
- Julaya is the only workflow competitor. Wave is the price anchor. Djamo is the zero-fee anchor.

## 8. Licences: what exists and what Jokko needs (Senegal)

- **EP (payment institution):**
  - Minimum capital is 100M FCFA (≈€152k) for the full service set (lower tiers 10–100M by service). Licensed per country; 6-month statutory review.
  - No lending, no interest, no distributors (only BCEAO-registered "agents de services de paiement").
  - **Senegal EPs** (BCEAO list at 31 Jan 2026): Dunya (PayDunya), Mikaty, Bictorys, Flutterwave SN, Samir Money, Versus Finances Tech, Copay, Sesa Digital Finance, Julaya SN, Djamo SN, African Financial Agent ([BCEAO EP list](https://www.bceao.int/sites/default/files/2026-03/LISTE%20DES%20ETABLISSEMENTS%20DE%20PAIEMENT%20AGR%C3%89%C3%89S%20DANS%20L%E2%80%99UMOA%20au%2031%20janvier%202026.pdf)).
  - In May 2025 Senegal had 100+ fintechs but only 2 licensed and 13 files in advanced review ([BIE/CCIAD](https://bie.cciad.sn/2025/05/09/regulation-des-fintechs-les-precisions-de-la-bceao/)).
- **EME:** 300M FCFA; no credit.
- **SFD:** usury cap 24% all-in. Djamo's licence took about 3 years.
- **Bank:** new minimum capital is 20bn FCFA.
- **Usury from 1 Jun 2026:** 14% for banks, 24% for SFDs and financial credit institutions, all-in TEG ([BCEAO Decision 19/29-12-2025](https://www.bceao.int/sites/default/files/2026-01/Decision-No19-du-29-12-2025_CMUMOA_fixant_le_taux_de_l-usure.pdf)).
- **Hard rule since 1 Sep 2025:** only licensed or registered structures may provide payment services. Before its EP, Jokko can be only a technical provider to, or a registered agent of, a licensed PSP. Under Instr. 001-01-2024 art. 9, it must not present itself as an EP.
- **BCEAO "digital bank" debate (Aug 2026):** three options are under discussion for telcos and fintechs that want to take deposits and lend: same activity same rules; a new digital-bank category; or functional separation. No decision yet ([Senego](https://senego.com/bceao-telecoms-et-fintechs-avancent-vers-le-credit-le-cadre-prudentiel-en-debat_1998398.html)). A new category could open a mid-cost route for Jokko by about 2028.

## 9. Banking sector, 2024–26 ownership changes, and fintech-partnership landscape

**Sector:**
- 29 banks and 4 financial institutions; aggregate balance sheet 15,681bn FCFA at end-2025 ([Senego, 24 Aug 2026, citing CB-UMOA 2025 report](https://senego.com/classement-des-banques-au-senegal-la-bis-monte-3e-orange-bank-signe-une-percee-spectaculaire_1996678.html); [Capmad](https://www.capmad.com/article/classement-2025-des-banques-au-senegal-cbao-reste-en-tete-bis-et-sunu-bicis-bousculent-la-hierarchie)) **[NEW]**.
- Credit HHI is 706 (low concentration). Private credit is 30.9% of GDP.

**Ranking by balance sheet, end-2025:**

| # | Bank | Balance sheet (bn FCFA) | Ownership / notes |
|---|---|---|---|
| 1 | CBAO Groupe Attijariwafa bank | 1,791 (≈11.4%); 433,917 accounts; 88 branches | Moroccan; Attijariwafa launched a neobank venture in Jun 2026 (launch market unconfirmed) |
| 2 | Société Générale Sénégal (ex-SGBS) | 1,615 | **For sale.** SG holds 63.31%. The State asserted its pre-emption right; a BNDE-led deal valued at about 175–176bn FCFA was reported in 2024–25. Still "envisaged" in Dec 2025–Jan 2026 analyses. **No closing found by Oct 2026** ([Le Soleil](https://lesoleil.sn/actualites/economie/banque-letat-envisage-lacquisition-de-la-societe-generale-senegal/); [Financial Afrik tribune, 31 Dec 2025](https://www.financialafrik.com/2025/12/31/tribune-lopportunite-strategique-et-les-risques-maitrisables-de-lacquisition-de-la-societe-generale-senegal/)). IFC lent SG SN up to €50M for MSMEs (Mar 2026) |
| 3 | **Banque Islamique du Sénégal (BIS)** | 1,291; 980 deposits; 875 financing; 249,119 accounts; 42 branches | Tamweel Africa Holding (IsDB group); IFC US$40M Murabaha facility (Oct 2025) to triple its MSME book to about $350M over 5 years ([AllAfrica](https://fr.allafrica.com/stories/202510090275.html)) |
| 4 | Ecobank Sénégal | ≈1,248 | ETI group; **issuer for Wave SN, Mixx and Djamo SN cards**; Hub2 MoU (Feb 2026) linking 200M wallets to Ecobank's platform ([Financial Afrik](https://www.financialafrik.com/2026/02/25/ecobank-et-hub2-elargissent-lacces-aux-paiements-numeriques-a-200-millions-dutilisateurs-de-portefeuilles-mobiles-en-afrique-francophone)) |
| 5 | BNDE | 853 | State-majority (81.8%); Kopar Express diaspora project; designated vehicle for the SG takeover |
| 6 | Bank of Africa Sénégal | ≈836; net profit 21.9bn (2025) | BMCE/Bank of Africa group; BOA CI white-labels Julaya bulk payments |
| 7 | **SUNU Bank Sénégal (ex-BICIS)** | 807 | BNP sold 54.11% to SUNU (closed 28 Apr 2023); renamed **23 Oct 2025** ([Seneweb](https://www.seneweb.com/fr/news/Economie/changement-de-denomination-sociale-la-bicis-devient-officiellement-sunu-bank-senegal_n_472135.html)); ambition to reach the top 3, so likely hungry for distribution |
| 9 | BHS (Banque de l'Habitat) | 504bn loans; 319,700 accounts | State-linked; civil-servant/housing lender |
| 15 | Afrika Banque Sénégal (ex-Banque de Dakar) | 443 | Renamed |
| n/a | La Banque Agricole (ex-CNCAS) | 44 branches | State-linked; civil-servant loans |
| n/a | UBA Sénégal | 89 loans / 246 deposits | Lends little; private APIs per Kolonell |
| n/a | Orabank SN (fell 3 places), Coris Bank SN, NSIA, Banque Atlantique (BCP; owns Wizall), CBI, FBN, BRM, Citi | not given | Not retrieved |

Ownership summary (2023–26):
- **BICIS → SUNU Bank Sénégal** (French exit, done).
- **SG Sénégal → State/BNDE** (pending; unconfirmed).
- Société Générale also exited Cameroon and other subsidiaries ([CFNews](https://www.cfnews.net/L-actualite/CFNEWS-Afrique/Un-ete-de-cessions-africaines-pour-Societe-Generale-495554)).
- **Banque de Dakar → Afrika Banque**.
- **Orange Bank Africa** scaling in SN.
- **Wave Bank Africa** (CI only).
- The government says it is "unacceptable" that the sector stays mostly foreign-controlled. Expect state-aligned banks (BNDE, BHS, LBA, SG SN if acquired) to seek digital and inclusion partners.

**Card issuing and BaaS in Senegal:**
- **Ecobank SN** issues for Wave (Visa virtual, Jan 2026), Mixx (Mastercard, Jun 2025) and Djamo SN. **Orange Bank** is the partner on the OM Mastercard. **Mansa Bank** (CI) partnered with Julaya on Mastercard prepaid. **Banque Atlantique** backs Wizall's Mastercard (CI). NAT/Flash went direct with Mastercard (issuer not named).
- **Open banking:** there is no regulated open-banking regime in UEMOA in 2026. Ecobank, SG, BICIS/SUNU and UBA expose **private, contractual APIs** to large corporates and selected fintechs ([Kolonell [VENDOR]](https://kolonell.com/fr/blog/open-banking-senegal-etat-2026)) **[NEW]**.
- Visa discussed opening a Dakar office with the digital minister in Mar 2026 (search summary) **[UNVERIFIED]**.

## 10. Microfinance (SFD) players as lending partners

**Sector, end-2025 (DGSF bulletin via Le Soleil, 12 Jun 2026)** ([AllAfrica](https://fr.allafrica.com/stories/202606120793.html)) **[NEW]**:
- 129 IMFs: 10 mutualist unions with 169 affiliated institutions, 106 non-affiliated, 11 companies and 2 associations.
- 4.7M+ members/clients; 1,009 service points.
- Deposits 634.7bn FCFA (+9.5%); **gross loans 849.9bn (+9.8%)**; Q4 2025 disbursements 262.7bn.
- Doubtful loans are 6.0% of the portfolio, against a 3% BCEAO norm. Equity 230.6bn.
- Senegal holds 26.5% of WAEMU microfinance assets.
- A 2bn FCFA FONAMIF–CDMP fund for microfinance digitisation was set up in Aug 2026. The PACTIFU programme (2025–29) targets 683bn FCFA for inclusion (search summary).

| SFD | Notes | Fit for Jokko |
|---|---|---|
| **Crédit Mutuel du Sénégal (CMS)** | Largest network: about 1.3M members, 215–250 points; savings about 200bn and loans about 105bn FCFA (Nov 2021) **[DATED]**; Oikocredit €5M | Big balance sheet and deposits; mutualist governance is slower; good for civil-servant/payroll loans |
| **PAMECAS** | Mutualist network; about 850k members and 90k+ borrowers (Proparco, undated); **DEFI Islamic window**; Proparco/CDP 4.5–5.2bn FCFA lines | Strong candidate for **salary advance plus an Islamic (Murabaha) variant** |
| **ACEP** | Historically a leading SME lender; Kolonell claims about 280bn outstanding **[VENDOR, UNVERIFIED, likely overstated]** | SME working capital |
| **Baobab Sénégal** (ex-Microcred) | Group: loan book €963M, PAR30 2.06% (end-2025), Beltone (Egypt) acquisition **[UNVERIFIED]**; SN: **M-Baobab** with Orange Money (Mar 2022: up to 500k FCFA instant loans, 6% savings); BRVM bond "GSS BAOBAB 6.80% 2024–2029"; Citi US$25M financing (2025) **[SECONDARY]**; IFC up to 68bn FCFA across 6 subsidiaries | **Best digital-lending track record**; API and wallet experience; IFC-backed; on PI-SPI |
| **Cofina Sénégal** | "Méso-finance" for SMEs; Senegal is the group's first market; met President Faye Mar 2025; Lebalma credit with Free Money (2021); Orange/Yabx/Cofina device finance (CI); FCTC securitisation precedent (2018) | Fintech-friendly, SME-focused; on PI-SPI; check financial health (no 2025 accounts found) |
| **U-IMCEC** | Mutualist union; no recent data | Secondary |
| Islamic MFIs | 3 Islamic MFI licences in 2023 (one in SN); Bouchra Microfinance SA joined in Q4 2025 (name suggests Islamic, **[UNVERIFIED]**) | For the Murabaha overlay |

## 11. Salary assignment and payroll deduction: the Senegal rules **[NEW, PRIMARY]**

**Labour Code (Loi 97-17 of 1 Dec 1997)**, read in the [eRegulations PDF](https://senegal.eregulations.org/media/t-loi-portant-code-travail%201.pdf):
- **Art. L.130:**
  - Permitted deductions are mandatory levies, repayments of assignments (*cessions*) made under the regulations, and consignments under collective agreements.
  - **Loans or advances by the employer to an employee are capped at six times the *quotité cessible***.
  - Repayment of employer cash advances may be deducted only through *saisie-arrêt* or a *cession volontaire* made under **Code de procédure civile arts. 571-1 to 571-6**.
  - **"Les acomptes sur salaire déjà acquis ne sont pas considérés comme avances."**
- **Art. L.131:** "Les portions de salaire … soumises à prélèvements progressifs et les taux y afférents sont fixés par l'**article 381 du Code de procédure civile**." The deduction base is gross pay as defined in L.118, less the art. 381 deductions.
- **Art. L.132:** any other deduction clause in a collective agreement or contract is void.

**Code de procédure civile** (read in the [eRegulations PDF](https://senegal.eregulations.org/media/cpc[1].pdf)):
- **Art. 381:** salaries and public pay may be seized only for the following portion of the monthly base:
  - 10% up to 20,000 FCFA
  - 20% from 20,001 to 30,000
  - 30% from 30,001 to 100,000
  - 40% from 100,001 to 200,000
  - **100% above 200,000 FCFA**
  - An additional equal portion applies for hospital debts and main-home housing loans.
  - Base: gross pay with all allowances, *less* taxes and compulsory levies withheld at source, expense allowances, family benefits, and allowances declared unseizable.
  - **Total deductions of any kind, including voluntary assignments, may never exceed two-thirds of the base**, even for maintenance debts.
  - Employees paid into a current, deposit or advance account may withdraw the unseizable portion monthly, notwithstanding any garnishment.
- **Art. 571-1:** the assignable portions are identical to the art. 381 seizable portions.
- **Art. 571-2:**
  - A voluntary assignment of salary, whatever the amount or beneficiary, may be made **only by a declaration signed by the assignor in person before the president of the regional court** of their residence.
  - The declaration must state the debt, its cause and the per-pay deduction.
  - It must be accompanied by a court clerk's certificate on existing garnishments; otherwise the assignment is null.
- **Arts. 571-3/571-4:** the clerk registers the assignment and notifies the employer, or the **Trésorier général** for State salaries. The employer *must* then deduct and pay the assignee directly, and can be compelled by an immediately enforceable order.

Worked examples (calc.) of the maximum assignable amount on a monthly net base:

| Base | Maximum |
|---|---|
| SMIG 64,223 | ≈14,300 (22%) |
| 100,000 | 25,000 (25%) |
| 150,000 | 45,000 (30%) |
| 200,000 | 65,000 (32.5%) |
| 300,000 | 165,000 (55%) |
| 380,000 (formal average) | 245,000 (64.5%) |
| 500,000 | capped at the 2/3 limit, 333,333 |

The FCFA bands are old and not indexed, so above about 200k FCFA the legal ceiling is very loose.

**[CONFLICT/UNVERIFIED]** A 2023 MAGP law-firm newsletter says art. 381 was abrogated but is still applied in practice for lack of a replacement ([MAGP](https://magp.sn/wp-content/uploads/2023/02/Newsletter_Droit_du_Travail_optimise_compressed.pdf)). OHADA AUPSRVE art. 177+ governs the procedure for wage garnishment and refers to national law for the portions. Get counsel confirmation.

Comparison with Côte d'Ivoire: CI's Decree 2014-370 sets the *quotité saisissable* at 33% and the *quotité cessible* for loans from licensed lenders on a 35–57% sliding scale.

Implications for product design (inference; needs counsel):
- **The legal cap will not be the binding constraint for most formal salaries; prudence is.** Set an internal affordability rule, for example total debt service ≤ 33–40% of net pay, mirroring bank practice, and note that the legal ceiling is 2/3.
- **The formal *cession volontaire* route is impractical at scale** because of the court declaration. In practice lenders rely on:
  1. **salary domiciliation** in an account they control, with an automatic sweep on salary credit;
  2. an **employer tripartite agreement** with an irrevocable instruction to pay the salary into the domiciled account; and
  3. for civil servants, Treasury/Solde deduction codes held by banks and SFDs.
- **Earned-wage access:** because "acomptes sur salaire déjà acquis" are *not* advances, an **employer-paid acompte on already-earned wages** can be netted on payday without saisie/cession formalities. One possible structure: Jokko's partner SFD funds the employer's treasury, or factors the payroll receivable, and the employer pays the acompte through Jokko. That is arguably not consumer credit to the employee, which may avoid the 24% TEG problem for short advances. Lender-funded advances to the employee are credit and fall under the 24% (SFD) or 14% (bank) all-in cap: 6% for 15 days, as Fintra charged, is about 146% annualised and not permitted. **Counsel must confirm.**
- Employer loans/advances are capped at **6× the quotité cessible**, a useful reference for advance sizing.

## 12. What a Senegalese/WAEMU bank (or SFD) will ask of a fintech partner

**Regulatory drivers the bank must satisfy:**
- **Outsourcing (BCEAO Instr. 001-01-2024, arts. 3, 7, 28, 36–37) [PRIMARY]** ([BCEAO PDF](https://www.bceao.int/sites/default/files/inline-files/Instruction-No001-01-2024_relative_aux_services_de_paiement_dans_l-UMOA.pdf)):
  - Partnerships are allowed subject to outsourcing rules; **exclusivity clauses are banned** (art. 7).
  - Outsourcing a *critical operational function* requires **30 days' prior notice to the BCEAO and the Commission Bancaire** (art. 28), as does launching a new product.
  - Art. 36: outsourcing must not impair internal control or supervision, must not reduce customer protection, and all data must be available at all times; the PSP must assess the opportunity and risks first. The Commission Bancaire **may order an external audit of the provider**, and data must be securely deleted at termination.
  - Art. 37 mandatory contract clauses: exhaustive scope and costs; rights and obligations; reporting nature and frequency; assets the provider may use (data, software, IP); termination and asset return; business continuity; KPIs reviewed at least annually; personal data, professional secrecy and IP clauses.
  - These articles are written for EPs. Banks follow analogous Commission Bancaire governance and internal-control circulars (01-2017 to 05-2017/CB/C, applied since 2 Jul 2018); the outsourcing text for banks was not retrieved.
- **Agents (arts. 38–40):** if Jokko touches customers for a licensed PSP before its own licence, it must be **registered by the BCEAO as an agent** (30-day review).
  - The file includes identity, the contract, AML internal-control mechanisms, and the fitness and probity of managers.
  - The principal stays fully liable and must monitor the agent's AML and outsourcing compliance.
- **AML/CFT:**
  - Senegal Law 2024-08 (14 Feb 2024, JORS 20 Mar 2024) transposes UEMOA Directive 01/2023 ([vie-publique](https://www.vie-publique.sn/documents/348/JO-7716-du-20-mars-2024); [Financial Afrik](https://www.financialafrik.com/2024/09/11/tribune-la-nouvelle-loi-relative-a-la-lutte-contre-le-blanchiment-de-capitaux-au-senegal-et-dans-la-zone-uemoa)).
  - **BCEAO Instruction 001-03-2025 (18 Mar 2025)** expressly covers **"entreprises de technologie financière ou FinTech"** alongside banks, EMEs and EPs ([CB-UMOA PDF](https://www.cb-umoa.org/sites/default/files/2025-08/Instruction%20n%C2%B0001-03-2025%20du%2018%20mars%2025%20portant%20modalit%C3%A9s%20de%20mise%20en%20oeuvre%20par%20les%20IF%20de%20leurs%20obligations%20en%20mati%C3%A8re%20de%20lutte%20contre%20le%20blanchiment%20de%20capitaux.pdf)) **[NEW, PRIMARY]**. It requires:
    - board-approved AML strategy, risk assessment and policies;
    - a dedicated AML function reporting to the CEO (merged with compliance/risk if small);
    - an information system able to profile customers, **screen clients and transactions in real time**, generate alerts, aggregate balances per client and detect suspicious transactions, with sanctions-list updates applied "sans délai" and the system reviewed annually;
    - profile updates within one month; staff training; annual independent audit;
    - an **annual AML implementation report to the BCEAO within 2 months of year-end**;
    - STRs to CENTIF.
  - It replaces Instruction 007-09-2017.
  - CENTIF Senegal received 928 STRs in 2024 (+15%) ([La Nouvelle Tribune](https://lanouvelletribune.info/2025/09/senegal-blanchiment-et-rapport-centif-2024-hausse-des-declarations-et-nouveaux-defis/)).
  - Senegal left the FATF grey list in 2024: October per the earlier notes, June per one search summary **[CONFLICT; Oct 2024 most likely]**. It was removed from the EU high-risk list in Jun 2025.
- **Data protection:** CDP declaration or authorisation under Law 2008-12 (reform still in draft); hosting and cross-border transfer questions.
- **Card schemes:**
  - **Visa Third-Party Agent registration:** the issuer must perform due diligence *before registration and annually* on the agent's business model, financial condition, background, and **PCI DSS/PIN compliance**; registration is filed by the issuer in Visa Membership Management ([Visa TPA overview](https://www.visa.ca/content/dam/VCOM/regional/na/canada/security/security-documents/third-party-agent-registration-overview-english.pdf)).
  - **Mastercard Service Provider Registration:** filed by the principal member bank **before** the provider supports any programme; annual PCI AOC; fees apply ([Mastercard SPR FAQ](https://www.mastercard.com/content/dam/public/mastercardcom/globalrisk/pdf/Service%20Provider%20Registration%20%20PCI%20FAQs%20(6%20September%202023).pdf)).
  - Exact fees were not found.
  - 96.7% of UEMOA cards were reported PCI DSS-compliant in 2023 ([Droit Médias Finance](https://www.droitmediasfinance.com/index.php/actualites/droit-tech-fintech/888-uemoa-gim-uemoa-sur-8-millions-de-cartes-bancaires-en-circulation-en-2023-96-7-en-conformite-avec-la-norme-pci-dss)), so banks will expect the same.

**Practical due-diligence and onboarding checklist a Senegalese bank or SFD will run** (synthesis of the above plus standard practice; exact lists are bank-specific and unpublished):
1. **Corporate:** statutes, RCCM, NINEA, tax and social clearance (attestation de régularité fiscale/IPRES/CSS), audited accounts or management accounts, cap table and **UBO declaration** (PEP and sanctions screening of founders and directors), board composition, proof of address, **business plan with 3-year volumes**.
2. **Regulatory status and roadmap:** EP/EME application status (filing receipt), BCEAO agent registration if applicable, legal opinion on the model, product notices to BCEAO (30 days), and evidence the fintech will not hold client funds. Funds must sit in the bank's or licensed partner's ring-fenced/trust account.
3. **AML/CFT programme mapped to Instr. 001-03-2025:** policy, risk assessment, KYC/KYB tiers, real-time sanctions/PEP screening vendor, transaction monitoring rules, STR escalation to the partner's AMLCO and CENTIF, record keeping (10 years under the uniform law), training logs, named AML officer.
4. **Information security:** PCI DSS (SAQ-D or ROC if storing or processing PAN; otherwise tokenised via the processor), ISO 27001 roadmap, pen-test reports, access controls, encryption, incident response, BCP/DRP with RTO/RPO, data-location map (servers abroad need justification) and CDP formalities.
5. **Outsourcing-contract terms (art. 37):** SLAs/KPIs, audit and access rights for the bank, the Commission Bancaire and the BCEAO, data ownership, exit and reversibility, sub-processor list (KYC vendor, cloud, processor), professional secrecy.
6. **Operations:** reconciliation and safeguarding process, complaints handling, fraud and chargeback procedures, customer T&Cs naming the issuer (EME Instr. art. 4 requires marketing to name the issuing institution), and a customer-funds flow diagram.
7. **Financial commitments (typical, not Senegal-sourced):** setup or integration fee; **collateral or prefunding deposit** sized on net settlement exposure (cards) or average daily payouts (payouts); minimum monthly fees or volumes; **interchange revenue share** (issuer keeps a slice; fintech gets most if it bears costs); per-card and per-transaction processing fees; first-loss cash collateral for any credit programme (5–20% of portfolio in the earlier lending notes) ([practitioner wiki [SECONDARY]](https://wiki.private.law/en/bin-sponsorship.md)). No Senegalese term sheet was found; **get quotes from 3+ banks**.
8. **Credit partnership (SFD):** credit policy and scorecard, pricing proof that the all-in TEG is ≤24%, collection mechanics (domiciliation and employer agreements), reporting to the BCEAO credit bureau (BIC), first-loss and risk-sharing, provisioning, and partner-branded loan contracts.

**Realistic partners and why:**
- **Ecobank Sénégal** is the path of least resistance for cards and PI-SPI API access.
  - Proven fintech card sponsor (Wave, Mixx, Djamo SN), present in all 8 WAEMU countries on PI-SPI's API Business tier, with an in-house issuing stack and the Hub2 MoU.
  - Downside: Jokko becomes one of many, and Ecobank serves competitors.
- **SUNU Bank Sénégal (ex-BICIS):** a newly renamed challenger aiming for the top 3 with an SME and corporate legacy, likely to value payroll and SME deposit inflows. Private APIs are reported. A good candidate for **RIB accounts plus payroll domiciliation**.
- **Bank of Africa Sénégal:** already white-labels Julaya's bulk payments in CI and is profitable (+101% net profit 2025). It understands the "bank-distributes-fintech" model.
- **BNDE (state-majority):** SME and inclusion mandate, diaspora ambitions (Kopar), and the likely acquirer of SG SN. Political tailwind for a local fintech, but slower and politically exposed.
- **Banque Islamique du Sénégal:** #3 and growing fast, with an IFC Murabaha line for MSMEs and a fintech-islamique hiring signal. A natural partner for an **Islamic payroll account or Murabaha advance**.
- **Orange Bank Africa:** fast-growing in SN, but a direct competitor (Tik Tak). Partner only for rails.
- **SFDs for salary advance:**
  - **Baobab Sénégal** (digital nano-loans, wallet integration, IFC backing, PAR30 about 2%) is first choice.
  - **PAMECAS** (scale plus an Islamic window).
  - **Cofina** (SME méso-finance, fintech partnerships, securitisation).
  - **CMS** (largest network, deposits, payroll-loan culture; slower).
  - All except CMS are already PI-SPI participants or digitally active **[partly UNVERIFIED]**.

## 13. Diaspora and remittances

- 2024 remittances: **2,211bn FCFA (≈€3.37bn), ≈12% of GDP** ([Launch Base Africa](https://launchbaseafrica.com/2026/03/19/bceao-opens-a-new-playbook-for-west-african-fintechs-in-diaspora-banking/)). WDI gives US$3.27bn, 10.6% of GDP (2023). One source claims more than 2,800bn FCFA in 2025 ([Senego [UNVERIFIED]](https://senego.com/dossier/transferts-argent-senegal)).
- Inbound international transfers into wallets (2024): **27.4M transactions / 1,700.8bn FCFA**, which is **64% of UEMOA inbound** ([BCEAO SFN 2024](https://www.bceao.int/sites/default/files/2026-03/Rapport%20annuel%20sur%20les%20services%20financiers%20num%C3%A9riques%20dans%20l'UEMOA%20-%202024.pdf)).
- **Diaspora stock:**
  - About 694k Senegalese abroad (UN DESA 2020).
  - RGPH-5 (2024) counts 166,561 emigrants over 5 years: France 34,434, Italy 25,442, Spain 24,823, Morocco 13,375, Mauritania 11,601. 71.9% left for work ([search summary of Senego/ANSD](https://senego.com/plus-de-senegalais-quittent-le-pays-que-detrangers-ny-entrent-voici-les-pays-qui-accueillent-le-plus-de-senegalais_1721760.html)) **[NEW]**.
  - OECD inflows rose from 9,700 a year (2000) to 23,500 (2019); Spain > Italy > France ([OECD](https://www.oecd.org/fr/publications/panorama-de-l-emigration-senegalaise_0e279cfb-fr/full-report/component-4.html)).
- **BCEAO Notice 001-03-2026 (signed 13 Mar 2026):**
  - WAEMU diaspora members may open and hold local FCFA **bank** accounts from abroad on the same terms as residents.
  - Two cumulative conditions: a WAEMU passport or national ID, **plus** proof of ties (residence certificate, domicile, or a civil-status document showing direct family ties to a resident).
  - AML rules remain in force. Outflows remain under FX Regulation 06/2024.
  - The article does not say whether EMEs or SFDs are covered ([Launch Base Africa](https://launchbaseafrica.com/2026/03/19/bceao-opens-a-new-playbook-for-west-african-fintechs-in-diaspora-banking/)).
  - **[CONFLICT]** CB-UMOA Instruction 009-07-2025 requires prior approval for non-resident accounts. The notice treats diaspora nationals as residents for account purposes, which needs counsel.
- France→Senegal corridor costs are already low (2.5–5% for €200). Taptap Send is reportedly fee-free to Wave/OM. The wedge is the receiving **account**, not price.

## 14. Islamic finance demand

- **BIS rose to #3 of 29 banks** with a 1,291bn FCFA balance sheet at end-2025 and an 89% financing/deposit ratio against a 74% sector average. The balance sheet has roughly doubled since 2020 (see §9). BIS plus Banque Islamique du Niger hold about 1.6–1.8% of UEMOA bank assets or deposits ([Droit Médias Finance](https://www.droitmediasfinance.com/index.php/actualites/finance-islamique/1370-finance-islamique-la-banque-islamique-du-senegal-et-la-banque-islamique-du-niger-ne-pese-quenviron-1-7-des-actifs-bancaires-totaux-de-lumoa-en-2025)) **[NEW]**.
- IFC's US$40M Murabaha facility to BIS (Oct 2025) was described as the World Bank Group's first Islamic-finance operation in sub-Saharan Africa **[NEW]**.
- Framework:
  - Senegal Law 2019-06 integrates Islamic finance into the SFD law. BCEAO Instructions 003-03-2018 and 005-05-2018 cover Islamic SFD operations.
  - 18 Islamic authorisations UEMOA-wide in 2023, including 3 new Islamic MFI licences (one in SN).
  - Senegal players: BIS, CBI Baraka (Coris), PAMECAS DEFI.
- Demand is not measured by survey, but BIS's growth is strong revealed demand. An **interest-free payroll account plus a Murabaha purchase advance** is a credible SN differentiator.

## 15. Political and regulatory climate for fintech, 2025–26

- **The fiscal stance is aggressive on digital flows** (TTA plus merchant withholding). Consumer associations and operators have lobbied for revision, with no change found. The GSMA rates the tax burden high.
- **Pro-digital rhetoric:**
  - New Deal Technologique (Feb 2025; operational phase Mar 2026: sovereign cloud and connectivity).
  - SenTrésor (G2P digitisation).
  - DGID digital payments via Max it, SenTimbre.
  - CSS benefits via Wave.
  - The government is building digital *public* rails while taxing *private* ones.
- **Sovereignty theme:** the push to take control of foreign banks (SG SN), CFA criticism, and an emphasis on "national champions". A Dakar-founded, Senegalese-led fintech can benefit (Startup Act label, DER/FJ, public procurement access) but should avoid looking like a foreign extraction play.
- **BCEAO enforcement is strict:**
  - Licensing deadline of 1 Sep 2025; PI-SPI mandatory from 2 Nov 2026.
  - Mali's DGCC disciplined Wave for absorbing a levy.
  - The BCEAO is debating a digital-bank category.
  - The BCEAO's BCSF-UEMOA fintech office (Decision 192-11-2021) is the regulatory engagement channel.
- **Startup Act (Loi 2020-01 of 6 Jan 2020):**
  - Label for innovative firms under 8 years old, majority Senegalese-owned, with capped capital.
  - Art. 8 incentives: customs, social and tax advantages; credit guarantees; public/private funding; access to public procurement; capacity building ([Droit Médias Finance](https://droitmediasfinance.com/index.php/actualites/droit-tech-fintech/55-senegal-une-loi-pour-encadrer-les-startups-economie-du-texte)).
  - Implementing texts took about 5 years. A vendor claims a 3-year corporate-tax exemption, turnover under 5bn FCFA and fewer than 50 staff ([Kolonell [VENDOR, UNVERIFIED]](https://kolonell.com/fr/blog/impot-societes-exoneration-startup-label-senegal-3-ans-2026)).
  - **Check the label against Jokko's cap table** (majority Senegalese ownership).
- **Fintech association:** no clearly identifiable Senegal fintech association was found. The Next Fintech Forum (Dakar, Nov 2025) and the DER/FJ ecosystem (about 200 startups) are the convening venues **[GAP]**.

## 16. Senegal B2C in 2–3 years (2028–29): what will likely have changed

- **P2P will be free or near-free** (PI-SPI from Nov 2026; cross-border UEMOA from Jun 2027). Wave's 1% P2P fee is under pressure on interoperable flows, though on-us transfers are not regulated. Monetisation shifts to credit, savings spread, interchange and subscriptions.
- **Wave will likely have launched credit and savings** (announced Feb 2026) and may seek a bank or digital-bank status in SN. With about 80% of float and cash-flow data on 8M+ users, Wave becomes the default nano-lender and saver unless the BCEAO rules otherwise.
- **Orange Bank Africa** will keep compounding (557k SN accounts in 2025, from almost zero).
- **Djamo** will likely have closed its Series C and expanded its SN business offer, salary domiciliation and credit (perhaps an SN SFD licence).
- **Regulation:** a possible BCEAO "digital bank" category; a non-resident/diaspora account framework clarified; maybe a national e-ID API (New Deal); usury caps at 14%/24% persisting; TTA possibly widened or adjusted.
- **Macro:** if the IMF programme is approved and executed, growth recovers toward 4–5% by 2028 with oil and gas (speculative). If not, arrears and austerity weigh on consumer credit quality.
- **Entry angles that should still be open:**
  1. **Converting the B2B base:** the employee salary-account base built in years 1–2 is the cheapest B2C acquisition channel.
  2. **The primary account with an IBAN** plus a real debit card that works on Apple Pay, Netflix and Meta ads.
  3. **Salary-backed instalment credit** above nano-loan sizes.
  4. **The diaspora family account** under Notice 001-03-2026.
  5. **Islamic/ethical accounts and Murabaha.**
  6. **Yield savings** backed by UMOA-Titres or BRVM T-bills via an SFD or bank partner (attractive while the State pays high domestic yields).

## 17. Remaining gaps and uncertainties

- **Art. 381 CPC status:** possible abrogation (MAGP 2023) and the current applicable barème. Whether employer *acomptes* funded by a third party escape credit characterisation. **Needs Senegalese counsel.**
- **Payroll deduction codes for civil servants** (Direction de la Solde/Trésor): the process for SFDs and fintechs was not found.
- **E-invoicing:** no official DGID arrêté or calendar.
- **SG Sénégal sale:** current status (pending vs closed) not confirmed.
- **Bank BaaS terms in Senegal:** no published setup fees, collateral or revenue shares. Julaya's Senegal sponsor bank, Djamo SN's exact issuing bank, and Naboopay's licence status are unconfirmed.
- **SFD institution-level 2025 data** (CMS, PAMECAS, ACEP, Baobab SN, Cofina SN): only dated or vendor numbers.
- **TTA:** actual collection status, receipts, and treatment of PI-SPI transfers.
- **IPRES/CSS** acceptance of electronic or mobile payment of contributions.
- **SMIG:** confirm 64,223 FCFA in the JO (Decree 2023-1710).
- **Mobile money 2025 country data:** the BCEAO SFN 2025 report has not yet been reviewed.
- **FATF delisting date** (Jun vs Oct 2024).
- **Diaspora notice scope** (banks only vs EMEs/SFDs) and its interaction with Instruction 009-07-2025.
- **Senegal Fintech Association** existence and contacts.
