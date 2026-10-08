# Business model: where the money comes from and where it goes

This page sets out how Jokko makes money with a partner bank in Senegal, product by product, what it costs to run, and what one typical client is worth. Amounts are in FCFA with euro equivalents (1 EUR = 655.957 FCFA).

**Most prices, revenue shares and costs below are working assumptions, not market data.** No Senegalese bank publishes its fintech-partnership prices, and no survey yet shows what SMEs will pay. Each assumption is labelled so you can replace it with real quotes after the bank meetings.

## The model in one paragraph

Jokko earns from four engines.

1. **Software subscriptions** that companies pay Jokko directly.
2. **Payment fees** on payouts, collections and card spending abroad.
3. **A share of the banking economics** the partner bank earns on Jokko's clients: deposits, card interchange and loans.
4. **Credit margin**, which becomes the largest engine once Jokko lends through a microfinance licence.

In the partner-bank phase, the first two engines carry the business, because the bank keeps most of the banking economics. Profit at scale comes from credit, as at Qonto's peers, Moniepoint and Nubank.

## First, who is allowed to charge what

During the partner phase, the account, the cards and the loans legally belong to the bank. That shapes the model in three ways.

**1. Basic account services must be free.** Since 1 October 2014, the BCEAO has required banks across WAEMU to provide **19 banking services free of charge**. They include account opening, a monthly statement, salary domiciliation, cash deposits and withdrawals at the client's own branch, and account closure ([BCEAO](https://www.bceao.int/fr/communique-presse/communique-de-presse-services-bancaires-offrir-titre-gratuit-par-les); [La Nouvelle Tribune](https://lanouvelletribune.info/2014/08/activites-bancaires-dans-l-uemoa-une-vingtaine-de-services-gratuits-des-octobre-prochain/)). The list dates from 2014 and must be checked against the current version. Either way, Jokko cannot charge "account keeping" fees. **The subscription must pay for software and service**: approvals, bulk payroll, cards management, bookkeeping, support.

**2. Two billing flows run side by side.**

| Flow | Who bills the client | What it covers |
|---|---|---|
| Jokko → client | Jokko, as a technology company | Subscription plans, software features, possibly payout fees for the service layer |
| Bank → client | The bank, under its published tariff | Transaction fees, card fees, loan interest and fees |
| Bank → Jokko | Revenue share or commission | Jokko's share of the bank's income from Jokko clients (deposits, interchange, loans) |

**Counsel must confirm** which fees Jokko may bill directly before it holds its own payment institution licence, and how the revenue share is documented (often as a business-introducer, or "apporteur d'affaires", contract).

**3. Loans and factoring are capped at 14% all-in through a bank.** WAEMU's usury cap is **14% a year for banks and 24% for microfinance institutions (SFDs)** from 1 June 2026, all fees included ([BCEAO Decision 19/2025](https://www.bceao.int/sites/default/files/2026-01/Decision-No19-du-29-12-2025_CMUMOA_fixant_le_taux_de_l-usure.pdf)). Factoring follows the WAEMU uniform factoring law of 10 December 2020: only credit institutions and licensed SFDs may provide it, and it is subject to the usury cap ([Sidwaya](https://www.sidwaya.info/boukare-zouanga-directeur-des-affaires-monetaires-et-financieres-laffacturage-offre-aux-entreprises-lassurance-dun-paiement-rapide-et-sur/)). Senegal is transposing the law in 2026 (bill n°09/2026) ([Vie publique Sénégal](https://www.vie-publique.sn/documents/13898/projet-loi-09-2026-activite-affacturage-senegal); [Droit Médias Finance](https://droitmediasfinance.com/index.php/actualites/droit-bancaire/1291-senegal-le-cadre-juridique-de-laffacturage-sharmonise-avec-les-normes-communautaires)).

**One distinction matters for your "affacturage on future receivables":** factoring finances **invoices already issued**. Financing **future** receivables is a cash-flow loan, not factoring. It is riskier, sits under the same 14% cap at a bank, and should come after classic factoring.

## Revenue, product by product

### Launch products (with the partner bank)

