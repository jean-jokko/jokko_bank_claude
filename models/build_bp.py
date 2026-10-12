"""Tabax business plan: a formula-driven Excel model (5 years, monthly)."""
import datetime, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as CL
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.worksheet.datavalidation import DataValidation

OUT = sys.argv[1]
EQUITY = [float(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else [900e6, 2000e6, 3000e6]

wb = Workbook()
FONT = "Arial"
BLUE, GREEN, BLACK, WHITE, GREY = "0000FF", "008000", "000000", "FFFFFF", "595959"
F = lambda bold=False, color=BLACK, size=10, italic=False: Font(name=FONT, bold=bold, color=color, size=size, italic=italic)
FILL = lambda c: PatternFill("solid", fgColor=c)
IN_FILL, HEAD_FILL, SEC_FILL, TOT_FILL, KEY_FILL = FILL("FFF6D5"), FILL("1F2A44"), FILL("DCE6F2"), FILL("F2F2F2"), FILL("FFFF00")
NUM = '#,##0;(#,##0);"-"'
NUM1 = '#,##0.0;(#,##0.0);"-"'
PCT = '0.0%;(0.0%);"-"'
PCT2 = '0.00%;(0.00%);"-"'
DATEF = 'mmm-yy'
THIN = Side(style="thin", color="BFBFBF")
NM, C0 = 60, 5
COLS = [CL(C0 + i) for i in range(NM)]
FC, LC = COLS[0], COLS[-1]


def name(nm, ref):
    wb.defined_names[nm] = DefinedName(nm, attr_text=ref)


def style(cell, fmt=None, bold=False, color=BLACK, fill=None, italic=False, align=None, wrap=False):
    cell.font = F(bold=bold, color=color, italic=italic)
    if fmt:
        cell.number_format = fmt
    if fill:
        cell.fill = fill
    if align or wrap:
        cell.alignment = Alignment(horizontal=align, vertical="top" if wrap else None, wrap_text=wrap)


def title(ws, text, desc):
    ws["A1"] = text
    ws["A1"].font = F(bold=True, size=14)
    ws["A2"] = desc
    ws["A2"].font = F(italic=True, color=GREY)


# =====================================================================================
# ASSUMPTIONS
# =====================================================================================
A = wb.active
A.title = "Assumptions"
title(A, "Assumptions and hypotheses", "Every blue cell on a cream background is an input. Change it and the whole model updates. Amounts in FCFA unless stated. Column D is the value the model uses.")
A["B4"] = "Scenario (1 = Prudent, 2 = Base, 3 = Ambitious)"
A["D4"] = 2
style(A["B4"], bold=True)
style(A["D4"], fmt="0", bold=True, color=BLUE, fill=KEY_FILL, align="center")
A["E4"] = '=CHOOSE(Scenario,"Prudent","Base","Ambitious")'
style(A["E4"], bold=True)
A["I4"] = "Rows with Prudent / Base / Ambitious values switch with this cell."
style(A["I4"], italic=True, color=GREY)
name("Scenario", "'Assumptions'!$D$4")
dv = DataValidation(type="list", formula1='"1,2,3"', allow_blank=False)
A.add_data_validation(dv)
dv.add("D4")
for col, w in {"A": 2, "B": 52, "C": 16, "D": 15, "E": 15, "F": 15, "G": 15, "H": 15, "I": 90}.items():
    A.column_dimensions[col].width = w
arow = [6]


def a_sec(text, kind="scalar"):
    r = arow[0] + 1
    A.cell(r, 2, text)
    heads = ["Unit", "Value used", "Prudent", "Base", "Ambitious", "", "Source / note"] if kind == "scalar" else \
        ["Unit", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Source / note"]
    for j, h in enumerate(heads):
        A.cell(r, 3 + j, h)
    for j in range(2, 10):
        c = A.cell(r, j)
        c.font = F(bold=True, color=WHITE)
        c.fill = HEAD_FILL
    arow[0] = r + 1


def a_in(nm, label, value, unit, fmt=NUM, note="", scen=None):
    r = arow[0]
    A.cell(r, 2, label).font = F()
    A.cell(r, 3, unit).font = F(color=GREY)
    if scen:
        A.cell(r, 4, f"=CHOOSE(Scenario,E{r},F{r},G{r})")
        style(A.cell(r, 4), fmt=fmt)
        for j, v in enumerate(scen):
            style(A.cell(r, 5 + j, v), fmt=fmt, color=BLUE, fill=IN_FILL)
    else:
        style(A.cell(r, 4, value), fmt=fmt, color=BLUE, fill=IN_FILL)
    A.cell(r, 9, note).font = F(color=GREY)
    name(nm, f"'Assumptions'!$D${r}")
    arow[0] += 1
    return r


def a_arr(nm, label, values, unit, fmt=NUM, note=""):
    r = arow[0]
    A.cell(r, 2, label).font = F()
    A.cell(r, 3, unit).font = F(color=GREY)
    for j, v in enumerate(values):
        style(A.cell(r, 4 + j, v), fmt=fmt, color=BLUE, fill=IN_FILL)
    A.cell(r, 9, note).font = F(color=GREY)
    name(nm, f"'Assumptions'!$D${r}:$H${r}")
    arow[0] += 1
    return r


a_sec("1. General")
a_in("Start_Date", "Model start (month 1)", datetime.date(2027, 1, 1), "date", "dd mmm yyyy", "First month of the plan. Company set-up, licence file and product build start here.")
a_in("FX_EUR", "FCFA per euro", 655.957, "FCFA", "#,##0.000", "Fixed parity CFA franc / euro (BCEAO).")
a_in("FX_USD", "FCFA per US dollar", 580, "FCFA", NUM, "Planning rate, used for vendor prices quoted in USD.")
a_in("Tax_Rate", "Corporate income tax rate", 0.30, "%", PCT, "Senegal CIT 30%. Simplification: losses carried forward without limit (Senegal allows 3 years). Minimum tax and the 17% TAF on financial services are not modelled.")
a_in("Salary_Raise", "Annual pay rise (from year 2)", 0.05, "% / year", PCT, "Applied to every salary each new year.")
a_in("Contingency_Pct", "Contingency on fixed costs", 0.05, "%", PCT, "Same 5% as the cost breakdown.")

a_sec("2. Timing (month numbers, 1 = first month of the model)")
a_in("Launch_SN", "Commercial launch, Senegal", 5, "month #", "0", "After partner bank integration and card programme set-up (business account with IBAN via the partner bank).")
a_in("Launch_CI", "Commercial launch, Côte d'Ivoire", 19, "month #", "0", "Year 2, as in the Senegal launch plan.")
a_in("Office_Start", "Dakar office opens (coworking before)", 4, "month #", "0", "")
a_in("CI_Office_Start", "Abidjan office / coworking opens", 13, "month #", "0", "")
a_in("PayLinks_Start", "Payment links go live", 18, "month #", "0", "'Bientôt' feature in the app.")
a_in("EmpAcc_Start", "Employee salary accounts go live", 9, "month #", "0", "Free account and card for client employees.")
a_in("Own_Funding_Month", "Own SFD funds the loan book from", 37, "month #", "0", "Before this month the partner SFD funds loans and Tabax keeps a share of the margin.")
a_in("SFD_Acq_Month", "Own SFD licence or acquisition paid", 36, "month #", "0", "")
a_in("Licence_SN_Month", "Payment licence capital paid in, Senegal", 12, "month #", "0", "EP licence: 100M FCFA minimum capital per country.")
a_in("Licence_CI_Month", "Payment licence capital paid in, Côte d'Ivoire", 30, "month #", "0", "")
a_in("Collateral_Month", "Card programme collateral at partner bank", 4, "month #", "0", "")
a_in("Bank_Setup_Month", "Partner bank set-up fee paid, Senegal", 2, "month #", "0", "")
a_in("CI_Bank_Setup_Month", "Partner bank set-up fee paid, Côte d'Ivoire", 16, "month #", "0", "")
a_in("Proc_Setup_Month", "Card processor set-up fee paid", 3, "month #", "0", "")
a_in("Proc_Min_Start", "Card processor monthly minimum starts", 5, "month #", "0", "")
a_in("Cloud_Start", "Cloud hosting starts", 2, "month #", "0", "")
a_in("SFD_Setup_Month", "Partner SFD integration fee paid", 9, "month #", "0", "")
a_in("CI_Company_Month", "Côte d'Ivoire subsidiary created", 13, "month #", "0", "")
a_in("Licence_File_SN_Months", "Senegal licence file: months of work from month 1", 9, "months", "0", "Counsel and consultants spread over this period.")
a_in("CI_Licence_File_Start", "Côte d'Ivoire licence file starts", 13, "month #", "0", "")
a_in("Licence_File_CI_Months", "Côte d'Ivoire licence file: months of work", 12, "months", "0", "")

a_sec("3. Client acquisition (sales and marketing)")
a_in("Rep_Productivity", "New clients signed per field sales rep per month", None, "clients", NUM1, "Rep counts come from the hiring plan. A rep sells from the month after joining. Senegal B2B field sales benchmark to validate in the pilot.", scen=(7, 10, 13))
a_in("CI_Productivity", "Côte d'Ivoire rep productivity vs Senegal", 0.9, "x", "0.00", "Slightly lower at first: new market, brand unknown.")
a_in("Partner_Base_SN", "Partner channel, Senegal: clients a month at launch", None, "clients", NUM1, "Accountants, payroll software, chambers of commerce.", scen=(6, 10, 14))
a_in("Partner_Base_CI", "Partner channel, Côte d'Ivoire: clients a month at launch", None, "clients", NUM1, "", scen=(4, 6, 9))
a_in("Partner_Growth", "Partner channel monthly growth", 0.06, "% / month", PCT, "")
a_in("Partner_Cap_SN", "Partner channel cap, Senegal", 80, "clients / month", NUM, "")
a_in("Partner_Cap_CI", "Partner channel cap, Côte d'Ivoire", 60, "clients / month", NUM, "")
a_in("CAC_Digital", "Digital ads cost per signed client", None, "FCFA", NUM, "Media spend only. Meta leads 600–2,800 FCFA; lead-to-client conversion assumed 2–4%.", scen=(100000, 75000, 55000))
a_in("Mix_Petite", "Share of new clients on Petite (1–10 staff)", 0.60, "%", PCT, "From Business model v2. The three shares must add up to 100% (see check on the Dashboard).")
a_in("Mix_Moyenne", "Share of new clients on Moyenne (11–50 staff)", 0.30, "%", PCT, "")
a_in("Mix_Grande", "Share of new clients on Grande (51+ staff)", 0.10, "%", PCT, "")
a_in("Churn_Petite", "Monthly churn, Petite", None, "% / month", PCT2, "Small companies leave or close more often.", scen=(0.03, 0.02, 0.015))
a_in("Churn_Moyenne", "Monthly churn, Moyenne", None, "% / month", PCT2, "", scen=(0.02, 0.0125, 0.01))
a_in("Churn_Grande", "Monthly churn, Grande", None, "% / month", PCT2, "", scen=(0.015, 0.0075, 0.005))
a_in("Referral_Fee", "Referral fee per partner-channel client", 25000, "FCFA", NUM, "Paid to accountants and payroll software partners (cost breakdown).")
a_in("Rep_Transport", "Field sales transport allowance per rep", 75000, "FCFA / month", NUM, "50–100k FCFA (cost breakdown).")

a_sec("4. Pricing and fees")
a_in("Price_Petite", "Subscription, Petite (1–10 staff)", 9900, "FCFA / month", NUM, "Business model v2.")
a_in("Price_Moyenne", "Subscription, Moyenne (11–50 staff)", 29900, "FCFA / month", NUM, "Business model v2.")
a_in("Price_Grande", "Subscription, Grande (51+ staff)", 79900, "FCFA / month", NUM, "Business model v2.")
a_in("Price_Increase", "Annual price increase", 0.0, "% / year", PCT, "")
a_in("Free_Months", "Free months for every new client", 3, "months", "0", "Launch offer: first 3 months free. Use 0 to 6.")
a_in("Annual_Share", "Share of clients paying yearly", 0.30, "%", PCT, "")
a_in("Annual_Free", "Months free on yearly billing", 2, "months", "0", "Yearly price = 10 months.")
a_in("Card_Fee", "Physical card fee (one-off; first card free)", 5000, "FCFA", NUM, "Business model v2.")
a_in("FX_Fee", "Fee on card spending in foreign currencies", 0.01, "%", PCT, "Business model v2. Card spending in FCFA is free.")
a_in("Interchange_Share", "Interchange share received on FCFA card spending", None, "%", PCT2, "Placeholder: WAEMU interchange levels are not published. Negotiate with the partner bank.", scen=(0.003, 0.005, 0.007))
a_in("Deposit_Share", "Share of bank income on client balances", None, "% / year", PCT2, "Negotiated with the partner bank; the largest non-credit lever.", scen=(0.01, 0.015, 0.02))
a_in("Overage_Fee", "Fee per supplier payout above the allowance", 100, "FCFA", NUM, "Allowance: 50 / 200 / 1,000 payouts a month. Salaries always unlimited.")
a_in("PL_Fee", "Payment links: fee on mobile money collections", 0.01, "%", PCT, "")
a_in("PL_Cost", "Payment links: operator and aggregator cost", 0.007, "%", PCT2, "0.5–1.5% (cost breakdown).")
a_in("PL_Momo_Share", "Payment links: share collected by mobile money", 0.70, "%", PCT, "The rest by card or transfer, free.")
a_in("PL_Adoption", "Payment links: share of clients using them (at maturity)", 0.25, "%", PCT, "")
a_in("PL_Ramp", "Payment links: months to reach maturity", 12, "months", "0", "")

a_sec("5. Usage per client (monthly, by plan)")
a_in("Spend_Dom_Petite", "Card spending in FCFA, Petite", 300000, "FCFA / month", NUM, "Business model v2 (assumption).")
a_in("Spend_Dom_Moyenne", "Card spending in FCFA, Moyenne", 800000, "FCFA / month", NUM, "")
a_in("Spend_Dom_Grande", "Card spending in FCFA, Grande", 2500000, "FCFA / month", NUM, "")
a_in("Spend_For_Petite", "Card spending in foreign currencies, Petite", 300000, "FCFA / month", NUM, "Ads, software subscriptions, travel.")
a_in("Spend_For_Moyenne", "Card spending in foreign currencies, Moyenne", 1200000, "FCFA / month", NUM, "")
a_in("Spend_For_Grande", "Card spending in foreign currencies, Grande", 3500000, "FCFA / month", NUM, "")
a_in("Balance_Petite", "Average balance, Petite", 3000000, "FCFA", NUM, "")
a_in("Balance_Moyenne", "Average balance, Moyenne", 10000000, "FCFA", NUM, "")
a_in("Balance_Grande", "Average balance, Grande", 40000000, "FCFA", NUM, "")
a_in("Emp_Petite", "Employees, Petite", 5, "people", NUM, "")
a_in("Emp_Moyenne", "Employees, Moyenne", 25, "people", NUM, "")
a_in("Emp_Grande", "Employees, Grande", 120, "people", NUM, "")
a_in("Supplier_Petite", "Supplier payouts a month, Petite", 10, "payouts", NUM, "")
a_in("Supplier_Moyenne", "Supplier payouts a month, Moyenne", 40, "payouts", NUM, "")
a_in("Supplier_Grande", "Supplier payouts a month, Grande", 150, "payouts", NUM, "")
a_in("Overage_Petite", "Payouts above the allowance, Petite", 0, "payouts", NUM, "")
a_in("Overage_Moyenne", "Payouts above the allowance, Moyenne", 5, "payouts", NUM, "")
a_in("Overage_Grande", "Payouts above the allowance, Grande", 40, "payouts", NUM, "")
a_in("Cards_New_Petite", "Physical cards ordered at sign-up, Petite", 1, "cards", NUM, "")
a_in("Cards_New_Moyenne", "Physical cards ordered at sign-up, Moyenne", 3, "cards", NUM, "")
a_in("Cards_New_Grande", "Physical cards ordered at sign-up, Grande", 8, "cards", NUM, "")
a_in("Cards_Act_Petite", "Active cards (physical + virtual), Petite", 2, "cards", NUM, "")
a_in("Cards_Act_Moyenne", "Active cards (physical + virtual), Moyenne", 6, "cards", NUM, "")
a_in("Cards_Act_Grande", "Active cards (physical + virtual), Grande", 15, "cards", NUM, "")
a_in("PL_Coll_Petite", "Payment link collections, Petite (users)", 800000, "FCFA / month", NUM, "")
a_in("PL_Coll_Moyenne", "Payment link collections, Moyenne (users)", 3000000, "FCFA / month", NUM, "")
a_in("PL_Coll_Grande", "Payment link collections, Grande (users)", 10000000, "FCFA / month", NUM, "")
a_in("Avg_Salary", "Average monthly salary paid through Tabax", 200000, "FCFA", NUM, "SME average; the formal-sector average is higher (about 380,000 FCFA).")
a_in("Wallet_Share", "Share of salaries paid to mobile money wallets", 0.60, "%", PCT, "Senegal: 20.1% of adults receive wages on a phone vs 12.0% in an account (Global Findex 2025).")
a_in("EmpAcc_Adoption", "Employees who open a Tabax salary account", 0.20, "%", PCT, "")

a_sec("6. Cost to serve (variable costs)")
a_in("Bank_Fee", "Partner bank fee per business account", 3000, "FCFA / month", NUM, "2,000–5,000 FCFA (estimate; replace with the term sheet).")
a_in("KYB_Cost", "Company checks at onboarding (KYB)", 12000, "FCFA / company", NUM, "€8–30 per company (cost breakdown).")
a_in("KYC_Cost", "ID check per person", 900, "FCFA", NUM, "Sumsub incl. AML screening, about €1.2–1.6.")
a_in("KYC_Persons", "People checked per new company", 2, "people", NUM, "Directors and beneficial owners.")
a_in("Card_Proc_Fee", "Card processing per active card", 1000, "FCFA / month", NUM, "€0.76–2.29 (estimate; processor quote needed).")
a_in("Card_Prod_Cost", "Physical card printed and delivered", 4500, "FCFA", NUM, "3,000–6,000 FCFA.")
a_in("Scheme_Rate", "Visa / Mastercard cross-border fees", 0.005, "% of foreign spending", PCT2, "About 0.5% (assumption).")
a_in("Fraud_Rate", "Fraud and chargebacks", 0.0015, "% of card spending", PCT2, "0.1–0.3%.")
a_in("Wallet_Payout_Cost", "Cost of a salary paid to a wallet", 0.0025, "% of amount", PCT2, "Estimate via PI-SPI / aggregator; Wave charges businesses 1% sender-pays. Quote needed.")
a_in("Bank_Payout_Cost", "Cost of a salary paid to a bank account", 100, "FCFA / payout", NUM, "PI-SPI / interbank transfer (estimate).")
a_in("Supplier_Payout_Cost", "Cost of a supplier payout", 100, "FCFA / payout", NUM, "Blend of PI-SPI, bank and wallet (estimate).")
a_in("Notif_Cost", "SMS, WhatsApp and support tools per client", 400, "FCFA / month", NUM, "")
a_in("Emp_Notif", "Messages per employee account", 50, "FCFA / month", NUM, "")
a_in("EmpAcc_Cost", "Processing per employee account", 150, "FCFA / month", NUM, "About €0.23 (cost breakdown).")

a_sec("7. Credit (lender of record: partner SFD, later own SFD)")
a_in("Credit_Mult", "Credit volume multiplier", None, "x", "0.00", "Scales every product's uptake.", scen=(0.6, 1.0, 1.4))
a_in("CoR_Mult", "Credit losses multiplier", None, "x", "0.00", "Scales every product's cost of risk.", scen=(1.5, 1.0, 0.8))
a_in("Credit_Ramp", "Months for a product to reach full uptake", 12, "months", "0", "")
a_in("Start_Factoring", "Factoring: start month", 12, "month #", "0", "Lowest risk: the debtor pays the invoice.")
a_in("Uptake_Factoring", "Factoring: share of active clients using it", 0.05, "%", PCT, "")
a_in("Avg_Factoring", "Factoring: average outstanding per user", 8000000, "FCFA", NUM, "80–90% of invoices, 30–90 days.")
a_in("Yield_Factoring", "Factoring: yield", 0.23, "% / year", PCT, "0.063% a day = 23% a year, under the 24% SFD usury cap.")
a_in("CoR_Factoring", "Factoring: cost of risk", 0.015, "% / year", PCT2, "")
a_in("Start_Bridge", "Payroll bridge: start month", 12, "month #", "0", "")
a_in("Uptake_Bridge", "Payroll bridge: share of active clients", 0.03, "%", PCT, "")
a_in("Avg_Bridge", "Payroll bridge: average outstanding", 3000000, "FCFA", NUM, "Up to one month of payroll, 45 days max.")
a_in("Yield_Bridge", "Payroll bridge: yield", 0.23, "% / year", PCT, "")
a_in("CoR_Bridge", "Payroll bridge: cost of risk", 0.02, "% / year", PCT2, "")
a_in("Start_Line", "Credit line: start month", 15, "month #", "0", "After 6 months of transactions.")
a_in("Uptake_Line", "Credit line: share of active clients", 0.08, "%", PCT, "")
a_in("Avg_Line", "Credit line: average drawn", 1500000, "FCFA", NUM, "5–30% of monthly inflows.")
a_in("Yield_Line", "Credit line: yield", 0.23, "% / year", PCT, "")
a_in("CoR_Line", "Credit line: cost of risk", 0.04, "% / year", PCT2, "")
a_in("Start_Term", "Equipment / term loans: start month", 20, "month #", "0", "")
a_in("Uptake_Term", "Term loans: share of active clients", 0.02, "%", PCT, "")
a_in("Avg_Term", "Term loans: average outstanding", 10000000, "FCFA", NUM, "1–50M FCFA, 6–24 months.")
a_in("Yield_Term", "Term loans: yield", 0.22, "% / year", PCT, "")
a_in("CoR_Term", "Term loans: cost of risk", 0.03, "% / year", PCT2, "")
a_in("Start_Advance", "Salary advances: start month", 12, "month #", "0", "Retention product, not a profit centre.")
a_in("Usage_Advance", "Salary advances: share of employee accounts with an advance", 0.10, "%", PCT, "")
a_in("Avg_Advance", "Salary advances: average outstanding", 50000, "FCFA", NUM, "Up to 50% of pay already earned.")
a_in("Yield_Advance", "Salary advances: yield", 0.23, "% / year", PCT, "")
a_in("CoR_Advance", "Salary advances: cost of risk", 0.015, "% / year", PCT2, "")
a_in("CoF", "Cost of funds", 0.09, "% / year", PCT, "8–10% (DFI lines, local debt).")
a_in("Servicing", "External servicing and collections", 0.01, "% / year", PCT, "Credit staff are in the hiring plan.")
a_in("Partner_Share", "Tabax share of the net margin while the partner SFD funds", 0.50, "%", PCT, "Negotiated; Tabax provides first-loss cover.")
a_in("First_Loss", "First-loss cash reserve (partner phase)", 0.10, "% of book", PCT, "")
a_in("Capital_Ratio", "Equity needed per FCFA lent (own SFD phase)", 0.15, "% of book", PCT, "The rest funded by debt lines (not modelled in the P&L except the cost of funds).")

a_sec("8. Staff charges (Senegal)")
a_in("IPRES_Rate", "IPRES pension, employer", 0.084, "%", PCT, "Up to the ceiling below.")
a_in("IPRES_Cap", "IPRES ceiling", 432000, "FCFA / month", NUM, "")
a_in("Cadre_Rate", "IPRES managers' supplement", 0.036, "%", PCT, "On the slice between the two ceilings.")
a_in("Cadre_Cap", "IPRES managers' ceiling", 1296000, "FCFA / month", NUM, "")
a_in("CSS_Rate", "CSS family allowances + work accidents", 0.08, "%", PCT, "7% + 1%, up to the ceiling below.")
a_in("CSS_Cap", "CSS ceiling", 63000, "FCFA / month", NUM, "")
a_in("IPM_Rate", "IPM health fund, employer", 0.03, "%", PCT, "")
a_in("IPM_Cap", "IPM ceiling", 250000, "FCFA / month", NUM, "")
a_in("CFCE_Rate", "CFCE payroll tax", 0.03, "%", PCT, "On the whole salary.")
a_in("Thirteenth", "13th month", 1, "months / year", "0", "Spread monthly.")
a_in("Transport_Allow", "Transport allowance", 25000, "FCFA / month", NUM, "")
a_in("Health_TopUp", "Private health top-up", 15000, "FCFA / month", NUM, "")
a_in("Laptop_Cost", "Laptop and equipment per new hire (capex)", 600000, "FCFA", NUM, "")
a_in("Phone_Cost", "Phone and data plan per employee", 15000, "FCFA / month", NUM, "")
a_in("Tools_USD", "Software tools per employee", 40, "USD / month", NUM, "Workspace, code hosting, design, monitoring.")
a_in("Dep_Months", "Depreciation period for capex", 36, "months", "0", "")

a_sec("9. Fixed costs by year", kind="arr")
A.cell(arow[0], 2, "Office and equipment").font = F(bold=True)
arow[0] += 1
r_cw = arow[0]
A.cell(r_cw, 2, "Coworking before the office opens").font = F()
A.cell(r_cw, 3, "FCFA / month").font = F(color=GREY)
style(A.cell(r_cw, 4, 800000), fmt=NUM, color=BLUE, fill=IN_FILL)
A.cell(r_cw, 9, "8 desks × 100k FCFA (Impact Hub / Jokkolabs: 70–150k a desk).").font = F(color=GREY)
name("Coworking_Monthly", f"'Assumptions'!$D${r_cw}")
arow[0] += 1
a_arr("Office_m2", "Dakar office surface", [150, 250, 350, 450, 550], "m²", NUM, "Point E / Mermoz.")
a_arr("Office_Price_Arr", "Office rent and charges per m²", [10500, 10500, 11000, 11500, 12000], "FCFA / m² / month", NUM, "8,500 rent + 2,000 charges.")
a_arr("Electricity", "Electricity (Senelec)", [300000, 450000, 600000, 750000, 900000], "FCFA / month", NUM, "From the office opening.")
a_arr("Internet", "Internet (fibre + dedicated line)", [440000, 440000, 600000, 700000, 800000], "FCFA / month", NUM, "")
a_arr("Cleaning", "Cleaning, security, supplies", [250000, 350000, 450000, 550000, 650000], "FCFA / month", NUM, "")
a_arr("Abidjan_Office", "Abidjan office", [0, 1200000, 3000000, 3500000, 4000000], "FCFA / month", NUM, "Coworking in year 2, then 120 m² in Cocody / Plateau.")
a_arr("Fitout", "Office fit-out, furniture, generator (capex)", [13300000, 5000000, 6000000, 5000000, 5000000], "FCFA / year", NUM, "Paid at the office opening in year 1, then in the first month of each year.")
A.cell(arow[0], 2, "Technology").font = F(bold=True)
arow[0] += 1
a_arr("Ledger_USD", "Core ledger / banking platform", [40000, 60000, 80000, 95000, 110000], "USD / year", NUM, "Open-source hosted + support, or regional vendor.")
a_arr("Cloud_USD", "Cloud hosting", [3000, 5000, 8000, 10000, 12000], "USD / month", NUM, "No AWS/GCP region in WAEMU; CDP authorisation for data abroad.")
a_arr("Monitoring_USD", "Transaction monitoring and sanctions screening", [6000, 15000, 30000, 40000, 50000], "USD / year", NUM, "")
a_arr("Backoffice_USD", "Back-office and internal tools", [12000, 18000, 24000, 30000, 36000], "USD / year", NUM, "")
a_arr("Freelance", "Freelance QA, DevOps on-call, design help", [15700000, 19700000, 11800000, 11800000, 11800000], "FCFA / year", NUM, "")
a_arr("Security_USD", "Penetration tests and PCI DSS", [25000, 45000, 45000, 50000, 55000], "USD / year", NUM, "")
a_arr("Proc_Min_USD", "Card processor monthly minimum", [5000, 5000, 7500, 10000, 12000], "USD / month", NUM, "Tabax pays the higher of this minimum and the per-card fees.")
r_proc = arow[0]
A.cell(r_proc, 2, "Card processor set-up fee (one-off)").font = F()
A.cell(r_proc, 3, "USD").font = F(color=GREY)
style(A.cell(r_proc, 4, 50000), fmt=NUM, color=BLUE, fill=IN_FILL)
A.cell(r_proc, 9, "USD 25–75k (estimate; quote needed).").font = F(color=GREY)
name("Proc_Setup_USD", f"'Assumptions'!$D${r_proc}")
arow[0] += 1
A.cell(arow[0], 2, "Bank and SFD partners").font = F(bold=True)
arow[0] += 1
for nm, label, v, note in [("Bank_Setup_SN", "Partner bank set-up and card programme, Senegal (one-off)", 15000000, "No public price; replace with the term sheet."),
                           ("Bank_Setup_CI", "Partner bank set-up, Côte d'Ivoire (one-off)", 15000000, ""),
                           ("SFD_Setup", "Partner SFD integration and legal set-up (one-off)", 5000000, "")]:
    r = arow[0]
    A.cell(r, 2, label).font = F()
    A.cell(r, 3, "FCFA").font = F(color=GREY)
    style(A.cell(r, 4, v), fmt=NUM, color=BLUE, fill=IN_FILL)
    A.cell(r, 9, note).font = F(color=GREY)
    name(nm, f"'Assumptions'!$D${r}")
    arow[0] += 1
a_arr("Bank_Min_SN", "Partner bank platform minimum, Senegal", [1500000, 1500000, 2000000, 2000000, 2000000], "FCFA / month", NUM, "From the Senegal launch.")
a_arr("Bank_Min_CI", "Partner bank platform minimum, Côte d'Ivoire", [0, 1500000, 2000000, 2000000, 2000000], "FCFA / month", NUM, "From the Côte d'Ivoire launch.")
a_arr("SFD_Annual", "Partner SFD running fees", [0, 3000000, 3000000, 3000000, 3000000], "FCFA / year", NUM, "")
A.cell(arow[0], 2, "Legal, regulatory and audit").font = F(bold=True)
arow[0] += 1
for nm, label, v, note in [("Company_Setup_SN", "Company set-up, Senegal (one-off, month 1)", 2500000, "1.5–3M FCFA excluding capital."),
                           ("Company_Setup_CI", "Company set-up, Côte d'Ivoire (one-off)", 3000000, ""),
                           ("Licence_File_SN", "Payment licence file, Senegal: counsel and consultants", 40000000, "30–80M FCFA per file (estimate; key gap)."),
                           ("Licence_File_CI", "Payment licence file, Côte d'Ivoire", 50000000, "")]:
    r = arow[0]
    A.cell(r, 2, label).font = F()
    A.cell(r, 3, "FCFA").font = F(color=GREY)
    style(A.cell(r, 4, v), fmt=NUM, color=BLUE, fill=IN_FILL)
    A.cell(r, 9, note).font = F(color=GREY)
    name(nm, f"'Assumptions'!$D${r}")
    arow[0] += 1
a_arr("SFD_Project", "SFD project (licence or acquisition due diligence)", [0, 30000000, 20000000, 0, 0], "FCFA / year", NUM, "")
a_arr("Legal_Counsel", "Ongoing legal counsel", [1000000, 1500000, 2000000, 2500000, 3000000], "FCFA / month", NUM, "")
a_arr("Auditor", "Statutory auditor", [5000000, 15000000, 25000000, 30000000, 35000000], "FCFA / year", NUM, "10–25M FCFA once licensed; two entities from year 2.")
a_arr("Accountant_Ext", "External chartered accountant and tax adviser", [300000, 600000, 800000, 900000, 1000000], "FCFA / month", NUM, "")
a_arr("AML_Audit", "Independent AML audit (mandatory)", [0, 8000000, 12000000, 14000000, 16000000], "FCFA / year", NUM, "")
a_arr("Data_Protection", "Data-protection filings (CDP, ARTCI)", [3500000, 3000000, 1500000, 1500000, 1500000], "FCFA / year", NUM, "")
a_arr("Insurance_USD", "Insurance: professional liability, cyber, directors", [20000, 25000, 35000, 45000, 55000], "USD / year", NUM, "")
A.cell(arow[0], 2, "Sales and marketing (non-staff)").font = F(bold=True)
arow[0] += 1
a_arr("Digital_SN", "Digital ads budget, Senegal", [1310000, 2620000, 3940000, 4590000, 5250000], "FCFA / month", NUM, "From the Senegal launch. Drives digital clients through the cost per client above.")
a_arr("Digital_CI", "Digital ads budget, Côte d'Ivoire", [0, 1310000, 2620000, 3280000, 3940000], "FCFA / month", NUM, "From the Côte d'Ivoire launch.")
a_arr("Brand_PR", "Brand, website, launch events, PR", [16400000, 5250000, 6560000, 6560000, 6560000], "FCFA / year", NUM, "")
a_arr("Events", "Events, sponsorships, sales materials", [9840000, 19700000, 29500000, 36100000, 42600000], "FCFA / year", NUM, "")
A.cell(arow[0], 2, "Other").font = F(bold=True)
arow[0] += 1
a_arr("Recruitment", "Recruitment fees (executive search, job boards)", [13300000, 21700000, 4000000, 5000000, 5000000], "FCFA / year", NUM, "Search firms charge about 30% of annual gross.")
a_arr("Travel", "Travel (Dakar–Abidjan, regulators, partners)", [5250000, 13100000, 16400000, 19700000, 23000000], "FCFA / year", NUM, "")
a_arr("Misc", "Company bank fees and miscellaneous", [300000, 450000, 600000, 700000, 800000], "FCFA / month", NUM, "")

a_sec("10. Cash, capital and funding")
a_in("Opening_Cash", "Cash at month 1 before the first round", 0, "FCFA", NUM, "")
a_in("Licence_Capital_SN", "Payment licence minimum capital, Senegal", 100000000, "FCFA", NUM, "BCEAO: 100M FCFA per country for a payment institution. Kept as restricted cash in this model.")
a_in("Licence_Capital_CI", "Payment licence minimum capital, Côte d'Ivoire", 100000000, "FCFA", NUM, "")
a_in("Card_Collateral", "Card programme collateral at the partner bank", 60000000, "FCFA", NUM, "To quote.")
a_in("Office_Deposit_Months", "Office deposit", 3, "months of rent", "0", "")
a_in("SFD_Acquisition", "Own SFD: licence capital or acquisition", 650000000, "FCFA", NUM, "Unknown; mid-range estimate (≈ €990k).")
a_in("Seed_Month", "Seed round: month", 1, "month #", "0", "")
a_in("Seed_Amount", "Seed round: amount", EQUITY[0], "FCFA", NUM, "Adjust to keep closing cash above zero (see Cash flow).")
a_in("SeriesA_Month", "Series A: month", 15, "month #", "0", "")
a_in("SeriesA_Amount", "Series A: amount", EQUITY[1], "FCFA", NUM, "")
a_in("SeriesB_Month", "Series B: month", 33, "month #", "0", "Funds the own SFD and the credit book's equity.")
a_in("SeriesB_Amount", "Series B: amount", EQUITY[2], "FCFA", NUM, "")
A.freeze_panes = "C6"

# =====================================================================================
# HIRING PLAN (input table)
# =====================================================================================
H = wb.create_sheet("Hiring plan")
title(H, "Hiring plan", "One line per hire or group of identical hires. Edit headcount, start month, end month (leave blank if they stay) and gross salary. Spare lines at the bottom for new roles.")
heads = ["#", "Department", "Role", "Country", "Category", "Headcount", "Start month", "End month", "Gross salary (FCFA / month)", "Manager (Y/N)", "Employer cost per person (FCFA / month)", "Note"]
for j, h in enumerate(heads):
    c = H.cell(4, 1 + j, h)
    c.font = F(bold=True, color=WHITE)
    c.fill = HEAD_FILL
    c.alignment = Alignment(wrap_text=True, vertical="top")
for col, w in {"A": 5, "B": 22, "C": 44, "D": 9, "E": 12, "F": 11, "G": 11, "H": 11, "I": 16, "J": 10, "K": 18, "L": 60}.items():
    H.column_dimensions[col].width = w
H.row_dimensions[4].height = 42
DEPTS = ["Leadership", "Engineering & product", "Compliance & risk", "Credit", "Operations & support", "Sales & partnerships", "Marketing", "Finance & admin"]
HIRES = [
    ("Leadership", "CEO", "SN", "", 1, 1, None, 2500000, "Y", ""),
    ("Leadership", "CTO (also codes)", "SN", "", 1, 1, None, 2500000, "Y", ""),
    ("Leadership", "COO", "SN", "", 1, 1, None, 2000000, "Y", ""),
    ("Leadership", "CFO", "SN", "", 1, 19, None, 2000000, "Y", ""),
    ("Leadership", "Country manager, Abidjan", "CI", "", 1, 13, None, 2800000, "Y", "Hired 6 months before the Côte d'Ivoire launch."),
    ("Engineering & product", "Senior backend developer", "SN", "", 1, 1, None, 1500000, "Y", "Lean team: 3 developers in year 1."),
    ("Engineering & product", "Senior mobile developer (Flutter / React Native)", "SN", "", 1, 1, None, 1500000, "Y", ""),
    ("Engineering & product", "Full-stack web developer", "SN", "", 1, 3, None, 800000, "Y", ""),
    ("Engineering & product", "Product designer (UI/UX)", "SN", "", 1, 1, None, 700000, "Y", ""),
    ("Engineering & product", "Data scientist (credit scoring)", "SN", "", 1, 10, None, 1200000, "Y", "Builds the scoring model before credit starts."),
    ("Engineering & product", "Senior backend developer", "SN", "", 1, 19, None, 1500000, "Y", ""),
    ("Engineering & product", "Full-stack web developer", "SN", "", 1, 19, None, 800000, "Y", ""),
    ("Engineering & product", "Product manager", "SN", "", 1, 25, None, 1300000, "Y", ""),
    ("Engineering & product", "DevOps / security engineer", "SN", "", 1, 31, None, 1200000, "Y", ""),
    ("Engineering & product", "Senior mobile developer", "SN", "", 1, 43, None, 1500000, "Y", ""),
    ("Engineering & product", "Senior backend developer", "SN", "", 1, 43, None, 1500000, "Y", ""),
    ("Compliance & risk", "Head of compliance / AML officer", "SN", "", 1, 3, None, 1500000, "Y", "Named compliance officer needed for the licence file."),
    ("Compliance & risk", "Compliance analyst", "SN", "", 1, 7, None, 550000, "Y", ""),
    ("Compliance & risk", "Compliance analyst", "SN", "", 1, 19, None, 550000, "Y", ""),
    ("Compliance & risk", "Compliance officer, Abidjan", "CI", "", 1, 16, None, 1000000, "Y", ""),
    ("Compliance & risk", "Compliance analyst", "SN", "", 1, 31, None, 550000, "Y", ""),
    ("Compliance & risk", "Compliance analyst", "SN", "", 1, 43, None, 550000, "Y", ""),
    ("Credit", "Credit risk manager", "SN", "", 1, 7, None, 1200000, "Y", "Ready for credit at month 12."),
    ("Credit", "Credit analyst", "SN", "", 1, 19, None, 500000, "Y", ""),
    ("Credit", "Collections agent (incl. variable pay)", "SN", "", 2, 19, None, 300000, "N", ""),
    ("Credit", "Credit analyst", "SN", "", 2, 31, None, 500000, "Y", ""),
    ("Credit", "Collections agent (incl. variable pay)", "SN", "", 1, 31, None, 300000, "N", ""),
    ("Credit", "Credit analyst", "SN", "", 1, 43, None, 500000, "Y", ""),
    ("Credit", "Collections agent (incl. variable pay)", "SN", "", 2, 43, None, 300000, "N", ""),
    ("Operations & support", "KYC / onboarding agent", "SN", "", 2, 4, None, 275000, "N", ""),
    ("Operations & support", "Customer support agent", "SN", "", 1, 4, None, 200000, "N", ""),
    ("Operations & support", "KYC / onboarding agent", "SN", "", 1, 19, None, 275000, "N", ""),
    ("Operations & support", "Customer support agent", "SN", "", 3, 19, None, 200000, "N", ""),
    ("Operations & support", "KYC and support agent, Abidjan", "CI", "", 2, 19, None, 300000, "N", ""),
    ("Operations & support", "Operations manager", "SN", "", 1, 25, None, 900000, "Y", ""),
    ("Operations & support", "KYC / onboarding agent", "SN", "", 2, 31, None, 275000, "N", ""),
    ("Operations & support", "Customer support agent", "SN", "", 2, 31, None, 200000, "N", ""),
    ("Operations & support", "KYC and support agent, Abidjan", "CI", "", 2, 37, None, 300000, "N", ""),
    ("Operations & support", "KYC / onboarding agent", "SN", "", 2, 43, None, 275000, "N", ""),
    ("Operations & support", "Customer support agent", "SN", "", 3, 43, None, 200000, "N", ""),
    ("Sales & partnerships", "Head of sales (incl. 25% bonus)", "SN", "", 1, 2, None, 1750000, "Y", ""),
    ("Sales & partnerships", "Partnerships manager (accountants, payroll software)", "SN", "", 1, 4, None, 900000, "Y", ""),
    ("Sales & partnerships", "Field sales rep (300k fixed + ~100k commission)", "SN", "Sales rep", 2, 4, None, 400000, "N", "Reps drive client acquisition (see Sales & marketing)."),
    ("Sales & partnerships", "Field sales rep", "SN", "Sales rep", 2, 7, None, 400000, "N", ""),
    ("Sales & partnerships", "Field sales rep", "SN", "Sales rep", 4, 19, None, 400000, "N", ""),
    ("Sales & partnerships", "Field sales rep, Abidjan", "CI", "Sales rep", 3, 19, None, 450000, "N", ""),
    ("Sales & partnerships", "Key account manager (Grande clients)", "SN", "", 1, 25, None, 1000000, "Y", ""),
    ("Sales & partnerships", "Field sales rep", "SN", "Sales rep", 4, 31, None, 400000, "N", ""),
    ("Sales & partnerships", "Field sales rep, Abidjan", "CI", "Sales rep", 3, 31, None, 450000, "N", ""),
    ("Sales & partnerships", "Field sales rep", "SN", "Sales rep", 4, 43, None, 400000, "N", ""),
    ("Sales & partnerships", "Field sales rep, Abidjan", "CI", "Sales rep", 3, 43, None, 450000, "N", ""),
    ("Marketing", "Marketing and growth manager", "SN", "", 1, 6, None, 900000, "Y", ""),
    ("Marketing", "Content and community officer", "SN", "", 1, 19, None, 400000, "N", ""),
    ("Finance & admin", "Accountant", "SN", "", 1, 1, None, 400000, "Y", ""),
    ("Finance & admin", "HR / admin assistant", "SN", "", 1, 19, None, 275000, "N", ""),
    ("Finance & admin", "Accountant", "SN", "", 1, 31, None, 400000, "Y", ""),
    ("Engineering & product", "Senior backend developer", "SN", "", 1, 49, None, 1500000, "Y", "Year 5: scale with volumes."),
    ("Compliance & risk", "Compliance analyst", "SN", "", 1, 49, None, 550000, "Y", ""),
    ("Credit", "Credit analyst", "SN", "", 1, 49, None, 500000, "Y", ""),
    ("Credit", "Collections agent (incl. variable pay)", "SN", "", 1, 49, None, 300000, "N", ""),
    ("Operations & support", "KYC / onboarding agent", "SN", "", 2, 49, None, 275000, "N", ""),
    ("Operations & support", "Customer support agent", "SN", "", 3, 49, None, 200000, "N", ""),
    ("Operations & support", "KYC and support agent, Abidjan", "CI", "", 2, 49, None, 300000, "N", ""),
]
SPARE = 20
H0 = 5
HN = H0 + len(HIRES) + SPARE - 1
dv_dep = DataValidation(type="list", formula1='"' + ",".join(DEPTS) + '"', allow_blank=True)
dv_cty = DataValidation(type="list", formula1='"SN,CI"', allow_blank=True)
dv_cat = DataValidation(type="list", formula1='"Sales rep"', allow_blank=True)
dv_yn = DataValidation(type="list", formula1='"Y,N"', allow_blank=True)
for d in (dv_dep, dv_cty, dv_cat, dv_yn):
    H.add_data_validation(d)
for k in range(len(HIRES) + SPARE):
    r = H0 + k
    vals = HIRES[k] if k < len(HIRES) else ("", "", "", "", None, None, None, None, "", "")
    dep, role, cty, cat, hc, st, en, sal, mgr, note = vals
    H.cell(r, 1, k + 1).font = F(color=GREY)
    for j, v in enumerate([dep, role, cty, cat, hc, st, en, sal, mgr]):
        c = H.cell(r, 2 + j, v)
        style(c, fmt=NUM if j in (4, 7) else ("0" if j in (5, 6) else None), color=BLUE, fill=IN_FILL)
    H.cell(r, 11, f'=IF(I{r}="",0,I{r}+IPRES_Rate*MIN(I{r},IPRES_Cap)+IF(J{r}="Y",Cadre_Rate*MAX(0,MIN(I{r},Cadre_Cap)-IPRES_Cap),0)'
                  f'+CSS_Rate*MIN(I{r},CSS_Cap)+IPM_Rate*MIN(I{r},IPM_Cap)+CFCE_Rate*I{r}+I{r}*Thirteenth/12+Transport_Allow+Health_TopUp)')
    style(H.cell(r, 11), fmt=NUM)
    H.cell(r, 12, note).font = F(color=GREY)
dv_dep.add(f"B{H0}:B{HN}")
dv_cty.add(f"D{H0}:D{HN}")
dv_cat.add(f"E{H0}:E{HN}")
dv_yn.add(f"J{H0}:J{HN}")
H.cell(HN + 2, 2, "Employer cost = gross + IPRES (+ managers' supplement) + CSS + IPM + CFCE + 13th month + transport + private health (rates on Assumptions, section 8). Côte d'Ivoire staff use the same rates as an approximation (CNPS rates differ).").font = F(italic=True, color=GREY)
H.freeze_panes = "D5"
HR = lambda col: f"'Hiring plan'!${col}${H0}:${col}${HN}"


# =====================================================================================
# Time-series sheet helper
# =====================================================================================
class TS:
    def __init__(self, nm, desc):
        self.ws = wb.create_sheet(nm)
        self.name, self.r, self.k = nm, 7, {}
        ws = self.ws
        title(ws, nm, desc)
        for rr, lab in ((3, "Month #"), (4, "Month"), (5, "Year")):
            ws.cell(rr, 1, lab).font = F(bold=True)
        ws["D3"] = "Total / end"
        ws["D3"].font = F(bold=True)
        for i, c in enumerate(COLS):
            ws[f"{c}3"] = 1 if i == 0 else f"={COLS[i - 1]}3+1"
            ws[f"{c}4"] = f"=DATE(YEAR(Start_Date),MONTH(Start_Date)+{c}3-1,1)"
            ws[f"{c}5"] = f"=INT(({c}3-1)/12)+1"
            for rr, fm in ((3, "0"), (4, DATEF), (5, '"Y"0')):
                cell = ws[f"{c}{rr}"]
                cell.number_format = fm
                cell.font = F(bold=True)
                cell.fill = SEC_FILL
                cell.alignment = Alignment(horizontal="center")
            ws.column_dimensions[c].width = 12
        ws.column_dimensions["A"].width = 50
        ws.column_dimensions["B"].width = 16
        ws.column_dimensions["C"].width = 3
        ws.column_dimensions["D"].width = 16
        ws.freeze_panes = "E6"

    def ref(self, key, c):
        return f"'{self.name}'!{c}{self.k[key]}"

    def sec(self, text):
        self.r += 1
        c = self.ws.cell(self.r, 1, text)
        c.font = F(bold=True)
        for col in range(1, C0 + NM):
            self.ws.cell(self.r, col).fill = SEC_FILL
        self.r += 1

    def line(self, key, label, fn, unit="FCFA", fmt=NUM, total="sum", bold=False, color=BLACK, fill=None):
        r = self.r
        self.k[key] = r
        ws = self.ws
        ws.cell(r, 1, label).font = F(bold=bold)
        ws.cell(r, 2, unit).font = F(color=GREY)
        for i, c in enumerate(COLS):
            p = COLS[i - 1] if i > 0 else None
            ws[f"{c}{r}"] = fn(c, p, i)
            style(ws[f"{c}{r}"], fmt=fmt, bold=bold, color=color, fill=fill)
        if total == "sum":
            ws[f"D{r}"] = f"=SUM({FC}{r}:{LC}{r})"
        elif total == "last":
            ws[f"D{r}"] = f"={LC}{r}"
        elif total == "max":
            ws[f"D{r}"] = f"=MAX({FC}{r}:{LC}{r})"
        if total:
            style(ws[f"D{r}"], fmt=fmt, bold=True, fill=TOT_FILL)
        self.r += 1
        return r


def prev(p, r, i, first="0"):
    return first if i == 0 else f"{p}{r}"


def yr(arr, c):
    return f"INDEX({arr},1,{c}$5)"


# =====================================================================================
# STAFF COST
# =====================================================================================
S = TS("Staff", "Headcount and employer cost by month, from the hiring plan. Pay rises each year by the rate on Assumptions.")
S.sec("Headcount by hire line")
hc_rows = []
for k in range(len(HIRES) + SPARE):
    hr = H0 + k
    r = S.line(f"hc{k}", "", lambda c, p, i, hr=hr: f"=IF(AND(N('Hiring plan'!$F${hr})>0,{c}$3>='Hiring plan'!$G${hr},{c}$3<=IF('Hiring plan'!$H${hr}=\"\",999,'Hiring plan'!$H${hr})),'Hiring plan'!$F${hr},0)",
               unit="people", total="max")
    S.ws.cell(r, 1, f"=IF('Hiring plan'!$C${hr}=\"\",\"(spare line {k + 1})\",'Hiring plan'!$C${hr}&\" · \"&'Hiring plan'!$D${hr})")
    hc_rows.append(r)
HC1, HCN = hc_rows[0], hc_rows[-1]
S.sec("Employer cost by hire line")
cost_rows = []
for k in range(len(HIRES) + SPARE):
    hr = H0 + k
    r = S.line(f"cost{k}", "", lambda c, p, i, hr=hr, k=k: f"={c}{hc_rows[k]}*'Hiring plan'!$K${hr}*(1+Salary_Raise)^({c}$5-1)")
    S.ws.cell(r, 1, f"=A{hc_rows[k]}")
    cost_rows.append(r)
CO1, CON = cost_rows[0], cost_rows[-1]
S.sec("Summary")
S.line("hc_total", "Total headcount", lambda c, p, i: f"=SUM({c}{HC1}:{c}{HCN})", unit="people", total="last", bold=True)
S.line("hc_sn", "Headcount, Senegal", lambda c, p, i: f"=SUMIF({HR('D')},\"SN\",{c}{HC1}:{c}{HCN})", unit="people", total="last")
S.line("hc_ci", "Headcount, Côte d'Ivoire", lambda c, p, i: f"=SUMIF({HR('D')},\"CI\",{c}{HC1}:{c}{HCN})", unit="people", total="last")
S.line("reps_sn", "Field sales reps, Senegal", lambda c, p, i: f"=SUMIFS({c}{HC1}:{c}{HCN},{HR('E')},\"Sales rep\",{HR('D')},\"SN\")", unit="people", total="last")
S.line("reps_ci", "Field sales reps, Côte d'Ivoire", lambda c, p, i: f"=SUMIFS({c}{HC1}:{c}{HCN},{HR('E')},\"Sales rep\",{HR('D')},\"CI\")", unit="people", total="last")
S.line("hires", "New hires this month", lambda c, p, i: f"=SUMPRODUCT(--({HR('G')}={c}$3),{HR('F')})", unit="people")
for d in DEPTS:
    S.line(f"dep_{d}", f"Staff cost: {d}", lambda c, p, i, d=d: f"=SUMIF({HR('B')},\"{d}\",{c}{CO1}:{c}{CON})")
S.line("staff_total", "Total staff cost", lambda c, p, i: f"=SUM({c}{CO1}:{c}{CON})", bold=True)

# =====================================================================================
# SALES & MARKETING
# =====================================================================================
M = TS("Sales & marketing", "Client acquisition by channel and country, and the non-staff sales and marketing budget.")
M.sec("Markets open")
M.line("live_sn", "Senegal open (1 = yes)", lambda c, p, i: f"=IF({c}$3>=Launch_SN,1,0)", unit="flag", fmt="0", total=None)
M.line("live_ci", "Côte d'Ivoire open (1 = yes)", lambda c, p, i: f"=IF({c}$3>=Launch_CI,1,0)", unit="flag", fmt="0", total=None)
M.sec("Field sales")
M.line("reps_sn", "Field sales reps, Senegal", lambda c, p, i: f"={S.ref('reps_sn', c)}", unit="people", total="last", color=GREEN)
M.line("reps_ci", "Field sales reps, Côte d'Ivoire", lambda c, p, i: f"={S.ref('reps_ci', c)}", unit="people", total="last", color=GREEN)
M.line("prod_sn", "Productive reps, Senegal (hired before this month)", lambda c, p, i: "=0" if i == 0 else f"={p}{M.k['reps_sn']}*{c}{M.k['live_sn']}", unit="people", total=None)
M.line("prod_ci", "Productive reps, Côte d'Ivoire", lambda c, p, i: "=0" if i == 0 else f"={p}{M.k['reps_ci']}*{c}{M.k['live_ci']}", unit="people", total=None)
M.line("field_sn", "New clients from field sales, Senegal", lambda c, p, i: f"={c}{M.k['prod_sn']}*Rep_Productivity", unit="clients", fmt=NUM1)
M.line("field_ci", "New clients from field sales, Côte d'Ivoire", lambda c, p, i: f"={c}{M.k['prod_ci']}*Rep_Productivity*CI_Productivity", unit="clients", fmt=NUM1)
M.sec("Partner channel (accountants, payroll software, chambers of commerce)")
M.line("part_sn", "New clients from partners, Senegal", lambda c, p, i: f"={c}{M.k['live_sn']}*MIN(Partner_Cap_SN,Partner_Base_SN*(1+Partner_Growth)^MAX(0,{c}$3-Launch_SN))", unit="clients", fmt=NUM1)
M.line("part_ci", "New clients from partners, Côte d'Ivoire", lambda c, p, i: f"={c}{M.k['live_ci']}*MIN(Partner_Cap_CI,Partner_Base_CI*(1+Partner_Growth)^MAX(0,{c}$3-Launch_CI))", unit="clients", fmt=NUM1)
M.sec("Digital marketing")
M.line("dig_b_sn", "Digital ads budget, Senegal", lambda c, p, i: f"={c}{M.k['live_sn']}*{yr('Digital_SN', c)}")
M.line("dig_b_ci", "Digital ads budget, Côte d'Ivoire", lambda c, p, i: f"={c}{M.k['live_ci']}*{yr('Digital_CI', c)}")
M.line("dig_sn", "New clients from digital, Senegal", lambda c, p, i: f"={c}{M.k['dig_b_sn']}/CAC_Digital", unit="clients", fmt=NUM1)
M.line("dig_ci", "New clients from digital, Côte d'Ivoire", lambda c, p, i: f"={c}{M.k['dig_b_ci']}/CAC_Digital", unit="clients", fmt=NUM1)
M.sec("New clients")
M.line("new_sn", "New clients, Senegal", lambda c, p, i: f"={c}{M.k['field_sn']}+{c}{M.k['part_sn']}+{c}{M.k['dig_sn']}", unit="clients", fmt=NUM1)
M.line("new_ci", "New clients, Côte d'Ivoire", lambda c, p, i: f"={c}{M.k['field_ci']}+{c}{M.k['part_ci']}+{c}{M.k['dig_ci']}", unit="clients", fmt=NUM1)
M.line("new_total", "New clients, total", lambda c, p, i: f"={c}{M.k['new_sn']}+{c}{M.k['new_ci']}", unit="clients", fmt=NUM1, bold=True)
M.line("new_p", "of which Petite", lambda c, p, i: f"={c}{M.k['new_total']}*Mix_Petite", unit="clients", fmt=NUM1)
M.line("new_m", "of which Moyenne", lambda c, p, i: f"={c}{M.k['new_total']}*Mix_Moyenne", unit="clients", fmt=NUM1)
M.line("new_g", "of which Grande", lambda c, p, i: f"={c}{M.k['new_total']}*Mix_Grande", unit="clients", fmt=NUM1)
M.line("new_partner", "New clients from partners (for referral fees)", lambda c, p, i: f"={c}{M.k['part_sn']}+{c}{M.k['part_ci']}", unit="clients", fmt=NUM1)
M.sec("Sales and marketing budget (non-staff)")
M.line("c_digital", "Digital ads", lambda c, p, i: f"={c}{M.k['dig_b_sn']}+{c}{M.k['dig_b_ci']}")
M.line("c_brand", "Brand, website, launch events, PR", lambda c, p, i: f"={yr('Brand_PR', c)}/12")
M.line("c_events", "Events, sponsorships, sales materials", lambda c, p, i: f"={yr('Events', c)}/12")
M.line("c_referral", "Referral fees to partners", lambda c, p, i: f"={c}{M.k['new_partner']}*Referral_Fee")
M.line("c_transport", "Field sales transport", lambda c, p, i: f"=({c}{M.k['reps_sn']}+{c}{M.k['reps_ci']})*Rep_Transport")
M.line("c_total", "Total sales and marketing budget (non-staff)", lambda c, p, i: f"=SUM({c}{M.k['c_digital']}:{c}{M.k['c_transport']})", bold=True)
M.sec("Acquisition efficiency")
M.line("sm_staff", "Sales, partnerships and marketing staff cost", lambda c, p, i: f"={S.ref('dep_Sales & partnerships', c)}+{S.ref('dep_Marketing', c)}", color=GREEN)
M.line("cac", "Blended cost to acquire a client (staff + budget)", lambda c, p, i: f"=IFERROR(({c}{M.k['c_total']}+{c}{M.k['sm_staff']})/{c}{M.k['new_total']},0)", total=None)

# =====================================================================================
# CLIENTS & REVENUE
# =====================================================================================
R = TS("Clients & revenue", "Active clients by plan, usage and every revenue line except credit (see Credit).")
R.sec("New clients by plan")
for pl, key in (("Petite", "p"), ("Moyenne", "m"), ("Grande", "g")):
    R.line(f"new_{key}", f"New clients, {pl}", lambda c, p, i, key=key: f"={M.ref('new_' + key, c)}", unit="clients", fmt=NUM1, color=GREEN)
R.sec("Active clients (end of month)")
for pl, key in (("Petite", "p"), ("Moyenne", "m"), ("Grande", "g")):
    R.line(f"act_{key}", f"Active clients, {pl}",
           lambda c, p, i, key=key, pl=pl: f"={c}{R.k['new_' + key]}" if i == 0 else f"={p}{R.k['act_' + key]}*(1-Churn_{pl})+{c}{R.k['new_' + key]}",
           unit="clients", fmt=NUM, total="last")
R.line("act_total", "Active clients, total", lambda c, p, i: f"={c}{R.k['act_p']}+{c}{R.k['act_m']}+{c}{R.k['act_g']}", unit="clients", total="last", bold=True)
R.line("churn_blend", "Blended monthly churn (by sales mix)", lambda c, p, i: "=Mix_Petite*Churn_Petite+Mix_Moyenne*Churn_Moyenne+Mix_Grande*Churn_Grande", unit="%", fmt=PCT2, total=None)
R.line("act_sn", "Active clients, Senegal (approx.)", lambda c, p, i: f"={M.ref('new_sn', c)}" if i == 0 else f"={p}{R.r}*(1-{c}{R.k['churn_blend']})+{M.ref('new_sn', c)}", unit="clients", total="last")
R.line("act_ci", "Active clients, Côte d'Ivoire (approx.)", lambda c, p, i: f"={M.ref('new_ci', c)}" if i == 0 else f"={p}{R.r}*(1-{c}{R.k['churn_blend']})+{M.ref('new_ci', c)}", unit="clients", total="last")
R.sec("Clients in their free months, and paying clients")
for pl, key in (("Petite", "p"), ("Moyenne", "m"), ("Grande", "g")):
    nr = R.k["new_" + key]
    R.line(f"free_{key}", f"In free months, {pl}", lambda c, p, i, nr=nr: f"=IF(Free_Months<=0,0,SUM(OFFSET({c}{nr},0,1-MIN(Free_Months,{c}$3),1,MIN(Free_Months,{c}$3))))", unit="clients", fmt=NUM, total=None)
for pl, key in (("Petite", "p"), ("Moyenne", "m"), ("Grande", "g")):
    R.line(f"pay_{key}", f"Paying clients, {pl}", lambda c, p, i, key=key: f"=MAX(0,{c}{R.k['act_' + key]}-{c}{R.k['free_' + key]})", unit="clients", fmt=NUM, total="last")
R.sec("Usage")
mix3 = lambda c, base: f"{c}{R.k['act_p']}*{base}_Petite+{c}{R.k['act_m']}*{base}_Moyenne+{c}{R.k['act_g']}*{base}_Grande"
R.line("employees", "Employees of active clients", lambda c, p, i: f"={mix3(c, 'Emp')}", unit="people", total="last")
R.line("emp_acc", "Employee salary accounts", lambda c, p, i: f"=IF({c}$3>=EmpAcc_Start,{c}{R.k['employees']}*EmpAcc_Adoption,0)", unit="accounts", total="last")
R.line("cards_issued", "Physical cards issued", lambda c, p, i: f"={c}{R.k['new_p']}*Cards_New_Petite+{c}{R.k['new_m']}*Cards_New_Moyenne+{c}{R.k['new_g']}*Cards_New_Grande", unit="cards", fmt=NUM1)
R.line("cards_paid", "Physical cards charged (first one free)", lambda c, p, i: f"={c}{R.k['new_p']}*MAX(0,Cards_New_Petite-1)+{c}{R.k['new_m']}*MAX(0,Cards_New_Moyenne-1)+{c}{R.k['new_g']}*MAX(0,Cards_New_Grande-1)", unit="cards", fmt=NUM1)
R.line("cards_active", "Active cards", lambda c, p, i: f"={mix3(c, 'Cards_Act')}", unit="cards", total="last")
R.line("spend_dom", "Card spending in FCFA", lambda c, p, i: f"={mix3(c, 'Spend_Dom')}")
R.line("spend_for", "Card spending in foreign currencies", lambda c, p, i: f"={mix3(c, 'Spend_For')}")
R.line("balances", "Client balances (average)", lambda c, p, i: f"={mix3(c, 'Balance')}", total="last")
R.line("payroll", "Salaries paid through Tabax", lambda c, p, i: f"={c}{R.k['employees']}*Avg_Salary")
R.line("supplier", "Supplier payouts", lambda c, p, i: f"={mix3(c, 'Supplier')}", unit="payouts")
R.line("overage", "Supplier payouts above the allowance", lambda c, p, i: f"={mix3(c, 'Overage')}", unit="payouts")
R.line("pl_adopt", "Payment links: share of clients using them", lambda c, p, i: f"=IF({c}$3>=PayLinks_Start,MIN(1,({c}$3-PayLinks_Start+1)/PL_Ramp)*PL_Adoption,0)", unit="%", fmt=PCT, total=None)
R.line("pl_coll", "Payment links: amounts collected", lambda c, p, i: f"=({mix3(c, 'PL_Coll')})*{c}{R.k['pl_adopt']}")
R.sec("Revenue (excluding credit)")
R.line("price_f", "Price factor (yearly increase × yearly-billing discount)", lambda c, p, i: f"=(1+Price_Increase)^({c}$5-1)*(1-Annual_Share*Annual_Free/12)", unit="x", fmt="0.000", total=None)
for pl, key in (("Petite", "p"), ("Moyenne", "m"), ("Grande", "g")):
    R.line(f"rev_sub_{key}", f"Subscriptions, {pl}", lambda c, p, i, key=key, pl=pl: f"={c}{R.k['pay_' + key]}*Price_{pl}*{c}{R.k['price_f']}")
R.line("rev_sub", "Subscriptions", lambda c, p, i: f"={c}{R.k['rev_sub_p']}+{c}{R.k['rev_sub_m']}+{c}{R.k['rev_sub_g']}", bold=True)
R.line("rev_fx", "Fees on foreign-currency card spending", lambda c, p, i: f"={c}{R.k['spend_for']}*FX_Fee")
R.line("rev_ic", "Interchange share on FCFA card spending", lambda c, p, i: f"={c}{R.k['spend_dom']}*Interchange_Share")
R.line("rev_dep", "Share of bank income on client balances", lambda c, p, i: f"={c}{R.k['balances']}*Deposit_Share/12")
R.line("rev_cards", "Physical card fees", lambda c, p, i: f"={c}{R.k['cards_paid']}*Card_Fee")
R.line("rev_over", "Supplier payouts above the allowance", lambda c, p, i: f"={c}{R.k['overage']}*Overage_Fee")
R.line("rev_pl", "Payment link fees", lambda c, p, i: f"={c}{R.k['pl_coll']}*PL_Momo_Share*PL_Fee")
R.line("rev_total", "Revenue excluding credit", lambda c, p, i: f"={c}{R.k['rev_sub']}+SUM({c}{R.k['rev_fx']}:{c}{R.k['rev_pl']})", bold=True)

# =====================================================================================
# CREDIT
# =====================================================================================
K = TS("Credit", "Loan book by product, interest, cost of funds, losses and the share Tabax keeps. The partner SFD is the lender of record until the own SFD funds the book.")
K.sec("Base")
K.line("act", "Active clients", lambda c, p, i: f"={R.ref('act_total', c)}", unit="clients", total="last", color=GREEN)
K.line("emp", "Employee salary accounts", lambda c, p, i: f"={R.ref('emp_acc', c)}", unit="accounts", total="last", color=GREEN)
PRODS = [("Factoring", "Factoring", "act", "Uptake_Factoring"), ("Bridge", "Payroll bridge", "act", "Uptake_Bridge"), ("Line", "Credit line", "act", "Uptake_Line"),
         ("Term", "Equipment and term loans", "act", "Uptake_Term"), ("Advance", "Salary advances", "emp", "Usage_Advance")]
K.sec("Ramp-up (share of full uptake)")
for pk, lab, base, upt in PRODS:
    K.line(f"ramp_{pk}", lab, lambda c, p, i, pk=pk: f"=IF({c}$3>=Start_{pk},MIN(1,({c}$3-Start_{pk}+1)/Credit_Ramp),0)", unit="%", fmt=PCT, total=None)
K.sec("Loans outstanding (end of month)")
for pk, lab, base, upt in PRODS:
    K.line(f"book_{pk}", lab, lambda c, p, i, pk=pk, base=base, upt=upt: f"={c}{K.k[base]}*{upt}*Credit_Mult*{c}{K.k['ramp_' + pk]}*Avg_{pk}", total="last")
K.line("book", "Total loan book", lambda c, p, i: f"=SUM({c}{K.k['book_Factoring']}:{c}{K.k['book_Advance']})", total="last", bold=True)
K.sec("Average loans outstanding in the month")
for pk, lab, base, upt in PRODS:
    br = K.k["book_" + pk]
    K.line(f"avg_{pk}", lab, lambda c, p, i, br=br: f"={c}{br}/2" if i == 0 else f"=({c}{br}+{p}{br})/2", total=None)
K.line("avg", "Average loan book", lambda c, p, i: f"=SUM({c}{K.k['avg_Factoring']}:{c}{K.k['avg_Advance']})", total=None, bold=True)
K.sec("Credit income and costs")
K.line("interest", "Interest and fees (daily rate)", lambda c, p, i: "=" + "+".join(f"{c}{K.k['avg_' + pk]}*Yield_{pk}/12" for pk, *_ in PRODS))
K.line("cof", "Cost of funds", lambda c, p, i: f"=-{c}{K.k['avg']}*CoF/12")
K.line("losses", "Credit losses", lambda c, p, i: "=-(" + "+".join(f"{c}{K.k['avg_' + pk]}*CoR_{pk}" for pk, *_ in PRODS) + f")*CoR_Mult/12")
K.line("servicing", "External servicing and collections", lambda c, p, i: f"=-{c}{K.k['avg']}*Servicing/12")
K.line("margin", "Net credit margin", lambda c, p, i: f"=SUM({c}{K.k['interest']}:{c}{K.k['servicing']})", bold=True)
K.line("share", "Share kept by Tabax", lambda c, p, i: f"=IF({c}$3>=Own_Funding_Month,1,Partner_Share)", unit="%", fmt=PCT, total=None)
K.line("net", "Net credit income to Tabax", lambda c, p, i: f"={c}{K.k['margin']}*{c}{K.k['share']}", bold=True)
K.sec("Cash tied up by credit")
K.line("locked", "First-loss reserve or equity in the loan book", lambda c, p, i: f"=IF({c}$3>=Own_Funding_Month,{c}{K.k['book']}*Capital_Ratio,{c}{K.k['book']}*First_Loss)", total="last")

# =====================================================================================
# COSTS
# =====================================================================================
C = TS("Costs", "Every cost line by month: variable costs that grow with clients, then fixed costs by category, capex and depreciation.")
rr = lambda key, c: R.ref(key, c)
C.sec("Variable costs (cost to serve)")
C.line("v_bank", "Partner bank fee per business account", lambda c, p, i: f"={rr('act_total', c)}*Bank_Fee")
C.line("v_onboard", "Onboarding checks (KYB, ID checks, employee accounts)",
       lambda c, p, i: f"={M.ref('new_total', c)}*(KYB_Cost+KYC_Cost*KYC_Persons)+MAX(0,{rr('emp_acc', c)}-{'0' if i == 0 else rr('emp_acc', p)})*KYC_Cost")
C.line("v_cardproc", "Card processing (per active card)", lambda c, p, i: f"={rr('cards_active', c)}*Card_Proc_Fee")
C.line("v_cardprod", "Physical cards printed and delivered", lambda c, p, i: f"={rr('cards_issued', c)}*Card_Prod_Cost")
C.line("v_scheme", "Visa / Mastercard cross-border fees", lambda c, p, i: f"={rr('spend_for', c)}*Scheme_Rate")
C.line("v_fraud", "Fraud and chargebacks", lambda c, p, i: f"=({rr('spend_dom', c)}+{rr('spend_for', c)})*Fraud_Rate")
C.line("v_wallet", "Salaries paid to wallets", lambda c, p, i: f"={rr('payroll', c)}*Wallet_Share*Wallet_Payout_Cost")
C.line("v_bankpay", "Salaries paid to bank accounts", lambda c, p, i: f"={rr('employees', c)}*(1-Wallet_Share)*Bank_Payout_Cost")
C.line("v_supplier", "Supplier payouts", lambda c, p, i: f"={rr('supplier', c)}*Supplier_Payout_Cost")
C.line("v_pl", "Payment link collection costs", lambda c, p, i: f"={rr('pl_coll', c)}*PL_Momo_Share*PL_Cost")
C.line("v_notif", "SMS, WhatsApp and support tools", lambda c, p, i: f"={rr('act_total', c)}*Notif_Cost+{rr('emp_acc', c)}*Emp_Notif")
C.line("v_empacc", "Employee account processing", lambda c, p, i: f"={rr('emp_acc', c)}*EmpAcc_Cost")
C.line("v_total", "Total variable costs", lambda c, p, i: f"=SUM({c}{C.k['v_bank']}:{c}{C.k['v_empacc']})", bold=True)
C.sec("Staff")
for d in DEPTS:
    C.line(f"s_{d}", d, lambda c, p, i, d=d: f"={S.ref('dep_' + d, c)}", color=GREEN)
C.line("s_total", "Total staff", lambda c, p, i: f"=SUM({c}{C.k['s_' + DEPTS[0]]}:{c}{C.k['s_' + DEPTS[-1]]})", bold=True)
C.sec("Office and equipment")
C.line("o_cowork", "Coworking before the office opens", lambda c, p, i: f"=IF({c}$3<Office_Start,Coworking_Monthly,0)")
C.line("o_rent", "Dakar office rent and charges", lambda c, p, i: f"=IF({c}$3>=Office_Start,{yr('Office_m2', c)}*{yr('Office_Price_Arr', c)},0)")
C.line("o_elec", "Electricity", lambda c, p, i: f"=IF({c}$3>=Office_Start,{yr('Electricity', c)},0)")
C.line("o_net", "Internet", lambda c, p, i: f"=IF({c}$3>=Office_Start,{yr('Internet', c)},0)")
C.line("o_clean", "Cleaning, security, supplies", lambda c, p, i: f"=IF({c}$3>=Office_Start,{yr('Cleaning', c)},0)")
C.line("o_abj", "Abidjan office", lambda c, p, i: f"=IF({c}$3>=CI_Office_Start,{yr('Abidjan_Office', c)},0)")
C.line("o_phone", "Phones and data plans", lambda c, p, i: f"={S.ref('hc_total', c)}*Phone_Cost")
C.line("o_total", "Total office and equipment", lambda c, p, i: f"=SUM({c}{C.k['o_cowork']}:{c}{C.k['o_phone']})", bold=True)
C.sec("Technology")
C.line("t_ledger", "Core ledger / banking platform", lambda c, p, i: f"={yr('Ledger_USD', c)}*FX_USD/12")
C.line("t_cloud", "Cloud hosting", lambda c, p, i: f"=IF({c}$3>=Cloud_Start,{yr('Cloud_USD', c)}*FX_USD,0)")
C.line("t_monitor", "Transaction monitoring and sanctions screening", lambda c, p, i: f"={yr('Monitoring_USD', c)}*FX_USD/12")
C.line("t_backoffice", "Back-office and internal tools", lambda c, p, i: f"={yr('Backoffice_USD', c)}*FX_USD/12")
C.line("t_tools", "Software tools per employee", lambda c, p, i: f"={S.ref('hc_total', c)}*Tools_USD*FX_USD")
C.line("t_freelance", "Freelance QA, DevOps, design", lambda c, p, i: f"={yr('Freelance', c)}/12")
C.line("t_security", "Penetration tests and PCI DSS", lambda c, p, i: f"={yr('Security_USD', c)}*FX_USD/12")
C.line("t_proc_setup", "Card processor set-up fee", lambda c, p, i: f"=IF({c}$3=Proc_Setup_Month,Proc_Setup_USD*FX_USD,0)")
C.line("t_proc_min", "Card processor minimum (top-up above per-card fees)", lambda c, p, i: f"=IF({c}$3>=Proc_Min_Start,MAX(0,{yr('Proc_Min_USD', c)}*FX_USD-{c}{C.k['v_cardproc']}),0)")
C.line("t_total", "Total technology", lambda c, p, i: f"=SUM({c}{C.k['t_ledger']}:{c}{C.k['t_proc_min']})", bold=True)
C.sec("Bank and SFD partners")
C.line("p_setup_sn", "Partner bank set-up, Senegal", lambda c, p, i: f"=IF({c}$3=Bank_Setup_Month,Bank_Setup_SN,0)")
C.line("p_min_sn", "Partner bank platform minimum, Senegal", lambda c, p, i: f"=IF({c}$3>=Launch_SN,{yr('Bank_Min_SN', c)},0)")
C.line("p_setup_ci", "Partner bank set-up, Côte d'Ivoire", lambda c, p, i: f"=IF({c}$3=CI_Bank_Setup_Month,Bank_Setup_CI,0)")
C.line("p_min_ci", "Partner bank platform minimum, Côte d'Ivoire", lambda c, p, i: f"=IF({c}$3>=Launch_CI,{yr('Bank_Min_CI', c)},0)")
C.line("p_sfd", "Partner SFD integration and fees", lambda c, p, i: f"=IF({c}$3=SFD_Setup_Month,SFD_Setup,0)+{yr('SFD_Annual', c)}/12")
C.line("p_total", "Total bank and SFD partners", lambda c, p, i: f"=SUM({c}{C.k['p_setup_sn']}:{c}{C.k['p_sfd']})", bold=True)
C.sec("Legal, regulatory and audit")
C.line("l_company", "Company set-up (Senegal, Côte d'Ivoire)", lambda c, p, i: f"=IF({c}$3=1,Company_Setup_SN,0)+IF({c}$3=CI_Company_Month,Company_Setup_CI,0)")
C.line("l_lic_sn", "Payment licence file, Senegal", lambda c, p, i: f"=IF({c}$3<=Licence_File_SN_Months,Licence_File_SN/Licence_File_SN_Months,0)")
C.line("l_lic_ci", "Payment licence file, Côte d'Ivoire", lambda c, p, i: f"=IF(AND({c}$3>=CI_Licence_File_Start,{c}$3<CI_Licence_File_Start+Licence_File_CI_Months),Licence_File_CI/Licence_File_CI_Months,0)")
C.line("l_sfd", "SFD project (licence or acquisition due diligence)", lambda c, p, i: f"={yr('SFD_Project', c)}/12")
C.line("l_counsel", "Ongoing legal counsel", lambda c, p, i: f"={yr('Legal_Counsel', c)}")
C.line("l_auditor", "Statutory auditor", lambda c, p, i: f"={yr('Auditor', c)}/12")
C.line("l_accountant", "External accountant and tax adviser", lambda c, p, i: f"={yr('Accountant_Ext', c)}")
C.line("l_aml", "Independent AML audit", lambda c, p, i: f"={yr('AML_Audit', c)}/12")
C.line("l_data", "Data-protection filings", lambda c, p, i: f"={yr('Data_Protection', c)}/12")
C.line("l_insurance", "Insurance", lambda c, p, i: f"={yr('Insurance_USD', c)}*FX_USD/12")
C.line("l_total", "Total legal, regulatory and audit", lambda c, p, i: f"=SUM({c}{C.k['l_company']}:{c}{C.k['l_insurance']})", bold=True)
C.sec("Sales and marketing (non-staff)")
for key, lab in (("c_digital", "Digital ads"), ("c_brand", "Brand, website, launch events, PR"), ("c_events", "Events, sponsorships, sales materials"),
                 ("c_referral", "Referral fees to partners"), ("c_transport", "Field sales transport")):
    C.line("m_" + key, lab, lambda c, p, i, key=key: f"={M.ref(key, c)}", color=GREEN)
C.line("m_total", "Total sales and marketing (non-staff)", lambda c, p, i: f"=SUM({c}{C.k['m_c_digital']}:{c}{C.k['m_c_transport']})", bold=True)
C.sec("Other")
C.line("x_recruit", "Recruitment fees", lambda c, p, i: f"={yr('Recruitment', c)}/12")
C.line("x_travel", "Travel", lambda c, p, i: f"={yr('Travel', c)}/12")
C.line("x_misc", "Company bank fees and miscellaneous", lambda c, p, i: f"={yr('Misc', c)}")
C.line("x_total", "Total other", lambda c, p, i: f"=SUM({c}{C.k['x_recruit']}:{c}{C.k['x_misc']})", bold=True)
C.sec("Fixed costs summary")
C.line("f_before", "Fixed costs before contingency",
       lambda c, p, i: "=" + "+".join(f"{c}{C.k[k]}" for k in ("s_total", "o_total", "t_total", "p_total", "l_total", "m_total", "x_total")))
C.line("f_cont", "Contingency", lambda c, p, i: f"={c}{C.k['f_before']}*Contingency_Pct")
C.line("f_total", "Total fixed costs", lambda c, p, i: f"={c}{C.k['f_before']}+{c}{C.k['f_cont']}", bold=True)
C.sec("Capex and depreciation")
C.line("cx_laptops", "Laptops and equipment for new hires", lambda c, p, i: f"={S.ref('hires', c)}*Laptop_Cost")
C.line("cx_fitout", "Office fit-out and furniture", lambda c, p, i: f"=IF({c}$3=IF({c}$5=1,Office_Start,({c}$5-1)*12+1),{yr('Fitout', c)},0)")
C.line("cx_total", "Total capex", lambda c, p, i: f"={c}{C.k['cx_laptops']}+{c}{C.k['cx_fitout']}", bold=True)
C.line("dep", "Depreciation", lambda c, p, i: f"=SUM(OFFSET({c}{C.k['cx_total']},0,1-MIN(Dep_Months,{c}$3),1,MIN(Dep_Months,{c}$3)))/Dep_Months")

# =====================================================================================
# P&L MONTHLY
# =====================================================================================
P = TS("P&L monthly", "Profit and loss by month. Revenue excludes VAT and taxes on financial services.")
P.sec("Revenue")
for key, lab in (("rev_sub", "Subscriptions"), ("rev_fx", "Fees on foreign-currency card spending"), ("rev_ic", "Interchange share"),
                 ("rev_dep", "Share of bank income on client balances"), ("rev_cards", "Physical card fees"), ("rev_over", "Supplier payout fees above the allowance"),
                 ("rev_pl", "Payment link fees")):
    P.line(key, lab, lambda c, p, i, key=key: f"={R.ref(key, c)}", color=GREEN)
P.line("rev_credit", "Net credit income", lambda c, p, i: f"={K.ref('net', c)}", color=GREEN)
P.line("revenue", "Total revenue", lambda c, p, i: f"=SUM({c}{P.k['rev_sub']}:{c}{P.k['rev_credit']})", bold=True, fill=TOT_FILL)
P.sec("Cost of revenue (variable costs)")
P.line("d_bank", "Bank accounts and onboarding", lambda c, p, i: f"={C.ref('v_bank', c)}+{C.ref('v_onboard', c)}")
P.line("d_cards", "Cards: processing, production, scheme fees, fraud", lambda c, p, i: f"={C.ref('v_cardproc', c)}+{C.ref('v_cardprod', c)}+{C.ref('v_scheme', c)}+{C.ref('v_fraud', c)}")
P.line("d_pay", "Payouts and collections", lambda c, p, i: f"={C.ref('v_wallet', c)}+{C.ref('v_bankpay', c)}+{C.ref('v_supplier', c)}+{C.ref('v_pl', c)}")
P.line("d_msg", "Messaging and employee accounts", lambda c, p, i: f"={C.ref('v_notif', c)}+{C.ref('v_empacc', c)}")
P.line("cogs", "Total cost of revenue", lambda c, p, i: f"=SUM({c}{P.k['d_bank']}:{c}{P.k['d_msg']})", bold=True)
P.line("gm", "Gross margin", lambda c, p, i: f"={c}{P.k['revenue']}-{c}{P.k['cogs']}", bold=True, fill=TOT_FILL)
P.line("gm_pct", "Gross margin %", lambda c, p, i: f"=IFERROR({c}{P.k['gm']}/{c}{P.k['revenue']},0)", unit="%", fmt=PCT, total=None)
P.sec("Operating expenses")
for key, lab, src in (("x_staff", "Staff", "s_total"), ("x_office", "Office and equipment", "o_total"), ("x_tech", "Technology", "t_total"),
                      ("x_partners", "Bank and SFD partners", "p_total"), ("x_legal", "Legal, regulatory and audit", "l_total"),
                      ("x_sm", "Sales and marketing (non-staff)", "m_total"), ("x_other", "Other", "x_total"), ("x_cont", "Contingency", "f_cont")):
    P.line(key, lab, lambda c, p, i, src=src: f"={C.ref(src, c)}", color=GREEN)
P.line("opex", "Total operating expenses", lambda c, p, i: f"=SUM({c}{P.k['x_staff']}:{c}{P.k['x_cont']})", bold=True)
P.line("ebitda", "EBITDA", lambda c, p, i: f"={c}{P.k['gm']}-{c}{P.k['opex']}", bold=True, fill=TOT_FILL)
P.line("ebitda_pct", "EBITDA margin", lambda c, p, i: f"=IFERROR({c}{P.k['ebitda']}/{c}{P.k['revenue']},0)", unit="%", fmt=PCT, total=None)
P.line("dep", "Depreciation", lambda c, p, i: f"={C.ref('dep', c)}", color=GREEN)
P.line("ebit", "Operating result (EBIT)", lambda c, p, i: f"={c}{P.k['ebitda']}-{c}{P.k['dep']}", bold=True)
P.line("cum_ebit", "Cumulative EBIT (for tax losses carried forward)", lambda c, p, i: f"={c}{P.k['ebit']}" if i == 0 else f"={p}{P.r}+{c}{P.k['ebit']}", total="last")
P.line("tax", "Corporate income tax", lambda c, p, i: f"=Tax_Rate*MAX(0,{c}{P.k['cum_ebit']})" if i == 0 else f"=Tax_Rate*MAX(0,{c}{P.k['cum_ebit']})-Tax_Rate*MAX(0,{p}{P.k['cum_ebit']})")
P.line("ni", "Net income", lambda c, p, i: f"={c}{P.k['ebit']}-{c}{P.k['tax']}", bold=True, fill=TOT_FILL)
P.line("cum_ni", "Cumulative net income", lambda c, p, i: f"={c}{P.k['ni']}" if i == 0 else f"={p}{P.r}+{c}{P.k['ni']}", total="last")
P.sec("Helpers")
P.line("be_flag", "Month number if EBITDA is positive (999 otherwise)", lambda c, p, i: f"=IF({c}{P.k['ebitda']}>0,{c}$3,999)", unit="month #", fmt="0", total=None)

# =====================================================================================
# CASH FLOW
# =====================================================================================
Q = TS("Cash flow", "Monthly cash: operating result, capex, cash set aside (licence capital, collateral, credit), funding rounds and the closing balance.")
Q.sec("Operations")
Q.line("ni", "Net income", lambda c, p, i: f"={P.ref('ni', c)}", color=GREEN)
Q.line("dep", "Add back depreciation", lambda c, p, i: f"={P.ref('dep', c)}", color=GREEN)
Q.line("capex", "Capex", lambda c, p, i: f"=-{C.ref('cx_total', c)}")
Q.sec("Cash set aside (restricted)")
Q.line("lic_sn", "Licence capital, Senegal", lambda c, p, i: f"=-IF({c}$3=Licence_SN_Month,Licence_Capital_SN,0)")
Q.line("lic_ci", "Licence capital, Côte d'Ivoire", lambda c, p, i: f"=-IF({c}$3=Licence_CI_Month,Licence_Capital_CI,0)")
Q.line("collat", "Card programme collateral", lambda c, p, i: f"=-IF({c}$3=Collateral_Month,Card_Collateral,0)")
Q.line("deposit", "Office deposit", lambda c, p, i: f"=-IF({c}$3=Office_Start,Office_Deposit_Months*{C.ref('o_rent', c)},0)")
Q.line("sfd", "Own SFD licence or acquisition", lambda c, p, i: f"=-IF({c}$3=SFD_Acq_Month,SFD_Acquisition,0)")
Q.line("credit", "Change in cash tied up by credit", lambda c, p, i: f"=-{K.ref('locked', c)}" if i == 0 else f"=-({K.ref('locked', c)}-{K.ref('locked', p)})")
Q.line("before", "Cash flow before funding", lambda c, p, i: f"=SUM({c}{Q.k['ni']}:{c}{Q.k['credit']})", bold=True)
Q.line("cum_before", "Cumulative cash flow before funding", lambda c, p, i: f"={c}{Q.k['before']}" if i == 0 else f"={p}{Q.r}+{c}{Q.k['before']}", total="last")
Q.sec("Funding")
Q.line("equity", "Equity raised", lambda c, p, i: f"=IF({c}$3=Seed_Month,Seed_Amount,0)+IF({c}$3=SeriesA_Month,SeriesA_Amount,0)+IF({c}$3=SeriesB_Month,SeriesB_Amount,0)")
Q.line("net", "Net cash flow", lambda c, p, i: f"={c}{Q.k['before']}+{c}{Q.k['equity']}", bold=True)
Q.sec("Cash balance")
Q.line("open", "Opening cash", lambda c, p, i: "=Opening_Cash" if i == 0 else f"={p}{Q.r + 1}", total=None)
Q.line("close", "Closing cash", lambda c, p, i: f"={c}{Q.k['open']}+{c}{Q.k['net']}", total="last", bold=True, fill=TOT_FILL)
Q.line("restricted", "Cash set aside so far (not included in closing cash)",
       lambda c, p, i: f"=-SUM({FC}{Q.k['lic_sn']}:{c}{Q.k['lic_sn']})-SUM({FC}{Q.k['lic_ci']}:{c}{Q.k['lic_ci']})-SUM({FC}{Q.k['collat']}:{c}{Q.k['collat']})-SUM({FC}{Q.k['deposit']}:{c}{Q.k['deposit']})+{K.ref('locked', c)}",
       total="last")
Q.line("burn", "Monthly burn (average of the last 3 months, if negative)", lambda c, p, i: f"=MAX(0,-AVERAGE({c}{Q.k['before']}))" if i < 2 else f"=MAX(0,-AVERAGE({COLS[i - 2]}{Q.k['before']}:{c}{Q.k['before']}))", total=None)
Q.line("runway", "Runway at that burn (months)", lambda c, p, i: f"=IF({c}{Q.k['burn']}=0,\"cash positive\",{c}{Q.k['close']}/{c}{Q.k['burn']})", unit="months", fmt=NUM1, total=None)

# =====================================================================================
# P&L ANNUAL (with cash and euros)
# =====================================================================================
Y = wb.create_sheet("P&L annual")
title(Y, "P&L annual", "Years 1–5, summed from the monthly sheets. Euro view at the bottom.")
Y.column_dimensions["A"].width = 50
Y.column_dimensions["B"].width = 14
Y.column_dimensions["C"].width = 3
for col in "DEFGHI":
    Y.column_dimensions[col].width = 16
Y["A4"] = "Year"
Y["A5"] = "Fiscal year"
for j in range(5):
    col = CL(4 + j)
    Y[f"{col}4"] = j + 1
    Y[f"{col}5"] = f"=YEAR(Start_Date)+{col}4-1"
    for rr_ in (4, 5):
        style(Y[f"{col}{rr_}"], fmt='"Y"0' if rr_ == 4 else "0", bold=True, fill=SEC_FILL, align="center")
Y["I4"] = "5 years"
style(Y["I4"], bold=True, fill=SEC_FILL, align="center")
Y.freeze_panes = "D6"
yrow = [7]
YK = {}


def y_sec(text):
    yrow[0] += 1
    Y.cell(yrow[0], 1, text).font = F(bold=True)
    for col in range(1, 10):
        Y.cell(yrow[0], col).fill = SEC_FILL
    yrow[0] += 1


def y_sum(key, label, sheet, srckey, fmt=NUM, bold=False, total=True):
    r = yrow[0]
    YK[key] = r
    Y.cell(r, 1, label).font = F(bold=bold)
    src = sheet.k[srckey]
    for j in range(5):
        col = CL(4 + j)
        Y[f"{col}{r}"] = f"=SUMIF('{sheet.name}'!${FC}$5:${LC}$5,{col}$4,'{sheet.name}'!${FC}${src}:${LC}${src})"
        style(Y[f"{col}{r}"], fmt=fmt, bold=bold, color=GREEN)
    if total:
        Y[f"I{r}"] = f"=SUM(D{r}:H{r})"
        style(Y[f"I{r}"], fmt=fmt, bold=True, fill=TOT_FILL)
    yrow[0] += 1
    return r


def y_end(key, label, sheet, srckey, fmt=NUM, bold=False):
    r = yrow[0]
    YK[key] = r
    Y.cell(r, 1, label).font = F(bold=bold)
    src = sheet.k[srckey]
    for j in range(5):
        col = CL(4 + j)
        Y[f"{col}{r}"] = f"=INDEX('{sheet.name}'!${FC}${src}:${LC}${src},1,{col}$4*12)"
        style(Y[f"{col}{r}"], fmt=fmt, bold=bold, color=GREEN)
    yrow[0] += 1
    return r


def y_f(key, label, fn, fmt=NUM, bold=False, total=None, fill=None):
    r = yrow[0]
    YK[key] = r
    Y.cell(r, 1, label).font = F(bold=bold)
    for j in range(5):
        col = CL(4 + j)
        Y[f"{col}{r}"] = fn(col)
        style(Y[f"{col}{r}"], fmt=fmt, bold=bold, fill=fill)
    if total == "sum":
        Y[f"I{r}"] = f"=SUM(D{r}:H{r})"
        style(Y[f"I{r}"], fmt=fmt, bold=True, fill=TOT_FILL)
    elif total:
        Y[f"I{r}"] = total(r)
        style(Y[f"I{r}"], fmt=fmt, bold=True, fill=TOT_FILL)
    yrow[0] += 1
    return r


y_sec("Revenue (FCFA)")
for key in ("rev_sub", "rev_fx", "rev_ic", "rev_dep", "rev_cards", "rev_over", "rev_pl", "rev_credit"):
    lab = P.ws.cell(P.k[key], 1).value
    y_sum(key, lab, P, key)
y_sum("revenue", "Total revenue", P, "revenue", bold=True)
y_f("growth", "Revenue growth", lambda col: "=0" if col == "D" else f"=IFERROR({col}{YK['revenue']}/{CL(ord(col) - 65)}{YK['revenue']}-1,0)", fmt=PCT)
y_sec("Cost of revenue")
for key in ("d_bank", "d_cards", "d_pay", "d_msg"):
    y_sum(key, P.ws.cell(P.k[key], 1).value, P, key)
y_sum("cogs", "Total cost of revenue", P, "cogs", bold=True)
y_f("gm", "Gross margin", lambda col: f"={col}{YK['revenue']}-{col}{YK['cogs']}", bold=True, total="sum", fill=TOT_FILL)
y_f("gm_pct", "Gross margin %", lambda col: f"=IFERROR({col}{YK['gm']}/{col}{YK['revenue']},0)", fmt=PCT, total=lambda r: f"=IFERROR(I{YK['gm']}/I{YK['revenue']},0)")
y_sec("Operating expenses")
for key in ("x_staff", "x_office", "x_tech", "x_partners", "x_legal", "x_sm", "x_other", "x_cont"):
    y_sum(key, P.ws.cell(P.k[key], 1).value, P, key)
y_sum("opex", "Total operating expenses", P, "opex", bold=True)
y_f("ebitda", "EBITDA", lambda col: f"={col}{YK['gm']}-{col}{YK['opex']}", bold=True, total="sum", fill=TOT_FILL)
y_f("ebitda_pct", "EBITDA margin", lambda col: f"=IFERROR({col}{YK['ebitda']}/{col}{YK['revenue']},0)", fmt=PCT, total=lambda r: f"=IFERROR(I{YK['ebitda']}/I{YK['revenue']},0)")
y_sum("dep", "Depreciation", P, "dep")
y_f("ebit", "Operating result (EBIT)", lambda col: f"={col}{YK['ebitda']}-{col}{YK['dep']}", bold=True, total="sum")
y_sum("tax", "Corporate income tax", P, "tax")
y_f("ni", "Net income", lambda col: f"={col}{YK['ebit']}-{col}{YK['tax']}", bold=True, total="sum", fill=TOT_FILL)
y_sec("Cash and funding (FCFA)")
y_sum("cf_before", "Cash flow before funding", Q, "before")
y_sum("equity", "Equity raised", Q, "equity")
y_end("cash", "Closing cash (end of year)", Q, "close", bold=True)
y_sec("Operating figures (end of year)")
y_end("clients", "Active clients", R, "act_total", bold=True)
y_end("clients_sn", "of which Senegal (approx.)", R, "act_sn")
y_end("clients_ci", "of which Côte d'Ivoire (approx.)", R, "act_ci")
y_sum("new_clients", "New clients in the year", M, "new_total")
y_end("headcount", "Headcount", S, "hc_total")
y_end("book", "Loan book", K, "book")
y_end("emp_acc", "Employee salary accounts", R, "emp_acc")
y_sec("In euros (thousands)")
for key, lab in (("revenue", "Total revenue"), ("gm", "Gross margin"), ("opex", "Total operating expenses"), ("ebitda", "EBITDA"), ("ni", "Net income"),
                 ("equity", "Equity raised"), ("cash", "Closing cash (end of year)"), ("book", "Loan book (end of year)")):
    y_f("eur_" + key, lab + " (€k)", lambda col, key=key: f"={col}{YK[key]}/FX_EUR/1000", fmt=NUM, bold=key in ("revenue", "ebitda"),
        total="sum" if key not in ("cash", "book") else None)

# =====================================================================================
# KPIs and unit economics
# =====================================================================================
U = wb.create_sheet("Unit economics")
title(U, "Unit economics and KPIs", "Per-client economics and efficiency ratios by year.")
U.column_dimensions["A"].width = 58
U.column_dimensions["B"].width = 14
U.column_dimensions["C"].width = 3
for col in "DEFGH":
    U.column_dimensions[col].width = 16
U["A4"] = "Year"
for j in range(5):
    col = CL(4 + j)
    U[f"{col}4"] = j + 1
    style(U[f"{col}4"], fmt='"Y"0', bold=True, fill=SEC_FILL, align="center")
U.freeze_panes = "D5"
urow = [6]
UK = {}


def u(key, label, fn, fmt=NUM, unit="", bold=False):
    r = urow[0]
    UK[key] = r
    U.cell(r, 1, label).font = F(bold=bold)
    U.cell(r, 2, unit).font = F(color=GREY)
    for j in range(5):
        col = CL(4 + j)
        U[f"{col}{r}"] = fn(col)
        style(U[f"{col}{r}"], fmt=fmt, bold=bold)
    urow[0] += 1
    return r


def u_sec(text):
    urow[0] += 1
    U.cell(urow[0], 1, text).font = F(bold=True)
    for col in range(1, 9):
        U.cell(urow[0], col).fill = SEC_FILL
    urow[0] += 1


avg_clients = lambda col: f"AVERAGEIF('{R.name}'!${FC}$5:${LC}$5,{col}$4,'{R.name}'!${FC}${R.k['act_total']}:${LC}${R.k['act_total']})"
ysum = lambda sheet, key, col: f"SUMIF('{sheet.name}'!${FC}$5:${LC}$5,{col}$4,'{sheet.name}'!${FC}${sheet.k[key]}:${LC}${sheet.k[key]})"
u_sec("Clients")
u("avg_clients", "Average active clients", lambda col: f"={avg_clients(col)}", unit="clients")
u("new", "New clients", lambda col: f"={ysum(M, 'new_total', col)}", unit="clients")
u("churned", "Clients lost (approx.)", lambda col: f"=MAX(0,{ysum(M, 'new_total', col)}-('P&L annual'!{col}{YK['clients']}-IF({col}$4=1,0,INDEX('P&L annual'!$D${YK['clients']}:$H${YK['clients']},1,{col}$4-1))))", unit="clients")
u_sec("Revenue and margin per client (per month)")
u("arpa", "Revenue per active client (ARPA), incl. credit", lambda col: f"=IFERROR('P&L annual'!{col}{YK['revenue']}/{col}{UK['avg_clients']}/12,0)", unit="FCFA / month", bold=True)
u("arpa_sub", "of which subscription", lambda col: f"=IFERROR('P&L annual'!{col}{YK['rev_sub']}/{col}{UK['avg_clients']}/12,0)", unit="FCFA / month")
u("cost_serve", "Cost to serve per client", lambda col: f"=IFERROR('P&L annual'!{col}{YK['cogs']}/{col}{UK['avg_clients']}/12,0)", unit="FCFA / month")
u("contrib", "Contribution per client (gross margin)", lambda col: f"={col}{UK['arpa']}-{col}{UK['cost_serve']}", unit="FCFA / month", bold=True)
u("contrib_eur", "Contribution per client in euros", lambda col: f"={col}{UK['contrib']}/FX_EUR", unit="€ / month", fmt=NUM1)
u_sec("Acquisition")
u("sm_spend", "Sales and marketing spend (staff + budget)", lambda col: f"={ysum(M, 'c_total', col)}+{ysum(M, 'sm_staff', col)}", unit="FCFA")
u("cac", "Blended cost to acquire a client (CAC)", lambda col: f"=IFERROR({col}{UK['sm_spend']}/{col}{UK['new']},0)", unit="FCFA", bold=True)
u("payback", "CAC payback", lambda col: f"=IFERROR({col}{UK['cac']}/{col}{UK['contrib']},0)", unit="months", fmt=NUM1)
u("churn", "Blended monthly churn (by sales mix)", lambda col: "=Mix_Petite*Churn_Petite+Mix_Moyenne*Churn_Moyenne+Mix_Grande*Churn_Grande", unit="% / month", fmt=PCT2)
u("ltv", "Lifetime contribution per client (contribution ÷ churn)", lambda col: f"=IFERROR({col}{UK['contrib']}/{col}{UK['churn']},0)", unit="FCFA")
u("ltv_cac", "Lifetime contribution ÷ CAC", lambda col: f"=IFERROR({col}{UK['ltv']}/{col}{UK['cac']},0)", unit="x", fmt="0.0x")
u_sec("Efficiency")
u("hc", "Headcount (end of year)", lambda col: f"='P&L annual'!{col}{YK['headcount']}", unit="people")
u("rev_emp", "Revenue per employee", lambda col: f"=IFERROR('P&L annual'!{col}{YK['revenue']}/{col}{UK['hc']},0)", unit="FCFA")
u("staff_pct", "Staff cost as % of revenue", lambda col: f"=IFERROR('P&L annual'!{col}{YK['x_staff']}/'P&L annual'!{col}{YK['revenue']},0)", unit="%", fmt=PCT)
u("clients_rep", "New clients per field sales rep (end-of-year reps)", lambda col: f"=IFERROR({col}{UK['new']}/(INDEX('{S.name}'!${FC}${S.k['reps_sn']}:${LC}${S.k['reps_sn']},1,{col}$4*12)+INDEX('{S.name}'!${FC}${S.k['reps_ci']}:${LC}${S.k['reps_ci']},1,{col}$4*12)),0)", unit="clients", fmt=NUM1)
u_sec("Credit")
u("credit_share", "Credit income as % of revenue", lambda col: f"=IFERROR('P&L annual'!{col}{YK['rev_credit']}/'P&L annual'!{col}{YK['revenue']},0)", unit="%", fmt=PCT)
u("book_client", "Loan book per active client (end of year)", lambda col: f"=IFERROR('P&L annual'!{col}{YK['book']}/'P&L annual'!{col}{YK['clients']},0)", unit="FCFA")
u("deposit_rev", "Bank income share on balances as % of revenue", lambda col: f"=IFERROR('P&L annual'!{col}{YK['rev_dep']}/'P&L annual'!{col}{YK['revenue']},0)", unit="%", fmt=PCT)

# =====================================================================================
# MARKET
# =====================================================================================
MK = wb.create_sheet("Market")
title(MK, "Market", "How many companies Tabax can serve, and the share of them the plan reaches. Blue cells are inputs with their sources.")
MK.column_dimensions["A"].width = 60
MK.column_dimensions["B"].width = 16
MK.column_dimensions["C"].width = 3
for col in "DEFGH":
    MK.column_dimensions[col].width = 15
MK.column_dimensions["I"].width = 100
mrow = [4]
MKK = {}


def mk_head(text, years=False):
    r = mrow[0] + 1
    MK.cell(r, 1, text)
    heads = ["Unit", "", "Value"] if not years else ["Unit", ""] + [f"Y{j + 1}" for j in range(5)]
    for j, h in enumerate(heads):
        MK.cell(r, 2 + j, h)
    MK.cell(r, 9, "Source / note")
    for col in range(1, 10):
        c = MK.cell(r, col)
        c.font = F(bold=True, color=WHITE)
        c.fill = HEAD_FILL
    mrow[0] = r + 1


def mk_in(key, label, v, unit, fmt, note):
    r = mrow[0]
    MKK[key] = r
    MK.cell(r, 1, label).font = F()
    MK.cell(r, 2, unit).font = F(color=GREY)
    style(MK.cell(r, 4, v), fmt=fmt, color=BLUE, fill=IN_FILL)
    MK.cell(r, 9, note).font = F(color=GREY)
    mrow[0] += 1


def mk_y(key, label, fn, unit, fmt=NUM, bold=False):
    r = mrow[0]
    MKK[key] = r
    MK.cell(r, 1, label).font = F(bold=bold)
    MK.cell(r, 2, unit).font = F(color=GREY)
    for j in range(5):
        col = CL(4 + j)
        MK[f"{col}{r}"] = fn(col, j + 1)
        style(MK[f"{col}{r}"], fmt=fmt, bold=bold)
    mrow[0] += 1


mk_head("Senegal: inputs")
mk_in("sn_emp", "Formal employers contributing to IPRES (2024)", 40300, "companies", NUM, "Le Soleil citing ANSD SES 2024: 40,300 contributing employers (+4.9% vs 2023). https://lesoleil.sn/actualites/economie/prevoyance-retraite-les-charges-de-lipres-estimees-a-plus-de-153-milliards-de-fcfa-en-2024/")
mk_in("sn_growth", "Growth in formal employers", 0.049, "% / year", PCT, "2023 → 2024 growth (38,381 → 40,300).")
mk_in("sn_staff", "Declared private-sector employees (IPRES, 2024)", 577171, "people", NUM, "Same source. Base for employee salary accounts.")
mk_in("sn_new", "New companies registered a year (APIX)", 26000, "companies / year", NUM, "AllAfrica / APS, Sep 2025.")
mk_in("sn_units", "Economic units (ANSD census 2016, 97% informal)", 407882, "units", NUM, "ANSD RGE 2016. A new census (RGE-2) is under way, results 2027–28.")
mk_in("sn_target", "Share of formal employers in Tabax's target (2–500 staff, urban, digital)", 0.50, "%", PCT, "Assumption. Core target: Dakar, Thiès, Saint-Louis.")
mk_head("Côte d'Ivoire: inputs")
mk_in("ci_emp", "Formal employers (estimate)", 60000, "companies", NUM, "ESTIMATE: no published CNPS count of contributing employers was found. About 1.5× Senegal, as Côte d'Ivoire's economy is about twice as large. Replace with the CNPS annual report.")
mk_in("ci_growth", "Growth in formal employers", 0.05, "% / year", PCT, "Assumption.")
mk_in("ci_new", "New companies created a year (CEPICI, 2025)", 26948, "companies / year", NUM, "CEPICI 2025 review (Feb 2026): 26,948 companies created, +6%. https://fr.allafrica.com/stories/202602200240.html")
mk_in("ci_target", "Share of formal employers in Tabax's target", 0.50, "%", PCT, "Assumption. Core target: Abidjan.")
mk_head("Addressable market and plan penetration (end of year)", years=True)
start_year = 2024
mk_y("sn_market", "Senegal: formal employers", lambda col, y: f"=$D${MKK['sn_emp']}*(1+$D${MKK['sn_growth']})^(YEAR(Start_Date)+{y - 1}-{start_year})", "companies")
mk_y("sn_sam", "Senegal: target companies (serviceable market)", lambda col, y: f"={col}{MKK['sn_market']}*$D${MKK['sn_target']}", "companies", bold=True)
mk_y("sn_clients", "Senegal: Tabax active clients", lambda col, y: f"='P&L annual'!{col}{YK['clients_sn']}", "clients")
mk_y("sn_share", "Senegal: share of target companies", lambda col, y: f"=IFERROR({col}{MKK['sn_clients']}/{col}{MKK['sn_sam']},0)", "%", fmt=PCT, bold=True)
mk_y("ci_market", "Côte d'Ivoire: formal employers", lambda col, y: f"=$D${MKK['ci_emp']}*(1+$D${MKK['ci_growth']})^(YEAR(Start_Date)+{y - 1}-{start_year})", "companies")
mk_y("ci_sam", "Côte d'Ivoire: target companies (serviceable market)", lambda col, y: f"={col}{MKK['ci_market']}*$D${MKK['ci_target']}", "companies", bold=True)
mk_y("ci_clients", "Côte d'Ivoire: Tabax active clients", lambda col, y: f"='P&L annual'!{col}{YK['clients_ci']}", "clients")
mk_y("ci_share", "Côte d'Ivoire: share of target companies", lambda col, y: f"=IFERROR({col}{MKK['ci_clients']}/{col}{MKK['ci_sam']},0)", "%", fmt=PCT, bold=True)
mk_y("emp_share", "Employee salary accounts vs declared employees in Senegal", lambda col, y: f"=IFERROR('P&L annual'!{col}{YK['emp_acc']}/$D${MKK['sn_staff']},0)", "%", fmt=PCT2)
mk_head("Revenue pool today (indicative)")
mk_in("bank_fee", "Bank business account fee (SME)", 15000, "FCFA / month", NUM, "UBA Senegal: 25,000 FCFA for SA/SARL, 10,000 for small businesses (comparison site, unverified).")
r = mrow[0]
MK.cell(r, 1, "Senegal: what target companies pay for business accounts today").font = F()
MK.cell(r, 2, "FCFA / year").font = F(color=GREY)
MK.cell(r, 4, f"=D{MKK['sn_sam']}*D{MKK['bank_fee']}*12")
style(MK.cell(r, 4), fmt=NUM)
MK.cell(r, 9, "Account fees only; transfer, card and payout fees come on top. Wave Business charges 1% on bulk payouts.").font = F(color=GREY)
mrow[0] += 1

# =====================================================================================
# DASHBOARD
# =====================================================================================
D = wb.create_sheet("Dashboard")
title(D, "Tabax business plan: dashboard", "Key results for the scenario selected on Assumptions. Amounts in FCFA unless stated.")
D.column_dimensions["A"].width = 48
D.column_dimensions["B"].width = 18
D.column_dimensions["C"].width = 3
for col in "DEFGHI":
    D.column_dimensions[col].width = 16
D["A4"] = "Scenario"
D["B4"] = "=Assumptions!E4"
style(D["A4"], bold=True)
style(D["B4"], bold=True, fill=KEY_FILL)
D["A6"] = "Headline numbers"
style(D["A6"], bold=True)
for col in range(1, 10):
    D.cell(6, col).fill = SEC_FILL
be_row = P.k["be_flag"]
cum_row = Q.k["cum_before"]
close_row = Q.k["close"]
heads = [
    ("First month with positive EBITDA", f"=IF(MIN('P&L monthly'!{FC}{be_row}:{LC}{be_row})=999,\"not reached\",MIN('P&L monthly'!{FC}{be_row}:{LC}{be_row}))", "0", "month #"),
    ("   which is", f"=IF(ISNUMBER(B7),DATE(YEAR(Start_Date),MONTH(Start_Date)+B7-1,1),\"-\")", "mmm yyyy", ""),
    ("Peak funding need (lowest cumulative cash flow before funding)", f"=-MIN(0,MIN('Cash flow'!{FC}{cum_row}:{LC}{cum_row}))", NUM, "FCFA"),
    ("   in euros", "=B9/FX_EUR", NUM, "€"),
    ("Equity raised in the plan", f"=SUM('Cash flow'!{FC}{Q.k['equity']}:{LC}{Q.k['equity']})", NUM, "FCFA"),
    ("   in euros", "=B11/FX_EUR", NUM, "€"),
    ("Lowest closing cash", f"=MIN('Cash flow'!{FC}{close_row}:{LC}{close_row})", NUM, "FCFA"),
    ("   in month", f"=MATCH(B13,'Cash flow'!{FC}{close_row}:{LC}{close_row},0)", "0", "month #"),
    ("Cash at the end of year 5", f"='Cash flow'!{LC}{close_row}", NUM, "FCFA"),
]
for j, (lab, fml, fm, unit) in enumerate(heads):
    r = 7 + j
    D.cell(r, 1, lab).font = F()
    D.cell(r, 2, fml)
    style(D.cell(r, 2), fmt=fm, bold=True)
    D.cell(r, 3, unit).font = F(color=GREY)
D["D13"] = '=IF(B13<0,"Cash goes negative: raise more or earlier (Assumptions, section 10)","OK: cash stays positive")'
style(D["D13"], bold=True, color="C00000")
D["A18"] = "Year by year"
style(D["A18"], bold=True)
for col in range(1, 10):
    D.cell(18, col).fill = SEC_FILL
D["A19"] = "Year"
for j in range(5):
    col = CL(4 + j)
    D[f"{col}19"] = f"='P&L annual'!{col}5"
    style(D[f"{col}19"], fmt="0", bold=True, fill=SEC_FILL, align="center")
dash = [("Active clients (end of year)", "clients", NUM), ("New clients in the year", "new_clients", NUM), ("Headcount (end of year)", "headcount", NUM),
        ("Total revenue", "revenue", NUM), ("Gross margin", "gm", NUM), ("Gross margin %", "gm_pct", PCT), ("Total operating expenses", "opex", NUM),
        ("EBITDA", "ebitda", NUM), ("EBITDA margin", "ebitda_pct", PCT), ("Net income", "ni", NUM), ("Closing cash", "cash", NUM),
        ("Loan book (end of year)", "book", NUM), ("Revenue (€k)", "eur_revenue", NUM), ("EBITDA (€k)", "eur_ebitda", NUM), ("Net income (€k)", "eur_ni", NUM)]
for j, (lab, key, fm) in enumerate(dash):
    r = 20 + j
    D.cell(r, 1, lab).font = F(bold=key in ("revenue", "ebitda", "clients"))
    for jj in range(5):
        col = CL(4 + jj)
        D[f"{col}{r}"] = f"='P&L annual'!{col}{YK[key]}"
        style(D[f"{col}{r}"], fmt=fm, bold=key in ("revenue", "ebitda", "clients"), color=GREEN)
for j, (lab, key, fm) in enumerate([("Revenue per active client a month (ARPA)", "arpa", NUM), ("Blended CAC", "cac", NUM), ("CAC payback (months)", "payback", NUM1)]):
    r = 20 + len(dash) + j
    D.cell(r, 1, lab).font = F()
    for jj in range(5):
        col = CL(4 + jj)
        D[f"{col}{r}"] = f"='Unit economics'!{col}{UK[key]}"
        style(D[f"{col}{r}"], fmt=fm, color=GREEN)
chk = 20 + len(dash) + 4
D.cell(chk, 1, "Checks").font = F(bold=True)
for col in range(1, 10):
    D.cell(chk, col).fill = SEC_FILL
checks = [
    ("New-client mix adds up to 100%", "=IF(ABS(Mix_Petite+Mix_Moyenne+Mix_Grande-1)<0.0001,\"OK\",\"ERROR\")"),
    ("Cost of revenue in the P&L equals variable costs", f"=IF(ABS(SUM('P&L monthly'!{FC}{P.k['cogs']}:{LC}{P.k['cogs']})-SUM('Costs'!{FC}{C.k['v_total']}:{LC}{C.k['v_total']}))<1,\"OK\",\"ERROR\")"),
    ("Opex in the P&L equals fixed costs", f"=IF(ABS(SUM('P&L monthly'!{FC}{P.k['opex']}:{LC}{P.k['opex']})-SUM('Costs'!{FC}{C.k['f_total']}:{LC}{C.k['f_total']}))<1,\"OK\",\"ERROR\")"),
    ("Annual revenue equals monthly revenue", f"=IF(ABS('P&L annual'!I{YK['revenue']}-SUM('P&L monthly'!{FC}{P.k['revenue']}:{LC}{P.k['revenue']}))<1,\"OK\",\"ERROR\")"),
    ("Closing cash never negative", f"=IF(MIN('Cash flow'!{FC}{close_row}:{LC}{close_row})>=0,\"OK\",\"RAISE MORE\")"),
]
for j, (lab, fml) in enumerate(checks):
    r = chk + 1 + j
    D.cell(r, 1, lab).font = F()
    D.cell(r, 2, fml)
    style(D.cell(r, 2), bold=True)

# charts
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.series import SeriesLabel
ch = BarChart()
ch.type = "col"
ch.title = "Revenue, operating expenses and EBITDA (FCFA)"
ch.y_axis.title = "FCFA"
ch.height, ch.width = 8, 17
for key, lab in (("revenue", "Revenue"), ("opex", "Operating expenses"), ("ebitda", "EBITDA")):
    ch.add_data(Reference(Y, min_col=4, max_col=8, min_row=YK[key], max_row=YK[key]), from_rows=True, titles_from_data=False)
    ch.series[-1].tx = SeriesLabel(v=lab)
ch.set_categories(Reference(Y, min_col=4, max_col=8, min_row=5, max_row=5))
D.add_chart(ch, "K4")
lc = LineChart()
lc.title = "Active clients by month"
lc.height, lc.width = 8, 17
lc.add_data(Reference(R.ws, min_col=C0, max_col=C0 + NM - 1, min_row=R.k["act_total"], max_row=R.k["act_total"]), from_rows=True, titles_from_data=False)
lc.series[0].tx = SeriesLabel(v="Active clients")
lc.set_categories(Reference(R.ws, min_col=C0, max_col=C0 + NM - 1, min_row=3, max_row=3))
D.add_chart(lc, "K21")
cc = LineChart()
cc.title = "Closing cash by month (FCFA)"
cc.height, cc.width = 8, 17
cc.add_data(Reference(Q.ws, min_col=C0, max_col=C0 + NM - 1, min_row=Q.k["close"], max_row=Q.k["close"]), from_rows=True, titles_from_data=False)
cc.series[0].tx = SeriesLabel(v="Closing cash")
cc.set_categories(Reference(Q.ws, min_col=C0, max_col=C0 + NM - 1, min_row=3, max_row=3))
D.add_chart(cc, "K38")

# =====================================================================================
# COVER
# =====================================================================================
CV = wb.create_sheet("Cover")
CV.column_dimensions["A"].width = 3
CV.column_dimensions["B"].width = 30
CV.column_dimensions["C"].width = 110
CV["B2"] = "Tabax (working name): business plan model"
CV["B2"].font = F(bold=True, size=16)
CV["B3"] = "B2B neobank for SMEs in Senegal, then Côte d'Ivoire. Five years, monthly, every figure driven by formulas."
CV["B3"].font = F(italic=True, color=GREY)
lines = [
    ("How to use", ""),
    ("1. Pick a scenario", "Assumptions › cell D4: 1 = Prudent, 2 = Base, 3 = Ambitious. Rows with three values switch with it."),
    ("2. Change any input", "Inputs are blue on a cream background (Assumptions, Hiring plan, Market). Everything else is a formula: do not type over it."),
    ("3. Change the team", "Hiring plan: one line per hire (headcount, start month, end month, gross salary). Field sales reps drive client acquisition."),
    ("4. Check the cash", "Dashboard › checks. If cash goes negative, raise more or earlier (Assumptions, section 10)."),
    ("", ""),
    ("Tabs", ""),
    ("Dashboard", "Headline numbers, year-by-year summary and checks."),
    ("Assumptions", "Every hypothesis with its source: timing, acquisition, pricing, usage per client, cost to serve, credit, staff charges, fixed costs by year, funding."),
    ("Hiring plan", "Roles, start months and salaries (employer cost computed with Senegal's charges)."),
    ("Staff", "Headcount and employer cost by month, by department and country."),
    ("Sales & marketing", "New clients by channel (field sales, partners, digital) and country; marketing budget; cost to acquire a client."),
    ("Clients & revenue", "Active clients by plan, usage (cards, balances, payroll, payouts) and every non-credit revenue line."),
    ("Credit", "Loan book by product, interest, cost of funds, losses and the share kept by Tabax; cash tied up by credit."),
    ("Costs", "Variable costs, fixed costs by category, capex and depreciation, month by month."),
    ("P&L monthly", "Revenue, cost of revenue, gross margin, operating expenses, EBITDA, depreciation, tax, net income."),
    ("P&L annual", "Years 1–5, cash and funding, operating figures and a euro view."),
    ("Cash flow", "Monthly cash, cash set aside, funding rounds, runway."),
    ("Unit economics", "ARPA, cost to serve, contribution, CAC, payback, lifetime value, efficiency and credit ratios."),
    ("Market", "Formal employers in Senegal and Côte d'Ivoire, target market and penetration."),
    ("", ""),
    ("Colour code", ""),
    ("Blue on cream", "Input: change freely."),
    ("Black", "Formula on the same sheet."),
    ("Green", "Link to another sheet."),
    ("", ""),
    ("Main caveats", ""),
    ("Estimates to replace", "Partner bank fees, card processor fees and minimums, interchange, the deposit income share, licence-file legal fees, insurance and the cost of wallet payouts have no public price. Replace them with term sheets and quotes."),
    ("Taxes", "Amounts exclude VAT and the 17% tax on financial activities (TAF), which apply to fees. Corporate tax is simplified (30%, losses carried forward without limit)."),
    ("Côte d'Ivoire", "Staff charges use Senegal's rates; the number of formal employers is an estimate."),
    ("Credit", "Loans are made by a partner microfinance institution (SFD) at 0.063% a day (23% a year, under the 24% cap), then by Tabax's own SFD. The loan book itself is funded by debt lines, not equity."),
    ("Sources", "Business model v2, Cost breakdown in euros, Senegal launch plan and the research notes in this project, plus IPRES/ANSD 2024 and CEPICI 2025 for the market."),
]
for j, (a, b) in enumerate(lines):
    r = 5 + j
    CV.cell(r, 2, a).font = F(bold=(b == "" and a != ""), size=11 if b == "" else 10)
    CV.cell(r, 3, b).font = F()
    CV.cell(r, 3).alignment = Alignment(wrap_text=True, vertical="top")
    CV.cell(r, 2).alignment = Alignment(vertical="top")

# sheet order
order = ["Cover", "Dashboard", "Assumptions", "Hiring plan", "Staff", "Sales & marketing", "Clients & revenue", "Credit", "Costs", "P&L monthly", "P&L annual", "Cash flow", "Unit economics", "Market"]
wb._sheets = [wb[n] for n in order]
for ws in wb.worksheets:
    ws.sheet_view.showGridLines = False if ws.title in ("Cover", "Dashboard") else True
wb.active = 0
wb.save(OUT)
print("saved", OUT)
