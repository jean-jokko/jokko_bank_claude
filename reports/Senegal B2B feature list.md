# B2B feature list for Senegal, by release priority

This is the full feature list for the Senegal business product, with a release priority for each feature. It draws on Qonto, Revolut Business, Mercury, Brex/Ramp (spend management), Julaya, Wave Business and Moniepoint, adapted to what Senegalese companies actually deal with: mobile money, double signatures, IPRES/CSS, Senelec bills and late payers.

One useful parallel: **Qonto is itself a payment institution, not a bank**. It cannot lend, offer overdrafts or pay interest on savings ([Milesopedia](https://milesopedia.fr/guides/avis-qonto/)). That is exactly Jokko's position once it holds a BCEAO payment institution (EP) licence. Qonto built a large business on accounts, cards, payments, invoicing and bookkeeping alone, and added financing through partners. Jokko can follow the same logic, with credit coming from a partner microfinance institution (SFD) and later its own SFD.

## Payroll yes, HR no

**You are right: companies will not want HR inside their bank account, and Jokko should not build it.**

Senegalese SMEs already have tools for payroll calculation, or an accountant who does it:

- **Sage Paie** is the long-standing local reference, with native IPRES/CSS handling and tax (DGID) reports.
- **PayHR Sénégal** (cloud, from about 25,000 FCFA a month), **PaySpace** (multi-country, from about 2,000 FCFA per employee a month), **Odoo Payroll** and **Cegid Talentia** for large groups.
- Below 5–10 employees, most firms still use Excel or their accountant ("expert-comptable").

These figures come from a commercial blog and should be checked ([Kolonell](https://kolonell.com/fr/blog/payroll-saas-senegal-logiciels-2026); [Kolonell](https://kolonell.com/fr/blog/logiciel-paie-bulletin-salaire-senegal-2026)). The same source notes that **paying salaries by Wave or Orange Money is an increasingly requested feature** of payroll tools. In other words, the payroll tools want a payment partner.

So the split is:

| Jokko does (paying people) | Jokko does not do (HR and payroll calculation) |
|---|---|
| Import the pay file from any payroll tool or accountant (Excel/CSV, Sage export, API) | Gross-to-net calculation, income tax, IPRES/CSS calculation |
| Saved employee payee list, payday scheduling, approvals | Payslip generation |
| Pay every employee on any bank or wallet, same day, with status per person | Contracts, leave, timesheets, performance |
| Retry failed payments; confirm receipt to each employee | HR records and HR compliance |
| Offer employees a free salary account and a salary advance | Anything an HRIS does |

**This also turns payroll software vendors and accountants into a sales channel instead of competitors.** A "Pay with Jokko" button inside Sage Paie, PayHR or an accountant's workflow brings employers to Jokko without Jokko writing a line of HR code. Qonto grew in France largely through accountants. In Senegal, accounting firms run payroll for many SMEs, so they are the first partners to recruit.

The earlier plan listed "payslips and IPRES/CSS exports" in the MVP. **They come out.** The only HR-adjacent item that stays is optional: if the payroll tool sends payslip PDFs with the pay file, Jokko can deliver each one to the employee's app alongside the salary.

## Priority levels

| Level | When | What makes it possible |
|---|---|---|
| **P0: Pilot** | Months 3–9 | Partner bank holds funds and issues cards; 10–20 pilot employers; Jokko as technology layer and registered agent |
| **P1: Launch** | Months 9–15 | Jokko's own Senegal EP licence; PI-SPI participation; partner SFD for salary advance |
| **P2: Growth** | Months 15–24 | Product depth, integrations, accountant channel |
| **P3: Expansion** | Months 24–36+ | Jokko's own SFD (credit, interest), international payments, Côte d'Ivoire |

## The full list

### A. Account and onboarding

| # | Feature | What it does | Inspired by | Priority |
|---|---|---|---|---|
| A1 | **Digital company onboarding (KYB)** | Upload RCCM, NINEA, statutes, directors' IDs, beneficial owners; selfie check; option of a field agent visit | Qonto (fully online), Djamo (field agents) | **P0** |
| A2 | **Business account with own bank details (RIB/IBAN)** | On the partner bank at first, then a Jokko EP account | Qonto, Julaya ("RIB Julaya") | **P0** |
| A3 | **Account statements and certificates** | Monthly statements, balance and RIB certificates for tenders and suppliers | Banks (local need) | **P0** |
| A4 | Top-ups from bank transfer and any wallet | Fund the account from a bank or from Wave, Orange Money, Mixx via PI-SPI | Wave, Julaya | **P0** (bank), **P1** (wallets via PI-SPI) |
| A5 | Sub-accounts | Separate balances by project, site, branch or budget | Qonto, Julaya | **P1** |
| A6 | Several companies under one login | For founders and groups with several entities | Julaya, Revolut Business | **P2** |
| A7 | Cash deposits | Deposit cash at partner branches or agents | Julaya "Cash & Collect" | **P2** |
| A8 | **Capital deposit for new companies** | Certificate of capital deposit needed to register a company with APIX (about 26,000 creations a year) | Qonto (a major acquisition channel in France) | **P2**, needs the partner bank to issue the certificate; to verify with counsel |

### B. Paying out (salaries, suppliers, field staff)

| # | Feature | What it does | Inspired by | Priority |
|---|---|---|---|---|
| B1 | **Single transfers to any bank or wallet** | Pay by account number or phone-number alias via PI-SPI | Wave, Revolut | **P0** |
| B2 | **Bulk payments by file import** | Upload the Excel/CSV from any payroll tool or accountant; pay hundreds of people at once | Qonto bulk transfers, Julaya | **P0** |
| B3 | **Payroll run** | Saved employee payee list, scheduled payday, status per person, automatic retry of failed payments, receipt confirmation to each employee | Julaya, Gusto + Mercury pattern | **P0** |
| B4 | **Payee name check before paying** | Shows the registered name on the wallet or account before money leaves, to stop wrong-number payments | UK Confirmation of Payee | **P0** |
| B5 | Scheduled and recurring payments | Rent, subscriptions, regular suppliers | Qonto | **P1** |
| B6 | Bill payment | Senelec, Sen'Eau, Sonatel, Canal+ and other billers | Wave, Orange Money | **P1** |
| B7 | Supplier invoice inbox | Forward or photograph a supplier invoice; Jokko reads it and prepares the payment for approval | Qonto, Ramp | **P2** |
| B8 | Cash-out codes for unbanked recipients | Recipient withdraws cash at an agent with a code | Julaya, money transfer operators | **P3** |
| B9 | International supplier payments | Pay foreign suppliers via the partner bank, with BCEAO FX documentation built in | Revolut Business, Qonto SWIFT | **P3** |

### C. Getting paid

| # | Feature | What it does | Inspired by | Priority |
|---|---|---|---|---|
| C1 | **Receive transfers and wallet payments** | Incoming bank transfers and PI-SPI payments credited instantly | PI-SPI | **P1** |
| C2 | **Payment links** | Send a link by WhatsApp or email; client pays by wallet or card | Paystack, Wave, Stripe | **P1** |
| C3 | **Quotes and invoices** | Branded quotes and invoices with NINEA, RCCM and 18% VAT; sent by WhatsApp or email; marked paid automatically when the money arrives | Qonto invoicing | **P1** |
| C4 | Receivables tracking and reminders | List of unpaid invoices, automatic reminders, ageing view | Qonto, Pennylane | **P2** |
| C5 | QR codes for shops and counters | Static and dynamic QR on PI-SPI | Wave, Moniepoint | **P2** |
| C6 | Field cash collection | Sales reps deposit their collections into the company account, tracked by rep | Julaya "Cash & Collect" | **P2** |
| C7 | DGID-compliant electronic invoicing | Certified e-invoices once the tax authority publishes its calendar | Côte d'Ivoire FNE model | **P2–P3**, depends on DGID |
| C8 | Online checkout API | Accept payments on a website | Paystack, CinetPay | **P3** (aggregators already do this; partner instead) |

### D. Cards and spending

| # | Feature | What it does | Inspired by | Priority |
|---|---|---|---|---|
| D1 | **Virtual cards for online spending** | Pay Meta and Google ads, SaaS, airline tickets; high approval rates are the selling point | Qonto, Revolut, Djamo | **P0** |
| D2 | **Card controls** | Limits per card, freeze, online/ATM/abroad toggles, real-time notifications | Qonto, Brex | **P0** |
| D3 | Physical employee cards | Cards for staff with individual limits | Qonto, Ramp | **P1** |
| D4 | **Receipt capture** | Photo or WhatsApp a receipt; Jokko attaches it to the card payment | Qonto, Ramp | **P1** |
| D5 | Single-use and per-merchant cards | A card locked to one supplier or one payment | Revolut, Brex | **P2** |
| D6 | Staff allowances and petty-cash replacement | Budgets for field staff on cards or wallets, instead of cash in an envelope | Ramp, Julaya | **P2** |
| D7 | Expense reimbursements | Employee submits an expense; once approved, it is paid to their wallet or Jokko account | Qonto, Spendesk | **P2** |

### E. Team, roles and approvals

| # | Feature | What it does | Inspired by | Priority |
|---|---|---|---|---|
| E1 | **Multiple users with roles** | Owner, admin, finance, manager, employee, accountant (read-only) | Qonto | **P0** |
| E2 | **Approval workflows ("double signature")** | One person prepares, one or two approve, with amount thresholds; matches the double-signature habit of Senegalese firms | Qonto requests, Julaya approval policies, bank mandates | **P0** |
| E3 | **Audit log** | Who did what and when, for every action | Qonto, Brex | **P0** |
| E4 | Spending requests | Employee asks for a card, a budget or a transfer; manager approves in one tap | Qonto, Spendesk | **P2** |

### F. Bookkeeping and the accountant

| # | Feature | What it does | Inspired by | Priority |
|---|---|---|---|---|
| F1 | **Categories, VAT tags, notes and attachments** on every transaction | Clean books without retyping | Qonto | **P1** |
| F2 | **Accountant access and exports** | Read-only access; Excel and Sage exports mapped to the SYSCOHADA chart of accounts | Qonto, Pennylane | **P1** |
| F3 | Accounting integrations | Sage, Odoo and other tools used locally | Qonto connectors | **P2** |
| F4 | **Accountant partner portal** | One screen for an accounting firm to manage all its clients' accounts, payroll files and exports | Qonto accountant programme | **P2** (key sales channel) |

### G. Cash and treasury

| # | Feature | What it does | Inspired by | Priority |
|---|---|---|---|---|
| G1 | **Dashboard** | Balance, money in and out, upcoming payments and paydays | Qonto, Mercury | **P1** |
| G2 | Cash-flow forecast | Projected balance from scheduled payments, payroll and invoices due | Agicap, Mercury | **P3** |
| G3 | Interest on idle cash | Term deposits or treasury-bill products | Mercury treasury | **P3** (own SFD or bank partner; an EP cannot pay interest) |

### H. Taxes and social contributions

| # | Feature | What it does | Inspired by | Priority |
|---|---|---|---|---|
| H1 | Pay DGID taxes and IPRES/CSS contributions from the account | Payment only, from figures supplied by the payroll tool or accountant | Local need | **P2**, depends on available electronic channels (unconfirmed for IPRES/CSS) |
| H2 | Tax and social deadline reminders | Calendar of VAT, income tax withholding and IPRES/CSS due dates | Qonto reminders | **P2** |

### I. Credit and financing

| # | Feature | What it does | Who lends | Priority |
|---|---|---|---|---|
| I1 | **Salary advance for employees** | Employer switches it on; employees draw part of earned pay; repaid on payday | Partner SFD, priced under the 24% all-in cap (or employer-funded, if counsel confirms Labour Code art. L.130) | **P1** (~6 months after launch) |
| I2 | **Payroll bridge** | Pays salaries on time when a client pays the company late; repaid when the invoice is paid | Partner SFD, then own SFD | **P3** |
| I3 | Working-capital line | Limit based on the company's flows through Jokko | Own SFD with a DFI guarantee | **P3** |
| I4 | Invoice financing | Advance on invoices issued to solid clients | Own SFD | **P3** (be careful with State invoices, given payment arrears) |
| I5 | Supplier pay-later | Pay a supplier now, repay Jokko in 30–60 days | Own SFD | **P3** |
| I6 | Equipment financing | Vehicles, machines, phones for staff, through partners | Partner lessors | **P3** |

### J. Integrations and API

| # | Feature | What it does | Inspired by | Priority |
|---|---|---|---|---|
| J1 | **Payroll software connectors ("Pay with Jokko")** | Send the pay file straight from Sage Paie, PayHR, PaySpace or Odoo | Mercury + Gusto | **P1** (file format), **P2** (API connectors) |
| J2 | Public API and webhooks | Payouts, collections and balances for larger clients and platforms | Mercury, Julaya | **P2** |

### K. The employee side (the bridge to B2C)

| # | Feature | What it does | Priority |
|---|---|---|---|
| K1 | **Free salary account for employees** | Opened in minutes from the employer's invitation; salary lands instantly | **P0** |
| K2 | **Employee card** | Virtual card first, physical later | **P0** (virtual), **P1** (physical) |
| K3 | Transfers, bill pay, savings vaults | Everyday banking; vaults without interest until Jokko has its SFD | **P0–P1** |
| K4 | Salary advance (see I1) | From the employee's app | **P1** |
| K5 | Payslip delivery | Only if the payroll tool sends the PDF with the pay file | **P2** (optional) |

### L. Trust, security and support

| # | Feature | What it does | Priority |
|---|---|---|---|
| L1 | **Web app plus mobile app** | Finance teams work on computers; managers approve on phones | **P0** |
| L2 | **Fraud controls** | Device binding, cooling-off on new payees, confirmation of large payments, alerts | **P0** |
| L3 | **Human support** | WhatsApp and phone support in French and Wolof; account manager for larger clients | **P0** |
| L4 | Service status and payment tracking | Clear status on every payment, with reasons for failures | **P0** |

## Release plan in order

**P0: Pilot (months 3–9), the minimum to replace the bank and Wave for paying people**

1. Digital onboarding (A1), business account with RIB (A2), statements and certificates (A3), bank top-up (A4)
2. Single and bulk payments to any bank or wallet (B1, B2)
3. Payroll run with retries and receipt confirmations (B3), payee name check (B4)
4. Multi-user roles, double-signature approvals, audit log (E1, E2, E3)
5. Virtual cards with controls (D1, D2)
6. Employee salary account and virtual card (K1, K2, K3)
7. Web and mobile apps, fraud controls, human support (L1–L4)

**P1: Launch (months 9–15), with Jokko's own licence**

8. Wallet top-ups and incoming payments via PI-SPI (A4, C1)
9. Salary advance through the partner SFD (I1, K4)
10. Payment links, quotes and invoices (C2, C3)
11. Physical cards and receipt capture (D3, D4)
12. Sub-accounts, scheduled payments, bill pay (A5, B5, B6)
13. Bookkeeping tags and accountant exports (F1, F2), dashboard (G1)
14. Standard pay-file format for payroll tools (J1)

**P2: Growth (months 15–24)**

15. Accountant partner portal and accounting integrations (F3, F4)
16. Payroll software API connectors, public API (J1, J2)
17. Supplier invoice inbox, receivables reminders (B7, C4)
18. Spending requests, single-use cards, staff allowances, reimbursements (E4, D5, D6, D7)
19. QR acceptance and field cash collection (C5, C6, A7)
20. Tax and IPRES/CSS payments and reminders (H1, H2)
21. Several companies per login, capital deposit for new companies (A6, A8)

**P3: Expansion (months 24–36+)**

22. Business credit on Jokko's own SFD: payroll bridge, working capital, invoice financing, pay-later (I2–I5)
23. Interest on idle cash, cash-flow forecast (G2, G3)
24. International supplier payments (B9), e-invoicing when DGID's calendar is set (C7)
25. Cash-out codes, online checkout, equipment financing (B8, C8, I6)

## Not building

- HR: contracts, leave, timesheets, performance, HR records.
- Payroll calculation: gross-to-net, income tax, IPRES/CSS computation, payslip generation.
- ERP, stock or point-of-sale software.
- Anything crypto.

## How features could map to plans (hypothesis to test)

| Plan | For | Includes | Price hypothesis |
|---|---|---|---|
| Solo | Freelancers, sole traders | Account, 1 user, virtual card, transfers, invoices | Free or low monthly fee |
| Essentiel | Small teams (2–10) | Multi-user, approvals, bulk payments, payroll run, 3–5 cards | 15,000–25,000 FCFA a month |
| Business | 10–100 employees | All of the above, sub-accounts, accountant exports, physical cards, salary advance for staff | 35,000–75,000 FCFA a month |
| Entreprise | 100+ employees, NGOs | API, integrations, account manager, custom limits | On quote |

Prices are hypotheses only: no survey of what Senegalese SMEs will pay exists yet. Wave's 1% on bulk payouts is the ceiling to stay under; for a 40-person firm at the average formal salary, that is about 152,000 FCFA a month.

## To verify

- Payroll software prices and market shares: the only source found is a commercial blog.
- Capital deposit: whether a payment institution's partner bank can issue the deposit certificate APIX needs, and the current minimum capital (Law 2015-07 lets founders set the SARL capital freely, while 2026 blogs still cite 100,000 FCFA) ([OHADA.com](https://www.ohada.com/actualite/2665/ohada-senegal-publication-de-la-loi-2015-07-du-09-avril-2015-portant-organisation-du-capital-social-de-la-sarl.html?langue=fr); [Kolonell](https://kolonell.com/fr/blog/creer-sarl-senegal-procedure-2-semaines-2026)).
- Whether IPRES and CSS contributions can be paid electronically.
- Whether Qonto's approval and bulk-transfer features match the descriptions above; they are drawn from general product knowledge, not a sourced feature page.