| Product | How it earns | Pricing hypothesis | Jokko's share | Direct cost | Margin quality |
|---|---|---|---|---|---|
| **Business account (IBAN)** | Not directly: basic services are free by rule. Earns through the **subscription** and the **deposit share** | Subscription plans (see below) | 100% of the subscription | Bank per-account or platform fee; KYB checks | Good, if clients value the software |
| **Deposits on business accounts** | The bank earns on client balances; Jokko negotiates a commission on average balances | 1–2% a year on average balances (the BCEAO policy rate is 3.25%) | Negotiated; **the most important line to negotiate** | None | High margin, but entirely at the bank's discretion |
| **Virtual and physical cards** | Card fee, a share of interchange, and an **FX margin on spending outside the CFA zone** (Meta and Google ads, SaaS, travel) | Physical card 5,000–10,000 FCFA a year; FX margin 1.5–2.5% over the network rate | 100% of the card fee and FX margin if Jokko bills them; 30–60% of interchange | Issuer-processor fees per card and per transaction, card printing and delivery, fraud and chargebacks | **FX margin is the best card revenue**; interchange in WAEMU is unknown and probably low |
| **Mass payouts (banks and mobile money)** | Fee per payout, or a percentage | 100–300 FCFA per payout, or 0.5–0.8% to wallets; **salaries included in the plan up to a quota**; Wave's 1% is the ceiling | 100% of Jokko's fee, minus rail costs | PI-SPI and bank transfer fees; aggregator fees for wallets that are not yet on PI-SPI | Medium: competitive, but recurring and high-volume |
| **Receiving from banks (IBAN) and mobile money** | Incoming bank transfers free (it brings deposits); fee on wallet collections and payment links | 0.8–1.5% on wallet collections (aggregators charge 1.5–3.5%) | 100%, minus rail costs | Pay-in costs of 0.5–1.5% through aggregators; PI-SPI receiving is free | Thin on wallets, good on volume |
| **Loans through the partner bank** | Referral or origination fee and a share of interest | ≤ 14% a year all-in for the client | Typically 20–50% of the net margin, often against Jokko first-loss cover | Credit losses Jokko covers; collection costs | Thin at 14%: funding costs 4–6%, losses 1–3%, leaving a small pool |
| **Factoring (existing invoices)** | Factoring fee on each financed invoice | About 1–1.15% a month all-in (inside 14% a year), advance of 80–90% of the invoice | Share of the fee | Debtor checks, collections, first-loss | **Good fit at 14%**, because risk sits with large, solid debtors and tenors are short |
| **Future-receivables financing** | Interest and fees | ≤ 14% a year at a bank | Share of the margin | Higher credit losses | Weak at 14%; wait for Jokko's own SFD (24% cap) |

### Later products

