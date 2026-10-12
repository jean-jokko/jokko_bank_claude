"""Render the Tabax business plan workbook as one commentable artifact page (values + formulas)."""
import base64, datetime, html, sys
from openpyxl import load_workbook

XLSX, SC1, SC3, OUT = sys.argv[1:5]
wv = load_workbook(XLSX, data_only=True)
wf = load_workbook(XLSX)
E = lambda s: html.escape(str(s), quote=True)
NNBSP = " "
MINUS = "−"


def fmt_num(v, kind, scale=1):
    if v is None or v == "":
        return ""
    if isinstance(v, str):
        return E(v)
    if isinstance(v, (datetime.date, datetime.datetime)):
        return v.strftime("%d %b %Y")
    x = v / scale
    if kind == "pct":
        s = f"{abs(x) * 100:.1f}%"
    elif kind == "pct2":
        s = f"{abs(x) * 100:.2f}%"
    elif kind == "dec1":
        s = f"{abs(x):,.1f}".replace(",", NNBSP)
    elif kind == "dec2":
        s = f"{abs(x):,.2f}".replace(",", NNBSP)
    elif kind == "dec3":
        s = f"{abs(x):,.3f}".replace(",", NNBSP)
    elif kind == "mult":
        s = f"{abs(x):.1f}×"
    else:
        s = f"{abs(round(x)):,}".replace(",", NNBSP)
    if abs(x) < 1e-9:
        return '<span class="z">–</span>'
    return (f'<span class="neg">{MINUS}{s}</span>' if x < 0 else s)


def kind_of(numfmt):
    f = numfmt or ""
    if "0.00%" in f:
        return "pct2"
    if "%" in f:
        return "pct"
    if "0.0x" in f:
        return "mult"
    if f.startswith("#,##0.0") or f == "0.0":
        return "dec1"
    if f == "0.00":
        return "dec2"
    if f in ("0.000", "#,##0.000"):
        return "dec3"
    if "yy" in f:
        return "date"
    return "int"


def formula_of(ws, coord):
    v = ws[coord].value
    return v if isinstance(v, str) and v.startswith("=") else ""


# ------------------------------------------------------------------ monthly sheets
MONTH_COLS = [5 + i for i in range(60)]


def ts_table(sheet, start_after=None, k_scale=True):
    v, f = wv[sheet], wf[sheet]
    head1 = "".join(f'<th scope="col">{v.cell(4, c).value.strftime("%b %y")}</th>' for c in MONTH_COLS)
    head0 = "".join(f'<th scope="col" class="yr">Y{v.cell(5, c).value}</th>' if (c - 5) % 12 == 0 else '<th scope="col"></th>' for c in MONTH_COLS)
    rows = []
    started = start_after is None
    for r in range(7, v.max_row + 1):
        a = v.cell(r, 1).value
        if not started:
            if a == start_after:
                started = True
            continue
        e_f = f.cell(r, 5).value
        if a is None and e_f is None:
            continue
        if e_f is None:  # section header
            rows.append(f'<tr class="sec"><th scope="rowgroup" colspan="{3 + len(MONTH_COLS)}">{E(a)}</th></tr>')
            continue
        unit = v.cell(r, 2).value or ""
        kind = kind_of(f.cell(r, 5).number_format)
        scale = 1000 if (k_scale and unit == "FCFA") else 1
        unit_show = "k FCFA" if scale == 1000 else unit
        bold = bool(f.cell(r, 1).font and f.cell(r, 1).font.b)
        fm = formula_of(f, f"F{r}") or formula_of(f, f"E{r}")
        tip = f' title="Formula (month 2): {E(fm)}"' if fm else ""
        tot = fmt_num(v.cell(r, 4).value, kind, scale) if f.cell(r, 4).value is not None else ""
        cells = "".join(f"<td>{fmt_num(v.cell(r, c).value, kind, scale)}</td>" for c in MONTH_COLS)
        rows.append(f'<tr data-comment-target{" class=b" if bold else ""}><th scope="row"{tip}>{E(a)}</th><td class="u">{E(unit_show)}</td><td class="t">{tot}</td>{cells}</tr>')
    return (f'<div class="tw"><table class="ts"><thead><tr><th class="c0"></th><th class="u"></th><th class="t"></th>{head0}</tr>'
            f'<tr><th class="c0" scope="col">Line</th><th class="u" scope="col">Unit</th><th class="t" scope="col">Total / end</th>{head1}</tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>')


