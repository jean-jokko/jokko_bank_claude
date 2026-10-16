# F — Card programme costs and deals in the WAEMU (research for Kelen)

Research date: 2026-10-16. Every figure has a source and a date. "Not found" means no public figure was found, not that the cost is zero. **PROXY** marks figures from markets outside the WAEMU (Nigeria, US, EU, Zambia, Uganda) or from consumer products. These show orders of magnitude, not WAEMU prices.

FX conventions: EUR/XOF is fixed at 655.957. USD conversions below use an **illustrative 580 FCFA per USD**, which is my assumption and should be checked against the current rate. NGN conversions are approximate and marked "~".

---

## 0. Key findings (read first)

1. **Processor pricing is not public.** Paymentology, Marqeta, Nium, HPS, Visa DPS and GIM-UEMOA all price by quote. The only public issuing rate card in Africa is Sudo (Nigeria): ₦50,000/month access, ₦50 per virtual card, ₦5 per authorisation, ₦50 quarterly maintenance. It is a weak proxy for a Visa/Mastercard business programme in the WAEMU.
2. **The current FX pricing (1% client fee, 0.5% cost) is out of line with the market.** WAEMU issuers charge clients **2–4%** on non-WAEMU spending: Djamo SN 200 F + 3–4% (EUR), NSIA CI 2.5% (minimum 2,500 F), UBA CI 2.5%, Coris SN 2% + 500 F, BICICI 2%, UBA CI enterprise web 3%. Network cross-border assessments alone are about **0.9–1% plus per-transaction fees** (US-issuer proxy). A 0.5% cost assumption is probably too low.
3. **Kelen will likely earn interchange on cross-border spending, and the model ignores it.** When a Visa commercial card is used at a US merchant (Meta, Google, AWS and so on), the **issuer interchange is 2.00%** (Visa USA IRF, effective 18 Apr 2026). For consumer Classic cards it is 1.10%. How much reaches Kelen depends on the sponsor contract.
4. **Domestic FCFA interchange is small and uncertain.** The only official split found (BCEAO, GIM-UEMOA domestic merchant commission) gives **20% to the issuer**, 30% to the acquirer and 50% to GIM. Merchant commissions are about 2% for GIM cards and 3–3.5% for Visa/MC (UBA CI 2026). That gives the issuing bank roughly 0.4–0.7% before any revenue share to Kelen. GIM-UEMOA **Decision n°31** (domestic routing and clearing of Visa/MC transactions through GIM-Switch, deadline 31 Mar 2026, Visa said compliance was "a few months" away in July 2026) may change domestic economics again.
5. **There is a regulatory risk to the B2B cross-border use case.** **Règlement 06/2024/CM/UEMOA** (signed Dec 2024; implementing instructions July 2025) has two relevant articles. **Art. 47** restricts a resident's card use abroad to "frais de voyage usuels et personnels". **Art. 12** (annex) requires authorised intermediaries to ensure that cards are used in line with the import-of-goods-and-services settlement rules. Financial Afrik (24 Mar 2026) reads this as "l'utilisation des cartes classiques ou prépayées pour payer des marchandises est strictement interdite". SME card spend on foreign SaaS or ads therefore needs a compliance design agreed with the sponsor bank and the BCEAO, such as import-of-services documentation or caps.
6. **The deals are bank-sponsored.** Wave's virtual Visa is issued by **Ecobank Sénégal** under its BIN and regulatory responsibility (Wave terms). Djamo CI is issued by **BGFIBank CI or Ecobank CI**. Mixx by Yas Mastercard runs with Ecobank. The Flash (NAT) Mastercard prepaid card was announced Nov 2024. Orange Money CI's virtual Visa (Dec 2025) runs with Orange Bank. **No revenue-share or fee terms of any of these deals are public.**

---

## 1. Card issuing processors active in (or relevant to) Francophone West Africa

