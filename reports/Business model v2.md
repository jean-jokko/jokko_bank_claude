# Business model v2: one subscription, few fees, credit from year one

This version replaces the first business model. The idea: make the account so simple and cheap that companies switch to it as their main account, then earn mostly on credit once their money flows through Jokko.

- **One subscription by company size** (1–10, 11–50, 51+ employees) that covers almost everything.
- **Only a handful of published fees**: a one-off fee for a physical card and a low fee on card spending in foreign currencies. Nothing hidden.
- **Credit up to 24% a year** from about **month 12**, with several products and simple, transparent pricing.

Amounts are in FCFA with euro equivalents (1 EUR = 655.957 FCFA). **Prices, volumes and costs are working assumptions**, labelled as such, to be replaced with real quotes and pilot data.

## One structural point first: 24% needs a microfinance partner, not a bank

The WAEMU usury cap is **14% a year for banks** and **24% for microfinance institutions (SFDs) and financial credit institutions**, all fees included, since 1 June 2026 ([BCEAO Decision 19/2025](https://www.bceao.int/sites/default/files/2026-01/Decision-No19-du-29-12-2025_CMUMOA_fixant_le_taux_de_l-usure.pdf)). **Loans made by the partner bank cannot be priced at 24%.**

So the set-up needs two partners from the start:

| Partner | Role | Why |
|---|---|---|
| **Partner bank** (Ecobank, SUNU Bank, BOA…) | Business accounts with IBAN, client funds, cards | Only a bank (or later Jokko's own payment licence) can do this |
| **Partner SFD** (Baobab, Cofina, PAMECAS…) | Lender of record for all credit products, including factoring | The 24% cap applies to SFDs; SFDs are allowed to do factoring under the WAEMU uniform factoring law |

Later, Jokko's **own SFD licence** lets it keep the whole credit margin. Because credit is now the core of the model, it is worth looking at **buying a small existing SFD** in Senegal (with BCEAO approval of the change of control) instead of waiting about three years for a new licence, as Djamo did.

## The subscription

| Plan | Company size | Price a month | Price a year (2 months free) |
|---|---|---|---|
| **Petite** | 1–10 employees | **9,900 FCFA (≈ €15)** | 99,000 FCFA (≈ €151) |
| **Moyenne** | 11–50 employees | **29,900 FCFA (≈ €46)** | 299,000 FCFA (≈ €456) |
| **Grande** | 51+ employees | **79,900 FCFA (≈ €122)** | 799,000 FCFA (≈ €1,218) |

Suggested launch offer: **first 3 months free**, no set-up fee, cancel any time.

**Every plan includes:**

- Business account with IBAN and statements
- Unlimited users with roles and double-signature approvals
- Unlimited virtual cards
- Salary payments to every employee, to any bank or wallet
- Supplier payouts to banks and wallets (fair-use allowance below)
- Receiving bank transfers and PI-SPI payments, free
- Payment links, quotes and invoices
- Sub-accounts and savings vaults
- Accountant access and exports
- **A free account and card for every employee**, with salary advance

**Why these prices work against the competition:**

| Alternative | What a 25-person company pays a month |
|---|---|
| Bank SME account (UBA Senegal) | 10,000–25,000 FCFA for the account alone, plus transfer and card fees |
| Wave Business | 1% of every bulk payout: **about 95,000 FCFA** for a 9.5 M FCFA payroll (25 × 380,000 FCFA average formal salary) |
| Djamo Business | Free account, but limited business workflows |
| **Jokko Moyenne** | **29,900 FCFA, everything included** |

Djamo Business is free, so the Petite plan must clearly do more than Djamo (approvals, payroll, invoices, accountant access) or the price should be tested lower.

## The only other fees

| Fee | Amount | Covers |
|---|---|---|
| Physical card | **5,000 FCFA (≈ €7.6) one-off**; first card free for the company owner | Printing and delivery (cost about 3,000–6,000 FCFA) |
| Card spending in FCFA (WAEMU and CEMAC) | **Free** | — |
| Card spending in other currencies (ads, SaaS, travel) | **1%** | FX cost and margin; banks and most wallets charge 2–3% or more |
| Supplier payouts above the fair-use allowance | **100 FCFA per payout** | Rail costs |
| Mobile money collections through payment links | **1%** | Operator and aggregator costs (0.5–1.5%) |
| 0.5% State transfer tax on supplier payouts | Passed through at cost, shown on each payout | A tax, not a Jokko fee; **salaries are exempt** |

**Fair-use allowance for supplier payouts:** 50 a month on Petite, 200 on Moyenne, 1,000 on Grande. Salary payments are always unlimited. A published allowance keeps the "no hidden fees" promise while protecting against clients who would otherwise cost more in rails than they pay.

## Credit products

All credit is priced on **one rule: a daily rate of 0.063% on the amount actually used**, which is **23% a year**, just under the 24% cap. No set-up fees, no commitment fees, no penalties hidden in small print. The cost in FCFA is shown before every draw.

**Why a daily rate and not a flat fee:** the all-in rate (TEG) is calculated on the real duration. A flat 2% fee on a loan repaid in 10 days is a 73% annual rate, which is illegal. Pricing per day keeps every product inside the cap, whatever the repayment date.

| Product | For | Amount | Duration | Price | Repayment | Start | Risk |
|---|---|---|---|---|---|---|---|
| **Factoring** (affacturage) | Companies with invoices on large private clients | 80–90% of the invoice | 30–90 days | 0.063% a day on the amount advanced: 1.9% for 30 days, 5.7% for 90 days | The debtor pays the invoice into Jokko | **Month 12** | Low (solid debtors) |
| **Payroll bridge** | Companies paying salaries through Jokko | Up to one month of payroll | Up to 45 days | 0.063% a day | Automatic, from incoming payments | **Month 12** | Low to medium |
| **Salary advance** | Employees of client companies | Up to 50% of pay already earned | Until payday | 0.063% a day: 75,000 FCFA for 15 days costs 709 FCFA | Deducted on payday | **Month 9–12** | Very low |
| **Flexible credit line** | Companies with 6+ months of activity on Jokko | 5–30% of monthly inflows | Revolving, 30 days per draw | 0.063% a day on the amount drawn only | Automatic sweep of incoming payments | **Month 15** | Medium |
| **Supplier pay-later** | Companies paying suppliers through Jokko | Supplier invoice amount | 30 / 60 / 90 days | 1.9% / 3.8% / 5.7% | Fixed date, automatic | **Month 15–18** | Medium |
| **Future-receivables financing** | Companies with regular collections | Based on past collections | 3–6 months | 0.063% a day; paying back faster costs less | 10–20% of each incoming payment | **Month 18+** | Medium to high |
| **Equipment and term loans** | Vehicles, machines, staff phones | 1–50 M FCFA | 6–24 months | 22–23% a year on the remaining balance | Monthly instalments | **Month 18–24** | Medium |
| **Personal loans (B2C)** | Employees and retail customers | Up to ~1 M FCFA, then more | 3–12 months | 22–23% a year | Monthly, from salary | **Year 2–3** | Medium to high |

**Which products make money.** At 23% a year, short and small loans earn little in FCFA. The salary advance in the table earns 709 FCFA, before funding costs and losses. **Salary advances are a retention and acquisition product, not a profit centre.** The profit comes from **larger and longer business credit**: factoring, the payroll bridge, the credit line and term loans.

**How to start as early as month 12:**

- Sign the partner SFD by month 6–9, with a written legal opinion on the pricing.
- Launch first the products that need the least history: **factoring** (risk is on the debtor, not the client) and the **payroll bridge** (Jokko sees the payroll).
- Open the **credit line** at month 15, once clients have 6 months of transactions in Jokko.
- Build the credit team in months 6–12: a credit risk lead, a collections lead, and the scoring model.

## What credit earns

For every **1 bn FCFA (≈ €1.52 M) of loans outstanding**, over a year:

| Line | Rate | FCFA |
|---|---|---|
| Interest and fees | 23% | 230 M |
| Cost of funds | 8–10% | −80 to −100 M |
| Credit losses | 2–4% | −20 to −40 M |
| Servicing and collections | 2% | −20 M |
| **Net credit margin** | **about 7–11%** | **about 70–110 M (≈ €107–168k)** |

**Who keeps that margin depends on who funds the loans:**

- **Partner SFD funds, Jokko provides first-loss cover:** Jokko keeps a negotiated share, assumed here at about **half, roughly 4–5% a year** of the loan book.
- **Jokko funds through its own SFD and debt lines (DFI lines, local debt funds, later deposits and securitisation):** Jokko keeps **all of it, about 7–11%**.

## What each plan is worth

Typical clients, **all figures assumed**. Interchange rates in WAEMU are unknown; 0.5% is a placeholder.

| Line (FCFA a month) | Petite (5 staff) | Moyenne (25 staff) | Grande (120 staff) |
|---|---|---|---|
| Subscription | 9,900 | 29,900 | 79,900 |
| 1% fee on foreign card spending | 3,000 (on 0.3 M) | 12,000 (on 1.2 M) | 35,000 (on 3.5 M) |
| Interchange share (0.5% placeholder) | 1,500 | 4,000 | 12,500 |
| Deposit share (1.5% a year on balances) | 3,750 (3 M) | 12,500 (10 M) | 50,000 (40 M) |
| Physical cards, spread over 24 months | 400 | 1,000 | 3,100 |
| **Revenue without credit** | **≈ 18,550 (≈ €28)** | **≈ 59,400 (≈ €91)** | **≈ 180,500 (≈ €275)** |
| Cost to serve (bank, cards, payouts, employee accounts, support) | ≈ −11,000 | ≈ −25,000 | ≈ −88,000 |
| Card scheme fees on foreign spending (≈ 0.5%, assumption) | ≈ −1,500 | ≈ −6,000 | ≈ −17,500 |
| **Contribution without credit** | **≈ 6,000 (≈ €9)** | **≈ 28,400 (≈ €43)** | **≈ 75,000 (≈ €114)** |
| Typical credit if the client borrows | 1.5 M FCFA credit line | 10 M FCFA factoring | 50 M FCFA factoring and credit line |
| Net credit margin to Jokko (partner-funded, ~4.5% a year) | ≈ 5,600 | ≈ 37,500 | ≈ 187,500 |
| Net credit margin to Jokko (own funding, ~9% a year) | ≈ 11,250 | ≈ 75,000 | ≈ 375,000 |
| **Contribution with credit (partner → own funding)** | **≈ 11,700–17,300** | **≈ 66,000–103,000** | **≈ 262,000–450,000** |

Four things stand out:

1. **The Petite plan barely pays for itself without credit.** That is fine if it is the entry door, but it must convert to credit or move up a plan as the company grows.
2. **Credit doubles or triples the value of Moyenne and Grande clients**, and multiplies it again once Jokko funds its own book.
3. **Deposits matter.** The share of the bank's income on client balances is the largest non-credit line for larger clients, so it is the first thing to negotiate with the bank.
4. **The 1% fee on foreign card spending is mostly a cost recovery.** Visa and Mastercard charge issuers cross-border fees, assumed here at about 0.5%, so Jokko keeps only about half of it.

## Cost structure

All costs below are **assumptions for planning**, to be replaced with quotes from the partner bank, the SFD, vendors and a Dakar salary benchmark. Amounts are in millions of FCFA (M) a year unless stated.

### 1. Team: the largest cost

"Loaded cost" means gross salary plus employer social charges (IPRES, CSS) and benefits.

| Function | Roles | Headcount Y1 / Y2 / Y3 | Loaded cost per person a month | Y1 | Y2 | Y3 |
|---|---|---|---|---|---|---|
| Leadership | CEO, CTO, COO; CFO from year 2 | 3 / 4 / 4 | 2.0 M | 72 | 96 | 96 |
| Engineering and product | Backend, mobile, web, QA and DevOps, product, design | 10 / 14 / 18 | 1.3 M | 156 | 218 | 281 |
| Compliance and risk | AML compliance officer (mandatory), compliance analysts, internal control | 2 / 3 / 4 | 1.1 M | 26 | 40 | 53 |
| Credit | Credit risk lead (from month 6), analysts, collections | 1 / 4 / 7 | 1.0–1.5 M | 9 | 48 | 84 |
| Operations and support | Company onboarding (KYB), customer support, reconciliation | 3 / 6 / 10 | 0.5 M | 18 | 36 | 60 |
| Sales and partnerships | B2B sales, accountant and payroll-software partnerships, account managers | 2 / 5 / 8 | 0.9 M | 22 | 54 | 86 |
| Finance and administration | Finance, HR, admin | 1 / 2 / 3 | 0.8 M | 10 | 19 | 29 |
| Côte d'Ivoire | Country manager (other CI staff counted above) | 0 / 1 / 1 | 2.0 M | 0 | 24 | 24 |
| **Total team** | | **22 / 39 / 55** | | **313** | **535** | **713** |

Year one assumes most hires are in place by month 3; a slower ramp-up would lower it to about 270 M.

### 2. Other fixed costs

| Category | What it covers | Y1 | Y2 | Y3 |
|---|---|---|---|---|
| Technology platforms | Core ledger and banking software, card processor platform fee, eKYC and AML screening minimums, cloud hosting, monitoring, development tools | 100 | 155 | 210 |
| Security and certification | Penetration tests, PCI DSS assessment, security tooling | 20 | 25 | 30 |
| Partner bank and SFD set-up | Integration, set-up fees, monthly minimums (Côte d'Ivoire bank in year 2) | 40 | 30 | 20 |
| Legal and regulatory | Banking counsel, licence files (Senegal payment licence, CI payment licence, SFD), regulatory reporting | 60 | 70 | 60 |
| Audit and compliance | Statutory auditor, mandatory annual AML audit, data-protection filings (CDP Senegal, ARTCI CI) | 20 | 30 | 40 |
| Insurance | Professional liability (required for a payment licence), cyber, directors' liability | 10 | 15 | 20 |
| Marketing and brand | Website, content, events, launch campaigns | 40 | 70 | 110 |
| Partner commissions | Referral fees to accountants and payroll software vendors | 20 | 30 | 40 |
| Office and administration | Dakar office, Abidjan office from year 2, equipment, travel, admin | 40 | 60 | 80 |
| **Total other fixed costs** | | **350** | **485** | **610** |

### 3. Variable costs (grow with clients, cards, payments and loans)

| Cost | Unit | Assumption | Recovered by |
|---|---|---|---|
| Partner bank account and platform fee | Per business client a month | 2,000–5,000 FCFA | Subscription |
| Company onboarding checks (KYB) | Per company, one-off | 5,000–20,000 FCFA | Subscription (note: the 3 free months delay recovery) |
| Card processing | Per active card a month | 500–1,500 FCFA | Subscription, interchange share |
| Physical card printing and delivery | Per card, one-off | 3,000–6,000 FCFA | 5,000 FCFA card fee |
| Card scheme cross-border fees | % of card spending in foreign currencies | ≈ 0.5% | 1% foreign spending fee |
| Payout rails (PI-SPI, bank transfers, wallet aggregators) | Per payout | 0–150 FCFA | Subscription; 100 FCFA above the allowance |
| Mobile money collections | % of amount collected | 0.5–1.5% | 1% collection fee |
| Employee accounts (KYC, processor, messaging) | Per employee a month | ≈ 150 FCFA | Subscription now, B2C revenue later |
| Customer support | Per client a month | 3,000–25,000 FCFA by plan | Subscription |
| Fraud and chargebacks | % of card spending | 0.1–0.3% | Margin |
| Credit: cost of funds | % of loans outstanding a year | 8–10% | Interest |
| Credit: losses | % of loans outstanding a year | 2–4% | Interest |
| Credit: servicing and collections | % of loans outstanding a year | ≈ 2% | Interest |
| State transfer tax on supplier payouts | 0.5% of the payout (salaries exempt) | Passed through at cost | Client |

Per client, these variable costs average about **12,500 FCFA a month on Petite, 31,000 on Moyenne and 105,500 on Grande**, or about **27,350 FCFA blended** across the assumed client mix.

### 4. The whole picture, year by year

Client mix: 60% Petite, 30% Moyenne, 10% Grande. Côte d'Ivoire opens in year 2. The loan book is partner-funded in year 2 and increasingly self-funded in year 3. Figures in millions of FCFA.

| | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Clients at year end | 500 | 2,000 (Senegal 1,400, CI 600) | 5,000 |
| Average clients in the year | ~250 | ~1,250 | ~3,500 |
| **Revenue without credit** (≈ 47,000 FCFA a client a month) | **141** | **705** | **1,974** |
| Variable costs (≈ 27,350 FCFA a client a month) | −82 | −410 | −1,149 |
| **Contribution without credit** | **59** | **295** | **825** |
| Average loan book | — (starts month 12) | ≈ 1,200 | ≈ 5,000 |
| Net credit margin to Jokko | — | 54 (≈ 4.5%) | 350 (≈ 7%) |
| **Total contribution** | **59** | **349** | **1,175** |
| Team | −313 | −535 | −713 |
| Other fixed costs | −350 | −485 | −610 |
| **Total fixed costs** | **−663** | **−1,020** | **−1,323** |
| **Result** | **≈ −604 (≈ −€0.92 M)** | **≈ −671 (≈ −€1.02 M)** | **≈ −148 (≈ −€0.23 M)** |

**Monthly break-even arrives late in year 3.** By the end of year 3, 5,000 clients bring about 98 M FCFA a month of contribution and an 8 bn FCFA loan book about 47 M FCFA a month, against about 110 M FCFA of monthly fixed costs. **The first full profitable year is year 4.**

### 5. Capital to raise (not costs, but cash needed)

| Item | Amount (M FCFA) | When |
|---|---|---|
| Operating losses until break-even | ≈ 1,420 | Years 1–3 |
| Payment licence capital: Senegal, then Côte d'Ivoire | 200 | Years 1–2 |
| Card programme collateral at the partner bank | 25–100 (to quote) | Year 1 |
| First-loss reserve (≈ 10% of the partner-funded loan book) | ≈ 250 | Year 2 |
| Own SFD: licence capital or acquisition price | 300–1,000 (unknown) | Years 2–3 |
| Cash buffer (about 6 months of fixed costs) | ≈ 600 | Ongoing |
| **Total equity to raise** | **≈ 2,800–3,600 (≈ €4.3–5.5 M)** | |

**Debt to fund the loans themselves comes on top**: DFI and local debt lines first, then deposits once Jokko has its own SFD, then securitisation above about 10 bn FCFA.

**What moves the result most:**

| Lever | Effect |
|---|---|
| Own funding of credit sooner (buying an SFD) | Doubles credit margin per FCFA lent |
| Deposit share negotiated with the bank | Each 0.5 point on balances changes year-3 contribution by about 150 M FCFA (≈ 31 bn FCFA of average client balances) |
| Credit losses | Each extra 1 point of losses on the year-end book of 8 bn FCFA costs 80 M FCFA a year |
| Client mix | More Moyenne and Grande clients than assumed brings break-even forward |
| Making the Petite plan free | Costs about 250 M FCFA of contribution in year 3 (≈ 2,100 Petite clients on average × 9,900 FCFA × 12) |

## Risks specific to this model

- **Cheap subscriptions mean many small clients**, each needing company checks (KYB) and support. Onboarding must be very efficient, or the Petite plan loses money.
- **Credit is where losses happen.** Start with the lowest-risk products, keep limits small, and review vintages monthly.
- **The BCEAO is debating new rules for fintechs that lend** (August 2026). Keeping the SFD as lender of record and pricing everything per day inside 24% is the safest structure.
- **Senegal's State payment arrears**: do not factor invoices on the State or state companies until the IMF programme is stable.
- **"Unlimited" invites abuse.** Publish the fair-use allowances clearly.

## To verify

- Whether the partner SFD can do factoring in Senegal now, or only once bill n°09/2026 is adopted ([Vie publique Sénégal](https://www.vie-publique.sn/documents/13898/projet-loi-09-2026-activite-affacturage-senegal)).
- Counsel's opinion that a daily-rate structure with no other fees keeps every product within the all-in rate (TEG) rules.
- Whether Jokko may bill the subscription directly while the bank holds the licence.
- The deposit share, interchange split and per-account fees the bank will actually offer.
- Cost of funds for a partner SFD and for DFI lines in FCFA.
- SME willingness to pay the three plan prices (survey in Dakar).
