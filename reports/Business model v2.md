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

The full, line-by-line cost breakdown in euros is in the **"Cost breakdown (€)"** tab. It is built from Dakar salary grids, Senegal's 2026 social-charge rates, local office rents and vendor price lists, for this plan (20 → 37 → 53 people, sales-heavy, lean technology). Summary:

| | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Fixed costs | ≈ €991k (≈ 650 M FCFA) | ≈ €1.51 M (≈ 989 M FCFA) | ≈ €1.93 M (≈ 1,266 M FCFA) |
| Result | ≈ −€901k (≈ −591 M FCFA) | ≈ −€976k (≈ −640 M FCFA) | ≈ −€138k (≈ −91 M FCFA) |
| Equity to raise (total) | ≈ €4.6 M (≈ 3.0 bn FCFA) | | |

The business becomes profitable month by month by the end of year 3, and year 4 is the first full profitable year.

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
