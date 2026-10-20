"""Kelen business plan: a formula-driven Excel model (5 years, monthly)."""
import datetime, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as CL
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.worksheet.datavalidation import DataValidation

OUT = sys.argv[1]
EQUITY = [float(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 else [900e6, 2000e6, 3000e6]
SERIES_B_MONTH = int(sys.argv[3]) if len(sys.argv) > 3 else 22

wb = Workbook()
FONT = "Arial"
BLUE, GREEN, BLACK, WHITE, GREY = "0000FF", "008000", "000000", "FFFFFF", "595959"
F = lambda bold=False, color=BLACK, size=10, italic=False: Font(name=FONT, bold=bold, color=color, size=size, italic=italic)
FILL = lambda c: PatternFill("solid", fgColor=c)
# Kelen brand: teal 0D7377 headers, its 12% tint for section rows, the app's light neutral for totals. Inputs keep blue on cream.
TEAL, INK = "0D7377", "0F1114"
IN_FILL, HEAD_FILL, SEC_FILL, TOT_FILL, KEY_FILL = FILL("FFF6D5"), FILL(TEAL), FILL("E2EEEF"), FILL("F2F3F5"), FILL("FFFF00")
NUM = '#,##0;(#,##0);"-"'
NUM1 = '#,##0.0;(#,##0.0);"-"'
PCT = '0.0%;(0.0%);"-"'
PCT2 = '0.00%;(0.00%);"-"'
DATEF = 'mmm-yy'
EUR_F = '[<100]"€"#,##0.00;"€"#,##0'
EURN = '"€"#,##0;("€"#,##0);"-"'
FCFA_F = '#,##0" FCFA"'


def equiv(unit, ref):
    """Formula and format for the other-currency equivalent of a money input (None if not money)."""
    u = unit or ""
    if u.startswith("FCFA"):
        return f"={ref}/FX_EUR", EUR_F
    if u.startswith("USD"):
        return f"={ref}*FX_USD/FX_EUR", EUR_F
    if u.startswith("€"):
        return f"={ref}*FX_EUR", FCFA_F
    return None, None
THIN = Side(style="thin", color="D5D8DD")
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
    ws["A1"].font = F(bold=True, size=14, color=TEAL)
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
for col, w in {"A": 2, "B": 52, "C": 16, "D": 15, "E": 15, "F": 15, "G": 15, "H": 18, "I": 90, "J": 3, "K": 16, "L": 16, "M": 16, "N": 16, "O": 16}.items():
    A.column_dimensions[col].width = w
arow = [6]


def a_sec(text, kind="scalar", opt=False):
    r = arow[0] + 1
    A.cell(r, 2, text)
    heads = ["Unit", "Value used", "Option A", "Option B", "Option C", "€ / FCFA equivalent", "Source / note"] if opt else \
        ["Unit", "Value used", "Prudent", "Base", "Ambitious", "€ / FCFA equivalent", "Source / note"] if kind == "scalar" else \
        ["Unit", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Source / note", "", "Y1 (€ / FCFA)", "Y2 (€ / FCFA)", "Y3 (€ / FCFA)", "Y4 (€ / FCFA)", "Y5 (€ / FCFA)"]
    for j, h in enumerate(heads):
        if h:
            A.cell(r, 3 + j, h)
    for j in list(range(2, 10)) + ([11, 12, 13, 14, 15] if kind != "scalar" else []):
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
    fml, fm = equiv(unit, f"D{r}")
    if fml and nm not in ("FX_EUR", "FX_USD"):
        style(A.cell(r, 8, fml), fmt=fm, color=GREY)
    name(nm, f"'Assumptions'!$D${r}")
    arow[0] += 1
    return r


def a_opt(nm, label, values, unit, fmt=NUM, note=""):
    """Input that switches with Pricing_Option (columns E-G = options A, B, C)."""
    r = arow[0]
    A.cell(r, 2, label).font = F()
    A.cell(r, 3, unit).font = F(color=GREY)
    A.cell(r, 4, f"=CHOOSE(Pricing_Option,E{r},F{r},G{r})")
    style(A.cell(r, 4), fmt=fmt)
    for j, v in enumerate(values):
        style(A.cell(r, 5 + j, v), fmt=fmt, color=BLUE, fill=IN_FILL)
    A.cell(r, 9, note).font = F(color=GREY)
    fml, fm = equiv(unit, f"D{r}")
    if fml:
        style(A.cell(r, 8, fml), fmt=fm, color=GREY)
    name(nm, f"'Assumptions'!$D${r}")
    arow[0] += 1
    return r


def a_arr(nm, label, values, unit, fmt=NUM, note=""):
    r = arow[0]
    A.cell(r, 2, label).font = F()
    A.cell(r, 3, unit).font = F(color=GREY)
    for j, v in enumerate(values):
        style(A.cell(r, 4 + j, v), fmt=fmt, color=BLUE, fill=IN_FILL)
        fml, fm = equiv(unit, f"{CL(4 + j)}{r}")
        if fml:
            style(A.cell(r, 11 + j, fml), fmt=fm, color=GREY)
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
a_in("Launch_CI", "Commercial launch, Côte d'Ivoire", 19, "month #", "0", "One month after the Abidjan office opens. Partners hold the licences in Côte d'Ivoire too.")
a_in("Office_Start", "Dakar office (Regus) from", 1, "month #", "0", "Regus from day one: no lease, deposit or fit-out (decision).")
a_in("CI_Office_Start", "Abidjan office (Regus) and first Côte d'Ivoire hires", 18, "month #", "0", "Not before month 18 (decision).")
a_in("PayLinks_Start", "Payment links go live", 18, "month #", "0", "'Bientôt' feature in the app.")
a_in("EmpAcc_Start", "B2C launch: employee salary accounts and personal accounts", 29, "month #", "0", "Not before 2 years of commercial activity: Senegal launch + 24 months (decision).")
a_in("SFD_Acq_Month", "Acquisition of a microfinance company (SFD) closes", 24, "month #", "0", "Around year 2 (decision). Due diligence and the change-of-control approval run during year 2.")
a_in("Own_Funding_Month", "Own SFD lends from", 25, "month #", "0", "Before this month the partner SFD lends and Kelen keeps a share of the margin. Côte d'Ivoire loans stay with a partner: SFD licences are national.")
a_in("Collateral_Month", "Card programme collateral at partner bank", 4, "month #", "0", "")
a_in("Bank_Setup_Month", "Partner bank set-up fee paid, Senegal", 2, "month #", "0", "")
a_in("CI_Bank_Setup_Month", "Partner bank set-up fee paid, Côte d'Ivoire", 16, "month #", "0", "")
a_in("Proc_Setup_Month", "Card processor set-up fee paid", 3, "month #", "0", "")
a_in("Proc_Min_Start", "Card processor monthly minimum starts", 5, "month #", "0", "")
a_in("Cloud_Start", "Cloud hosting starts", 2, "month #", "0", "")
a_in("SFD_Setup_Month", "Partner SFD integration fee paid", 15, "month #", "0", "Partner SFD signed early; integration paid before the first loans.")
a_in("CI_Company_Month", "Côte d'Ivoire subsidiary created", 16, "month #", "0", "Before the first Abidjan hires.")
a_in("Audit_Month", "First tech audit (then every 12 months)", 4, "month #", "0", "Before launch, for the partner bank; repeated yearly.")

a_sec("3. Client acquisition (sales and marketing)")
a_in("Rep_Productivity", "New clients signed per field sales rep per month", None, "clients", NUM1, "Rep counts come from the hiring plan. A rep sells from the month after joining. Base lowered from 10 to 8 after the market analysis (Oct 2026): Julaya had about 2,800 active users in Senegal after six years. Validate in the pilot.", scen=(7, 8, 13))
a_in("CI_Productivity", "Côte d'Ivoire rep productivity vs Senegal", 0.9, "x", "0.00", "Slightly lower at first: new market, brand unknown.")
a_in("Partner_Base_SN", "Partner channel, Senegal: clients a month at launch", None, "clients", NUM1, "Accountants, payroll software (KayFay, Sage, Odoo), chambers of commerce. Base lowered from 10 to 8 after the market analysis (Oct 2026).", scen=(6, 8, 14))
a_in("Partner_Base_CI", "Partner channel, Côte d'Ivoire: clients a month at launch", None, "clients", NUM1, "", scen=(4, 6, 9))
a_in("Partner_Growth", "Partner channel monthly growth", 0.06, "% / month", PCT, "")
a_in("Partner_Cap_SN", "Partner channel cap, Senegal", 80, "clients / month", NUM, "")
a_in("Partner_Cap_CI", "Partner channel cap, Côte d'Ivoire", 60, "clients / month", NUM, "")
a_in("CAC_Digital", "Digital ads cost per signed client", None, "FCFA", NUM, "Media spend only. Meta leads 600–2,800 FCFA; lead-to-client conversion assumed 2–4%.", scen=(100000, 75000, 55000))
a_in("Mix_Petite", "Share of new clients on Essentiel (mostly small firms)", 0.60, "%", PCT, "Plans are chosen by limits and features, not staff count. Small firms (about 5 staff) take Essentiel. The three shares must add up to 100% (see check on the Dashboard).")
a_in("Mix_Moyenne", "Share of new clients on Pro (mostly mid-size firms)", 0.30, "%", PCT, "Firms that need approvals (double signature) or the accounting module, typically 10–50 staff.")
a_in("Mix_Grande", "Share of new clients on Business (mostly large firms)", 0.10, "%", PCT, "")
a_in("Churn_Petite", "Monthly churn, Essentiel", None, "% / month", PCT2, "Small companies leave or close more often.", scen=(0.03, 0.02, 0.015))
a_in("Churn_Moyenne", "Monthly churn, Pro", None, "% / month", PCT2, "", scen=(0.02, 0.0125, 0.01))
a_in("Churn_Grande", "Monthly churn, Business", None, "% / month", PCT2, "", scen=(0.015, 0.0075, 0.005))
a_in("Referral_Fee", "Referral fee per partner-channel client", 25000, "FCFA", NUM, "Paid to accountants and payroll software partners (cost breakdown).")
a_in("Rep_Transport", "Field sales transport allowance per rep", 75000, "FCFA / month", NUM, "50–100k FCFA (cost breakdown).")

a_sec("4. Plans and pricing")
a_in("Pricing_Option", "Pricing option (1 = A acquisition first, 2 = B balanced, 3 = C revenue first)", 2, "option", "0", "Decision (Oct 2026): plans by limits and features, not staff count. B is the base. Switch to compare; prices below change with it. See the Pricing levers tab.")
a_sec("4a. Plan prices (columns E–G are options A, B, C)", opt=True)
a_opt("Price_Petite", "Essentiel plan", (7500, 9900, 9900), "FCFA / month", NUM, "Decision (Oct 2026): package P3. 1 user + 1 invited free, 30 transfers, 1 physical and 2 virtual cards, salaries free up to 3M FCFA a month. Below a bank's micro-business account fee (10,000).")
a_opt("Price_Moyenne", "Pro plan", (17500, 19500, 29900), "FCFA / month", NUM, "Decision (Oct 2026): 19,500 (was 29,900; option C keeps the old price for comparison). 3 users, 150 transfers, 3 physical and 10 virtual cards, approvals, accounting module, salaries free up to 15M FCFA a month.")
a_opt("Price_Grande", "Business plan", (59500, 69500, 89900), "FCFA / month", NUM, "Decision (Oct 2026): 69,500 (was 89,900). 10 users, 500 transfers, 10 physical and unlimited virtual cards, multi-level approvals, API, several companies, adviser, salaries free up to 60M FCFA a month.")
a_sec("4b. Plan limits, add-ons and fees")
a_in("Price_Increase", "Annual price increase", 0.0, "% / year", PCT, "")
a_in("Free_Months", "Free months for every new client", 1, "months", "0", "Decision (Oct 2026): first month free on every plan (was 3).")
a_in("Annual_Share", "Share of clients paying yearly", 0.30, "%", PCT, "")
a_in("Annual_Free", "Months free on yearly billing", 2, "months", "0", "Yearly price = 10 months.")
a_in("Users_Incl_Petite", "Users included, Essentiel", 2, "users", NUM, "1 main user + 1 invited free.")
a_in("Users_Incl_Moyenne", "Users included, Pro", 3, "users", NUM, "")
a_in("Users_Incl_Grande", "Users included, Business", 10, "users", NUM, "")
a_in("Transfers_Incl_Petite", "Transfers included a month, Essentiel", 30, "transfers", NUM, "Decision (Oct 2026): transfers to bank accounts only. Salaries never count; transfers to wallets fall under the mobile money allowance.")
a_in("Transfers_Incl_Moyenne", "Transfers included a month, Pro", 100, "transfers", NUM, "Decision (Oct 2026): 100.")
a_in("Transfers_Incl_Grande", "Transfers included a month, Business", 400, "transfers", NUM, "Decision (Oct 2026): 400.")
a_in("Cards_Phys_Incl_Petite", "Physical cards included, Essentiel", 1, "cards", NUM, "Decision (Oct 2026): the first physical card is free on every plan; the others are paid (one-off fee below). Virtual cards: 2 / 10 / unlimited.")
a_in("Cards_Phys_Incl_Moyenne", "Physical cards included, Pro", 1, "cards", NUM, "")
a_in("Cards_Phys_Incl_Grande", "Physical cards included, Business", 1, "cards", NUM, "")
a_in("Payroll_Free_Petite", "Salaries to bank accounts free up to, Essentiel", 3000000, "FCFA / month", NUM, "Decision (Oct 2026). Above it, each salary to a bank account costs the fee per transfer above the allowance. Average clients stay far below. Salaries to wallets count in the mobile money allowance.")
a_in("Payroll_Free_Moyenne", "Salaries to bank accounts free up to, Pro", 15000000, "FCFA / month", NUM, "")
a_in("Payroll_Free_Grande", "Salaries to bank accounts free up to, Business", 60000000, "FCFA / month", NUM, "")
a_in("Extra_User_Fee", "Extra user beyond the plan", 2500, "FCFA / month", NUM, "")
a_in("Extra_Card_Fee", "Extra physical card beyond the plan", 0, "FCFA / month", NUM, "Decision (Oct 2026): no monthly fee; only the one-off card fee below.")
a_in("MM_Free_Petite", "Mobile money free up to, Essentiel", 200000, "FCFA / month", NUM, "Decision (Oct 2026): every transfer to a wallet (Wave, Orange Money…), salaries included. Fair use: the allowance cannot be split into many tiny transfers.")
a_in("MM_Free_Moyenne", "Mobile money free up to, Pro", 1000000, "FCFA / month", NUM, "")
a_in("MM_Free_Grande", "Mobile money free up to, Business", 5000000, "FCFA / month", NUM, "")
a_in("MM_Fee", "Fee on mobile money above the free amount", 0.0115, "% of amount", PCT2, "Decision (Oct 2026): 1.15%, capped per transfer (below). No deal with the operators yet: Kelen pays 1% capped at 5,000 FCFA. Wave charges 1%.")
a_in("MM_Fee_Cap", "Mobile money fee: cap per transfer", 8500, "FCFA / transfer", NUM, "Decision (Oct 2026). Reached at about 740,000 FCFA per transfer; average transfers (75,000–200,000) stay below it, so it does not change the totals.")
a_in("Card_Fee", "Physical card fee beyond the plan (one-off)", 6500, "FCFA", NUM, "Decision (Oct 2026): 6,500 for printing and delivery of each card beyond the first.")
a_in("FX_Fixed_Fee", "Fee per card payment in foreign currencies", 200, "FCFA / payment", NUM, "Decision (Oct 2026): 200, like Djamo.")
a_in("FX_Avg_Txn", "Average card payment in foreign currencies", 25000, "FCFA", NUM, "Assumption: ads and software subscriptions, about $40. Used to count payments.")
a_in("FX_Fee", "Fee on card spending in foreign currencies", 0.025, "%", PCT2, "Decision (Oct 2026): 2.5% plus a fixed fee per payment (below), like Djamo (3–4% + 200 F). Cost research (Oct 2026): networks charge the issuer about 1.2%; banks charge clients 2–3% (NSIA 2.5%, UBA 2.5–3%, Coris 2% + 500 F), Djamo 3–4% + 200 F. Card spending in FCFA is free.")
a_in("FX_Interchange", "Interchange earned on card spending in foreign currencies", 0, "% of foreign spending", PCT2, "Not in the plan: no partner has agreed to share it. Possible upside if negotiated: see Pricing levers. Card networks pay the issuer (the partner bank) about 0.4–1.2%.")
a_in("Foreign_Spend_Factor", "Card spending in foreign currencies allowed by the FX rules", None, "x", "0.00", "Règlement 06/2024/CM/UEMOA, Art. 47, limits residents' card use abroad to usual travel and personal expenses. Prudent assumes 40% of SME foreign card spending (ads, software) is blocked.", scen=(0.6, 1.0, 1.0))
a_in("Interchange_Share", "Interchange share received on FCFA card spending", 0, "%", PCT2, "Not in the plan: no partner has agreed to share it. Possible upside if negotiated: see Pricing levers. The BCEAO gives the issuer (the partner bank) 20% of the merchant fee, about 0.4–0.7%.")
a_in("Deposit_Share", "Share of bank income on client balances", 0, "% / year", PCT2, "Not in the plan: no partner has agreed to share it. Possible upside if negotiated: see Pricing levers. The partner bank earns about 3–5% a year on client balances.")
a_in("Overage_Fee", "Fee per transfer above the plan allowance", 450, "FCFA", NUM, "Decision (Oct 2026). Allowance: 30 / 150 / 500 transfers to bank accounts a month; salaries and transfers to wallets never count. Also charged on each salary to a bank account above the free amount. Banks charge 3,000–5,000 per interbank transfer.")
a_in("PL_Fee", "Payment links: fee on mobile money collections", 0.012, "%", PCT2, "Decision (Oct 2026): 1.2%. Cost research (Oct 2026): gateways charge 1.5–3% (PayTech 1.5–2%, PayDunya 2.25%, Flutterwave 2%); Wave and Orange merchant 1%. Card and transfer payments are free.")
a_in("PL_Cost", "Payment links: operator and aggregator cost", None, "%", PCT2, "Cost research (Oct 2026): Wave and Orange merchant pricing 1%; gateways 1.5–3%; receiving through PI-SPI is free. Ambitious = direct operator deal or PI-SPI routing.", scen=(0.012, 0.01, 0.005))
a_in("PL_Momo_Share", "Payment links: share collected by mobile money", 0.70, "%", PCT, "The rest by card or transfer, free.")
a_in("PL_Adoption", "Payment links: share of clients using them (at maturity)", 0.25, "%", PCT, "")
a_in("PL_Ramp", "Payment links: months to reach maturity", 12, "months", "0", "")
a_sec("4c. Paid modules")
a_in("Payroll_Mod_Start", "Payroll module goes live", 11, "month #", "0", "Payslips plus the monthly IPRES, CSS and income-tax declarations, built from the salaries Kelen pays. Senegal first, Côte d'Ivoire rules at its launch.")
a_in("Payslip_Fee", "Payroll module: price per payslip", 900, "FCFA / payslip", NUM, "Decision (Oct 2026): 900. Still about 2× cheaper than payroll software (KayFay 1,500–2,500 per payslip, minimum 15,000 a month).")
a_in("Payroll_Mod_Uptake", "Payroll module: share of client employees covered (at maturity)", 0.40, "%", PCT, "Assumption: 40% of clients use it.")
a_in("Payroll_Mod_Ramp", "Payroll module: months to reach maturity", 12, "months", "0", "")
a_in("Payslip_Cost", "Payroll module: cost per payslip", 15, "FCFA / payslip", NUM, "Cost research (Oct 2026): WhatsApp utility message about 2.3 FCFA (Meta, Rest of Africa); Orange SMS 4–10 FCFA; plus computing.")
a_in("Intl_Start", "International supplier payments go live", 13, "month #", "0", "Through the partner bank's foreign-exchange set-up, under the 2024 WAEMU foreign-exchange rules.")
a_in("Intl_Fee", "International payments: fee charged (% of amount)", 0.035, "% of amount", PCT2, "Decision (Oct 2026): Kelen charges what the bank or provider charges (break-even on the rate) and earns the fixed fee below. Banks charge SMEs about 3–4% all-in; Capi Money about 3% (to check). The 0.6% tax on transfers out of the zone is passed on at cost.")
a_in("Intl_Cost", "International payments: cost to Kelen (% of amount)", 0.035, "% of amount", PCT2, "Provider not chosen yet (partner bank, Capi Money or others). Assumed all-in 3.5%, the same as the fee.")
a_in("Intl_Fixed_Fee", "International payments: fixed fee per payment", 750, "FCFA / payment", NUM, "Decision (Oct 2026): Kelen's only margin on international payments.")
a_in("Intl_Avg_Payment", "International payments: average payment", 1000000, "FCFA", NUM, "Assumption, used to count payments for the fixed fee.")
a_in("Intl_Uptake", "International payments: share of clients using them (at maturity)", 0.20, "%", PCT, "Importers: China, Turkey, Dubai, France.")
a_in("Intl_Ramp", "International payments: months to reach maturity", 12, "months", "0", "")

a_sec("5. Usage per client (monthly, by plan)")
a_in("Spend_Dom_Petite", "Card spending in FCFA, Essentiel", 300000, "FCFA / month", NUM, "Business model v2 (assumption).")
a_in("Spend_Dom_Moyenne", "Card spending in FCFA, Pro", 800000, "FCFA / month", NUM, "")
a_in("Spend_Dom_Grande", "Card spending in FCFA, Business", 2500000, "FCFA / month", NUM, "")
a_in("Spend_For_Petite", "Card spending in foreign currencies, Essentiel", 300000, "FCFA / month", NUM, "Ads, software subscriptions, travel.")
a_in("Spend_For_Moyenne", "Card spending in foreign currencies, Pro", 1200000, "FCFA / month", NUM, "")
a_in("Spend_For_Grande", "Card spending in foreign currencies, Business", 3500000, "FCFA / month", NUM, "")
a_in("Balance_Petite", "Average balance, Essentiel", 3000000, "FCFA", NUM, "")
a_in("Balance_Moyenne", "Average balance, Pro", 10000000, "FCFA", NUM, "")
a_in("Balance_Grande", "Average balance, Business", 40000000, "FCFA", NUM, "")
a_in("Emp_Petite", "Employees, Essentiel", 5, "people", NUM, "")
a_in("Emp_Moyenne", "Employees, Pro", 25, "people", NUM, "")
a_in("Emp_Grande", "Employees, Business", 120, "people", NUM, "")
a_in("Supplier_Petite", "Transfers out a month (salaries not counted), Essentiel", 10, "payouts", NUM, "")
a_in("Supplier_Moyenne", "Transfers out a month (salaries not counted), Pro", 40, "payouts", NUM, "")
a_in("Supplier_Grande", "Transfers out a month (salaries not counted), Business", 150, "payouts", NUM, "")
a_in("Overage_Petite", "Paid transfers above the allowance (average per client), Essentiel", 1, "transfers", NUM, "All transfers out above the allowance; the model keeps only the share going to bank accounts (1 − share sent to wallets). Most clients stay inside; about 1 in 10 exceeds it by about 10.")
a_in("Overage_Moyenne", "Paid transfers above the allowance (average per client), Pro", 3, "transfers", NUM, "")
a_in("Overage_Grande", "Paid transfers above the allowance (average per client), Business", 10, "transfers", NUM, "")
a_in("Users_Petite", "Users per client, Essentiel", 2, "users", NUM, "")
a_in("Users_Moyenne", "Users per client, Pro", 4, "users", NUM, "Owner, manager, accountant, assistant.")
a_in("Users_Grande", "Users per client, Business", 12, "users", NUM, "")
a_in("Intl_Vol_Petite", "International payments a month (clients who use them), Essentiel", 650000, "FCFA / month", NUM, "Decision (Oct 2026): about €1,000 / 1.5M / 6M FCFA.")
a_in("Intl_Vol_Moyenne", "International payments a month (clients who use them), Pro", 1500000, "FCFA / month", NUM, "")
a_in("Intl_Vol_Grande", "International payments a month (clients who use them), Business", 6000000, "FCFA / month", NUM, "")
a_in("Cards_New_Petite", "Physical cards ordered at sign-up, Essentiel", 1, "cards", NUM, "")
a_in("Cards_New_Moyenne", "Physical cards ordered at sign-up, Pro", 1, "cards", NUM, "Decision (Oct 2026).")
a_in("Cards_New_Grande", "Physical cards ordered at sign-up, Business", 3, "cards", NUM, "Decision (Oct 2026): 1 free, 2 paid.")
a_in("Cards_Act_Petite", "Active cards (physical + virtual), Essentiel", 2, "cards", NUM, "")
a_in("Cards_Act_Moyenne", "Active cards (physical + virtual), Pro", 6, "cards", NUM, "")
a_in("Cards_Act_Grande", "Active cards (physical + virtual), Business", 10, "cards", NUM, "Decision (Oct 2026).")
a_in("PL_Coll_Petite", "Payment link collections, Essentiel (users)", 800000, "FCFA / month", NUM, "")
a_in("PL_Coll_Moyenne", "Payment link collections, Pro (users)", 3000000, "FCFA / month", NUM, "")
a_in("PL_Coll_Grande", "Payment link collections, Business (users)", 10000000, "FCFA / month", NUM, "")
a_in("Avg_Salary", "Average monthly salary paid through Kelen", 200000, "FCFA", NUM, "SME average; the formal-sector average is higher (about 380,000 FCFA).")
a_in("Wallet_Share", "Share of salaries paid to mobile money wallets", 0.65, "%", PCT, "Decision (Oct 2026): 65%. Global Findex 2025: about 64% of Senegal's private wage earners are paid by phone, 33% into an account; in Côte d'Ivoire 57% are still paid in cash only (market analysis, Oct 2026).")
a_in("Sup_Wallet_Share", "Share of other transfers sent to wallets", 0.40, "%", PCT, "Assumption: suppliers, drivers, small contractors paid on Wave or Orange Money. To check with clients.")
a_in("Sup_Avg_Amount", "Average transfer to a wallet (non-salary)", 75000, "FCFA", NUM, "Decision (Oct 2026): 75,000. To check with clients.")
a_in("MM_Low_Share", "Clients sending half the plan's average to wallets", 0.50, "%", PCT, "Clients are not all average: half send about half the average, 30% the average, the rest 2.25 times the average. Used for the fee above the free amount.")
a_in("MM_Mid_Share", "Clients sending the plan's average to wallets", 0.30, "%", PCT, "")
a_in("EmpAcc_Adoption", "Employees who open a Kelen salary account", 0.20, "%", PCT, "")

a_sec("6. Cost to serve (variable costs)")
a_in("Bank_Fee", "Partner bank fee per business account", None, "FCFA / month", NUM, "Cost research (Oct 2026): no WAEMU bank–fintech deal publishes its terms; UBA CI charges SMEs at least 5,000 retail. Replace with the term sheet.", scen=(4000, 2500, 1500))
a_in("KYB_Cost", "Company screening tool at onboarding (sanctions, adverse media)", 1500, "FCFA / company", NUM, "Tool fee only (estimate, about €2): our support team reviews the company documents (RCCM, NINEA, statutes), and that time is in their salaries.")
a_in("KYC_Cost", "ID check tool per person (document, face match, sanctions)", 900, "FCFA", NUM, "Tool fee only: Sumsub-type service, about €1.2–1.6 per check.")
a_in("KYC_Persons", "People checked per new company", 2, "people", NUM, "Directors and beneficial owners.")
a_in("Card_Proc_Fee", "Card processing per active card", None, "FCFA / month", NUM, "Cost research (Oct 2026): processors (Paymentology, HPS, Visa DPS, GIM-UEMOA) quote privately; proxy: Sudo Nigeria ₦50 per card plus per-authorisation fees. Quote needed.", scen=(1500, 1000, 600))
a_in("Card_Prod_Cost", "Physical card printed and delivered", 4500, "FCFA", NUM, "3,000–6,000 FCFA.")
a_in("Scheme_Rate", "Visa / Mastercard cross-border fees and bank FX margin", None, "% of foreign spending", PCT2, "Cost research (Oct 2026): network cross-border fees about 0.9% plus the partner bank's FX margin on dollars (BCEAO spread about 0.6%; none on euros, which are pegged).", scen=(0.018, 0.015, 0.012))
a_in("Scheme_Fixed", "Visa / Mastercard fixed fees per foreign payment", 250, "FCFA / payment", NUM, "Cost research (Oct 2026): about $0.43 per cross-border transaction (authorisation and clearing, proxy).")
a_in("Fraud_Rate", "Fraud and chargebacks", 0.0015, "% of card spending", PCT2, "0.1–0.3%.")
a_in("MM_Cost_Pct", "Cost of a transfer to a wallet: % of amount", None, "% of amount", PCT2, "No deal yet (Oct 2026): Wave Business and Orange Money charge 1%. Base: 1% capped at 5,000 FCFA per transfer (Wave business cap, secondary source: to verify). Prudent: 1% with no cap. Ambitious: flat price on PI-SPI through the partner bank once negotiated.", scen=(0.01, 0.01, 0))
a_in("MM_Cost_Cap", "Cost of a transfer to a wallet: cap (0 = no cap)", None, "FCFA / transfer", NUM, "", scen=(0, 5000, 0))
a_in("MM_Cost_Flat", "Cost of a transfer to a wallet: flat part", None, "FCFA / transfer", NUM, "PI-SPI business pricing is set freely by each bank: 200 FCFA is a negotiation target, not a quote.", scen=(0, 0, 200))
a_in("Bank_Payout_Cost", "Cost of a salary paid to a bank account", None, "FCFA / payout", NUM, "Cost research (Oct 2026): online transfers 150–2,000 FCFA in bank tariffs; same-bank transfers free.", scen=(400, 200, 75))
a_in("Supplier_Payout_Cost", "Cost of a transfer to a bank account", None, "FCFA / transfer", NUM, "Cost research (Oct 2026): 150 FCFA (SG Sénégal, unconfirmed) to 750 (UBA CI) and 2,000 (BOA Sénégal) per online transfer; above 50M FCFA the RTGS costs 15,000+.", scen=(500, 300, 150))
a_in("Notif_Cost", "SMS, WhatsApp and support tools per client", 350, "FCFA / month", NUM, "Cost research (Oct 2026): WhatsApp utility/authentication about 2.3 FCFA a message, Orange SMS 4–10 FCFA; plus support software seats.")
a_in("Emp_Notif", "Messages per employee account", 30, "FCFA / month", NUM, "Cost research (Oct 2026).")
a_in("EmpAcc_Cost", "Processing per employee account", 150, "FCFA / month", NUM, "About €0.23 (cost breakdown).")

a_sec("7. Credit (lender of record: partner SFD, then own SFD in Senegal)")
a_in("Credit_Mult", "Credit volume multiplier", None, "x", "0.00", "Scales every product's uptake.", scen=(0.6, 1.0, 1.4))
a_in("CoR_Mult", "Credit losses multiplier", None, "x", "0.00", "Scales every product's cost of risk.", scen=(1.5, 1.0, 0.8))
a_in("Credit_Ramp", "Months for a product to reach full uptake", 12, "months", "0", "")
a_in("Start_Factoring", "Factoring: start month", 18, "month #", "0", "No loans before month 18 (decision). Lowest risk: the debtor pays the invoice.")
a_in("Uptake_Factoring", "Factoring: share of active clients using it", 0.05, "%", PCT, "")
a_in("Avg_Factoring", "Factoring: average outstanding per user", 8000000, "FCFA", NUM, "80–90% of invoices, 30–90 days.")
a_in("Yield_Factoring", "Factoring: yield", 0.23, "% / year", PCT, "0.063% a day = 23% a year. All-in: the 24% SFD cap counts fees and insurance, so no extra file fee is modelled.")
a_in("CoR_Factoring", "Factoring: cost of risk", 0.015, "% / year", PCT2, "")
a_in("Start_Bridge", "Payroll bridge: start month", 18, "month #", "0", "")
a_in("Uptake_Bridge", "Payroll bridge: share of active clients", 0.03, "%", PCT, "")
a_in("Avg_Bridge", "Payroll bridge: average outstanding", 3000000, "FCFA", NUM, "Up to one month of payroll, 45 days max.")
a_in("Yield_Bridge", "Payroll bridge: yield", 0.23, "% / year", PCT, "")
a_in("CoR_Bridge", "Payroll bridge: cost of risk", 0.02, "% / year", PCT2, "")
a_in("Start_Line", "Credit line: start month", 21, "month #", "0", "Three months after the first loans, on transaction history.")
a_in("Uptake_Line", "Credit line: share of active clients", 0.08, "%", PCT, "")
a_in("Avg_Line", "Credit line: average drawn", 1500000, "FCFA", NUM, "5–30% of monthly inflows.")
a_in("Yield_Line", "Credit line: yield", 0.23, "% / year", PCT, "")
a_in("CoR_Line", "Credit line: cost of risk", 0.045, "% / year", PCT2, "Cost research (Oct 2026): large WAEMU microfinance institutions 4.3% net bad loans (2025); Advans CI PAR30 4.64%.")
a_in("Start_Term", "Equipment / term loans: start month", 27, "month #", "0", "Longer loans once the own SFD lends.")
a_in("Uptake_Term", "Term loans: share of active clients", 0.02, "%", PCT, "")
a_in("Avg_Term", "Term loans: average outstanding", 10000000, "FCFA", NUM, "1–50M FCFA, 6–24 months.")
a_in("Yield_Term", "Term loans: yield", 0.22, "% / year", PCT, "")
a_in("CoR_Term", "Term loans: cost of risk", 0.04, "% / year", PCT2, "Cost research (Oct 2026): same benchmarks.")
a_in("Start_Advance", "Salary advances: start month", 30, "month #", "0", "B2C product: after employee accounts open. Retention product, not a profit centre.")
a_in("Usage_Advance", "Salary advances: share of employee accounts with an advance", 0.10, "%", PCT, "")
a_in("Avg_Advance", "Salary advances: average outstanding", 50000, "FCFA", NUM, "Up to 50% of pay already earned.")
a_in("Yield_Advance", "Salary advances: yield", 0.23, "% / year", PCT, "")
a_in("CoR_Advance", "Salary advances: cost of risk", 0.015, "% / year", PCT2, "")
a_in("CoF", "Cost of funds", 0.09, "% / year", PCT, "8–10% (DFI lines, local debt).")
a_in("Servicing", "External servicing and collections", 0.01, "% / year", PCT, "Credit staff are in the hiring plan.")
a_in("Partner_Share", "Kelen share of the net margin while the partner SFD funds", 0.50, "%", PCT, "Negotiated; Kelen provides first-loss cover.")
a_in("First_Loss", "First-loss cash reserve (partner phase)", 0.10, "% of book", PCT, "")
a_in("Capital_Ratio", "Equity needed per FCFA lent (own SFD phase)", 0.15, "% of book", PCT, "The rest funded by debt lines (not modelled in the P&L except the cost of funds).")

a_sec("8. Team, offices and tools")
a_in("Employer_Charges", "Employer charges and taxes on top of the gross salary", 0.30, "% of gross", PCT, "All-in: social security, pension, health and payroll taxes, about 30% (decision).")
a_in("Support_Start", "Customer support: first agents join", 4, "month #", "0", "One month before the Senegal launch.")
a_in("Support_Min", "Customer support: starting team", 2, "people", NUM, "Decision. Agents also run onboarding checks with the partner.")
a_in("Clients_per_Support", "Customer support: active business clients per agent", 500, "clients", NUM, "Estimate. The team grows with the client base.")
a_in("EmpAcc_per_Support", "Customer support: B2C accounts per extra agent", 5000, "accounts", NUM, "From the B2C launch.")
a_in("Salary_Support", "Customer support agent: gross salary", 280000, "FCFA / month", NUM, "Decision (Oct 2026): 280,000, what the team is paid today. Support and onboarding (KYC) work.")
a_in("Devs_Min", "Developers: starting team (CTO not included)", 2, "people", NUM, "Decision.")
a_in("Clients_per_Dev", "Developers: one more per this many active clients", 2000, "clients", NUM, "Estimate. Maak's platform covers the core; developers adapt and extend it.")
a_in("Salary_Dev", "Developer: gross salary", 1200000, "FCFA / month", NUM, "Blend of senior (1.5M) and mid-level (0.8M) developers in Dakar.")
a_in("Reps_Start", "Field sales: first reps join", 4, "month #", "0", "One month before the Senegal launch.")
a_in("Reps_Min_SN", "Field sales reps, Senegal: starting team", 2, "people", NUM, "Plus the sales lead on the hiring plan: 3 sellers at launch (decision: 'a few sales').")
a_in("Reps_Min_CI", "Field sales reps, Côte d'Ivoire: starting team", 2, "people", NUM, "From the Abidjan opening.")
a_in("Clients_per_Rep", "Field sales: one rep per this many active clients in the country", 400, "clients", NUM, "Estimate. Based on the previous month's clients, so the team follows the client base.")
a_in("Salary_Rep_SN", "Field sales rep, Senegal: gross salary", 400000, "FCFA / month", NUM, "300k fixed + about 100k commission.")
a_in("Salary_Rep_CI", "Field sales rep, Côte d'Ivoire: gross salary", 450000, "FCFA / month", NUM, "")
a_in("Credit_Lead_Months", "Credit team joins this many months before the first loans", 2, "months", "0", "Financial experts are added when loans start (decision).")
a_in("Book_per_Credit", "Credit analysts and collections: one per this loan book", 1000000000, "FCFA", NUM, "Estimate. Minimum one from the start of credit.")
a_in("Salary_Credit", "Credit analyst: gross salary", 600000, "FCFA / month", NUM, "")
a_in("Regus_EUR", "Office: Regus, all included", 300, "€ / employee / month", NUM, "Desk, electricity, internet, cleaning and security included (decision). Dakar from month 1, Abidjan from its opening.")
a_in("Laptop_EUR", "Laptop per new hire (non-developers)", 500, "€ / hire", NUM, "Decision: at most €500. Expensed in the month of hiring (no depreciation).")
a_in("Laptop_Dev_USD", "MacBook per new developer and the CTO", 2000, "USD / hire", NUM, "Decision: about $2,000.")
a_in("Agency_Fee_EUR", "Recruitment agency fee per senior hire", 800, "€ / hire", NUM, "Decision: about €800 per hire for the CEO, CTO, developers, financial and credit experts, country manager and compliance officer. Other roles are hired directly at no fee.")
a_in("Agency_Dev", "Developers hired through an agency (1 = yes, 0 = no)", 1, "flag", "0", "")
a_in("Agency_Credit", "Credit analysts hired through an agency (1 = yes, 0 = no)", 1, "flag", "0", "")
a_in("Agency_Support", "Customer support hired through an agency (1 = yes, 0 = no)", 0, "flag", "0", "Hired directly (decision).")
a_in("Agency_Rep", "Field sales reps hired through an agency (1 = yes, 0 = no)", 0, "flag", "0", "Hired directly.")
a_in("Phone_Cost", "Phone and data plan per employee", 5000, "FCFA / month", NUM, "Decision: about 5,000 FCFA.")
a_in("Gmail_USD", "Google Workspace (Gmail) per user", 9, "USD / user / month", NUM, "Decision: about $9.")
a_in("ClickUp_USD", "ClickUp per user", 9, "USD / user / month", NUM, "Decision: same price as Gmail.")
a_in("Claude_USD", "Claude Enterprise seat", 25, "USD / seat / month", NUM, "Decision. One seat per developer and the CTO, plus the shared seats below.")
a_in("Claude_Shared", "Shared Claude seats", 2, "seats", NUM, "One for support and marketing together, one for everyone else who needs it.")
a_in("Website_USD", "Website builder", 25, "USD / month", NUM, "Decision: the group's site tool.")
a_in("Domain_USD", "Domain name", 20, "USD / year", NUM, "")

a_sec("9. Technology from Maak (group company)")
a_in("Maak_Option", "Deal with Maak (1 = lease, 2 = equity)", 1, "option", "0", "1: Kelen pays a yearly lease, lease-to-own. 2: Maak takes a small stake in Kelen instead and there is no lease cost. Either way, adapting the platform to Kelen is included.")
a_in("Maak_Lease_EUR", "Lease of Maak's platform (option 1)", 70000, "€ / year", NUM, "Decision: about 70k a year, paid monthly from month 1, for 3 years. TO VALIDATE with Maak. Includes adapting the platform to Kelen's products.")
a_in("Maak_Lease_Months", "Lease length (then Kelen owns the platform)", 36, "months", "0", "Decision (Oct 2026): the lease stops after 3 years and the technology is Kelen's.")
a_in("Maak_Maint_USD", "Maak upgrades and maintenance after the lease", 40000, "USD / year", NUM, "Decision (Oct 2026): from the end of the lease to the end of the plan.")
a_in("Maak_Equity_Pct", "Maak's stake in Kelen (option 2)", 0.05, "% of Kelen", PCT, "Assumption for 'a small %'. No cash cost; shown on the Dashboard.")
a_in("Tech_Audit_USD", "Tech audit", 10000, "USD", NUM, "Reference price (decision). Before launch, then once a year.")

a_sec("10. Fixed costs by year", kind="arr")
A.cell(arow[0], 2, "Technology").font = F(bold=True)
arow[0] += 1
a_arr("Cloud_USD", "Cloud hosting", [3000, 5000, 8000, 10000, 12000], "USD / month", NUM, "Check whether Maak's lease includes hosting. No AWS/GCP region in WAEMU; CDP authorisation for data abroad.")
a_in("KYC_Min_USD", "Identity-check vendor monthly minimum", 150, "USD / month", NUM, "Cost research (Oct 2026): Sumsub-type vendors charge $149–299 a month minimum; the usage fees below count towards it.")
a_arr("Credit_Bureau", "Credit bureau membership and reports", [0, 4500000, 6000000, 8000000, 10000000], "FCFA / year", NUM, "Cost research (Oct 2026): BIC UEMOA (Creditinfo VoLo) 3.8M FCFA a year for banks and financial institutions (1.8M for large SFDs) plus 400–1,000 FCFA per report. From the first loans.")
a_arr("Monitoring_USD", "Transaction monitoring and sanctions screening", [9000, 20000, 30000, 40000, 50000], "USD / year", NUM, "Cost research (Oct 2026): screening starter plans $99–319 a month exclude monitoring; usage-based monitoring about $0.02 per transaction.")
a_arr("Freelance", "Freelance QA testing and DevOps on-call", [7900000, 9800000, 5900000, 5900000, 5900000], "FCFA / year", NUM, "Design is done in-house with Claude Design (decision). About €12k in year 1, €15k in year 2, then €9k a year.")
a_arr("Proc_Min_USD", "Card processor monthly minimum", [5000, 5000, 7500, 10000, 12000], "USD / month", NUM, "Kelen pays the higher of this minimum and the per-card fees.")
r_proc = arow[0]
A.cell(r_proc, 2, "Card processor set-up fee (one-off)").font = F()
A.cell(r_proc, 3, "USD").font = F(color=GREY)
style(A.cell(r_proc, 4, 50000), fmt=NUM, color=BLUE, fill=IN_FILL)
style(A.cell(r_proc, 11, f"=D{r_proc}*FX_USD/FX_EUR"), fmt=EUR_F, color=GREY)
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
    style(A.cell(r, 11, f"=D{r}/FX_EUR"), fmt=EUR_F, color=GREY)
    A.cell(r, 9, note).font = F(color=GREY)
    name(nm, f"'Assumptions'!$D${r}")
    arow[0] += 1
a_arr("Bank_Min_SN", "Partner bank platform minimum, Senegal", [1500000, 1500000, 2000000, 2000000, 2000000], "FCFA / month", NUM, "From the Senegal launch.")
a_arr("Bank_Min_CI", "Partner bank platform minimum, Côte d'Ivoire", [0, 1500000, 2000000, 2000000, 2000000], "FCFA / month", NUM, "From the Côte d'Ivoire launch.")
a_arr("SFD_Annual", "Partner SFD running fees", [0, 3000000, 3000000, 3000000, 3000000], "FCFA / year", NUM, "Still needed after the acquisition for Côte d'Ivoire loans.")
A.cell(arow[0], 2, "Legal, regulatory and audit").font = F(bold=True)
arow[0] += 1
for nm, label, v, note in [("Company_Setup_SN", "Company set-up, Senegal (one-off, month 1)", 2500000, "1.5–3M FCFA excluding capital."),
                           ("Company_Setup_CI", "Company set-up, Côte d'Ivoire (one-off)", 3000000, "")]:
    r = arow[0]
    A.cell(r, 2, label).font = F()
    A.cell(r, 3, "FCFA").font = F(color=GREY)
    style(A.cell(r, 4, v), fmt=NUM, color=BLUE, fill=IN_FILL)
    style(A.cell(r, 11, f"=D{r}/FX_EUR"), fmt=EUR_F, color=GREY)
    A.cell(r, 9, note).font = F(color=GREY)
    name(nm, f"'Assumptions'!$D${r}")
    arow[0] += 1
a_arr("SFD_Project", "SFD acquisition: due diligence, counsel and approval file", [0, 40000000, 10000000, 0, 0], "FCFA / year", NUM, "Estimate. Year 2: target search, due diligence, change-of-control file; year 3: integration.")
a_arr("SFD_Running", "Own SFD running costs (board, regulatory reporting, systems)", [36000000, 36000000, 42000000, 48000000, 54000000], "FCFA / year", NUM, "ESTIMATE, from the acquisition month only. Replace after due diligence (the SFD's own staff and revenue).")
a_arr("Legal_Counsel", "Ongoing legal counsel", [1000000, 1500000, 2000000, 2500000, 3000000], "FCFA / month", NUM, "")
a_arr("Auditor", "Statutory auditor", [5000000, 10000000, 25000000, 30000000, 35000000], "FCFA / year", NUM, "Two entities from year 2; the SFD adds a regulated audit from year 3.")
a_arr("Accountant_Ext", "External chartered accountant and tax adviser", [300000, 600000, 800000, 900000, 1000000], "FCFA / month", NUM, "")
a_arr("AML_Audit", "Independent AML audit", [0, 0, 12000000, 14000000, 16000000], "FCFA / year", NUM, "From the own SFD (year 3). Before that the partners carry the AML obligations.")
a_arr("Data_Protection", "Data-protection filings (CDP, ARTCI)", [3500000, 3000000, 1500000, 1500000, 1500000], "FCFA / year", NUM, "")
a_arr("Insurance_USD", "Insurance: professional liability, cyber, directors", [20000, 25000, 35000, 45000, 55000], "USD / year", NUM, "")
A.cell(arow[0], 2, "Sales and marketing (non-staff)").font = F(bold=True)
arow[0] += 1
a_arr("Digital_SN", "Digital ads budget, Senegal", [1310000, 2620000, 3940000, 4590000, 5250000], "FCFA / month", NUM, "From the Senegal launch. Drives digital clients through the cost per client above.")
a_arr("Digital_CI", "Digital ads budget, Côte d'Ivoire", [0, 1310000, 2620000, 3280000, 3940000], "FCFA / month", NUM, "From the Côte d'Ivoire launch.")
a_arr("Brand_PR", "Brand, launch events, PR", [16400000, 5250000, 6560000, 6560000, 6560000], "FCFA / year", NUM, "The website itself is under Technology (site tool).")
a_arr("Events", "Events, sponsorships, sales materials", [9840000, 19700000, 29500000, 36100000, 42600000], "FCFA / year", NUM, "")
A.cell(arow[0], 2, "Other").font = F(bold=True)
arow[0] += 1
a_arr("Travel", "Travel (Dakar–Abidjan, regulators, partners)", [5250000, 13100000, 16400000, 19700000, 23000000], "FCFA / year", NUM, "")
a_arr("Misc", "Company bank fees and miscellaneous", [300000, 450000, 600000, 700000, 800000], "FCFA / month", NUM, "")

a_sec("11. Cash, capital and funding")
a_in("Opening_Cash", "Cash at month 1 before the first round", 0, "FCFA", NUM, "")
a_in("Card_Collateral", "Card programme collateral at the partner bank", 60000000, "FCFA", NUM, "To quote.")
a_in("SFD_Acquisition", "Acquisition of a microfinance company (SFD)", 650000000, "FCFA", NUM, "Estimate (≈ €990k) for a small Senegalese SFD. Recent deals: Microsen (9.3bn FCFA assets) to SF Capital and Kajas (5.75bn) to Witti, prices not disclosed, Kajas by capital increase; small SFDs trade at or below 1× book (market analysis, Oct 2026).")
a_in("Seed_Month", "Seed round: month", 1, "month #", "0", "")
a_in("Seed_Amount", "Seed round: amount", EQUITY[0], "FCFA", NUM, "Adjust to keep closing cash above zero (see Cash flow).")
a_in("SeriesA_Month", "Series A: month", 15, "month #", "0", "")
a_in("SeriesA_Amount", "Series A: amount", EQUITY[1], "FCFA", NUM, "")
a_in("SeriesB_Month", "Series B: month", SERIES_B_MONTH, "month #", "0", "Funds the SFD acquisition and the credit book's equity.")
a_in("SeriesB_Amount", "Series B: amount", EQUITY[2], "FCFA", NUM, "")
A.freeze_panes = "C6"

# =====================================================================================
# HIRING PLAN (input table)
# =====================================================================================
H = wb.create_sheet("Hiring plan")
title(H, "Hiring plan", "One line per hire or group of identical hires. Edit headcount, start month, end month (leave blank if they stay) and gross salary. Spare lines at the bottom for new roles.")
heads = ["#", "Department", "Role", "Country", "Category", "Headcount", "Start month", "End month", "Gross salary (FCFA / month)", "Agency hire (Y/N)", "Employer cost per person (FCFA / month)", "Note", "Gross salary (€ / month)", "Employer cost per person (€ / month)"]
for j, h in enumerate(heads):
    c = H.cell(4, 1 + j, h)
    c.font = F(bold=True, color=WHITE)
    c.fill = HEAD_FILL
    c.alignment = Alignment(wrap_text=True, vertical="top")
for col, w in {"A": 5, "B": 22, "C": 44, "D": 9, "E": 12, "F": 11, "G": 11, "H": 11, "I": 16, "J": 10, "K": 18, "L": 60, "M": 14, "N": 16}.items():
    H.column_dimensions[col].width = w
H.row_dimensions[4].height = 42
DEPTS = ["Leadership", "Engineering & product", "Compliance & risk", "Credit", "Operations & support", "Sales & partnerships", "Marketing", "Finance & admin"]
HIRES = [
    ("Leadership", "CEO (full salary from year 2)", "SN", "", 1, 13, None, 2500000, "Y", "Founders and shareholders run the company unpaid in year 1 (decision)."),
    ("Engineering & product", "CTO (also codes)", "SN", "", 1, 1, None, 2500000, "Y", "Developers are added with volume on the Staff sheet (2 at the start)."),
    ("Finance & admin", "Financial expert (finance, partners, credit lead)", "SN", "", 1, 1, None, 1500000, "Y", "Starting team. Credit analysts are added with the loan book."),
    ("Sales & partnerships", "Sales lead (also sells; incl. bonus)", "SN", "Sales rep", 1, 1, None, 1200000, "N", "Plus 2 field reps from month 4, then reps grow with clients (Staff sheet)."),
    ("Marketing", "Marketing manager (senior)", "SN", "", 1, 4, None, 900000, "N", "Prepares the launch; runs digital ads and partnerships."),
    ("Marketing", "Marketing officer (junior)", "SN", "", 1, 5, None, 400000, "N", "Content, social media, events."),
    ("Leadership", "Country manager, Abidjan", "CI", "", 1, "=CI_Office_Start", None, 2800000, "Y", "Joins when the Abidjan office opens."),
    ("Compliance & risk", "Compliance officer (AML/CFT)", "SN", "", 1, "=SFD_Acq_Month", None, 1500000, "Y", "Required once Kelen holds its own licence (SFD)."),
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
        style(c, fmt=NUM if j in (4, 7) else ("0" if j in (5, 6) else None), color=BLACK if str(v).startswith("=") else BLUE, fill=IN_FILL)
    H.cell(r, 11, f'=IF(I{r}="",0,I{r}*(1+Employer_Charges))')
    style(H.cell(r, 11), fmt=NUM)
    H.cell(r, 12, note).font = F(color=GREY)
    for col_, src in ((13, "I"), (14, "K")):
        style(H.cell(r, col_, f'=IF(N({src}{r})=0,0,{src}{r}/FX_EUR)'), fmt=EURN, color=GREY)
dv_dep.add(f"B{H0}:B{HN}")
dv_cty.add(f"D{H0}:D{HN}")
dv_cat.add(f"E{H0}:E{HN}")
dv_yn.add(f"J{H0}:J{HN}")
H.cell(HN + 2, 2, "Employer cost = gross salary × (1 + employer charges), 30% on Assumptions section 8. Customer support, developers, field sales reps and credit analysts grow with volume: see the Staff sheet and the ratios on Assumptions section 8.").font = F(italic=True, color=GREY)
H.freeze_panes = "D5"
HR = lambda col: f"'Hiring plan'!${col}${H0}:${col}${HN}"


# =====================================================================================
# Time-series sheet helper
# =====================================================================================
class TS:
    def __init__(self, nm, desc):
        self.ws = wb.create_sheet(nm)
        self.name, self.r, self.k, self.secs = nm, 7, {}, set()
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
        self.secs.add(self.r)
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
# Roles that grow with volume: rows are reserved here and their formulas written once the client and credit sheets exist (fill_volume_team below).
VD = [("support", "Customer support agents", "Operations & support", "SN", "Salary_Support"),
      ("devs", "Developers", "Engineering & product", "SN", "Salary_Dev"),
      ("reps_sn", "Field sales reps, Senegal", "Sales & partnerships", "SN", "Salary_Rep_SN"),
      ("reps_ci", "Field sales reps, Côte d'Ivoire", "Sales & partnerships", "CI", "Salary_Rep_CI"),
      ("credit", "Credit analysts and collections", "Credit", "SN", "Salary_Credit")]
S.sec("Team that grows with volume")
for key, lab, dep, cty, sal in VD:
    S.line(f"vd_{key}", f"{lab} · {cty}", lambda c, p, i: "=0", unit="people", total="max")
for key, lab, dep, cty, sal in VD:
    S.line(f"vdc_{key}", f"Employer cost: {lab}",
           lambda c, p, i, key=key, sal=sal: f"={c}{S.k['vd_' + key]}*{sal}*(1+Employer_Charges)*(1+Salary_Raise)^({c}$5-1)")
S.line("vd_hires", "New hires in these roles", lambda c, p, i: "=" + "+".join(
    (f"{c}{S.k['vd_' + key]}" if i == 0 else f"MAX(0,{c}{S.k['vd_' + key]}-{p}{S.k['vd_' + key]})") for key, *_ in VD), unit="people")
vd_sum = lambda c, pred: "+".join(f"{c}{S.k['vd_' + key]}" for key, lab, dep, cty, sal in VD if pred(dep, cty)) or "0"
vdc_sum = lambda c, pred: "+".join(f"{c}{S.k['vdc_' + key]}" for key, lab, dep, cty, sal in VD if pred(dep, cty)) or "0"
S.sec("Summary")
S.line("hc_total", "Total headcount", lambda c, p, i: f"=SUM({c}{HC1}:{c}{HCN})+{vd_sum(c, lambda d, t: True)}", unit="people", total="last", bold=True)
S.line("hc_sn", "Headcount, Senegal", lambda c, p, i: f"=SUMIF({HR('D')},\"SN\",{c}{HC1}:{c}{HCN})+{vd_sum(c, lambda d, t: t == 'SN')}", unit="people", total="last")
S.line("hc_ci", "Headcount, Côte d'Ivoire", lambda c, p, i: f"=SUMIF({HR('D')},\"CI\",{c}{HC1}:{c}{HCN})+{vd_sum(c, lambda d, t: t == 'CI')}", unit="people", total="last")
S.line("hc_eng", "Engineering headcount (CTO and developers)", lambda c, p, i: f"=SUMIF({HR('B')},\"Engineering & product\",{c}{HC1}:{c}{HCN})+{c}{S.k['vd_devs']}", unit="people", total="last")
S.line("reps_sn", "Field sales reps, Senegal", lambda c, p, i: f"=SUMIFS({c}{HC1}:{c}{HCN},{HR('E')},\"Sales rep\",{HR('D')},\"SN\")+{c}{S.k['vd_reps_sn']}", unit="people", total="last")
S.line("reps_ci", "Field sales reps, Côte d'Ivoire", lambda c, p, i: f"=SUMIFS({c}{HC1}:{c}{HCN},{HR('E')},\"Sales rep\",{HR('D')},\"CI\")+{c}{S.k['vd_reps_ci']}", unit="people", total="last")
S.line("hires", "New hires this month", lambda c, p, i: f"=SUMPRODUCT(--({HR('G')}={c}$3),{HR('F')})+{c}{S.k['vd_hires']}", unit="people")
S.line("hires_eng", "of which CTO and developers (MacBooks)", lambda c, p, i: f"=SUMPRODUCT(--({HR('G')}={c}$3),--({HR('B')}=\"Engineering & product\"),{HR('F')})+"
       + (f"{c}{S.k['vd_devs']}" if i == 0 else f"MAX(0,{c}{S.k['vd_devs']}-{p}{S.k['vd_devs']})"), unit="people")
for d in DEPTS:
    S.line(f"hcd_{d}", f"Headcount: {d}", lambda c, p, i, d=d: f"=SUMIF({HR('B')},\"{d}\",{c}{HC1}:{c}{HCN})+{vd_sum(c, lambda dd, t, d=d: dd == d)}", unit="people", total="last")
for d in DEPTS:
    S.line(f"dep_{d}", f"Staff cost: {d}", lambda c, p, i, d=d: f"=SUMIF({HR('B')},\"{d}\",{c}{CO1}:{c}{CON})+{vdc_sum(c, lambda dd, t, d=d: dd == d)}")
S.line("staff_total", "Total staff cost", lambda c, p, i: f"=SUM({c}{CO1}:{c}{CON})+{vdc_sum(c, lambda d, t: True)}", bold=True)


def fill_volume_team():
    """Write the volume-driven headcount formulas (needs the Clients & revenue and Credit sheets)."""
    first_loan = "MIN(Start_Factoring,Start_Bridge,Start_Line,Start_Term)-Credit_Lead_Months"
    for i, c in enumerate(COLS):
        p = COLS[i - 1] if i else None
        prv = lambda sheet, key: f"{sheet.ref(key, p)}" if p else "0"
        f = {
            "support": f"=IF({c}$3>=Support_Start,MAX(Support_Min,ROUNDUP({R.ref('act_total', c)}/Clients_per_Support+{R.ref('emp_acc', c)}/EmpAcc_per_Support,0)),0)",
            "devs": f"=Devs_Min+ROUNDDOWN({R.ref('act_total', c)}/Clients_per_Dev,0)",
            "reps_sn": f"=IF({c}$3>=Reps_Start,MAX(Reps_Min_SN,ROUNDUP({prv(R, 'act_sn')}/Clients_per_Rep,0)),0)",
            "reps_ci": f"=IF({c}$3>=CI_Office_Start,MAX(Reps_Min_CI,ROUNDUP({prv(R, 'act_ci')}/Clients_per_Rep,0)),0)",
            "credit": f"=IF({c}$3>={first_loan},MAX(1,ROUNDUP({prv(K, 'book')}/Book_per_Credit,0)),0)",
        }
        for key, *_ in VD:
            S.ws[f"{c}{S.k['vd_' + key]}"] = f[key]


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
M.line("new_p", "of which Essentiel", lambda c, p, i: f"={c}{M.k['new_total']}*Mix_Petite", unit="clients", fmt=NUM1)
M.line("new_m", "of which Pro", lambda c, p, i: f"={c}{M.k['new_total']}*Mix_Moyenne", unit="clients", fmt=NUM1)
M.line("new_g", "of which Business", lambda c, p, i: f"={c}{M.k['new_total']}*Mix_Grande", unit="clients", fmt=NUM1)
M.line("new_partner", "New clients from partners (for referral fees)", lambda c, p, i: f"={c}{M.k['part_sn']}+{c}{M.k['part_ci']}", unit="clients", fmt=NUM1)
M.sec("Sales and marketing budget (non-staff)")
M.line("c_digital", "Digital ads", lambda c, p, i: f"={c}{M.k['dig_b_sn']}+{c}{M.k['dig_b_ci']}")
M.line("c_brand", "Brand, launch events, PR", lambda c, p, i: f"={yr('Brand_PR', c)}/12")
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
DISP = {"Petite": "Essentiel", "Moyenne": "Pro", "Grande": "Business"}
R = TS("Clients & revenue", "Active clients by plan, usage and every revenue line except credit (see Credit).")
R.sec("New clients by plan")
for pl, key in (("Petite", "p"), ("Moyenne", "m"), ("Grande", "g")):
    R.line(f"new_{key}", f"New clients, {DISP[pl]}", lambda c, p, i, key=key: f"={M.ref('new_' + key, c)}", unit="clients", fmt=NUM1, color=GREEN)
R.sec("Active clients (end of month)")
for pl, key in (("Petite", "p"), ("Moyenne", "m"), ("Grande", "g")):
    R.line(f"act_{key}", f"Active clients, {DISP[pl]}",
           lambda c, p, i, key=key, pl=pl: f"={c}{R.k['new_' + key]}" if i == 0 else f"={p}{R.k['act_' + key]}*(1-Churn_{pl})+{c}{R.k['new_' + key]}",
           unit="clients", fmt=NUM, total="last")
R.line("act_total", "Active clients, total", lambda c, p, i: f"={c}{R.k['act_p']}+{c}{R.k['act_m']}+{c}{R.k['act_g']}", unit="clients", total="last", bold=True)
R.line("churn_blend", "Blended monthly churn (by sales mix)", lambda c, p, i: "=Mix_Petite*Churn_Petite+Mix_Moyenne*Churn_Moyenne+Mix_Grande*Churn_Grande", unit="%", fmt=PCT2, total=None)
R.line("act_sn", "Active clients, Senegal (approx.)", lambda c, p, i: f"={M.ref('new_sn', c)}" if i == 0 else f"={p}{R.r}*(1-{c}{R.k['churn_blend']})+{M.ref('new_sn', c)}", unit="clients", total="last")
R.line("act_ci", "Active clients, Côte d'Ivoire (approx.)", lambda c, p, i: f"={M.ref('new_ci', c)}" if i == 0 else f"={p}{R.r}*(1-{c}{R.k['churn_blend']})+{M.ref('new_ci', c)}", unit="clients", total="last")
R.sec("Clients in their free months, and paying clients")
for pl, key in (("Petite", "p"), ("Moyenne", "m"), ("Grande", "g")):
    nr = R.k["new_" + key]
    R.line(f"free_{key}", f"In free months, {DISP[pl]}", lambda c, p, i, nr=nr: f"=IF(Free_Months<=0,0,SUM(OFFSET({c}{nr},0,1-MIN(Free_Months,{c}$3),1,MIN(Free_Months,{c}$3))))", unit="clients", fmt=NUM, total=None)
for pl, key in (("Petite", "p"), ("Moyenne", "m"), ("Grande", "g")):
    R.line(f"pay_{key}", f"Paying clients, {DISP[pl]}", lambda c, p, i, key=key: f"=MAX(0,{c}{R.k['act_' + key]}-{c}{R.k['free_' + key]})", unit="clients", fmt=NUM, total="last")
R.sec("Usage")
mix3 = lambda c, base: f"{c}{R.k['act_p']}*{base}_Petite+{c}{R.k['act_m']}*{base}_Moyenne+{c}{R.k['act_g']}*{base}_Grande"
R.line("employees", "Employees of active clients", lambda c, p, i: f"={mix3(c, 'Emp')}", unit="people", total="last")
R.line("emp_acc", "Employee salary accounts", lambda c, p, i: f"=IF({c}$3>=EmpAcc_Start,{c}{R.k['employees']}*EmpAcc_Adoption,0)", unit="accounts", total="last")
R.line("cards_issued", "Physical cards issued", lambda c, p, i: f"={c}{R.k['new_p']}*Cards_New_Petite+{c}{R.k['new_m']}*Cards_New_Moyenne+{c}{R.k['new_g']}*Cards_New_Grande", unit="cards", fmt=NUM1)
R.line("cards_paid", "Physical cards beyond the plan, ordered", lambda c, p, i: f"={c}{R.k['new_p']}*MAX(0,Cards_New_Petite-Cards_Phys_Incl_Petite)+{c}{R.k['new_m']}*MAX(0,Cards_New_Moyenne-Cards_Phys_Incl_Moyenne)+{c}{R.k['new_g']}*MAX(0,Cards_New_Grande-Cards_Phys_Incl_Grande)", unit="cards", fmt=NUM1)
R.line("cards_active", "Active cards", lambda c, p, i: f"={mix3(c, 'Cards_Act')}", unit="cards", total="last")
R.line("spend_dom", "Card spending in FCFA", lambda c, p, i: f"={mix3(c, 'Spend_Dom')}")
R.line("spend_for", "Card spending in foreign currencies", lambda c, p, i: f"=({mix3(c, 'Spend_For')})*Foreign_Spend_Factor")
R.line("balances", "Client balances (average)", lambda c, p, i: f"={mix3(c, 'Balance')}", total="last")
R.line("payroll", "Salaries paid through Kelen", lambda c, p, i: f"={c}{R.k['employees']}*Avg_Salary")
R.line("supplier", "Transfers out (salaries not counted)", lambda c, p, i: f"={mix3(c, 'Supplier')}", unit="transfers")
R.line("mm_n", "Transfers to wallets (salaries and others)", lambda c, p, i: f"={c}{R.k['employees']}*Wallet_Share+{c}{R.k['supplier']}*Sup_Wallet_Share", unit="transfers")
R.line("mm_vol", "Amount sent to wallets (salaries and others)", lambda c, p, i: f"={c}{R.k['payroll']}*Wallet_Share+{c}{R.k['supplier']}*Sup_Wallet_Share*Sup_Avg_Amount")
R.line("overage", "Bank transfers above the plan allowance", lambda c, p, i: f"=({mix3(c, 'Overage')})*(1-Sup_Wallet_Share)", unit="transfers")
R.line("users_extra", "Extra users beyond the plans", lambda c, p, i: f"={c}{R.k['act_p']}*MAX(0,Users_Petite-Users_Incl_Petite)+{c}{R.k['act_m']}*MAX(0,Users_Moyenne-Users_Incl_Moyenne)+{c}{R.k['act_g']}*MAX(0,Users_Grande-Users_Incl_Grande)", unit="users", total="last")
R.line("cards_extra", "Extra physical cards beyond the plans (in use)", lambda c, p, i: f"={c}{R.k['act_p']}*MAX(0,Cards_New_Petite-Cards_Phys_Incl_Petite)+{c}{R.k['act_m']}*MAX(0,Cards_New_Moyenne-Cards_Phys_Incl_Moyenne)+{c}{R.k['act_g']}*MAX(0,Cards_New_Grande-Cards_Phys_Incl_Grande)", unit="cards", total="last")
R.line("payroll_over", "Mobile money above the plans' free amount", lambda c, p, i: f"={c}{R.k['act_p']}*(MM_Low_Share*MAX(0,0.5*(Emp_Petite*Avg_Salary*Wallet_Share+Supplier_Petite*Sup_Wallet_Share*Sup_Avg_Amount)-MM_Free_Petite)+MM_Mid_Share*MAX(0,(Emp_Petite*Avg_Salary*Wallet_Share+Supplier_Petite*Sup_Wallet_Share*Sup_Avg_Amount)-MM_Free_Petite)+(1-MM_Low_Share-MM_Mid_Share)*MAX(0,2.25*(Emp_Petite*Avg_Salary*Wallet_Share+Supplier_Petite*Sup_Wallet_Share*Sup_Avg_Amount)-MM_Free_Petite))+{c}{R.k['act_m']}*(MM_Low_Share*MAX(0,0.5*(Emp_Moyenne*Avg_Salary*Wallet_Share+Supplier_Moyenne*Sup_Wallet_Share*Sup_Avg_Amount)-MM_Free_Moyenne)+MM_Mid_Share*MAX(0,(Emp_Moyenne*Avg_Salary*Wallet_Share+Supplier_Moyenne*Sup_Wallet_Share*Sup_Avg_Amount)-MM_Free_Moyenne)+(1-MM_Low_Share-MM_Mid_Share)*MAX(0,2.25*(Emp_Moyenne*Avg_Salary*Wallet_Share+Supplier_Moyenne*Sup_Wallet_Share*Sup_Avg_Amount)-MM_Free_Moyenne))+{c}{R.k['act_g']}*(MM_Low_Share*MAX(0,0.5*(Emp_Grande*Avg_Salary*Wallet_Share+Supplier_Grande*Sup_Wallet_Share*Sup_Avg_Amount)-MM_Free_Grande)+MM_Mid_Share*MAX(0,(Emp_Grande*Avg_Salary*Wallet_Share+Supplier_Grande*Sup_Wallet_Share*Sup_Avg_Amount)-MM_Free_Grande)+(1-MM_Low_Share-MM_Mid_Share)*MAX(0,2.25*(Emp_Grande*Avg_Salary*Wallet_Share+Supplier_Grande*Sup_Wallet_Share*Sup_Avg_Amount)-MM_Free_Grande))")
R.line("payslips", "Payslips in the payroll module", lambda c, p, i: f"=IF({c}$3>=Payroll_Mod_Start,MIN(1,({c}$3-Payroll_Mod_Start+1)/Payroll_Mod_Ramp)*Payroll_Mod_Uptake,0)*{c}{R.k['employees']}", unit="payslips")
R.line("intl_vol", "International payments sent", lambda c, p, i: f"=IF({c}$3>=Intl_Start,MIN(1,({c}$3-Intl_Start+1)/Intl_Ramp)*Intl_Uptake,0)*({mix3(c, 'Intl_Vol')})")
R.line("pl_adopt", "Payment links: share of clients using them", lambda c, p, i: f"=IF({c}$3>=PayLinks_Start,MIN(1,({c}$3-PayLinks_Start+1)/PL_Ramp)*PL_Adoption,0)", unit="%", fmt=PCT, total=None)
R.line("pl_coll", "Payment links: amounts collected", lambda c, p, i: f"=({mix3(c, 'PL_Coll')})*{c}{R.k['pl_adopt']}")
R.sec("Revenue (excluding credit)")
R.line("price_f", "Price factor (yearly increase × yearly-billing discount)", lambda c, p, i: f"=(1+Price_Increase)^({c}$5-1)*(1-Annual_Share*Annual_Free/12)", unit="x", fmt="0.000", total=None)
for pl, key in (("Petite", "p"), ("Moyenne", "m"), ("Grande", "g")):
    R.line(f"rev_sub_{key}", f"Subscriptions, {DISP[pl]}", lambda c, p, i, key=key, pl=pl: f"={c}{R.k['pay_' + key]}*Price_{pl}*{c}{R.k['price_f']}")
R.line("rev_sub", "Subscriptions", lambda c, p, i: f"={c}{R.k['rev_sub_p']}+{c}{R.k['rev_sub_m']}+{c}{R.k['rev_sub_g']}", bold=True)
R.line("rev_fx", "Fees on foreign-currency card spending", lambda c, p, i: f"={c}{R.k['spend_for']}*(FX_Fee+FX_Fixed_Fee/FX_Avg_Txn)")
R.line("rev_ic", "Interchange share on FCFA card spending (not in the plan)", lambda c, p, i: f"={c}{R.k['spend_dom']}*Interchange_Share")
R.line("rev_dep", "Share of bank income on client balances (not in the plan)", lambda c, p, i: f"={c}{R.k['balances']}*Deposit_Share/12")
R.line("rev_cards", "Physical card fees (one-off, cards beyond the plan)", lambda c, p, i: f"={c}{R.k['cards_paid']}*Card_Fee")
R.line("rev_over", "Transfers above the plan allowance", lambda c, p, i: f"={c}{R.k['overage']}*Overage_Fee")
R.line("rev_pl", "Payment link fees", lambda c, p, i: f"={c}{R.k['pl_coll']}*PL_Momo_Share*PL_Fee")
R.line("rev_users", "Extra users", lambda c, p, i: f"={c}{R.k['users_extra']}*Extra_User_Fee")
R.line("rev_cardx", "Extra physical cards (monthly)", lambda c, p, i: f"={c}{R.k['cards_extra']}*Extra_Card_Fee")
R.line("rev_payover", "Mobile money above the plans' free amount", lambda c, p, i: f"={c}{R.k['payroll_over']}*MM_Fee")
R.line("rev_payslip", "Payroll module (payslips and declarations)", lambda c, p, i: f"={c}{R.k['payslips']}*Payslip_Fee")
R.line("rev_intl", "International payments", lambda c, p, i: f"={c}{R.k['intl_vol']}*(Intl_Fee+Intl_Fixed_Fee/Intl_Avg_Payment)")
R.line("rev_fxic", "Interchange on card spending abroad (not in the plan)", lambda c, p, i: f"={c}{R.k['spend_for']}*FX_Interchange")
R.line("rev_total", "Revenue excluding credit", lambda c, p, i: f"={c}{R.k['rev_sub']}+SUM({c}{R.k['rev_fx']}:{c}{R.k['rev_fxic']})", bold=True)

# =====================================================================================
# CREDIT
# =====================================================================================
K = TS("Credit", "Loan book by product, interest, cost of funds, losses and the share Kelen keeps. A partner SFD lends until Kelen's own SFD (Senegal) takes over; Côte d'Ivoire loans stay with a partner.")
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
K.line("sn_part", "Senegal share of clients (own SFD lends there only)", lambda c, p, i: f"=IFERROR({R.ref('act_sn', c)}/({R.ref('act_sn', c)}+{R.ref('act_ci', c)}),1)", unit="%", fmt=PCT, total=None)
K.line("share", "Share of the margin kept by Kelen", lambda c, p, i: f"=IF({c}$3>=Own_Funding_Month,{c}{K.k['sn_part']}+(1-{c}{K.k['sn_part']})*Partner_Share,Partner_Share)", unit="%", fmt=PCT, total=None)
K.line("net", "Net credit income to Kelen", lambda c, p, i: f"={c}{K.k['margin']}*{c}{K.k['share']}", bold=True)
K.sec("Cash tied up by credit")
K.line("locked", "First-loss reserve (partner loans) and equity in the own SFD's loans", lambda c, p, i: f"=IF({c}$3>=Own_Funding_Month,{c}{K.k['book']}*({c}{K.k['sn_part']}*Capital_Ratio+(1-{c}{K.k['sn_part']})*First_Loss),{c}{K.k['book']}*First_Loss)", total="last")

fill_volume_team()

# =====================================================================================
# COSTS
# =====================================================================================
C = TS("Costs", "Every cost line by month: variable costs that grow with clients, then fixed costs by category and the contingency.")
rr = lambda key, c: R.ref(key, c)
C.sec("Variable costs (cost to serve)")
C.line("v_bank", "Partner bank fee per business account", lambda c, p, i: f"={rr('act_total', c)}*Bank_Fee")
C.line("v_onboard", "Onboarding check tools (company screening, ID checks)",
       lambda c, p, i: f"={M.ref('new_total', c)}*(KYB_Cost+KYC_Cost*KYC_Persons)+MAX(0,{rr('emp_acc', c)}-{'0' if i == 0 else rr('emp_acc', p)})*KYC_Cost")
C.line("v_cardproc", "Card processing (per active card)", lambda c, p, i: f"={rr('cards_active', c)}*Card_Proc_Fee")
C.line("v_cardprod", "Physical cards printed and delivered", lambda c, p, i: f"={rr('cards_issued', c)}*Card_Prod_Cost")
C.line("v_scheme", "Visa / Mastercard cross-border fees and bank FX margin", lambda c, p, i: f"={rr('spend_for', c)}*(Scheme_Rate+Scheme_Fixed/FX_Avg_Txn)")
C.line("v_fraud", "Fraud and chargebacks", lambda c, p, i: f"=({rr('spend_dom', c)}+{rr('spend_for', c)})*Fraud_Rate")
C.line("v_wallet", "Transfers to wallets (salaries and others)", lambda c, p, i: f"={rr('employees', c)}*Wallet_Share*(IF(MM_Cost_Cap>0,MIN(MM_Cost_Pct*Avg_Salary,MM_Cost_Cap),MM_Cost_Pct*Avg_Salary)+MM_Cost_Flat)+{rr('supplier', c)}*Sup_Wallet_Share*(IF(MM_Cost_Cap>0,MIN(MM_Cost_Pct*Sup_Avg_Amount,MM_Cost_Cap),MM_Cost_Pct*Sup_Avg_Amount)+MM_Cost_Flat)")
C.line("v_bankpay", "Salaries paid to bank accounts", lambda c, p, i: f"={rr('employees', c)}*(1-Wallet_Share)*Bank_Payout_Cost")
C.line("v_supplier", "Transfers to bank accounts (suppliers and others)", lambda c, p, i: f"={rr('supplier', c)}*(1-Sup_Wallet_Share)*Supplier_Payout_Cost")
C.line("v_pl", "Payment link collection costs", lambda c, p, i: f"={rr('pl_coll', c)}*PL_Momo_Share*PL_Cost")
C.line("v_intl", "International payments (FX spread and correspondent fees)", lambda c, p, i: f"={rr('intl_vol', c)}*Intl_Cost")
C.line("v_payslip", "Payroll module (payslip delivery)", lambda c, p, i: f"={rr('payslips', c)}*Payslip_Cost")
C.line("v_notif", "SMS, WhatsApp and support tools", lambda c, p, i: f"={rr('act_total', c)}*Notif_Cost+{rr('emp_acc', c)}*Emp_Notif")
C.line("v_empacc", "Employee account processing", lambda c, p, i: f"={rr('emp_acc', c)}*EmpAcc_Cost")
C.line("v_total", "Total variable costs", lambda c, p, i: f"=SUM({c}{C.k['v_bank']}:{c}{C.k['v_empacc']})", bold=True)
C.sec("Staff")
for d in DEPTS:
    C.line(f"s_{d}", d, lambda c, p, i, d=d: f"={S.ref('dep_' + d, c)}", color=GREEN)
C.line("s_total", "Total staff", lambda c, p, i: f"=SUM({c}{C.k['s_' + DEPTS[0]]}:{c}{C.k['s_' + DEPTS[-1]]})", bold=True)
C.sec("Office and equipment")
C.line("o_regus_sn", "Dakar office (Regus, all included)", lambda c, p, i: f"=IF({c}$3>=Office_Start,{S.ref('hc_sn', c)}*Regus_EUR*FX_EUR,0)")
C.line("o_regus_ci", "Abidjan office (Regus, all included)", lambda c, p, i: f"=IF({c}$3>=CI_Office_Start,{S.ref('hc_ci', c)}*Regus_EUR*FX_EUR,0)")
C.line("o_phone", "Phones and data plans", lambda c, p, i: f"={S.ref('hc_total', c)}*Phone_Cost")
C.line("o_laptops", "Laptops for new hires (MacBooks for the CTO and developers)", lambda c, p, i: f"=({S.ref('hires', c)}-{S.ref('hires_eng', c)})*Laptop_EUR*FX_EUR+{S.ref('hires_eng', c)}*Laptop_Dev_USD*FX_USD")
C.line("o_total", "Total office and equipment", lambda c, p, i: f"=SUM({c}{C.k['o_regus_sn']}:{c}{C.k['o_laptops']})", bold=True)
C.sec("Technology")
C.line("t_maak", "Maak platform: lease, then upgrades and maintenance", lambda c, p, i: f"=IF({c}$3<=Maak_Lease_Months,IF(Maak_Option=1,Maak_Lease_EUR*FX_EUR/12,0),Maak_Maint_USD*FX_USD/12)")
C.line("t_cloud", "Cloud hosting", lambda c, p, i: f"=IF({c}$3>=Cloud_Start,{yr('Cloud_USD', c)}*FX_USD,0)")
C.line("t_monitor", "Transaction monitoring and sanctions screening", lambda c, p, i: f"={yr('Monitoring_USD', c)}*FX_USD/12")
C.line("t_kycmin", "Identity-check vendor minimum (above usage)", lambda c, p, i: f"=IF({c}$3>=Launch_SN-1,MAX(0,KYC_Min_USD*FX_USD-{c}{C.k['v_onboard']}),0)")
C.line("t_workspace", "Gmail and ClickUp (every employee)", lambda c, p, i: f"={S.ref('hc_total', c)}*(Gmail_USD+ClickUp_USD)*FX_USD")
C.line("t_claude", "Claude Enterprise seats (CTO, developers, 2 shared)", lambda c, p, i: f"=({S.ref('hc_eng', c)}+Claude_Shared)*Claude_USD*FX_USD")
C.line("t_web", "Website tool and domain", lambda c, p, i: f"=(Website_USD+Domain_USD/12)*FX_USD")
C.line("t_freelance", "Freelance QA testing and DevOps on-call", lambda c, p, i: f"={yr('Freelance', c)}/12")
C.line("t_audit", "Tech audit", lambda c, p, i: f"=IF(AND({c}$3>=Audit_Month,MOD({c}$3-Audit_Month,12)=0),Tech_Audit_USD*FX_USD,0)")
C.line("t_proc_setup", "Card processor set-up fee", lambda c, p, i: f"=IF({c}$3=Proc_Setup_Month,Proc_Setup_USD*FX_USD,0)")
C.line("t_proc_min", "Card processor minimum (top-up above per-card fees)", lambda c, p, i: f"=IF({c}$3>=Proc_Min_Start,MAX(0,{yr('Proc_Min_USD', c)}*FX_USD-{c}{C.k['v_cardproc']}),0)")
C.line("t_total", "Total technology", lambda c, p, i: f"=SUM({c}{C.k['t_maak']}:{c}{C.k['t_proc_min']})", bold=True)
C.sec("Bank and SFD partners")
C.line("p_setup_sn", "Partner bank set-up, Senegal", lambda c, p, i: f"=IF({c}$3=Bank_Setup_Month,Bank_Setup_SN,0)")
C.line("p_min_sn", "Partner bank platform minimum, Senegal", lambda c, p, i: f"=IF({c}$3>=Launch_SN,{yr('Bank_Min_SN', c)},0)")
C.line("p_setup_ci", "Partner bank set-up, Côte d'Ivoire", lambda c, p, i: f"=IF({c}$3=CI_Bank_Setup_Month,Bank_Setup_CI,0)")
C.line("p_min_ci", "Partner bank platform minimum, Côte d'Ivoire", lambda c, p, i: f"=IF({c}$3>=Launch_CI,{yr('Bank_Min_CI', c)},0)")
C.line("p_sfd", "Partner SFD integration and fees", lambda c, p, i: f"=IF({c}$3=SFD_Setup_Month,SFD_Setup,0)+{yr('SFD_Annual', c)}/12")
C.line("p_total", "Total bank and SFD partners", lambda c, p, i: f"=SUM({c}{C.k['p_setup_sn']}:{c}{C.k['p_sfd']})", bold=True)
C.sec("Legal, regulatory and audit")
C.line("l_company", "Company set-up (Senegal, Côte d'Ivoire)", lambda c, p, i: f"=IF({c}$3=1,Company_Setup_SN,0)+IF({c}$3=CI_Company_Month,Company_Setup_CI,0)")
C.line("l_sfd", "SFD acquisition: due diligence, counsel, approval file", lambda c, p, i: f"={yr('SFD_Project', c)}/12")
C.line("l_sfd_run", "Own SFD running costs", lambda c, p, i: f"=IF({c}$3>=SFD_Acq_Month,{yr('SFD_Running', c)}/12,0)")
C.line("l_counsel", "Ongoing legal counsel", lambda c, p, i: f"={yr('Legal_Counsel', c)}")
C.line("l_auditor", "Statutory auditor", lambda c, p, i: f"={yr('Auditor', c)}/12")
C.line("l_accountant", "External accountant and tax adviser", lambda c, p, i: f"={yr('Accountant_Ext', c)}")
C.line("l_aml", "Independent AML audit", lambda c, p, i: f"={yr('AML_Audit', c)}/12")
C.line("l_data", "Data-protection filings", lambda c, p, i: f"={yr('Data_Protection', c)}/12")
C.line("l_bureau", "Credit bureau membership and reports", lambda c, p, i: f"={yr('Credit_Bureau', c)}/12")
C.line("l_insurance", "Insurance", lambda c, p, i: f"={yr('Insurance_USD', c)}*FX_USD/12")
C.line("l_total", "Total legal, regulatory and audit", lambda c, p, i: f"=SUM({c}{C.k['l_company']}:{c}{C.k['l_insurance']})", bold=True)
C.sec("Sales and marketing (non-staff)")
for key, lab in (("c_digital", "Digital ads"), ("c_brand", "Brand, launch events, PR"), ("c_events", "Events, sponsorships, sales materials"),
                 ("c_referral", "Referral fees to partners"), ("c_transport", "Field sales transport")):
    C.line("m_" + key, lab, lambda c, p, i, key=key: f"={M.ref(key, c)}", color=GREEN)
C.line("m_total", "Total sales and marketing (non-staff)", lambda c, p, i: f"=SUM({c}{C.k['m_c_digital']}:{c}{C.k['m_c_transport']})", bold=True)
C.sec("Other")
def _vd_new(key, c, p, i):
    cur = S.ref('vd_' + key, c)
    return cur if i == 0 else f"MAX(0,{cur}-{S.ref('vd_' + key, p)})"


C.line("x_recruit", "Recruitment agency fees (senior hires)", lambda c, p, i: f"=Agency_Fee_EUR*FX_EUR*(SUMPRODUCT(--({HR('G')}={c}$3),--({HR('J')}=\"Y\"),{HR('F')})"
       f"+Agency_Dev*{_vd_new('devs', c, p, i)}+Agency_Credit*{_vd_new('credit', c, p, i)}+Agency_Support*{_vd_new('support', c, p, i)}"
       f"+Agency_Rep*({_vd_new('reps_sn', c, p, i)}+{_vd_new('reps_ci', c, p, i)}))")
C.line("x_travel", "Travel", lambda c, p, i: f"={yr('Travel', c)}/12")
C.line("x_misc", "Company bank fees and miscellaneous", lambda c, p, i: f"={yr('Misc', c)}")
C.line("x_total", "Total other", lambda c, p, i: f"=SUM({c}{C.k['x_recruit']}:{c}{C.k['x_misc']})", bold=True)
C.sec("Fixed costs summary")
C.line("f_before", "Fixed costs before contingency (staff, office, tech, partners, legal, marketing, other)",
       lambda c, p, i: "=" + "+".join(f"{c}{C.k[k]}" for k in ("s_total", "o_total", "t_total", "p_total", "l_total", "m_total", "x_total")))
C.line("f_cont", "Contingency (5% buffer for unplanned costs)", lambda c, p, i: f"={c}{C.k['f_before']}*Contingency_Pct")
C.line("f_total", "Total fixed costs", lambda c, p, i: f"={c}{C.k['f_before']}+{c}{C.k['f_cont']}", bold=True)

# =====================================================================================
# P&L MONTHLY
# =====================================================================================
P = TS("P&L monthly", "Profit and loss by month. Revenue excludes VAT and taxes on financial services.")
P.sec("Revenue")
for key, lab in (("rev_sub", "Subscriptions"), ("rev_fx", "Fees on foreign-currency card spending"), ("rev_ic", "Interchange share (not in the plan)"),
                 ("rev_dep", "Share of bank income on balances (not in the plan)"), ("rev_cards", "Physical card fees"), ("rev_over", "Bank transfers above the plan allowance"),
                 ("rev_pl", "Payment link fees"), ("rev_users", "Extra users"), ("rev_cardx", "Extra physical cards (monthly)"),
                 ("rev_payover", "Mobile money above the free amount"), ("rev_payslip", "Payroll module"), ("rev_intl", "International payments"),
                 ("rev_fxic", "Interchange abroad (not in the plan)")):
    P.line(key, lab, lambda c, p, i, key=key: f"={R.ref(key, c)}", color=GREEN)
P.line("rev_credit", "Net credit income", lambda c, p, i: f"={K.ref('net', c)}", color=GREEN)
P.line("revenue", "Total revenue", lambda c, p, i: f"=SUM({c}{P.k['rev_sub']}:{c}{P.k['rev_credit']})", bold=True, fill=TOT_FILL)
P.sec("Cost of revenue (variable costs)")
P.line("d_bank", "Bank accounts and onboarding", lambda c, p, i: f"={C.ref('v_bank', c)}+{C.ref('v_onboard', c)}")
P.line("d_cards", "Cards: processing, production, scheme fees, fraud", lambda c, p, i: f"={C.ref('v_cardproc', c)}+{C.ref('v_cardprod', c)}+{C.ref('v_scheme', c)}+{C.ref('v_fraud', c)}")
P.line("d_pay", "Payouts, collections and international payments", lambda c, p, i: f"={C.ref('v_wallet', c)}+{C.ref('v_bankpay', c)}+{C.ref('v_supplier', c)}+{C.ref('v_pl', c)}+{C.ref('v_intl', c)}")
P.line("d_msg", "Messaging, payslips and employee accounts", lambda c, p, i: f"={C.ref('v_notif', c)}+{C.ref('v_empacc', c)}+{C.ref('v_payslip', c)}")
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
P.line("cum_ebitda", "Cumulative EBITDA (for tax losses carried forward)", lambda c, p, i: f"={c}{P.k['ebitda']}" if i == 0 else f"={p}{P.r}+{c}{P.k['ebitda']}", total="last")
P.line("tax", "Corporate income tax", lambda c, p, i: f"=Tax_Rate*MAX(0,{c}{P.k['cum_ebitda']})" if i == 0 else f"=Tax_Rate*MAX(0,{c}{P.k['cum_ebitda']})-Tax_Rate*MAX(0,{p}{P.k['cum_ebitda']})")
P.line("ni", "Net income", lambda c, p, i: f"={c}{P.k['ebitda']}-{c}{P.k['tax']}", bold=True, fill=TOT_FILL)
P.line("cum_ni", "Cumulative net income", lambda c, p, i: f"={c}{P.k['ni']}" if i == 0 else f"={p}{P.r}+{c}{P.k['ni']}", total="last")
P.sec("Helpers")
P.line("be_flag", "Month number if EBITDA is positive (999 otherwise)", lambda c, p, i: f"=IF({c}{P.k['ebitda']}>0,{c}$3,999)", unit="month #", fmt="0", total=None)

# =====================================================================================
# CASH FLOW
# =====================================================================================
Q = TS("Cash flow", "Monthly cash: net income, cash set aside (card collateral, credit), the SFD acquisition, funding rounds and the closing balance.")
Q.sec("Operations")
Q.line("ni", "Net income", lambda c, p, i: f"={P.ref('ni', c)}", color=GREEN)
Q.sec("Cash set aside (restricted)")
Q.line("collat", "Card programme collateral", lambda c, p, i: f"=-IF({c}$3=Collateral_Month,Card_Collateral,0)")
Q.line("sfd", "Acquisition of a microfinance company (SFD)", lambda c, p, i: f"=-IF({c}$3=SFD_Acq_Month,SFD_Acquisition,0)")
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
       lambda c, p, i: f"=-SUM({FC}{Q.k['collat']}:{c}{Q.k['collat']})+{K.ref('locked', c)}",
       total="last")
Q.line("burn", "Monthly burn (average of the last 3 months, if negative)", lambda c, p, i: f"=MAX(0,-AVERAGE({c}{Q.k['before']}))" if i < 2 else f"=MAX(0,-AVERAGE({COLS[i - 2]}{Q.k['before']}:{c}{Q.k['before']}))", total=None)
Q.line("runway", "Runway at that burn (months)", lambda c, p, i: f"=IF({c}{Q.k['burn']}=0,\"cash positive\",{c}{Q.k['close']}/{c}{Q.k['burn']})", unit="months", fmt=NUM1, total=None)

# =====================================================================================
# EURO TWINS of the monthly sheets: every FCFA line divided by the euro parity
# =====================================================================================
def euro_twin(ts):
    src = ts.ws
    ws = wb.create_sheet(f"{ts.name} (€)")
    title(ws, f"{ts.name} (€)", f"Every amount of the '{ts.name}' sheet in euros (FCFA ÷ FCFA per euro on Assumptions). Edit the FCFA sheets and Assumptions, not this one.")
    for rr_, lab in ((3, "Month #"), (4, "Month"), (5, "Year")):
        ws.cell(rr_, 1, lab).font = F(bold=True)
    ws["D3"] = "Total / end"
    ws["D3"].font = F(bold=True)
    for c in COLS:
        for rr_, fm in ((3, "0"), (4, DATEF), (5, '"Y"0')):
            cell = ws[f"{c}{rr_}"]
            cell.value = f"='{ts.name}'!{c}{rr_}"
            cell.number_format = fm
            cell.font = F(bold=True)
            cell.fill = SEC_FILL
            cell.alignment = Alignment(horizontal="center")
        ws.column_dimensions[c].width = 11
    ws.column_dimensions["A"].width = 50
    ws.column_dimensions["B"].width = 8
    ws.column_dimensions["C"].width = 3
    ws.column_dimensions["D"].width = 14
    ws.freeze_panes = "E6"
    out = 7
    for r in range(7, ts.r):
        lab = src.cell(r, 1).value
        unit = src.cell(r, 2).value
        if r in ts.secs:
            out += 1
            ws.cell(out, 1, lab).font = F(bold=True)
            for col in range(1, C0 + NM):
                ws.cell(out, col).fill = SEC_FILL
            out += 1
            continue
        if unit != "FCFA":
            continue
        bold = bool(src.cell(r, 1).font and src.cell(r, 1).font.b)
        ws.cell(out, 1, f"='{ts.name}'!A{r}" if str(lab).startswith("=") else lab).font = F(bold=bold)
        ws.cell(out, 2, "€").font = F(color=GREY)
        if src[f"D{r}"].value is not None:
            ws[f"D{out}"] = f"='{ts.name}'!D{r}/FX_EUR"
            style(ws[f"D{out}"], fmt=NUM, bold=True, fill=TOT_FILL)
        for c in COLS:
            ws[f"{c}{out}"] = f"='{ts.name}'!{c}{r}/FX_EUR"
            style(ws[f"{c}{out}"], fmt=NUM, bold=bold)
        out += 1
    return ws.title


TWINS = {t.name: euro_twin(t) for t in (S, M, R, K, C, P, Q)}

# =====================================================================================
# P&L ANNUAL (with cash and euros)
# =====================================================================================
Y = wb.create_sheet("P&L annual")
title(Y, "P&L annual", "Years 1–5, summed from the monthly sheets. FCFA in columns D–I, euros in columns K–P.")
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


def y_sum(key, label, sheet, srckey, fmt=NUM, bold=False, total=True, unit="FCFA"):
    r = yrow[0]
    YK[key] = r
    Y.cell(r, 1, label).font = F(bold=bold)
    Y.cell(r, 2, unit).font = F(color=GREY)
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


def y_end(key, label, sheet, srckey, fmt=NUM, bold=False, unit="FCFA"):
    r = yrow[0]
    YK[key] = r
    Y.cell(r, 1, label).font = F(bold=bold)
    Y.cell(r, 2, unit).font = F(color=GREY)
    src = sheet.k[srckey]
    for j in range(5):
        col = CL(4 + j)
        Y[f"{col}{r}"] = f"=INDEX('{sheet.name}'!${FC}${src}:${LC}${src},1,{col}$4*12)"
        style(Y[f"{col}{r}"], fmt=fmt, bold=bold, color=GREEN)
    yrow[0] += 1
    return r


def y_f(key, label, fn, fmt=NUM, bold=False, total=None, fill=None, unit=None):
    r = yrow[0]
    YK[key] = r
    Y.cell(r, 1, label).font = F(bold=bold)
    Y.cell(r, 2, unit if unit is not None else ("%" if fmt == PCT else "FCFA")).font = F(color=GREY)
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


y_sec("Revenue")
for key in ("rev_sub", "rev_fx", "rev_ic", "rev_dep", "rev_cards", "rev_over", "rev_pl", "rev_users", "rev_cardx", "rev_payover", "rev_payslip", "rev_intl", "rev_fxic", "rev_credit"):
    lab = P.ws.cell(P.k[key], 1).value
    y_sum(key, lab, P, key)
y_sum("revenue", "Total revenue", P, "revenue", bold=True)
y_f("growth", "Revenue growth", lambda col: "=0" if col == "D" else f"=IFERROR({col}{YK['revenue']}/{CL(ord(col) - 65)}{YK['revenue']}-1,0)", fmt=PCT, unit="%")
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
y_sum("tax", "Corporate income tax", P, "tax")
y_f("ni", "Net income", lambda col: f"={col}{YK['ebitda']}-{col}{YK['tax']}", bold=True, total="sum", fill=TOT_FILL)
y_sec("Cash and funding")
y_sum("cf_before", "Cash flow before funding", Q, "before")
y_sum("equity", "Equity raised", Q, "equity")
y_end("cash", "Closing cash (end of year)", Q, "close", bold=True)
y_sec("Operating figures (end of year)")
y_end("clients", "Active clients", R, "act_total", bold=True, unit="clients")
y_end("clients_sn", "of which Senegal (approx.)", R, "act_sn", unit="clients")
y_end("clients_ci", "of which Côte d'Ivoire (approx.)", R, "act_ci", unit="clients")
y_sum("new_clients", "New clients in the year", M, "new_total", unit="clients")
y_end("headcount", "Headcount", S, "hc_total", unit="people")
y_end("book", "Loan book", K, "book")
y_end("emp_acc", "Employee salary accounts (B2C)", R, "emp_acc", unit="accounts")
# euro twin columns K..P for every FCFA row
Y.column_dimensions["J"].width = 3
for j in range(6):
    col = CL(11 + j)
    Y.column_dimensions[col].width = 16
    Y[f"{col}4"] = f"Y{j + 1} (€)" if j < 5 else "5 years (€)"
    style(Y[f"{col}4"], bold=True, fill=SEC_FILL, align="center")
    if j < 5:
        Y[f"{col}5"] = f"={CL(4 + j)}5"
        style(Y[f"{col}5"], fmt="0", bold=True, fill=SEC_FILL, align="center")
for r in range(6, yrow[0]):
    if Y.cell(r, 2).value == "FCFA":
        bold = bool(Y.cell(r, 1).font and Y.cell(r, 1).font.b)
        for j in range(6):
            src = CL(4 + j)
            if Y[f"{src}{r}"].value is not None:
                Y[f"{CL(11 + j)}{r}"] = f"={src}{r}/FX_EUR"
                style(Y[f"{CL(11 + j)}{r}"], fmt=EURN, bold=bold)

# =====================================================================================
# KPIs and unit economics
# =====================================================================================
U = wb.create_sheet("Unit economics")
title(U, "Unit economics and KPIs", "Per-client economics and efficiency ratios by year. Euros in columns J–N.")
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
u("mm_rev", "Mobile money fees as % of revenue", lambda col: f"=IFERROR('P&L annual'!{col}{YK['rev_payover']}/'P&L annual'!{col}{YK['revenue']},0)", unit="%", fmt=PCT)
U.column_dimensions["I"].width = 3
for j in range(5):
    col = CL(10 + j)
    U.column_dimensions[col].width = 16
    U[f"{col}4"] = f"Y{j + 1} (€)"
    style(U[f"{col}4"], bold=True, fill=SEC_FILL, align="center")
for r in range(6, urow[0]):
    unit = U.cell(r, 2).value or ""
    if unit.startswith("FCFA"):
        for j in range(5):
            U[f"{CL(10 + j)}{r}"] = f"={CL(4 + j)}{r}/FX_EUR"
            style(U[f"{CL(10 + j)}{r}"], fmt=EURN)

# =====================================================================================
# MARKET
# =====================================================================================
MK = wb.create_sheet("Market")
title(MK, "Market", "How many companies Kelen can serve, and the share of them the plan reaches. Blue cells are inputs with their sources.")
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
    heads = ["Unit", "", "Value", "€ equivalent"] if not years else ["Unit", ""] + [f"Y{j + 1}" for j in range(5)]
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
    if unit.startswith("FCFA"):
        style(MK.cell(r, 5, f"=D{r}/FX_EUR"), fmt=EURN, color=GREY)
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
mk_in("sn_target", "Share of formal employers in Kelen's target (2–500 staff, urban, digital)", 0.50, "%", PCT, "Assumption. Core target: Dakar, Thiès, Saint-Louis.")
mk_in("sn_ready", "Digital-ready SMEs (market analysis estimate, midpoint)", 24000, "companies", NUM, "Market analysis (Oct 2026): 20,000–28,000 formal employers in Dakar and other cities that already bank and pay by phone; large firms excluded. To validate in interviews.")
mk_head("Côte d'Ivoire: inputs")
mk_in("ci_emp", "Formal employers (CNPS declared companies)", 49000, "companies", NUM, "CNPS: about 49,000 declared companies (gouv.ci, Apr 2025; not fully verified). Was 60,000 before the market analysis (Oct 2026). https://www.gouv.ci/actualite/protection-sociale-environ-12-million-de-travailleurs-du-secteur-prive-et-pres-dun-million-de-travailleurs-independants-declares-a-la-cnps-2374")
mk_in("ci_growth", "Growth in formal employers", 0.05, "% / year", PCT, "Assumption.")
mk_in("ci_new", "New companies created a year (CEPICI, 2025)", 26948, "companies / year", NUM, "CEPICI 2025 review (Feb 2026): 26,948 companies created, +6%. https://fr.allafrica.com/stories/202602200240.html")
mk_in("ci_target", "Share of formal employers in Kelen's target", 0.50, "%", PCT, "Assumption. Core target: Abidjan.")
mk_head("Addressable market and plan penetration (end of year)", years=True)
start_year = 2024
mk_y("sn_market", "Senegal: formal employers", lambda col, y: f"=$D${MKK['sn_emp']}*(1+$D${MKK['sn_growth']})^(YEAR(Start_Date)+{y - 1}-{start_year})", "companies")
mk_y("sn_sam", "Senegal: target companies (serviceable market)", lambda col, y: f"={col}{MKK['sn_market']}*$D${MKK['sn_target']}", "companies", bold=True)
mk_y("sn_clients", "Senegal: Kelen active clients", lambda col, y: f"='P&L annual'!{col}{YK['clients_sn']}", "clients")
mk_y("sn_share", "Senegal: share of target companies", lambda col, y: f"=IFERROR({col}{MKK['sn_clients']}/{col}{MKK['sn_sam']},0)", "%", fmt=PCT, bold=True)
mk_y("sn_ready_share", "Senegal: share of digital-ready SMEs (market analysis)", lambda col, y: f"=IFERROR({col}{MKK['sn_clients']}/$D${MKK['sn_ready']},0)", "%", fmt=PCT)
mk_y("ci_market", "Côte d'Ivoire: formal employers", lambda col, y: f"=$D${MKK['ci_emp']}*(1+$D${MKK['ci_growth']})^(YEAR(Start_Date)+{y - 1}-{start_year})", "companies")
mk_y("ci_sam", "Côte d'Ivoire: target companies (serviceable market)", lambda col, y: f"={col}{MKK['ci_market']}*$D${MKK['ci_target']}", "companies", bold=True)
mk_y("ci_clients", "Côte d'Ivoire: Kelen active clients", lambda col, y: f"='P&L annual'!{col}{YK['clients_ci']}", "clients")
mk_y("ci_share", "Côte d'Ivoire: share of target companies", lambda col, y: f"=IFERROR({col}{MKK['ci_clients']}/{col}{MKK['ci_sam']},0)", "%", fmt=PCT, bold=True)
mk_y("emp_share", "Employee salary accounts vs declared employees in Senegal", lambda col, y: f"=IFERROR('P&L annual'!{col}{YK['emp_acc']}/$D${MKK['sn_staff']},0)", "%", fmt=PCT2)
mk_head("Revenue pool today (indicative)")
mk_in("bank_fee", "Bank business account fee (SME)", 15000, "FCFA / month", NUM, "Published tariffs: BNDE 12,500, BIS 12,000, UBA Sénégal 25,000 (SA/PME) or 10,000 (micro); SGCI PME packs 25,000–35,000. With online banking and transfers a 10-employee SARL pays about 35,000–52,500 a month (market analysis, Oct 2026).")
r = mrow[0]
MK.cell(r, 1, "Senegal: what target companies pay for business accounts today").font = F()
MK.cell(r, 2, "FCFA / year").font = F(color=GREY)
MK.cell(r, 4, f"=D{MKK['sn_sam']}*D{MKK['bank_fee']}*12")
style(MK.cell(r, 4), fmt=NUM)
style(MK.cell(r, 5, f"=D{r}/FX_EUR"), fmt=EURN)
MK.cell(r, 9, "Account fees only; transfer, card and payout fees come on top. Today SMEs also pay 1% of payroll to Wave Business or Orange Money (1.5% to non-Orange wallets), and Julaya charges 0.5–1.5%.").font = F(color=GREY)
mrow[0] += 1


EUR2 = '"€"#,##0.00;-"€"#,##0.00;"-"'
PL3 = ("Petite", "Moyenne", "Grande")

# =====================================================================================
# PLANS (the offer, as clients see it)
# =====================================================================================
PS = wb.create_sheet("Plans")
PS.sheet_view.showGridLines = False
for col, w in {"A": 44, "B": 20, "C": 20, "D": 20, "E": 70}.items():
    PS.column_dimensions[col].width = w
PS["A1"] = "Plans, add-ons and commissions"
PS["A1"].font = F(bold=True, size=14, color=TEAL)
PS["A2"] = "The offer as clients see it, for the pricing option selected on Assumptions. Every price, limit and fee links to Assumptions; feature rows are the product definition."
PS["A2"].font = F(italic=True, color=GREY)
psr = [4]


def ps_title(text, sub=""):
    psr[0] += 1
    PS.cell(psr[0], 1, text).font = F(bold=True, size=12, color=TEAL)
    psr[0] += 1
    if sub:
        PS.cell(psr[0], 1, sub).font = F(italic=True, color=GREY)
        psr[0] += 1


def ps_head(heads):
    for j, h in enumerate(heads):
        c = PS.cell(psr[0], 1 + j, h)
        c.font = F(bold=True, color=WHITE)
        c.fill = HEAD_FILL
        c.alignment = Alignment(wrap_text=True, vertical="top")
    psr[0] += 1


def ps_sub(text, ncol=5):
    PS.cell(psr[0], 1, text).font = F(bold=True)
    for col in range(1, ncol + 1):
        PS.cell(psr[0], col).fill = SEC_FILL
    psr[0] += 1


def ps_row(vals, fmt=None, eur=None, bold=False):
    r = psr[0]
    for j, v in enumerate(vals):
        if v is None:
            continue
        c = PS.cell(r, 1 + j, v)
        if isinstance(v, str) and v.startswith("="):
            style(c, fmt=fmt, bold=bold)
        else:
            c.font = F(bold=bold and j == 0, color=GREY if j == len(vals) - 1 and j >= 2 else BLACK)
            c.alignment = Alignment(wrap_text=True, vertical="top")
    psr[0] += 1
    if eur:
        r2 = psr[0]
        PS.cell(r2, 1, "   in €").font = F(italic=True, color=GREY)
        for col in eur:
            PS[f"{col}{r2}"] = f"=IF(ISNUMBER({col}{r}),{col}{r}/FX_EUR,\"\")"
            style(PS[f"{col}{r2}"], fmt=EUR2, italic=True, color=GREY)
        psr[0] += 1
    return r


three = lambda base: [f"={base}_Petite", f"={base}_Moyenne", f"={base}_Grande"]
ps_title("The three plans", "Clients choose by what they need, not by staff count. Two simple limits: a number of transfers to bank accounts (salaries never count) and an amount sent to mobile money (salaries included).")
ps_head(["What is included", "Essentiel", "Pro", "Business", "Notes"])
ps_sub("Price")
ps_row(["Monthly price"] + three("Price") + ["FCFA a month, excluding VAT. Option A / B / C on Assumptions."], NUM, eur=list("BCD"), bold=True)
ps_row(["Yearly billing (price for 12 months)", "=Price_Petite*(12-Annual_Free)", "=Price_Moyenne*(12-Annual_Free)", "=Price_Grande*(12-Annual_Free)", "=\"Pay yearly and get \"&Annual_Free&\" months free.\""], NUM, eur=list("BCD"))
ps_row(["Free trial", "=Free_Months&\" month free\"", "=Free_Months&\" month free\"", "=Free_Months&\" month free\"", "Every new client, every plan."])
ps_sub("Limits")
ps_row(["Users included"] + three("Users_Incl") + ["Essentiel: 1 main user + 1 invited free. More users: add-on below."], NUM)
ps_row(["Bank transfers a month"] + three("Transfers_Incl") + ["Payments to suppliers and others by bank transfer. Salaries and transfers to wallets never count. Above it: fee per extra transfer. Incoming transfers are free and unlimited."], NUM)
ps_row(["Mobile money free up to"] + three("MM_Free") + ["FCFA a month sent to wallets (Wave, Orange Money, Mixx…), salaries included. Above it: the mobile money fee below. Fair use: no splitting into many tiny transfers."], NUM, eur=list("BCD"))
ps_row(["Salaries to bank accounts free up to"] + three("Payroll_Free") + ["FCFA of salaries a month. Above it: fee per extra transfer for each salary."], NUM, eur=list("BCD"))
ps_row(["Physical cards included"] + three("Cards_Phys_Incl") + ["Visa cards for staff, co-branded with the partner bank. More cards: one-off fee below."], NUM)
ps_row(["Virtual cards", "2", "10", "Unlimited", "For online payments: ads, software, subscriptions."])
ps_row(["Sub-accounts", "1", "5", "Unlimited", "Separate balances by project, site or budget."])
ps_sub("Features")
for lab, a, b, c, note in (
        ("Business account with its own IBAN", "✓", "✓", "✓", "Held at the partner bank."),
        ("Salary payments to any bank or wallet", "✓", "✓", "✓", "Bulk runs, scheduled paydays, status per employee."),
        ("Import a payroll file (KayFay, Sage, Excel…)", "✓", "✓", "✓", ""),
        ("Invoices and payment links (Wave, Orange Money, card)", "✓", "✓", "✓", "Commission on mobile-money collections: see commissions."),
        ("Approvals (double signature)", "—", "✓", "✓ multi-level, custom rules", "Locked on Essentiel: tapping it shows an \"Unlock with Pro\" button."),
        ("Accounting module (accountant access, receipts, SYSCOHADA export)", "—", "✓", "✓", "Locked on Essentiel."),
        ("Spend control (limits and budgets per card or person)", "—", "Basic", "Full", ""),
        ("API and several companies under one login", "—", "—", "✓", ""),
        ("Support", "Chat", "Priority", "Dedicated adviser", ""),
        ("Payroll module (payslips and declarations)", "Paid option", "Paid option", "Paid option", "Per payslip: see add-ons."),
        ("International supplier payments", "✓", "✓", "✓", "Fee per payment: see commissions."),
):
    ps_row([lab, a, b, c, note])

ps_title("Add-ons", "Paid only when a client goes beyond its plan or chooses an option. Upgrade prompts appear at 80% and 100% of each limit.")
ps_head(["Add-on", "Price", "Unit", "", "When it applies"])
for lab, nm, unit, fm, note in (
        ("Extra user", "Extra_User_Fee", "FCFA / month", NUM, "Each user beyond the plan."),
        ("Extra physical card", "Card_Fee", "FCFA, one-off", NUM, "The first physical card is free; each other card is paid once, for printing and delivery. No monthly fee."),
        ("Bank transfer above the plan allowance", "Overage_Fee", "FCFA / transfer", NUM, "Each bank transfer beyond the monthly number, and each salary to a bank account above the free amount. Not charged on transfers to wallets. Banks charge 3,000–5,000."),
        ("Mobile money above the free amount", "MM_Fee", "% of amount", PCT2, "Only the part sent to wallets above the plan's free amount. Kelen pays the operators 1% (capped at 5,000 FCFA) until a deal is signed. Wave charges 1%."),
        ("Mobile money fee: cap per transfer", "MM_Fee_Cap", "FCFA / transfer", NUM, "The fee above never exceeds this on a single transfer (reached at about 740,000 FCFA)."),
        ("Card payment in other currencies", "FX_Fixed_Fee", "FCFA / payment", NUM, "On top of the % below, for each card payment in dollars or euros."),
        ("International payment", "Intl_Fixed_Fee", "FCFA / payment", NUM, "On top of the % below, for each payment abroad."),
        ("Payroll module", "Payslip_Fee", "FCFA / payslip", NUM, "Payslip plus the monthly IPRES, CSS and income-tax declarations. Optional, every plan."),
):
    ps_row([lab, f"={nm}", unit, None, note], fm, eur=["B"] if fm == NUM else None)

ps_title("Commissions", "Charged as a share of the amount, on top of the plan.")
ps_head(["Commission", "Rate", "Unit", "", "What it is for"])
for lab, nm, note in (
        ("Payment links and QR collections (mobile money)", "PL_Fee", "When a client's customer pays an invoice by Wave or Orange Money. Card and transfer payments are free."),
        ("Card spending in other currencies", "FX_Fee", "Ads, software and travel paid in dollars or euros, plus a fixed fee per payment (below). Card spending in FCFA is free."),
        ("International supplier payments", "Intl_Fee", "Paying suppliers abroad (China, Turkey, Dubai, France). The same rate the bank or provider charges Kelen, plus a fixed fee (below). The 0.6% tax on transfers out of the zone is added at cost."),
):
    ps_row([lab, f"={nm}", "% of amount", None, note], PCT2)

ps_title("Always free", "What clients never pay for.")
ps_head(["Item", "Note"])
for lab, note in (("Opening the account", "Online, no branch visit."), ("Salaries to bank accounts up to the plan's free amount", "Any number of employees."),
                  ("Mobile money up to the plan's free amount", "Salaries and other payments to wallets."), ("Incoming transfers", "From any bank or wallet in the WAEMU."),
                  ("Card spending in FCFA", ""), ("Virtual cards up to the plan limit", "")):
    ps_row([lab, note])

ps_title("Possible income from partners (not in the plan)", "This income goes to the partner bank, which owns the accounts and cards. Nothing obliges it to share; the plan counts zero. Items to ask for in the negotiation; what they would add is on Pricing levers.")
ps_head(["Item", "Possible rate", "Unit", "", "What it is"])
ps_row(["Interchange share on card spending in FCFA", "about 0.3%", "% of spending", None, "Part of the fee shops pay on every card payment. The BCEAO gives it to the bank that issues the card."])
ps_row(["Share of bank income on client balances", "about 1.25%", "% a year", None, "Part of what the partner bank earns on the money clients keep in their accounts."])
ps_row(["Interchange on card spending abroad", "about 0.8%", "% of spending", None, "Paid by Visa / Mastercard to the bank that issues the card, on foreign payments."])

ps_title("Credit (from month 18)", "Loans made by a partner microfinance institution, then by Kelen's own in Senegal. Rates are all-in, under the 24% cap.")
ps_head(["Product", "Rate", "Unit", "", "What it is"])
for pk, lab, note in (("Factoring", "Invoice financing", "Cash now against an invoice a client will pay in 30–90 days."),
                      ("Bridge", "Payroll bridge", "Short loan to pay salaries on time when a client pays late."),
                      ("Line", "Credit line", "Cash reserve to draw and repay, sized on the account's flows."),
                      ("Term", "Equipment loan", "Vehicles, machines, computers; 6–24 months."),
                      ("Advance", "Salary advance (employees)", "Part of earned salary before payday, repaid from the next salary.")):
    ps_row([lab, f"=Yield_{pk}", "% a year", None, note], PCT)

ps_title("Pricing options", "Switch on Assumptions (Pricing option). B is the base.")
ps_head(["Plan", "A: acquisition first", "B: balanced", "C: revenue first", "Note"])
for pl in PL3:
    ps_row([DISP[pl], f"=OFFSET(Price_{pl},0,1)", f"=OFFSET(Price_{pl},0,2)", f"=OFFSET(Price_{pl},0,3)", "FCFA a month"], NUM, eur=list("BCD"))


# =====================================================================================
# HOW IT WORKS
# =====================================================================================
HW = wb.create_sheet("How it works")
HW.sheet_view.showGridLines = False
for col, w in {"A": 34, "B": 48, "C": 48, "D": 56, "E": 44}.items():
    HW.column_dimensions[col].width = w
HW["A1"] = "How Kelen works"
HW["A1"].font = F(bold=True, size=14, color=TEAL)
HW["A2"] = "Who does what, how the money moves, and when Kelen needs its own cash. Kelen never holds client money: it sits at the partner bank, and later also at Kelen's own SFD."
HW["A2"].font = F(italic=True, color=GREY)
hwr = [4]


def hw_title(text, sub=""):
    hwr[0] += 1
    HW.cell(hwr[0], 1, text).font = F(bold=True, size=12, color=TEAL)
    hwr[0] += 1
    if sub:
        HW.cell(hwr[0], 1, sub).font = F(italic=True, color=GREY)
        hwr[0] += 1


def hw_head(heads):
    for j, h in enumerate(heads):
        c = HW.cell(hwr[0], 1 + j, h)
        c.font = F(bold=True, color=WHITE)
        c.fill = HEAD_FILL
        c.alignment = Alignment(wrap_text=True, vertical="top")
    hwr[0] += 1


def hw_row(vals):
    for j, v in enumerate(vals):
        c = HW.cell(hwr[0], 1 + j, v)
        c.font = F(bold=j == 0)
        c.alignment = Alignment(wrap_text=True, vertical="top")
    hwr[0] += 1


hw_title("The partners", "Kelen is the app, the onboarding, the support and the controls. The licences, the accounts and the cards belong to partners until Kelen owns an SFD.")
hw_head(["Partner", "What it does", "What Kelen pays it", "When"])
for row in (
        ("Partner bank", "Holds every client account (in the client's name, at the bank), signs off the identity checks, executes transfers (same bank, interbank, PI-SPI, SWIFT), issues the Visa cards under its name and keeps the client money.", "A fee per account, a fee per transfer, card programme set-up, and a cash guarantee (collateral) for the cards.", "From launch, both countries."),
        ("Wave and Orange Money (directly or through an aggregator: HUB2, PayDunya, CinetPay, InTouch)", "Deliver transfers to wallets and collect payment-link payments.", "1% per transfer to a wallet today (Wave capped at 5,000 FCFA), about 1% on collections. Aggregators: 1.5–2% public, less with volume.", "From launch."),
        ("Card processor (HPS, Paymentology, GIM-UEMOA…)", "Approves every card payment in real time against the client's balance and handles card files.", "A monthly fee per active card.", "From the card launch."),
        ("Visa / Mastercard", "The card network. Paid through the partner bank.", "Cross-border fees on payments in other currencies.", "From the card launch."),
        ("Partner SFD (microfinance institution)", "Lends under its licence and with its funding; Kelen finds, scores and services the loans.", "Kelen keeps a share of the net margin and puts up a first-loss reserve.", "Month 18 to month 24 in Senegal; all along in Côte d'Ivoire."),
        ("International payment provider (partner bank, Capi Money or others)", "Converts FCFA and pays suppliers abroad in euros, dollars or yuan.", "Its rate (about 3.5% assumed) plus the 0.6% tax, both passed on to the client.", "From month 13."),
        ("Maak (group company)", "The banking platform: accounts ledger, payments, cards and app back-end.", "A lease for 3 years, then upgrades and maintenance.", "From month 1."),
):
    hw_row(row)

hw_title("Service by service", "What each side does and how the money moves. 'Cash Kelen must put up' is Kelen's own money, not client money.")
hw_head(["Service", "Partner bank or SFD does", "Kelen does", "How the money moves", "Cash Kelen must put up"])
for row in (
        ("Business account", "Opens the account in the client's name and holds the money.", "App and web access, onboarding file, identity checks, support.", "The client's money stays in the client's account at the bank.", "None."),
        ("Bank transfers and salaries to bank accounts", "Executes the transfer from the client's account: free inside the same bank, through the interbank system or PI-SPI otherwise.", "Payment screens, bulk payroll runs, approvals, status per payment.", "Client account → recipient's bank account, directly.", "None."),
        ("Transfers to wallets (salaries and others)", "Route 1: sends from the client's account straight to Wave or Orange Money through PI-SPI, if the bank offers business transfers to wallets.", "Bulk runs and approvals. Route 2 or 3: Kelen runs the payout through Wave, Orange Money or an aggregator.", "Route 1: client account → wallet. Routes 2 and 3: client account → a prefunded business wallet or aggregator balance → employee's wallet.", "Route 1: none. Routes 2 and 3: a float covering 1–3 days of payouts, larger on paydays. Not in the plan yet: see the routes below."),
        ("Payment links (collections)", "Receives the settlement and credits the client's account.", "The link, the invoice, matching payments to invoices.", "The customer pays by Wave or Orange Money → operator or aggregator merchant account → settled to the bank (same day to 5 days; Orange D+5) → client's account.", "None if the client is credited at settlement. A float if Kelen credits instantly."),
        ("Cards (co-branded with the partner bank)", "Issues the cards under its name and Visa licence, pays Visa every day and debits the client's account.", "Card design and ordering, spending limits and controls in the app, first-line disputes.", "The client pays → the processor checks the balance and blocks the amount → next day Visa debits the bank → the bank debits the client's account.", "Collateral at the bank (60M FCFA in the plan, from month 4). If the bank runs the cards as prepaid, also a float of a few days of card spending."),
        ("International payments", "Converts and sends the payment (SWIFT), checks the foreign-exchange paperwork.", "Collects invoices and import documents, compliance checks, sends the instruction.", "Client account debited (amount + fee + 0.6% tax) → provider → supplier abroad.", "None if the provider debits on execution; a balance if it needs prefunding."),
        ("Payroll module and accounting", "Nothing.", "Software only: payslips, declarations, accountant access, exports.", "No money moves.", "None."),
        ("Credit, partner SFD (Senegal months 18–24; Côte d'Ivoire)", "Signs the loan, lends its money (or debt lines), carries the risk above the first-loss reserve.", "Scoring from account data, the loan offer in the app, repayments collected from the account.", "SFD → client's account; repayments taken from the account.", "First-loss reserve (share of the loan book)."),
        ("Credit, Kelen's own SFD (Senegal from month 24)", "—", "Lends itself and keeps the whole margin, under the 24% rate cap.", "Kelen's SFD → client's account; repayments back to the SFD.", "Equity in the loans (capital ratio) plus debt lines for the rest."),
):
    hw_row(row)

hw_title("Transfers to mobile money: the three routes", "Not every bank can send to wallets today. The route decides the cost and whether Kelen must prefund a float. The plan assumes no deal: 1% capped at 5,000 FCFA.")
hw_head(["Route", "How it works", "Cost today", "Cash Kelen must put up", "Status"])
for row in (
        ("1. Partner bank through PI-SPI", "The bank sends from the client's account straight to the wallet. From 2 November 2026 every interoperable transfer goes through PI-SPI, Wave included.", "Set freely by the bank for businesses: to negotiate (capped or flat).", "None.", "The bank needs PI-SPI business access (bulk payments). Certified in Senegal so far: 9 participants, including Ecobank, which is certified in all 8 countries. Make it a condition when choosing the bank."),
        ("2. Direct contract with Wave Business and Orange Money", "A business wallet with each operator, paid out through their API.", "Wave 1% (reportedly capped at 5,000 FCFA); Orange 1%, 1.5% to other wallets.", "The business wallets must be topped up before payouts (1–3 days of volume, more on paydays).", "Possible now. The float is client money in transit: it must sit under a licensed partner's name."),
        ("3. Aggregator (HUB2, PayDunya, CinetPay, InTouch)", "One API to every operator.", "1.5–2% public; HUB2 and InTouch on quote, lower with volume.", "A prefunded balance at the aggregator.", "Possible now; the most expensive public route."),
        ("4. Kelen's own SFD on PI-SPI (after month 24)", "SFDs can join PI-SPI (UM ACEP, an SFD, is certified for business payments).", "PI-SPI fees only.", "The SFD's own settlement account.", "Later; depends on the SFD bought."),
):
    hw_row(row)

hw_title("The card programme", "Co-branded, not fully white-label: like Djamo's cards with Ecobank, or Wave's virtual Visa with Ecobank.")
hw_head(["Question", "Answer"])
for row in (
        ("Whose name is on the card?", "The partner bank is the issuer (its Visa licence and card number range) and its name is on the card next to Kelen's brand."),
        ("Does Kelen need cash for card payments?", "Not for the payments themselves: the bank pays Visa and debits the client's account. Kelen puts up collateral (60M FCFA in the plan) so the bank is covered for disputes, fraud or a failed debit. If the bank runs the cards as prepaid, a float of a few days of spending must also be prefunded."),
        ("Who earns the interchange?", "The bank, as the issuer. Kelen only if the bank agrees to share it: not in the plan."),
        ("What does Kelen pay?", "The processor per active card, the printing of physical cards, Visa's cross-border fees on foreign payments, and any set-up fee the bank asks."),
        ("Can Kelen's own SFD issue cards later?", "Not on its own at first: Visa membership needs a bank sponsor or large collateral. The plan keeps the partner bank for cards."),
):
    hw_row(row)

hw_title("What changes when Kelen owns an SFD (Senegal, from month 24)")
hw_head(["Item", "With partners only", "With Kelen's own SFD"])
for row in (
        ("Credit", "The partner SFD lends; Kelen keeps a share of the margin and covers first losses.", "Kelen's SFD lends and keeps the whole margin; it needs capital and debt lines to fund the loans."),
        ("Client money", "At the partner bank; the bank keeps the income on balances.", "SFDs can take deposits: money held at Kelen's SFD would earn Kelen the income. The bank account stays for cards and transfers."),
        ("Transfers to wallets", "Through the partner bank, the operators or an aggregator.", "Possibly direct through PI-SPI, if the SFD connects."),
        ("Cards", "Partner bank.", "Still the partner bank."),
        ("Côte d'Ivoire", "Partner bank and partner SFD.", "No change: Kelen's SFD is licensed in Senegal only."),
        ("Rules", "The partners' licences; Kelen is their outsourced provider.", "BCEAO supervision of the SFD, the 24% rate cap, capital and reporting rules."),
):
    hw_row(row)

# =====================================================================================
# PRICING LEVERS
# =====================================================================================
EUR2 = '"€"#,##0.00;-"€"#,##0.00;"-"'
PL3 = ("Petite", "Moyenne", "Grande")
LV = wb.create_sheet("Pricing levers")
LV.sheet_view.showGridLines = False
for col, w in {"A": 46, "B": 52, "C": 16, "D": 14, "E": 16, "F": 18, "G": 18, "H": 14}.items():
    LV.column_dimensions[col].width = w
LV["A1"] = "Pricing levers"
LV["A1"].font = F(bold=True, size=14, color=TEAL)
LV["A2"] = "What each change does to year-5 revenue and EBITDA, all else equal. Type a change in the blue cells. The model's client numbers do not depend on prices, so these effects are exact; the price-response line at the end is an estimate."
LV["A2"].font = F(italic=True, color=GREY)
lvr = [4]


def lv_title(text, sub=""):
    lvr[0] += 1
    LV.cell(lvr[0], 1, text).font = F(bold=True, size=12, color=TEAL)
    lvr[0] += 1
    if sub:
        LV.cell(lvr[0], 1, sub).font = F(italic=True, color=GREY)
        lvr[0] += 1


def lv_head(heads):
    for j, h in enumerate(heads):
        c = LV.cell(lvr[0], 1 + j, h)
        c.font = F(bold=True, color=WHITE)
        c.fill = HEAD_FILL
        c.alignment = Alignment(wrap_text=True, vertical="top")
    LV.row_dimensions[lvr[0]].height = 30
    lvr[0] += 1


def lv_sub(text):
    LV.cell(lvr[0], 1, text).font = F(bold=True)
    for col in range(1, 9):
        LV.cell(lvr[0], col).fill = SEC_FILL
    lvr[0] += 1


def lv_row(vals, fmts, inputs=(), bold=False, eur=None):
    r = lvr[0]
    for j, (v, fm) in enumerate(zip(vals, fmts)):
        if v is None:
            continue
        c = LV.cell(r, 1 + j, v(r) if callable(v) else v)
        if j in inputs:
            style(c, fmt=fm, color=BLUE, fill=IN_FILL)
        else:
            style(c, fmt=fm, bold=bold)
        if j == 1:
            c.font = F(color=GREY)
            c.alignment = Alignment(wrap_text=True, vertical="top")
    lvr[0] += 1
    if eur:
        r2 = lvr[0]
        LV.cell(r2, 1, "   in €").font = F(italic=True, color=GREY)
        for col in eur:
            LV[f"{col}{r2}"] = f"=IF(ISNUMBER({col}{r}),{col}{r}/FX_EUR,\"\")"
            style(LV[f"{col}{r2}"], fmt=EUR2, italic=True, color=GREY)
        lvr[0] += 1
    return r


Y5REV, Y5EB = f"'P&L annual'!$H${YK['revenue']}", f"'P&L annual'!$H${YK['ebitda']}"
RS = "'Clients & revenue'"
y5 = lambda key: f"SUMIF({RS}!${FC}$5:${LC}$5,5,{RS}!${FC}${R.k[key]}:${LC}${R.k[key]})"
PF5 = "((1+Price_Increase)^4*(1-Annual_Share*Annual_Free/12))"

# --- volumes behind the levers (year 5)
VOL = {}
def vol(key, label, expr, unit, fmt=NUM):
    VOL[key] = f"$C${lvr[0]}"
    lv_row([label, unit, "=" + expr], [None, None, fmt])

lv_title("Year 5 at a glance", "Base for every lever below: the current scenario and pricing option.")
lv_head(["Item", "Unit", "Year 5"])
lv_row(["Total revenue", "FCFA", f"={Y5REV}"], [None, None, NUM], eur=["C"])
lv_row(["EBITDA", "FCFA", f"={Y5EB}"], [None, None, NUM], eur=["C"])
lv_row(["EBITDA margin", "%", f"=IFERROR({Y5EB}/{Y5REV},0)"], [None, None, PCT])
lv_row(["Pricing option in use", "1 = A, 2 = B, 3 = C", "=Pricing_Option"], [None, None, "0"])

LH = ["Lever", "What it means", "Today", "Change (type here)", "After the change", "Revenue, year 5 (change)", "EBITDA, year 5 (change)", "EBITDA margin after"]
LF = [None, None, NUM, NUM, NUM, NUM, NUM, PCT]
LP = [None, None, PCT2, PCT2, PCT2, NUM, NUM, PCT]


LD = [None, None, NUM1, NUM1, NUM1, NUM, NUM, PCT]


def lever(label, what, today, change, drev, debit, pct=False, dec=False):
    """drev / debit: formulas using D{r} (the change)."""
    return lv_row([label, what, f"={today}", change, lambda r: f"=C{r}+D{r}", lambda r: "=" + drev.format(d=f"D{r}"), lambda r: "=" + debit.format(d=f"D{r}"),
                   lambda r: f"=IFERROR(({Y5EB}+G{r})/({Y5REV}+F{r}),0)"], LP if pct else (LD if dec else LF), inputs=(3,), eur=["F", "G"])


lv_title("Plans", "Prices and what is included. A higher price or a smaller allowance raises revenue but may slow sales: see the price-response line at the end.")
lv_head(LH)
for pl in PL3:
    k = {"Petite": "p", "Moyenne": "m", "Grande": "g"}[pl]
    e = f"{{d}}*{y5('pay_' + k)}*{PF5}"
    lever(f"{DISP[pl]} price", "Monthly subscription. Change in FCFA (e.g. -2000 or 5000).", f"Price_{pl}", {"Petite": -2000, "Moyenne": -5000, "Grande": -10000}[pl], e, e)
e = f"{{d}}*{y5('rev_sub')}"
lever("All plans at once", "Change in % of every plan price (e.g. -10%).", "0", -0.10, e, e, pct=True)
newc = "+".join(f"SUMIF({RS}!${FC}$5:${LC}$5,5,{RS}!${FC}${R.k['new_' + k]}:${LC}${R.k['new_' + k]})*Price_{pl}" for k, pl in (("p", "Petite"), ("m", "Moyenne"), ("g", "Grande")))
e = f"-{{d}}*({newc})*{PF5}"
lever("Free months at sign-up", "Each extra free month gives away one month of subscription for every new client.", "Free_Months", 1, e, e)
act = y5("act_total")
lever("Paid bank transfers above the allowance", "Average extra bank transfers each client pays for per month. A smaller allowance raises it.", "0", 1, f"{{d}}*{act}*Overage_Fee", f"{{d}}*{act}*(Overage_Fee-Supplier_Payout_Cost)", dec=True)
lever("Fee per extra transfer", "Price of each transfer above the allowance (FCFA).", "Overage_Fee", 100, f"{{d}}*{y5('overage')}", f"{{d}}*{y5('overage')}")
lever("Extra users per client", "Average users above the plan, e.g. if Pro included 2 users instead of 3.", "0", 0.5, f"{{d}}*{act}*Extra_User_Fee", f"{{d}}*{act}*Extra_User_Fee", dec=True)
lever("Fee per extra user", "Monthly fee for each user beyond the plan (FCFA).", "Extra_User_Fee", 500, f"{{d}}*{y5('users_extra')}", f"{{d}}*{y5('users_extra')}")
lever("Extra physical cards per client", "Average physical cards above the plan, e.g. if plans included fewer cards.", "0", 0.5, f"{{d}}*{act}*Extra_Card_Fee", f"{{d}}*{act}*(Extra_Card_Fee-Card_Proc_Fee)", dec=True)
lever("Fee per extra physical card", "Monthly fee for each physical card beyond the plan (FCFA).", "Extra_Card_Fee", 500, f"{{d}}*{y5('cards_extra')}", f"{{d}}*{y5('cards_extra')}")
mm_o = y5('payroll_over')
lever("Fee on mobile money above the free amount", "% of the amount sent to wallets above each plan's free amount.", "MM_Fee", 0.0015, f"{{d}}*{mm_o}", f"{{d}}*{mm_o}", pct=True)

lv_title("Paid modules and commissions", "Fees on top of the subscription.")
lv_head(LH)
lever("Payroll module: price per payslip", "FCFA per payslip (payslip plus the monthly declarations).", "Payslip_Fee", 250, f"{{d}}*{y5('payslips')}", f"{{d}}*{y5('payslips')}")
lever("Payroll module: uptake", "Share of client employees covered (at maturity).", "Payroll_Mod_Uptake", 0.10, f"{{d}}/Payroll_Mod_Uptake*{y5('payslips')}*Payslip_Fee", f"{{d}}/Payroll_Mod_Uptake*{y5('payslips')}*(Payslip_Fee-Payslip_Cost)", pct=True)
lever("International payments: fixed fee", "FCFA per payment, Kelen's margin.", "Intl_Fixed_Fee", 250, f"{{d}}*{y5('intl_vol')}/Intl_Avg_Payment", f"{{d}}*{y5('intl_vol')}/Intl_Avg_Payment")
lever("International payments: fee", "% charged on international payments (today the same as the cost).", "Intl_Fee", 0.005, f"{{d}}*{y5('intl_vol')}", f"{{d}}*{y5('intl_vol')}", pct=True)
lever("International payments: uptake", "Share of clients using them (at maturity).", "Intl_Uptake", 0.10, f"{{d}}/Intl_Uptake*{y5('intl_vol')}*(Intl_Fee+Intl_Fixed_Fee/Intl_Avg_Payment)", f"{{d}}/Intl_Uptake*{y5('intl_vol')}*(Intl_Fee+Intl_Fixed_Fee/Intl_Avg_Payment-Intl_Cost)", pct=True)
lever("Card spending in other currencies: fee", "Fee on card payments in other currencies (ads, software, travel).", "FX_Fee", 0.005, f"{{d}}*{y5('spend_for')}", f"{{d}}*{y5('spend_for')}", pct=True)
fx_net = "(FX_Fee+FX_Fixed_Fee/FX_Avg_Txn+FX_Interchange-Scheme_Rate-Scheme_Fixed/FX_Avg_Txn-Fraud_Rate)"
lever("Foreign card spending allowed (FX rules)", "Share of SME foreign card spending the 2024 FX rules allow (1 = all). E.g. -0.4 if ads and software by card are blocked.", "Foreign_Spend_Factor", -0.4, f"{{d}}/Foreign_Spend_Factor*{y5('spend_for')}*(FX_Fee+FX_Fixed_Fee/FX_Avg_Txn+FX_Interchange)", f"{{d}}/Foreign_Spend_Factor*{y5('spend_for')}*{fx_net}", dec=True)
pl_m = f"{y5('pl_coll')}*PL_Momo_Share"
lever("Payment links: fee", "Fee on mobile-money collections through payment links.", "PL_Fee", 0.005, f"{{d}}*{pl_m}", f"{{d}}*{pl_m}", pct=True)
bal = f"{y5('balances')}/12"
lv_title("Possible income from partners (not in the plan)", "Goes to the partner bank, which owns the accounts and cards; nothing obliges it to share. Kept at zero in the P&L. What each would add if negotiated.")
lv_head(LH)
lever("Interchange share on FCFA card spending", "Part of the fee shops pay on card payments, if the bank shares it.", "Interchange_Share", 0.003, f"{{d}}*{y5('spend_dom')}", f"{{d}}*{y5('spend_dom')}", pct=True)
lever("Interchange on card spending abroad", "Paid by Visa / Mastercard to the issuing bank, if shared.", "FX_Interchange", 0.008, f"{{d}}*{y5('spend_for')}", f"{{d}}*{y5('spend_for')}", pct=True)
lever("Share of bank income on balances", "Part of what the bank earns on client balances, per year, if shared.", "Deposit_Share", 0.0125, f"{{d}}*{bal}", f"{{d}}*{bal}", pct=True)

lv_title("Costs to negotiate", "Lower costs raise EBITDA without changing what clients pay. Type a negative change for a lower cost.")
lv_head(LH)
cs5 = f"SUMIF('Costs'!${FC}$5:${LC}$5,5,'Costs'!${FC}${C.k['v_wallet']}:${LC}${C.k['v_wallet']})"
lever("Transfers to wallets: average cost per transfer", "FCFA per transfer to a wallet (salaries and others). E.g. -200 for a cheaper PI-SPI price.", f"IFERROR({cs5}/{y5('mm_n')},0)", -200, "0", f"-{{d}}*{y5('mm_n')}")
lever("Transfers to bank accounts", "Cost per transfer through the partner bank (FCFA).", "Supplier_Payout_Cost", -150, "0", f"-{{d}}*{y5('supplier')}*(1-Sup_Wallet_Share)")
lever("International payments: cost", "Partner bank FX spread and correspondent fees (unknown).", "Intl_Cost", 0.003, "0", f"-{{d}}*{y5('intl_vol')}", pct=True)
lever("Card spending in other currencies: cost", "Visa / Mastercard cross-border fees (unknown).", "Scheme_Rate", 0.003, "0", f"-{{d}}*{y5('spend_for')}", pct=True)
lever("Card processing", "Per active card per month (FCFA).", "Card_Proc_Fee", -500, "0", f"-{{d}}*{y5('cards_active')}")
lever("Partner bank fee per account", "Per business account per month (FCFA).", "Bank_Fee", -1500, "0", f"-{{d}}*{act}")

# --- fee vs cost grids
def grid(title, sub, vol_expr, fees, costs):
    lv_title(title, sub)
    lv_head(["Fee charged → / cost to Kelen ↓", "Net margin on 1M FCFA"] + [f"Fee {f:.1%}".replace(".0%", "%") for f in fees])
    for c_ in costs:
        lv_row([f"Cost {c_:.1%}".replace(".0%", "%"), f"=1000000*({fees[1]}-{c_})"] + [f"=({f}-{c_})*{vol_expr}" for f in fees],
               [None, NUM] + [NUM] * len(fees))
grid("International payments: year-5 EBITDA by fee and cost", "Cost is unknown until a provider quotes. Each cell = (fee − cost) × year-5 volume sent, before the fixed fee per payment. Middle column of fees = net margin shown in column B.",
     y5("intl_vol"), (0.03, 0.035, 0.04, 0.045), (0.025, 0.03, 0.035, 0.04))
grid("Card spending in other currencies: year-5 EBITDA by fee and cost", "Visa / Mastercard cross-border fees are unknown until the processor quotes. Each cell = (fee − cost) × year-5 foreign card spending, before the fixed fees per payment.",
     y5("spend_for"), (0.02, 0.025, 0.03, 0.035), (0.01, 0.012, 0.015, 0.02))

# --- insurance referrals (outside the P&L)
lv_title("Insurance referrals (kept outside the plan)", "Kelen introduces clients to an insurer (staff health cover, vehicle fleets) and earns a commission. Not in the P&L: what it could add in year 5.")
lv_head(["Item", "What it means", "Value"])
ri = {}
for k_, lab, what, v_, fm in (("u", "Clients insured through Kelen", "Share of active clients", 0.10, PCT), ("p", "Average premium per insured client", "FCFA a month (health cover for staff, fleet)", 150000, NUM),
                              ("c", "Commission", "% of premiums paid by the insurer", 0.10, PCT), ("k", "Cost of running it", "% of commissions (support, partner management)", 0.20, PCT)):
    ri[k_] = lv_row([lab, what, v_], [None, None, fm], inputs=(2,))
ri["rev"] = lv_row(["Revenue, year 5", "Active client-months × share insured × premium × commission", f"={act}*C{ri['u']}*C{ri['p']}*C{ri['c']}"], [None, None, NUM], bold=True, eur=["C"])
lv_row(["EBITDA, year 5", "Revenue × (1 − running cost)", f"=C{ri['rev']}*(1-C{ri['k']})"], [None, None, NUM], bold=True, eur=["C"])

# --- price response (estimate)
lv_title("If lower prices bring more clients (estimate)", "The model's sales come from reps, partners and ads, not from price. This line estimates the trade-off: a price cut on every plan, with more clients signing as a result.")
lv_head(["Item", "What it means", "Value"])
rp = lv_row(["Price cut on all plans", "% (negative = cheaper)", -0.10], [None, None, PCT], inputs=(2,))
rq = lv_row(["Extra clients it brings", "% more active clients in year 5 (your estimate)", 0.05], [None, None, PCT], inputs=(2,))
gm_ex = f"('P&L annual'!$H${YK['revenue']}-'P&L annual'!$H${YK['rev_credit']}-'P&L annual'!$H${YK['cogs']})"
rs_ = lv_row(["Subscriptions lost on existing clients", "Price cut × year-5 subscriptions", f"=C{rp}*{y5('rev_sub')}"], [None, None, NUM], eur=["C"])
rg = lv_row(["Margin from the extra clients", "Extra clients × year-5 gross margin before credit, at the new price", f"=C{rq}*({gm_ex}+C{rs_})"], [None, None, NUM], eur=["C"])
lv_row(["Net effect on EBITDA, year 5", "Positive means the price cut pays for itself", f"=C{rs_}+C{rg}"], [None, None, NUM], bold=True, eur=["C"])
lv_row(["Extra clients needed to break even", "% more clients that would offset the price cut", f"=IFERROR(-C{rs_}/({gm_ex}+C{rs_}),0)"], [None, None, PCT], bold=True)

# =====================================================================================
# DASHBOARD
# =====================================================================================
D = wb.create_sheet("Dashboard")
title(D, "Kelen business plan: dashboard", "Key results for the scenario selected on Assumptions. FCFA in columns B–H, euros in column D (headline) and J–N (year by year).")
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
    ("   in euros", "=B9/FX_EUR", EURN, "€"),
    ("Equity raised in the plan", f"=SUM('Cash flow'!{FC}{Q.k['equity']}:{LC}{Q.k['equity']})", NUM, "FCFA"),
    ("   in euros", "=B11/FX_EUR", EURN, "€"),
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
for r_ in (13, 15):
    D.cell(r_, 4, f"=B{r_}/FX_EUR")
    style(D.cell(r_, 4), fmt=EURN, bold=True)
D["E13"] = '=IF(B13<0,"Cash goes negative: raise more or earlier (Assumptions, section 11)","OK: cash stays positive")'
for r_, lab, fml, fm in ((16, "Technology from Maak", '=IF(Maak_Option=1,"Lease (option 1)","Equity stake (option 2)")', None),
                         (17, "   Maak's stake in Kelen", "=IF(Maak_Option=2,Maak_Equity_Pct,0)", PCT)):
    D.cell(r_, 1, lab).font = F()
    D.cell(r_, 2, fml)
    style(D.cell(r_, 2), fmt=fm, bold=True)
style(D["E13"], bold=True, color="C00000")
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
        ("Loan book (end of year)", "book", NUM)]
DUNIT = {"clients": "clients", "new_clients": "clients", "headcount": "people", "gm_pct": "%", "ebitda_pct": "%"}
for jj in range(5):
    D[f"{CL(10 + jj)}19"] = f"=\"Y\"&{jj + 1}&\" (€)\""
    style(D[f"{CL(10 + jj)}19"], bold=True, fill=SEC_FILL, align="center")
    D.column_dimensions[CL(10 + jj)].width = 16
for j, (lab, key, fm) in enumerate(dash):
    r = 20 + j
    D.cell(r, 1, lab).font = F(bold=key in ("revenue", "ebitda", "clients"))
    D.cell(r, 2, DUNIT.get(key, "FCFA")).font = F(color=GREY)
    for jj in range(5):
        col = CL(4 + jj)
        D[f"{col}{r}"] = f"='P&L annual'!{col}{YK[key]}"
        style(D[f"{col}{r}"], fmt=fm, bold=key in ("revenue", "ebitda", "clients"), color=GREEN)
        if DUNIT.get(key, "FCFA") == "FCFA":
            D[f"{CL(10 + jj)}{r}"] = f"={col}{r}/FX_EUR"
            style(D[f"{CL(10 + jj)}{r}"], fmt=EURN, bold=key in ("revenue", "ebitda"))
for j, (lab, key, fm, un) in enumerate([("Revenue per active client a month (ARPA)", "arpa", NUM, "FCFA / month"), ("Blended CAC", "cac", NUM, "FCFA / client"), ("CAC payback (months)", "payback", NUM1, "months")]):
    r = 20 + len(dash) + j
    D.cell(r, 1, lab).font = F()
    D.cell(r, 2, un).font = F(color=GREY)
    for jj in range(5):
        col = CL(4 + jj)
        D[f"{col}{r}"] = f"='Unit economics'!{col}{UK[key]}"
        style(D[f"{col}{r}"], fmt=fm, color=GREEN)
        if un.startswith("FCFA"):
            D[f"{CL(10 + jj)}{r}"] = f"={col}{r}/FX_EUR"
            style(D[f"{CL(10 + jj)}{r}"], fmt=EURN)
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
D.add_chart(ch, "P4")
lc = LineChart()
lc.title = "Active clients by month"
lc.height, lc.width = 8, 17
lc.add_data(Reference(R.ws, min_col=C0, max_col=C0 + NM - 1, min_row=R.k["act_total"], max_row=R.k["act_total"]), from_rows=True, titles_from_data=False)
lc.series[0].tx = SeriesLabel(v="Active clients")
lc.set_categories(Reference(R.ws, min_col=C0, max_col=C0 + NM - 1, min_row=3, max_row=3))
D.add_chart(lc, "P21")
cc = LineChart()
cc.title = "Closing cash by month (FCFA)"
cc.height, cc.width = 8, 17
cc.add_data(Reference(Q.ws, min_col=C0, max_col=C0 + NM - 1, min_row=Q.k["close"], max_row=Q.k["close"]), from_rows=True, titles_from_data=False)
cc.series[0].tx = SeriesLabel(v="Closing cash")
cc.set_categories(Reference(Q.ws, min_col=C0, max_col=C0 + NM - 1, min_row=3, max_row=3))
D.add_chart(cc, "P38")
for chart_, colours in ((ch, (TEAL, "9AA3AF", INK)), (lc, (TEAL,)), (cc, (TEAL,))):
    for ser, col in zip(chart_.series, colours):
        ser.graphicalProperties.solidFill = col
        ser.graphicalProperties.line.solidFill = col
        if chart_ is not ch:
            ser.graphicalProperties.line.width = 28575
            ser.smooth = False

# =====================================================================================
# UNIT COSTS AND PRICES: what one employee, one client, one loan and each fixed item cost or earn
# =====================================================================================
UC = wb.create_sheet("Unit costs")
title(UC, "Unit costs and prices", "What one of each thing costs or earns, in FCFA with the euro amount on the 'in €' line underneath. Every cell links to the inputs on Assumptions and Hiring plan: change them there.")
for col, w in {"A": 46, "B": 30, "C": 12}.items():
    UC.column_dimensions[col].width = w
for j in range(3, 14):
    UC.column_dimensions[CL(1 + j)].width = 15
EUR2 = '"€"#,##0.00;-"€"#,##0.00;"-"'
ucr = [4]


def uc_title(text, sub=""):
    ucr[0] += 1
    UC.cell(ucr[0], 1, text).font = F(bold=True, size=12, color=TEAL)
    ucr[0] += 1
    if sub:
        UC.cell(ucr[0], 1, sub).font = F(italic=True, color=GREY)
        ucr[0] += 1


def uc_head(heads):
    for j, h in enumerate(heads):
        c = UC.cell(ucr[0], 1 + j, h)
        c.font = F(bold=True, color=WHITE)
        c.fill = HEAD_FILL
        c.alignment = Alignment(wrap_text=True, vertical="top")
    UC.row_dimensions[ucr[0]].height = 30
    ucr[0] += 1


def uc_sub(text):
    UC.cell(ucr[0], 1, text).font = F(bold=True)
    for col in range(1, 15):
        UC.cell(ucr[0], col).fill = SEC_FILL
    ucr[0] += 1


def uc_row(vals, fmts, bold=False, eur=None):
    """One row; with eur (column letters), an 'in €' row underneath converts those FCFA cells."""
    r = ucr[0]
    for j, (v, fm) in enumerate(zip(vals, fmts)):
        if v is None:
            continue
        c = UC.cell(r, 1 + j, v(r) if callable(v) else v)
        style(c, fmt=fm, bold=bold, color=GREEN if isinstance(c.value, str) and "!" in c.value and j == 0 else BLACK)
        if j == 1 and fm is None:
            c.font = F(color=GREY)
            c.alignment = Alignment(wrap_text=True, vertical="top")
    ucr[0] += 1
    if eur:
        r2 = ucr[0]
        UC.cell(r2, 1, "   in €").font = F(italic=True, color=GREY)
        for col in eur:
            UC[f"{col}{r2}"] = f"=IF(ISNUMBER({col}{r}),{col}{r}/FX_EUR,\"\")"
            style(UC[f"{col}{r2}"], fmt=EUR2, italic=True, color=GREY)
        ucr[0] += 1
    return r



# --- each service
MMC = lambda amt: f"(IF(MM_Cost_Cap>0,MIN(MM_Cost_Pct*{amt},MM_Cost_Cap),MM_Cost_Pct*{amt})+MM_Cost_Flat)"
uc_title("Each service: what the client pays, what it costs Kelen, what Kelen keeps", "One example of each service, in FCFA, at the current scenario's costs. 'Status' says how solid the cost is: quoted, researched (public prices) or estimate. Kelen never pays the 0.6% tax on transfers out of the zone or the transfer tax: they are passed on at cost.")
uc_head(["Service (example)", "Who Kelen pays", "Client pays", "Cost to Kelen", "Kelen keeps", "Margin", "Status of the cost"])
svc_f = [None, None, NUM, NUM, NUM, PCT, None]


def svc(label, who, pays, cost, status):
    return uc_row([label, who, "=" + pays, "=" + cost, lambda r: f"=C{r}-D{r}", lambda r: f"=IF(C{r}>0,E{r}/C{r},\"\")", status], svc_f, eur=list("CDE"))


uc_sub("Account and plan")
svc("Pro plan, one month (bank fee and messaging only)", "Partner bank (fee per account), WhatsApp / SMS", "Price_Moyenne", "Bank_Fee+Notif_Cost", "Bank fee: estimate, no term sheet yet")
svc("Opening a new client (identity checks)", "Identity-check vendor", "0", "KYB_Cost+KYC_Cost*KYC_Persons", "Researched (vendor prices)")
svc("Extra user, one month", "Nobody", "Extra_User_Fee", "0", "")
uc_sub("Transfers")
svc("Bank transfer to a supplier, inside the allowance", "Partner bank", "0", "Supplier_Payout_Cost", "Researched: 150–2,000 FCFA in bank tariffs; same-bank transfers free")
svc("Bank transfer above the allowance", "Partner bank", "Overage_Fee", "Supplier_Payout_Cost", "Researched, as above")
svc("Salary to a bank account", "Partner bank", "0", "Bank_Payout_Cost", "Researched, as above")
svc("75,000 FCFA to a wallet, inside the free amount", "Wave / Orange Money (or an aggregator)", "0", MMC(75000), "Public price: 1% (no deal yet)")
svc("200,000 FCFA salary to a wallet, above the free amount", "Wave / Orange Money (or an aggregator)", "MIN(MM_Fee*200000,MM_Fee_Cap)", MMC(200000), "Public price: 1% (no deal yet)")
svc("1,000,000 FCFA to a wallet, above the free amount (both caps apply)", "Wave / Orange Money (or an aggregator)", "MIN(MM_Fee*1000000,MM_Fee_Cap)", MMC(1000000), "5,000 FCFA cap: secondary source, to verify")
svc("100,000 FCFA collected by Wave through a payment link", "Wave / Orange Money (or an aggregator)", "PL_Fee*100000", "PL_Cost*100000", "Public price: about 1%")
uc_sub("Cards")
svc("Active card, one month", "Card processor", "0", "Card_Proc_Fee", "Estimate: processors quote privately")
svc("Extra physical card (one-off)", "Card printer", "Card_Fee", "Card_Prod_Cost", "Researched: 3,000–6,000 FCFA")
svc("50,000 FCFA card payment in FCFA", "Fraud and disputes (interchange stays with the bank)", "0", "50000*Fraud_Rate", "Estimate")
svc("25,000 FCFA card payment in dollars (ads, software)", "Visa / Mastercard and the partner bank (FX margin)", "25000*FX_Fee+FX_Fixed_Fee", "25000*(Scheme_Rate+Fraud_Rate)+Scheme_Fixed", "Researched: network fees about 0.9% + $0.43; bank FX margin to quote")
uc_sub("International payments and payroll")
svc("1,000,000 FCFA paid to a supplier abroad", "Partner bank or provider (Capi Money…)", "1000000*Intl_Fee+Intl_Fixed_Fee", "1000000*Intl_Cost", "Assumed: provider not chosen; break-even on the rate")
svc("One payslip with the monthly declarations", "WhatsApp / SMS, computing", "Payslip_Fee", "Payslip_Cost", "Researched")
uc_sub("Credit")
svc("1,000,000 FCFA credit line for a year, Kelen's own SFD", "Lenders (cost of funds), credit losses, servicing", "1000000*Yield_Line", "1000000*(CoF+CoR_Line*CoR_Mult+Servicing)", "With the partner SFD, Kelen keeps its share of this (Assumptions, section 7)")

# --- one employee
uc_title("One employee, per month", "Employer cost plus what each person adds: Regus desk, phone, Gmail and ClickUp, a Claude seat for the CTO and developers. One-off at hiring: a laptop (a MacBook for the CTO and developers), plus the agency fee for senior roles.")
uc_head(["Role", "Country", "Agency hire", "Gross salary", "Employer charges", "Employer cost", "Office (Regus)", "Phone and data", "Gmail and ClickUp", "Claude seat",
         "All-in per month", "One-off at hiring"])
emp_f = [None, None, None, NUM, NUM, NUM, NUM, NUM, NUM, NUM, NUM, NUM]
EMP_EUR = list("DEFGHIJKL")
common = [lambda r: f"=D{r}*Employer_Charges", lambda r: f"=D{r}+E{r}", lambda r: "=Regus_EUR*FX_EUR", lambda r: "=Phone_Cost",
          lambda r: "=(Gmail_USD+ClickUp_USD)*FX_USD"]
tail = lambda eng: [lambda r: f"=SUM(F{r}:J{r})",
                    lambda r: f"=IF({eng},Laptop_Dev_USD*FX_USD,Laptop_EUR*FX_EUR)+IF(C{r}=\"Y\",Agency_Fee_EUR*FX_EUR,0)"]
for k in range(len(HIRES)):
    hr = H0 + k
    uc_row([f"='Hiring plan'!C{hr}", f"='Hiring plan'!D{hr}", f"='Hiring plan'!J{hr}", f"='Hiring plan'!I{hr}"] + common
           + [f"=IF('Hiring plan'!B{hr}=\"Engineering & product\",Claude_USD*FX_USD,0)"] + tail(f"'Hiring plan'!B{hr}=\"Engineering & product\""), emp_f, eur=EMP_EUR)
for lab, cty, flag, sal, claude in (("Customer support agent", "SN", "Agency_Support", "Salary_Support", False), ("Developer", "SN", "Agency_Dev", "Salary_Dev", True),
                                    ("Field sales rep, Senegal", "SN", "Agency_Rep", "Salary_Rep_SN", False), ("Field sales rep, Côte d'Ivoire", "CI", "Agency_Rep", "Salary_Rep_CI", False),
                                    ("Credit analyst", "SN", "Agency_Credit", "Salary_Credit", False)):
    uc_row([lab + " (grows with volume)", cty, f"=IF({flag}=1,\"Y\",\"N\")", f"={sal}"] + common + ["=Claude_USD*FX_USD" if claude else "=0"] + tail("TRUE" if claude else "FALSE"), emp_f, eur=EMP_EUR)
UC.cell(ucr[0], 1, "Company-wide, not per person: 2 shared Claude seats, the website and domain. Field reps also get the transport allowance (Sales & marketing). Pay rises 5% a year from year 2.").font = F(italic=True, color=GREY)
ucr[0] += 1

# --- one client
uc_title("One business client, per month, by plan", "Steady state: after the free month, payment links and paid modules at full adoption, no credit. Pricing option and scenario inputs at their current value.")
uc_head(["Line", "How it is calculated", "", "Essentiel (small firm)", "Pro (mid-size firm)", "Business (large firm)"])
PL3 = ("Petite", "Moyenne", "Grande")
cli_f = [None, None, None, NUM, NUM, NUM]


def cli(label, how, expr, bold=False, fmt=NUM):
    vals = [label, how, None] + [(lambda r, pl=pl: "=" + expr.replace("{P}", pl)) for pl in PL3]
    return uc_row(vals, [None, None, None, fmt, fmt, fmt], bold=bold, eur=list("DEF"))


def cli_tot(label, how, fn, bold=True):
    return uc_row([label, how, None] + [(lambda r, c=c: fn(c)) for c in "DEF"], cli_f, bold=bold, eur=list("DEF"))


uc_sub("Revenue")
rev_rows = [
    cli("Subscription (after the yearly-billing discount)", "Plan price × (1 − share paying yearly × free months on yearly billing ÷ 12)", "Price_{P}*(1-Annual_Share*Annual_Free/12)"),
    cli("Fees on foreign-currency card spending", "Foreign-currency card spending × (FX fee + fixed fee ÷ average payment)", "Spend_For_{P}*Foreign_Spend_Factor*(FX_Fee+FX_Fixed_Fee/FX_Avg_Txn)"),
    cli("Bank transfers above the plan allowance", "Paid bank transfers above the allowance × fee per transfer", "Overage_{P}*(1-Sup_Wallet_Share)*Overage_Fee"),
    cli("Payment link fees (average client)", "Collections × adoption × share by mobile money × fee", "PL_Coll_{P}*PL_Adoption*PL_Momo_Share*PL_Fee"),
    cli("Extra users", "Users beyond the plan × fee per user", "MAX(0,Users_{P}-Users_Incl_{P})*Extra_User_Fee"),
        cli("Mobile money above the free amount (average client)", "Amount sent to wallets above the plan's free amount × fee (clients spread around the average)", "(MM_Low_Share*MAX(0,0.5*(Emp_{P}*Avg_Salary*Wallet_Share+Supplier_{P}*Sup_Wallet_Share*Sup_Avg_Amount)-MM_Free_{P})+MM_Mid_Share*MAX(0,(Emp_{P}*Avg_Salary*Wallet_Share+Supplier_{P}*Sup_Wallet_Share*Sup_Avg_Amount)-MM_Free_{P})+(1-MM_Low_Share-MM_Mid_Share)*MAX(0,2.25*(Emp_{P}*Avg_Salary*Wallet_Share+Supplier_{P}*Sup_Wallet_Share*Sup_Avg_Amount)-MM_Free_{P}))*MM_Fee"),
    cli("Payroll module (average client)", "Employees × uptake × price per payslip", "Emp_{P}*Payroll_Mod_Uptake*Payslip_Fee"),
    cli("International payments (average client)", "Monthly volume × uptake × (fee + fixed fee ÷ average payment)", "Intl_Vol_{P}*Intl_Uptake*(Intl_Fee+Intl_Fixed_Fee/Intl_Avg_Payment)"),
]
r_revt = cli_tot("Revenue per client", None, lambda c: "=" + "+".join(f"{c}{x}" for x in rev_rows))
uc_sub("Cost to serve")
cost_rows = [
    cli("Partner bank fee per business account", "Flat fee per account", "Bank_Fee"),
    cli("Card processing", "Active cards × processing fee per card", "Cards_Act_{P}*Card_Proc_Fee"),
    cli("Visa / Mastercard cross-border fees", "Foreign-currency card spending × (scheme rate + fixed fee ÷ average payment)", "Spend_For_{P}*Foreign_Spend_Factor*(Scheme_Rate+Scheme_Fixed/FX_Avg_Txn)"),
    cli("Fraud and chargebacks", "All card spending × fraud rate", "(Spend_Dom_{P}+Spend_For_{P}*Foreign_Spend_Factor)*Fraud_Rate"),
    cli("Transfers to wallets (salaries and others)", "Transfers to wallets × cost per transfer", "Emp_{P}*Wallet_Share*(IF(MM_Cost_Cap>0,MIN(MM_Cost_Pct*Avg_Salary,MM_Cost_Cap),MM_Cost_Pct*Avg_Salary)+MM_Cost_Flat)+Supplier_{P}*Sup_Wallet_Share*(IF(MM_Cost_Cap>0,MIN(MM_Cost_Pct*Sup_Avg_Amount,MM_Cost_Cap),MM_Cost_Pct*Sup_Avg_Amount)+MM_Cost_Flat)"),
    cli("Salaries paid to bank accounts", "Employees × share to banks × cost per transfer", "Emp_{P}*(1-Wallet_Share)*Bank_Payout_Cost"),
    cli("Transfers to bank accounts", "Transfers to banks × cost per transfer", "Supplier_{P}*(1-Sup_Wallet_Share)*Supplier_Payout_Cost"),
    cli("International payments", "Monthly volume × uptake × cost", "Intl_Vol_{P}*Intl_Uptake*Intl_Cost"),
    cli("Payroll module", "Employees × uptake × cost per payslip", "Emp_{P}*Payroll_Mod_Uptake*Payslip_Cost"),
    cli("Payment link collection costs", "Collections × adoption × share by mobile money × operator cost", "PL_Coll_{P}*PL_Adoption*PL_Momo_Share*PL_Cost"),
    cli("SMS, WhatsApp and support tools", "Flat per client", "Notif_Cost"),
]
r_ct = cli_tot("Cost to serve per client", None, lambda c: "=" + "+".join(f"{c}{x}" for x in cost_rows))
r_cm = cli_tot("Contribution per client per month", "Revenue − cost to serve", lambda c: f"={c}{r_revt}-{c}{r_ct}")
uc_row(["Contribution margin", None, None] + [(lambda r, c=c: f"=IFERROR({c}{r_cm}/{c}{r_revt},0)") for c in "DEF"], [None, None, None, PCT, PCT, PCT])
uc_sub("Once, when the client signs up")
cli("Onboarding check tools", "Company screening + people checked × ID check (our team's review time is in salaries)", "KYB_Cost+KYC_Cost*KYC_Persons")
cli("Physical cards printed and delivered", "Cards ordered at sign-up × cost per card", "Cards_New_{P}*Card_Prod_Cost")
cli("Card fees charged to the client (revenue)", "(Cards ordered − cards in the plan) × card fee", "MAX(0,Cards_New_{P}-Cards_Phys_Incl_{P})*Card_Fee")
cli("Referral fee (partner-channel clients only)", "Fee paid to the accountant or software partner", "Referral_Fee")
cli("Subscription given away (free months)", "Free months × plan price", "Free_Months*Price_{P}")

# --- one loan
uc_title("One loan: 1,000,000 FCFA lent for a year", "Net margin after cost of funds, credit losses and servicing; what Kelen keeps with the partner SFD and with its own SFD; cash Kelen must lock up.")
uc_head(["Product", "Yield", "Cost of funds", "Credit losses", "Servicing", "Net margin", "Net margin a year", "Kelen keeps, partner phase",
         "Kelen keeps, own SFD", "Cash locked, partner phase", "Cash locked, own SFD"])
for pk, lab, *_ in PRODS:
    uc_row([lab, f"=Yield_{pk}", "=CoF", f"=CoR_{pk}*CoR_Mult", "=Servicing", lambda r: f"=B{r}-C{r}-D{r}-E{r}", lambda r: f"=F{r}*1000000",
            lambda r: f"=G{r}*Partner_Share", lambda r: f"=G{r}", "=1000000*First_Loss", "=1000000*Capital_Ratio"],
           [None, PCT, PCT, PCT2, PCT, PCT2, NUM, NUM, NUM, NUM, NUM], eur=list("GHIJK"))
UC.cell(ucr[0], 1, "The usury cap is 24% a year all-in (TEG) for microfinance institutions: interest plus every fee charged to the borrower.").font = F(italic=True, color=GREY)
ucr[0] += 1

# --- price list and fixed items
uc_title("Price list and fixed items", "List prices clients pay, and the price of each fixed cost at its year-1 level (later years on Assumptions, section 10).")
uc_head(["Item", "Unit", "Price", "In FCFA"])
conv = lambda r, unit: f"=C{r}" if unit.startswith("FCFA") else (f"=C{r}*FX_USD" if unit.startswith("USD") else (f"=C{r}*FX_EUR" if unit.startswith("€") else None))


def price(label, unit, expr, fmt=NUM):
    vals = [label, unit, "=" + expr]
    if conv(0, unit):
        vals += [lambda r, u=unit: conv(r, u)]
    return uc_row(vals, [None, None, fmt, NUM], eur=["D"] if conv(0, unit) else None)


uc_sub("What clients pay")
for pl in PL3:
    price(f"Subscription, {DISP[pl]}", "FCFA / month", f"Price_{pl}")
price("Extra user", "FCFA / month", "Extra_User_Fee")
price("Extra physical card (monthly)", "FCFA / month", "Extra_Card_Fee")
price("Extra physical card (printing, one-off)", "FCFA / card", "Card_Fee")
price("Bank transfer above the plan allowance", "FCFA / transfer", "Overage_Fee")
price("Mobile money above the free amount", "% of amount", "MM_Fee", PCT2)
price("Mobile money fee: cap per transfer", "FCFA / transfer", "MM_Fee_Cap")
price("Payroll module, per payslip", "FCFA / payslip", "Payslip_Fee")
price("International payment", "% of amount", "Intl_Fee", PCT2)
price("Fee on foreign-currency card spending", "% of spending", "FX_Fee", PCT2)
price("Payment link fee (mobile money)", "% of amount", "PL_Fee", PCT2)
price("Credit (factoring, payroll bridge, credit line, advances)", "% / year", "Yield_Line", PCT)
uc_sub("Technology")
price("Maak platform lease (option 1, first 3 years)", "€ / year", "IF(Maak_Option=1,Maak_Lease_EUR,0)")
price("Maak upgrades and maintenance (after the lease)", "USD / year", "Maak_Maint_USD")
price("Cloud hosting", "USD / month", "INDEX(Cloud_USD,1,1)")
price("Transaction monitoring and sanctions screening", "USD / year", "INDEX(Monitoring_USD,1,1)")
price("Freelance QA testing and DevOps on-call", "FCFA / year", "INDEX(Freelance,1,1)")
price("Laptop (non-developers)", "€ / hire", "Laptop_EUR")
price("MacBook (CTO and developers)", "USD / hire", "Laptop_Dev_USD")
price("Phone and data plan", "FCFA / person / month", "Phone_Cost")
price("Tech audit", "USD / year", "Tech_Audit_USD")
price("Website tool", "USD / month", "Website_USD")
price("Domain name", "USD / year", "Domain_USD")
price("Claude Enterprise seat", "USD / seat / month", "Claude_USD")
price("Card processor set-up (once)", "USD", "Proc_Setup_USD")
price("Card processor monthly minimum", "USD / month", "INDEX(Proc_Min_USD,1,1)")
uc_sub("Partners")
price("Partner bank set-up and card programme, Senegal (once)", "FCFA", "Bank_Setup_SN")
price("Partner bank platform minimum, Senegal", "FCFA / month", "INDEX(Bank_Min_SN,1,1)")
price("Partner bank set-up, Côte d'Ivoire (once)", "FCFA", "Bank_Setup_CI")
price("Partner bank platform minimum, Côte d'Ivoire (year 2)", "FCFA / month", "INDEX(Bank_Min_CI,1,2)")
price("Partner SFD integration (once)", "FCFA", "SFD_Setup")
price("Partner SFD running fees (year 2)", "FCFA / year", "INDEX(SFD_Annual,1,2)")
price("Card programme collateral (cash set aside, not a cost)", "FCFA", "Card_Collateral")
uc_sub("Legal, audit and insurance")
price("Company set-up, Senegal (once)", "FCFA", "Company_Setup_SN")
price("Ongoing legal counsel", "FCFA / month", "INDEX(Legal_Counsel,1,1)")
price("External accountant and tax adviser", "FCFA / month", "INDEX(Accountant_Ext,1,1)")
price("Statutory auditor", "FCFA / year", "INDEX(Auditor,1,1)")
price("Data-protection filings", "FCFA / year", "INDEX(Data_Protection,1,1)")
price("Insurance", "USD / year", "INDEX(Insurance_USD,1,1)")
uc_sub("Sales, marketing and other")
price("Digital ads budget, Senegal", "FCFA / month", "INDEX(Digital_SN,1,1)")
price("Digital ads: cost per signed client", "FCFA / client", "CAC_Digital")
price("Referral fee to partners", "FCFA / client", "Referral_Fee")
price("Field sales transport allowance", "FCFA / rep / month", "Rep_Transport")
price("Brand, launch events, PR", "FCFA / year", "INDEX(Brand_PR,1,1)")
price("Events, sponsorships, sales materials", "FCFA / year", "INDEX(Events,1,1)")
price("Travel", "FCFA / year", "INDEX(Travel,1,1)")
price("Company bank fees and miscellaneous", "FCFA / month", "INDEX(Misc,1,1)")
price("Recruitment agency fee (senior hire)", "€ / hire", "Agency_Fee_EUR")
UC.freeze_panes = "B4"

# =====================================================================================
# REGULATORY PATH (text, stage months linked to the timing inputs)
# =====================================================================================
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from reg_data import REG_NOTES, REG
G = wb.create_sheet("Regulatory path")
title(G, "Regulatory path", "What each stage needs from regulators (BCEAO / WAEMU, Senegal, Côte d'Ivoire) and where its cost sits in the model. Not legal advice: confirm with local counsel.")
for col, w in {"A": 34, "B": 30, "C": 22, "D": 70, "E": 55, "F": 40, "G": 16}.items():
    G.column_dimensions[col].width = w
gr = 4
for note in REG_NOTES:
    G.cell(gr, 1, "Note: " + note).font = F(italic=True, color=GREY)
    gr += 1
gr += 1
for j, h in enumerate(["Stage", "When", "Topic", "Requirement", "Authority and legal basis", "In the model", "Status"]):
    c = G.cell(gr, 1 + j, h)
    c.font = F(bold=True, color=WHITE)
    c.fill = HEAD_FILL
gr += 1
for stage, when, summary, items in REG:
    G.cell(gr, 1, stage).font = F(bold=True)
    G.cell(gr, 2, when).font = F(bold=True)
    G.cell(gr, 4, summary).font = F(italic=True)
    for col in range(1, 8):
        G.cell(gr, col).fill = SEC_FILL
        G.cell(gr, col).alignment = Alignment(wrap_text=True, vertical="top")
    gr += 1
    for topic, req, auth, model, status in items:
        for j, val in enumerate([topic, req, auth, model, status]):
            c = G.cell(gr, 3 + j, val)
            c.font = F(bold=j == 0, color=GREY if j == 2 else BLACK)
            c.alignment = Alignment(wrap_text=True, vertical="top")
        gr += 1
G.freeze_panes = "A7"

# =====================================================================================
# COVER
# =====================================================================================
CV = wb.create_sheet("Cover")
CV.column_dimensions["A"].width = 3
CV.column_dimensions["B"].width = 30
CV.column_dimensions["C"].width = 110
CV["B2"] = "Kelen: business plan model"
CV["B2"].font = F(bold=True, size=16, color=TEAL)
CV["B3"] = "B2B neobank for SMEs in Senegal, then Côte d'Ivoire. Five years, monthly, every figure driven by formulas."
CV["B3"].font = F(italic=True, color=GREY)
lines = [
    ("How to use", ""),
    ("1. Pick a scenario", "Assumptions › cell D4: 1 = Prudent, 2 = Base, 3 = Ambitious. Rows with three values switch with it."),
    ("2. Change any input", "Inputs are blue on a cream background (Assumptions, Hiring plan, Market). Everything else is a formula: do not type over it."),
    ("3. Change the team", "Hiring plan: the fixed roles (founder, CTO, financial expert, sales lead, marketing, country manager, compliance officer). Support, developers, field sales reps and credit analysts grow with clients and the loan book: ratios on Assumptions, section 8."),
    ("4. Check the cash", "Dashboard › checks. If cash goes negative, raise more or earlier (Assumptions, section 11)."),
    ("", ""),
    ("Tabs", ""),
    ("Dashboard", "Headline numbers, year-by-year summary and checks."),
    ("Plans", "The three plans with their prices, limits and features; add-ons, commissions, what is always free, partner income, credit rates and the A/B/C pricing options."),
    ("Assumptions", "Every hypothesis with its source: timing, acquisition, pricing, usage per client, cost to serve, credit, team and tools, Maak, fixed costs by year, funding."),
    ("Unit costs", "What one of each thing costs or earns: one employee by role, one client by plan, one loan, and the price of every fixed item."),
    ("Hiring plan", "Fixed roles, start months and salaries (employer cost = gross + 30% charges); 'Agency hire' adds the €800 agency fee."),
    ("Staff", "Headcount and employer cost by month: fixed roles plus the team that grows with volume."),
    ("Sales & marketing", "New clients by channel (field sales, partners, digital) and country; marketing budget; cost to acquire a client."),
    ("Clients & revenue", "Active clients by plan, usage (cards, balances, payroll, payouts) and every non-credit revenue line."),
    ("Credit", "Loan book by product, interest, cost of funds, losses and the share kept by Kelen; cash tied up by credit."),
    ("Costs", "Variable costs, fixed costs by category and the contingency, month by month."),
    ("P&L monthly", "Revenue, cost of revenue, gross margin, operating expenses, EBITDA, tax, net income (no depreciation: equipment is expensed)."),
    ("P&L annual", "Years 1–5, cash and funding, operating figures and a euro view."),
    ("Cash flow", "Monthly cash, cash set aside, funding rounds, runway."),
    ("Pricing levers", "What changing a price, a limit, a fee or a cost does to year-5 revenue and EBITDA; fee-versus-cost grids for international payments and card fees; insurance referrals kept outside the plan."),
    ("Unit economics", "ARPA, cost to serve, contribution, CAC, payback, lifetime value, efficiency and credit ratios."),
    ("Market", "Formal employers in Senegal and Côte d'Ivoire, target market and penetration."),
    ("Sheets ending in (€)", "The same monthly sheet with every amount in euros. Annual sheets, Dashboard, Assumptions and Hiring plan show euros in extra columns."),
    ("Regulatory path", "What each stage requires from regulators, and where its cost sits in the model."),
    ("", ""),
    ("Colour code", ""),
    ("Blue on cream", "Input: change freely."),
    ("Black", "Formula on the same sheet."),
    ("Green", "Link to another sheet."),
    ("", ""),
    ("Main caveats", ""),
    ("Estimates to replace", "Every cost line was checked against published prices and proxies in the cost research (Oct 2026, research/costs). Partner bank fees, card processing, Visa/Mastercard fees, PI-SPI business pricing (transfers to wallets) and FX costs have no public price: prudent uses public prices, base the researched value, ambitious negotiated targets. Replace them with term sheets."),
    ("Partner income", "Interchange and a share of bank income on balances go to the partner bank. No partner has agreed to share them, so the plan counts zero; Pricing levers shows what they would add."),
    ("Taxes", "Amounts exclude VAT and the 17% tax on financial activities (TAF), which apply to fees. Corporate tax is simplified (30%, losses carried forward without limit)."),
    ("Côte d'Ivoire", "Same 30% employer charges as Senegal; the number of formal employers is an estimate."),
    ("Credit", "No loans before month 18. A partner microfinance institution (SFD) lends at 23% a year, under the 24% SFD usury cap. Kelen buys an SFD around month 24 and lends from it in Senegal; Côte d'Ivoire loans stay with a partner. The loan book is funded by debt lines, not equity."),
    ("Licences", "Kelen holds no licence of its own until the SFD acquisition: partners hold the accounts, cards and loans. See Regulatory path."),
    ("Sources", "Business model v2, Cost breakdown in euros, Senegal launch plan, the market and competitor analysis (Oct 2026, research/market) and the research notes in this project, plus IPRES/ANSD 2024, CNPS and CEPICI 2025 for the market."),
]
for j, (a, b) in enumerate(lines):
    r = 5 + j
    CV.cell(r, 2, a).font = F(bold=(b == "" and a != ""), size=11 if b == "" else 10)
    CV.cell(r, 3, b).font = F()
    CV.cell(r, 3).alignment = Alignment(wrap_text=True, vertical="top")
    CV.cell(r, 2).alignment = Alignment(vertical="top")

# sheet order
order = ["Cover", "Dashboard", "Plans", "How it works", "Assumptions", "Hiring plan"]
for nm_ in ("Staff", "Sales & marketing", "Clients & revenue", "Credit", "Costs", "P&L monthly"):
    order += [nm_, TWINS[nm_]]
order += ["P&L annual", "Pricing levers", "Cash flow", TWINS["Cash flow"], "Unit economics", "Market", "Regulatory path"]
order.insert(order.index("Hiring plan"), "Unit costs")
wb._sheets = [wb[n] for n in order]
for ws in wb.worksheets:
    ws.sheet_view.showGridLines = False if ws.title in ("Cover", "Dashboard") else True
    ws.sheet_properties.tabColor = TEAL
wb.active = 0
wb.save(OUT)
print("saved", OUT)
