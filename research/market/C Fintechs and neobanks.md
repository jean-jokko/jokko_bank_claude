# C. Direct competitors: fintechs and neobanks for SMEs in Senegal and Côte d'Ivoire

*Research date: 2026-10-14. Prepared for Kelen (B2B neobank for SMEs, Senegal launch 2027, then Côte d'Ivoire).*

**Conventions**
- Every fact has a source ID `[Sxx]`. The full source list, with URLs and dates, is at the end (§10).
- **Verification levels.** "(fetched)" means I opened and read the page. "(search)" means the fact comes from a search-engine summary of the page and I did not open it. **[UNVERIFIED]** means the fact comes from one secondary source, from a third-party blog, or is my own inference.
- "Accessed 2026-10-14" means the live page on the research date. Undated product and pricing pages carry the access date.
- Fees are quoted as published, mostly "TTC". FCFA = XOF.

---

## 0. Key takeaways

1. **No one in Senegal yet offers an IBAN business account + multi-user approvals + bulk pay to banks and all wallets + cards + SME credit in one subscription product.** The two closest players attack it from different sides:
   - **Julaya** is B2B-native: payroll and bulk payouts, approvals, sub-accounts, exports, and a new UEMOA RIB. It has no cards and no credit yet [S1–S6].
   - **Djamo** is consumer-first and has a free "Djamo Business" add-on. It has cards, a microfinance licence and live consumer credit in CI, but a thin SME feature set [S13–S17].
2. **Licensing has caught up with Kelen's plan.** Both Julaya and Djamo hold BCEAO payment-institution (EP) licences in **both** Senegal (EP.SN.009/2025 and EP.SN.010/2025) and CI (EP.CI.004/2025 and EP.CI.005/2025) [S8, S9]. Djamo Finances also holds a microfinance licence in CI, announced Sept 2025 [S23]. Kelen's "partner bank + later MFI licence" route is the same one Djamo has already taken.
3. **Pricing benchmark: the incumbents charge per transaction, not per month.**
   - Wave: 1% per payout [S25].
   - Orange Money "Paiement Pro": 1% / 1.5% [S31].
   - Julaya: 0.5–1.5% to wallets [S2].
   - Djamo Business: account free, bulk pay free via the web app, 0.5% via API, 1% on collections [S14].
   - A typical bank (UBA Sénégal) charges **25,000 FCFA/month** account maintenance for SA/PME and 10,000 for TPE [S44].

   Kelen's 9,900 / 29,900 / 79,900 FCFA plans sit between the two models. To beat "free + per-transaction", they need included transaction volume.
4. **The biggest strategic threats are platform moves, not feature parity.**
   - **Wave** has applied for a banking licence (Wave Bank Africa S.A., capital 20 bn FCFA; "still under review" as of 29 Apr 2026) [S27, S28].
   - **Orange Bank Africa** is scaling SME credit: CFA 747 bn lent since 2020, a Senegal branch since Feb 2025, and new SGPME and IFC guarantees in 2026 [S33, S34].
   - **Djamo** is raising a **$40M Series C** (target, July 2026) and is pursuing SME cross-border payments through a bank partnership [S21].
5. **Gaps Kelen can own in Senegal.** These are inferences from the matrix in §8:
   - True double-signature approvals combined with bulk pay to **banks and all wallets** from one balance.
   - Employee salary accounts with salary advance tied to payroll (today handled by niche apps such as Fintra and BaraPay [S43]).
   - Accountant access and exports in a Senegalese format.
   - Bundled SME credit.

---

## 1. Regulatory snapshot (who is licensed to do what)

| Licence (BCEAO / UMOA) | Senegal | Côte d'Ivoire | Source |
|---|---|---|---|
| **Payment institution (EP)**, under Instruction 001-01-2024 | 12 EPs: African Financial Agent, **Bictorys**, CoPay, **Djamo Sénégal**, **Dunya Digital Payment (PayDunya)**, **Flutterwave Sénégal**, **Julaya Sénégal**, Mikaty, Samir Money, Sesa Digital Finance, Versus Finances Tech, Wafacash West Africa | 10 EPs: **CinetPay Africa**, **Djamo CI**, Dunya Digital Payment CI, FeexPay CI, Firstcom Global Payments, **Julaya CI**, Paymetrust, **SYCA (Sycapay)**, **Touchpoint Financial Services (InTouch)**, NITA (branch) | [S9] list as of 29 Jun 2026 (fetched) |
| **E-money institution (EME)** | Mobile Cash (Free/Mixx), Orange Finances Mobiles Sénégal, QuickPay, Touchpoint Financial Services (InTouch), **Wave Digital Finance** (EME.SN.017/2022) | Djogana Pay, Moov Money CI, MTN MFS CI, Orange Money CI | [S9] |
| **Microfinance (SFD)** | Djamo's Senegalese SFD status was not found. **[UNVERIFIED]** | **Djamo Finances SA**: first fintech to obtain an MFI licence, announced 11–12 Sep 2025 | [S23] (search) |
| **Bank** | Orange Bank Africa has a Senegal branch (opened Feb 2025) | Orange Bank Africa. **Wave Bank Africa S.A.** is incorporated; its banking licence is "toujours à l'étude" as of 29 Apr 2026 | [S34], [S28] (fetched) |

Notes:
- Wave does **not** appear in the CI EME list as of 29 Jun 2026 [S9]. Its regulatory basis in CI was not verified **[UNVERIFIED]**.
- The licence dates in the BCEAO list as of 28 Feb 2026 are:
  - Julaya CI: 09/05/25
  - Julaya SN: 11/09/25
  - Djamo CI: 04/09/25
  - Djamo SN: 03/09/25
  - Bictorys: 20/05/25
  - Flutterwave SN: 22/05/25
  - [S8] (fetched)

---

## 2. Tier 1: direct competitors

### 2.1 Julaya (B2B payments and payroll), threat level **HIGH**

| Item | Facts | Source |
|---|---|---|
| Description | "Compte professionnel de paiement et d'encaissement". It covers mobile-money and bank transfers, collections (cash and mobile money), and bill pay / invoicing. | [S1] fetched, accessed 2026-10-14 |
| Countries | Côte d'Ivoire, Senegal, Benin, Togo. Bank partnerships exist in all four. | [S1], [S10] |
| Licences | BCEAO EP licences: CI **EP.CI.004/2025** (09/05/2025), SN **EP.SN.009/2025** (11/09/2025), Benin **EP.BN.001/2025** (08/09/2025). The CI licence covers card payments, transfers and direct debits, issuing payment instruments, payment initiation, and account information services. | [S8], [S7] (2025-05-13) |
| Founded / founders | 2018. Mathias Léopoldie (CEO) and Charles Talbot. | [S10] (2025-10-21) |
| Funding | **Pre-Series A, July 2021:** $2M from Orange Ventures, MFS Africa Frontiers, Saviu Ventures, Launch Africa and 50 Partners Capital [S11]. **Sept 2022:** $5M extension led by Speedinvest, with EQ2 Ventures, Kibo Ventures, Unpopular Ventures, Jedar Capital, Mohamed Diabi and existing investors [S12] (search). **17 Oct 2025:** CFA 800M (~$1.41M) in convertible bonds from **CDC-CI Capital**, convertible within 2–3 years [S10]. Totals differ across databases ($7.8M to $12.6M) **[UNVERIFIED]**. | [S10] [S11] [S12] |
| Scale | "Plus de 10 000 professionnels", "plus de 1 000 moyennes et grandes entreprises", "+700K paiements et salaires reçus par an" (undated homepage) [S1]. ">1,000 corporate clients" and annual volume "> CFA 1,000 billion" [S10]. **Senegal 2024:** 820,000 transactions (+37% vs 2023) and >2,800 active users [S10]. | [S1] [S10] |
| Clients (logos) | Jumia, SODECI, Ministère de l'Éducation CI, World Bank, Kamtar, CinetPay, InTouch, Legafrik, Ivoire Transport. Logos are on the homepage. | [S1] (fetched HTML) |
| Business products | Bulk pay: "Jusqu'à 3 000 transferts et virements en un clic" for suppliers and salaries, to all MNOs (Orange, Wave, MTN, Moov) and all banks [S3]. Customisable validation levels, delegation, 2FA [S3, S5]. Multi-company and **sub-accounts** with separate access and signing rights, plus per-user spending caps [S1, S5]. Real-time tracking and **accounting exports** [S1]. **"RIB JULAYA" (new)** to receive transfers from the whole UEMOA; the issuing bank is not named [S4]. Bill pay (CIE, SODECI) and invoice collection [S6]. | [S1]–[S6] |
| Not offered (per site) | No cards, credit, invoice creation, payment links, or public API on the product pages. | [S1] [S3] [S6] |
| Pricing (published) | **Pay to mobile money** (Orange, MTN, Moov, Wave, Djamo): 0.5%–1.5% TTC depending on volume. **Bill payments:** 0.5%. **Inter-company transfers:** free, but the payee pays 0.1–0.5%. **Bank transfers:** "selon volume" (no rate). **Cash & Collect** (Wave, Xpress): 0.5–1%. **Invoice collection:** 0.1–0.5%. **Emergency MoMo top-up:** 0.8–1%. **Cash, cheque or transfer deposit at partner banks:** free. No subscription is shown. | [S2] fetched, accessed 2026-10-14 |
| Target segment | Medium and large firms and institutions (CFO/DG persona). Payroll for salaried and day workers. | [S1] |
| Distribution | Direct sales ("Demander une démo"). Partner banks for cash deposit. Content marketing such as a Deloitte CI tax-reform tool [search, sikafinance]. | [S1] [S2] |
| Partner banks | Not named on the site. **No BOA partnership found** in searches **[UNVERIFIED]**. | [S4] |
| Strengths | B2B-native. Licensed in SN and CI. Proven payroll use case. Approvals and sub-accounts. Pays to banks **and** all wallets. Free cash deposit. | – |
| Weaknesses | No cards, credit or employee accounts. Small Senegal base (~2,800 active users in 2024). Funded with debt since 2022 rather than equity. Percentage pricing becomes expensive on large payrolls. | [S10] |
| News 2025–26 | May 2025: EP licence in CI. Sept 2025: EP licences in SN and Benin. Oct 2025: CDC-CI debt round, earmarked for **SME short-term credit products** and infrastructure [S10]. No 2026 news found. | [S7] [S8] [S10] |
| **Threat to Kelen** | **HIGH.** It is the closest functional match (payroll, approvals, sub-accounts, RIB) and is already licensed in Senegal. It plans SME credit [S10]. It would be the default alternative for Kelen's mid and upper tiers. | – |

### 2.2 Djamo / Djamo Business, threat level **HIGH**

| Item | Facts | Source |
|---|---|---|
| Description | Consumer neobank (Visa cards, savings, investment, credit) with a **Djamo Business** account for companies, sole traders and NGOs/associations. | [S13] [S19] |
| Countries | Côte d'Ivoire. Senegal since about Dec 2023, with ">500,000 users" after two years. | [S22] (2026-04-02) |
| Licences | EP **EP.CI.005/2025** (04/09/2025) and **EP.SN.010/2025** (03/09/2025) [S8]. **Djamo Finances SA** obtained a microfinance licence in CI, announced Sept 2025 [S23] (search). "Djamo Finance" in Senegal is "à venir… sous licence de microfinance" [S22]. Ecobank is the partner for international-payment cards [S21]. | [S8] [S21] [S22] [S23] |
| Founded / founders | Founded 2020 (YC W21). Hassan Bourgi (CEO) and Régis Bamba. | [S24], [S22] |
| Funding | $14M Series A (2022) [S20]. **$17M (April 2025)** led by Janngo Capital with SANAD Fund, Partech, Oikocredit, Enza Capital and Y Combinator [S20]. **To date $31M equity + $5M debt**. It is **targeting a $40M Series C** (8 Jul 2026, not confirmed closed) [S21]. | [S20] [S21] |
| Scale | >1M customers in CI and SN, ~10,000 small businesses onboarded, >$4.5B processed, ~25% on premium (Apr 2025) [S20]. **2M users** (Jul 2026) [S21]. Senegal: >500k users, ~700 agents (Apr 2026) [S22]. | [S20] [S21] [S22] |
| Business products | **Bulk payments** by file upload for salaries and suppliers. **Employee Djamo cards** at a preferential rate. Bank transfers to any UEMOA bank. Real-time tracking, one-click export. Web portal (business-civ.djamo.com). Collections (QR code, payment link, API). **API** [S13] [S14]. The API pays out only to **Djamo accounts**, and API collections are Djamo-to-Djamo only ("mobile money arrive bientôt"). The API limit is 5,000–500,000 F per transfer [S16]. Merchant tools: bulk payments, payment links, QR [S20]. | [S13] [S14] [S16] [S20] |
| Limits | Informal businesses: 2M F per transaction and 10M F/month deposits. SMEs / legal entities: **10M F per transaction and 100M F/month deposits**. | [S13] |
| Pricing (Business) | Opening and maintenance free ("0 F", "Zéro frais de gestion"). **Bulk payments via web app: free.** Bank transfers via web app: free. **API unit/bulk transfers: 0.5%.** **Collections (QR, payment link, API): 1%.** | [S14] fetched, accessed 2026-10-14 |
| Pricing (consumer, for reference) | Premium 2,000 F/month. To mobile money: 1.5% (Free plan) or free up to 1M F then 1% (Premium). To bank: 1.5% (Free) or free (Premium). | [S18] |
| Credit | Consumer credit in CI, up to **1,000,000 F**: 0.78% interest + 1% dossier fee, plus 3% for instant disbursement, late fee 0.3%/day (cap 9%). It is **not** offered to Business accounts. | [S17] fetched |
| Multi-user / approvals | Not described on the business or support pages [S13] [S19]. A job posting lists "multi-user access" among SMB product areas (search) **[UNVERIFIED]**. Opening a business account requires an existing personal Djamo account (CI help article, search) **[UNVERIFIED]**. | – |
| Target segment | Micro and small businesses, sole traders, associations, often converted from retail users [S20]. | [S20] |
| Distribution | App-led, plus ~700 agents in Senegal [S22]. Retail-to-business conversion [S20]. | – |
| Strengths | Brand and user base (2M). Both EP licences. MFI licence in CI. Live credit engine. Cards (Visa / Ecobank). Free business account. Strong investors and an active raise. | – |
| Weaknesses | The business offer is shallow (no documented roles, approvals or sub-accounts). The API is limited to Djamo accounts. Low limits (10M F per transaction). Credit is consumer-only. No accountant features found. Only 5–10% of users receive their salary on Djamo [S20]. | [S16] [S20] |
| News 2025–26 | Apr 2025: $17M raise. Sept 2025: EP licences in SN and CI, plus the MFI licence in CI. **Apr 2026:** Senegal press briefing announcing Djamo Finance (MFI). **Jul 2026:** $40M Series C target, 2M users, a bank partnership sought for **SME cross-border payments**, and BCEAO sandbox talks on a stablecoin. | [S20]–[S23] |
| **Threat to Kelen** | **HIGH.** Its free SME account undercuts Kelen's entry plan. It already does bulk pay and employee cards in Senegal. If the Series C closes, it can fund the Kelen-type features (roles, credit) quickly. Its weakness is the depth of the business offer. | – |

### 2.3 Wave (Wave Business), threat level **HIGH (strategic)** / MEDIUM (feature)

| Item | Facts | Source |
|---|---|---|
| Description | The dominant mobile-money wallet in SN and CI. **Wave Business** offers bulk payments, a merchant app, collections through agents, and API checkout. | [S25] fetched |
| Licence | EME Senegal "Wave Digital Finance" EME.SN.017/2022 [S9]. The BCEAO EME was granted April 2022, and Wave was the "first non-bank, non-telecom fintech authorized" in UEMOA [S27]. **Wave Bank Africa S.A.** (Abidjan, capital 20 bn FCFA) is incorporated [S27]. The bank licence is "toujours à l'étude" (29 Apr 2026) [S28]. | [S9] [S27] [S28] |
| Scale | ">21 million users across Africa" [S27]. **CI:** 21M accounts opened, ~1M merchants, ~60% of mobile-money market share (May 2026) [S28]. SN: "plus de 10 millions d'utilisateurs actifs" (Ecofin, Jan 2026, search) **[UNVERIFIED]**. | [S27] [S28] |
| Funding | $200M Series A in 2021 (unicorn) [search, fintechnews.africa]. €117M debt (June 2025) [S27]. | [S27] |
| Business products / pricing | **Bulk payments: "1% pour vous, gratuit pour le destinataire."** Merchant app: first 20,000 F/day free, then 1%. Collections via agents with a Business Portal [S25]. **Payout API:** batches to **mobile numbers only** (the recipient doesn't need a Wave account), same country only. API keys are per wallet and admin-only. **No approval workflow is documented** [S26]. Virtual Visa card with Ecobank (consumer, Jan 2026) [S29]. In CI, "Bank to Wallet" works with 23 banks [S28]. | [S25] [S26] [S28] [S29] |
| Target segment | Merchants and informal businesses, plus companies paying many low-income workers. | [S25] |
| Distribution | Massive agent network and viral consumer adoption. | – |
| Strengths | Ubiquity. Recipients pay nothing. Trust. Low cost. The 2026 virtual card. A potential bank licence. | – |
| Weaknesses (B2B) | No IBAN account, no payouts to banks, no documented approvals or roles, no sub-accounts, no invoicing, no credit. In CI, a monthly cap of 2M FCFA per (consumer) account was cited by Wave CI's director [S28]. | [S26] [S28] |
| **Threat to Kelen** | **HIGH strategically.** A Wave bank with SME accounts and credit would compress the whole category. **MEDIUM today**, since Wave Business lacks treasury and control features. Wave is also a **must-have payout rail for Kelen**: about 1% of payroll value is the price that Kelen's bulk payouts must match or beat. | – |

### 2.4 Orange Money business offers + Orange Bank Africa, threat level **MEDIUM**

| Item | Facts | Source |
|---|---|---|
| Offers (Senegal) | **Paiement Pro** pays suppliers, salaries, allowances, bonuses and per diems to OM accounts or by code. Web platform: salaires.orange-sonatel.com. Free back office. Paiement Marchand and Paiement Internet (API). **Salary sub-accounts** limited to 2 withdrawals/week. | [S31] fetched |
| Pricing (Senegal) | Free subscription. **Paiement Pro: 1% if the payee has OM, 1.5% if not.** Payees withdraw free. Merchant and internet collections cost the merchant **1%**, settled to the bank at **J+5**. | [S31] |
| Offers (CI) | Paiement de Salaires et Primes, Fast Pay, bill payments, e-commerce, Orange Money API, OM bank transfers. Prices are not shown. | [S32] fetched |
| Licence | EME: Orange Finances Mobiles Sénégal and Orange Money CI [S9]. **Orange Bank Africa** is a bank in CI with a Senegal branch (opened Feb 2025) [S34]. | [S9] [S34] |
| OBA scale / SME credit | >3.6M customers (80% CI, 20% SN), **>CFA 747 bn lent since 2020** [S34]. Tik Tak app: ~3M Orange Money customers signed up [S33]. **Feb 2026:** IFC CFA 17 bn guarantee covering 50% of a working-capital SME loan portfolio of up to $60M (CI and SN targets) [S33]. **Jul 2026:** SGPME guarantees mobilise up to CFA 17 bn of SME credit in CI [S34]. | [S33] [S34] |
| Strengths | Distribution. SME credit at scale. Bank licence. Integration with payroll on Orange Money. | – |
| Weaknesses (B2B) | Pays out to OM only. No multi-bank payouts, no approvals documented, no IBAN business account in the wallet, slow J+5 settlement. | [S31] |
| **Threat to Kelen** | **MEDIUM.** OBA is the most credible **SME-credit** competitor for Kelen's later loan product. The payments side is commoditised. | – |

---

## 3. Tier 2: B2B payment infrastructure that overlaps parts of Kelen

| Player | What it does (B2B) | Countries / licence | Founding / funding | Scale | Pricing | Threat | Sources |
|---|---|---|---|---|---|---|---|
| **InTouch (Touchpoint Financial Services)** | Aggregator for collections and disbursements. "Paiement de masse" (bulk payment). **"Crédit Digital", including salary advances and split payments.** API, PayLink, POS, billing. | EME Senegal (EME.SN.024/2025) and EP in CI, Mali, Burkina, Togo and Guinea-Bissau [S9]. "Available in 27 African countries" [S35]. | Founded 2014, Omar Cissé [S36]. 2017 round of €3.7M–€10M from Total and Worldline (figures conflict) [search, Osiris] **[UNVERIFIED]**. | 5,200 business clients on the site, or ">4,000 entreprises" (Feb 2025) [S35] [S36]. | Not published. | **MEDIUM.** It could bundle salary advance with bulk pay for large employers. It is enterprise-focused, not an SME account. | [S9] [S35] [S36] |
| **PayDunya (Dunya Digital Payment)** | Collect (bulk collections), **Push (bulk disbursements)**, invoices by SMS/email, WebPay, MobPay, Social Shop, MyDunya transfers. | EP in SN (EP.SN.001/2025) and CI (EP.CI.008/2025) [S9]. | Senegalese. Funding not verified. | ">1 000 entreprises clientes" (press, search) **[UNVERIFIED]**. | Not published on the homepage. | **LOW–MEDIUM.** A rail rather than an account. | [S9] [S37] |
| **Bictorys** | Omnichannel collection (Orange Money, Wave, Visa/MC) [search]. | EP Senegal EP.SN.003/2025 (20/05/2025) [S8]. | No funding found. | n/a | n/a | **LOW.** Collections focus. A possible partner. | [S8] [S50] |
| **HUB2** | One API for fintechs to collect and pay out (mobile money, bank, cards). Clients include Djamo, Julaya and CinetPay. | 6 Francophone countries including SN and CI [S38]. | $8.5M Series A (Dec 2024) led by TLcom, with FMO, Enza, Bpifrance [S38] (search). | ~€1bn projected 2024 volume [S38]. | Est. 1–1.5% payouts **[UNVERIFIED]**. | **LOW** as a competitor. **A likely payout-rail supplier for Kelen.** | [S38] |
| **CinetPay** | Payment gateway. Transfers to mobile money. | EP CI (EP.CI.007/2025) [S9]. | – | ">25,000 entreprises" [S39]. | ~3% + 50 F per collection (third party) **[UNVERIFIED]**. | **LOW.** Reported cyberattack and liquidity issues in late 2025 [S39] (search). | [S9] [S39] |
| **Wizall Money (BCP group)** | "Wizall Money Pro": salaries, invoices, bulk payments. Payees without an account get an SMS withdrawal code. | Senegal, CI. Licence status not found in the 2026 lists (it may operate under a BCP bank). **[UNVERIFIED]** | Founded 2015, subsidiary of Groupe BCP [S40]. | Contracts: CSS (sugar company), a construction (BTP) consortium of 1,500 workers [S40]. | 0.8–1.5% per payment (Kolonell, Jun 2026) **[UNVERIFIED]**. | **LOW–MEDIUM.** A payroll-to-wallet niche for large employers. | [S40] |
| **Flash / New Africa Technology** | Mastercard virtual and physical prepaid cards. **"Flash in Business"** platform for companies. | SN, CI, Benin (programme announced) [S47]. | – | – | – | **LOW–MEDIUM.** It is the only local B2B card-programme announcement found. Live business features were not verified. | [S47] |
| **Mixx by Yas (ex-Free Money)** | Wallet. Mixx Mastercard prepaid card (with Ecobank, Jun 2025) aimed at freelancers and small businesses. A TPE offer is "in preparation". | EME "Mobile Cash" SN [S9]. | Axian group. | – | – | **LOW.** Labour dispute in Feb 2026 [S48]. | [S9] [S48] |
| **Flutterwave / Paystack** | Merchant collection gateways. Flutterwave has an EP licence in Senegal [S8]. Paystack is operational in CI with XOF settlement to local banks (third party) [S51]. | – | – | – | – | **LOW.** They serve online merchants, not an SME operating account. | [S8] [S51] |

---

## 4. Tier 3: adjacent SaaS that could bundle payments (payroll, invoicing, salary advance, credit)

| Category | Player | Facts | Threat | Source |
|---|---|---|---|---|
| Payroll SaaS (SN) | **KayFay** (SoftValley Labs, Dakar) | Computes IPRES, IPM, IR, TRIMF and CFCE. Batch payslips. **Salary advances ("Acomptes et avances").** Time tracking and leave. **Pricing:** 2,500 F per payslip (1–20), 2,000 (21–50), 1,750 (51–150), 1,500 (>150). Minimum 15,000 F HT/month. No payment rail. | **LOW–MEDIUM.** It is a **partner/integration** candidate: payroll file goes to Kelen for bulk pay. | [S41] fetched |
| Payroll SaaS | SunuPayRH, CloudPaie, Odoo "Paie Sénégal V17" module, Sage Paie Sénégal (~40–100k FCFA/yr est.) | All handle IPRES/CSS declarations. None offers a payment rail (from search summaries). | **LOW.** Integration targets. | [S42b] (search) **[UNVERIFIED]** for Sage pricing |
| Invoicing SaaS (SN) | **Facture SN** | Invoices with NINEA and VAT. **Collection by Wave/OM link or QR "sans commission"**. WhatsApp sending. VAT summary for the accountant. Team access and exports. **3,900 FCFA/month.** | **LOW–MEDIUM.** It covers Kelen's "invoices + payment links" at a very low price. A potential partner. | [S42] fetched |
| Invoicing SaaS | MaFactureProSN and others | Senegalese e-invoicing (DGID) timelines are contested: reception in 2026, issuing in 2027 per Baobizz (Aug 2025, search). | Watch: e-invoicing regulation may favour certified invoicing tools. **[UNVERIFIED]** | (search) |
| Salary advance | **Fintra** (Orya Technologies, SN, 2022) | Up to 20% of salary from the 15th of the month, paid to mobile money, 6% fee if repaid within 15 days. Employer-enrolled. Pilot Sept 2022. | **LOW–MEDIUM.** It validates demand for Kelen's salary-advance feature. | [S43] (search) |
| Salary advance | **BaraPay / BaraPaie** (CI) | Employer-set advance percentage. Paid to mobile money within 24h. "Ne coûte rien à votre employeur". Fixed withdrawal fee to the employee. | **LOW–MEDIUM.** | [S43] (search) |
| SME credit | **COFINA** (mesofinance, SN and CI) | EIB credit line (Sept 2023, €25M, of which €9.75M to COFINA SN). >440M FCFA to 57 agri SMEs (2024). | **MEDIUM** for Kelen's later loan product. Not digital-first. | [S53] (search) |
| SME credit | **Orange Bank Africa** | See §2.4. | **MEDIUM–HIGH** for credit. | [S33] [S34] |

No local spend-management player (a Ramp or Spendesk equivalent) was found in Senegal or CI. The infrastructure exists: GIM-UEMOA prepaid card programmes are open to EMEs and SFDs (search). **This is an open niche, inferred from the absence of results.**

---

## 5. Typical bank (benchmark column)

- **UBA Sénégal, Compte Entreprise** (data verified by Comparek on 13 Oct 2026) [S44]:
  - **SA/PME:** account maintenance **25,000 FCFA/month**, Internet Banking Entreprises with **grouped transfers** and reporting, corporate Visa Classic card **20,000 FCFA/year**.
  - **TPE / individual business:** 10,000 FCFA/month.
  - **NGO / public body:** 15,000 FCFA/month.
  - Opening is free but requires a **branch visit**.
- Other banks (SG Sénégal, Ecobank, BIS, CBAO, BOA Sénégal) are listed with no published fees [S44].
- BOA launched BOAWEB for corporates in Dakar in Oct 2019 (search). Its current SME digital offer was not verified **[UNVERIFIED]**.
- Interbank RTGS transfers in CI "can reach 17,000 CFA" per transfer (TechCabal 2021, search) **[UNVERIFIED for 2026]**.

---

## 6. Foreign-model entrants (WAEMU watch-list)

| Player | Status | Threat | Source |
|---|---|---|---|
| **Moniepoint** | Acquired 78% of Kenya's **Sumac Microfinance Bank** (Mar–May 2026). Phasing out its UK MonieWorld remittance business (Aug 2026) to focus on **Nigeria and Kenya**. No WAEMU licence or announcement found. | **LOW (2027 horizon).** Its "business-in-a-box" model is the closest analogue to Kelen. Acquiring an MFI is its entry playbook, so watch for a WAEMU MFI or bank target. | [S45] (search) |
| **TymeBank / GoTyme** | Expanding to the Philippines, Vietnam and Indonesia. No African expansion beyond South Africa found. | **LOW.** | [S46] (search) |
| **Qonto, Revolut Business** | No evidence of any WAEMU plan was found in searches. | **LOW.** | (no source found) |
| **Zazu** | A "Mercury-style" SME banking platform for Africa. $1M pre-seed (Dec 2025). Not Francophone West African. | **LOW.** | [S52] (search) |

## 7. Screened out (not relevant or no current SME offer)

These were checked briefly. Reasons without a source are general knowledge **[UNVERIFIED]**.
- **Cauri Money:** a diaspora neobank. It expanded to Cameroon through Gajo Money in Jul 2025 [S49] (search). It holds no WAEMU EP or EME licence of its own as of Jun 2026 [S9].
- **Kalpay:** a Senegalese wallet and Kalpay Business QR app founded in 2019. No recent activity found (search).
- **Wari:** collapsed. **Yup** (Société Générale): shut down. **[UNVERIFIED]**
- **Ejara, Afriex, LemFi, Chipper Cash, Kuda, Mono, Sudo Africa:** consumer or remittance products, or no WAEMU business banking. **[UNVERIFIED]**
- **Paps:** logistics.
- **Sycapay (SYCA):** a CI payment aggregator with an EP licence [S9]. Collections only.
- **Afriland First Bank, Baobab, NSIA, Bamboo:** no specific digital SME account found.
- **"BAMBA", "Kwik", "Ziwa", "Mansa", "Sabi", "Lono", "Kalanbi", "Weebi", "Kossi", "Comptaplus", "Fatura":** no relevant Senegal or CI SME-banking activity found in searches.

---

## 8. Feature matrix

**Legend:**
- **Y** = yes, documented. **P** = partial or limited. **N** = not offered or not documented. **?** = unknown.
- The source IDs are in brackets.
- The "Typical bank" column is UBA Sénégal [S44] plus general practice, which is marked **[U]** (unverified).
- The Kelen column is the planned offer from the brief.

| Feature | Julaya | Djamo Business | Wave Business | Orange Money business (SN) | Typical bank (UBA SN) | **Kelen (plan)** |
|---|---|---|---|---|---|---|
| IBAN / RIB business account | **P**: "RIB JULAYA" to receive UEMOA transfers; the bank is not named [S4] | **P**: IBAN advertised for Djamo accounts [S22]; business IBAN not explicit [S13] | **N** [S25] | **N**: wallet only [S31] | **Y** [S44] | **Y**, via partner bank |
| Multi-user / roles | **Y**: collaborators, per-user caps, deactivation [S5] | **?**: not documented [S13] [S19] | **P**: admin role for API keys only [S26] | **P**: multi-SIM tills and master SIM [S31] | **Y** [U] | **Y** |
| Approval workflow (double signature) | **Y**: "niveaux d'accès et de validation personnalisables", signing rights [S3] [S5] | **N** (not documented) [S13] | **N** (not documented) [S26] | **N** (not documented) [S31] | **P**: corporate e-banking usually has maker-checker [U] | **Y** |
| Bulk payroll to **banks** | **Y**: "tous les opérateurs… toutes les banques" [S3] | **P**: UEMOA bank transfers; bulk file payee types are unclear [S13] | **N** [S26] | **N** [S31] | **Y**: "virements groupés" [S44] | **Y** |
| Bulk payroll to **wallets** | **Y**: OM, Wave, MTN, Moov, Djamo [S2] [S3] | **P**: to Djamo accounts (API) [S16]; other wallets not stated | **P**: Wave/SMS-code only [S26] | **P**: Orange Money/code only [S31] | **N** [U] | **Y**: any wallet |
| Virtual cards | **N** (licence allows it) [S7] | **P**: consumer Visa cards; business card spec not stated [S13] | **P**: consumer virtual Visa only [S29] | **N** [S31] | **P**: physical corporate Visa; virtual not shown [S44] | **Y** |
| Physical cards | **N** [S1] | **Y**: "carte Djamo" per employee [S13] | **N** | **N** | **Y**: Visa Classic 20k/yr [S44] | **Y** |
| Invoices / payment links | **P**: bill pay and invoice collection; no invoice creation [S6] [S2] | **Y**: payment link and QR collections at 1% [S14] | **P**: API checkout, no invoices [S25] | **P**: Paiement Internet API [S31] | **N** [U] | **Y** |
| Collections via wallets | **Y**: Wave, Xpress cash and collect [S2] | **P**: QR/link; API is Djamo-only for now [S14] [S16] | **Y** [S25] | **Y**: OM, 1% [S31] | **N** [U] | **Y** (planned) |
| Sub-accounts | **Y** [S1] [S5] | **N** (not documented) | **P**: multiple wallets, one API key each [S26] | **P**: master and till SIMs, salary sub-accounts [S31] | **P**: multiple accounts [U] | **Y** |
| Accounting export / accountant access | **Y**: exports; no dedicated accountant role found [S1] | **P**: "exportables en un clic" [S13] | **P**: Business Portal history [S25] | **P**: back office [S31] | **P**: statements [U] | **Y**: accountant access and exports |
| API | **?**: not on the product pages | **Y**: payouts and collections (Djamo-only), 0.5% [S14] [S16] | **Y**: Checkout and Payout API [S25] [S26] | **Y**: Paiement Internet API [S31] [S32] | **P** [U] | **?** (not in brief) |
| SME credit | **N** today; planned (Oct 2025) [S10] | **N** for business; consumer credit up to 1M F in CI [S17] | **N**; bank licence pending [S28] | **Y** via Orange Bank Africa (Tik Tak, SME loans) [S33] [S34] | **Y** [U] | **Later** (MFI licence) |
| Employee salary accounts | **N** | **P**: employees get Djamo accounts and cards; "salary-linked accounts" [S13] [S20] | **P**: payee gets a Wave wallet [S26] | **P**: salary sub-accounts, 2 withdrawals/week [S31] | **Y**: salary accounts [U] | **Y** |
| Salary advance | **N** | **P**: consumer credit gated by salary domiciliation [S17] | **N** | **N** (not documented) | **P**: overdraft or advance on salary account [U] | **Y** |
| Cash deposit | **Y**: free at partner banks; MoMo cash top-up [S2] | **Y**: free deposits; agents [S22] | **Y**: agents [S25] | **Y**: agents | **Y**: branch | **?** (via partner bank / wallets) |
| **Pricing model** | % per transaction (0.5–1.5% to wallets) [S2] | Free account; 0.5% API, 1% collections [S14] | 1% payout, 1% merchant over 20k/day [S25] | Free sub; 1–1.5% payout, 1% collection [S31] | 10–25k FCFA/month + fees [S44] | **9,900 / 29,900 / 79,900 FCFA/month** |

---

## 9. Pricing benchmark against Kelen's plans

The figures below are an illustrative calculation using published rates. The scenario is an SME paying **20 employees × 150,000 FCFA = 3,000,000 FCFA** in monthly payroll to wallets (an assumption).

| Provider | Payroll cost per month | Account fee | Notes |
|---|---|---|---|
| Wave Business | 1% → **30,000 FCFA** | 0 | [S25] |
| Orange Money Paiement Pro | 1% (payee has OM) → **30,000 FCFA** | 0 | [S31] |
| Julaya | 0.5–1.5% → **15,000–45,000 FCFA** | none published | [S2] |
| Djamo Business (web bulk) | **0** (to Djamo accounts) | 0 | [S14]. Payees must hold Djamo accounts. |
| UBA Sénégal | bank-transfer fees (not published) | **25,000 FCFA** (PME) | [S44] |
| **Kelen Standard (29,900 FCFA)** | to be defined | 29,900 | It competes if it **includes** payroll payouts. At about 1% the break-even is about 3M FCFA of payroll per month. |

What this implies:
- **Kelen's subscription must bundle payout volume.** One option is X free payouts per month or an included payroll value, so that it beats the 1% wallet benchmark for SMEs with payrolls of 3M FCFA or more.
- **Kelen should position against bank fees rather than wallet fees.** The 9,900 plan is below UBA's TPE fee of 10,000 FCFA/month and well below its PME fee of 25,000 FCFA/month [S44].
- **Djamo's free business account is the main price threat at the low end.** Kelen's differentiation has to be control (approvals, roles, accountant access) and multi-rail payouts.

---

## 10. Sources

**Julaya**
- [S1] Julaya homepage: https://julaya.co (fetched; accessed 2026-10-14)
- [S2] Julaya pricing: https://julaya.co/fr/prices (fetched; accessed 2026-10-14)
- [S3] Julaya transfers product: https://julaya.co/fr/products/transfer (fetched; accessed 2026-10-14)
- [S4] Julaya RIB feature: https://julaya.co/fr/features/iban (fetched; accessed 2026-10-14)
- [S5] Julaya access levels: https://julaya.co/fr/features/accessibility-levels (fetched; accessed 2026-10-14)
- [S6] Julaya billing: https://julaya.co/fr/products/billing (fetched; accessed 2026-10-14)
- [S7] Julaya press release on its EP licence: https://blog.julaya.co/communique/ (fetched; dated 2025-05-10/13)
- [S10] Ecofin Agency, "Julaya secures CFA800mln from CDC-CI Capital": https://www.ecofinagency.com/news-finances/2110-49719-julaya-secures-cfa800mln-from-cdc-ci-capital-for-regional-expansion (fetched; 2025-10-21)
- [S11] Launch Africa, Julaya $2M pre-Series A: https://www.launchafrica.vc/news/ivorian-fintech-julaya-raises-2m-to-digitize-business-payments-in-francophone-africa (fetched; Jul 2021)
- [S12] TechCabal, Julaya $5M extension: https://techcabal.com/2022/09/21/west-african-fintech-julaya-raises-us5m-extension-round-to-expand-its-operations/ (search; 2022-09-21)

**Regulators**
- [S8] BCEAO, list of EPs in UMOA as of 28 Feb 2026: https://www.bceao.int/sites/default/files/2026-03/LISTE%20DES%20ETABLISSEMENTS%20DE%20PAIEMENT%20AGR%C3%89%C3%89S%20DANS%20L%E2%80%99UMOA%20au%2031%20janvier%202026.pdf (fetched PDF; Mar 2026)
- [S9] Commission Bancaire UMOA, EME and EP lists updated 29 Jun 2026: https://www.cb-umoa.org/sites/default/files/Liste%20%20des%20EME%20ET%20EP%20de%20l%27UMOA%202026.pdf (fetched PDF; 2026-06-29)

**Djamo**
- [S13] Djamo Business CI: https://www.djamo.com/fr-ci/compte-business and https://www.djamo.com/ci/business/ (fetched; accessed 2026-10-14)
- [S14] Djamo business pricing: https://www.djamo.com/fr-ci/tarifs-business (fetched; accessed 2026-10-14)
- [S15] Djamo Business SN: https://www.djamo.com/fr-sn/compte-business (fetched; accessed 2026-10-14)
- [S16] Djamo API: https://www.djamo.com/fr-ci/api (fetched; accessed 2026-10-14)
- [S17] Djamo credit: https://www.djamo.com/fr-ci/credit (fetched; accessed 2026-10-14)
- [S18] Djamo consumer pricing: https://www.djamo.com/fr-ci/tarifs (fetched; accessed 2026-10-14)
- [S19] Djamo SN help, "C'est quoi Djamo Business ?": https://support-sn.djamo.com/fr/articles/12461355-c-est-quoi-djamo-business (fetched; 2025-09-30)
- [S20] TechCrunch, "Djamo raises $17M…": https://techcrunch.com/2025/04/03/djamo-raises-17m-and-has-1m-users-across-francophone-africa (fetched; 2025-04-03)
- [S21] ITWeb Africa, "Djamo targets Francophone Africa with $40m raise": https://itweb.africa/article/djamo-targets-francophone-africa-with-40m-raise/nWJad7bNlr47bjO1 (fetched; 2026-07-08)
- [S22] Directactu, "Djamo Sénégal…": https://directactu.net/2026/04/02/djamo-senegal-la-fintech-qui-revolutionne-linclusion-financiere-par-le-digital/ (fetched; 2026-04-02)
- [S23] Ecofin Agency, Djamo BCEAO microfinance approval: https://www.ecofinagency.com/finance/1209-48632-ivorian-fintech-djamo-breaks-new-ground-with-bceao-microfinance-approval (search; 2025-09-12). Also TechMoran: https://techmoran.com/2025/09/12/ivorian-fintech-djamo-obtains-microfinance-license-to-offer-savings-cash-loans/ (search)
- [S24] Y Combinator, Djamo: https://www.ycombinator.com/companies/djamo (fetched; accessed 2026-10-14)

**Wave**
- [S25] Wave Business: https://www.wave.com/fr/business/ (fetched; accessed 2026-10-14)
- [S26] Wave Payout API docs: https://docs.wave.com/payout (fetched; accessed 2026-10-14)
- [S27] Ecofin Agency, "Wave Launches Commercial Bank in Côte d'Ivoire": https://www.ecofinagency.com/news-finances/2610-49842-wave-launches-commercial-bank-in-cote-d-ivoire (fetched; 2025-10-26)
- [S28] Abidjan Économie, "Wave, la révolution est-elle toujours en marche ? (2026)": https://www.abidjaneconomie.net/2026/05/04/wave-ci-bilan-2025/ (fetched; 2026-05-04)
- [S29] Agence Ecofin, Wave virtual Visa card: https://www.agenceecofin.com/actualites-numerique/2601-135155-senegal-wave-lance-avec-visa-une-carte-bancaire-virtuelle-pour-les-paiements-internationaux (search; Jan 2026)
- [S30] Simiz, Wave merchant guide: https://simiz.io/blog/ouvrir-compte-marchand-wave-senegal (fetched; 2026-08-21; third party)

**Orange**
- [S31] Orange Business Sénégal, Orange Money B2B: https://www.orangebusiness.sn/orange-money (fetched; accessed 2026-10-14)
- [S32] Orange Business CI, Orange Money solutions: https://business.orange.ci/fr/b2b-orangemoney-nossolutions.html (fetched; accessed 2026-10-14)
- [S33] Ecofin Agency, IFC $30.6M guarantee for Orange Bank: https://www.ecofinagency.com/news-finances/0302-52548-ifc-to-provide-30-6m-guarantee-for-orange-bank-digital-lending-in-cote-d-ivoire-senegal (fetched; 2026-02-03)
- [S34] Ecofin Agency, SGPME and Orange Bank guarantee agreements: https://www.ecofinagency.com/news-finances/2607-57726-cote-d-ivoire-s-sme-agency-orange-bank-sign-guarantee-agreements-to-expand-sme-lending (fetched; 2026-07-26)

**Tier 2 players**
- [S35] InTouch website: https://www.intouchgroup.net/en (fetched; accessed 2026-10-14)
- [S36] Le Soleil / Osiris, InTouch licences: https://lesoleil.sn/web-tv/startup-a-la-une/monnaie-electronique-et-etablissement-de-paiement-intouch-decroche-ses-licences/ (search; 2025)
- [S37] PayDunya website: https://paydunya.com/ (fetched; accessed 2026-10-14)
- [S38] Condia, HUB2 $8.5M: https://thecondia.com/ivory-coast-fintech-hub2-raises-8-5m-stripe-francophone-africa/ (search; Dec 2024)
- [S39] TechCabal (FR), CinetPay cyberattack report: https://techcabal.com/fr/?p=179865 (search; late 2025). The URL-to-article mapping is **[UNVERIFIED]**. The CinetPay transfer docs are at https://docs.cinetpay.com/api/1.0-en/BO/virer-fond (search)
- [S40] We Are Tech, Wizall Money Pro: https://www.wearetech.africa/fr/fils/solutions/senegal-wizall-money-propose-des-services-financiers-aux-entreprises-et-aux-particuliers (search; undated). Kolonell fee estimate: https://kolonell.com/fr/blog/wizall-paiement-entreprise-senegal-frais-2026 (search; Jun 2026; Kolonell is a Dakar web agency's blog, low reliability)

**Tier 3 players**
- [S41] KayFay: https://kayfay.com/ (fetched; accessed 2026-10-14)
- [S42] Facture SN: https://facturesn.com/ (fetched; accessed 2026-10-14)
- [S42b] Payroll SaaS search summaries: https://www.sunupayrh.com/paie-senegal, https://www.cloudpaie.com/, https://apps.odoo.com/apps/modules/17.0/hr_payroll_seng (search; accessed 2026-10-14)
- [S43] Agence Ecofin, Fintra: https://www.agenceecofin.com/entreprendre/1710-102091-des-avances-sur-salaires-grace-a-fintra-l-application-concue-par-le-senegalais-oumar-diallo (search; 2022). BaraPay: https://barapay.africa/ (search; accessed 2026-10-14)
- [S44] Comparek.sn, Compte Entreprise (UBA Sénégal): https://comparek.sn/banques/produits/compte-entreprise (fetched; data "vérifiées le 13 octobre 2026")

**Foreign entrants and screened-out players**
- [S45] WeeTracker, Moniepoint acquires Sumac Bank: https://weetracker.com/2026/03/27/moniepoint-acquires-sumac-bank-kenya-fintech-expansion/ (search; 2026-03-27). TechCabal, MonieWorld phase-out: https://techcabal.com/2026/08/25/moniepoint-phasing-out-monieworld-uk-remittance/ (search; 2026-08-25)
- [S46] BusinessTech, TymeBank international: https://businesstech.co.za/news/business/844767/south-african-bank-moving-big-in-international-markets/ (search; late 2025)
- [S47] Financial Afrik, Mastercard and New Africa Technology: https://www.financialafrik.com/2024/11/20/mastercard-collabore-avec-new-africa-technology-pour-lancer-un-programme-de-cartes-fintech-au-senegal-en-cote-divoire-et-au-benin (search; 2024-11-20)
- [S48] Osiris, Mixx by Yas card and labour dispute: https://osiris.sn/mixx-by-yas-lance-une-carte-prepayee-pour-booster-l-inclusion-financiere-au.html and https://www.osiris.sn/crise-sociale-chez-mixx-le-personnel-de-yas-denonce-un-licenciement-abusif-et.html (search; 2025–Feb 2026)
- [S49] Ecomatin, Cauri Money in Cameroon: https://ecomatin.net/fintech-le-senegalais-cauri-money-debarque-au-cameroun-et-vise-79-milliards-fcfa-de-transferts (search; Jul 2025)
- [S50] Financial Afrik, BCEAO-licensed fintechs as of 27 May 2025: https://www.financialafrik.com/2025/05/27/uemoa-les-fintech-officiellement-agreees-par-la-bceao-au-27-mai-2025-exclusif/ (search; 2025-05-27)
- [S51] MCTaba, Paystack settlement in CI: https://mctaba.com/learn/paystack/settlement-and-payouts-on-paystack-in-cote-d-ivoire (search; third party; undated)
- [S52] TechCabal, Zazu $1M pre-seed: https://techcabal.com/2025/12/01/zazu-raises-1-million-pre-seed/ (search; 2025-12-01)
- [S53] EIB, COFINA Senegal agricultural SMEs: https://www.eib.org/fr/press/all/2024-324-cofina-senegal-finance-les-pme-agricoles-avec-le-soutien-de-la-bei-et-de-l-ue (search; 2024)