| Product | How it earns | Notes |
|---|---|---|
| **Multi-users, approvals, invoices, payment links** | Included in subscription plans; they justify higher tiers | Payment links also earn the collection fee |
| **Vaults (savings pots)** | Deposit share now; interest margin once Jokko has its own SFD | A payment institution cannot pay interest on balances |
| **B2C accounts** | Premium subscription (Djamo charges 2,000 FCFA ≈ €3.05 a month, and 25% of its users pay), card FX margin, deposit share | Retail revenue per user is low (Djamo's implied figure: $10–50 a year); the value is in credit and deposits |
| **Salary advance** | Fee or interest within the **24% cap** through a partner SFD: at most about **1.97% for 30 days** | Low risk because the salary lands in Jokko; Jokko shares the margin with the SFD |
| **Unsecured lending** | Interest margin, up to 24% through an SFD | The biggest profit pool long term, and the biggest risk |
| **Accounting portal** | Free for accountants: it is a **sales channel**, not a revenue line | Optionally a paid tier for large accounting firms |

### Subscription plans (hypothesis to test)

| Plan | For | Includes | Price a month |
|---|---|---|---|
| Solo | Freelancers, sole traders | Account, 1 user, virtual card, transfers | Free to 5,000 FCFA (≈ €8) |
| Essentiel | 2–10 employees | Multi-user, approvals, bulk payments, payroll up to 10 people, 3 cards | 15,000–25,000 FCFA (≈ €23–38) |
| Business | 10–100 employees | Payroll up to 100 people, sub-accounts, accountant access, physical cards, salary advance for staff | 35,000–75,000 FCFA (≈ €53–114) |
| Entreprise | 100+ employees, NGOs | API, integrations, account manager, custom limits | On quote |

For comparison, banks charge SMEs **10,000–25,000 FCFA (≈ €15–38) a month** for an account alone (UBA Senegal), and Wave charges **1% on every bulk payout**. A 40-person company at the average formal salary pays Wave about **152,000 FCFA (≈ €232) a month** for its payroll alone. Jokko's whole bill should stay well below that.

## Costs

### Variable costs (grow with clients and volume)

| Cost | What it is | Order of magnitude (assumption) |
|---|---|---|
| Partner bank fees | Per account, per transaction, platform fee | To be quoted; budget 2,000–5,000 FCFA per business client a month |
| Card processing | Issuer-processor fees per active card and per transaction; 3-D Secure; tokenisation | About 500–1,500 FCFA per active card a month |
| Card production and delivery | Physical cards and courier in Dakar | About 3,000–6,000 FCFA per physical card |
| Payment rails | PI-SPI and bank transfer costs; wallet aggregators (Hub2, InTouch, CinetPay) for pay-ins and payouts | Pay-ins 0.5–1.5%; payouts 0–300 FCFA each (vendor estimates) |
| KYC and KYB | ID checks, sanctions and PEP screening, company document checks, field visits | 300–1,500 FCFA per individual; 5,000–20,000 FCFA per company onboarded |
| Messaging | SMS, WhatsApp notifications, one-time passwords | Small per message, adds up with volume |
| Fraud and chargebacks | Card fraud, social-engineering losses | Budget 0.1–0.3% of card volume at first |
| **Credit losses** | Jokko's first-loss cover on partner loans and factoring | 5–20% first-loss on the portfolio, to negotiate; expected losses 1–3% for salary-backed and invoice products |
| Taxes on flows | **0.5% transfer tax on supplier payouts** (salaries are exempt) | Usually passed to the client |

### Fixed costs (year one, lean team in Dakar)

| Cost | What it is | Year-one estimate (assumption) |
|---|---|---|
| **Team** (largest cost) | About 20 people: engineering and product, compliance (a named AML officer is mandatory), operations and support, B2B sales and account management, finance | **≈ 300 M FCFA (≈ €457k)** at an average loaded cost of 1.25 M FCFA a month |
| Technology and vendors | Core ledger, card processor platform fees, eKYC, AML screening, cloud, security audits and PCI DSS | 100–150 M FCFA (≈ €152–229k) |
| Partner bank set-up | Integration, set-up fee, platform minimums | 20–60 M FCFA (≈ €30–91k); quotes needed |
| Legal, audit, compliance | Banking counsel, licence file, auditors, data-protection filings, insurance | 60–100 M FCFA (≈ €91–152k) |
| Sales and marketing | B2B sales, accountant partner commissions, events | 50–100 M FCFA (≈ €76–152k) |
| Office and administration | Rent, equipment, admin | 30–50 M FCFA (≈ €46–76k) |
| **Total year-one operating costs** | | **≈ 560–760 M FCFA (≈ €0.85–1.16 M)** |

### Capital tied up (not spent, but must be raised)

| Item | Amount |
|---|---|
| Payment institution licence capital (Senegal) | 100 M FCFA (≈ €152k), plus 100 M FCFA for Côte d'Ivoire later |
| Card programme collateral at the partner bank | To be quoted; often tens of millions of FCFA |
| First-loss reserve for partner loans and factoring | 5–20% of the loan book Jokko originates |
| SFD capital (later) | Not fixed by law; set by the business plan |

## What one client is worth

A 40-employee Dakar company on the Business plan. **Every figure is an assumption.**

| Revenue line | Basis | FCFA a month |
|---|---|---|
| Subscription | Business plan | 50,000 |
| Supplier payouts | 30 payouts × 300 FCFA (salaries included in the plan) | 9,000 |
| Card FX margin | 1.2 M FCFA of ad and SaaS spending abroad × 2% | 24,000 |
| Card interchange share | 0.8 M FCFA local spending × 0.5% | 4,000 |
| Deposit share | 12 M FCFA average balance × 1.5% a year | 15,000 |
| Collections | 3 M FCFA through payment links and wallets × 0.5% net | 15,000 |
| **Subtotal without credit** | | **≈ 117,000 (≈ €178)** |
| Factoring, if used | 10 M FCFA outstanding × 3% a year (Jokko's share) | 25,000 |
| Salary advance for staff (later) | 12 employees × 75,000 FCFA × 0.8% Jokko share per cycle | 7,000 |
| **Total with credit** | | **≈ 149,000 (≈ €227)** |

| Cost to serve | Basis | FCFA a month |
|---|---|---|
| Bank per-client fees | Assumption | 5,000 |
| Card processing | 4 cards | 4,000 |
| Payout rail costs | 30 payouts × 100 FCFA | 3,000 |
| 40 employee accounts | Processor, KYC, messaging, at ~150 FCFA each | 6,000 |
| Support and onboarding, spread over time | Assumption | 7,000 |
| **Total** | | **≈ 25,000 (≈ €38)** |

**Contribution: about 90,000–125,000 FCFA (≈ €140–190) a month per client of this size**, or roughly 1.1–1.5 M FCFA (≈ €1,700–2,300) a year.

## When does it break even?

With year-one fixed costs of about **700 M FCFA (≈ €1.07 M)**:

- With mid-size clients like the one above, break-even needs **about 470–640 clients**.
- With a realistic mix that includes many small firms (contribution nearer 40,000–50,000 FCFA a month), it needs **about 1,200–1,450 clients**.

Senegal has about **40,300 employers paying IPRES**, most of them small. 1,200–1,450 clients is roughly **3–3.5% of all formal employers**, and a much larger share of those with 10 or more staff. That is achievable but demanding. Three things follow:

1. **Senegal alone is a tight market for break-even.** Côte d'Ivoire is what makes the numbers comfortable.
2. **Credit is what turns the model profitable.** Factoring and salary advances add 20–30% to revenue per client at launch; with Jokko's own SFD, credit should become the largest revenue line.
3. **The deposit share is the line to fight for** in the bank negotiation. It costs Jokko nothing to deliver and grows with every client.

## How the revenue mix should shift

Illustrative shares of revenue, not a forecast:

| Phase | Subscriptions | Payments (payouts, collections) | Cards (FX, interchange) | Deposit share or interest | Credit |
|---|---|---|---|---|---|
| Partner bank (months 0–15) | 40–50% | 20–30% | 15–20% | 5–10% | 0–10% |
| Own payment licence (months 15–30) | 30–40% | 20–25% | 15–20% | 5–10% | 15–25% |
| Own SFD (year 3+) | 20–25% | 10–15% | 10–15% | 10–15% | **40–50%** |

Moving to Jokko's own payment licence improves margins on payments and cards, because Jokko stops sharing them with the bank. Moving to its own SFD raises the credit cap from 14% to 24% and lets Jokko pay interest on savings.

## What to negotiate with the partner bank

1. **A commission on client deposits** (average balances): the biggest margin line.
2. **The interchange split** on cards, and Jokko's right to set the FX margin.
3. **Origination and servicing fees on loans and factoring**, and the size of first-loss cover.
4. **Per-transaction and per-account prices**, with volume tiers.
5. **The size of the card collateral deposit.**
6. **No exclusivity** (the BCEAO bans exclusivity clauses), and the right to move clients to Jokko's own licence later.
7. **Jokko owns the customer relationship and data**, within data-protection law.

## Points to verify

- The current list of free banking services (the 2014 list may have been updated) ([Burkina24](https://burkina24.com/?p=68585)).
- **Tax on Jokko's fees.** Senegal's standard VAT is 18%. Several WAEMU states replace VAT on financial services with a financial activities tax (Burkina Faso's is 17%), but no source confirmed whether Senegal does ([Sidwaya](https://www.sidwaya.info/nouvelle-taxe-sur-les-activites-financieres-les-operations-soumises-a-la-taf-sont-exonerees-de-la-tva-dixit-linspecteur-des-impots-idrissa-ouedraogo/)). A tax adviser must confirm.
- Whether Jokko may bill subscriptions and payout fees directly while the bank holds the licence.
- WAEMU card interchange rates: none found.
- Senegal's factoring law: whether bill n°09/2026 has passed, and its usury article.
- Every price and cost assumption above, against real quotes.
