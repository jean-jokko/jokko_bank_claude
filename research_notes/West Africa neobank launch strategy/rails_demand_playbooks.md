# Rails, Demand Signals and Neobank Playbooks for a Francophone West/Central Africa Neobank (as of October 2026)

Scope note: research run 8 Oct 2026. Evidence is thinner for CEMAC/Cameroon than for WAEMU (Côte d'Ivoire/Senegal). Several commercial-blog sources (notably kolonell.com, which sells integration/structuring services) are used only for order-of-magnitude pricing and are flagged as such.

---

## A1. BCEAO PI-SPI (instant payments): launch, participants, fees, QR, alias, competitive impact

### Takeaway
PI-SPI went live on 30 Sep 2025 and, by a BCEAO communiqué of 2 Oct 2026, becomes **mandatory for all interoperable e-money transactions in WAEMU from 2 Nov 2026**, with free sending up to 8,000 FCFA/day per user per participant, fees capped at 0.8% above that, and free receiving. P2P transfer fees are being regulated toward zero, so a new entrant cannot win on "cheaper transfers"; the opening is in products built *on top* of PI-SPI (merchant QR acceptance, business payments/API, savings, credit, reconciliation).

### Cited Findings
- Official launch 30 Sep 2025 in Dakar; available 24/7 in all 8 WAEMU countries; standardized QR for universal merchant acceptance; banks, e-money institutions (EMEs) and microfinance institutions connected; individuals get free access to their funds "through any channel or institution"; built in-house by BCEAO — [BCEAO launch page](https://www.bceao.int/fr/content/lancement-officiel-de-la-plateforme-interoperable-du-systeme-de-paiement-instantane-pi-spi)
- Same BCEAO page: WAEMU electronic payments grew from 260 million (2014) to >11 billion (2024) transactions; estimated financial inclusion 74% — [BCEAO](https://www.bceao.int/fr/content/lancement-officiel-de-la-plateforme-interoperable-du-systeme-de-paiement-instantane-pi-spi)
- Participants at launch: 62 institutions authorized per press reporting of BCEAO list — [Financial Afrik, 6 Oct 2025](https://www.financialafrik.com/2025/10/06/pi-spi-liste-des-62-institutions-autorisees-par-la-bceao-a-ouvrir-les-services-au-public-dans-luemoa/); contradicted by Launch Base Africa which says 31 at launch and >70 by Feb 2026 — [Launch Base Africa](https://launchbaseafrica.com/2026/03/24/the-267bn-crown-wave-edges-closer-to-dethroning-orange-in-west-africa/). Official BCEAO list: [BCEAO participant list 30 Sep 2025](https://www.bceao.int/fr/communique-presse/liste-des-participants-autorises-ouvrir-les-services-de-pi-spi-au-public-30-sept-2025)
- 80 institutions as of 2 Apr 2026 (Senegal 20, Côte d'Ivoire 18) — [FinancesAO](https://financesao.com/bceao-pi-spi-participants-autorises-avril-2026/)
- 175 institutions authorized as of 30 Sep 2026 (up from 104 two months earlier); >38 million people have access; Senegal 43, Côte d'Ivoire 38, Burkina 20, Mali 19 — [Financial Afrik, 4 Oct 2026](https://www.financialafrik.com/2026/10/04/la-bceao-rend-pi-spi-obligatoire-revoit-ses-tarifs-et-pose-enfin-la-question-de-nouveaux-services-financiers-adosses-a-la-plateforme/); [Dakar92](https://dakar92.com/bceao-etablit-les-regles-du-jeu-economique-5-octobre-2026/)
- **Wave Côte d'Ivoire** was absent from the 31 Jul 2026 list and present on 30 Sep 2026; Wave and Moov joined Orange Money and MTN MoMo, so all four major CI wallets are now on PI-SPI — [Jeune Afrique](https://www.jeuneafrique.com/1848345/economie-entreprises/paiement-instantane-wave-rallie-la-plateforme-de-la-bceao-et-acte-une-nouvelle-ere-pour-lunion-monetaire/); [allAfrica](https://allafrica.com/stories/202610050727.html)
- **New rules (BCEAO communiqué 2 Oct 2026):** from 2 Nov 2026, interoperable e-money transactions in WAEMU must go "exclusivement" via PI-SPI; national transfers free up to 8,000 FCFA cumulative per user per participant per day (no limit on number) — BCEAO says this covers ~75% of WAEMU e-money transactions; above that, 0%–0.8% (excl. tax); receiving free with no limit; cross-border intra-WAEMU sending aligned to same conditions only **from 1 June 2027** (until then priced freely by each institution) — [Financial Afrik](https://www.financialafrik.com/2026/10/04/la-bceao-rend-pi-spi-obligatoire-revoit-ses-tarifs-et-pose-enfin-la-question-de-nouveaux-services-financiers-adosses-a-la-plateforme/); [AITN](https://afriqueitnews.com/finance/pi-spi-la-bceao-plafonne-la-gratuite-des-transferts-interoperables-a-8-000-fcfa/); [Senego](https://senego.com/bceao-pi-spi-obligatoire-envois-nationaux-gratuits-jusqua-8-000-fcfa-cumules-jour-usager_2009226.html)
- Search-summary reporting (not directly verified) says the reform removes a former rule charging 1% on receipts after 30 monthly operations — [AITN](https://afriqueitnews.com/finance/pi-spi-la-bceao-plafonne-la-gratuite-des-transferts-interoperables-a-8-000-fcfa/)
- **API Business** tier (approved list for programmatic products) had only 24 names in mid-Sep 2026; Ecobank is the only one present in all 8 countries; others mostly CI and Senegal. BCEAO lists four target audiences: individuals, businesses, financial institutions, the State — [Financial Afrik](https://www.financialafrik.com/2026/10/04/la-bceao-rend-pi-spi-obligatoire-revoit-ses-tarifs-et-pose-enfin-la-question-de-nouveaux-services-financiers-adosses-a-la-plateforme/)
- The same Financial Afrik op-ed argues free national transfers remove the direct profitability of connecting to PI-SPI (transfer and withdrawal fees long a "significant share" of revenues) and that products on PI-SPI will need other revenue: credit, micro-insurance, programmed savings, SME treasury/reconciliation; Visa estimate (via Forbes Afrique) that full interoperability could add up to $12bn/yr transactional value in West Africa — [Financial Afrik](https://www.financialafrik.com/2026/10/04/la-bceao-rend-pi-spi-obligatoire-revoit-ses-tarifs-et-pose-enfin-la-question-de-nouveaux-services-financiers-adosses-a-la-plateforme/)
- **Alias:** central alias directory (RAC); alias types include a platform-generated 36-character "SHID", phone number, or payment address; directory shows recipient name and country before payment — [PI-SPI alias page](https://pispi.bceao.int/lalias); [PI-SPI developer guide](https://developer.pispi.bceao.int/guides/alias-overview)
- **QR:** EMV-based payload; PI-SPI octagon logo; static QR, static QR with fixed amount, dynamic QR per transaction (requires unique TxID), and P2P "transfer QR"; merchant needs an active PI-SPI alias with its institution; BCEAO publishes a sandbox and QR SDK — [PI-SPI QR guide](https://developer.pispi.bceao.int/guides/qr-generation); [PI-SPI sandbox](https://developer.pispi.bceao.int/); [pub.dev bceao_pispi_qrcode](https://pub.dev/packages/bceao_pispi_qrcode)
- Market context: WAEMU mobile money 2024 = 11bn transactions worth 160,415bn FCFA (~$267bn, 119% of GDP); 248m accounts opened but only 76.8m active (31%, down from 45% in 2020); 88% of wallet deposits withdrawn as cash; registered merchants 3.7m (CI 2.72m); merchant share of mobile payment volume 23.3% (vs 3.3% in 2020); banks' share of volume 18%; bank–fintech partnerships 52 (source: BCEAO Annual Report on DFS 2024, published Jan 2026) — [Launch Base Africa](https://launchbaseafrica.com/2026/03/24/the-267bn-crown-wave-edges-closer-to-dethroning-orange-in-west-africa/)
- Market shares by value 2024: Orange Money 41.3%, Wave 38.2%, MTN 11.7%, Moov 2.6% (by volume: Orange 38.4%, Wave 23%) — [Launch Base Africa](https://launchbaseafrica.com/2026/03/24/the-267bn-crown-wave-edges-closer-to-dethroning-orange-in-west-africa/); a different secondary summary gives Wave 28.4% of transaction volume in 2024 (21.4% in 2023) and Orange 38.4% — [Seneweb](https://www.seneweb.com/en/news/Economie/mobile-money-why-the-orange-money-wave-duel-no-longer-sums-up-the-market_n_505004.html) (figures conflict; likely value vs volume definitions)
- Orange Money Senegal reportedly removed transfer fees, keeping a 1% withdrawal fee capped at 5,000 FCFA (per a Senegalese MP, early 2026) — [Launch Base Africa](https://launchbaseafrica.com/2026/03/24/the-267bn-crown-wave-edges-closer-to-dethroning-orange-in-west-africa/)

### Inferences
- With P2P sending largely free up to 8,000 FCFA/day and receiving free, "free transfers" (the Wave/Kuda/OPay wedge) is now a regulatory baseline in WAEMU, not a differentiator. A neobank that joins PI-SPI (directly, via a licensed partner, or via an API-Business participant) instantly reaches every wallet/bank account by phone alias — this neutralizes the closed-loop network effect that Wave/Orange enjoyed.
- Revenue must come from: (a) merchant acceptance (QR) MDR, (b) above-threshold transfers (≤0.8%), (c) cross-border intra-WAEMU until June 2027, (d) cash-out (still a fee line for wallets), (e) credit/savings/FX/subscriptions.
- The very small API Business list (24 in Sep 2026) suggests B2B tooling on PI-SPI (bulk payouts, collections with reconciliation, request-to-pay-like flows) is early and under-served.
- Low activation (31%) and 88% cash-out show the problem is not access but *keeping money digital*; features that keep balances in-app (savings vaults, bill pay, merchant QR, salary) address the real gap.

### Gaps
- No public PI-SPI transaction volume/value data found as of Oct 2026.
- Whether PI-SPI supports request-to-pay / direct debit / scheduled payments was not confirmed from official docs.
- Exact conditions for a non-licensed fintech to access PI-SPI (indirect participation via sponsor) not found.
- The "1% after 30 operations" prior receiving-fee rule not verified against a primary BCEAO text.

---

## A2. Cards: GIM-UEMOA, Visa/Mastercard issuing for fintechs, processors, declines

### Takeaway
Card issuing in francophone West Africa is bank-centric: fintechs (Djamo, Wave, Wizall, Money Fusion) issue Visa/Mastercard prepaid/virtual cards through local partner banks (e.g., Wave with Orabank, Wizall with Banque Atlantique). Locally issued BINs get better approval rates abroad than foreign-BIN cards. Virtual cards for international subscriptions are rapidly commoditizing (Wave offers one with no issuance/decline fees), so cards are an acquisition tool, not a margin source.

### Cited Findings
- WAEMU end-2023: >8 million cards (+7.9%), 6.3m bank-account cards, 1.6m prepaid (+16%), 1.2m contactless; 4,214 ATMs; 15,259 EFTPOS; 122 of 128 GIM-UEMOA members actively integrated; market is bank-centric with fintechs complementing banks — [Launch Base Africa, Nov 2024](https://launchbaseafrica.com/2024/11/20/in-francophone-west-africa-payment-cards-are-run-by-banks-not-fintechs/)
- Djamo works with local banks to issue "local" Visa cards; co-founder Hassan Bourgi: merchants' fraud algorithms favor locally issued cards, and partnering with a foreign bank could hurt approval rates — [Launch Base Africa](https://launchbaseafrica.com/2024/11/20/in-francophone-west-africa-payment-cards-are-run-by-banks-not-fintechs/)
- Wave partnered with Orabank to launch a Visa virtual card with no issuance or rejection fees; Wizall Money (BCP-owned) issues a prepaid card backed by Banque Atlantique; prepaid cards described as good for acquisition but becoming low-margin and commoditized — [Launch Base Africa, Sep 2025](https://launchbaseafrica.com/2025/09/12/facing-a-telco-onslaught-djamos-answer-is-now-a-banking-license-and-a-new-model)
- Wave virtual Visa available to all Wave CI customers; earlier reported limits of 500,000 FCFA per transaction and 2,000,000 FCFA/month international (possibly outdated); Money Fusion (2025) offers virtual USD Visa/Mastercard for Netflix/Facebook Ads/AWS across CI, SN, ML, TG, BF, BJ — [Digitalmag CI](https://digitalmag.ci/cote-divoire-la-carte-visa-virtuelle-wave-est-maintenant-accessible/); [Digitalmag CI – Money Fusion](https://digitalmag.ci/money-fusion-la-nouvelle-carte-virtuelle-qui-diversifie-loffre-en-cote-divoire/)
- GIM-UEMOA is a member of Visa and Mastercard; GIM prepaid co-brands exist (e.g., Baraka GIM-Mastercard by BMS Mali, Aug 2025; Benin Treasury regional prepaid card without bank account, Aug 2025) — [Financial Afrik](https://www.financialafrik.com/2025/08/18/la-banque-malienne-de-solidarite-bms-s-a-et-satguru-travel-lancent-des-cartes-prepayees-baraka-gim-mastercard-co-brandees-pour-faciliter-les-paiements-pour-les-voyageurs); [Osiris](https://osiris.sn/le-gim-uemoa-et-le-tresor-public-du-benin-lancent-la-premiere-carte-prepayee.html)
- Paymentology (issuer-processor) states direct connections to GIM-UEMOA, Visa and Mastercard and supports local wallet integrations — [Paymentology Africa](https://www.paymentology.com/demo-africa)
- Common decline causes (vendor-sourced, treat with caution): currency conversion issues, BIN blocks, bank restrictions on international e-commerce; Ivorian bank cards sometimes refused on Amazon/Shein — [Spendfigo guide](https://www.spendfigo.com/guides/amazon/cote-divoire); [Digitalmag CI](https://digitalmag.ci/6-facons-dutiliser-la-carte-virtuelle-en-cote-divoire/?amp=1)
- **Union54 (verify request):** suspended card operations in mid-2022 after a large chargeback-fraud episode (reported $1.2bn attempted chargebacks), triggering shutdowns of virtual dollar cards at Barter, Eversend, Klasha, Payday; it later pivoted to ChitChat and in 2024 partnered with Paymentology — no evidence of a 2024–25 shutdown found — [TechCrunch, Jul 2022](https://techcrunch.com/2022/07/18/african-fintechs-halt-virtual-dollar-cards-after-union54-chargeback-fraud-surge); [The Condia](https://thecondia.com/virtual-dollar-cards-shutdown-union54-alternative/)
- CEMAC: BEAC Instruction 008/GR/2019 limits use of cards outside CEMAC to current transactions within FX allocation thresholds: ATM/POS abroad free up to XAF 5m per trip with proof of travel; remote/online payments above XAF 1m per month per person require justification within 30 days (2019 thresholds; not confirmed current) — [Gabonreview](https://www.gabonreview.com/blog/cartes-de-paiement-le-guide-dutilisation-hors-cemac-de-la-beac); [Business in Cameroon](https://www.businessincameroon.com/finance/2706-9262-beac-caps-electronic-payments-and-withdrawals-outside-cemac)

### Inferences
- MVP card strategy: a locally issued (WAEMU BIN) virtual Visa/Mastercard via a partner bank, processed by a regional-capable issuer-processor (e.g., Paymentology) — needed for parity, not differentiation. Differentiation must be reliability (high approval rate on Meta Ads, Google, AWS, Apple, airlines), transparent FX, and good dispute handling.
- Union54 is a cautionary tale: card programs are exposed to chargeback fraud and BIN-sponsor risk; build fraud tooling and multi-sponsor redundancy.
- In CEMAC, online international card spend >XAF 1m/month triggers justification requirements — a compliance workflow feature (document upload) could itself be a value-add.

### Gaps
- No public data on WAEMU interchange rates (domestic or GIM-UEMOA) or on approval/decline rates by merchant category.
- Djamo's processor and sponsor bank are not publicly named.
- No data found on whether Nymcard actively serves WAEMU/CEMAC issuers.

---

## A3. Mobile money interoperability, APIs and aggregators — pay-in/pay-out costs

### Takeaway
Typical merchant collection costs in Côte d'Ivoire (2026, secondary sources) are ~1% via the Wave API, ~1.5–2% via Orange Money API, and ~1.5–3.5% via aggregators (Hub2, CinetPay), with volume discounts. PI-SPI mandatory routing from Nov 2026 should compress interoperable costs further.

### Cited Findings
- Estimated pay-in fees (CI, 2026): Wave API ~1.0%, settlement T+0/T+1, no setup fee; Orange Money API 1.5–2.0% (setup case by case); Hub2 1.8–2.5% (setup 0–100,000 FCFA; negotiable above 50m FCFA/month); CinetPay 2.5–3.5% in one table vs 1.5–2.5% plus fixed fees in others — [Kolonell comparison](https://kolonell.com/fr/blog/comparatif-frais-agregateur-paiement-hub2-semoa-cinetpay-cote-ivoire-2026); [Kolonell gateway guide](https://kolonell.com/en/blog/payment-gateway-cote-divoire-wave-orange-mtn-2026) (commercial blog; internally inconsistent figures)
- Wave pricing model: free deposits/withdrawals, 1% P2P fee; bill-payment fees shifted to businesses; incumbents previously charged 5–10% per transaction in Senegal and cut prices in response — [TriplePundit](https://triplepundit.com/2025/wave-mobile-money-cote-divoire/); [AfricaSignal Wave case study](https://africasignal.com/wp-content/uploads/2025/11/04_Wave-Analysis-of-the-Business-Model-of-a-High-Impact-Fintech-.pdf)
- Senegal applies (since late 2025) a tax on mobile money transfers of 0.5% of amount, capped at 2,000 FCFA, also on transfers received into wallets — [Les Afriques](https://lesafriques.com/en/2026/09/sending-money-to-senegal-fee-and-rate-comparison-2026/)
- Julaya (CI/SN B2B "neobank for companies") runs bulk payments through all mobile money channels — [Africa Private Equity News](https://www.africaprivateequitynews.com/p/speedinvest-leads-5m-investment-round-for-west-african-fintech-company)

### Inferences
- A business-account product can sell "one API/dashboard to collect and pay out across Wave, Orange, MTN, Moov and banks via PI-SPI" — but aggregator margins (~1–2 pts above direct) will compress as PI-SPI becomes mandatory; the value shifts to reconciliation, invoicing, payroll and treasury rather than raw connectivity.
- Pay-out costs (disbursement to wallets) were not reliably found; assume they are similar or lower than pay-in and negotiable at volume.

### Gaps
- No official rate cards for Hub2, CinetPay, Bizao, Intouch, Wave Business or Orange; no data at all found on Bizao or Intouch pricing; no CEMAC (Cameroon: MTN/Orange) aggregator pricing.

---

## A4. Multi-currency: FCFA peg, EUR/USD accounts for residents, stablecoins, ECO

### Takeaway
Resident foreign-currency accounts are restricted in both zones: WAEMU (Règlement 06/2024/CM/UEMOA, in force with 15 implementing instructions since 1 Aug 2025) requires prior authorization of the Finance Minister after BCEAO concurring opinion; CEMAC (Règlement 02/18, in force March 2019) treats resident FX accounts as exceptional and requires BEAC authorization. A mass-market "EUR/USD account for residents" is therefore not feasible as an MVP; feasible alternatives are FCFA accounts with good FX-at-spend on cards, and non-resident (diaspora) products — though non-resident accounts now also need BCEAO prior approval. Crypto/stablecoins are unregulated (no framework) in WAEMU; the ECO remains officially targeted for 2027 but widely doubted.

### Cited Findings
- WAEMU Règlement 06/2024/CM/UEMOA art. 7: opening by residents of domestic foreign-currency accounts or accounts abroad requires prior authorization of the Minister of Finance after concurring opinion of BCEAO, under Annex II conditions; residence based on centre of predominant economic interest — [Règlement 06/2024 (Lextenso PDF)](https://www.labase-lextenso.fr/sites/lextenso/files/lextenso_upload/l_regl._ndeg_062024cmuemoa.pdf); [Financial Afrik, Mar 2026](https://www.financialafrik.com/2026/03/24/reglement-06-2024-uemoa-ce-qui-change-vraiment-pour-les-banques-et-les-entreprises/)
- 15 implementing instructions in force from 1 Aug 2025 (incl. 001-07-2025 general application; 009-07-2025 on non-resident foreign accounts) — [Regafrik](https://regafrik.com/actualites/panorama-reglementaire-uemoa-2024-2026); [CB-UMOA instruction 09/07/2025](https://cb-umoa.org/sites/default/files/2025-08/Instruction%20n%C2%B0%2009%2007%202025%20RFE%20relative%20aux%20conditions%20d'ouverture%20et%20aux%20modalit%C3%A9s%20de%20fonctionnement%20des%20comptes%20%C3%A9trangers%20de%20non%20r%C3%A9sidents.pdf)
- Any account opening for non-residents now requires prior BCEAO approval regardless of currency; foreign-currency accounts can only be credited in their own currency; residents must surrender to an authorized intermediary FX revenues received from outside WAEMU or paid by a non-resident; reported annual authorization (unverified in text) — [Challenges Économiques](https://challengeseconomiques.com/?p=8539); [Financial Afrik, Jan 2025](https://www.financialafrik.com/2025/01/09/nouveau-reglement-relatif-aux-relations-financieres-exterieures-des-etats-membres-de-luemoa-entre-ouverture-au-reste-du-monde-et-preservation-de-la-valeur-de-la-monnaie-commune/)
- FCFA–EUR fixed parity 655.957 (visible in World Bank RPW corridor data showing rate 655.96 for France→Senegal) — [World Bank RPW record](https://remittanceprices.worldbank.org/node/382753)
- CEMAC: Règlement 02/18 (adopted 21 Dec 2018, in force 1 Mar 2019); residents should not hold FX accounts save exceptionally; resident legal entities need BEAC authorization; 2,188 resident FX accounts (~XAF 92.3bn) found at end-Feb 2019 and banks told to regularize — [Gabonreview](https://www.gabonreview.com/blog/cemac-2%E2%80%89188-comptes-en-devises-ouverts-dans-lillegalite); [Deloitte Avocats](https://blog.avocats.deloitte.fr/cemac-nouvelle-reglementation-changes/); [BEAC Règlement 02/18](https://www.beac.int/wp-content/uploads/2019/03/REGLEMENT-02_18_CEMAC_UMAC_CM-compressé.pdf)
- EME rules (WAEMU Instruction 008-05-2015): reported to prohibit EMEs from paying interest/remuneration on e-money and from granting credit; EMEs may offer e-money payment services only within WAEMU (exact article wording not retrieved) — [UNSW/UNCDF training doc](https://clmr.unsw.edu.au/sites/default/files/content_files/Training%20Course%20Outline%20-%20Paying%20Interest%20%20on%20E-Money%20Accounts.pdf); [BCEAO Instruction 008-05-2015](https://edenpub.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf)
- **Crypto/stablecoins:** no WAEMU crypto regulation as of Jul–Aug 2026; Governor Brou (22 Jul 2026): cryptos "are not a currency and are not regulated"; roadmap being prepared with AMF-UMOA, no timeline; C-CRYPTO committee; stablecoins referred to the Association of African Central Banks, no position adopted; international conference 8 May 2026 — [Ecofin](https://www.ecofinagency.com/news-finances/2407-57691-waemu-cryptoasset-regulation-remains-in-preparation-bceao-urges-caution); [Financial Afrik, Jul 2026](https://www.financialafrik.com/2026/07/23/la-bceao-avance-avec-prudence-sur-la-monnaie-numerique/); [BCEAO conference communiqué](https://www.bceao.int/sites/default/files/2026-04/Communique-sur-la-Conference-internationale-2026-sur-les-crypto-actifs.pdf)
- **ECO:** ECOWAS 69th summit (Jul 2026) reaffirmed 2027 with progressive adoption by countries meeting convergence criteria; Convergence Council met 7 Sep 2026; analysts call 2027 unrealistic (deficits up to >13% GDP, Nigeria inflation >30%, AES exit of Burkina/Mali/Niger); deadline reportedly postponed five times in two decades — [allAfrica, Jul 2026](https://fr.allafrica.com/stories/202607210573.html); [Financial Afrik, Aug 2026](https://www.financialafrik.com/2026/08/04/leco-la-monnaie-unique-de-la-cedeao-en-2027-un-nouveau-depart-ou-un-calendrier-trop-ambitieux/)

### Inferences
- Product implication: market "pay globally / get paid globally" via FCFA account + FX conversion at the edge (card spend, inbound payouts), not resident EUR/USD balances. EUR/FCFA peg makes EUR→XOF conversion near-riskless, so a competitive margin on EUR inflows is a viable revenue line while USD conversion carries real spread.
- Because of FX-surrender rules, inbound freelancer income must be converted to FCFA on receipt; holding USD balances for residents would need a bank partner with authorization — a roadmap item at best.
- Founder's no-crypto stance aligns with regulatory reality (no licensable framework in WAEMU).
- ECO uncertainty is low-impact for a 2027 MVP; WAEMU/CEMAC FCFAs remain the planning base.

### Gaps
- The specific instruction text governing resident FX accounts post-Aug 2025 (Annex II conditions; whether individuals can get authorization at scale) was not retrieved.
- Whether the 2019 CEMAC card thresholds still apply in 2026 not confirmed.
- Exact wording/article of the EME interest prohibition not confirmed.

---

## A5. Cross-border: intra-WAEMU, WAEMU↔CEMAC, diaspora remittances, PAPSS

### Takeaway
Intra-WAEMU cross-border P2P will fall under the free/≤0.8% PI-SPI regime only from 1 June 2027. WAEMU↔CEMAC has no shared instant rail (PAPSS links are not yet live in WAEMU: BCEAO only preparing a six-month pilot with >80 banks as an observer; BEAC joined July 2026). Remittances into Sub-Saharan Africa remain the world's most expensive (8.78% avg for $200, Q1 2025), but the France→Senegal/CI corridors are cheap and competitive (2.5–5% for €200), so diaspora is a weaker price wedge than an FX/UX wedge.

### Cited Findings
- Cross-border intra-WAEMU transfers align with national PI-SPI conditions from 1 June 2027; until then each institution sets cross-border sending prices — [Financial Afrik, Oct 2026](https://www.financialafrik.com/2026/10/04/la-bceao-rend-pi-spi-obligatoire-revoit-ses-tarifs-et-pose-enfin-la-question-de-nouveaux-services-financiers-adosses-a-la-plateforme/)
- Remittance costs: Sub-Saharan Africa most expensive receiving region at 8.78% total average cost (Q1 2025) vs global 6.49%; banks 14.55% avg; digital-only MTOs 3.55% — [World Bank RPW Q1 2025 report](https://remittanceprices.worldbank.org/sites/default/files/rpw_main_report_and_annex_q125_1_0.pdf); SSA trend 7.73% (Q1'24), 8.37%, 8.45%, 8.16% (Q4'24) — [RPW Q4 2024](https://remittanceprices.worldbank.org/sites/default/files/rpw_main_report_and_annex_q424_13.pdf); global avg 6.36% at Aug 2025 update — [World Bank RPW](https://remittanceprices.worldbank.org/node/1)
- France→Senegal: Western Union record €10 fee, 2.53% total cost for €200, FX margin −0.37% (period unknown) — [World Bank RPW](https://remittanceprices.worldbank.org/node/382753); a secondary guide attributing World Bank data gives €6.99 fee / 4.91% total for €200 and €9.99 / 2.81% for €500 — [Les Afriques, Sep 2026](https://lesafriques.com/2026/09/envoyer-argent-senegal-comparatif-frais-taux-2026/) (numbers not reconcilable without the RPW corridor page)
- Remittances ≈11.4–11.6% of Senegal GDP in 2024; ≈2.0% for Côte d'Ivoire — [statisticsoftheworld (WDI)](https://statisticsoftheworld.com/country/senegal/remittances-received); [Trading Economics](https://tradingeconomics.com/senegal/workers-remittances-and-compensation-of-employees-received-percent-of-gdp-wb-data.html); [statisticsoftheworld CI](https://statisticsoftheworld.com/country/ivory-coast/remittances-received); Cameroon diaspora remittances ~652bn FCFA (~$1.2bn) in 2024 — [Financial Afrik](https://www.financialafrik.com/en/?p=488180)
- PAPSS: 28 countries, >190 commercial banks/fintechs, 16 switches after BEAC joined (Jul 2026); BEAC integration of CEMAC institutions to run through end-2026 — [Launch Base Africa](https://launchbaseafrica.com/2026/07/09/papss-inches-closer-to-continent-wide-coverage-as-central-african-central-bank-joins/); [BEAC communiqué](https://www.beac.int/wp-content/uploads/2016/10/Communique-de-presse-PAPSS-x-BEAC.pdf)
- BCEAO preparing six-month PAPSS pilot with >80 WAEMU banks, BCEAO as observer to ensure compliance before formal commitment (announced 21 Jul 2026; no start date) — [Ecofin](https://www.ecofinagency.com/news-finances/2107-57583-bceao-prepares-papss-pilot-with-more-than-80-west-african-banks)

### Inferences
- WAEMU↔CEMAC (XOF↔XAF, both pegged to EUR at the same rate) remains a pricing anomaly with no instant rail; a corridor product (e.g., Abidjan/Dakar ↔ Douala) via correspondent partners or MTO licensing could be differentiated — but it needs licensing in both zones and isn't MVP-grade.
- Diaspora: France→SN/CI inbound pricing is already low via Wave/digital MTOs; differentiation is in the *receiving account* (instant credit to a savings vault, bill-pay for family, "diaspora-funded" cards) and in diaspora-owned SMEs, not in undercutting fees.
- Intra-WAEMU cross-border sending is a temporary revenue window until June 2027.

### Gaps
- No RPW corridor averages retrieved for France→CI or France→Cameroon; no data on WAEMU↔CEMAC transfer costs.
- PAPSS pilot start in WAEMU after July 2026 not confirmed.

---

## A6. KYC / ID infrastructure and business registries

### Takeaway
eKYC is feasible in CI (biometric RNPP/NNI managed by ONECI; Smile ID claims 2 ID authority connections covering 10M+ records) but appears document-based (OCR + liveness) in Senegal and Cameroon. Business registration is digitized partially (CEPICI 24–48h official, 3–7 days real; APIX/e-RCCM in Senegal), and RCCM is a precondition for a business account — onboarding SMEs is slower and more manual than retail.

### Cited Findings
- Smile ID Côte d'Ivoire: access to 2 ID API authorities covering 10M+ ID records; verifies up to 7 Ivorian ID types — [Smile ID CI](https://usesmileid.com/countries/cote-d-ivoire)
- ONECI manages RNPP and NNI databases; NNI consolidated with biometrics — [CIO Mag](https://cio-mag.com/cote-divoire-ce-quil-faut-savoir-sur-la-strategie-nationale-de-letat-civil-et-de-lidentification); CI planning a national authentication platform and digital ID wallet — [Digital Business Africa](https://www.digitalbusiness.africa/cote-divoire-bientot-une-plateforme-nationale-dauthentification-et-un-portefeuille-didentite-numerique/)
- Smile ID Senegal: ANSD-issued national ID is primary KYC doc; CDP data protection regulator — [Smile ID Senegal](https://usesmileid.com/countries/senegal); Cameroon national ID issued by MINAT; Smile ID claims 96% OCR accuracy — [Smile ID Cameroon](https://usesmileid.com/countries/cameroon)
- Smile ID acquired Appruve (2023) partly to expand into CI and Senegal — [fintech.global](https://fintech.global/2023/04/27/smile-identity-acquires-appruve-to-bolster-identity-verification-in-africa/); government ID authority downtime can frustrate onboarding — [allbusiness.africa](https://allbusiness.africa/insights/smile-id-case-study); Youverify also publishes CI identity verification content, citing fraud and infrastructure obstacles — [Youverify](https://youverify.co/en/blogs/defis-verification-identite-numerique-cote-divoire)
- ~500 million Africans lack formal legal ID (ABA report via Smile ID) — [allbusiness.africa regtech 2026](https://allbusiness.africa/insights/african-regtech-2026)
- CEPICI (CI) reduced company creation to 24h (official); commercial guides cite 24–48h official, 3–7 days real; APIX (Senegal) centralizes RCCM + NINEA in 48–72h (2–5 days real); RCCM required to invoice or open a business bank account; e-RCCM real-time registration launched in Dakar in 2016 — [CEPICI reforms](https://cepici.gouv.ci/web/docs/tableau-r%e9capitulatif-des-r%e9formes-2014-et-textes-y-aff%e9rents-focus-doing-business-2015.pdf); [Kolonell CEPICI vs APIX](https://kolonell.com/fr/blog/cepici-vs-apix-comparatif-creation-senegal-cote-ivoire-2026); [OHADA](https://www.ohada.com/actualite/3050/amelioration-du-climat-des-affaires-au-senegal-creation-dune-entreprise-en-moins-de-24-heures-du-reve-a-la-realite.html)
- Hybrid onboarding works: Djamo combines its app with offline agents who meet customers in person — [TechCrunch](https://techcrunch.com/2025/04/03/djamo-raises-17m-and-has-1m-users-across-francophone-africa/)

### Inferences
- Retail MVP: start in CI (best eKYC database coverage) with tiered KYC (phone + ID scan + selfie liveness for low tier; database match for higher limits).
- SME onboarding requires RCCM/NINEA/DFE document collection; a differentiated B2B wedge could be "company creation + account opening" (partner with CEPICI/APIX intermediaries), since RCCM is the gate to any business account.

### Gaps
- Official national ID coverage rates (% of adults) for CI/SN/CMR not found; SIM registration rules and their use for KYC not researched; whether Smile ID has live database checks in Senegal/Cameroon unconfirmed; Cameroon business registry digitization not found.

---

## A7. Core banking / BaaS / card processing vendors

### Takeaway
Leading emerging-market neobanks mostly run proprietary cores after scale; at launch, cloud cores (Mambu, Oradian) and regional issuer-processors (Paymentology, BPC SmartVista, Network International) are the common pattern. No core vendor is publicly linked to Djamo.

### Cited Findings
- Mambu powers Carbon (Nigeria, full-service bank 2022) and Nyla (Ghana Islamic neobank, 2026) — [FinTech Futures](https://fintechfutures.com/category/outsourcing/page/22); [fintech.global](https://fintech.global/2026/03/12/mambu-powers-nylas-islamic-neobank-launch-in-ghana/)
- Oradian: cloud core for fintechs/MFIs, used by FairMoney; SEAP (Nigeria) migrated in six weeks — [Techpoint](https://techpoint.africa/2024/12/04/oradian-is-driving-sustainable-financial-inclusion-through-its-core-banking-application); TymeBank reported on Mambu; most top neobanks (Nubank, Revolut, Moniepoint, WeBank, Tinkoff) run proprietary cores; Nequi uses Finacle — [Frontier Fintech](https://frontierfintech.substack.com/p/76-what-the-neobank-greats-get-right)
- Kuda runs in-house core ("Nerve"); issued own Visa cards powered by Network International from 2021 — [CB Insights / profiles via search](https://www.cbinsights.com/compare/kudimoney-bank-vs-tymebank) (secondary)
- TymeBank cards: BPC SmartVista for issuing/acquiring/fraud; IDEMIA card manufacturing (2018–2020 era) — [The Asian Banker](https://www.theasianbanker.com/press-releases/bpc-banking-technologies-and-tyme-bank-awarded-the-best-digital-transformation-implementation-in-africa-at-the-middle-east-and-africa-regional-awards-2020)
- Paymentology: issuer-processor connecting to GIM-UEMOA, Visa, Mastercard; Bank Zero (SA) uses it — [Paymentology Africa](https://www.paymentology.com/demo-africa); [FinTech Futures](https://www.fintechfutures.com/partnerships/bank-zero-partners-paymentology-card-issuance); NymCard: issuer-processor for banks in Africa/Middle East — [G2](https://www.g2.com/sellers/nymcard)

### Inferences
- MVP stack: cloud core (Mambu/Oradian or a ledger like in-house) + Paymentology-type processor with GIM-UEMOA connectivity + PI-SPI access via licensed partner + Smile ID for eKYC + aggregator for wallets pre-PI-SPI-API.

### Gaps
- Mono/Okra open banking is Nigeria-focused (Okra shut down in 2025 per general press; not verified in this research); no WAEMU open-banking framework identified. Temenos, Thought Machine, Sopra, Musoni not tied to any francophone neobank in sources found.

---

## B1. Consumer demand: savings, credit, international payments, tontines, cash, trust, gender, youth, diaspora

### Takeaway
Access is no longer the main barrier in WAEMU (mobile money ubiquitous; ~248m accounts) — usage depth is: only 31% of accounts active and 88% of deposits cashed out. Savings demand is strong and largely informal (tontines ~31% of savers in Senegal 2016 data); Findex 2025 shows mobile-enabled saving surging regionally. Gender gaps persist, particularly in CI. Hard, recent country-level survey data for CI/SN/CMR is scarce.

### Cited Findings
- SSA (Findex 2025, 2024 survey): 58.2% account ownership (49.3% in 2021); 40% had mobile money accounts (27% in 2021); top reason for no mobile money account = lack of money (59%) — [Findex 2025 summary](https://www.ezo.app/blog/2025-global-findex-financial-inclusion-and-mobile-tech-in-sub-saharan-africa); [World Bank press release](https://www.worldbank.org/en/news/press-release/2025/07/16/mobile-phone-technology-powers-saving-surge-in-developing-economies)
- Senegal among top five non-high-income economies by share of mobile money account holders (Findex 2025) — [Findex summary](https://www.ezo.app/blog/2025-global-findex-financial-inclusion-and-mobile-tech-in-sub-saharan-africa)
- Senegal 2016 (ANSD): 30.8% of savers use a tontine or cagnotte; 27.9% keep savings at home; 91% of the unbanked cite lack of money — [ANSD via vie-publique.sn](https://www.vie-publique.sn/documents/10457/inclusion-financiere-2016-ansd)
- CI: financial inclusion 58% in 2024 (target 60%) vs 41% in 2017; 2017 gender gap 11 pts, women 52% of 8m unbanked; in 2021 CI was the WAEMU exception where mobile money widened the gender gap (13 pts) — [economie-ivoirienne.ci](https://economie-ivoirienne.ci/banques-et-finances/inclusion-financiere.html); [World Bank blog](https://blogs.worldbank.org/allaboutfinance/maintaining-momentum-financial-inclusion-through-digital-adoption-west-african); [CGAP](https://cgap.org/node/3155)
- AVEC mapping in CI's Nawa region: 484 groups, 16,855 members, 71% women — [FAOLEX](https://faolex.fao.org/docs/pdf/ivc228495.pdf)
- Digital tontines exist but small: E-Tontine (Senegal) 15,000 users since 2015 (2020 figure); MaTontine women's groups; Ollo Africa (Togo, BCEAO-licensed) building Ohana Africa tontine app (Sep 2026) — [Osiris](https://www.osiris.sn/les-tontines-numeriques-une-innovation-africaine-contre-la-precarite.html); [allAfrica, Sep 2026](https://fr.allafrica.com/stories/202609280688.html)
- Djamo user evidence: >55% previously unbanked; women ~1/3 of users; 9 in 10 primary-account users come from the unbanked segment; banked users use it as secondary account for bills and mobile money integration; only 5–10% receive salary in-app — [TechCrunch](https://techcrunch.com/2025/04/03/djamo-raises-17m-and-has-1m-users-across-francophone-africa/)
- Djamo savings at up to 6% p.a. and credit up to 1m FCFA under its new microfinance licence (Sep 2025); pilot loan of 160,000 FCFA disbursed in-app in a minute — [Ecofin](https://www.ecofinagency.com/finance/1209-48632-ivorian-fintech-djamo-breaks-new-ground-with-bceao-microfinance-approval); [Launch Base Africa](https://launchbaseafrica.com/2025/09/12/facing-a-telco-onslaught-djamos-answer-is-now-a-banking-license-and-a-new-model)
- Orange Money partnered with JUMO for AI-scored microcredit — [Launch Base Africa](https://launchbaseafrica.com/2025/09/12/facing-a-telco-onslaught-djamos-answer-is-now-a-banking-license-and-a-new-model)

### Inferences
- Strongest validated demand signals: (1) a place to save that is safer than cash/tontine and pays interest (requires MFI/bank licence — EMEs can't pay interest); (2) small, fast credit; (3) international online payments (card); (4) group savings (tontine/AVEC digitization, women-heavy).
- "Group vaults / digital tontine" fits a women-and-youth segment and is differentiated (existing apps are small), but trust and dispute rules matter.

### Gaps
- No recent (2024–26) CI/SN/CMR survey quantifying desired features, trust levels, cash preference or youth segment behavior; Findex 2025 country tables not retrieved; Afrobarometer/FinScope not found; Cameroon demand data essentially missing.

---

## B2. Freelancers, creators and remote workers earning abroad

### Takeaway
PayPal remains effectively "send-only" in Senegal and not fully accessible in CI; freelancers rely on Payoneer (native Upwork/Fiverr integration) and Wise, losing ~1.5% + 2–3% FX spread and 2–5 days per withdrawal. This is a real, monetizable pain point, but regulatory FX-surrender rules mean the solution is fast conversion into FCFA, not USD/EUR holding.

### Cited Findings
- PayPal "send-only" from Dakar in 2026; Payoneer first choice for Upwork in Dakar (online KYC); Payoneer withdrawal to local bank 1.5% + min $3; USD→FCFA spread 2–3%; 2–4 business days (5 for first withdrawal); Wise ~1–1.5% cheaper on FX on average; FX income above thresholds subject to exchange declaration — [Kolonell (EN)](https://kolonell.com/en/blog/receive-international-payments-freelance-senegal-payoneer-wise-2026); [Kolonell Wise vs Payoneer](https://kolonell.com/en/blog/wise-vs-payoneer-freelance-senegal-fees-comparison-2026) (commercial source)
- PayPal not fully accessible from Côte d'Ivoire; alternatives Wise, Payoneer, mobile money — [AnnuaireCI](https://annuaireci.com/blog/freelance-en-afrique-travailler-pour-le-monde-entier-depuis-abidjan/)
- Residents must surrender FX revenues received from outside WAEMU to an authorized intermediary — [Challenges Économiques](https://challengeseconomiques.com/?p=8539)

### Inferences
- A "get paid from abroad" feature (local-currency receiving via EUR/USD collection partner, converted at transparent spread, credited instantly) + reliable international virtual card for ad spend/SaaS is a credible wedge for freelancers/creators/micro-agencies — a segment that bridges B2C and B2B (sole proprietors).
- Size of the segment in CI/SN is not quantified; treat as niche-but-high-ARPU.

### Gaps
- No figures on number of freelancers/creators in CI/SN/CMR or on platform payout volumes (YouTube/TikTok monetization availability in these countries not verified).

---

## C1. Neobank go-to-market case studies: wedge, revenue model, CAC, profitability, lessons

### Takeaway
Winners chose wedges matched to local market structure: credit (Nubank), FX/travel (Revolut), SME accounts + subscription (Qonto), agent/POS for merchants (Moniepoint), free transfers + agents (Wave, OPay/PalmPay, Kuda), retail-kiosk onboarding (TymeBank), salary/early wage access (Chime), international card (Djamo). In francophone West Africa the transfer and card wedges are being commoditized (PI-SPI free tier; telcos' free virtual cards), pushing Djamo itself toward a microfinance licence for savings and credit.

### Cited Findings
- **Nubank:** FY2025 131m customers, 17m net adds; Q4'25 monthly ARPAC ~$15 (+27% YoY), mature cohorts ~$26–27; monthly cost to serve ~$0.80; activity 83%; ~30% of new customers via word of mouth; revenue ~$16.3bn and net income ~$2.9bn, ROE 33% (secondary) — [Nu Holdings Q4/FY2025 release](https://international.nubank.com.br/company/nu-holdings-ltd-reports-fourth-quarter-and-full-year-2025-financial-results/); [startups.com.br](https://startups.com.br/negocios/nubank-fecha-2025-com-us-29b-em-lucro-e-roe-de-33/); credit-led wedge (no-fee card for underserved) — [Frontier Fintech](https://frontierfintech.substack.com/p/76-what-the-neobank-greats-get-right)
- **Revolut:** 2025 revenue $6.0bn (+46%), pre-tax profit $2.3bn (38% margin), 5th consecutive profitable year; subscriptions $936m (+67%); 68.3m retail and 767k business customers; Business = 16% of income; payments/FX-led wedge from founder FX expertise — [Revolut](https://www.revolut.com/en-AT/news/revolut_reports_record_profit_of_2_3bn_for_2025_as_revenue_surges_to_6bn/); [Frontier Fintech](https://frontierfintech.substack.com/p/76-what-the-neobank-greats-get-right)
- **Qonto (SME-first, subscription):** 2024 revenue €448.7m (+44%), net profit €144m; subscriptions + transaction commissions €261.3m; interest revenue €136m; ~600k customers in 8 countries; profitable thanks to NII, targeting operational profitability ex-NII — [Sifted](https://sifted.eu/articles/qonto-results-2024); [Qonto Activity Report 2024](https://www.lobbyregister.bundestag.de/media/24/01/586158/Qonto_Activity-report_2024_EN.pdf)
- **Moniepoint (merchant/agent-first):** started as bank settlement/POS acquiring tooling (2016; 26 of 30 Nigerian banks by 2018, first client Fidelity, sometimes free to banks); terminals distributed via aggregators to agents; ~611k agents; expanded in 2022 to banking, credit, business management; 2025: ₦412tn (~$297bn) processed, >14bn transactions, >₦1tn loans disbursed; claims 8 of 10 in-person payments in Nigeria; reportedly profitable (unverified) — [Techpoint](https://techpoint.africa/2024/10/30/6-key-strategies-moniepoint-adopted-a-1-billion-fintech/); [Techeconomy](https://techeconomy.ng/beyond-payments-how-moniepoint-powered-nigerias-msme-growth-in-2025); [allbusiness.africa](https://allbusiness.africa/insights/moniepoint-case-study); [TechCabal](https://techcabal.com/?p=180023)
- **Kuda (free transfers):** 2024 loss $5.83m vs $35.11m in 2023 (−84%, cost cuts); CEO claims Nigerian arm profitable Q1 2025 (~₦6bn); >7m customers (dated); targeting 1.7m active users by 2026 — [Techpoint](https://techpoint.africa/news/kuda-q1-2025-performance/); [BusinessDay](https://businessday.ng/?p=1072114)
- **OPay/PalmPay (free transfers + agents + device preinstall):** free transfers early (OPay until Jun 2023, then ₦10 above threshold); OPay >500k agents (2023), PalmPay claims >1m agents/merchants; PalmPay preinstalled on Tecno/Infinix/Itel phones → >35m users; gained trust during 2022–23 naira-redesign crisis and bank outages — [TechCabal](https://techcabal.com/2025/08/25/opay-palmpay-lead-20trn-mobile-money-boom/); [BusinessDay](https://businessday.ng/technology/article/how-two-chinese-fintechs-clinched-nigerias-pos-market/)
- **TymeBank (retail kiosks):** first month of profit Dec 2023, "sustainable profit" from 30 Sep 2024; group >15m customers (>10m in SA); GoTyme Philippines 6.7m users (Jun 2025), not yet profitable; SA entity renamed GoTyme Bank (Apr 2026) — [BusinessTech](https://businesstech.co.za/news/banking/803626/tymebank-now-making-sustainable-profits/); [GMA](https://www.gmanetwork.com/news/money/companies/951685/gotyme-to-hit-9m-customers-in-2025/story/); [Financial Afrik](https://www.financialafrik.com/en/2026/04/13/south-africa-tymebank-completes-its-rebranding/)
- **Chime (salary/early access):** revenue mostly interchange; MyPay (early wage access) nearly doubled platform revenue; Q1 2025 revenue $518.7m (+32%), net income $12.9m; 8.6m active members; ARPU $251 (annualized); IPO Jun 2025 at ~$11.6bn — [Nasdaq/MarketBeat](https://www.nasdaq.com/articles/chimes-smart-ipo-half-valuation-double-strength)
- **Wave (cheap transfers + agents):** free deposits/withdrawals, 1% P2P; ~29m MAU and >150k agents (mid-2025); ~8m monthly users in Senegal; $137m debt raise (Jun 2025, RMB-led) for working capital; no audited profit data — [TechCabal](https://techcabal.com/2025/06/30/wave-raises-137-milion/); [TriplePundit](https://triplepundit.com/2025/wave-mobile-money-cote-divoire/)
- **Djamo (card-first for international payments):** >1m customers CI+SN (Apr 2025); $17m raise led by Janngo; 250 staff; ~10,000 SMEs onboarded (many started as retail users) with bulk payments, payment links, QR; revenue = merchant fees on online card purchases + premium tier paid by 25% of users (+ interchange, payout and float fees per Dealroom); revenue 5x since 2022; >$4.5bn processed — [TechCrunch](https://techcrunch.com/2025/04/03/djamo-raises-17m-and-has-1m-users-across-francophone-africa/); [Dealroom](https://dealroom.co/companies/djamo/); first fintech to obtain a BCEAO microfinance licence (Sep 2025) as a defensive move vs telco virtual cards — [Launch Base Africa](https://launchbaseafrica.com/2025/09/12/facing-a-telco-onslaught-djamos-answer-is-now-a-banking-license-and-a-new-model)
- Cross-case lessons: no single right wedge; market structure biggest determinant; act like a bank from day one (licensing); hybrid digital+physical distribution in Africa; domain-expert founders; cloud-native core — [Frontier Fintech](https://frontierfintech.substack.com/p/76-what-the-neobank-greats-get-right)

### Inferences
- Transferable to francophone Africa: (1) Moniepoint's "serve the merchant/SME, then the consumer" path; (2) Qonto's subscription pricing for SMEs (businesses pay for time-saving tools); (3) Djamo's freemium premium tier (25% paying) shows consumers in CI will pay subscriptions for card/international features; (4) Chime/salary — Djamo only has 5–10% of users with salary in-app, so payroll is an open lever (via B2B payroll clients); (5) hybrid agents for onboarding/trust.
- Less transferable now: free-transfer wedges (Kuda/OPay/Wave) — PI-SPI makes them table stakes; standalone virtual card wedge — commoditized by Wave/Orabank.
- Credit-first (Nubank) requires a licence (MFI/bank) and data; EMEs cannot lend in WAEMU.

### Gaps
- No public CAC figures for Djamo, Wave, Kuda or any francophone neobank; no reliable Nubank 2025 CAC disclosure.

---

## C2. Revenue models and benchmarks (interchange, FX, subscriptions, float, lending, merchant fees)

### Takeaway
In WAEMU, the main viable revenue lines for a neobank are merchant/acceptance fees, card FX margin, subscriptions (proven by Djamo's 25% premium uptake), cash-out fees, cross-border (temporary), and — only with an MFI/bank licence — lending and interest margin. EMEs reportedly cannot pay interest on e-money nor lend; P2P transfer fees are being regulated away.

### Cited Findings
- Djamo revenue sources: merchant fees on online card purchases, premium tier (25% of users), interchange, payout and "floating" fees; planned lending and deposit interest — [TechCrunch](https://techcrunch.com/2025/04/03/djamo-raises-17m-and-has-1m-users-across-francophone-africa/); [Dealroom](https://dealroom.co/companies/djamo/)
- PI-SPI pricing: free ≤8,000 FCFA/day; ≤0.8% above; free receiving; cross-border aligned from June 2027 — [Financial Afrik](https://www.financialafrik.com/2026/10/04/la-bceao-rend-pi-spi-obligatoire-revoit-ses-tarifs-et-pose-enfin-la-question-de-nouveaux-services-financiers-adosses-a-la-plateforme/)
- EMEs: reported prohibition on fund remuneration and on credit (Instruction 008-05-2015) — [UNSW/UNCDF](https://clmr.unsw.edu.au/sites/default/files/content_files/Training%20Course%20Outline%20-%20Paying%20Interest%20%20on%20E-Money%20Accounts.pdf); [regalert summary](https://regalert.today/document/8b87137a-ac90-4c19-9f88-0f3d8c7dd3ea/text)
- Djamo MFI licence allows savings up to 6% and credit up to 1m FCFA — [Ecofin](https://www.ecofinagency.com/finance/1209-48632-ivorian-fintech-djamo-breaks-new-ground-with-bceao-microfinance-approval)
- Card FX/payout spreads freelancers face today: ~1.5% + 2–3% FX — [Kolonell](https://kolonell.com/en/blog/receive-international-payments-freelance-senegal-payoneer-wise-2026)
- Global benchmarks: Nubank monthly ARPAC ~$15, cost-to-serve ~$0.80 — [Nu Holdings](https://international.nubank.com.br/company/nu-holdings-ltd-reports-fourth-quarter-and-full-year-2025-financial-results/); Revolut subscriptions $936m of $6.0bn — [Revolut](https://www.revolut.com/en-AT/news/revolut_reports_record_profit_of_2_3bn_for_2025_as_revenue_surges_to_6bn/); Qonto NII €136m of €448.7m — [Sifted](https://sifted.eu/articles/qonto-results-2024)
- Djamo revenue estimates conflict: Dealroom $10–50M; RocketReach $23.1M (aggregator, unverified) — [Dealroom](https://dealroom.co/companies/djamo/); [RocketReach](https://rocketreach.co/djamo-profile_b40cc4f5ffb9a1fb)

### Inferences
- Float income: EMEs hold float at partner banks; whether the EME (not the customer) earns interest from the bank on trust accounts is not clearly prohibited in sources found — Dealroom lists "floating fees" for Djamo, suggesting some float monetization occurs; verify with counsel.
- Implied Djamo ARPU (rough): $10–50M revenue / ~1m users ≈ $10–50 per user per year — far below Nubank's ~$180/yr; plan unit economics for low single/double-digit $ ARPU on retail, much higher on SMEs.
- The licence path (EME → MFI/bank) is decisive for revenue depth; plan regulatory roadmap accordingly.

### Gaps
- No WAEMU interchange rate data; no regional ARPU/CAC benchmarks from credible sources; no data on BCEAO policy rate pass-through to float.

---

## C3. B2B-first vs B2C-first in this region

### Takeaway
Evidence leans toward an SME/merchant-anchored entry (or a B2B2C hybrid) in WAEMU: consumer transfer and card wedges are commoditized by regulation and telcos, whereas business tooling on PI-SPI (API Business list only 24 names), merchant QR acceptance (3.7m registered merchants, merchant share 23% of mobile payment volume), payroll and reconciliation are under-served and monetizable via subscriptions — a Qonto/Moniepoint-like path. B2C remains important for scale and deposits, best reached via payroll and freelancers rather than paid acquisition.

### Cited Findings
- Merchants: 3.7m registered in WAEMU in 2024 (from 1.75m); merchant share of mobile payment volume 23.3% (3.3% in 2020) — [Launch Base Africa](https://launchbaseafrica.com/2026/03/24/the-267bn-crown-wave-edges-closer-to-dethroning-orange-in-west-africa/)
- PI-SPI API Business: 24 approved names (mid-Sep 2026); analyst expects SME cross-border treasury, payroll and reconciliation tools to be the first products, credit later — [Financial Afrik](https://www.financialafrik.com/2026/10/04/la-bceao-rend-pi-spi-obligatoire-revoit-ses-tarifs-et-pose-enfin-la-question-de-nouveaux-services-financiers-adosses-a-la-plateforme/); BCEAO reportedly now targeting business payments — [AITN](https://afriqueitnews.com/finance/wave-integre-le-pi-spi-et-la-bceao-cible-desormais-les-paiements-dentreprises/)
- Djamo: ~10,000 SMEs onboarded, many converting from retail; only 5–10% of users get salary in-app, goal 50% — [TechCrunch](https://techcrunch.com/2025/04/03/djamo-raises-17m-and-has-1m-users-across-francophone-africa/)
- Julaya: "neobank for African companies" (CI/SN/BJ etc.), bulk payouts to workers/suppliers across mobile money, corporate prepaid card; 500+ clients incl. Jumia; raised $7m pre-Series A (Speedinvest-led extension) and $1.4m from CDC-CI Capital (Oct 2025) — [Africa PE News](https://www.africaprivateequitynews.com/p/speedinvest-leads-5m-investment-round-for-west-african-fintech-company); [CB Insights](https://www.cbinsights.com/company/julaya/financials)
- Moniepoint B2B-first (banks → agents → merchants → consumers) reached unicorn scale; Revolut Business is 16% of income; Qonto SME-first profitable — [Techpoint](https://techpoint.africa/2024/10/30/6-key-strategies-moniepoint-adopted-a-1-billion-fintech/); [Revolut](https://www.revolut.com/en-AT/news/revolut_reports_record_profit_of_2_3bn_for_2025_as_revenue_surges_to_6bn/); [Sifted](https://sifted.eu/articles/qonto-results-2024)
- B2C counter-evidence: Djamo reached >1m consumers with 25% paying premium; consumer card wedge worked 2020–24 but is now commoditized — [TechCrunch](https://techcrunch.com/2025/04/03/djamo-raises-17m-and-has-1m-users-across-francophone-africa/); [Launch Base Africa](https://launchbaseafrica.com/2025/09/12/facing-a-telco-onslaught-djamos-answer-is-now-a-banking-license-and-a-new-model)
- Business onboarding friction: RCCM required for business accounts; real registration 2–7 days — [Kolonell](https://kolonell.com/fr/blog/cepici-vs-apix-comparatif-creation-senegal-cote-ivoire-2026)

### Inferences
- Recommended framing for the report writer: "B2B-anchored, B2C-enabled" — sell an SME account (collections via PI-SPI QR + wallets, bulk payouts/payroll, cards for ad/SaaS spend, invoicing, reconciliation) on subscription; payroll then onboards employees as retail users (Chime/salary lever) at near-zero CAC; freelancers/creators serve as the bridge segment.
- Risk: B2B sales cycles and KYB friction; mitigate with self-serve for sole proprietors/informal merchants and company-creation partnerships.

### Gaps
- No quantitative comparison of B2B vs B2C CAC/LTV in francophone Africa; no SME survey on willingness to pay for subscriptions in CI/SN; Cameroon/CEMAC SME data not found.
