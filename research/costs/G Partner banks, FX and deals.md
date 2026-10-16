# G. Partnership deals and costs: partner bank, deposits, agents, international payments, partner SFD

Research date: 2026-10-16. Scope: Kelen (B2B neobank for SMEs, Senegal 2027, then Côte d'Ivoire), running on a partner bank's licence.

Conventions
- Every figure has a source and a date. "Search extract" means the figure came from a search-engine summary of a page that could not be opened (bot-blocked or 403). Treat it as unverified.
- **PROXY** = evidence from outside WAEMU, or from a different product. Use it only for orders of magnitude.
- **Not found** = searched and no public figure exists. Most bank–fintech contracts in WAEMU are private.
- FX used for conversions: EUR 1 = 655.957 FCFA (fixed peg). USD mid ≈ 584.75 FCFA (BCEAO buy 581.25 / sell 588.25, 15 Oct 2026, https://www.bceao.int/fr).

---

## 0. Key takeaways

1. **No WAEMU bank publishes BaaS terms.** We found no public set-up fee, per-account fee, platform minimum or deposit revenue share for any WAEMU bank–fintech deal (Djamo, Julaya, Wave, Hub2, PUSH and others). Kelen's model values for these items can only be checked against US/African proxies and against the banks' own public tariffs.
2. **Deposit value is falling.** The BCEAO cut its policy rate to 3.00% (16 Mar 2026). The interbank average fell to **4.52% in Q1 2026**, from 5.11% in Q4 2025 and 6.01% a year earlier. A 1.5% share of balances paid to Kelen is about **33% of the interbank yield** on free current-account money. That is in line with the only hard proxy we found (US Vast Bank/USBC: 40–50% of deposit revenue *net of programme costs*). But it is optimistic for Year 1, and it is exposed to further rate cuts.
3. **Outbound transfers carry a 0.6% tax that sits outside any margin.** Every formal transfer out of WAEMU pays a **0.6% tax on transfers outside the UEMOA (TTHU, "taxe Etat")**. It appears in UBA CI, SIB CI, SG Sénégal and Versus Bank tariffs. On top of that, the BCEAO's own buy/sell spread is about **±0.6% on USD and ±1.0% on CNY/AED**. A Kelen cost of **0.5% is achievable only for EUR payments (France), and only excluding the tax**. For USD/CNY/AED/TRY a realistic all-in cost is **1.0–1.8% plus fixed SWIFT/correspondent fees**.
4. **Bank prices to SMEs for outbound transfers are high.** Published commissions run 0.85% (SG Sénégal, minimum 20k FCFA) to **1.5–2.0%** (UBA CI, SIB CI), plus 0.6% tax, plus 25–60k FCFA in fixed fees, plus the FX margin. A Kelen price of 1.5% is competitive if the 0.6% tax is passed through on top.
5. **Lending-as-a-service:** no public WAEMU revenue-share or first-loss terms were found. Proxies support a 40–50% split and a 5–10% first-loss reserve. The usury ceiling for SFDs is **24%** (14% for banks) from 1 June 2026. That leaves room for a margin worth sharing.

---

## 1. Bank–fintech partnerships and BaaS in WAEMU

### 1.1 Who partners with whom (public evidence)

| Bank | Fintech / partner | What is offered | Commercial terms disclosed? | Source (date) |
|---|---|---|---|---|
| BGFIBank CI | Djamo CI | Co-branded prepaid Visa cards ("BGFI CI-Djamo") | No | BCEAO list of bank-led e-money partnerships, as of 14 Mar 2024: https://www.bceao.int/en/content/electronic-money-issuing-institutions-0 |
| Ecobank Senegal | Djamo | Co-branded cards "Ecobank SN-Djamo" | No | Same BCEAO list (14 Mar 2024) |
| BGFIBank CI / Ecobank CI | Djamo | Visa card "émise par nos partenaires BGFIBank Côte d'Ivoire ou Ecobank Côte d'Ivoire". Djamo also advertises an IBAN, free to open, but the page does not name the bank holding it. | No | https://www.djamo.com/ci/iban/ (accessed 2026-10-16) |
| (own licence) | Djamo Finances SA | Microfinance licence (Sept 2025). Savings up to 6%/yr, cash credit up to 1M FCFA for individuals and SMEs. No pre-licence SFD partner documented. | n/a | https://www.ecofinagency.com/finance/1209-48632-ivorian-fintech-djamo-breaks-new-ground-with-bceao-microfinance-approval (12 Sep 2025) |
| Ecobank CI, SIB (CI), plus UBA and SGBCI for cash deposits | Julaya | Collection accounts in Julaya's name ("RIB Julaya") at Ecobank CI (SWIFT ECOCCIAB) and SIB (code banque CI007). Clients top up by transfer or cash at partner banks. Julaya holds a payment institution (EP) licence. "Partner of 10 banks in CI and SN" (2022 Series A press). | No | RIB PDF: https://6087706.fs1.hubspotusercontent-na1.net/hubfs/6087706/RIB%20ECOBANK%20JULAYA%20COTE%20D%20IVOIRE.pdf (undated); SIB RIB: https://6087706.fs1.hubspotusercontent-na1.net/hubfs/6087706/JCI_BANQUE_RIB_SIB_OPERATIONS.pdf (undated); FAQ: https://blog.julaya.co/f-a-q-familiarisez-vous-avec-julaya/ ; https://www.frenchweb.fr/serie-a-julaya-fintech-franco-ivoirienne-leve-5-millions-de-dollars-aupres-de-speedinvest/435607 |
| BOA Côte d'Ivoire | Julaya | BOA sells a "Bulk Payment (Julaya)" service to its corporate clients (mass payouts to wallets). This is a bank distributing a fintech product. We found no evidence of a white-label Julaya account. | No | https://boacoteivoire.com/pme/comptes-services/bulk-payment/ (accessed 2026-10-16) |
| UBA CI, Orabank CI (CI); Ecobank SN, UBA SN (SN) | Wave | Bank-led e-money partnerships (Wave as distributor). Wave Digital Finance (SN) later got its own EME licence (2022). | No | BCEAO list (14 Mar 2024); background: https://magazinedelafrique.com/dossier-senegal/lafrique-de-louest-vit-une-revolution-dans-le-mobile-money/ (older) |
| Ecobank SN + Visa | Wave | Wave virtual Visa card (launched 23 Jan 2026) | No | https://www.financialafrik.com/2026/01/24/senegal-wave-lance-une-carte-virtuelle-avec-visa-et-ecobank/ (24 Jan 2026) |
| UBA SN, Banque Atlantique SN | Wave | Bank↔Wave wallet link priced at **1% TTC per transaction to the customer**. Search extract, unverified. | Customer price only | Search extract (Oct 2026); originating page not opened |
| Banque Atlantique SN (issuer) / BACI (CI) / Ecobank SN | Wizall Money (BCP group) | Wizall is a BCEAO-approved e-money *distributor*. The issuer is Banque Atlantique (same BCP group). | No | https://www.osiris.sn/senegal-wizall-money-partenaire-du-gouvernement-dans-le-cadre-des-transferts.html (2022); BCEAO list (14 Mar 2024) |
| Ecobank Transnational | Hub2 | MoU signed 25 Feb 2026 in Lomé. Connects Hub2's single API (200M+ wallets, 12 countries incl. SN, CI) to Ecobank's settlement network in 32 markets. Phased rollout, UEMOA and CEMAC first. | **No** (no fees, split or exclusivity disclosed) | https://www.financialafrik.com/2026/02/25/ecobank-et-hub2-elargissent-lacces-aux-paiements-numeriques-a-200-millions-dutilisateurs-de-portefeuilles-mobiles-en-afrique-francophone/ (25 Feb 2026) |
| Ecobank Group | Unified API / sandbox ("Ecobank Developer") | Collections (QR, cards, mobile money), payouts to accounts and wallets. Sandbox on request. Fintech Challenge with a $50k prize; 2024 themes included BaaS. | **No public pricing** | https://www.ecobank.com/fintech ; https://documenter.getpostman.com/view/1855568/SW7ezR5q |
| Ecobank Group | CIPS (China) | MoU to join CIPS for yuan settlement for corporate clients (Oct 2026). Direct local-currency→CNY product targeted by end-2026. | No | https://www.globenewswire.com/news-release/2026/10/12/3379080/0/en/ecobank-group-and-cips-partner-to-strengthen-china-africa-financial-corridor.html (12 Oct 2026) |
| BNI, Ecobank CI, Versus Bank (+ Orange Money) | PUSH CI | Partnerships for cocoa/coffee payment traceability. 700k+ individual accounts. | No | https://news.abidjan.net/articles/749614/ (15 Oct 2026, sponsored article) |
| BNDE (Senegal) | Kopar Express | Agreement (24 Oct 2024) to create a diaspora neobank. Kopar supplies the tech. Launch not confirmed. | No | https://www.sikafinance.com/marches/senegal-la-neo-banque-consacree-a-la-diaspora-sera-operationnelle-en-decembre_48944 (2024) |
| Coris Bank BF | Orange Money | Bank-to-wallet / wallet-to-bank (5 Aug 2026) | No | https://cfinance.news/index.php/fr/fintech/technologie/1351-burkina-faso-inclusion-financiere-coris-bank-et-orange-money-rapprochent-la-banque-du-mobile |
| Société Générale | YUP (own e-money) | **Closed in March 2022**: "not a viable model". About 2M clients. Investors lost about $8M. | n/a | https://itweb.africa/article/e-wallet-yup-closes-up-shop-in-africa/lwrKx73K6V87mg1o (2022); https://launchbaseafrica.com/2024/11/04/french-banks-african-fintech-arm-yup-leaves-investors-with-over-8m-loss-post-liquidation (4 Nov 2024) |
| PayDunya | — | Payment institution (EP) licence under Instruction 001-01-2024. Acquired by Peach Payments (announced Apr 2025). Partner bank not found. | No | https://www.dabafinance.com/en/news/peach-payments-to-acquire-senegal-s-paydunya-in-west-africa-push (Apr 2025) |
| Kalpay | — | **Not found** (partner bank / terms) | — | — |
| CBAO, Bridge Bank, NSIA, Orabank (beyond Wave), Afriland, Coris (SN/CI) | — | **No public BaaS / fintech-account offer found** | — | — |

Regulatory facts that shape any partnership:
- **PI-SPI interoperability.** All banks, EMIs and EPs had to connect by 30 Jun 2026, and 24 business APIs were approved by 16 Sep 2026 (https://www.agenceecofin.com/actualites-finance/1709-141663-uemoa-24-solutions-permettent-desormais-aux-entreprises-d-utiliser-le-paiement-instantane). From 2 Nov 2026, domestic e-money transfers are **free up to 8,000 FCFA/day/user/participant**, with **up to 0.8% excl. tax** above that. Intra-UEMOA cross-border transfers follow from 1 Jun 2027 (https://www.togofirst.com/fr/finance/1210-20307-uemoa-la-bceao-double-le-plafond-des-comptes-mobile-money-a-l-heure-de-pi-spi, 12 Oct 2026).
- **E-money issuance cannot be outsourced to a technical operator** (Instruction 008-05-2015, art. 4). The issuer bank stays responsible. https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf
- **The IOB status was replaced by the "agent bancaire" status** (UEMOA regulation of 2023). Agents can open accounts under a bank mandate. https://fr.allafrica.com/stories/202602020483.html (Nov 2025)

### 1.2 Reported commercial terms (WAEMU): none public

| Term | WAEMU evidence | PROXY evidence | Source (date) |
|---|---|---|---|
| Set-up / integration fee | **Not found** | US sponsor banks: **$0 to $100,000+**; some banks waive it and BaaS platforms charge onboarding instead | PROXY: https://fintechspecs.com/blog/what-is-a-sponsor-bank/ (18 Jul 2026) |
| Monthly platform minimum | **Not found** | US: **$5,000–50,000/month** (≈2.9M–29M FCFA) | PROXY: same (18 Jul 2026) |
| Middleware BaaS platform fee | **Not found** | US: $1k–25k/month (search extract, vendor) | PROXY, unverified |
| Compliance audit cost borne by fintech | **Not found** | US: $20k–150k/yr | PROXY: fintechspecs (18 Jul 2026) |
| Per-account fee | **Not found** | Not published even in the US ("no standard rate card") | fintechspecs (18 Jul 2026) |
| Interchange split | **Not found** | US: bank keeps **10–40%** of interchange | PROXY: fintechspecs (18 Jul 2026) |
| Deposit revenue share | **Not found** | US Vast Bank / USBC / Uphold contract: deposit revenue, *after programme costs*, split **Vast 60 / USBC 40 (Y1), 55/45 (Y2), 50/50 (Y3+)**. Floor = balances × (Prime − 450 bp) | PROXY: SEC 8-K exhibit, effective 20 Jan 2026: https://www.sec.gov/Archives/edgar/data/1074828/000165495426000601/usbc_101.htm |
| Deposit revenue as fintech income | **Not found** | Mercury (US SME neobank): majority of ~$500M annualised revenue from interest sharing with partner banks (~90% per secondary estimate) | PROXY: https://sacra.com/research/mercury-at-500m-annualized-revenue/ (2025) |
| Revenue share on fees/subscriptions | **Not found** | Duplo × Wema/ALAT Business (Nigeria): share subscription revenue, split undisclosed | PROXY: https://techcabal.com/2026/07/24/duplo-wants-to-reach-more-businesses-through-banks/ (24 Jul 2026) |
| Nigeria BaaS (Anchor) | — | Revenue = processing fees + **account/card issuance fees** + float interest; amounts "contact sales" | PROXY: https://nairametrics.com/?p=463633 (search extract) |
| What Moniepoint / Kuda paid partner banks | **Not found** | Kuda partnered GTBank/Access/Zenith (old); Kuda, Moniepoint and others got national licences by Jan 2026 | https://allbusiness.africa/insights/african-bank-fintech-partnerships-2026 (12 Apr 2026) |

### 1.3 What banks charge SMEs directly (benchmark for the per-account fee)

| Bank | Item | Price | Source (date) |
|---|---|---|---|
| UBA CI (Entreprises 2026) | Current account opening | Free; initial deposit 250k (EI) / 500k (SARL) / 1M (SA), half held in escrow | https://www.ubacotedivoire.com/wp-content/uploads/sites/12/2026/04/Conditions-tarifaires-Entreprises-UBA-CI-2026.pdf (Apr 2026) |
| UBA CI (2026) | Debit turnover commission (companies) | **0.040%/month, minimum 5,000 FCFA** | same |
| UBA CI (2026) | Account maintenance fee, chequing account (individual) / institutional clients | 5,000 FCFA/month / 5,000 FCFA/month | same |
| UBA CI (2026) | Local interbank transfer / regional transfer / SICA / RTGS | 750 / 5,000 / 10,000 / 15,000 FCFA | same |

So an SME pays a WAEMU bank roughly **≥5,000 FCFA/month** in minimum account charges, plus per-transaction fees. A wholesale fee of 3,000 FCFA/month paid by Kelen to the bank would be about 60% of that retail floor, which is on the high side for a wholesale price.

---

## 2. Deposit economics

### 2.1 E-money float rules (BCEAO)

| Rule | Value | Source (date) |
|---|---|---|
| EMIs may not pay interest on e-money funds, nor grant credit | Art. 5, Instruction 008-05-2015 | https://www.bceao.int/sites/default/files/2017-11/instruction_no008_05_2015_intranet.pdf (21 May 2015) |
| Cover ≥ 100% of e-money outstanding, in a dedicated account at banks/SFDs, reconciled daily, not usable for operations | Art. 33 and cover article | same |
| Allowed placements: demand deposits, term deposits, government/regional/BRVM-listed securities | Art. 34 | same |
| Minimum share held in demand deposits | **75%** (2015) → **65%** from **2 Nov 2026** (Instruction n°020 of 8 Oct 2026, replacing arts 31 and 34) | https://www.financialafrik.com/2026/10/09/umoa-la-bceao-double-le-plafond-des-avoirs-en-monnaie-electronique-a-4-millions-de-fcfa/ (9 Oct 2026); https://www.togofirst.com/fr/finance/1210-20307-uemoa-la-bceao-double-le-plafond-des-comptes-mobile-money-a-l-heure-de-pi-spi (12 Oct 2026) |
| Wallet balance cap / monthly reload cap per client per issuer | 2M → **4M FCFA**; 10M → **15M FCFA** (from 2 Nov 2026) | Togo First (12 Oct 2026) |
| Remuneration paid by banks on cantonnement (cover) accounts | **Not found** (no regulation and no disclosed rate). The BCEAO notes the e-money model relied mainly on cash-out fees. | World Bank WAEMU doc: https://documents1.worldbank.org/curated/en/099050523150080117/pdf/P173143-11131e66-2bf2-406d-a46e-e71c4011163a.pdf |
| PROXY (Ghana) | Bank of Ghana: providers must pass **≥80% of trust-account interest** to customers (2016 rule) | https://clmr.unsw.edu.au/sites/default/files/content_files/Case%20Study%20on%20Payment%20of%20Interest%20-%20Ghana.pdf (older) |
| PROXY (Kenya) | E-money issuers may not earn interest; trust income goes to charity | https://www.gsma.com/solutions-and-impact/connectivity-for-good/mobile-for-development/gsma_resources/regulatory-approaches-to-managing-interest-on-mobile-money-trust-accounts/ (2024) |

Relevance to Kelen: under the agent model, client funds are **bank deposits, not e-money**, so the e-money rules do not apply directly. If Kelen later holds an EME/EP licence, its float would be at most 35% placeable in term deposits/securities from Nov 2026.

### 2.2 Interest rates (BCEAO)

| Indicator | Value | Period | Source (date) |
|---|---|---|---|
| Policy rate (minimum bid rate) | **3.00%** (cut from 3.25%) | from 16 Mar 2026; held 10 Jun and 9 Sep 2026 | https://www.koaci.com/article/2026/03/05/cote-divoire/economie/cote-divoire-bceao-le-principal-taux-directeur-auquel-la-banque-centrale-prete-ses-ressources-aux-banques-est-desormais-fixe-a-3-le-gouverneur-brou-sexplique_194838.html (5 Mar 2026); https://www.financialafrik.com/2026/09/09/uemoa-la-bceao-maintient-ses-taux-directeurs-linflation-attendue-a-1-en-2026/ (9 Sep 2026) |
| Marginal lending rate | 5.00% | same | same |
| Reserve requirement | 3.00% | same | same |
| Interbank weighted average, all maturities | **4.52%** (Q1 2026); 5.11% (Q4 2025); 6.01% (Q1 2025) | Q1 2026 | BCEAO Rapport politique monétaire juin 2026: https://www.bceao.int/sites/default/files/2026-07/RAPPORT_SUR_LA_POLITIQUE_MONETAIRE_DANS_L-UMOA-JUIN_2026.pdf |
| 1-week interbank (weekly) | 4.70–5.26% | Oct–Dec 2025 | BCEAO Bulletin trimestriel T4 2025: https://www.bceao.int/sites/default/files/2026-04/Bulletin-Trimestriel-des-Statistiques-Quatri%C3%A8me-trimestre-2025.pdf |
| Average term-deposit rate, UEMOA | **5.27%** (Q1 2026); 5.48% (Q4 2025) | Q1 2026 | RPM juin 2026 (above) |
| Term-deposit rate, Senegal | **5.62%** (Q1 2026); 5.56% (Q4 2025) | | RPM juin 2026 |
| Term-deposit rate, Côte d'Ivoire | **4.76%** (Q1 2026); 5.01% (Q4 2025) | | RPM juin 2026 |
| Annual term-deposit rate 2024: UEMOA / SN / CI | 5.30% / 5.62% / 4.84% | 2024 | BCEAO Rapport conditions de banque 2024: https://www.bceao.int/sites/default/files/2025-07/Rapport%20sur%20les%20conditions%20de%20banque%20dans%20l'UEMOA%20-%202024_compressed.pdf (Jul 2025) |
| Term-deposit rate by depositor 2024: private non-financial companies / individual enterprises / legal persons | 4.97% / 5.61% / 5.31% | 2024 | same |
| Special-regime savings ("épargne à régime spécial") | 3.59% | 2024 | same |
| Average lending rate: UEMOA / SN / CI | 6.72% / 6.32% / 6.06% | Q1 2026 | RPM juin 2026 |
| Government bills (weighted average) | 5.88% | Q4 2025 | RPM mars 2026: https://www.bceao.int/sites/default/files/2026-03/RAPPORT-SUR-LA-POLITIQUE-MONETAIRE-DANS-L-UMOA-DE-MARS-2026.pdf |
| Remuneration of demand deposits / current accounts | **Not found** as a statistic. Current accounts are generally not paid interest; the BCEAO publishes only term-deposit rates. | — | — |
| Usury ceiling | **Banks 14%; other institutions incl. SFDs 24%** (from 1 Jun 2026; banks previously 15%) | Decision n°19 of 29 Dec 2025 | https://www.bceao.int/sites/default/files/2026-01/Decision-No19-du-29-12-2025_CMUMOA_fixant_le_taux_de_l-usure.pdf |

### 2.3 What a 1.5% share means for the bank (our arithmetic, not a source)

| Bank's yield on SME current-account balances (cost ≈ 0%) | Value | 1.5% to Kelen as % of that yield | 1.0% | 2.0% |
|---|---|---|---|---|
| Interbank Q1 2026 (4.52%) less reserve drag (3% × 4.52%) ≈ 4.4% | 4.4% | **34%** | 23% | 45% |
| T-bills (5.88%) ≈ 5.7% after reserves | 5.7% | 26% | 18% | 35% |
| If policy rate −50 bp more (interbank ≈ 4.0%) | 3.9% | 38% | 26% | 51% |

Evidence of revenue sharing on balances **in WAEMU: not found**. The closest proxy is Vast/USBC (US, 2026): **40% rising to 50%** of deposit revenue to the programme manager, net of costs, with a floor. Note also that the bank's alternative is to pay **~5% on term deposits** (SN 5.6%) for stable funding. A bank may therefore value sticky SME current-account balances highly, but it will want the share indexed to its reference rate, not fixed.

---

## 3. Agent ("agent bancaire" / IOB) economics

| Item | Value | Source (date) |
|---|---|---|
| Commission a WAEMU bank pays an agent per account opened | **Not found** | — |
| Commission on balances / distribution paid to agents in WAEMU | **Not found** | — |
| Legal frame | IOB status replaced by "agent bancaire" (UEMOA regulation 2023). IOBs say banks give them little partnership support. | https://fr.allafrica.com/stories/202602020483.html (Nov 2025) |
| PROXY (e-money, Burkina Faso) | Orange Money sub-distributor: **150 FCFA per wallet created** (with 500 FCFA load); 0.30% on deposits, 0.40% on withdrawals | https://www.investirauburkina.net/idees-de-business/devenir-revendeur-sous-distributeur-orange-money-au-burkina-faso-capital-minimum-benefices-et-conditions-douverture.html (≈2022, may be outdated) |
| PROXY (Kenya, Equity Bank) | Bank pays agents commissions on deposits and withdrawals (no customer charge on deposits); per-account figure not given | https://www.microsave.net/files/pdf/1370324973_BN_140_Success_Factors_of_EB_Agency_Banking.pdf (Apr 2013) |

---

## 4. International B2B payments out of WAEMU

### 4.1 Regulation

| Rule | Value | Source (date) |
|---|---|---|
| Framework | Règlement n°06/2024/CM/UEMOA (20 Dec 2024). Application instructions in force from 1 Aug 2025. | https://www.financialafrik.com/2026/03/24/reglement-06-2024-uemoa-ce-qui-change-vraiment-pour-les-banques-et-les-entreprises/ (24 Mar 2026) |
| Import domiciliation threshold | **> 20M FCFA** (was 10M). Now covers **services** as well as goods. | Instruction n°02/07/2025/RFE, art. 6; https://bankipay.io/blog/payer-prestation-services-etranger (7 Oct 2026) |
| Below the threshold | FX released on a final invoice | same |
| Advance payments | Capped at **50%** of value, on invoice or contract | same |
| Liability | Importer and approved intermediary jointly liable for clearing domiciliation files | Financial Afrik (24 Mar 2026) |
| Who can execute | Outbound FX transfers go through an **approved intermediary (bank)**. Kelen therefore depends on its partner bank (or Ecobank/another bank) for execution. | Règlement 06/2024 (above) |
| Tax on transfers outside UEMOA | **0.6% of amount** (TTHU / "taxe Etat"). Plus TOB 10% on the commission in CI. | UBA CI 2026, SIB CI 2025, SG SN 2026 (below) |

### 4.2 Published bank tariffs for outbound SWIFT (SME/corporate)

| Bank (country, date) | Transfer commission | FX commission | Fixed fees | Tax | Source |
|---|---|---|---|---|---|
| **UBA CI** (Entreprises, 2026) | **From 1.5% excl. tax, minimum 25,000 FCFA** (EUR and other currencies), plus correspondent fees | "Selon le cours appliqué" (FX margin in the rate) | Dossier 11,500 + SWIFT 15,000 + "Finex" 10,500 FCFA | TTHU 0.6% + TOB 10% on the commission | https://www.ubacotedivoire.com/wp-content/uploads/sites/12/2026/04/Conditions-tarifaires-Entreprises-UBA-CI-2026.pdf |
| **SIB CI** (2 Aug 2025) | "Commission fixe de transfert": **Entreprises 1.5%; SME segment (PACTE) 2% up to 20M, 1.8% above**; another line 1.3–1.8% | Euro: none; **outside euro: "frais de change 2%"**; elsewhere "voir barème, min 10,000" | SWIFT 10,000; correspondent **15,000 (≤3.3M) to 56,500 FCFA (≥590M)**; Finex 10,000 | TTHU 0.6% | https://sib.ci/wp-content/uploads/2025/07/TARIFS-DES-PRODUITS-ET-SERVICES-OFFERTS-A-LA-CLIENTELE%E2%80%A2-2-Aout.pdf |
| **SG Sénégal** (Entreprises, 2nd half 2026) | **0.85% (minimum 20,000 FCFA)** outside UEMOA | **0.25% (minimum 10,000)** outside euro | Dossier 30,000 + telecom 12,000 FCFA | "Taxe Etat" 0.6% | Search extract (PDF bot-blocked): https://societegenerale.sn/fileadmin/user_upload/SG_Senegal/PDF/SGSN_CONDITION_TARIFAIRE__2Semestre_2026_CLICOM.pdf |
| SG Sénégal (Entreprises, 2025) | 0.325% to euro zone | 0.25% (minimum 10,000) | Dossier 10,000 + telecom 12,000 | 0.6% | Search extract: https://societegenerale.sn/fileadmin/user_upload/senegal/PDF/SG_SN_CONDITION_TARIFAIRE_2025_CLICOM.pdf |
| BOA Sénégal (individuals, 2024) | 0.3% (minimum 15,000) above 100k FCFA | — | SWIFT 12,000 | — | Search extract: https://www.boasenegal.com/wp-content/uploads/2024/04/Conditions-tarifaires-2024_Particuliers.pdf |
| Versus Bank CI (undated) | **2%** | **1%** | SWIFT/telex 10,000 | 0.6% | Search extract: https://versusbank.ci/nos-produits/professionnels/conditions-tarifaires-appliquees-aux-entreprises/ |

**BCEAO FX fixing (15 Oct 2026):** USD 581.25 / 588.25 (≈ **±0.6%** around mid); CNY 86.50 / 88.25 (≈ **±1.0%**); AED 157.75 / 160.75 (≈ **±0.95%**); TRY not listed; EUR fixed at 655.957. https://www.bceao.int/fr. Commercial banks add their own margin on top.

**Worked example (our arithmetic):** an SME pays $20,000 (≈11.7M FCFA) to China via UBA CI.
- Commission 1.5% = 175k
- TTHU 0.6% = 70k
- Fixed fees ≈ 37k
- FX margin ≥ 1% ≈ 117k
- **All-in ≈ 3.4%**, before correspondent fees.

Via SG Sénégal: 0.85% + 0.25% + 0.6% + 42k fixed ≈ 2.0% plus FX margin.

Anecdotal evidence: a €3,000 (≈1.97M FCFA) bank transfer from Senegal reportedly carried about 400,000 FCFA in fees (>20%) and took about a week. This is a small-ticket, single-source anecdote. https://www.dakaractu.com/Commerce-les-portefeuilles-electroniques-chinois-numerisent-l-informel-africain_a276801.html (7 Oct 2026)

### 4.3 Alternatives and their pricing

| Provider / channel | What it does | Price | Source (date) |
|---|---|---|---|
| Informal sourcing agents (FCFA → CNY/Alipay) | Pay agent locally (Wave/OM), agent pays supplier in China | **3–8%** of amount (includes FX risk and logistics) | https://momocalc.com/fr/china (2026, undated page) |
| Informal FCFA → Alipay intermediaries (Senegal) | Bypasses banks; a BCEAO "grey zone" | % **not found** | Dakaractu / Impact.sn (7 Oct 2026) |
| WorldFirst (Ant Group) | Multi-currency account, pays Chinese suppliers in CNY | FX margin **0.3–1.5%** plus a small fixed fee; <1.5% above $5k | momocalc (2026) |
| Alibaba RMB Pay via foreign card | Card payment | FX surcharge **3–4%** plus fees | momocalc (2026) |
| Verto (B2B FX, UAE/UK; covers West Africa and China corridors) | B2B payments | Markup "**as low as 0.4%**" (vendor claim); third party: spread 0.6–1.2%, total 0.75–1.5% on a $10k ZA→NG payment | https://verto.co/ (2026); https://technext24.com/fintech/verto-cross-border-b2b-payments-africa/ |
| Cedar Money | B2B Africa↔world (incl. Côte d'Ivoire) | No subscription; fee embedded in FX; % **not published** | https://www.cedar.money/ (2026) |
| Thunes | Wholesale payout network (130+ countries). UnionPay direct-to-card into mainland China (Jan 2026) | **Not published** (B2B contracts) | https://www.thunes.com/news/thunes-and-unionpay-international-launch-instant-money-transfers-to-chinas-mainland/ (Jan 2026) |
| Onafriq (ex-MFS Africa) | Intra-Africa wallet/bank interoperability; no China route found | **Not published** | https://eversend.co/best/payment-infrastructure-providers-africa (2026) |
| Hub2 × Ecobank | Wallet↔bank settlement across 32 markets | **Not published** | Financial Afrik (25 Feb 2026) |
| Ecobank × CIPS | Direct yuan settlement for corporate clients, targeted end-2026 | **Not published** | GlobeNewswire (12 Oct 2026) |
| Flutterwave Send, Nium, Ecobank Rapidtransfer, Cauri Money | Mostly consumer remittances / inbound | **Not found** for B2B outbound from XOF. Cauri claimed "no fees up to €10k/month" (2024, promotional, inbound). | https://www.wearetech.africa/fr/fils/solutions/cauri-money-une-neobanque-senegalaise-pour-les-expatries (2024) |
| Djamo planned cross-border offer | — | **Not found**. Djamo Business currently offers UEMOA transfers only. | https://www.djamo.com/ci/business/ (accessed 2026-10-16) |
| Vendor claim on bank cost | "Banks can charge up to 5–7%" | Unverified vendor claim | Search extract (cedar.money / verto blog) |

**What fintechs charge SMEs:** no WAEMU fintech publishes an outbound B2B FX price. Proxies are:
- Verto: 0.4–1.5%
- WorldFirst: 0.3–1.5% FX margin
- Informal agents: 3–8%

---

## 5. Partner SFD (microfinance): lending-as-a-service

| Item | Evidence | Source (date) |
|---|---|---|
| WAEMU fintech–SFD revenue-share or first-loss terms | **Not found**. Djamo went straight to its own microfinance licence (Sep 2025) with no documented SFD partner before it. Orange Bank Africa is itself a bank. Advans CI × MTN (savings for cocoa farmers) shows the partnership model, but no split was disclosed. | Ecofin (12 Sep 2025); https://blogs.worldbank.org/fr/nasikiliza/les-producteurs-ivoiriens-de-cacao-adoptent-des-services-financiers-numeriques |
| Risk-sharing in WAEMU digital lending | IFC × Orange Bank Africa: IFC guarantees **50%** of an eligible short-term MSME loan portfolio (up to $30M) | https://ifc.org/en/pressroom/2023/ifc-partners-with-orange-bank-africa-to-increase-digital-lending-for-small-businesses-in-west-africa (Jul 2023) |
| PROXY: first loss, Kenya | IFC Catalytic First Loss Guarantee (Aug 2026): $24.2M of first-loss cover for ~$144M of lending. 4G Capital: first-loss tranche ~$2.2M on a ~$44.4M portfolio = **~5%** (our arithmetic) | https://www.ifc.org/en/pressroom/2026/ifc-supports-expansion-of-financing-for-kenya-s-small-businesses-through-the-first (4 Aug 2026); https://www.businessdailyafrica.com/bd/corporate/companies/ifc-in-sh803m-loan-guarantee-deal-with-kenyan-lender-4g-5474084 |
| PROXY: platform–bank lending | JUMO: bank is the balance-sheet provider; JUMO claims cost of risk <4%; split undisclosed | https://storage.mfn.se/79ea0db5-bc3d-406d-b062-460103cb98a3/vef-portfolio-company-jumo-announces-usd-120m-financing-round-led-by-fidelity-visa-and-kingsway.pdf |
| PROXY: revenue split | Vast/USBC: 60/40 → 50/50 of net deposit revenue (deposits, not loans) | SEC 8-K (20 Jan 2026) |
| Pricing headroom | SFD usury ceiling **24%** vs bank 14% (from 1 Jun 2026); average bank lending rate 6.7% | BCEAO Decision 19 (29 Dec 2025); RPM juin 2026 |
| Constraint (older) | MFI revenue from non-savings/credit services may not exceed **5% of total revenue**. Check the current text. | https://www.cgap.org/sites/default/files/Working-Paper-Market-Stystem-Assessment-of-Digital-Financial-Services-in-WAEMU_0.pdf (older) |
| Market size (CI) | 45 licensed SFDs, 2.57M clients (31 Dec 2025). BCEAO: SFDs on instant payments by 30 Jun 2027. | https://fr.allafrica.com/stories/202607160323.html (Jul 2026) |
| SFD integration / running fees | **Not found** | — |

---

## 6. Model inputs check

| Model input | Current value | Evidence (best available) | Recommended low / **base** / high | Reasoning |
|---|---|---|---|---|
| Partner bank fee per business account | 3,000 FCFA/month | WAEMU: **not found**. Benchmark: UBA CI charges SMEs ≥5,000 FCFA/month (account maintenance / minimum debit commission), 2026. US: per-account fees not standardised. | 1,500 / **2,500** / 5,000 FCFA | A wholesale fee should sit well below the bank's retail floor (~5,000), especially if the bank also keeps most of the balance income. 3,000 is defensible as a cautious figure. Base 2,500 assumes a volume tier after Year 1. Model 3,000 for Year 1 and 2,000–2,500 after 5,000 accounts if tiers are negotiated. |
| Partner bank set-up (per country) | 15M FCFA one-off, SN and CI each | WAEMU: **not found**. US: $0–100k+ (0–58M FCFA), often waived when the bank wants deposits (Jul 2026). | 5M / **15M** / 30M FCFA | 15M (~€23k) is mid-range. Banks hungry for SME deposits in a falling-rate market may waive it. Bespoke IBAN/API work at a less digital bank could double it. Keep 15M and add 5–10M of internal integration cost (compliance audit, KYC flows). |
| Platform minimum | 1.5M FCFA/month | WAEMU: **not found**. US: $5k–50k/month (≈2.9–29M FCFA). | 0.75M / **1.5M** / 3M FCFA | WAEMU price levels and bank cost bases are lower than in the US. 1.5M (~$2.6k) is plausible. The high case matches the US floor. Usually creditable against per-account fees, so model it as max(minimum, fees). |
| Share of bank income on balances paid to Kelen | 1.5%/yr (scen. 1 / 1.5 / 2%) | WAEMU: **not found**. Interbank 4.52% (Q1 2026, falling); policy rate 3%; reserve 3%. 1.5% ≈ 34% of the bank's interbank yield. Proxy Vast/USBC: 40%→50% *net of costs*, with a floor. | **0.75% / 1.25% / 2.0%** | 1.5% is achievable at today's rates but sits in the upper half once costs, the bank's liquidity buffers and possible further cuts are counted. Use 1.25% base. Better: model it as **30% (low 20%, high 45%) of the BCEAO interbank or policy reference rate**, so it moves with rates. Keep 2.0% only as an upside case for large, sticky balances or a Year-3 step-up. |
| International payments: cost to Kelen | 0.5% of amount | Banks' public SME prices: 0.85–2.0% commission + 0.6% tax + 25–60k FCFA fixed + FX margin (BCEAO spread alone ±0.6% USD, ±1.0% CNY/AED). Wholesale FX fintechs: 0.4–1.5%. | EUR: 0.3% / **0.5%** / 0.8%. USD/CNY/AED/TRY: 0.8% / **1.2%** / 1.8%. **Plus 0.6% TTHU passed through and ~15–25k FCFA fixed per transfer.** | 0.5% holds only for EUR (pegged, no FX risk) at negotiated wholesale bank pricing. China, UAE and Turkey flows need USD/CNY conversion: the BCEAO half-spread alone is 0.6–1.0%. A blended base of ~1.0% (assuming ~30% EUR / 70% other) is more realistic. The 0.6% tax must be modelled as a pass-through, not absorbed. |
| International payments: Kelen price | 1.5% | Banks charge an SME an all-in ~2–3.5% (worked examples); informal 3–8%. | 1.2% / **1.5%** + tax + fixed fee / 2.0% | 1.5% is competitive *if* the 0.6% tax and a fixed fee (~10–15k FCFA) are charged on top. Blended net margin ≈ 0.5% (base), not 1.0%. Consider 1.0% for EUR and 1.75–2.0% for CNY/AED/TRY. |
| Partner SFD: Kelen share of net credit margin | 50% | WAEMU: **not found**. Proxy splits 40–50% (Vast/USBC). SFD usury ceiling 24% leaves a gross margin. | 35% / **45%** / 55% | Kelen brings origination, scoring and servicing; the SFD brings licence, funding and regulatory capital. A 50/50 split is market-like only if Kelen also carries first loss. Use 45% base to reflect funding cost and SFD overhead. Watch the possible cap on SFD non-credit revenue when structuring Kelen's fees. |
| Partner SFD: first-loss reserve | 10% | Proxy: IFC/4G ~5% first-loss tranche (Kenya, 2026). IFC–OBA 50% pari-passu guarantee (2023). JUMO cost of risk <4% (company claim). | 5% / **10%** / 15% | 10% is prudent for unproven SME credit in a new market. It can step down to 5–7% after 12–18 months of data. Model it as a cash reserve (working capital), released on performance. |
| SFD integration (one-off) | 5M FCFA | **Not found** | 3M / **5M** / 10M | SFD core systems are often less API-ready (CI SFDs only join instant payments by June 2027). The high case covers custom work. |
| SFD running fees | 3M FCFA/yr | **Not found** | 2M / **3M** / 6M | Reasonable for a small SFD. The high case adds audit, reporting and compliance support. |

### Gaps to close in partner discussions (questions for banks and SFDs)
1. Will the bank pay a balance commission as a % of a reference rate (BCEAO policy rate, interbank or TMM), with a floor? Will it carve out term-deposit balances?
2. Are the per-account fee and the platform minimum creditable against each other? Are there volume tiers?
3. Wholesale outbound FX pricing: commission, FX margin vs the BCEAO fixing, SWIFT and correspondent fees, and who handles domiciliation files above 20M FCFA.
4. Whether Ecobank's CIPS yuan product (end-2026) can be white-labelled for Kelen's China flows.
5. SFD: who funds the loan book, who bears losses beyond the first-loss reserve, and how the usury ceiling (24%, effective rate including fees) applies to Kelen's fees.
