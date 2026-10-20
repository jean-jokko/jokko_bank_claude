"""Kelen V5 teal web app: desktop shell, flow layout, onboarding layout, tables. Builds on kelen_lib (tokens and base components)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kelen_lib import *  # noqa: F401,F403
from kelen_lib import kelenize, _balanced

W = 1440


def p(t, size=14, color=MUTED, w=400):
    return f'<p style="margin: 0; font-size: {size}px; line-height: 1.5; color: {color}; font-weight: {w}">{t}</p>'


def label(t):
    return f'<span style="font-size: 13px; font-weight: 600">{t}</span>'


def stack(*parts, gap=10):
    return f'<div style="display: flex; flex-direction: column; gap: {gap}px; min-width: 0">{"".join(parts)}</div>'


def hrow(*parts, gap=12, align="center", wrap=True, justify="flex-start"):
    return (f'<div style="display: flex; align-items: {align}; justify-content: {justify}; gap: {gap}px; {"flex-wrap: wrap; " if wrap else ""}min-width: 0">'
            f'{"".join(parts)}</div>')


def cols(*parts, gap=24, basis=(560, 320)):
    """Responsive columns: each part grows from its basis and wraps under the previous one when narrow."""
    out = []
    for i, part in enumerate(parts):
        b = basis[i] if i < len(basis) else basis[-1]
        grow = 2 if i == 0 and len(parts) > 1 else 1
        out.append(f'<div style="flex: {grow} 1 {b}px; min-width: 0; display: flex; flex-direction: column; gap: 20px">{part}</div>')
    return f'<div style="display: flex; flex-wrap: wrap; gap: {gap}px; align-items: flex-start">{"".join(out)}</div>'


def autogrid(*items, min_w=240, gap=16):
    return f'<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax({min_w}px, 1fr)); gap: {gap}px">{"".join(items)}</div>'


def av(init, bg=SOFT, size=40):
    fg = "#FFFFFF" if bg == ACC else INK
    return (f'<span style="width: {size}px; height: {size}px; border-radius: {size // 2}px; background: {bg}; color: {fg}; display: flex; align-items: center; '
            f'justify-content: center; flex: none; font-size: {13 if size >= 40 else 12}px; font-weight: 600">{init}</span>')


def btn(label_, href=None, kind="primary", icon=None, size="m"):
    h, fs, padx = {"m": (48, 15, 22), "s": (40, 14, 16)}[size]
    if kind == "primary":
        st = f"background: {ACC}; border: 1px solid {ACC}; color: #FFFFFF"
    elif kind == "danger":
        st = f"background: #FFFFFF; border: {FIELD_BORDER}; color: {ERR}"
    else:
        st = f"background: #FFFFFF; border: {FIELD_BORDER}; color: {INK}"
    i = ic(icon, 18 if size == "m" else 16, "1.8") if icon else ""
    base = (f"box-sizing: border-box; height: {h}px; padding: 0 {padx}px; border-radius: {h // 2}px; {st}; display: inline-flex; align-items: center; justify-content: center; "
            f"gap: 8px; font-size: {fs}px; font-weight: 600; text-decoration: none; white-space: nowrap; flex: none")
    if href:
        return f'<a href="{href}" style="{base}">{i}{label_}</a>'
    return f'<button style="all: unset; cursor: pointer; {base}">{i}{label_}</button>'


def card(inner, pad="20px", gap=14, radius=22, extra=""):
    return (f'<div style="box-sizing: border-box; border-radius: {radius}px; padding: {pad}; background: {GLASS}; -webkit-backdrop-filter: blur(24px); backdrop-filter: blur(24px); '
            f'border: {BORDER}; box-shadow: {SH_CARD}; display: flex; flex-direction: column; gap: {gap}px; min-width: 0; {extra}">{inner}</div>')


def card_title(t, right=""):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 12px">'
            f'<h2 style="margin: 0; font-size: 17px; font-weight: 600; letter-spacing: -0.2px">{t}</h2>{right}</div>')


def tlink(text, href="#"):
    return f'<a href="{href}" style="{link_style()}">{text}</a>'


def eyebrow(t):
    return f'<span style="font-size: 11px; font-weight: 500; letter-spacing: 1.8px; text-transform: uppercase; color: {MUTED}">{t}</span>'


def stat_card(lbl, value, color=INK, sub=None):
    s = f'<span style="font-size: 12px; color: {MUTED}">{sub}</span>' if sub else ""
    return card(f'<span style="font-size: 13px; color: {MUTED}">{lbl}</span><span style="font-size: 26px; font-weight: 500; letter-spacing: -0.8px; color: {color}">{value}</span>{s}',
                pad="18px 20px", gap=6)


def search_field(ph, width=320):
    return (f'<label style="display: flex; align-items: center; gap: 8px; height: 44px; box-sizing: border-box; padding: 0 14px; border-radius: 22px; background: #FFFFFF; '
            f'border: {FIELD_BORDER}; flex: 0 1 auto; width: {width}px; max-width: 100%; color: {MUTED}">{ic("search", 18, "1.8")}'
            f'<input aria-label="{ph}" placeholder="{ph}" style="flex: 1 1 auto; min-width: 0; border: 0; outline: none; background: transparent; font: inherit; font-size: 14px; color: {INK}"></label>')


def date_btn(text):
    return (f'<button style="all: unset; cursor: pointer; box-sizing: border-box; height: 44px; padding: 0 16px; border-radius: 22px; background: #FFFFFF; border: {FIELD_BORDER}; '
            f'display: inline-flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 600">{ic("calendar", 18, "1.8")}{text}{ic("chev_d", 16, "1.8")}</button>')


# ------------------------------------------------------------------ table
def table(heads, rows, aligns=None):
    aligns = aligns or ["left"] * len(heads)
    th = "".join(f'<th scope="col" style="text-align: {a}; padding: 12px 16px; font-size: 12px; font-weight: 500; letter-spacing: 0.6px; text-transform: uppercase; color: {MUTED}; '
                 f'border-bottom: 1px solid {LINE}; white-space: nowrap">{h}</th>' for h, a in zip(heads, aligns))
    body = []
    for k, r in enumerate(rows):
        sep = "" if k == len(rows) - 1 else f"border-bottom: 1px solid {LINE}; "
        tds = "".join(f'<td style="text-align: {a}; padding: 12px 16px; {sep}vertical-align: middle; font-size: 14px">{c}</td>' for c, a in zip(r, aligns))
        body.append(f"<tr>{tds}</tr>")
    return (f'<div style="overflow-x: auto; border-radius: 22px; background: {GLASS}; border: {BORDER}; box-shadow: {SH_CARD}">'
            f'<table style="width: 100%; border-collapse: collapse; min-width: 640px"><thead><tr>{th}</tr></thead><tbody>{"".join(body)}</tbody></table></div>')


def cell_main(lead, title, sub=None, href=None):
    s = f'<span style="font-size: 12px; color: {MUTED}">{sub}</span>' if sub else ""
    t = (f'<a href="{href}" style="font-size: 14px; font-weight: 600; color: {INK}; text-decoration: none">{title}</a>' if href
         else f'<span style="font-size: 14px; font-weight: 600">{title}</span>')
    return f'<div style="display: flex; align-items: center; gap: 12px; min-width: 0">{lead}<span style="display: flex; flex-direction: column; gap: 2px; min-width: 0">{t}{s}</span></div>'


def money_cell(n, sign=True, color=None):
    c = color or (POS if n > 0 and sign else INK)
    return f'<span style="font-size: 14px; font-weight: 600; color: {c}; white-space: nowrap">{("+" if sign and n > 0 else "") + money(n)}</span>'


def muted(t):
    return f'<span style="font-size: 13px; color: {MUTED}">{t}</span>'


# ------------------------------------------------------------------ desktop shell (side menu + content)
NAV = [
    ("", [("Accueil", "Main", "home"), ("Paiements", "Payments", "swap"), ("Cartes", "Cards", "card"), ("Comptes", "Accounts", "bank")]),
    ("Opérations", [("Envoyer", "Send", "send"), ("Recharger", "TopUp", "plus"), ("Paie groupée", "Bulk", "users"), ("Factures", "Bills", "receipt")]),
    ("Entreprise", [("Équipe et droits", "Team", "users"), ("Validations", "Approvals", "shield"), ("Relevés", "Statements", "file"), ("Offre", "Plan", "wallet")]),
    ("Bientôt", [("International", "Intl", "globe"), ("Liens de paiement", "PayLinks", "link"), ("Cartes budget", "BudgetCards", "tag"),
                 ("Comptabilité", "Accounting", "book"), ("Financement", "Financing", "trend")]),
]


def nav_item(label_, target, icon, active, badge=None):
    b = (f'<span style="margin-left: auto; min-width: 20px; height: 20px; padding: 0 6px; box-sizing: border-box; border-radius: 10px; background: {WARNBG}; color: {WARN}; '
         f'font-size: 11px; font-weight: 600; display: inline-flex; align-items: center; justify-content: center">{badge}</span>') if badge else ""
    if active:
        st = f"background: {ACC}; color: #FFFFFF"
    else:
        st = f"color: {NAVFG}"
    cur = ' aria-current="page"' if active else ""
    return (f'<a href="{target}.dc.html"{cur} style="display: flex; align-items: center; gap: 10px; height: 40px; padding: 0 12px; border-radius: 14px; '
            f'{st}; text-decoration: none; font-size: 14px; font-weight: {600 if active else 500}">{ic(icon, 18, "1.8" if active else "1.5")}{label_}{b}</a>')


def sidebar(active):
    groups = []
    for title, items in NAV:
        h = (f'<span style="padding: 0 12px; font-size: 11px; font-weight: 500; letter-spacing: 1.6px; text-transform: uppercase; color: {SUBTLE}">{title}</span>' if title else "")
        its = "".join(nav_item(l, t, i, t == active, "2" if t == "Approvals" else None) for l, t, i in items)
        groups.append(f'<div style="display: flex; flex-direction: column; gap: 2px">{h}{its}</div>')
    company = (f'<a href="Settings.dc.html" style="display: flex; align-items: center; gap: 10px; padding: 10px; border-radius: 16px; background: {GLASS}; border: {BORDER}; '
               f'box-shadow: {SH_CARD}; text-decoration: none; color: {INK}">{av("AN", ACC, 36)}<span style="display: flex; flex-direction: column; gap: 1px; min-width: 0">'
               f'<span style="font-size: 14px; font-weight: 600">Atelier Ndiaye SARL</span><span style="font-size: 12px; color: {MUTED}">Premier mois offert · 5 nov.</span></span></a>')
    bottom_ = (f'<div style="display: flex; flex-direction: column; gap: 2px; margin-top: auto; padding-top: 12px; border-top: 1px solid {LINE}">'
               + nav_item("Paramètres", "Settings", "gear", active == "Settings")
               + f'<button style="all: unset; cursor: pointer; display: flex; align-items: center; gap: 10px; height: 40px; padding: 0 12px; border-radius: 14px; color: {NAVFG}; font-size: 14px; font-weight: 500">{ic("help", 18, "1.5")}Aide et contact</button>'
               + f'<a href="Welcome.dc.html" style="display: flex; align-items: center; gap: 10px; height: 40px; padding: 0 12px; border-radius: 14px; color: {ERR}; text-decoration: none; font-size: 14px; font-weight: 500">{ic("logout", 18, "1.5")}Se déconnecter</a></div>')
    return (f'<nav aria-label="Menu principal" style="flex: 1 1 248px; box-sizing: border-box; padding: 22px 14px; display: flex; flex-direction: column; gap: 20px; '
            f'background: rgba(255,255,255,0.45); border-right: 1px solid {LINE}">'
            f'<a href="Main.dc.html" style="padding: 4px 12px; text-decoration: none">{wordmark(18, 10)}</a>{company}{"".join(groups)}{bottom_}</nav>')


def topbar(title, sub=None, right=None, back=None):
    s = f'<p style="margin: 0; font-size: 14px; color: {MUTED}">{sub}</p>' if sub else ""
    bk = (f'<a href="{back}" style="display: inline-flex; align-items: center; gap: 4px; font-size: 13px; font-weight: 600; color: {MUTED}; text-decoration: none">'
          f'{ic("chev_l", 16, "1.8")}Retour</a>') if back else ""
    r = right if right is not None else default_actions()
    return (f'<div style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 16px">'
            f'<div style="display: flex; flex-direction: column; gap: 6px; min-width: 0">{bk}<h1 style="margin: 0; font-size: 30px; font-weight: 600; letter-spacing: -0.8px">{title}</h1>{s}</div>'
            f'<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 10px">{r}</div></div>')


def bell():
    return icon_link("bell", "Notifications.dc.html", "Notifications", dot=True)


def default_actions():
    return search_field("Rechercher une opération, un bénéficiaire", 300) + bell() + btn("Recharger", "TopUp.dc.html", "primary", "plus", "s") + btn("Envoyer", "Send.dc.html", "secondary", "send", "s")


def shell(active, title, content, sub=None, right=None, back=None):
    return (f'<div style="display: flex; flex-wrap: wrap; min-height: 100vh">{sidebar(active)}'
            f'<main style="flex: 999 1 560px; min-width: 0; box-sizing: border-box; padding: 30px 36px 56px">'
            f'<div style="max-width: 1180px; margin: 0 auto; display: flex; flex-direction: column; gap: 24px">{topbar(title, sub, right, back)}{content}</div></main></div>')


# ------------------------------------------------------------------ flow layout (focused task, no side menu)
def flow(title, body, actions="", close="Main.dc.html", back=None, width=640, step=None, aside=None):
    st = f'<span style="font-size: 13px; color: {MUTED}">{step}</span>' if step else ""
    bk = (f'<a href="{back}" style="display: inline-flex; align-items: center; gap: 4px; font-size: 13px; font-weight: 600; color: {MUTED}; text-decoration: none">'
          f'{ic("chev_l", 16, "1.8")}Retour</a>') if back else ""
    top = (f'<header style="display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: 16px 28px; border-bottom: 1px solid {LINE}; '
           f'background: rgba(255,255,255,0.55)"><div style="display: flex; align-items: center; gap: 14px; min-width: 0">'
           f'<a href="Main.dc.html" style="text-decoration: none">{wordmark(16, 9)}</a><span style="width: 1px; height: 20px; background: rgba(15,17,20,0.12)"></span>'
           f'<span style="font-size: 15px; font-weight: 600">{title}</span>{st}</div>{icon_link("x", close, "Fermer")}</header>')
    acts = f'<div style="display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 12px; padding-top: 8px">{actions}</div>' if actions else ""
    main_col = f'<div style="flex: 2 1 420px; min-width: 0; display: flex; flex-direction: column; gap: 20px">{bk}{body}{acts}</div>'
    side = f'<aside style="flex: 1 1 280px; min-width: 0; display: flex; flex-direction: column; gap: 16px">{aside}</aside>' if aside else ""
    mw = width if not aside else width + 360
    return (f'<div style="min-height: 100vh; display: flex; flex-direction: column">{top}'
            f'<main style="flex: 1 1 auto; box-sizing: border-box; padding: 36px 24px 64px"><div style="max-width: {mw}px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 28px; align-items: flex-start">'
            f'{main_col}{side}</div></main></div>')


def flow_h1(t, sub=None, size=30, badge=False):
    return h1(t, sub, size=size, badge=badge)


# ------------------------------------------------------------------ onboarding layout (brand panel + form)
ONB_STEPS = ["Entreprise", "Documents", "Dirigeant", "Actionnaires"]


def onboarding(body, actions="", step=None, close="Welcome.dc.html", back=None, aside_title=None, aside_text=None):
    steps_html = ""
    if step is not None:
        items = []
        for i, s in enumerate(ONB_STEPS):
            done, cur = i < step - 1, i == step - 1
            dotbg = ACC if (done or cur) else "rgba(255,255,255,0.12)"
            mark = ic("check", 14, "2.4") if done else f'<span style="font-size: 12px; font-weight: 600">{i + 1}</span>'
            items.append(f'<div style="display: flex; align-items: center; gap: 12px; color: {"#FFFFFF" if (done or cur) else "#A9AFBA"}">'
                         f'<span style="width: 28px; height: 28px; border-radius: 14px; background: {dotbg}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; flex: none">{mark}</span>'
                         f'<span style="font-size: 15px; font-weight: {600 if cur else 500}">{s}</span></div>')
        steps_html = f'<div style="display: flex; flex-direction: column; gap: 16px">{"".join(items)}</div>'
    at = aside_title or "Le compte pro qui construit avec vous."
    ax = aside_text or "IBAN, cartes Visa, paie des salariés et paiements par banque, Wave ou Orange Money."
    aside = (f'<aside style="flex: 1 1 380px; box-sizing: border-box; padding: 36px 40px; background: {INK}; color: #FFFFFF; display: flex; flex-direction: column; gap: 36px; '
             f'position: relative; overflow: hidden; min-height: 320px">'
             f'<span aria-hidden="true" style="position: absolute; right: -120px; bottom: -120px; width: 360px; height: 360px; border-radius: 180px; background: {ACC}; opacity: 0.9"></span>'
             f'<span aria-hidden="true" style="position: absolute; right: 150px; bottom: 150px; width: 44px; height: 44px; border-radius: 22px; border: 1.5px solid rgba(255,255,255,0.5)"></span>'
             f'<a href="Welcome.dc.html" style="position: relative; text-decoration: none">{wordmark(20, 11, "#FFFFFF")}</a>'
             f'<div style="position: relative; display: flex; flex-direction: column; gap: 12px; max-width: 360px"><h2 style="margin: 0; font-size: 30px; font-weight: 600; letter-spacing: -0.8px; line-height: 1.15">{at}</h2>'
             f'<p style="margin: 0; font-size: 15px; line-height: 1.5; color: #C9CED6">{ax}</p></div>'
             f'<div style="position: relative">{steps_html}</div></aside>')
    bk = (f'<a href="{back}" style="display: inline-flex; align-items: center; gap: 4px; font-size: 13px; font-weight: 600; color: {MUTED}; text-decoration: none">'
          f'{ic("chev_l", 16, "1.8")}Retour</a>') if back else '<span></span>'
    x = icon_link("x", close, "Fermer") if close else ""
    acts = f'<div style="display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 12px; padding-top: 8px">{actions}</div>' if actions else ""
    form = (f'<main style="flex: 999 1 520px; min-width: 0; box-sizing: border-box; padding: 28px 40px 56px; display: flex; flex-direction: column; gap: 24px">'
            f'<div style="display: flex; align-items: center; justify-content: space-between">{bk}{x}</div>'
            f'<div style="max-width: 560px; width: 100%; margin: 0 auto; display: flex; flex-direction: column; gap: 20px">{body}{acts}</div></main>')
    return f'<div style="display: flex; flex-wrap: wrap; min-height: 100vh">{aside}{form}</div>'


# ------------------------------------------------------------------ page file
def web_page(title, body, h=900):
    props = json.dumps({"accent": {"editor": "color", "default": ACC_DEFAULT, "options": ACC_OPTIONS}, "$preview": {"width": W, "height": h}}, separators=(",", ":"))
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="stylesheet" href="{FONTLINK}">
<style>
body{{margin:0}}
a{{color:#0F1114}}a:hover{{color:{ACC_DEFAULT}}}
input::placeholder{{color:#7A808C}}
</style>
</helmet>
<div style="min-height: 100vh; box-sizing: border-box; background: #F2F3F5; color: #0F1114; font-family: 'Geist', system-ui, sans-serif; font-variant-numeric: tabular-nums; line-height: 1.3; -webkit-font-smoothing: antialiased">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{props}'>
class Component extends DCLogic {{
renderVals() {{
return {{ accent: this.props.accent ?? '{ACC_DEFAULT}' }};
}}
}}
</script>
</body>
</html>
"""
    html = kelenize(html).replace(ACC, "{{accent}}").replace("flex: none; width: 112px", "flex: none; width: 210px")
    inner = html.split("<x-dc>")[1].split("</x-dc>")[0]
    err = _balanced(inner)
    assert err is None, f"{title}: {err}"
    return html
