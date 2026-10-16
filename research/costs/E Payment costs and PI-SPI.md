# E. Payment costs: Kelen (SME neobank, Senegal 2027, then Côte d'Ivoire)

Research date: 2026-10-16. Every figure below has a source URL and a confidence tag.
- **official**: primary document from the regulator, operator or bank (PDF or live page fetched).
- **press**: news article quoting an official text.
- **third-party**: blog, comparison site or search-engine extraction of a document that could not be fetched directly.
- **unverified**: one weak source, or sources that contradict each other.

Anything not found is marked **not found**. No numbers are invented.

> Research limits:
> - The pispi.bceao.int site (FAQ and fee pages) returned 503 errors or TLS failures throughout.
> - Société Générale Sénégal's PDFs are behind Incapsula, so they were read only through search extracts.
> - Paystack and CinetPay returned 403.
> - The session's web-search quota ran out before Ecobank, CBAO, MTN CI, Moov and Mixx tariffs could be searched further.

---

## 1. PI-SPI (BCEAO instant payment system)

### 1.1 Official 2 Nov 2026 grid (BCEAO communiqué dated 2 Oct 2026)

Primary source: BCEAO communiqué *"Transactions de monnaie électronique entre personnes physiques par l'intermédiaire de PI-SPI"*, Dakar, 2 Oct 2026.
- PDF: https://www.bceao.int/sites/default/files/2026-10/Communiqu%C3%A9%20du%202%20octobre%202026.pdf
- Page: https://www.bceao.int/fr/communique-presse/transactions-de-monnaie-electronique-entre-personnes-physiques-par-lintermediaire

The PDF was downloaded and read in full.

| Item | Figure | Unit | Effective | Confidence |
|---|---|---|---|---|
| PI-SPI mandatory for all **interoperable e-money** transactions in UEMOA | n/a | n/a | 2 Nov 2026 | official |
| **Send**: domestic transfers with daily cumulative amount ≤ **8,000 FCFA** per user and per participant | **free**, no limit on the number of operations (BCEAO: covers 75% of e-money transactions) | per user/day/participant | 2 Nov 2026 | official |
| **Send**: domestic transfers above 8,000 FCFA | fees "dont le taux, compris entre **0 et 0,8%**, est appliqué au montant hors taxes du transfert" | % of amount, excl. tax | 2 Nov 2026 | official |
| **Receive** | **free**, no limit on amount or number of operations | n/a | 2 Nov 2026 | official |
| Cross-border intra-UEMOA e-money transfers | same rules as domestic | n/a | **1 Jun 2027** (until then each institution sets its own price) | official |
| Scope | (a) bank/IMF account ↔ EME or EP account; (b) EME ↔ EP | n/a | n/a | official |
| Network size | 175 participants connected, 38 million people with access | n/a | 2 Oct 2026 | official |

**Key interpretation for Kelen.** The title and recitals limit the communiqué to **transfers between natural persons (personnes physiques)**.
- It sets **no price** for transfers sent by legal entities, such as salary or supplier payments made by a company, or bulk/API business payments.
- It also sets no price for bank ↔ bank instant transfers.
- In those cases each participant prices freely. No BCEAO grid for businesses was found.

### 1.2 Earlier regime (30 Sep 2025 to 1 Nov 2026): the "30 free receipts then ≤ 1%" claim

| Item | Figure | Source | Date | Confidence |
|---|---|---|---|---|
| Natural persons and sole-trader merchants: all domestic sends and all payments free | free | https://mondedesbanques.com/culture-generale/pi-spi-tout-ce-quil-faut-savoir/ | 7 Aug 2026 | press (secondary; the official FAQ was unreachable) |
| First **30 receipts per calendar month** free; beyond that, fees allowed, **capped by BCEAO at 1% of amount received** | ≤ 1% | same | 7 Aug 2026 | press |
| A person receiving more than 30 transfers in a month has the excess treated as "payments" | n/a | https://www.seneweb.com/en/news/Economie/pi-spi-la-gratuite-des-paiements-bouscule-le-partage-des-revenus_n_505386.html | 27 Sep 2026 | press |
| Returns of funds, **payment requests (request-to-pay)** and cancellation requests free | free | Monde des Banques (above) | 7 Aug 2026 | press |
| Fees for receipts by **type-C merchants** (legal entities) and ancillary services **freely set by each participant** | free pricing | Monde des Banques (above) | 7 Aug 2026 | press |
| Cross-border: sending priced by each institution; receiving free | n/a | same | 7 Aug 2026 | press |
| "30 receipts / 1%" rule repeated | ≤ 1% | https://www.lejecos.com/PI-SPI-Le-piege-tarifaire-de-Wave_a31598.html | 2 Oct 2026 | press |