# ------------------------------------------------------------------ annual-style sheets (label in A, values in D..H/I)
def annual_table(sheet, cols="DEFGHI", head_row=4, first=6, scale_fcfa=None, last=None):
    v, f = wv[sheet], wf[sheet]
    heads = []
    for i, c in enumerate(cols):
        hv = v[f"{c}{head_row}"].value
        if isinstance(hv, (int, float)) and hv >= 2000:
            heads.append(f"Year {i + 1}<br><span class='fy'>{int(hv)}</span>")
        elif isinstance(hv, (int, float)) and c != "I":
            fy = v[f"{c}5"].value if sheet == "P&L annual" else None
            heads.append(f"Year {int(hv)}" + (f"<br><span class='fy'>{int(fy)}</span>" if fy else ""))
        else:
            heads.append(E(hv or ""))
    rows = []
    for r in range(first, (last or v.max_row) + 1):
        a = v.cell(r, 1).value
        d_f = f[f"D{r}"].value
        if a is None and d_f is None:
            continue
        if d_f is None and all(f[f"{c}{r}"].value is None for c in cols):
            rows.append(f'<tr class="sec"><th scope="rowgroup" colspan="{len(cols) + 2}">{E(a)}</th></tr>')
            continue
        unit = (v.cell(r, 2).value or "") if sheet != "P&L annual" else ""
        kind = kind_of(f[f"D{r}"].number_format)
        lab = str(a)
        scale = 1
        if scale_fcfa and kind == "int" and "€" not in lab and lab not in scale_fcfa.get("skip", ()):
            scale = scale_fcfa["div"]
            unit = scale_fcfa["unit"]
        elif scale_fcfa and lab in ("Revenue per active client a month (ARPA)", "Blended CAC"):
            unit = "FCFA"
        bold = bool(f.cell(r, 1).font and f.cell(r, 1).font.b)
        fm = formula_of(f, f"E{r}") or formula_of(f, f"D{r}")
        tip = f' title="Formula (year 2): {E(fm)}"' if fm else ""
        cells = "".join(f"<td>{fmt_num(v[f'{c}{r}'].value, kind, scale)}</td>" for c in cols)
        rows.append(f'<tr data-comment-target{" class=b" if bold else ""}><th scope="row"{tip}>{E(lab)}</th><td class="u">{E(unit)}</td>{cells}</tr>')
    th = "".join(f'<th scope="col">{h}</th>' for h in heads)
    return f'<div class="tw"><table class="an"><thead><tr><th class="c0" scope="col">Line</th><th class="u" scope="col">Unit</th>{th}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'


# ------------------------------------------------------------------ assumptions
def assumptions_html():
    v, f = wv["Assumptions"], wf["Assumptions"]
    out, rows, mode = [], [], None

    def flush():
        if rows:
            if mode == "scalar":
                th = "<th scope='col'>Value used</th><th scope='col'>Prudent</th><th scope='col'>Base</th><th scope='col'>Ambitious</th>"
            else:
                th = "".join(f"<th scope='col'>Year {k}</th>" for k in range(1, 6))
            out.append(f'<div class="tw"><table class="as"><thead><tr><th class="c0" scope="col">Assumption</th><th class="u" scope="col">Unit</th>{th}<th class="note" scope="col">Source / note</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>')
            rows.clear()

    for r in range(6, v.max_row + 1):
        b, c3, d = v.cell(r, 2).value, v.cell(r, 3).value, v.cell(r, 4).value
        if b is None and d is None:
            continue
        if c3 == "Unit":
            flush()
            mode = "arr" if v.cell(r, 4).value == "Year 1" else "scalar"
            out.append(f'<h3 data-comment-target>{E(b)}</h3>')
            continue
        if d is None and v.cell(r, 9).value is None:
            rows.append(f'<tr class="sub"><th scope="rowgroup" colspan="8">{E(b)}</th></tr>')
            continue
        kind = kind_of(f.cell(r, 4).number_format)
        if kind == "date":
            dv = v.cell(r, 4).value
            val = dv.strftime("%d %b %Y") if hasattr(dv, "strftime") else E(dv)
        else:
            val = fmt_num(d, kind)
        note = E(v.cell(r, 9).value or "")
        if mode == "scalar":
            scen = [v.cell(r, k).value for k in (5, 6, 7)]
            has = any(s is not None for s in scen)
            sc = "".join(f"<td{' class=in' if has else ''}>{fmt_num(s, kind) if s is not None else ''}</td>" for s in scen)
            cells = f"<td class='{'used' if has else 'in'}'>{val}</td>{sc}"
        else:
            vals = [v.cell(r, k).value for k in range(4, 9)]
            cells = "".join(f"<td class='in'>{fmt_num(x, kind) if x is not None else ''}</td>" for x in vals)
            if all(x is None for x in vals[1:]):
                cells = f"<td class='in'>{val}</td>" + "<td></td>" * 4
        rows.append(f'<tr data-comment-target><th scope="row">{E(b)}</th><td class="u">{E(c3 or "")}</td>{cells}<td class="note">{note}</td></tr>')
    flush()
    return "".join(out)


