# B. Mobile money and payment players: Senegal (SN) and Côte d'Ivoire (CI)

*Competitor research for Kelen (B2B neobank for SMEs; SN launch 2027, then CI). Research date: 2026-10-14.*

**Conventions**
- Every fact has a source link and a date. "Pub." is the publication date. "Accessed 2026-10-14" is used for undated official pages.
- **[UNVERIFIED]** means a single secondary source, a vendor blog, or conflicting sources.
- **"Not published"** means no official figure was found. No price in this file is estimated.
- Licence abbreviations:
  - **EME**: établissement de monnaie électronique (e-money institution).
  - **EP**: établissement de paiement (payment institution, BCEAO Instruction 001-01-2024).
  - **Bank**: licensed by the Commission Bancaire UMOA.
- Djamo is out of scope (covered by another researcher). Julaya appears only as context.
- Research limit: the shared web-search budget ran out near the end of the work. A few items (Paystack transfer fees, Kkiapay licence date, Wizall licence) could not be checked further and are flagged.

---

## 0. Key takeaways for Kelen

1. **Wave is the price anchor and the main threat.** Wave Business charges **1% to the sender for bulk payments, and the recipient pays nothing**. Merchants get **the first 20,000 FCFA per day free, then 1%**. Wave also has a public Payout/Batch API.
   - Kelen's price comparison: an SME paying 3M FCFA of salaries per month pays about 30,000 FCFA to Wave. That is roughly the price of Kelen's "Moyenne" plan (29,900 FCFA).
   - Wave incorporated **Wave Bank Africa S.A.** in Abidjan with 20 bn FCFA of capital (Oct 2025). A banking licence is **not confirmed** as of Aug 2026.
   - Wave announced credit and savings in Feb 2026. Sources: [wave.com/fr/business](https://www.wave.com/fr/business/) (accessed 2026-10-14); [Financial Afrik, 2026-08-30](https://www.financialafrik.com/2026/08/30/telecoms-et-fintechs-a-lassaut-de-la-banque-lumoa-peut-elle-encore-attendre-la-rupture/).
2. **Orange is moving into SME banking through two arms:**
   - OM Business app in CI (launched 19 Jun 2026), with credit via Orange Bank Africa.
   - Orange Bank Africa: 3M clients, 640 bn FCFA of credit since 2020, and a 17 bn FCFA SGPME guarantee for SMEs in CI (Jul 2026).
   - In Senegal, Orange's published B2B prices are **1% merchant** and **1%/1.5% "Paiement Pro"** (salaries and suppliers). Source: [orangebusiness.sn](https://www.orangebusiness.sn/orange-money).
3. **PI-SPI changes the economics of payouts.** The BCEAO instant-payment system (live since 30 Sep 2025) is free for individuals sending money. Receivers get 30 free receipts per month, then fees are capped at 1% ([Le Jecos, 2026-10-02](https://www.lejecos.com/PI-SPI-Le-piege-tarifaire-de-Wave_a31598.html)).
   - Wave, Orange, Mixx, MTN, Moov and InTouch's TouchPoint (probable) are all on the 30 Sep 2026 list. Kelen can reach every wallet and bank through PI-SPI by way of its partner bank. This undercuts the 1–2% payout fees charged by wallets and aggregators.
4. **Aggregators are mostly partners, not competitors.**
   - Published payout fees run 1.5–2% (PayDunya, CinetPay, Flutterwave). Collection fees run 1.5–3%.
   - None of them offers accounts, IBANs, approval workflows or payroll as a product.
   - The best rail or aggregation partner candidates are InTouch (EME in SN), PayDunya (EP in SN, owned by Peach Payments) and Hub2 (infrastructure only).
5. **Market structure (BCEAO 2024, UEMOA-wide):**
   - Orange leads on value (41.3%), with Wave close behind (38.2%).
   - On transaction volume, Orange has 38.4% and Wave 28.4% (the report gives 23% in another paragraph).
   - Senegal and CI together hold about 65% of UEMOA e-money transaction value.
   - In CI, Wave holds **70% of merchant payments** (INS, Apr 2024).

---

## 1. Market share and market data

### 1a. UEMOA-wide shares by network (BCEAO, year 2024)
Source: [BCEAO, *Rapport annuel sur les services financiers numériques dans l'UEMOA – 2024*](https://www.bceao.int/sites/default/files/2026-03/Rapport%20annuel%20sur%20les%20services%20financiers%20num%C3%A9riques%20dans%20l'UEMOA%20-%202024.pdf) (PDF posted 2026-03), §9, §22–26.

| Network | Accounts opened 2023 | Accounts opened 2024 | Tx volume 2023 | Tx volume 2024 | Tx value 2023 | Tx value 2024 |
|---|---|---|---|---|---|---|
| Orange | 25.4% | 23.0% | 42.0% | 38.4% | 43.3% | 41.3% |
| Wave | 20.1% | 22.1% | 21.4% (19% in §22) | 28.4% (23% in §22) | 34.0% | 38.2% |
| MTN | 19.5% | 16.6% | 21.5% | 17.4% | 16.3% | 11.7% |
| Moov | 16.6% | 18.4% | 5.3% | 6.9% | 2.8% | 2.6% |
| Yas (Mixx) | 4.1% | 5.1% | 3.0% | 3.0% | 2.1% | 2.0% |
| Others | n/a | n/a | 6.8% | 5.9% | 4.1% | 1.7% |

Note: the BCEAO report contradicts itself on Wave's volume share (§22 says 19%→23%; §23 says 21.4%→28.4%). Secondary coverage: [Launch Base Africa, 2026-03-24](https://launchbaseafrica.com/2026/03/24/the-267bn-crown-wave-edges-closer-to-dethroning-orange-in-west-africa/).

### 1b. Country totals (BCEAO 2024, Annex 2)

| Indicator (2024) | Senegal | Côte d'Ivoire | UEMOA |
|---|---|---|---|
| E-money accounts opened | 42,579,300 (17.1% of UEMOA) | 99,649,204 (40.1%) | 248,710,918 |
| Active accounts (90 days) | 14,648,818 (34.4% active) | 26,370,627 (26.5%) | 76,863,533 |
| Service points | 298,359 | 424,562 | 1,590,243 |
| Merchants registered for merchant payment | 412,172 | 2,719,463 | 3,705,726 |
| Number of transactions | 2.874 bn (24.1%, #1 in UEMOA) | 2.549 bn (21.4%) | 11.92 bn |
| Value of transactions (bn FCFA) | 48,487 (30.2%) | 55,728 (34.7%) | 160,415 |
| E-money issuers, by type (Table 1) | 1 telco-bank, 7 bank/fintech, 3 EME = 11 | 14 bank/fintech, 3 EME, 1 IMF, 1 Treasury = 19 | 69 |

Source: same BCEAO report, Annex 2 and Table 1.

### 1c. Senegal: operator-level data (no official split by operator is published)

| Operator | Metric | Value | Date | Source |
|---|---|---|---|---|
| Orange Money (Sonatel) | Active clients | 13,029,465 (+2.8%) | FY2025 | [Sonatel FY2025 BRVM deck, 2026-02-16](https://sonatel.sn/wp-content/uploads/2026/03/BRVM-FY-2025-FR-VF.pdf); [Sonatel results page](https://sonatel.sn/resultats-consolides-du-groupe-sonatel-senegal-mali-guinee-guinee-bissau-sierra-leone-au-31-decembre-2025/) |
| Orange Money (Sonatel) | Transactions | ~3.79 bn | 2025 | [Seneweb, 2026-02-17](https://www.seneweb.com/en/news/Economie/gros-benefice-en-2025-chiffre-daffaires-revenus-orange-money-sonatel-devoile-ses-chiffres_n_483798.html) |
| Orange Money (Sonatel) | Revenue | 208.9 bn FCFA **[UNVERIFIED; the deck may show 130.1 bn]** | 2025 | Seneweb (above) |
| Orange Money | Withdrawal points | ~90,000 **[UNVERIFIED]** | 2026 | [Les Afriques, 2026-09](https://lesafriques.com/2026/09/banques-mobile-money-senegal-diaspora-2026/) |
| Wave | Clients claimed | ~11 million | 2026-10 | [Le Jecos, 2026-10-02](https://www.lejecos.com/PI-SPI-Le-piege-tarifaire-de-Wave_a31598.html) |
| Wave | Regular users | 7.18 million **[UNVERIFIED]** | 2026 | [Les Afriques, 2026-09](https://lesafriques.com/2026/09/banques-mobile-money-senegal-diaspora-2026/) |
| Wave | "Active users" | >10 million (claim) | 2026-01 | [Financial Afrik, 2026-01-24](https://www.financialafrik.com/2026/01/24/senegal-wave-lance-une-carte-virtuelle-avec-visa-et-ecobank/) |
| Mixx by Yas | Users | Not published | n/a | n/a |
| Market | Licensed payment institutions in SN | 11 (of 31 in UEMOA) | 2026-02-28 | [Seneweb, 2026-09-23](https://seneweb.com/en/news/Economie/mobile-money-pourquoi-le-duel-orange-money-wave-ne-resume-plus-le-marche_n_505004.html) |

Comment: the operator claims (Orange 13.0M + Wave 7–11M + Mixx) exceed the BCEAO's 14.6M active accounts for 2024. That gap points to heavy multi-homing. Several secondary sources say Wave leads Senegal by users or volume, but **no official Wave-vs-Orange split for Senegal was found**.

### 1d. Côte d'Ivoire: operator-level data

| Operator | Metric | Value | Date | Source |
|---|---|---|---|---|
| Orange Money CI | Mobile money subscribers (ARTCI) | 16,216,656 | 2025-06-30 | [KOACI, 2025-09-11](https://www.koaci.com/index.php/article/2025/09/11/cote-divoire/societe/cote-divoire-telephonie-mobile-59942676-dabonnes-au-30-juin-2025-et-un-chiffre-daffaires-de-plus-de-257-milliards-ht_190072.html) |
| MTN MoMo CI | Mobile money subscribers (ARTCI) | 7,990,791 | 2025-06-30 | KOACI (above) |
| Moov Money CI | Mobile money subscribers (ARTCI) | 2,314,128 | 2025-06-30 | KOACI (above) |
| Wave CI | Not in ARTCI data (Wave is not a telecom operator) | n/a | n/a | n/a |
| Orange Money CI | Self-declared mobile money share | 58%; >20M users; 65,000 points of sale | 2025 (published 2026-06) | [Boursorama forum relaying Agence Ecofin, 2026-06-22](https://www.boursorama.com/bourse/forum/1rPORA/detail/468135190/); [Agence Ecofin](https://www.agenceecofin.com/actualites-services/2106-139474-orange-money-ci-lance-om-business-pour-accelerer-la-digitalisation-des-commerces-et-pme) |
| Wave CI | Share of merchant payments | **70%** | INS survey, Apr 2024 | [Ecomatin, 2025-09-01](https://ecomatin.net/mobile-money-mtn-cote-divoire-tente-le-0-de-frais-pour-contrer-wave) |
| Wave CI | Share of classic transfers | 31% | INS, Apr 2024 | Ecomatin (above) |
| MTN MoMo CI | Share of classic transfers | 23.5% | INS, Apr 2024 | Ecomatin (above) |
| Wave CI | Accounts opened | >20 million | 2026-08 | [Financial Afrik, 2026-08-30](https://www.financialafrik.com/2026/08/30/telecoms-et-fintechs-a-lassaut-de-la-banque-lumoa-peut-elle-encore-attendre-la-rupture/) |
| MTN MoMo CI | Active users | 4.8M (down from 6.3M in 2021) | 2024 | Ecomatin (above) |
| Moov Money CI | Active users; points | >4.2M; ~70,000 | 2026-07 | [KOACI, 2026-07-16](https://www.koaci.com/article/2026/07/16/cote-divoire/societe/cote-divoire-20-ans-de-moov-africa-cote-divoire-loperateur-voit-grand-et-accelere-sa-revolution-digitale_198629.html) |
| Context | Individual bank accounts in CI | 7.2M across 28 banks | 2026 | Financial Afrik, 2026-08-30 |

Secondary estimates of CI shares vary widely (Wave from 18% to about 40%) and are **[UNVERIFIED]**: [Simiz, 2026](https://simiz.io/blog/marche-paiement-mobile-uemoa-2026).

### 1e. PI-SPI participation (BCEAO instant payment system)

PI-SPI launched on 30 Sep 2025. The final deadline for all banks, EMEs and EPs was 30 Sep 2026, after being extended from 30 Jun.
- Official BCEAO list of **16 Sep 2026** (123 participants): [PDF](https://www.bceao.int/sites/default/files/2026-09/Liste%20des%20participants_PI-SPI_sept2026.pdf).
- List of **30 Sep 2026** (175 participants; SN 43, CI 38): [Financial Afrik, 2026-10-01](https://www.financialafrik.com/2026/10/01/bceao-liste-des-175-participants-autorises-a-ouvrir-les-services-de-pi-spi-au-public-au-30-septembre-2026/).

| Player | SN, 16 Sep 2026 | SN, 30 Sep 2026 | CI, 16 Sep 2026 | CI, 30 Sep 2026 |
|---|---|---|---|---|
| Wave (Wave Digital Finance / Wave Côte d'Ivoire) | No | **Yes** | No | **Yes** |
| Orange (Orange Finances Mobiles SN / Orange Money CI) | Yes | Yes | Yes | Yes |
| Orange Bank Africa | Yes | Yes | Yes | Yes |
| Mixx by Yas (Mobile Cash SA) | Yes | Yes | n/a | n/a |
| MTN Money | n/a | n/a | Yes | Yes |
| Moov Money | n/a | n/a | No | **Yes** |
| TouchPoint Financial Services (probably InTouch **[UNVERIFIED link]**) | Yes | Yes | Yes | Yes |
| Wizall, PayDunya, CinetPay, PayTech, Hub2, Kkiapay, NabooPay, Flutterwave, Paystack | No | No | No | No |
| For reference: Djamo, Julaya, Mikaty, Samir Money, SesaPay, Versus Finances Tech, Quick Pay, African Financial Agent (SN); Paymetrust, Sycapay, Connekt4 (CI) | partly | Yes | partly | Yes |

PI-SPI fee rules, as reported by [Le Jecos, 2026-10-02](https://www.lejecos.com/PI-SPI-Le-piege-tarifaire-de-Wave_a31598.html):
- Individuals pay nothing to send domestically or to pay a merchant.
- Receivers get the first 30 receipts per month free. Above that, fees are capped by the BCEAO at 1% of the amount received.
- Wave has not said which PI-SPI services it will activate, or at what price. It still charges 1% on Wave-to-Wave transfers.

[allAfrica, 2026-10-02](https://allafrica.com/stories/202610050727.html) confirms Wave joined PI-SPI for CI on 30 Sep 2026, after being absent from the 31 Jul list.

---

## 2. Player profiles

### 2.1 Wave (Wave Mobile Money / Wave Digital Finance / Wave Côte d'Ivoire)

| Field | Detail | Source (date) |
|---|---|---|
| What it is | Low-fee mobile money wallet: free deposits and withdrawals, 1% to send. Agent network; app and QR payments. | [wave.com/en](https://www.wave.com/en/) (accessed 2026-10-14) |
| Countries | 8 West African countries per June 2025 coverage, including SN, CI and Niger (EME agreement via Ecobank Niger in 2024). Also Uganda (group). Full list **[UNVERIFIED]**. | [Dabafinance / TechCabal summary, 2025-06-30](https://dabafinance.com/en/news/wave-raises-137m-debt-round-mobile-money-expansion-africa-2025); BCEAO SFN 2024 report, footnote 1 |
| Licence | **EME** (Wave Digital Finance), BCEAO, 14 Apr 2022: the first non-telco, non-bank EME in the UEMOA. | [Wave blog](https://www.wave.com/en/blog/sn-emi/); [Droit Médias Finance](https://droitmediasfinance.com/index.php/actualites/droit-tech-fintech/353-uemoa-l-agrement-communautaire-de-wave-digital-finance-comme-etablissement-de-monnaie-electronique) |
| Bank project | **Wave Bank Africa S.A.**, incorporated in Abidjan, capital 20 bn FCFA (~$32M), formalised 24 Oct 2025. Planned services: deposits, lending, accounts, payments. **No banking licence confirmed** ("la constitution d'une société ne vaut pas encore agrément bancaire", Aug 2026). The Rio Times (Sep 2026) says Wave "secures a bank licence" but cites no primary source **[UNVERIFIED]**. | [Ecofin Agency, 2025-10-26](https://www.ecofinagency.com/news-finances/2610-49842-wave-launches-commercial-bank-in-cote-d-ivoire); [Financial Afrik, 2026-08-30](https://www.financialafrik.com/2026/08/30/telecoms-et-fintechs-a-lassaut-de-la-banque-lumoa-peut-elle-encore-attendre-la-rupture/); [Rio Times, 2026-09-07](https://www.riotimesonline.com/africa-mobile-money-fintech-2026/) |
| Owner / funding | Founders Drew Durbin and Lincoln Quirk; private. Series A of $200M at a **$1.7bn valuation** (2021). Debt facility of **€117M (~$137M)** led by Rand Merchant Bank with BII, Finnfund and Norfund (30 Jun 2025). Cumulative funding about $439–442M. No new valuation disclosed. | [Africa Markets, 2025](https://africamarkets.com/deals/wave-mobile-money-debt-2025); [Fintech News Africa, 2025-07](https://fintechnews.africa/45533/senegal/wave-137m-debt-funding/) |
| Users / volumes | Group: >20M monthly users, ~150,000 agents, ~3,000 staff (Jun 2025). SN: ~11M clients (Oct 2026). CI: >20M accounts opened (Aug 2026). UEMOA value share 38.2% (2024). | Dabafinance (2025-06-30); Le Jecos (2026-10-02); Financial Afrik (2026-08-30); BCEAO SFN 2024 |
| Business products | **Wave Business**: in-person collections in the business app (QR), **bulk payments** (recipients can cash out at any agent without a Wave account), payment collection, **Checkout API**, **Payout API with batch endpoint** (`/v1/payout-batch`), B2B Payout API, multi-user business accounts. Virtual Visa card with Ecobank SN (Jan 2026, consumer). | [wave.com/fr/business](https://www.wave.com/fr/business/) (accessed 2026-10-14); [docs.wave.com/payout](https://docs.wave.com/payout); [docs.wave.com/b2b/payout](https://docs.wave.com/b2b/payout); [Financial Afrik, 2026-01-24](https://www.financialafrik.com/2026/01/24/senegal-wave-lance-une-carte-virtuelle-avec-visa-et-ecobank/) |
| Business pricing (official) | **Bulk payments: 1% paid by the sender, free for the recipient.** **In-person collections: first 20,000 FCFA per day free, then 1%.** API payout examples in the docs: fee of 150 on 15,000 XOF (= 1%). | wave.com/fr/business (page appears about 2 years old; accessed 2026-10-14); docs.wave.com/payout |
| Business pricing (secondary) | 1% transfer fee capped at 5,000 FCFA (Le Jecos, 2026-10). Bank settlement: "free/instant" (Simiz) vs "250 FCFA" (other guide). Wave Business limits of ~10M FCFA balance and ~100M FCFA per month **[UNVERIFIED]**. | [Le Jecos](https://www.lejecos.com/PI-SPI-Le-piege-tarifaire-de-Wave_a31598.html); [Simiz CI, 2026-08-25](https://simiz.io/blog/ouvrir-compte-marchand-wave-cote-ivoire); [Simiz SN](https://simiz.io/blog/ouvrir-compte-marchand-wave-senegal) |
| Consumer pricing | Deposits, withdrawals and bills free; sending 1%. | wave.com/en (accessed 2026-10-14) |
| Account fees | Not published (no subscription mentioned for Wave Business). | n/a |
| Credit / savings / insurance | Feb 2026: credit and savings "in the coming months", insurance later. Jun 2026: car and motorbike insurance with Baloon live in the app. **No confirmed launch of credit or savings found** as of Oct 2026. | [Financial Afrik interview, 2026-02-18](https://www.financialafrik.com/2026/02/18/entretien-exclusif-avec-el-hadji-malick-gueye-directeur-general-de-wave-digital-finance/); [Seneweb (Baloon), 2026](https://www.seneweb.com/fr/news/Societe/wave-et-baloon-deploient-leur-service-dassurance-automobile-et-moto-100-digital-au-senegal_n_495143.html) |
| Target segment | Mass market consumers, micro-merchants, SMEs and large payers (bulk). Government: the Caisse de sécurité sociale pays some benefits to Wave accounts (Sep 2026). | [Senego, 2026-09](https://senego.com/senegal-samba-diouf-discute-avec-wave-des-perspectives-de-collaboration-pour-les-services-publics_2002560.html) |
| Strengths | Lowest prices, huge user base in SN and CI, merchant leadership in CI (70%), free cash-out for recipients, simple API, brand trust, PI-SPI participant since 30 Sep 2026. | as above |
| Weaknesses | No IBAN or bank account (EME only; balance caps such as 2M FCFA for individuals). Single-rail. No approval workflows, accounting or invoicing for SMEs (none documented). Bank licence still pending. Thin, slow-changing published business pricing. | [Payments.gi Senegal monitor](https://payments.gi/jurisdictions/senegal/); wave.com/fr/business |
| Recent moves 2025–26 | Jun 2025: €117M debt. Oct 2025: Wave Bank Africa S.A. Jan 2026: virtual Visa card. Feb 2026: credit and savings announced. Jun 2026: insurance. 30 Sep 2026: joins PI-SPI in SN and CI. | as above |
| **Threat to Kelen** | **HIGH.** Wave Business already covers bulk payouts, collections and an API at 1%, with free cash-out. If Wave Bank Africa gets licensed, Wave could add accounts and SME lending in CI. Wave is the default rail SMEs already use. Kelen's edge is the bank account and IBAN, multi-rail payroll, approvals, invoices, and accounting exports. | analysis |
| Partner potential | **Yes, as a rail.** Pay out to Wave wallets via PI-SPI (through the partner bank) or via the Wave Payout API (an `aggregated_merchant_id` exists for approved aggregators). Cash-in from Wave to a Kelen account via the Checkout API or PI-SPI. | [docs.wave.com/payout](https://docs.wave.com/payout) |

### 2.2 Orange Money (Orange Finances Mobiles Sénégal / Orange Money CI), Max it, Orange Bank Africa

| Field | Detail | Source (date) |
|---|---|---|
| What it is | The largest telco wallet in the UEMOA. Max it is Orange's super-app, with Orange Money as its payment engine. Orange Bank Africa (OBA) is Orange's digital bank (CI headquarters plus a Senegal branch). | [Orange newsroom (Max it)](https://newsroom.orange.com/orange-introduces-its-super-app-max-it-to-simplify-everyday-life-for-people-in-africa-and-the-middle-east/) |
| Countries | Orange Money in 17 countries (group). SN via Sonatel, CI via Orange CI. | [KOACI, 2025-02-19](https://www.koaci.com/index.php/article/2025/02/19/cote-divoire/economie/cote-divoire-orange-money-atteint-40-millions-de-clients-actifs-et-inaugure-son-siege-a-abidjan-renforcant-son-ancrage-en-afrique-et-au-moyen-orient_184648.html) |
| Licence | Orange Money: **EME** entities (Orange Finances Mobiles Sénégal; Orange Money CI). Licence dates not verified **[UNVERIFIED]**. OBA: **bank**, approved in the UMOA, with a Senegal branch authorised by the Commission Bancaire. | PI-SPI lists; [Droit Médias Finance](https://www.droitmediasfinance.com/index.php/actualites/droit-tech-fintech/615-senegal-orange-bank-africa-oba-recoit-lautorisation-douvrir-une-succursale-senegalaise); Financial Afrik 2026-08-30 |
| Owner | Orange SA through Sonatel (SN, listed on the BRVM) and Orange CI (listed on the BRVM). OBA: Orange plus NSIA (historical partner) **[UNVERIFIED current cap table]**. | n/a |
| Users / volumes | Group: 40M monthly active users (Feb 2025). SN: 13.03M active clients, ~3.79bn transactions (FY2025). CI: 16.2M ARTCI subscribers (Jun 2025); claims 58% share and >20M users. Max it: ~25M users (Mar 2026), target 75M by end 2028. OBA: **3M clients (80% CI, 20% SN), 640 bn FCFA of credit and 585 bn FCFA of savings since 2020** (data published Feb 2026). | KOACI 2025-02-19; Sonatel FY2025 deck; KOACI 2025-09-11; [Developing Telecoms, 2026-03](https://developingtelecoms.com/telecom-business/operator-news/19961-orange-targets-75-million-users-for-max-it-super-app-as-africa-growth-accelerates.html); Financial Afrik 2026-08-30 |
| Business products, SN | **Paiement Marchand** (Orange supplies phones and SIMs). **Paiement Internet** (API). **Paiement Pro** (supplier invoices, salaries, bonuses, per diems via a web platform; recipients without OM get a code). Salary sub-accounts. App "Maxi Business Sénégal". | [orangebusiness.sn/orange-money](https://www.orangebusiness.sn/orange-money) (accessed 2026-10-14) |
| Business pricing, SN (official) | Subscription free. **Merchant and internet payments: 1% commission** paid by the merchant, free for the customer. **Paiement Pro: 1% if the recipient has OM, 1.5% if not**; payer pays, recipient withdraws free. Settlement to bank **D+5**. Back office and hotline free. | orangebusiness.sn (accessed 2026-10-14) |
| Business products, CI | Orange Money Business (SMEs, large companies, administrations, NGOs), Paiement Petits Commerces, FastPay (collections), online payment and QR, **Paiement de Salaires et Primes**. **OM Business app** launched **19 Jun 2026**: QR, payment links, dashboard, **credit via Orange Bank**. | [business.orange.ci offers](https://business.orange.ci/fr/offres-om-encaissement.html) (accessed 2026-10-14); [AITN, 2026-06](https://afriqueitnews.com/fintech/cote-divoire-orange-money-lance-om-business-pour-commercants-et-pme/); [Agence Ecofin, 2026-06-21](https://www.agenceecofin.com/actualites-services/2106-139474-orange-money-ci-lance-om-business-pour-accelerer-la-digitalisation-des-commerces-et-pme) |
| Business pricing, CI | **Salary payments (official contract annex, dated 2016 but still hosted): 2.0% for funding of 1,000–999,999 F; 1.5% for 1M–4.99M F; 1.0% from 5M F**, plus the recipient pays the normal withdrawal fee. Merchant commission: **not published** (set in a contract annex). Secondary sources give 0.5–2.5% plus 75,000 FCFA opening, 35,000 FCFA per month API fee and 0.5% settlement **[UNVERIFIED]**. | [business.orange.ci salary annex PDF](https://business.orange.ci/business/resources/other/annexes_paiement_salaire.pdf) (PDF dated 2016-05-24); [Simiz, 2026-08-25](https://simiz.io/blog/ouvrir-compte-marchand-wave-cote-ivoire) |
| Consumer pricing, CI | National transfer to Orange: 0 FCFA to send, **1% to withdraw** on receipt. Cash-out grid from 100 FCFA (200–2,000) to 19,900 FCFA (1M–1.5M). OM Visa card: 8,000–10,000 FCFA. | [orange.ci tarifs](https://www.orange.ci/fr/tarifs-orange-money.html); [business.orange.ci tarifs](https://business.orange.ci/fr/tarifs-orange-money.html) (accessed 2026-10-14) |
| SME lending | OBA + **SGPME**: two portfolio guarantee agreements of ~17 bn FCFA (up to $29.5M) for TPE, PME and ETI in CI, including a women-led envelope (22–24 Jul 2026). OBA + IFC risk-sharing (2023) for digital loans to small businesses, CI then SN. SN consumer loans: **Tik Tak / Tik Tak+** (51,000–500,000 FCFA, 90 days). **No confirmed SME loan product in SN.** | [Agence Ecofin, 2026-07](https://www.agenceecofin.com/actualites-finance/2607-140511-la-sgpme-et-orange-bank-africa-mobiliseront-jusqua-29-5-millions-pour-faciliter-le-credit-aux-pme-en-cote-divoire); [KOACI, 2026-07-24](https://www.koaci.com/article/2026/07/24/cote-divoire/economie/cote-divoire-financement-des-mpme-orange-bank-africa-et-la-sgpme-sengagent-a-mobiliser-17-milliards-fcfa-pour-booster-la-croissance-des-entreprises-ivoiriennes_198899.html); [IFC, 2023](https://www.ifc.org/fr/pressroom/2023/27646); [orangebank.sn Tik Tak+](https://orangebank.sn/pret-tik-tak-plus) |
| Target segment | Mass market. Micro-merchants up to large accounts and administrations. OBA: individuals plus micro and small businesses. | as above |
| Strengths | Largest base and densest agent network. Bank in the group (OBA) with SME credit and a guarantee line. B2B sales force. PI-SPI participant (OM and OBA in both countries). | as above |
| Weaknesses | Higher consumer fees than Wave; losing value share (43.3% to 41.3%). Settlement at D+5 in SN. Business tools are telco-style (SIMs, back-office), not a banking UX. Pricing opaque in CI. | BCEAO SFN 2024; orangebusiness.sn |
| Recent moves 2025–26 | Mar 2026: Max it target of 75M users. Jun 2026: OM Business in CI. Jul 2026: OBA–SGPME 17 bn FCFA. 2025: Sonatel OM base +2.8%. | as above |
| **Threat to Kelen** | **MEDIUM-HIGH**, highest in CI, where OM Business plus OBA credit now targets SMEs directly. In SN, Paiement Pro (1%/1.5%) competes with Kelen's payroll. OBA could become an SME neobank competitor. | analysis |
| Partner potential | **Yes, as a rail** (OM API for collections and payouts, or via PI-SPI). OBA is a **possible partner bank or lending partner**, though with a conflict of interest. | analysis |

### 2.3 Free Money → Mixx by Yas (Senegal)

| Field | Detail | Source (date) |
|---|---|---|
| What it is | The wallet of telco Yas (formerly Free Sénégal). Rebranded **Free Money → Mixx by Yas** on 26–27 Nov 2024. | [prixdakar](https://prixdakar.com/free-senegal-devient-yas-free-money-devient-mixx-by-yas/); [TechAfrica News, 2024-11-26](https://techafricanews.com/2024/11/26/axian-telecom-rebrands-across-africa-with-yas-and-mixx-by-yas-for-unified-digital-future/) |
| Countries | Mixx: Senegal, Togo, Tanzania (Axian). | TechAfrica News |
| Licence | Legal entity **Mobile Cash SA (Mixx Sénégal)**, a PI-SPI participant. EME status **[UNVERIFIED]**; the BCEAO counts one telco-bank partnership and 3 EMEs in SN. | BCEAO PI-SPI list (2026-09-16); BCEAO SFN 2024 Table 1 |
| Owner | **Axian Telecom** (Madagascar group), which acquired 80% of Free Sénégal. | [Wikipedia FR Yas Sénégal](https://fr.wikipedia.org/wiki/Yas_S%C3%A9n%C3%A9gal) |
| Users / volumes | Not published. UEMOA share of Yas (SN + Togo): 5.1% of accounts, 3% of volume, 2% of value (2024). | BCEAO SFN 2024 |
| Business products | **Mixx Business Suite (Flexpay)**: user access management, **salary, supplier and invoice payments**, loan management, cash collection. Mixx Business merchant app (updated Jul 2026). **Mixx Mastercard** prepaid card with Ecobank SN (Jun 2025), aimed partly at freelancers and small businesses. **Lebalma** nano-credit up to 300,000 FCFA. | [yas.sn/mixx-by-yas](https://yas.sn/mixx-by-yas/) (accessed 2026-10-14); [AITN](https://afriqueitnews.com/finance/mixx-by-yas-lance-carte-prepayee-mixx-mastercard-paiements-senegal/); [Google Play Mixx Business](https://play.google.com/store/apps/details?id=sn.mixx.merchant.app&hl=en_US) |
| Pricing (official) | National transfer: free to send. Receipt: free for the first 30 per month, then 0.5%. **Merchant payment: free for the payer; 1% (incl. 0.5% tax) paid by the merchant.** Cash-out "Canal Mixx": 1%. International: 1.5%. Mixx Business Suite bulk fees: **not published**. | yas.sn/mixx-by-yas (accessed 2026-10-14) |
| Target segment | Mass market and youth. Freelancers and small businesses (card). | as above |
| Strengths | Free P2P (mirrors PI-SPI rules). Bulk and salary tool. Card with Ecobank. PI-SPI participant since the first lists. | as above |
| Weaknesses | Small share (about 3% of UEMOA volume). Limited agent network (FAQ says "2,000 POS" or "6,000 agents"). No published business pricing. | yas.sn; BCEAO |
| Recent moves 2025–26 | Jun 2025: Mixx Mastercard. Dec 2025: first anniversary. 2026: Lebalma credit and merchant app updates. | [Osiris, 2025-12-16](https://www.osiris.sn/mixx-senegal-une-premiere-annee-sous-le-signe-de-l-inclusion-et-de-l-innovation.html) |
| **Threat to Kelen** | **LOW-MEDIUM.** The Business Suite overlaps with payroll, but the brand is weak with SMEs. | analysis |
| Partner potential | **Yes, as a rail** (via PI-SPI or aggregators). | analysis |

### 2.4 MTN MoMo Côte d'Ivoire (MoMo, MoMo Pay, MoMo Business)

| Field | Detail | Source (date) |
|---|---|---|
| What it is | MTN CI's mobile money service (second telco wallet in CI). MoMo Pay for merchant payments. | [mtn.ci/momo](https://www.mtn.ci/momo/) (accessed 2026-10-14) |
| Countries | CI (MTN group: 16 fintech markets). Not present in SN. | Financial Afrik 2026-08-30 |
| Licence | Entity "MTN Money" in PI-SPI CI. Licence type (EME vs bank partnership) **[UNVERIFIED]**. | Financial Afrik PI-SPI list 2026-10-01 |
| Owner | MTN Group. Group fintech: 301M clients, $342bn of transactions (+38%). On 25 Aug 2026, MTN said it is exploring **bank licences** in several African markets. | Financial Afrik 2026-08-30 |
| Users / volumes, CI | 7.99M ARTCI subscribers (Jun 2025). 4.8M active users (2024, down from 6.3M in 2021). MoMo CI revenue 13.2 bn FCFA in H1 2025 (−11.5%). 23.5% of transfers (INS, Apr 2024). UEMOA value share 11.7% (2024). | KOACI 2025-09-11; [Ecomatin, 2025-09-01](https://ecomatin.net/mobile-money-mtn-cote-divoire-tente-le-0-de-frais-pour-contrer-wave); BCEAO SFN 2024 |
| Business products | MoMo Pay, a "Business" section, developer API. **MoMo Helep Pro**: employer salary advance up to 100,000 FCFA (presented 19 Jun 2026). Micro-loans and savings with Bridge Bank (older product). | [mtnpromote.com](https://www.mtnpromote.com/) (2026); [Agence Ecofin (Bridge Bank)](https://www.agenceecofin.com/operateur/2507-58900-cote-d-ivoire-mtn-mobile-money-et-bridge-bank-lancent-le-premier-service-de-micro-pret-et-micro-epargne-sur-mobile) |
| Business pricing | **Not published** on mtn.ci. Secondary estimates: merchant 1–2%, direct API ~1.5%, setup 400k–900k FCFA **[UNVERIFIED]**. | [mtn.ci marchands](https://www.mtn.ci/momo/marchands-momo/) (accessed 2026-10-14); [Kolonell, 2026](https://kolonell.com/fr/blog/mtn-momo-api-integration-site-web-cote-ivoire-2026) |
| Consumer pricing | Since 28 Aug 2025: **0% on deposits, transfers and withdrawals via the MoMo app** (to counter Wave). | [KOACI, 2025-09-02](https://www.koaci.com/article/2025/09/02/cote-divoire/economie/cote-divoire-mobile-money-pour-contrer-wave-et-se-relancer-mtn-tente-le-pari-du-0-de-frais_189861.html) |
| Strengths | Group scale and lending know-how. 0% app pricing. Salary-advance product aimed at employers. | as above |
| Weaknesses | Shrinking active base and revenue in CI. Losing to Wave in merchant payments. | Ecomatin |
| Recent moves 2025–26 | Aug 2025: 0% fees. Jun 2026: Helep Pro. Aug 2026: exploring bank licences. Sep 2026: PI-SPI participant. | as above |
| **Threat to Kelen** | **LOW-MEDIUM** (CI phase only). | analysis |
| Partner potential | **Yes, as a rail** (MoMo API or PI-SPI). Possible salary-advance partner. | analysis |

### 2.5 Moov Money Côte d'Ivoire (Moov Africa CI)

| Field | Detail | Source (date) |
|---|---|---|
| What it is | Third telco wallet in CI (Moov Africa, Maroc Telecom group). | [KOACI, 2026-07-16](https://www.koaci.com/article/2026/07/16/cote-divoire/societe/cote-divoire-20-ans-de-moov-africa-cote-divoire-loperateur-voit-grand-et-accelere-sa-revolution-digitale_198629.html) |
| Licence | "Moov Money" in PI-SPI CI (30 Sep 2026 list). Type **[UNVERIFIED]**. | Financial Afrik 2026-10-01 |
| Users | >4.2M active users, ~70,000 service points (Jul 2026). 2.31M ARTCI subscribers (Jun 2025). UEMOA: 18.4% of accounts but only 2.6% of value (2024). | KOACI 2026-07-16; KOACI 2025-09-11; BCEAO SFN 2024 |
| Business products | Merchant payment. **Microcredit "soon"**. Planned super-app. MoovMoney Mastercard card. | KOACI 2026-07-16; [Digital Mag CI](https://digitalmag.ci/moov-africa-devoile-la-moovmoney-card-pour-les-paiements/) |
| Business pricing | **Not published.** Secondary: transfers ~1% **[UNVERIFIED]**. | [momocalc](https://momocalc.com/fr/cote-divoire/frais-moov-ci) |
| **Threat to Kelen** | **LOW.** | analysis |
| Partner potential | **Rail only** (via PI-SPI or aggregators). | analysis |

### 2.6 Wizall Money (Senegal; also CI, Mali, Burkina)

| Field | Detail | Source (date) |
|---|---|---|
| What it is | B2B-first wallet and bulk payout platform: **Wizall Money Pro** for salaries, invoices, collections and **bulk payments**. Recipients without an account get an SMS withdrawal code. | [We are Tech](https://www.wearetech.africa/fr/fils/solutions/senegal-wizall-money-propose-des-services-financiers-aux-entreprises-et-aux-particuliers) (older) |
| Owner | **Groupe Banque Centrale Populaire (BCP, Morocco)**, acquired Dec 2018. | [PitchBook](https://pitchbook.com/profiles/company/236838-61); [Agence Ecofin (Mali)](https://www.agenceecofin.com/banque/2101-72988-mali-wizall-filiale-du-groupe-bcp-lance-wizall-money-une-solution-de-mobile-money-100-inclusive) |
| Licence | Described as a BCEAO-approved e-money "distributor" or "issuer"; the sources conflict **[UNVERIFIED]**. **Not on the PI-SPI lists.** | [Osiris](https://www.osiris.sn/Cote-d-Ivoire-une-fintech-lance.html); BCEAO PI-SPI lists |
| Volumes | Old figures only: 100,000 transfers per month, 60,000 accounts, 2 bn FCFA per month (date about 2017). Senegal government cash transfers: 542,956 households, 43.4 bn FCFA (2022). | [Jeune Afrique](https://www.jeuneafrique.com/628344/economie-entreprises/start-up-de-la-semaine-au-senegal-la-fintech-wizall-vise-dabord-les-entreprises/); [Agence Ecofin, 2022](https://www.agenceecofin.com/banque/0806-98460-senegal-wizall-money-partenaire-du-gouvernement-dans-le-cadre-des-transferts-monetaires-exceptionnels) |
| Pricing | **Not published.** Model: free for end users; commission taken when the company funds the platform. | Jeune Afrique |
| Recent moves 2025–26 | None found. Mixed app reviews (Jun 2026). Still accepted as a payment method by PayDunya and PayTech in SN (2026). | [Google Play](https://play.google.com/store/apps/details?id=com.wizall.wizallclient&hl=en_US); PayDunya fee grid 2026-09 |
| **Threat to Kelen** | **LOW-MEDIUM.** It is the closest in concept (corporate payroll to wallets) but appears dormant. BCP backing could revive it. | analysis |
| Partner potential | Low. Possibly a rail for unbanked payroll recipients. | analysis |

### 2.7 InTouch (TouchPay / TouchPoint), Senegal-headquartered

| Field | Detail | Source (date) |
|---|---|---|
| What it is | B2B payment aggregator: collections across all mobile money operators, **business payouts**, cash network ("TouchPoints"), bill payment, airtime distribution, custom integrations. Visa PayFac. | [Burkina24 press release, 2025-07-04](https://burkina24.com/2025/07/04/communique-le-groupe-intouch-acquiert-des-licences-detablissement-de-paiement-et-detablissement-de-monnaie-electronique-dans-la-zone-uemoa/); [Osiris, 2025-02-13](https://www.osiris.sn/intouch-10-ans-d-innovation-pour-revolutionner-les-paiements-en-afrique.html) |
| Countries | 26–27 African countries. | Osiris (2025-02-13); Burkina24 (2025-07-04) |
| Licence | **EME in Senegal**; **EP in CI, Mali, Burkina** (BCEAO, announced 2 Jul 2025). Also Guinea and Tanzania. PI-SPI: "TouchPoint Financial Services" is listed in SN and CI, probably InTouch's entity **[UNVERIFIED link]**. | Burkina24; BCEAO PI-SPI list |
| Owner / funding | Founder and CEO Omar Cissé. TotalEnergies and Worldline took stakes in an earlier round (about 2017). No 2025–26 raise found. Says it is profitable (several million euros of profit, Feb 2025). | [Jeune Afrique](https://www.jeuneafrique.com/460397/economie/total-intouch-lagregateur-de-paiement-senegalais/); Osiris |
| Volumes | ~4,000 large-account clients, ~60,000 merchants and TouchPoints, ~10,000 bn FCFA processed cumulatively, ~1.5M transactions per month, ~500 staff (Feb 2025). | Osiris (2025-02-13) |
| Pricing | **Not published.** Secondary: 250,000 FCFA setup plus a 50,000 FCFA monthly minimum **[UNVERIFIED]**. | [Kolonell, 2026](https://kolonell.com/fr/blog/intouch-paydunya-cinetpay-frais-detail-2026) |
| Target segment | Large corporates (energy, telco, utilities), merchants, financial institutions. | Osiris |
| **Threat to Kelen** | **MEDIUM.** Holds an EME licence in SN and offers payouts and collections to corporates, but has no SME banking UX. | analysis |
| Partner potential | **HIGH.** It is a licensed aggregator, a PI-SPI participant (probable), and has a cash network for unbanked staff. | analysis |

### 2.8 PayDunya (Dunya Digital Payment Sénégal SA)

| Field | Detail | Source (date) |
|---|---|---|
| What it is | Payment gateway (Pay-in and Pay-out API, payment links, plugins, MyDunya app). | [paydunya.com/service-fees](https://paydunya.com/service-fees) (accessed 2026-10-14) |
| Countries | SN, CI, Benin, Burkina, Togo, Mali (Cameroon in the fee grid). | [PayDunya FAQ](https://paydunya.com/faq); fee grid |
| Licence | **EP**: the first fintech licensed as an EP in Senegal (~May 2025). Not on PI-SPI. | [Le Soleil, 2025-05-08](https://lesoleil.sn/actualites/economie/blocage-fintech-au-senegal-2-000-milliards-de-fcfa-de-flux-perdus-en-six-jours/); [Seneweb, 2026-09-23](https://seneweb.com/en/news/Economie/mobile-money-pourquoi-le-duel-orange-money-wave-ne-resume-plus-le-marche_n_505004.html) |
| Owner | **Peach Payments** (South Africa) agreed to acquire it (announced Apr 2025, pending approvals at the time). | [Peach Payments](https://www.peachpayments.com/scale/peach-payments-acquires-west-african-payments-gateway-paydunya); [Electronic Payments International, 2025-04](https://www.electronicpaymentsinternational.com/news/peach-payments-acquire-paydunya/) |
| Volumes | >4,000 B2B clients, ~70,000 transactions per day, ~40 staff (Apr 2025). | Peach / EPI (2025-04) |
| Pricing (official grid "new fees Sept 2026", standard plan) | **Pay-in SN** (OM, Mixx, Wizall, Wave): **2.25%** below 100M FCFA per month; 2.20% for 100–500M; 2.15% above 500M. **Pay-in CI** (OM, Moov, Wave, MTN): the same 2.25/2.20/2.15%. **Cards: 3.5%.** Djamo SN/CI: 2.00/1.75/1.50%. **Pay-out SN** (OM, Mixx, Wizall, Wave): **2.00/1.95/1.90%**. **Pay-out CI**: **2.00/1.80/1.50%**. Djamo payouts: 1.50/1.25/1.00%. **No subscription or setup fee.** V.I.B (>100M per month): negotiated. Senegal transaction tax: 0.5%, capped at 2,000 FCFA. | [Fee grid PNG](https://paydunya.com/images/fees/new-fees-sept-2026.png); paydunya.com/service-fees (accessed 2026-10-14). Older ToS mention a 20,000 FCFA monthly fee, contradicted by the current page: [ToS](https://paydunya.com/terms-of-service) |
| **Threat to Kelen** | **MEDIUM-LOW.** Payouts API used by SMEs and e-commerce, but no accounts or payroll workflow. | analysis |
| Partner potential | **HIGH.** A collection gateway for Kelen's payment links and invoices across SN and CI, with Peach backing. | analysis |

### 2.9 CinetPay (CinetPay Africa SA, CI-headquartered)

| Field | Detail | Source (date) |
|---|---|---|
| What it is | Payment gateway: collections, **mass payout** ("in under 5 minutes"), payment links, school fees. | [cinetpay.com/products/mass-payout](https://cinetpay.com/products/mass-payout) |
| Countries | CI, SN, and around 10 francophone markets (CI, Togo and Burkina are cited in incidents). | TechCabal 2026-02-01 |
| Licence | **EP**, CinetPay Africa SA (BCEAO; announced ~2 Aug 2025, published in the Sep 2025 batch of 9 EPs). Not on PI-SPI. | [Digital Mag CI](https://digitalmag.ci/la-fintech-cinetpay-africa-sa-obtient-son-agrement-detablissement-de-paiement/); [Financial Afrik, 2025-09-02](https://www.financialafrik.com/2025/09/02/uemoa-la-bceao-agree-9-nouveaux-etablissements-de-paiement/) |
| Owner | Founders plus investors; Flutterwave-backed. | [WeeTracker, 2026-02-02](https://weetracker.com/2026/02/02/cinetpay-1m-debt-cyber-fraud/) |
| Volumes | >25,000 merchants **[UNVERIFIED]**. | WeeTracker |
| Pricing | From cinetpay.com/pricing (seen via search index; direct fetch blocked by Cloudflare) **[partly UNVERIFIED]**. **CI collections:** card 3.5%, Orange 3%, MTN 1.8%, Wave 2%, Moov 2.5%. **Mass payout CI:** 1.3% (MTN) to 2% (Wave); OM CI 1.5% on a mirror page. **SN mass payout:** Wave 2%, OM SN 1.8% (2% on the mirror). No monthly fee. Basic-tier payout cap: 400,000 FCFA per day. | [cinetpay.com/pricing](https://cinetpay.com/pricing); [elixir.cinetpay.com/pricing](https://elixir.cinetpay.com/pricing); [CGU](https://cinetpay.com/legal/cgu-services) (accessed via search 2026-10-14) |
| Recent moves / issues | Sep 2025: fraud or cyber incidents in CI, Togo and Burkina. Dec 2025: legal notice claiming 655M FCFA. Feb 2026: ~$1.1M settlement backlog reported. Named in a Senegal money-laundering case (company denies wrongdoing, Sep 2025). | [TechCabal, 2026-02-01](https://techcabal.com/2026/02/01/cinetpay-cyberattack/); [Startupmedias](https://startupmedias.net/senegal-des-accusations-de-blanchiment-planent-sur-cinetpay-fraichement-agreee-par-la-bceao) |
| **Threat to Kelen** | **LOW-MEDIUM.** Mass payout overlaps, but trust has been damaged. | analysis |
| Partner potential | **Possible but risky** (settlement and counterparty risk). | analysis |

### 2.10 PayTech (paytech.sn, Senegal)

| Field | Detail | Source (date) |
|---|---|---|
| What it is | Senegalese gateway: e-commerce plugins and API, POS terminal (card plus mobile money), PayTech Business app. Supports OM, Wave, Free/Mixx, Wizall, E-Money, Visa and Mastercard. | [paytech.sn](https://paytech.sn/) (accessed 2026-10-14) |
| Countries | SN, CI, Mali (Benin in the FAQ). | paytech.sn |
| Licence | **Not stated.** Not among the 11 Senegal EPs named at 28 Feb 2026, and not on PI-SPI **[licence status UNVERIFIED]**. | Seneweb 2026-09-23 |
| Pricing (official) | **Web/API, SN:** mobile money 2.0% (0–9.99M FCFA per month), 1.75% (10–99.99M), 1.50% (≥100M). Cards 3%, 2.75%, 2.50%. **CI and Mali:** mobile money with the same tiers; cards 2.5%. **POS "All in One":** 25,000 FCFA membership plus **11,800 FCFA per month**; card 3%, mobile money 1.5%. Business account opening: 10,000 FCFA. Withdrawals and disbursement: **no fees**. Bank transfer up to 72 hours in the UEMOA. | paytech.sn (accessed 2026-10-14) |
| **Threat to Kelen** | **LOW** (collections for e-commerce; no payroll or accounts). | analysis |
| Partner potential | Medium. An alternative collection gateway in SN. Check its licence first. | analysis |

### 2.11 Paystack (Stripe), Côte d'Ivoire

| Field | Detail | Source (date) |
|---|---|---|
| What it is | Stripe-owned gateway. Live in CI for mobile money (Wave, MTN, Orange) and cards. Virtual Terminal in CI. | [Paystack blog](https://paystack.com/blog/product/virtual-terminal-expansion) |
| Countries | CI only in the UEMOA. No SN presence found **[UNVERIFIED]**. | [mctaba](https://www.mctaba.com/learn/paystack/paystack-by-country-nigeria-ghana-south-africa-kenya-rwanda-cote-d-ivoire) |
| Licence | Not found in BCEAO EP lists. CI status (live vs private beta) conflicts between sources **[UNVERIFIED]**. | [PaymentReview](https://paymentreview.com/reviews/paystack/) |
| Pricing (official, CI) | **Mobile money 1.95%**, local cards 3.2%, international 3.8% (excl. VAT). No caps. Transfers and payout fees for CI: **not verified** (separate article not retrieved). | [support.paystack.com/2130306](https://support.paystack.com/en/articles/2130306) (accessed 2026-10-14) |
| **Threat to Kelen** | **LOW** (developer gateway; no SME banking). | analysis |
| Partner potential | Medium. A card-acceptance option for Kelen payment links in CI. | analysis |

### 2.12 Flutterwave (Flutterwave Sénégal SA)

| Field | Detail | Source (date) |
|---|---|---|
| What it is | Pan-African gateway. In SN: collections (Wave, OM, Free Money, cards), **single and bulk payouts** to bank and mobile money, payment links, invoices, plugins. | [Flutterwave blog, 2025-07-10](https://flutterwave.com/ng/blog/bonjour-senegal-flutterwave-is-now-licensed-to-power-payments-for-senegalese-businesses) |
| Licence | **EP in Senegal**, BCEAO (Jul 2025). No CI licence found. Investor in CinetPay. | Flutterwave blog; [The Paypers](https://thepaypers.com/payments/news/flutterwave-gains-a-payment-institution-licence-in-senegal); WeeTracker |
| Pricing (official, SN) | Local mobile money **2%**; cards (local and international) **4.8%**. **Payouts: to bank XOF 1,500 per transfer; to mobile money 2%.** Excl. VAT; customer pays by default. CI: no prices shown. | [flutterwave.com/sn/pricing](https://flutterwave.com/sn/pricing) (accessed 2026-10-14) |
| **Threat to Kelen** | **LOW-MEDIUM** (bulk payouts and invoices for exporters and tech firms). | analysis |
| Partner potential | Medium (cross-border collections, cards). | analysis |

### 2.13 Bizao

| Field | Detail | Source (date) |
|---|---|---|
| Status | **Defunct.** French parent Bizao SAS: receivership on 20 Mar 2025, then **compulsory liquidation on 27 May 2025** (Paris). Status of the African subsidiaries (Abidjan, Dakar) unclear. | [Launch Base Africa, 2025-06-18](https://launchbaseafrica.com/2025/06/18/french-court-orders-compulsory-liquidation-of-ivorian-founded-fintech-bizao/); [CIO Mag](https://cio-mag.com/bizao-plateforme-de-paiement-digital-en-afrique-entre-en-procedure-de-redressement-judiciaire/); [post-mortem, 2025-07-16](https://launchbaseafrica.com/2025/07/16/bizao-post-mortem-what-went-wrong-at-africas-b2b-payments-infrastructure-startup/) |
| Funding | €8M Series A (AfricInvest FIVE, Adelie, Seedstars), about 2022. | [Sika Finance](https://www.sikafinance.com/marches/la-fintech-bizao-leve-8-millions-d-euros-pour-devenir-l-un-des-hubs-du-paiement-en-afrique_35971) |
| **Threat / partner** | **None.** It is a cautionary tale for B2B payment hubs (thin margins, telco dependence). | analysis |

### 2.14 HUB2 (CI / France / Mauritius)

| Field | Detail | Source (date) |
|---|---|---|
| What it is | Payment infrastructure: a single API for mobile money, bank transfers, cards and (planned) stablecoins. "Stripe of francophone Africa". About 98% of clients are fintechs (B2B2B). | [The Condia](https://thecondia.com/ivory-coast-fintech-hub2-raises-8-5m-stripe-francophone-africa/); [Dabafinance](https://www.dabafinance.com/fr/nouvelles/hub2-secures-8-5m-pour-tendre-les-paiements-numriques-en-afrique-francophone) |
| Countries | 12 countries in West and Central Africa, including CI, SN, Benin, Cameroon. | [Financial Afrik, 2026-02-25](https://www.financialafrik.com/2026/02/25/ecobank-et-hub2-elargissent-lacces-aux-paiements-numeriques-a-200-millions-dutilisateurs-de-portefeuilles-mobiles-en-afrique-francophone/) |
| Funding | **$8.5M Series A** (Dec 2024) led by TLcom, with FMO, Enza, Bpifrance, Axian, DCG and others. | [Agence Ecofin, 2024-12-04](https://www.agenceecofin.com/actualites-finance/0412-124051-la-fintech-ivoirienne-hub2-leve-8-5-millions-pour-etendre-ses-services-de-paiement) |
| Licence | **None found** (not in the EP lists cited; not on PI-SPI) **[UNVERIFIED]**. | n/a |
| Recent moves | **25 Feb 2026: MoU with Ecobank** to connect more than 200M aggregated wallets to Ecobank's banking network (UEMOA and CEMAC first). | Financial Afrik 2026-02-25; [Ecofin Agency](https://www.ecofinagency.com/news/2602-53289-fintech-hub2-ecobank-move-to-create-unified-gateway-linking-200-million-mobile-wallets) |
| Pricing | **Not published.** | n/a |
| **Threat to Kelen** | **LOW** (sells to fintechs, not SMEs). | analysis |
| Partner potential | **HIGH.** It is a wallet-aggregation back end. The Ecobank link is relevant if Ecobank is Kelen's partner bank. | analysis |

### 2.15 Kkiapay (Open SI, Benin)

| Field | Detail | Source (date) |
|---|---|---|
| What it is | Beninese aggregator: POS terminal, merchant app, API integration, "Push Up", payouts to mobile money and bank. Publishes SME salary-payment guides. | [kkiapay.me/tarifs](https://kkiapay.me/tarifs/) (accessed 2026-10-14); [kkiapay salary guide, 2026-09-06](https://kkiapay.me/paiement-salaires-mobile-money/) |
| Countries | Benin, Togo, CI, SN, Niger, Burkina (selector on the pricing page). | kkiapay.me/tarifs |
| Licence | **EP (BCEAO, Benin)**, ~2025 **[date UNVERIFIED]**. Not on PI-SPI SN or CI. | [Startupmedias](https://startupmedias.net/public/kkiapay-open-si-obtient-son-agrement-bceao-detablissement-de-paiement-une-etape-cle-pour-la-fintech-beninoise) |
| Pricing (official; country mapping unclear on the page) | **Integration (API): 9,900 FCFA per month**; mobile money 1.3%, 1.5% or 1.9%; cards 2.1% UEMOA, 3% non-UEMOA. **App: 1,000 FCFA per month**; mobile money 1.3–1.9%. **POS: 4,900 FCFA per month**; mobile money 1%; cards 1.8% or 2.3%. Payout fees: **not published**. Payment link: 100 FCFA. | kkiapay.me/tarifs |
| **Threat to Kelen** | **LOW** in SN and CI (Benin-centric), but its subscription-plus-percentage model mirrors Kelen's. | analysis |
| Partner potential | Low-medium. | analysis |

### 2.16 NabooPay and other new Senegalese aggregators

| Field | Detail | Source (date) |
|---|---|---|
| NabooPay | Dakar startup (© 2024): checkout, **escrow**, AI reporting, SDKs. **Prices: 3% OM and Wave; 6% Visa and Mastercard**; no setup or monthly fee. 150–250 merchants (conflicting claims). Licence **not stated**. Payouts not mentioned. | [naboopay.com](https://naboopay.com/) (accessed 2026-10-14); [Socialnetlink, 2025-03-01](https://www.socialnetlink.org/2025/03/01/djim-momar-lo-ce-genie-senegalais-qui-veut-transformer-lafrique-avec-naboopay/) |
| Other licensed EPs in Senegal (28 Feb 2026) | DUNYA Digital Payment (PayDunya), **Mikaty**, **Bictorys**, Flutterwave Senegal, **Samir Money**, **Versus Finances Tech**, **Copay**, **Sesa Digital Finance**, **Julaya Senegal** (B2B payouts, a direct Kelen comparator, covered by the fintech researcher), Djamo Senegal, African Financial Agent. | [Seneweb, 2026-09-23](https://seneweb.com/en/news/Economie/mobile-money-pourquoi-le-duel-orange-money-wave-ne-resume-plus-le-marche_n_505004.html) |
| Context | Senegal had a six-day "blocage" of fintech flows in spring 2025, estimated by a consultant at >2,000 bn FCFA of flows. The licence deadline was 1 May 2025, later 31 Aug 2025. | [Le Soleil, 2025-05-08](https://lesoleil.sn/actualites/economie/blocage-fintech-au-senegal-2-000-milliards-de-fcfa-de-flux-perdus-en-six-jours/) |
| **Threat / partner** | NabooPay: **LOW**. Mikaty, Bictorys, Samir Money and SesaPay are on PI-SPI SN and are potential partners or competitors (not profiled here; **[follow-up]**). | analysis |

---

## 3. Pricing comparison for businesses (published prices only)

All fees are in FCFA or as a % of the amount. "NP" means not published. Sources and dates are in the profiles above.

| Player | Country | Merchant collection fee | Bulk / payout fee | Cash-out / withdrawal for recipient | Account or subscription fee | Settlement to bank |
|---|---|---|---|---|---|---|
| **Wave Business** | SN, CI | First 20,000/day free, then **1%** | **1% sender**, recipient free | Free at any Wave agent | NP (none mentioned) | NP (secondary: free vs 250 FCFA **[UNV]**) |
| **Orange Money B2B** | SN | **1%** | **Paiement Pro: 1% (OM) / 1.5% (non-OM)** | Free for recipient (payer pays) | Free subscription | **D+5** |
| **Orange Money** | CI | NP (contract annex) | **Salaries: 2.0% / 1.5% / 1.0%** by funding tier (2016 doc) | Recipient pays the standard withdrawal grid (1% transfer withdrawal; cash-out grid) | NP | NP |
| **Mixx by Yas** | SN | **1%** (incl. 0.5% tax) | NP (Business Suite) | 1% Canal Mixx | NP | NP |
| **MTN MoMo** | CI | NP | NP | 0% in app since Aug 2025 (consumer) | NP | NP |
| **Moov Money** | CI | NP | NP | NP | NP | NP |
| **Wizall** | SN | NP | NP (commission on funding) | Free (claimed) | NP | n/a |
| **InTouch** | SN, CI | NP | NP | n/a | NP (secondary 250k setup + 50k/month **[UNV]**) | NP |
| **PayDunya** | SN | **2.25 / 2.20 / 2.15%** (cards 3.5%) | **2.00 / 1.95 / 1.90%** | n/a | **None** | NP |
| **PayDunya** | CI | **2.25 / 2.20 / 2.15%** | **2.00 / 1.80 / 1.50%** | n/a | None | NP |
| **CinetPay** | CI | OM 3%, MTN 1.8%, Wave 2%, Moov 2.5%, card 3.5% **[partly UNV]** | 1.3% (MTN) to 2% (Wave); OM 1.5% | n/a | None | NP |
| **CinetPay** | SN | NP | Wave 2%, OM 1.8–2% **[UNV]** | n/a | None | NP |
| **PayTech** | SN | Mobile money 2.0 / 1.75 / 1.5%; card 3–2.5% | "No fees" on withdrawals and disbursement | n/a | Account opening 10,000; POS 25,000 + 11,800/month | ≤72h UEMOA |
| **Paystack** | CI | Mobile money **1.95%**; card 3.2% / 3.8% | NP | n/a | None | NP |
| **Flutterwave** | SN | Mobile money **2%**; card **4.8%** | **Mobile money 2%; bank XOF 1,500** | n/a | None | n/a |
| **Kkiapay** | multi | Mobile money 1–1.9%; card 1.8–3% | NP | n/a | **1,000 / 4,900 / 9,900 per month** by product | NP |
| **NabooPay** | SN | **3%** OM/Wave; **6%** card | NP | n/a | None | NP |
| **PI-SPI (BCEAO)** | UEMOA | Free for the payer; receiver gets 30 free per month, then ≤1% cap | Free for individual senders | n/a | n/a | Instant |

Tiers for PayDunya and PayTech are monthly flow bands. PayDunya: <100M / 100–500M / >500M FCFA. PayTech: <10M / 10–99M / ≥100M FCFA.

**Benchmark against Kelen plans (illustrative):**

| Monthly payroll | Wave 1% | Orange SN Paiement Pro (OM recipients, 1%) | Orange SN Paiement Pro (non-OM, 1.5%) | PayDunya payout SN (2%) |
|---|---|---|---|---|
| 1M FCFA (Petite) | 10,000 | 10,000 | 15,000 | 20,000 |
| 3M FCFA (Moyenne) | 30,000 | 30,000 | 45,000 | 60,000 |
| 15M FCFA (Grande) | 150,000 | 150,000 | 225,000 | 300,000 |

Kelen plans cost 9,900, 29,900 and 79,900 FCFA per month. These flat fees beat percentage pricing for any SME paying more than about 1M, 3M or 8M FCFA per month respectively, **if** Kelen's own payout cost is near zero (PI-SPI). This is an analysis, not sourced data. PayDunya's lower tiers start at 100M FCFA per month, so all three rows use 2%.

---

## 4. Threat and partner summary

| Player | Threat to Kelen | Main reason | Partner potential |
|---|---|---|---|
| Wave | **HIGH** | 1% bulk payouts with free cash-out, merchant tools and API; bank (Wave Bank Africa) and credit in preparation; dominant SME habit | **Yes**: rail (Payout API or PI-SPI), cash-in |
| Orange Money / Orange Bank Africa | **MEDIUM-HIGH** | OM Business in CI with OBA SME credit; Paiement Pro payroll in SN; OBA has 3M clients and a SGPME guarantee | **Yes**: rail; OBA as a possible bank or lending partner (conflicted) |
| Mixx by Yas | LOW-MEDIUM | Business Suite with salaries, but small share | Rail |
| MTN MoMo CI | LOW-MEDIUM | Helep Pro salary advance; exploring bank licences | Rail; possible salary-advance partner |
| Moov Money CI | LOW | Small, consumer-focused | Rail |
| Wizall | LOW-MEDIUM | Corporate bulk-pay concept, BCP-owned, but dormant | Low |
| InTouch | MEDIUM | EME in SN, corporate payouts and collections | **HIGH** (aggregator and cash network) |
| PayDunya | MEDIUM-LOW | Payout API used by SMEs | **HIGH** (collections gateway) |
| CinetPay | LOW-MEDIUM | Mass payout; trust issues | Possible, risky |
| PayTech | LOW | Collections only | Medium |
| Paystack CI | LOW | Developer gateway | Medium (cards) |
| Flutterwave SN | LOW-MEDIUM | Bulk payouts and invoices | Medium (cross-border, cards) |
| Bizao | None (liquidated) | n/a | n/a |
| HUB2 | LOW | Sells to fintechs only | **HIGH** (wallet aggregation; Ecobank link) |
| Kkiapay | LOW | Benin-centric | Low-medium |
| NabooPay | LOW | Small, expensive | Low |

## 5. Open items (follow-up research)
- Whether Wave Bank Africa holds a banking licence: check the Commission Bancaire list of approved banks and the CI Finance Ministry decree (arrêté).
- Wave Business current settlement fee and account limits from an official source (only blog sources exist).
- Orange CI merchant commission and the current Paiement de Salaires grid (the catalogue PDF link is dead; the annex is dated 2016).
- Paystack CI transfer and payout fees; MTN and Moov CI business grids.
- Wizall's current licence and activity.
- Whether "TouchPoint Financial Services" is InTouch's entity.
- Profiles of the newer SN EPs on PI-SPI: Mikaty, Bictorys, Samir Money, SesaPay, Versus Finances Tech, Quick Pay.
- An official Senegal-level operator market-share split (the ARTP or BCEAO publishes none at operator level).