**Reconciling the conflicting reports**
1. The "30 free receipts then ≤ 1%" rule was the **launch regime** (Sep 2025). It is **replaced on 2 Nov 2026**: receiving becomes free without limit.
2. Sending was free for individuals at launch. From 2 Nov 2026 it is free only up to 8,000 FCFA cumulated per day, with 0–0.8% above that.
3. Both regimes apply to natural persons only. Legal-entity flows (type-C merchants, businesses) were and remain priced freely by participants.
4. Remaining ambiguity: the communiqué says the threshold is a "montant cumulé quotidien ≤ 8,000". The fee clause says it applies to "transferts d'un montant supérieur à 8,000 FCFA".
   - Pi Business Info (https://www.pibusinessinfo.com/paiements-instantanes-uemoa-bceao-pi-spi/) reads it as the rate applying to the **whole** transfer.
   - Other outlets do not settle the point.
   - Status: **unverified**.
5. The press consistently reports "0 to 0.8% excluding tax". Some outlets say "capped at 0.8%". These are the same thing, consistent with the PDF.

### 1.3 Other PI-SPI cost items

| Item | Figure | Source | Date | Confidence |
|---|---|---|---|---|
| Fee the participant (bank) pays BCEAO per PI-SPI transaction | **not found** (not published in any communiqué found) | n/a | n/a | not found |
| PI-SPI membership or connection fee | **not found** | n/a | n/a | not found |
| Indirect participation (fintech via sponsor bank): rules and fees | **not found** in primary sources. One search snippet mentions direct participation for CB-supervised institutions above a 2 bn FCFA threshold; it could not be confirmed | n/a | n/a | unverified |
| Connection deadline: banks, EMEs and EPs | 30 Sep 2026 | https://www.bceao.int/fr/communique-presse/prolongation-du-delai-de-connexion-a-pi-spi | 25 Jun 2026 | official |
| Connection deadline: **MFIs supervised by the Commission Bancaire** (relevant to the MFI Kelen plans to buy) | **30 Jun 2027** | same | 25 Jun 2026 | official |
| **API Business** certified (issue and receive payments, **bulk payment orders**, real-time tracking) | 24 participants certified. **Senegal (9):** African Financial Agent SN, Ecobank, FBNBank, Mikaty SN, Orange Finances Mobiles, TouchPoint Financial Services, Samir Money, UM ACEP, Versus Finance Tech-AS. **CI (8):** Connekt4, Ecobank, Mansa Bank, MTN MFS, PaymeTrust, Standard Chartered, SYCA SA, TouchPoint. **Ecobank** is certified in all 8 countries | https://www.bceao.int/fr/communique-presse/homologation-des-api-business-de-la-plateforme-interoperable-du-systeme-de and https://www.bceao.int/sites/default/files/inline-files/Liste_des_API-Business_PI-SPI_%20homologue%CC%81es_sept2026%20%281%29.pdf | 16–17 Sep 2026 | official |
| API Business **pricing** (bulk/API sends by businesses) | **not found**; free pricing by participant | n/a | n/a | not found |
| Public sandbox for API Business | launched | https://www.bceao.int/fr/communique-presse/deploiement-du-sandbox-public-de-lapi-business-de-la-plateforme-interoperable-du | 13 Nov 2025 | official |
| Treasury of Côte d'Ivoire runs **mass payments** (salaries etc.) on PI-SPI | n/a | https://www.bceao.int/fr/communique-presse/connexion-des-tresors-publics-la-plateforme-interoperable-du-systeme-de-paiement | 8 Oct 2026 | official |
| Merchant payments on PI-SPI | free for the paying individual; merchant-side (type C) fees freely set by participant | Monde des Banques (above) | Aug 2026 | press |
| Example aggregator on PI-SPI (AFAPAY): P2P free; "pour les encaissements marchands, une commission s'applique selon la grille tarifaire de votre contrat" | rate not published | https://afa-pay.com/guide/pi-spi | 2026 | third-party |
| Wave joins PI-SPI (Senegal and CI) | n/a | https://www.financialafrik.com/2026/10/04/la-bceao-rend-pi-spi-obligatoire-revoit-ses-tarifs-et-pose-enfin-la-question-de-nouveaux-services-financiers-adosses-a-la-plateforme/ | 4 Oct 2026 | press |
| E-money balance cap raised from 2M to **4M FCFA**; monthly reload cap from 10M to **15M FCFA** (instruction dated 8 Oct 2026) | n/a | https://www.togofirst.com/fr/finance/1210-20307-uemoa-la-bceao-double-le-plafond-des-comptes-mobile-money-a-l-heure-de-pi-spi | 12 Oct 2026 | press |

---

## 2. Interbank transfers (STAR-UEMOA RTGS, SICA-UEMOA clearing)

### 2.1 BCEAO fees charged to banks

| Item | Figure | Source | Date | Confidence |
|---|---|---|---|---|
| BCEAO per-transfer fee for SICA-UEMOA or STAR-UEMOA | **not found** (not public in the documents found) | n/a | n/a | not found |
| Evidence that BCEAO bills SICA transfers: billing suspended in Q2 2020 on condition that banks **cut customer transfer fees by 50%** (Avis n°004-03-2020, 1 Apr 2020) | n/a | https://www.bceao.int/sites/default/files/2023-07/BCEAO%20-%20Rapport%20sur%20les%20IMF,%20Moyens%20et%20Services%20de%20Paiement_2020-2021.pdf | 2020 | official |
| SICA accepts transfers ≤ **50M FCFA**; larger ones must go through STAR (RTGS) | 50M FCFA | search summary of https://www.bceao.int/fr/content/sica-uemoa (page now redirects) | n/a | third-party |
| BCEAO list of services that must be free since 1 Oct 2014, including: **same-bank account-to-account transfer**, receipt of national/UEMOA/international transfers, cash deposit at own bank (excl. stamp duty), salary domiciliation | free | https://www.bceao.int/fr/communique-presse/communique-de-presse-services-bancaires-offrir-titre-gratuit-par-les | 2014 | official |

### 2.2 Bank customer tariffs (public, retail list prices)

| Bank / product | Figure | Unit | Source | Date | Confidence |
|---|---|---|---|---|---|
| BOA Sénégal: SICA transfer to another bank, **digital** channel, ≤ 5M | **2,000** | FCFA HT/transfer | https://www.boasenegal.com/wp-content/uploads/2026/06/Conditions-de-banque-Particuliers-2026.pdf | 1 Jan 2026 | official |
| BOA Sénégal: SICA digital > 5M | 5,000 | FCFA HT | same | 2026 | official |
| BOA Sénégal: SICA paper ≤ 5M / > 5M | 4,000 / 7,000 | FCFA HT | same | 2026 | official |
| BOA Sénégal: STAR-UEMOA digital, by amount band (0–5M / 5–10M / 10–50M / > 50M) | 15,000 / 20,000 / 30,000 / 50,000 | FCFA HT | same | 2026 | official |
| BOA Sénégal: **multiple transfers**, first 2 lines / from line 3 | 4,000 / **1,500 per line** | FCFA HT | same | 2026 | official |
| BOA Sénégal: standing order execution ≤ 5M | 2,000 | FCFA HT | same | 2026 | official |
| Société Générale Sénégal (corporate, 2026): STAR-UEMOA unit | 20,000 | FCFA | search extract of https://societegenerale.sn/fileadmin/user_upload/SG_Senegal/PDF/EXES__SG_SN_CONDITION_TARIFAIRE_2026_CLICOM.pdf | 2026 | third-party |
| SG Sénégal (corporate, H2 2026): multiple transfer to other UEMOA banks | 7,500 per line (min 20,000) | FCFA | search extract of https://societegenerale.sn/fileadmin/user_upload/SG_Senegal/PDF/SGSN_CONDITION_TARIFAIRE__2Semestre_2026_CLICOM.pdf | H2 2026 | third-party |
| SG Sénégal: unit / multiple transfer (domestic) | 15,000 / 5,000 per line | FCFA | same | H2 2026 | third-party |
| SG Sénégal: **electronic transfer to another bank via Sogecashnet / MyBusiness** | **150 per line** | FCFA | same | H2 2026 | third-party (could not open PDF) |
| SG Sénégal: STAR-UEMOA unit via Sogecashnet | 2,500 | FCFA | search extract | 2026 | third-party |
| SG Sénégal Sogecashnet pack | 10,000 (standard) / 25,000 (premium) | FCFA HT/month | https://societegenerale.sn/fr/entreprises-institutions/cash-management/pilotage-vos-comptes-distance/sogecashnet/ (search extract) | 2025–26 | third-party |
| UBA Côte d'Ivoire (corporate): **online local interbank transfer** | **750** | FCFA/transaction | https://www.ubacotedivoire.com/wp-content/uploads/sites/12/2026/04/Conditions-tarifaires-Entreprises-UBA-CI-2026.pdf | 2026 | official |
| UBA CI: online regional transfer | 5,000 | FCFA | same | 2026 | official |
| UBA CI: branch transfer via SICA / via STAR (RTGS) | 10,000 / 15,000 | FCFA | same | 2026 | official |
| UBA CI: other-bank local interbank transfer (other grid) | 2,500 | FCFA | same | 2026 | official |
| UBA CI: bulk file submission (télétransmission) | free (per-line execution fee applies) | n/a | same | 2026 | official |
| Brief's "250–1,000 FCFA per line online" | consistent with 150 (SG, third-party) and 750 (UBA CI, official) | FCFA/line | see above | 2026 | n/a |

**What a fintech could negotiate (inference, not sourced).**
- The lowest public online interbank price found is 150 FCFA per line (SG Sogecashnet, third-party extract). The lowest official one is 750 FCFA (UBA CI).
- BCEAO's own per-transfer charge to banks is unpublished. In 2020 it was material enough that suspending it was traded against a 50% cut in customer fees.
- A high-volume agent or partner programme could therefore plausibly reach about 100–300 FCFA per SICA or PI-SPI line. **No public source confirms a wholesale price.**
- Same-bank transfers (Kelen client → employee or supplier at the partner bank) should cost about 0, because the BCEAO 2014 free-services list covers them.

---

## 3. Bank-to-wallet and wallet payouts for businesses

| Item | Figure | Unit | Source | Date | Confidence |
|---|---|---|---|---|---|
| **Wave Business bulk payments** ("Paiements en masse"): "1% pour vous, gratuit pour le destinataire" | **1%**, no cap stated | % of amount, paid by sender | https://www.wave.com/fr/business/ (fetched live 2026-10-16) | live Oct 2026 | official |
| Wave Payout API: response returns a `fee` field; `receive_amount` is net of fees; business wallet must cover amount + fees. Examples: 15,000 → fee 150; 1,000 → 10 | about 1% in the examples (illustrative only, not a fee schedule) | n/a | https://docs.wave.com/payout | 2026 | official (docs) |
| Is Wave's 1% negotiable for aggregators or large payers? | **not found** (no public wholesale rate). Wave's partner API is "non publique, sur dossier" | n/a | https://sentur.net/mobile-money-backend-afrique-ouest/ (search summary) | 2026 | unverified |
| Wave: bank ↔ Wave transfers capped at **500 FCFA** (1% up to 50,000 FCFA); free first transfer of the month discontinued | 1%, max 500 | FCFA | https://x.com/WaveSenegal/status/1852323481154904188 | 1 Nov 2024 (decoded from post ID) | official (operator social post) |
| **BOA Sénégal**: "Virement Wave vers Compte / Compte vers Wave" | **1% of amount, max 500 FCFA**; 1st transfer of the month free | FCFA HT | https://www.boasenegal.com/wp-content/uploads/2026/06/Conditions-de-banque-Particuliers-2026.pdf | 2026 | official |
| BOA Sénégal: account → Orange Money (charged by BOA) | 500 | FCFA HT flat | same | 2026 | official |
| BOA Sénégal: Orange Money → account (charged by Orange) | 200 (≤ 10k) / 300 / 400 / 700 / 1,000 (100–200k) | FCFA | same | 2026 | official |
| Wave "bridge" to UBA or Banque Atlantique accounts (Senegal) | 1% incl. VAT | % | https://lesafriques.com/2026/09/banques-mobile-money-senegal-diaspora-2026/ | updated 12 Oct 2026 | third-party |
| **Orange Money Sénégal "Paiement PRO"** (salaries, suppliers, per diem via salaires.orange-sonatel.com) | **1%** if beneficiary has an OM account; **1.5%** if not. Payer bears the withdrawal fee | % of amount, paid by company | https://www.orangebusiness.sn/orange-money | live Oct 2026 | official |
| Orange Money B2B subscription | free, no recurring fee | n/a | same | live | official |
| Mixx by Yas (Senegal): business payouts | **not found** | n/a | n/a | n/a | not found |
| MTN MoMo CI: disbursement / bulk pay | **not found**. Retail: sending 1% capped at 4,500 FCFA; deposit and withdrawal free since Aug 2025 | % | https://lesafriques.com/2026/09/mobile-money-banques-cote-ivoire-france-2026/ | Sep 2026 | third-party |
| Moov Africa CI: business payouts | **not found** | n/a | n/a | n/a | not found |
| **Flutterwave Senegal**: payout to mobile money / to bank account | **2%** / **1,500 XOF** per transfer (excl. VAT and local taxes) | n/a | https://flutterwave.com/sn/pricing (fetched) | Oct 2026 | official |
| **Flutterwave CI**: payout to mobile money / to bank (< 50M) / bank (≥ 50M) | 2% / 1,500 XOF / 4,000 XOF (excl. VAT) | n/a | https://flutterwave.com/ci/pricing (fetched) | Oct 2026 | official |
| CinetPay mass payouts ("Mass Payout") | about 1.5% depending on volume (page shown for Mali, BF and Congo; page has a typo) | % | https://cinetpay.com/pricing (search summary; 403 on fetch) | n/a | third-party |
| CinetPay CI: transfer-account funding | 2% on top-up (or a fixed grid) | % | https://support.cinetpay.com/d/52-tarifications-des-paiements-entrants-et-sortants (search summary) | undated | third-party |
| HUB2, InTouch, Bizao, PayDunya: wholesale or payout prices | **not found** (no public grid; PayDunya pricing URLs return 404) | n/a | n/a | n/a | not found |
| GIM-UEMOA interbank ATM withdrawal | 500 | FCFA | https://www.gim-uemoa.org/fr/interbancarite-gim | undated (live) | official |
| GIM-UEMOA / BCEAO interchange between EMEs and banks ("frais d'interopérabilité") | **not found**. Under PI-SPI no interchange is published; GIMpay had still not processed a transaction by Sep 2026 | n/a | https://techcabal.com/2026/09/22/francophone-weekly-by-techcabal-041/ (search summary) | Sep 2026 | not found |

**Read-across.** Before 2 Nov 2026, the public business list price to pay wallets is **1%** (Wave, and OM for OM holders), with no cap. Bank tariffs that route bank → wallet cap it at **500 FCFA** (BOA, Wave's own bank bridge).

From 2 Nov 2026 all interoperable e-money flows go through PI-SPI, which changes Kelen's route:
- Kelen (via its partner bank) → employee's Wave or OM wallet becomes a **bank → EME PI-SPI transfer**.
- Receiving is free for the employee.
- The sending price is whatever the partner bank charges Kelen. It is not regulated for legal-entity senders. As a reference, individuals pay ≤ 0.8% above 8,000 FCFA.

---

## 4. Collection costs (payment links)

| Item | Figure | Unit | Source | Date | Confidence |
|---|---|---|---|---|---|
| **Wave merchant** (Business app): "Les premiers **20,000 CFA** de paiement sont gratuits pour vous chaque jour, avec des frais de **1%** par la suite"; free for customers | 1% above 20k/day | % | https://www.wave.com/fr/business/ (live 2026-10-16) | live | official |
| Wave Checkout API fee | **not published** on the API docs; third-party guides say about 1% | % | https://kolonell.com/en/blog/wave-business-api-integration-guide-2026-en | 2026 | third-party |
| **Orange Money Sénégal** merchant and internet payment: free for the customer; "Le partenaire paie **1%** de commission du montant encaissé"; settled to bank at **D+5** | 1% | % | https://www.orangebusiness.sn/orange-money | live | official |
| Orange Money merchant (third-party claims) | 1.5–2.5% | % | https://simiz.io/blog/frais-orange-money-wave-senegal | 2026 | unverified (conflicts with official 1%) |
| MTN CI merchant | 2.0–2.8% (one blog), 1–1.2% (another) | % | https://simiz.io/blog/frais-de-scolarite-mobile-money-cote-ivoire ; https://kolonell.com/en/blog/payment-gateway-cote-divoire-wave-orange-mtn-2026 | 2026 | unverified |
| **UBA CI acquiring** (POS / e-commerce): UBA cards / GIM-UEMOA cards / Visa-Mastercard | **1% / 2% / 3–3.5%**; POS rental 20,000 FCFA | % of amount | https://www.ubacotedivoire.com/wp-content/uploads/sites/12/2026/04/Conditions-tarifaires-Entreprises-UBA-CI-2026.pdf | 2026 | official |
| UBA CI "Transaction TPE-WEB" GIM-UEMOA / international | free / 3% | n/a | same (another section of the same grid) | 2026 | official (internal inconsistency in the grid) |
| SGCI 3% card acquiring (the brief's figure) | **not found** in a 2026 SGCI grid | n/a | n/a | n/a | not found |
| **PayTech (Senegal)**, by annual turnover: < 10M / 10–100M / > 100M FCFA | cards **3% / 2.75% / 2.5% HT**; mobile money **2.0% / 1.75% / 1.5%** | % | https://paytech.sn/ (fetched) | Oct 2026 | official |
| PayTech (CI) | cards 2.5% HT; mobile money 2.0% / 1.75% / 1.5% by tier | % | same | Oct 2026 | official |
| PayTech "lieu de commerce" (physical) offer | 25,000 FCFA joining fee + 11,800/month; cards 3% HT; mobile money 1.5% | n/a | same | Oct 2026 | official |
| **Flutterwave Senegal** collections | local cards **4.8%**, mobile money **2%**, international 4.8% (excl. VAT) | % | https://flutterwave.com/sn/pricing | Oct 2026 | official |
| **Flutterwave CI** collections | local cards 3.5%, mobile money 2.5%, international 4.8% (excl. VAT) | % | https://flutterwave.com/ci/pricing | Oct 2026 | official |
| PayDunya | 1.5–3.5% (sources disagree; the brief's 2.25% not confirmed) | % | https://afrotools.com/fr/blog/wave-vs-orange-money-senegal-2026/ and others | 2026 | unverified |
| CinetPay CI | 3.5% per mobile money or card transaction | % | https://support.cinetpay.com/d/52-tarifications-des-paiements-entrants-et-sortants (search summary) | undated | third-party |
| Paystack CI 1.95% (the brief's figure) | **not verified** (page returns 403) | % | https://paystack.com/ci/pricing | n/a | not found |
| **PI-SPI request-to-pay ("demande de paiement")** | Supported. Payment requests were **free** for individuals under the launch regime. Merchant (type C / legal-entity) receiving fees freely set by the participant. No BCEAO price for business RTP | n/a | https://mondedesbanques.com/culture-generale/pi-spi-tout-ce-quil-faut-savoir/ ; API Business communiqué (RTP and bulk listed) | Aug–Sep 2026 | press / official (feature) |
| Wholesale or volume pricing from aggregators | only PayTech's published volume tiers (above); others **not found** | n/a | n/a | n/a | n/a |

---

## 5. Taxes

| Item | Figure | Source | Date | Confidence |
|---|---|---|---|---|
| **Senegal TTA** (Taxe sur les transferts d'argent, CGI arts. 395–399 ter, Loi n°2025-17 of 27 Sep 2025): **0.5% per transaction, capped at 2,000 FCFA** | 0.5%, max 2,000 FCFA | https://cabex.sn/en/la-loi-n2025-17-du-27-septembre-2025-un-defi-dequilibre-entre-objectif-budgetaire-justice-fiscale-et-transformation-digitale/ | law of Sep 2025 | press (tax firm summary) |
| TTA base excludes the TTA itself, the TAF, and send or withdrawal commissions. The operator collects and remits by the 15th of the following month | n/a | same | n/a | press |
| TTA **exemptions**: cash deposits; withdrawals ≤ 20,000 FCFA/day; **bank transfers**; transfers inside the same provider's network; **salaries and scholarships**; State and local-authority operations | n/a | same; https://lesafriques.com/2026/09/banques-mobile-money-senegal-diaspora-2026/ | 2025–26 | press |
| Bank ↔ wallet treatment under the "virements bancaires" exemption | "doit être précisée par des textes d'application" (to be clarified by implementing texts) | cabex.sn (above) | n/a | unverified |
| TTA live at Orange Money from 16–17 Dec 2025; the 2,000 cap is stated "pour les clients particuliers" | n/a | https://lemarche.finance/transferts-dargent-mise-en-vigueur-de-la-tta-a-05-chez-orange-finances-mobiles-senegal/ | 12 Dec 2025 | press |
| **Separate 0.5% levy on payments received via a merchant code** (CGI art. 220 ter): withheld at source by the operator and remitted to the Treasury | 0.5% of amount received by the merchant | https://cabex.sn/... (above); https://www.lejournaldupole.com/la-niche-du-mobile-money-taxee/ | 2025 | press. Whether it is an advance on income tax or a final levy: **not determined** |
| **Pending change**: draft LFR 2026 would remove "la taxe de 1% sur chaque transaction immédiate du mobile money" (dating from Sep 2025) and replace it with a **contribution of 8% / 9% / 10% of e-money operators' turnover** (non-deductible). It is unclear whether this refers to the TTA plus the merchant levy. Adoption not confirmed: on 19 Sep 2026 the Assembly president said no complete LFR had been received | n/a | https://www.impact.sn/SENEGAL-Ce-que-dit-le-Projet-de-loi-de-finances-rectificative-2026-pour-l-economie-et-pour-les-contribuables_a59180.html (22 Sep 2026); https://www.seneplus.com/article/lfr-2026-la-mise-au-point | Sep 2026 | press / unverified |
| **Who pays on Kelen flows (Senegal)** | Salary payouts to wallets: **exempt**. Supplier payouts to wallets: TTA 0.5% max 2,000 applies (bank-origin exemption unclear). Collections via a merchant code: 0.5% levy on the merchant (uncapped per the texts found). Bank-to-bank transfers: exempt | derived from rows above | n/a | inference |
| **Senegal TAF** (taxe sur les activités financières) on banking, money-transfer and financial fees, **instead of VAT** | **17%** | https://taxsummaries.pwc.com/senegal/corporate/other-taxes | reviewed 31 Mar 2026 | third-party (PwC) |
| Bank tariffs quoted HT (BOA SN "Montant en F CFA HT"); Flutterwave and PayTech prices exclude VAT and taxes. Add the 17% TAF in Senegal to every fee Kelen pays | n/a | BOA PDF; Flutterwave page | 2026 | official |
| **Côte d'Ivoire TOB** (taxe sur les opérations bancaires) on bank commissions | **10%** (UBA CI grid: "TTHU 0,6% et TOB 10%") | https://www.ubacotedivoire.com/wp-content/uploads/sites/12/2026/04/Conditions-tarifaires-Entreprises-UBA-CI-2026.pdf | 2026 | official (bank grid) |
| CI tax on transfers outside UEMOA (TTHU) | 0.6% | same | 2026 | official |
| CI user-level mobile-money transfer tax in 2026 | **not found** in force. A 0.5% sender tax was in the 2018 finance-law annex (status disputed). A 7.2% pass-through of an operator tax from 2019 and a 5% levy on operators' turnover from 2021 were reported | https://www.agenceecofin.com/monetique/1001-53334-cote-d-ivoire-l-etat-impose-une-taxe-de-0-5-sur-le-transfert-d-argent-par-mobile ; https://momocalc.com/cote-divoire | 2018–2026 | unverified |
| CI informal "frais d'agence" of 100 FCFA per mobile-money operation at agents | 100 FCFA | https://www.koaci.com/article/2026/07/24/cote-divoire/societe/cote-divoire-taxe-de-100-fcfa-appliquee-sur-les-operations-mobile-money-dans-les-points-de-vente-les-operateurs-complices_198876.html | Jul 2026 | press |
| UBA CI stamp duty on cash deposit | 100 FCFA | UBA CI 2026 grid | 2026 | official |

---

## 6. Cash-in / cash-out (if Kelen clients deposit cash)

| Item | Figure | Source | Date | Confidence |
|---|---|---|---|---|
| Wave (consumer): "Déposez et retirez gratuitement" | free deposit and withdrawal | https://www.wave.com/fr/ (live) | Oct 2026 | official |
| Wave Business "Collecte": deposit your network's cash at Wave agents, credited instantly | price **not published** | https://www.wave.com/fr/business/ | Oct 2026 | official (no price) |
| Orange Money SN: withdrawals free (consumer) | free | https://lesafriques.com/2026/09/banques-mobile-money-senegal-diaspora-2026/ | Oct 2026 | third-party |
| MTN CI: deposit and withdrawal free since Aug 2025 | free | https://lesafriques.com/2026/09/mobile-money-banques-cote-ivoire-france-2026/ | Sep 2026 | third-party |
| Bank cash deposit at own bank: must be free (BCEAO list), stamp duty excluded | free (+ stamp duty) | https://www.bceao.int/fr/communique-presse/communique-de-presse-services-bancaires-offrir-titre-gratuit-par-les | 2014 | official |
| CI stamp duty on cash deposit | 100 FCFA | UBA CI 2026 | 2026 | official |
| TTA: cash deposits exempt; withdrawals ≤ 20k/day exempt | n/a | cabex.sn | 2025 | press |
| EME → bank funding or cash-in **cost to Kelen** (agent commission Kelen would pay if clients cash-in to a Kelen account via agents) | **not found** | n/a | n/a | not found |

---

## 7. Model inputs check

| Model input | Current model | Evidence (best sources) | Recommended low / **base** / high | Reasoning |
|---|---|---|---|---|
| **Salary paid to a wallet** | 0.4% (scenarios 0.8 / 0.4 / 0.25%) | Wave Business bulk **1%** uncapped (official). OM Paiement PRO **1% / 1.5%** (official). Bank → Wave **1% capped at 500 FCFA** (BOA SN, Wave). Flutterwave 2%. From 2 Nov 2026 the flow becomes a bank → EME **PI-SPI** transfer: **free to receive**, sender price unregulated for legal entities, ≤ 0.8% reference for individuals. Salaries **TTA-exempt**. +17% TAF on the fee | **0.20% / 0.50% / 1.0%** | The 0.4% base only holds via the PI-SPI route through the partner bank with a cap. Example: "1% max 500" on a 125k FCFA salary is 0.4%, and on 250k it is 0.2%. Public direct-to-operator price is 1%, so the high case should be **1.0%**, not 0.8%. Base 0.5% (before TAF) reflects uncertainty about the sponsor bank's PI-SPI business price. Better to model it as min(x%, cap) or a flat 250–500 FCFA per payout |
| **Salary paid to a bank account** | 100 FCFA / payout | Same-bank transfer **free** (BCEAO 2014 list). Online interbank: **150** (SG Sogecashnet, third-party), **750** (UBA CI online, official), 1,500/line multiple (BOA SN), 2,000 digital SICA (BOA SN). BCEAO SICA fee to banks: not published | **50 / 200 / 750 FCFA** | 100 FCFA is below every public price found except same-bank (0). It needs a partner-bank wholesale deal plus a meaningful share of same-bank employees. Base 200 is a negotiated SICA/PI-SPI line below SG's 150–750 retail range. High 750 is the UBA CI official online price. Add 17% TAF (SN) or 10% TOB (CI) |
| **Transfer out (supplier etc.)** | 250 FCFA | Same as above for ≤ 50M (SICA or PI-SPI). Transfers > **50M must use STAR (RTGS)**: retail 15,000–50,000 (BOA), 15,000 (UBA CI), 2,500 (SG Sogecashnet, third-party). Supplier payouts to **wallets** attract TTA 0.5% max 2,000 (SN) and 1% operator price | **150 / 300 / 750 FCFA** per bank transfer, + **RTGS surcharge of 2,500–15,000** on > 50M lines, + wallet-destination case at the wallet-salary % plus TTA | 250 is plausible for negotiated bulk SICA/PI-SPI lines but sits at the bottom of the public range. Model large-ticket supplier payments separately (STAR) and wallet suppliers separately (%, TTA) |
| **Payment links: operator/aggregator cost** | 0.7% (Kelen charges 1%) | Wave merchant **1%** after 20k/day free (official). OM merchant **1%** (official). PayTech mobile money **1.5–2.0%**, cards **2.5–3% HT**. Flutterwave mobile money 2–2.5%, cards 3.5–4.8%. UBA CI acquiring GIM **2%**, Visa/MC **3–3.5%**. PI-SPI RTP: no regulated merchant price. **Plus SN 0.5% merchant-code levy** (art. 220 ter; status under LFR 2026 uncertain) | **0.5% / 1.0% / 1.8%** blended (cards priced separately at 2.5–3.5%) | 0.7% is below every published direct-operator merchant price (1%). It needs negotiated Wave/OM rates or a high share of PI-SPI RTP/QR collections. With Kelen charging 1%, the base case margin is about 0 before TAF and the 0.5% levy. Recommend repricing collections to 1.5% (or pass-through for cards) or modelling the 0.7% only as an upside scenario once PI-SPI RTP is the main rail |

### Key open items to obtain from partners (cannot be found publicly)
1. Partner/sponsor bank price for **PI-SPI API Business** sends (per line, or % plus cap) to wallets and to bank accounts, and whether BCEAO charges participants per transaction.
2. Wave and Orange negotiated B2B rates for payouts and Checkout at Kelen's expected volume. Wave states no public wholesale price.
3. BCEAO SICA/STAR fees billed to the partner bank. These were only evidenced indirectly (2020 Avis).
4. Final text of the Senegal **LFR 2026**: whether the TTA and the 0.5% merchant levy are abolished and replaced by the operator turnover contribution.
5. CI: confirm the absence of a user-level mobile-money tax in 2026, and check that TOB 10% applies to fintech-agent fees.