def hiring_html():
    v = wv["Hiring plan"]
    rows = []
    for r in range(5, v.max_row + 1):
        role = v.cell(r, 3).value
        if not role:
            continue
        cells = [v.cell(r, k).value for k in range(1, 13)]
        n, dep, role, cty, cat, hc, st, en, sal, mgr, cost, note = cells
        rows.append(f'<tr data-comment-target><td class="u">{n}</td><td>{E(dep)}</td><th scope="row">{E(role)}</th><td>{E(cty)}</td><td>{E(cat or "")}</td>'
                    f'<td>{fmt_num(hc, "int")}</td><td>{st}</td><td>{en or ""}</td><td>{fmt_num(sal, "int")}</td><td>{fmt_num(cost, "int")}</td><td class="note">{E(note or "")}</td></tr>')
    th = "".join(f'<th scope="col">{h}</th>' for h in ["#", "Department", "Role", "Country", "Category", "People", "Start month", "End month", "Gross salary (FCFA / month)", "Employer cost per person (FCFA / month)", "Note"])
    return f'<div class="tw"><table class="hp"><thead><tr>{th}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'


# ------------------------------------------------------------------ headline + scenarios
def dash_values(path):
    w = load_workbook(path, data_only=True)
    D, Y = w["Dashboard"], w["P&L annual"]
    lab = {Y.cell(r, 1).value: r for r in range(1, Y.max_row + 1)}
    yv = lambda name, col: Y[f"{col}{lab[name]}"].value
    return {
        "scenario": D["B4"].value, "be": D["B7"].value, "be_date": D["B8"].value, "peak": D["B9"].value, "equity": D["B11"].value,
        "low": D["B13"].value, "low_m": D["B14"].value, "end_cash": D["B15"].value,
        "rev": [yv("Total revenue", c) for c in "DEFGH"], "ebitda": [yv("EBITDA", c) for c in "DEFGH"],
        "clients": [yv("Active clients", c) for c in "DEFGH"], "hc": [yv("Headcount", c) for c in "DEFGH"],
        "ni": [yv("Net income", c) for c in "DEFGH"], "cash": [yv("Closing cash (end of year)", c) for c in "DEFGH"],
    }


base = dash_values(XLSX)
s1, s3 = dash_values(SC1), dash_values(SC3)
FX = 655.957
fy0 = wv["P&L annual"]["D5"].value
M = lambda x: fmt_num(x / 1e6, "dec1") if isinstance(x, (int, float)) else E(x)
EURM = lambda x: fmt_num(x / FX / 1e6, "dec1") if isinstance(x, (int, float)) else E(x)


def be_text(d):
    if isinstance(d["be"], (int, float)):
        return f"Month {int(d['be'])} ({d['be_date'].strftime('%b %Y')})"
    return "Not within 5 years"


kpis = [
    ("EBITDA turns positive", be_text(base), "First month with positive EBITDA"),
    ("Peak funding need", f"€{EURM(base['peak'])}M", f"{fmt_num(base['peak'] / 1e9, 'dec2')} bn FCFA of cumulative burn before break-even"),
    ("Equity in the plan", f"€{EURM(base['equity'])}M", "Seed, Series A and Series B"),
    ("Year 5 revenue", f"€{EURM(base['rev'][4])}M", f"{fmt_num(base['clients'][4], 'int')} active clients at the end of year 5"),
    ("Year 5 EBITDA", f"€{EURM(base['ebitda'][4])}M", f"{fmt_num(base['ebitda'][4] / base['rev'][4], 'pct')} of revenue"),
]
kpi_html = "".join(f'<div class="kpi" data-comment-target><div class="kl">{E(a)}</div><div class="kv">{b}</div><div class="ks">{c}</div></div>' for a, b, c in kpis)