| Processor | WAEMU presence / role | Published pricing | Source (date) |
|---|---|---|---|
| **GIM-UEMOA** (GIM-Switch, GIM-Délégataire, GIM-Prepaid) | Regional interbank switch, created 2003 and operational 15 Jun 2007. Majority BCEAO-owned since Dec 2009. Offers issuer processing by delegation, card personalisation, and GIM-Prepaid (pure GIM, GIM-Visa and GIM-Mastercard prepaid cards for banks, EMEs, SFDs and corporates). | **Not found** (no member fees, entry ticket or processing tariff published). Membership requires paying a "ticket d'entrée" set by the General Assembly. The only public figure is the **cardholder cap of 500 F CFA TTC** per interbank ATM withdrawal. | [BCEAO monétique interbancaire](https://www.bceao.int/fr/content/monetique-interbancaire-regionale); [GIM-Prepaid](https://www.gim-uemoa.org/index.php/fr/solutions-services/gim-prepaid); [GIM adhésion](https://www.gim-uemoa.org/fr/membres/adherer-au-gim-uemoa); [GIM-Switch](https://www.gim-uemoa.org/solutions-services/gim-switch) (pages accessed 2026-10-16) |
| GIM-UEMOA domestic commission split | Interbank merchant commission, domestic transactions (ACU model): **issuer 20% / acquirer (domiciliataire) 30% / GIM-UEMOA 50%** | Split only; the rate is not published | [BCEAO](https://www.bceao.int/fr/content/monetique-interbancaire-regionale) (accessed 2026-10-16) |
| **Paymentology** | Says it serves "Kenya, Ivory Coast and Senegal" and connects directly to GIM-UEMOA, Visa and Mastercard. Raised USD 175M in May 2026. | **Not found**; quote-based | [Paymentology Africa](https://www.paymentology.com/demo-africa) (accessed 2026-10-16); [BusinessWire 12 May 2026](https://www.businesswire.com/news/home/20260512676799/en/) |
| **HPS PowerCARD** | Present in 39 African markets including the WAEMU. Offers ASP (outsourced) processing. | **Not found** | [Jeune Afrique](https://www.jeuneafrique.com/mag/553204/economie-entreprises/monetique-hps-cherche-a-mieux-profiter-du-potentiel-africain/) (older article, undated in result) |
| Marqeta | Quote-based. Line items are implementation fee, monthly platform minimum, card creation, active-card fee, transaction processing, network costs and sponsor charges. | **Not found** | [Guideflow 2026](https://www.guideflow.com/blog/payment-card-issuance-software) |
| Nium | Quote-based. One-time issuing fee per card and declined-transaction fees mentioned, but no amounts. | **Not found** | [Aspire review 2026](https://aspireapp.com/blog/nium-global-card-review-singapore) |
| **Sudo Africa** (Nigeria) **PROXY** | API card issuing (Verve, Visa, Mastercard) | **Monthly access ₦50,000** (~USD 30–35); **virtual card ₦50**; **authorisation ₦5**; **quarterly maintenance ₦50**; dispute ₦100; ATM ₦35; funding free; physical card "contact sales" (founder quote, 2021: physical cards "as low as ₦1,000") | [sudo.africa/pricing](https://sudo.africa/pricing) (accessed 2026-10-16); [BusinessDay ~2021](https://businessday.ng/technology/article/sudo-africa-is-helping-simplify-debit-card-issuing-for-businesses/) |
| **Union54** (Zambia) **PROXY** | Pay-as-you-go per API call. Physical card **USD 7–9 flat**. Suspended in Oct 2022 after paying ~**USD 0.5M in declined-transaction fees** to keep its Mastercard licence. | 2021–2023 reporting | [TechCrunch 6 Aug 2021](https://techcrunch.com/2021/08/06/the-first-zambian-startup-to-get-into-yc-is-developing-africas-first-card-issuing-api/); [Semafor 18 May 2023](https://www.semafor.com/article/05/18/2023/mastercard-visa-tighten-rules-of-african-dollar-cards) |
| Interswitch / Verve, Bankly | Nigerian local scheme and processor; Verve now accepted on GIM-UEMOA (Apr 2025) | **Not found** | [ThisDay 25 Apr 2025](https://www.thisdaylive.com/2025/04/25/verve-gim-uemoa-partner-to-boost-seamless-payments-across-west-africa/) |
| Visa DPS / Mastercard processing | Scheme processing | **Not found** | — |
| Processors behind Djamo, Wave, Mixx, Flash | Not disclosed. Wave and Mixx are issued by Ecobank (see §2). | **Not found** | — |
| Scheme-membership costs in Nigeria **PROXY** | For international schemes: "**$2,000 monthly implementation charge**, opening an offshore account, renewing their contracts annually, and **collateral that runs into millions of dollars**" (three sources familiar with card operations) | Reported | [TechCabal 26 Jun 2024](https://techcabal.com/2024/06/26/nigerian-fintechs-dump-visa-and-mastercard/) |
| Stripe Issuing (US) **PROXY** | Public rate card | **USD 0.10 per virtual card; USD 3.50 per standard physical card (shipping excluded)**; cross-border "1% + 30¢", +1% if currency conversion; USD 15 per dispute (as extracted from the pricing page) | [stripe.com/pricing](https://stripe.com/pricing) (accessed 2026-10-16) |
| Swan (EU BaaS) **PROXY, unverified** | €0.10 per issued card; plans "from €2,990/month" (aggregator) | Third-party | [Lago template](https://getlago.com/resources/templates/swan); [fitgap](https://us.fitgap.com/products/swan) |

### 1b. Scheme pass-through fees borne by an issuer (US-issuer PROXY, Mastercard)

Synctera's Mastercard pass-through schedule (accessed 2026-10-16, [docs.synctera.com](https://docs.synctera.com/docs/mastercard-passthrough-fees)):

| Fee | Amount |
|---|---|
| **Issuer cross-border** | **0.9% of volume** |
| International authorisation (issuer) | **USD 0.30 per transaction** |
| International clearing (issuer) | **USD 0.125 per transaction** |
| Domestic authorisation | USD 0.0065–0.011 per transaction |
| Domestic clearing | USD 0.01–0.02 per transaction |
| Assessment (purchase volume) | 0.025–0.065% |
| CNP security resiliency | 0.015% (≥ USD 50) / USD 0.0075 (< USD 50) |
| MasterCom claim | USD 1.35–3.05 per claim + USD 0.50 per resolved claim |
| Tokenisation (MDES) | listed as a category, **amount not found** |

These figures imply that a cross-border transaction costs the issuer about **0.9% + about USD 0.43 in fixed fees**, before any FX spread. On a USD 20 SaaS charge, the fixed fees alone are about 2.1%. WAEMU issuer fees are **not found** and may differ.

---

## 2. BIN sponsorship and card programme deals (WAEMU)

| Programme | Sponsor / issuer | Scheme | Date | Known terms | Source |
|---|---|---|---|---|---|
| **Wave virtual Visa (Senegal)** | **Ecobank Sénégal** is the issuer: the card is issued "sous la responsabilité réglementaire et le BIN de la banque émettrice" | Visa | Launched 23 Jan 2026, after pilots in CI and SN | Cardholder: **no issuance, management or transaction fees** (§8.1). Limits 1M FCFA per transaction, 10M FCFA per month. No FX clause in the terms. **Revenue share between Wave and Ecobank not found.** | [Wave CGU](https://www.wave.com/fr/terms_vv_sn_ecobank/) (undated, accessed 2026-10-16); [Socialnetlink 23 Jan 2026](https://www.socialnetlink.org/2026/01/23/wave-en-partenariat-avec-visa-et-ecobank-lance-une-carte-virtuelle-pour-accelerer-linclusion-financiere-en-afrique/) |
| **Djamo CI** | **BGFIBank Côte d'Ivoire or Ecobank Côte d'Ivoire** (co-branded) | Visa | Visa–Djamo strategic partnership 24 Mar 2025 (CI, SN, then a third WAEMU country) | Terms not public | [Djamo carte Visa](https://www.djamo.com/fr-ci/carte-visa); [Sikafinance Mar 2025](https://www.sikafinance.com/marches/visa-et-djamo-unissent-leurs-forces-pour-stimuler-l-innovation-financiere-en-afrique-de-l-ouest_51786) |
| **Djamo SN** | "Une Banque agréée" (unnamed in CGU, Feb 2025; Ecobank logo on the page) | Visa | CGU from 20 Feb 2025 | Cardholder: virtual card 0 F; **physical card 2,000 F; delivery 0 F**; Premium 2,000 F/month | [Djamo SN CGU](https://www.djamo.com/fr-sn/conditions-generales-et-tarifaires/djamo-sn) |
| **Mixx by Yas Mastercard (Senegal)** | Ecobank ("acceptation mondiale", ATM, replacement) | Mastercard | ~Apr 2025 | No top-up fees; free withdrawals on the Ecobank network; 2M F per transaction, 10M F per month. Deal terms not public. | [Yas SN](https://yas.sn/mixx-by-yas/); [Le Marché finance](https://lemarche.finance/mixx-bye-yas-mastercard-et-ecobank-lancent-mixx-mastercard-pour-accelerer-linclusion-financiere/); [X post Apr 2025](https://x.com/YasSenegal/status/1907730354288427478) |
| **Flash (New Africa Technology)** | Not disclosed | Mastercard (virtual and physical prepaid; "Flash in Business") | Announced 20 Nov 2024 (SN, CI, BJ) | Not public | [Mastercard newsroom Nov 2024](https://newsroom.mastercard.com/news/eemea/en/newsroom/press-releases/en/2024/november/mastercard-collaborates-with-new-africa-technology-to-launch-fintech-card-in-senegal-cote-d-ivoire-and-benin/) |
| **Orange Money virtual Visa (CI)** | Orange Bank (partner; legal issuer not explicit) | Visa | Dec 2025 | Advertised as zero activation, management and top-up fees; 2M F/day, 10M F/month. The Orange CI grid shows 1% on withdrawals (conflict). | [Ecofin 15 Dec 2025](https://www.ecofinagency.com/news/1512-51403-orange-money-launches-fee-free-virtual-visa-card-in-cote-d-ivoire) |
| **Visa Fintech Fast Track (CEMEA)** | Links fintechs to sponsor banks and certified processors (GTP for SSA: BIN sponsorship, issuer processing, programme management) | Visa | Launched Feb 2019 | "Reduced fees", onboarding "in as little as four weeks". Requirements: licence, clean background checks, **≥ 12 months of working capital**. **No fee figures published.** | [Capital FM Sep 2019](https://www.capitalfm.co.ke/business/2019/09/visa-takes-fintech-fast-track-program-to-africa-middle-east/); [NextBillion 2019](https://nextbillion.net/news/visa-launches-fintech-fast-track-program-in-africa-and-other-regions) |
| **Mastercard Start Path** | Accelerator | Mastercard | — | Not a fee-paying programme for startups: at the 2015 launch, "no equity taken up front (but an option to participate in your next round)". The **USD 800/month** figure found online is the fee *banks* pay for Start Path database access, not a startup fee. | [BetaKit 2015](https://betakit.com/mastercard-invites-applications-for-start-path-global-partnership-program/); [Mastercard Services](https://www.mastercardservices.com/es/node/8571) |
| Collateral / security deposits | — | — | — | **WAEMU figures not found.** Nigeria: "collateral that runs into millions of dollars" for scheme membership (TechCabal 26 Jun 2024). A vendor blog claims BIN-sponsor collateral "can exceed USD 500,000" (unverified). For prepaid, the sponsor usually requires prefunding of balances. | [TechCabal 2024](https://techcabal.com/2024/06/26/nigerian-fintechs-dump-visa-and-mastercard/); [sdk.finance](https://sdk.finance/blog/bin-sponsorship-a-key-to-unlocking-card-issuance-in-fintech/) |

---

## 3. Scheme fees, FX fees and FX rules

### 3a. Network cross-border fees

| Item | Figure | Status | Source (date) |
|---|---|---|---|
| Visa International Service Assessment (merchant/acquirer side, US) | 0.80% (2008) → **1.00%** base (Apr 2019); 1.40% if settled in non-USD | Secondary | [CardFellow](https://www.cardfellow.com/blog/international-service-assessment); [Woodforest schedule Oct 2022](https://woodforest.com/media/bsubodo1/capstar.pdf) |
| Mastercard cross-border (acquirer side, US) | 0.60% USD-settled / 1.00% non-USD | Secondary | [CardFellow](https://www.cardfellow.com/blog/mastercard-cross-border-fee) |
| Mastercard **issuer** cross-border (US issuer) | **0.9% of volume** + USD 0.30 international authorisation + USD 0.125 international clearing per transaction | **PROXY** | [Synctera](https://docs.synctera.com/docs/mastercard-passthrough-fees) |
| Network share of a 3% consumer foreign transaction fee (US) | "Visa and Mastercard both charge a fee of **1%**", and the issuer adds about 2% | **PROXY** (older Bankrate data) | [Bankrate](https://www.bankrate.com/credit-cards/travel/a-guide-to-foreign-transaction-fees) |
| Network cross-border fees for WAEMU issuers | **Not found** | — | — |

### 3b. What WAEMU issuers charge clients for non-WAEMU card spending

| Issuer / product | Payment outside WAEMU | Source (date) |
|---|---|---|
| Djamo SN virtual card | **200 F + 4%** (EUR); 200 F + FX fees (other currencies) | [Djamo SN CGU, Annexe 4, Feb 2025](https://www.djamo.com/fr-sn/conditions-generales-et-tarifaires/djamo-sn) |
| Djamo SN physical (Free / Premium) | **200 F + 3%** (EUR); 200 F + FX fees (others) | same |
| Djamo CI / SN tariff pages | "200 F + taux de change Visa" (no % shown) | [djamo.com/fr-ci/tarifs](https://www.djamo.com/fr-ci/tarifs); [djamo.com/sn/tarifs](https://www.djamo.com/sn/tarifs/) (accessed 2026-10-16) |
| Djamo (June 2026) | Card top-ups now charged: local card 1.5%, international card 2.5% (search snippet of the Djamo page; not re-verified) | Djamo tarifs (2026) |
| Wave virtual Visa SN | **0 F** transaction fee per the CGU; FX margin not disclosed (third-party claim of 0.5–2.5% and 1.2–1.5% unverified) | [Wave CGU](https://www.wave.com/fr/terms_vv_sn_ecobank/); [Kolonell 2026](https://kolonell.com/fr/blog/carte-prepayee-senegal-comparatif-2026) |
| NSIA Banque CI | **2.5% TTC, minimum 2,500 F** (payment); ATM 2.2% minimum 2,500 F | [NSIA CB Feb 2026](https://www.nsiabanque.ci/wp-content/uploads/2026/02/CONDITIONS-DE-BANQUE-CLIENTELES-DES-PARTICULIERS.pdf) |
| UBA CI prepaid | **2.5%, minimum 650 F** (TPE and internet outside WAEMU); ATM 2.5% minimum 3,500 F | [UBA CI particuliers 2026](https://www.ubacotedivoire.com/wp-content/uploads/sites/12/2026/04/Conditions-tarifaires-Particuliers-UBA-CI-2026.pdf) |
| UBA CI enterprise | TPE-web international **3%** | [UBA CI entreprises 2026](https://www.ubacotedivoire.com/wp-content/uploads/sites/12/2026/04/Conditions-tarifaires-Entreprises-UBA-CI-2026.pdf) |
| BICICI CI (PME) | **2%, minimum 182 F** (TPE outside WAEMU) | [BICICI PME Jan 2026](https://bicici.ci/documents/d/website-bicici/01-bicici-conditions_pme_janvier-2026-091226-1) |
| Coris Bank SN | **2% + 500 F** | [Coris SN Jul 2025](https://senegal.coris.bank/wp-content/uploads/2025/07/Conditions-Generales-A4.pdf) |
| CBAO SN | **855 F + 0.5% HT** (TPE and internet outside WAEMU); ATM 2,564 F + 1.3% | [CBAO CB 1 Sep 2025](https://cbaobank.com/sites/default/files/Conditions%20de%20banque_2025_0.pdf) |
| Eversend (Uganda) **PROXY** | **3.5% + USD 0.50** (non-USD) | [Eversend help](https://help.eversend.co/en/articles/15931555-virtual-card-fees-and-minimum-amounts) |

The market range is **2–4% plus a fixed fee**. CBAO, at 0.5% + 855 F, is the low outlier.

### 3c. BCEAO / UEMOA foreign-exchange rules affecting cards

Source: **Règlement n°06/2024/CM/UEMOA** relating to external financial relations (Comité des Experts opinion 13 Dec 2024; in force on signature). Text from the PDF ([labase-lextenso](https://www.labase-lextenso.fr/sites/lextenso/files/lextenso_upload/l_regl._ndeg_062024cmuemoa.pdf); [BCEAO page](https://www.bceao.int/fr/reglementations/reglement-ndeg062024cmuemoa-relatif-aux-relations-financieres-exterieures-des-etats)):
- **Annex, Art. 12 (last paragraph):** "Les intermédiaires agréés s'assurent, par tous moyens appropriés, que les cartes de retrait et de paiement classiques ou prépayées mises à la disposition de leur clientèle sont utilisées dans le strict respect des règles et procédures régissant le règlement d'importations de biens et de services".
- **Annex, Art. 47:** "L'utilisation, par un résident, à l'étranger ou au profit d'un non-résident de cartes de retrait et de paiement prépayées et/ou classiques … est strictement réservée aux règlements des frais de voyage usuels et personnels visés à l'article 45". Issuers must ensure their clients comply.
- Financial Afrik (24 Mar 2026): implementing instructions were published in July 2025, and "l'utilisation des cartes classiques ou prépayées pour payer des marchandises est strictement interdite". Breaches can lead to "retrait d'agrément". [Financial Afrik](https://www.financialafrik.com/2026/03/24/reglement-06-2024-uemoa-ce-qui-change-vraiment-pour-les-banques-et-les-entreprises/)
- **What this means for Kelen:** foreign-currency spending on a business card (SaaS, ads, supplies) counts as an *import of services or goods*. Card use for goods is described as prohibited, and services need import-settlement compliance. The cross-border revenue line has to be validated with the sponsor bank's compliance team. Possible design responses are per-client caps, merchant-category whitelists, and supporting-document capture.

### 3d. GIM-UEMOA Decision n°31 (domestic routing)

- Adopted 2015. It requires any transaction on a WAEMU-issued card, even on Visa or Mastercard rails, to be routed and cleared through GIM-Switch in local currency. The compliance deadline for Visa, Mastercard and UnionPay was **31 Mar 2026** ([Financial Afrik 29 Jan 2026](https://www.financialafrik.com/2026/01/29/uemoa-les-cartes-visa-et-mastercard-ont-90-jours-pour-se-conformer/)). From 2 Jan 2026 some e-commerce sites, such as Air Côte d'Ivoire, suspended local-card payments ([barid.tv 16 Jan 2026](https://barid.tv/2026/01/16/uemoa-le-bras-de-fer-des-paiements-en-ligne-gim-switch-defie-visa-et-mastercard/)). Eight banks passed pilot tests on 7 May 2026 ([Financial Afrik 11 May 2026](https://www.financialafrik.com/2026/05/11/mise-en-conformite-a-la-decision-n31-huit-banques-de-luemoa-reussissent-les-premieres-operations-e-commerce-regionales/)). Visa said in July 2026 it was "only a matter of a few months" from full compliance ([Ecofin 3 Jul 2026](https://www.ecofinagency.com/news/0307-57043-interview-visa-s-aminata-kane-on-mobile-money-payment-sovereignty-and-gim-uemoa-s-decision-31)). **Status at Oct 2026: not confirmed.** No fee or interchange figures were found.

---

## 4. Interchange and merchant discount rates

| Item | Figure | Source (date) |
|---|---|---|
| GIM-UEMOA domestic merchant commission split | Issuer **20%**, acquirer 30%, GIM 50% | [BCEAO](https://www.bceao.int/fr/content/monetique-interbancaire-regionale) |
| GIM-UEMOA domestic interchange rate (%) | **Not found** | — |
| Visa/MC intra-WAEMU / CEMEA intra-regional interchange | **Not found** (no public CEMEA or WAEMU schedule) | — |
| Visa UAE domestic debit consumer (general) | 1.00% (May 2022) | **PROXY** [Visa UAE IRF](https://ae.visamiddleeast.com/dam/VCOM/regional/cemea/unitedarabemirates/home-page/support-consumer/Visa-United-Arab-Emirates-interchange-reimbursement-fees.pdf) |
| **Visa interregional interchange: foreign card at a US merchant** (what a WAEMU issuer would receive) | Classic/Gold/Electron **1.10%** base (1.60% alternative); Signature/Premium 1.85%; Infinite 1.98%; **All Visa Commercial 2.00%**; B2B Virtual Payments (commercial) 2.00% | [Visa USA IRF, rates effective 18 Apr 2026](https://usa.visa.com/content/dam/VCOM/download/merchants/visa-usa-interchange-reimbursement-fees.pdf) |
| **Merchant discount rates (MDR), acquirer side** | UBA CI: **GIM-UEMOA cards 2%**, **Visa/Mastercard 3–3.5%**; TPE rental 20,000 F/month | [UBA CI entreprises 2026](https://www.ubacotedivoire.com/wp-content/uploads/sites/12/2026/04/Conditions-tarifaires-Entreprises-UBA-CI-2026.pdf) |
| MDR, Société Générale Sénégal | 2.75% plus a monthly TPE fee (search snippet of the SG SN 2025 tariff; the PDF did not download) | [SG SN 2025](https://societegenerale.sn/fileadmin/user_upload/SG_Senegal/PDF/Dossier_SG_SN_CONDITION_TARIFAIRE_2025_CLIPRI_.pdf.pdf) |
| BICICI TPE rental | 15,000 F/month | [BICICI PME Jan 2026](https://bicici.ci/documents/d/website-bicici/01-bicici-conditions_pme_janvier-2026-091226-1) |
| Cardholder price for domestic / WAEMU payments | **Free** at every bank checked (UBA, BICICI, Coris, CBAO, Djamo) | Tariffs above |
| Market size, Senegal 2023 | 1.51M cards; **4,828 TPE**; card *payments* (including online) **558 bn FCFA** (12.4M transactions) vs withdrawals 2,345 bn | [BCEAO Tableau de bord monétique 2023 (Aug 2024)](https://www.bceao.int/sites/default/files/2024-11/Tableau_Bord_Monetique_2023.pdf) |
| Market size, Côte d'Ivoire 2023 | 3.10M cards; 7,556 TPE; payments 773 bn FCFA | same |

Implication: the issuing bank's domestic take is roughly 20% × 2–3.5% MDR ≈ **0.4–0.7%** (derived, not published). Kelen then receives a negotiated share of that. Domestic card acceptance is thin (4,828 terminals in Senegal), so FCFA card spend per SME card may be modest.

---

## 5. Physical card production and delivery

| Item | Figure | Status | Source (date) |
|---|---|---|---|
| Card manufacture, Nigeria (Sudo) | ₦600 (2020) → ₦800 (2021) → ₦1,200 → **up to ₦1,800 (~USD 1.70) per card**; about ₦1,900–2,200 per card over a 3-year lifecycle | **PROXY** | [Techpoint 17 Mar 2025](https://techpoint.africa/insight/contactless-card-issuing-cost-400/) |
| Stripe Issuing standard physical card | **USD 3.50** (shipping excluded) | **PROXY** (US) | [stripe.com/pricing](https://stripe.com/pricing) |
| Union54 physical card | **USD 7–9 flat** | **PROXY** (2021) | [TechCrunch Aug 2021](https://techcrunch.com/2021/08/06/the-first-zambian-startup-to-get-into-yc-is-developing-africas-first-card-issuing-api/) |
| Chip module example | USD 1.50 per chip (illustrative); ~10% price rise in 2026 (chip crunch) | Vendor blog | [ABCorp 2026](https://abcorp.com/card-resources/card-program-manage-emv-chip-shortage-2026/) |
| Personalisation, prepaid card (retail price) | UBA CI: **2,000 F TTC** personalisation + 9,000 F TTC issuance | WAEMU retail price | [UBA CI 2026](https://www.ubacotedivoire.com/wp-content/uploads/sites/12/2026/04/Conditions-tarifaires-Particuliers-UBA-CI-2026.pdf) |
| Prepaid card price (retail) | BICICI "Prix de la carte" **6,364 F** HT | WAEMU retail price | [BICICI Jan 2026](https://bicici.ci/documents/d/website-bicici/01-bicici-conditions_pme_janvier-2026-091226-1) |
| Business card annual fee (retail) | BICICI Carte Affaires / Visa Business **80,500 F/year** HT | WAEMU retail price | same |
| Fintech physical card (retail) | Djamo SN **2,000 F, delivery 0 F**; Wave physical card 2,500 F (third party) | WAEMU retail price | [Djamo CGU Feb 2025](https://www.djamo.com/fr-sn/conditions-generales-et-tarifaires/djamo-sn); [Kolonell 2026](https://kolonell.com/fr/blog/carte-prepayee-senegal-comparatif-2026) |
| Local personalisation bureau | ICS (Abidjan), certified by GIM-UEMOA, Visa, MC and CUP; GIM-UEMOA also offers personalisation. **Prices not found.** No Idemia or Thales bureau found in Dakar. | — | [ics.ci](https://ics.ci/personnalisation-de-cartes-bancaires/) |
| Delivery, Dakar (moto courier) | **1,000–3,000 F** per drop (Plateau 1,000–1,500; suburbs 2,000–2,500; Rufisque 2,500–3,000); Yango 1,200–2,800; La Poste 600–2,500 (3–7 days) | Blog, 2026 | [Kolonell 2026](https://kolonell.com/fr/blog/tarif-livraison-dakar-abidjan-grille-2026) |
| PIN mailer | **Not found** (digital PIN in-app is common: Djamo and NSIA activate in-app) | — | — |

---

## 6. Fraud and chargebacks

| Item | Figure | Status | Source (date) |
|---|---|---|---|
| EEA card fraud rate | **0.031% of value** (H1 2023); 71% of card-fraud value was cross-border | **PROXY** (EU, with strong customer authentication) | [ECB/EBA 1 Aug 2024](https://www.ecb.europa.eu/press/pr/date/2024/html/ecb.pr240801~f21cc4a009.en.html) |
| South Africa gross card fraud | R1.466 bn in 2024 (+26.2%); card-not-present is dominant (68% in 2023) | **PROXY** (no rate) | [SABRIC 2024](https://www.securitysa.com/25832R) |
| Union54 | ~USD 0.5M in declined-transaction fees triggered by chargeback fraud on USD virtual cards → suspension in 2022 | **PROXY** (event) | [Semafor May 2023](https://www.semafor.com/article/05/18/2023/mastercard-visa-tighten-rules-of-african-dollar-cards) |
| Chipper Cash | ₦500 penalty per declined transaction (Nigeria) | **PROXY** | same |
| Visa VAMP | Excessive-merchant threshold 150 bps from 1 Apr 2026 | Merchant-side | [Redo](https://redo.com/resources/articles/chargebacks/chargeback-statistics) |
| Dispute handling costs | MasterCom USD 1.35–3.05 per claim; Stripe USD 15 per dispute; Sudo ₦100 per dispute | **PROXY** | Synctera; Stripe; Sudo |
| WAEMU card fraud rate | **Not found** (BCEAO and GIM publish no fraud rate) | — | — |

---

## 7. Virtual card providers (consumer-facing prices, PROXY)

| Provider | Creation | Monthly | FX / other | Source (date) |
|---|---|---|---|---|
| Sudo (NG) | ₦50 | ₦50 per quarter | ₦5 per authorisation; ₦50,000/month platform access | [sudo.africa/pricing](https://sudo.africa/pricing) |
| Chipper Cash (USD card) | USD 5 (USD 3 per Raenest) | **USD 1/month "charged by our partner issuing bank"** | — | [Chipper support](https://support.chippercash.com/en/articles/10435074-understanding-your-usd-virtual-card-maintenance-fee); [Techeconomy Feb 2026](https://techeconomy.ng/cardtonic-vs-chipper-cash-virtual-usd-card-fees-fx-rates-compared/) |
| Eversend (UG) | USD 0 | USD 0.99–1/month or USD 2.99–3 one-time | **3.5% + USD 0.50** FX; USD 0.35–0.50 per declined payment | [Eversend help](https://help.eversend.co/en/articles/8185032-eversend-virtual-card-fees) |
| Afriex | **USD 5 one-time** | 0 | USD-denominated; FX % not found | [Afriex Oct 2025](https://www.afriex.com/post/introducing-afriex-virtual-usd-cards-pay-globally-for-just-5) |
| Flutterwave | Not published ("email for charges") | — | — | [Flutterwave docs](https://developer.flutterwave.com/docs/making-payments/virtual-cards) |
| Union54 | Pay per API call | — | 1% of transaction (2022 example) | [Technext Jul 2022](https://technext24.com/2022/07/20/union54-and-issues-of-chargeback-fraud/) |
| Nium | Not published | — | — | [Aspire 2026](https://aspireapp.com/blog/nium-global-card-review-singapore) |
| WAEMU banks: monthly management of a prepaid card | UBA CI **500 F/month**; BICICI 454 F/month | — | — | UBA CI 2026; BICICI 2026 |

---

## 8. Model inputs check

FX assumption for conversions: 580 FCFA per USD (illustrative).

| Input | Current model | Evidence (summary) | Recommended low / base / high | Reasoning |
|---|---|---|---|---|
| **Card processing per active card per month** | 1,000 FCFA (~USD 1.7) | No WAEMU processor price is public. Proxies: Sudo per-card costs are tiny (₦50 per quarter + ₦5 per authorisation). Chipper's partner bank charges cardholders USD 1/month. WAEMU banks charge prepaid holders 454–500 F/month. Mastercard per-transaction scheme fees are about USD 0.01–0.03 domestic and **USD 0.43 per cross-border transaction** (US proxy). | **600 / 1,000 / 1,800 FCFA** | 1,000 F is a reasonable all-in figure for processor + sponsor + domestic scheme fees on a low-transaction SME card. The high case covers business cards with many cross-border transactions. Alternatively, model fixed cross-border per-transaction fees separately (about 250 F per foreign transaction). Until scale is reached the monthly minimum binds, so the per-card rate matters little in years 1–2. |
| **Physical card printed and delivered** | 4,500 FCFA | Manufacture ₦1,800 (~USD 1.2–1.7, NG 2025). Stripe USD 3.50 (~2,000 F) before shipping. Union54 USD 7–9. Dakar courier 1,000–3,000 F. Retail references: Djamo charges 2,000 F with free delivery; UBA personalisation 2,000 F. | **3,000 / 4,500 / 7,000 FCFA** | Card + personalisation + carrier is about 1,500–3,000 F at small runs, and delivery about 1,500–2,500 F, so 4,500 F is a sound base. The high case covers small minimum-order runs of a custom business design, failed deliveries and Abidjan or out-of-Dakar delivery. In-app PIN avoids PIN-mailer cost. |
| **Visa/MC cross-border fees (cost)** | 0.5% of FX spend | Network issuer cross-border is about **0.9–1%** (Synctera MC 0.9%; "1%" Bankrate), plus fixed international authorisation and clearing (~USD 0.43 per transaction), plus the sponsor's FX spread on non-EUR currencies. No WAEMU-specific schedule found. | **0.8% / 1.2% / 2.0%** (plus ~250 F per transaction in the high case) | 0.5% looks too low for an issuer whose sponsor bank settles in EUR/USD. EUR spend has no conversion spread (peg), but USD spend does. |
| **Kelen FX fee charged to clients** | 1% | Market: Djamo 200 F + 3–4% (EUR); NSIA 2.5% (minimum 2,500); UBA 2.5–3%; Coris 2% + 500 F; BICICI 2%; CBAO 0.5% + 855 F; Wave "0" (margin hidden in rate). | **1.5% / 2.0% / 2.5%** (+100–200 F fixed) | At 1% with a ~1.2% cost the line loses money. Charging 2% still undercuts banks and Djamo. Price separately for EUR (no conversion) and USD/other. |
| **Interchange received on FX spend** (missing from model) | not modelled | Visa interregional at US merchants: **Commercial 2.00%**, Classic 1.10% (Visa USA IRF, 18 Apr 2026). The share passed to the programme manager is not public. | **0.5% / 0.8% / 1.2%** of FX spend (Kelen's net share) | This is a large revenue line for SME spend on US/EU digital services, and adding it partly offsets the higher cross-border cost. It depends on the sponsor contract and a commercial (business) BIN. |
| **Fraud and chargebacks** | 0.15% of card spend | EEA 0.031% of value (H1 2023), mostly cross-border. No WAEMU data. African USD-virtual-card programmes had severe chargeback-fraud episodes (Union54 2022). Dispute fees are USD 1.35–15 per case. | **0.07% / 0.15% / 0.40%** | 0.15% is about 5× the EEA rate and reasonable for a 3DS-protected, KYB'd business card. The high case reflects a card-not-present-heavy, cross-border-heavy mix in the launch year and declined-transaction or dispute fees. |
| **Interchange share on FCFA spend** | 0.5% (scenarios 0.3 / 0.5 / 0.7) | GIM domestic split gives the issuer 20% of the merchant commission. MDR is 2% (GIM) to 3–3.5% (Visa/MC) at UBA CI and ~2.75% at SG SN, so the issuer gets **about 0.4–0.7%** before Kelen's share. Decision 31 re-routes domestic Visa/MC through GIM, with unknown effect on interchange. | **0.15% / 0.30% / 0.50%** | The sponsor bank keeps part of an already small issuer share. 0.5% would require Kelen to keep about 100% of a 2.5% MDR × 20%. Domestic acceptance is thin (4,828 terminals in Senegal, 2023). |
| **Processor set-up** | USD 50,000 one-off | No public quotes. The Fast Track promises "reduced fees". Scheme-related costs in Nigeria: USD 2,000/month implementation charge (TechCabal 2024). | **USD 25k / 50k / 120k** | 50k is a fair base for processor integration + BIN set-up + scheme and 3DS certification + card design approval. The high case covers a direct GIM-UEMOA connection, Decision-31 routing and two-country (SN + CI) set-up. |
| **Processor monthly minimum** | USD 5,000 (years 1–2) → 12,000 | No public quotes. Sudo ₦50k/month (~USD 35) is far below. Swan "from €2,990/month" (unverified). Nigeria scheme implementation USD 2,000/month. | **Years 1–2: USD 3k / 5k / 8k. Later: model as max(minimum, per-card × active cards)** rather than a flat 12k | A step to 12k is plausible only if it mirrors per-card volume. Contracts usually set a minimum that is overtaken by usage. Negotiate a ramp. |
| **Card programme collateral at partner bank** | 60M FCFA (~USD 103k) | WAEMU figures not found. Nigeria: "collateral that runs into millions of dollars" for direct scheme membership. A vendor claims more than USD 500k for BIN sponsorship (unverified). For prepaid/debit, the sponsor also requires **prefunded settlement float**. | **30M / 60M / 300M FCFA** (plus prefunding of ~3–5 days of card spend, modelled separately) | 60M F is a defensible base for a sponsored (non-principal) programme. The high case (~USD 500k) reflects bank demands for credit-risk cover if Kelen offers any post-paid or credit feature, or if the sponsor sizes collateral on chargeback exposure. |

### Main changes I would make to the model
1. Raise the **cross-border cost to ~1.2%** and the **client FX fee to ~2%**.
2. **Add interchange income on FX spend** (base 0.8% net to Kelen, subject to the sponsor deal).
3. Cut **FCFA interchange share to base 0.3%**.
4. Add a **regulatory-risk scenario** in which RFE Art. 47 and Art. 12 cap or block SME cross-border card spend, for example a 50% haircut on FX spend.
5. Model a **settlement prefunding float** separate from collateral.