scen_rows = [
    ("EBITDA turns positive", lambda d: be_text(d)),
    ("Peak funding need (€M)", lambda d: EURM(d["peak"])),
    ("Active clients, end of year 5", lambda d: fmt_num(d["clients"][4], "int")),
    ("Revenue year 3 (€M)", lambda d: EURM(d["rev"][2])),
    ("Revenue year 5 (€M)", lambda d: EURM(d["rev"][4])),
    ("EBITDA year 5 (€M)", lambda d: EURM(d["ebitda"][4])),
    ("Lowest closing cash with the planned rounds (€M)", lambda d: EURM(d["low"])),
]
scen_html = '<div class="tw"><table class="an sc"><thead><tr><th class="c0" scope="col">Result</th><th scope="col">Prudent</th><th scope="col" class="hl">Base</th><th scope="col">Ambitious</th></tr></thead><tbody>' + "".join(
    f'<tr data-comment-target><th scope="row">{E(l)}</th><td>{fn(s1)}</td><td class="hl">{fn(base)}</td><td>{fn(s3)}</td></tr>' for l, fn in scen_rows) + "</tbody></table></div>"


# ------------------------------------------------------------------ charts (inline SVG, drawn to scale)
def bar_chart():
    rev = [x / FX / 1e6 for x in base["rev"]]
    eb = [x / FX / 1e6 for x in base["ebitda"]]
    hi = max(rev + [0]) * 1.1
    lo = min(eb + [0]) * 1.15
    W, H, L, R_, T, B = 640, 280, 48, 12, 16, 34
    ph = H - T - B
    y = lambda val: T + (hi - val) / (hi - lo) * ph
    step = 2 if hi - lo < 16 else 5
    ticks = [t for t in range(int(lo // step) * step, int(hi) + step, step) if lo <= t <= hi]
    g = []
    for t in ticks:
        g.append(f'<line x1="{L}" x2="{W - R_}" y1="{y(t):.1f}" y2="{y(t):.1f}" class="{"zero" if t == 0 else "grid"}"/>'
                 f'<text x="{L - 6}" y="{y(t) + 4:.1f}" class="ax" text-anchor="end">{t}</text>')
    gw = (W - L - R_) / 5
    bw = gw * 0.3
    for k in range(5):
        x0 = L + k * gw + gw * 0.18
        for j, (val, cls) in enumerate(((rev[k], "b1"), (eb[k], "b2"))):
            x = x0 + j * (bw + 4)
            top, bot = (y(val), y(0)) if val >= 0 else (y(0), y(val))
            g.append(f'<rect x="{x:.1f}" y="{top:.1f}" width="{bw:.1f}" height="{max(bot - top, 0.5):.1f}" class="{cls}" rx="2"><title>{"Revenue" if j == 0 else "EBITDA"} year {k + 1}: €{val:.1f}M</title></rect>')
        g.append(f'<text x="{L + k * gw + gw / 2:.1f}" y="{H - 12}" class="ax" text-anchor="middle">Y{k + 1} · {fy0 + k}</text>')
    return (f'<figure class="chart" data-comment-target><figcaption>Revenue and EBITDA by year, € millions</figcaption>'
            f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Revenue and EBITDA by year">{"".join(g)}</svg>'
            f'<div class="legend"><span><i class="b1"></i>Revenue</span><span><i class="b2"></i>EBITDA</span></div></figure>')


def cash_chart():
    Q = wv["Cash flow"]
    lab = {Q.cell(r, 1).value: r for r in range(1, Q.max_row + 1)}
    vals = [Q.cell(lab["Closing cash"], c).value / FX / 1e6 for c in MONTH_COLS]
    hi, lo = max(vals) * 1.1, min(0, min(vals)) * 1.1
    W, H, L, R_, T, B = 640, 240, 48, 12, 16, 30
    ph = H - T - B
    y = lambda v_: T + (hi - v_) / (hi - lo) * ph
    x = lambda i: L + i * (W - L - R_) / 59
    step = 1
    while (hi - lo) / step > 6:
        step *= 2
    ticks = [t for t in range(int(lo // step) * step, int(hi) + step, step) if lo <= t <= hi]
    g = [f'<line x1="{L}" x2="{W - R_}" y1="{y(t):.1f}" y2="{y(t):.1f}" class="{"zero" if t == 0 else "grid"}"/><text x="{L - 6}" y="{y(t) + 4:.1f}" class="ax" text-anchor="end">{t}</text>' for t in ticks]
    pts = " ".join(f"{x(i):.1f},{y(v_):.1f}" for i, v_ in enumerate(vals))
    g.append(f'<polygon points="{x(0):.1f},{y(0):.1f} {pts} {x(59):.1f},{y(0):.1f}" class="area"/>')
    g.append(f'<polyline points="{pts}" class="line"/>')
    for k in range(5):
        g.append(f'<text x="{x(k * 12 + 6):.1f}" y="{H - 10}" class="ax" text-anchor="middle">Y{k + 1}</text>')
    lowi = vals.index(min(vals))
    g.append(f'<circle cx="{x(lowi):.1f}" cy="{y(vals[lowi]):.1f}" r="4" class="dot"><title>Lowest: €{vals[lowi]:.2f}M in month {lowi + 1}</title></circle>')
    return (f'<figure class="chart" data-comment-target><figcaption>Closing cash by month, € millions (after the funding rounds)</figcaption>'
            f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Closing cash by month">{"".join(g)}</svg></figure>')


# ------------------------------------------------------------------ page
tabs = [
    ("overview", "Overview"), ("assumptions", "Assumptions"), ("hiring", "Hiring plan"), ("pnl", "P&L by year"), ("pnlm", "P&L by month"),
    ("cash", "Cash flow"), ("costs", "Costs"), ("sales", "Sales & marketing"), ("revenue", "Clients & revenue"), ("credit", "Credit"),
    ("staff", "Staff"), ("unit", "Unit economics"), ("market", "Market"),
]
sections = {
    "overview": ("Overview", "Base scenario. Five years from January 2027, Senegal first, Côte d'Ivoire from month 19.",
                 f'<div class="kpis">{kpi_html}</div><div class="charts">{bar_chart()}{cash_chart()}</div>'
                 f'<h3 data-comment-target>Three scenarios</h3><p class="lead">The scenario switch changes sales productivity, partner and digital acquisition, churn, interchange, the bank income share on balances, credit volumes and credit losses.</p>{scen_html}'
                 f'<h3 data-comment-target>Year by year (FCFA millions unless stated)</h3>' + annual_table("Dashboard", cols="DEFGH", head_row=19, first=20, last=37,
                                                                                                             scale_fcfa={"div": 1e6, "unit": "M FCFA", "skip": ("Active clients (end of year)", "New clients in the year", "Headcount (end of year)", "Revenue per active client a month (ARPA)", "Blended CAC")})),
    "assumptions": ("Assumptions", "Every input of the model with its source. Values in the 'Value used' column are those of the base scenario.", assumptions_html()),
    "hiring": ("Hiring plan", "One line per hire or group of identical hires. The employer cost adds Senegal's charges, a 13th month, transport and health top-up.", hiring_html()),
    "pnl": ("P&L by year", "FCFA millions unless stated. Euro view at the bottom.", annual_table("P&L annual", scale_fcfa={"div": 1e6, "unit": "M FCFA"})),
    "pnlm": ("P&L by month", "Amounts in thousands of FCFA (k FCFA). Hover a line name to see its formula.", ts_table("P&L monthly")),
    "cash": ("Cash flow", "Amounts in thousands of FCFA. Cash set aside (licence capital, card collateral, deposits, credit reserves) is excluded from closing cash.", ts_table("Cash flow")),
    "costs": ("Costs", "Every cost line, in thousands of FCFA: variable costs, fixed costs by category, capex and depreciation.", ts_table("Costs")),
    "sales": ("Sales & marketing", "New clients by channel and country, and the non-staff marketing budget (k FCFA).", ts_table("Sales & marketing")),
    "revenue": ("Clients & revenue", "Active clients by plan, usage and revenue lines except credit (k FCFA).", ts_table("Clients & revenue")),
    "credit": ("Credit", "Loan book by product and credit income (k FCFA). The partner SFD lends until month 37, then Tabax's own SFD.", ts_table("Credit")),
    "staff": ("Staff", "Headcount and employer cost by department (k FCFA). The detail per hire is in the Excel file.", ts_table("Staff", start_after="Summary")),
    "unit": ("Unit economics", "Per-client economics and efficiency ratios by year.", annual_table("Unit economics", cols="DEFGH", first=6)),
    "market": ("Market", "Formal employers in Senegal and Côte d'Ivoire, the target market and the share the plan reaches.", annual_table("Market", cols="DEFGH", head_row=4, first=5)),
}
nav = "".join(f'<button type="button" role="tab" id="t-{k}" aria-controls="p-{k}" aria-selected="{"true" if i == 0 else "false"}" data-tab="{k}">{E(lab)}</button>' for i, (k, lab) in enumerate(tabs))
panels = "".join(
    f'<section class="panel" id="p-{k}" role="tabpanel" aria-labelledby="t-{k}"{"" if i == 0 else " hidden"}>'
    f'<div class="ph"><div><h2>{E(sections[k][0])}</h2><p class="lead">{sections[k][1]}</p></div>'
    f'<button type="button" class="cbtn" data-comment-for="p-{k}" hidden>Comment on this tab</button></div>{sections[k][2]}</section>'
    for i, (k, lab) in enumerate(tabs))
xlsx_b64 = base64.b64encode(open(XLSX, "rb").read()).decode()
today = datetime.date(2026, 10, 12).strftime("%d %B %Y")

page = f"""<title>Tabax Business Plan</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Epilogue:wght@600;800&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
/* Layout: a working financial file. Header with the five numbers that matter, tabs mirroring the Excel sheets, wide tables that scroll inside their own frame with a sticky first column. */
:root {{
  --bg: #F6F7F9; --surface: #FFFFFF; --ink: #161616; --muted: #5A6170; --line: #E3E6EB; --soft: #EEF1F5;
  --accent: #6FB6EE; --accent-ink: #1C5F96; --neg: #B42318; --hl: #E8F3FC;
  --display: 'Epilogue', 'Helvetica Neue', Arial, sans-serif; --body: 'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #0F1216; --surface: #161A20; --ink: #ECEFF3; --muted: #9AA3AF; --line: #2A3038; --soft: #1C2128;
  --accent: #6FB6EE; --accent-ink: #8FC9F5; --neg: #FF8A80; --hl: #17283A; color-scheme: dark; }} }}
:root[data-theme="dark"] {{
  --bg: #0F1216; --surface: #161A20; --ink: #ECEFF3; --muted: #9AA3AF; --line: #2A3038; --soft: #1C2128;
  --accent: #6FB6EE; --accent-ink: #8FC9F5; --neg: #FF8A80; --hl: #17283A; color-scheme: dark; }}
body {{ background: var(--bg); color: var(--ink); font-family: var(--body); font-size: 14px; line-height: 1.45; }}
.wrap {{ max-width: 1240px; margin: 0 auto; padding-inline: 16px; padding-block: 24px 64px; }}
header.top {{ display: flex; flex-wrap: wrap; gap: 16px 24px; align-items: flex-end; justify-content: space-between; }}
.eyebrow {{ font-size: 12px; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); display: flex; align-items: center; gap: 8px; }}
.eyebrow i {{ width: 10px; height: 10px; border-radius: 3px; background: var(--accent); box-shadow: inset 0 0 0 2px var(--ink); }}
h1 {{ font-family: var(--display); font-weight: 800; font-size: clamp(26px, 4vw, 38px); letter-spacing: -.02em; margin: 6px 0 4px; text-wrap: balance; }}
.sub {{ color: var(--muted); margin: 0; max-width: 70ch; }}
.actions {{ display: flex; gap: 8px; flex-wrap: wrap; }}
.btn {{ font: inherit; font-weight: 600; border: 1.5px solid var(--ink); background: var(--accent); color: #161616; border-radius: 20px; height: 38px; padding: 0 16px; cursor: pointer; }}
.btn.ghost {{ background: var(--surface); color: var(--ink); border-color: var(--line); }}
.btn:focus-visible, nav button:focus-visible, .cbtn:focus-visible {{ outline: 3px solid var(--accent); outline-offset: 2px; }}
.status {{ font-size: 13px; color: var(--muted); min-height: 1.2em; }}
nav.tabs {{ position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--bg); margin-top: 20px; padding-block: 8px; border-bottom: 1px solid var(--line); display: flex; gap: 4px; overflow-x: auto; scrollbar-width: thin; }}
nav.tabs button {{ font: inherit; font-weight: 600; font-size: 13px; color: var(--muted); background: none; border: 0; border-radius: 16px; padding: 7px 12px; white-space: nowrap; cursor: pointer; }}
nav.tabs button[aria-selected="true"] {{ background: var(--ink); color: var(--bg); }}
.panel {{ margin-top: 20px; }}
.ph {{ display: flex; flex-wrap: wrap; gap: 12px; justify-content: space-between; align-items: flex-start; }}
.ph > div {{ min-width: 0; }}
h2 {{ font-family: var(--display); font-weight: 800; font-size: 24px; margin: 0; letter-spacing: -.01em; }}
h3 {{ font-family: var(--display); font-weight: 600; font-size: 17px; margin: 28px 0 8px; }}
.lead {{ color: var(--muted); margin: 4px 0 12px; max-width: 80ch; }}
.cbtn {{ font: inherit; font-size: 13px; font-weight: 600; color: var(--accent-ink); background: var(--surface); border: 1px solid var(--line); border-radius: 16px; padding: 6px 12px; cursor: pointer; }}
.kpis {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; margin-block: 8px 16px; }}
.kpi {{ background: var(--surface); border: 1px solid var(--line); border-radius: 14px; padding: 12px 14px; min-width: 0; }}
.kl {{ font-size: 12px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: var(--muted); }}
.kv {{ font-family: var(--display); font-weight: 800; font-size: 24px; margin-top: 4px; font-variant-numeric: tabular-nums; }}
.ks {{ font-size: 12px; color: var(--muted); }}
.charts {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px; }}
.chart {{ margin: 0; background: var(--surface); border: 1px solid var(--line); border-radius: 14px; padding: 12px 14px; min-width: 0; }}
.chart figcaption {{ font-weight: 600; font-size: 13px; margin-bottom: 6px; }}
.chart svg {{ width: 100%; height: auto; display: block; }}
.chart .grid {{ stroke: var(--line); stroke-width: 1; }}
.chart .zero {{ stroke: var(--muted); stroke-width: 1.2; }}
.chart .ax {{ fill: var(--muted); font-size: 11px; font-family: var(--body); }}
.chart .b1 {{ fill: var(--accent); }}
.chart .b2 {{ fill: var(--ink); }}
.chart .line {{ fill: none; stroke: var(--accent-ink); stroke-width: 2; }}
.chart .area {{ fill: var(--hl); }}
.chart .dot {{ fill: var(--neg); }}
.legend {{ display: flex; gap: 14px; font-size: 12px; color: var(--muted); margin-top: 4px; }}
.legend i {{ display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 6px; vertical-align: -1px; }}
.legend i.b1 {{ background: var(--accent); }} .legend i.b2 {{ background: var(--ink); }}
.tw {{ overflow-x: auto; border: 1px solid var(--line); border-radius: 12px; background: var(--surface); max-width: 100%; }}
.tw + .tw {{ margin-top: 12px; }}
table {{ border-collapse: separate; border-spacing: 0; font-variant-numeric: tabular-nums; width: max-content; min-width: 100%; }}
th, td {{ padding: 6px 10px; border-bottom: 1px solid var(--line); text-align: right; white-space: nowrap; font-weight: 400; }}
thead th {{ position: sticky; top: 0; background: var(--soft); font-size: 12px; font-weight: 600; color: var(--muted); z-index: 1; }}
th[scope="row"], th.c0 {{ text-align: left; position: sticky; left: 0; background: var(--surface); z-index: 2; min-width: 240px; max-width: 360px; white-space: normal; }}
thead th.c0 {{ background: var(--soft); z-index: 3; }}
th[scope="row"][title] {{ cursor: help; text-decoration: underline dotted var(--line); text-underline-offset: 3px; }}
td.u, th.u {{ text-align: left; color: var(--muted); font-size: 12px; }}
td.t, th.t {{ font-weight: 600; background: var(--soft); }}
tr.b th, tr.b td {{ font-weight: 600; }}
tr.b th[scope="row"] {{ font-weight: 700; }}
tr.sec th {{ text-align: left; background: var(--soft); font-weight: 700; color: var(--ink); font-size: 12px; letter-spacing: .04em; text-transform: uppercase; position: static; }}
tr.sec th {{ position: sticky; left: 0; }}
tr.sub th {{ text-align: left; font-weight: 700; padding-top: 12px; }}
th.yr {{ color: var(--ink); }}
.fy {{ font-weight: 400; color: var(--muted); }}
.neg {{ color: var(--neg); }}
.z {{ color: var(--muted); }}
td.in {{ color: var(--accent-ink); }}
td.used {{ font-weight: 600; }}
td.note, th.note {{ text-align: left; white-space: normal; min-width: 280px; max-width: 520px; color: var(--muted); font-size: 12px; }}
table.as th[scope="row"] {{ min-width: 260px; }}
table.hp td {{ text-align: left; }}
table.hp th[scope="row"] {{ position: static; }}
.sc .hl {{ background: var(--hl); font-weight: 600; }}
tbody tr:hover td, tbody tr:hover th[scope="row"] {{ background: var(--hl); }}
footer {{ margin-top: 40px; color: var(--muted); font-size: 12px; max-width: 90ch; }}
@media (max-width: 600px) {{ th[scope="row"], th.c0 {{ min-width: 170px; max-width: 200px; }} .kv {{ font-size: 21px; }} }}
</style>
<div class="wrap">
<header class="top">
  <div>
    <div class="eyebrow"><i></i>Tabax (working name) · business plan · base scenario</div>
    <h1>Tabax business plan</h1>
    <p class="sub">B2B neobank for SMEs in Senegal, then Côte d'Ivoire. Five years, month by month, from the Excel model of {today}. Comment on any line: Claude updates the Excel formulas and republishes this page.</p>
  </div>
  <div>
    <div class="actions"><button type="button" class="btn" id="dl" hidden>Download the Excel model</button></div>
    <div class="status" id="dl-status" role="status"></div>
  </div>
</header>
<nav class="tabs" role="tablist" aria-label="Sheets">{nav}</nav>
{panels}
<footer>Source: the Excel model in this project (every number is a formula of the Assumptions and Hiring plan sheets). Amounts exclude VAT and the 17% tax on financial activities. Prices and costs marked as estimates on the Assumptions tab must be replaced with partner quotes.</footer>
</div>
<script type="application/octet-stream" id="xlsx">{xlsx_b64}</script>
<script>
(function () {{
  var tabs = Array.prototype.slice.call(document.querySelectorAll('nav.tabs button'));
  function show(key, focus) {{
    var found = false;
    tabs.forEach(function (b) {{
      var on = b.getAttribute('data-tab') === key;
      if (on) found = true;
      b.setAttribute('aria-selected', on ? 'true' : 'false');
      document.getElementById('p-' + b.getAttribute('data-tab')).hidden = !on;
      if (on && focus) b.scrollIntoView({{block: 'nearest', inline: 'nearest'}});
    }});
    if (!found) show('overview');
  }}
  tabs.forEach(function (b) {{
    b.addEventListener('click', function () {{ show(b.getAttribute('data-tab'), true); try {{ history.replaceState(null, '', '#' + b.getAttribute('data-tab')); }} catch (e) {{}} }});
  }});
  var h = (location.hash || '').slice(1);
  if (h) show(h);

  function start() {{
    if (!window.claude || !window.claude.use) return;
    window.claude.use('downloads').then(function (dl) {{
      if (!dl) return;
      var btn = document.getElementById('dl'), st = document.getElementById('dl-status');
      btn.hidden = false;
      btn.addEventListener('click', function () {{
        var raw = atob(document.getElementById('xlsx').textContent.trim());
        var bytes = new Uint8Array(raw.length);
        for (var i = 0; i < raw.length; i++) bytes[i] = raw.charCodeAt(i);
        st.textContent = '';
        dl.save({{filename: 'Tabax business plan.xlsx', data: new Blob([bytes])}}).then(function () {{
          st.textContent = 'Excel model saved.';
        }}, function (err) {{
          var code = err && err.code;
          if (code === 'declined') st.textContent = 'Download cancelled.';
          else if (code === 'rate_limited') st.textContent = 'A download prompt is already open.';
          else {{ st.textContent = 'Download is not available here. Ask Claude for the file.'; btn.hidden = true; }}
        }});
      }});
    }});
    window.claude.use('comments').then(function (cm) {{
      if (!cm) return;
      Array.prototype.forEach.call(document.querySelectorAll('.cbtn'), function (b) {{
        b.hidden = false;
        b.addEventListener('click', function () {{
          var el = document.getElementById(b.getAttribute('data-comment-for'));
          cm.openComposer({{element: el.querySelector('h2') || el}}).catch(function (err) {{
            if (err && (err.code === 'unavailable' || err.code === 'not_granted')) {{
              Array.prototype.forEach.call(document.querySelectorAll('.cbtn'), function (x) {{ x.hidden = true; }});
            }}
          }});
        }});
      }});
    }});
  }}
  start();
}})();
</script>
"""
open(OUT, "w").write(page)
print(round(len(page) / 1024), "KB")
