"""Kelen V5 teal component library for the app screens (light grey, glass cards, graphite, teal accent, Geist)."""
import json, re

ACC = "@ACC@"                      # becomes {{accent}} in the page
ACC_DEFAULT = "#0D7377"
ACC_OPTIONS = ["#0D7377", "#0B8466", "#12804E", "#0B6BCB", "#2453D6", "#1E3A8A"]
INK, MUTED, SUBTLE = "#0F1114", "#5E6470", "#7A808C"
TINT, SOFT, LINE = "color-mix(in srgb, @ACC@ 12%, #FFFFFF)", "#E6E8EC", "rgba(15,17,20,0.07)"
BORDER, GLASS = "1px solid #FFFFFF", "rgba(255,255,255,0.72)"
POS, POSBG = "#08785C", "#DDF2EA"
WARN, WARNBG = "#8A5A00", "#FFF1D6"
ERR, ERRBG = "#B42318", "#FDE3E1"
NAVFG = "#3A3F49"
SH_CARD = "0 6px 16px rgba(15,17,20,0.05)"
SH_TILE = "0 1px 2px rgba(15,17,20,0.04), 0 12px 30px rgba(15,17,20,0.07)"
SH_BTN = "0 6px 16px rgba(15,17,20,0.07)"
SH_NAV = "0 12px 32px rgba(15,17,20,0.14)"
FONTLINK = "https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&amp;display=swap"
RING = "box-shadow: none"
ACC_INK = "#FFFFFF"   # text on the accent
FIELD_BORDER = "1px solid rgba(15,17,20,0.12)"

ICONS = {
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "send": '<path d="M7 17 17 7M8 7h9v9"/>',
    "receive": '<path d="M17 7 7 17M16 17H7V8"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "receipt": '<path d="M5 3h14v18l-3-2-2 2-2-2-2 2-2-2-3 2z"/><path d="M9 8h6M9 12h6"/>',
    "bell": '<path d="M6 8a6 6 0 1 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
    "home": '<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
    "swap": '<path d="M7 4 3 8l4 4M3 8h14M17 20l4-4-4-4M21 16H7"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>',
    "dots": '<circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/>',
    "chev_r": '<path d="m9 6 6 6-6 6"/>',
    "chev_l": '<path d="m15 6-6 6 6 6"/>',
    "chev_d": '<path d="m6 9 6 6 6-6"/>',
    "copy": '<rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "check": '<path d="M5 12.5 10 17l9-10"/>',
    "x": '<path d="M6 6l12 12M18 6 6 18"/>',
    "upload": '<path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/>',
    "download": '<path d="M12 4v12M7 11l5 5 5-5"/><path d="M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/>',
    "file": '<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5"/>',
    "camera": '<path d="M4 8h3l2-3h6l2 3h3a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/><circle cx="12" cy="13.5" r="3.5"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21v-1a6 6 0 0 1 6-6h4a6 6 0 0 1 6 6v1"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
    "building": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 7h1M14 7h1M9 11h1M14 11h1M9 15h1M14 15h1M10 21v-3h4v3"/>',
    "phone": '<rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    "snow": '<path d="M12 2v20M3.3 7l17.4 10M3.3 17 20.7 7"/><path d="m9.5 3.5 2.5 2 2.5-2M9.5 20.5l2.5-2 2.5 2"/>',
    "sliders": '<path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.8 5.5 3.8 9s-1.3 6.5-3.8 9c-2.5-2.5-3.8-5.5-3.8-9S9.5 5.5 12 3z"/>',
    "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
    "wallet": '<path d="M4 7a2 2 0 0 1 2-2h12v4"/><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M16 13.5h2"/>',
    "book": '<path d="M4 4h6a2 2 0 0 1 2 2v14a2 2 0 0 0-2-2H4z"/><path d="M20 4h-6a2 2 0 0 0-2 2v14a2 2 0 0 1 2-2h6z"/>',
    "trend": '<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>',
    "alert": '<path d="M12 3 2 20h20z"/><path d="M12 10v4M12 17h.01"/>',
    "share": '<circle cx="18" cy="5" r="2.5"/><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="19" r="2.5"/><path d="m8.2 10.8 7.6-4.6M8.2 13.2l7.6 4.6"/>',
    "help": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.6M12 17h.01"/>',
    "logout": '<path d="M15 4h3a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1h-3"/><path d="M10 17l-5-5 5-5M5 12h11"/>',
    "face": '<path d="M4 8V6a2 2 0 0 1 2-2h2M16 4h2a2 2 0 0 1 2 2v2M20 16v2a2 2 0 0 1-2 2h-2M8 20H6a2 2 0 0 1-2-2v-2"/><path d="M9 10v1M15 10v1M12 10v3h-1M9.5 16a3.5 3.5 0 0 0 5 0"/>',
    "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
    "wifi": '<path d="M2 9a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0M12 19.5h.01"/>',
    "tv": '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="m8 2 4 4 4-4M8 21h8"/>',
    "bank": '<path d="M3 10 12 4l9 6"/><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/>',
    "cash": '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 12h.01M18 12h.01"/>',
    "pin": '<path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "percent": '<path d="M19 5 5 19"/><circle cx="7" cy="7" r="2.5"/><circle cx="17" cy="17" r="2.5"/>',
    "tag": '<path d="M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
    "brief": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>',
    "pie": '<path d="M12 3v9h9"/><circle cx="12" cy="12" r="9"/>',
    "msg": '<path d="M4 5h16v11H8l-4 4z"/>',
    "edit": '<path d="M4 20h4L19 9l-4-4L4 16z"/>',
    "refresh": '<path d="M20 11a8 8 0 0 0-14.9-3M4 4v4h4M4 13a8 8 0 0 0 14.9 3M20 20v-4h-4"/>',
    "arrow_r": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "truck": '<path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "back": '<path d="M9 7 4 12l5 5M4 12h11a5 5 0 0 1 5 5"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>',
}


def money(n):
    s = f"{abs(n):,}".replace(",", " ")
    return ("−" if n < 0 else "") + s


def ic(name, size=20, sw="2"):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def circ(name, bg=TINT, fg=INK, size=40, isz=18, ring=False, text=None):
    inner = f'<span style="font-size: {13 if size >= 40 else 12}px; font-weight: 800">{text}</span>' if text else ic(name, isz, "2.2")
    extra = f"; {RING}" if ring else ""
    return (f'<span style="width: {size}px; height: {size}px; border-radius: {size // 2}px; background: {bg}; color: {fg}; '
            f'display: flex; align-items: center; justify-content: center; flex: none{extra}">{inner}</span>')


def wordmark(size=13, sq=8, color=INK):
    return (f'<span style="display: inline-flex; align-items: center; gap: {max(4, size // 3)}px; font-weight: 700; letter-spacing: -0.2px; font-size: {size + 2}px; color: {color}">'
            f'<span style="width: {sq - 1}px; height: {sq - 1}px; border-radius: {sq}px; background: {ACC}"></span>kelen</span>')


def glass_btn_style(size=44):
    return (f"width: {size}px; height: {size}px; border-radius: {size // 2}px; background: {GLASS}; -webkit-backdrop-filter: blur(20px); backdrop-filter: blur(20px); border: {BORDER}; box-shadow: {SH_BTN}; "
            f"display: flex; align-items: center; justify-content: center; color: {INK}; text-decoration: none; box-sizing: border-box; flex: none; position: relative")


def icon_link(name, href, label, dot=False):
    d = f'<span style="position: absolute; top: 10px; right: 11px; width: 8px; height: 8px; border-radius: 4px; background: {ACC}"></span>' if dot else ""
    return f'<a href="{href}" aria-label="{label}" style="{glass_btn_style()}">{ic(name, 20, "2")}{d}</a>'


def icon_button(name, label):
    return f'<button aria-label="{label}" style="all: unset; cursor: pointer; {glass_btn_style()}">{ic(name, 20, "2")}</button>'


def header(back, right="", close=None):
    left = icon_link("chev_l", back, "Retour") if back else '<span style="width: 44px; height: 44px"></span>'
    x = icon_link("x", close, "Fermer") if close else ""
    r = f'<div style="display: flex; align-items: center; gap: 8px">{right}{x}</div>' if (right or x) else ""
    return f'<div style="display: flex; align-items: center; justify-content: space-between">{left}{r}</div>'


def soon_badge():
    return f'<span style="font-size: 11px; font-weight: 600; letter-spacing: 0.6px; text-transform: uppercase; padding: 4px 9px; border-radius: 10px; background: {TINT}; color: {ACC}; flex: none">Bientôt</span>'


def h1(text, sub=None, size=28, badge=False):
    b = soon_badge() if badge else ""
    s = f'<p style="margin: 0; font-size: 15px; line-height: 1.45; color: {MUTED}">{sub}</p>' if sub else ""
    return (f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap">'
            f'<h1 style="margin: 0; font-size: {size}px; font-weight: 600; letter-spacing: -0.8px; line-height: 1.1">{text}</h1>{b}</div>{s}</div>')


def link_style():
    return f"font-size: 14px; font-weight: 600; color: {ACC}; text-decoration: none"


def section(title, link=None, href="#"):
    l = f'<a href="{href}" style="{link_style()}">{link}</a>' if link else ""
    return (f'<div style="display: flex; align-items: center; justify-content: space-between">'
            f'<h2 style="margin: 0; font-size: 17px; font-weight: 600; letter-spacing: -0.2px">{title}</h2>{l}</div>')


def group(title, inner, link=None, href="#"):
    return f'<div style="display: flex; flex-direction: column; gap: 10px">{section(title, link, href) if title else ""}{inner}</div>'


def panel(inner, pad="2px 14px", radius=22, gap=None, extra=""):
    g = f"gap: {gap}px; " if gap is not None else ""
    return (f'<div style="border-radius: {radius}px; padding: {pad}; background: {GLASS}; border: {BORDER}; box-shadow: {SH_CARD}; '
            f'display: flex; flex-direction: column; {g}{extra}">{inner}</div>')


def tile(inner, pad="22px 20px 18px", align="center", radius=28):
    return (f'<div style="border-radius: {radius}px; padding: {pad}; background: {GLASS}; -webkit-backdrop-filter: blur(24px); backdrop-filter: blur(24px); border: {BORDER}; box-shadow: {SH_TILE}; '
            f'display: flex; flex-direction: column; align-items: {align}; gap: 4px">{inner}</div>')


def row(lead, title, sub=None, right="", href=None, last=False, chevron=False, title_w=600, pad="12px 0"):
    sep = "" if last else f"border-bottom: 1px solid {LINE}; "
    s = f'<span style="font-size: 12px; color: {MUTED}">{sub}</span>' if sub else ""
    ch = f'<span style="color: {SUBTLE}; display: flex; flex: none">{ic("chev_r", 18, "1.8")}</span>' if chevron else ""
    body = (f'{lead}<span style="display: flex; flex-direction: column; gap: 2px; flex: 1 1 auto; min-width: 0">'
            f'<span style="font-size: 14px; font-weight: {title_w}">{title}</span>{s}</span>{right}{ch}')
    st = f"display: flex; align-items: center; gap: 12px; padding: {pad}; {sep}"
    if href:
        return f'<a href="{href}" style="{st}color: {INK}; text-decoration: none">{body}</a>'
    return f'<div style="{st}">{body}</div>'


def amt(n, color=INK, w=600, size=14, sign=False):
    t = ("+" if sign and n > 0 else "") + money(n)
    return f'<span style="font-size: {size}px; font-weight: {w}; color: {color}; flex: none; white-space: nowrap">{t}</span>'


def right_text(t, color=MUTED, size=13, w=600):
    return f'<span style="font-size: {size}px; font-weight: {w}; color: {color}; flex: none; text-align: right">{t}</span>'


PILL = {"pos": (POSBG, POS), "warn": (WARNBG, WARN), "err": (ERRBG, ERR), "info": (TINT, ACC), "neutral": (SOFT, NAVFG), "ink": (ACC, "#FFFFFF")}


def pill(text, kind="neutral"):
    bg, fg = PILL[kind]
    return f'<span style="font-size: 12px; font-weight: 600; padding: 5px 10px; border-radius: 12px; background: {bg}; color: {fg}; flex: none; white-space: nowrap">{text}</span>'


def fcfa_tag(size=12):
    return f'<span style="font-size: {size + 1}px; font-weight: 600; letter-spacing: 2px; color: {ACC}">FCFA</span>'


def big_amount(value, size=46, label=None, sign=""):
    l = f'<span style="font-size: 12px; font-weight: 600; letter-spacing: 1.2px; text-transform: uppercase; color: {MUTED}">{label}</span>' if label else ""
    return (f'<div style="display: flex; flex-direction: column; align-items: center; gap: 6px">{l}'
            f'<span style="font-size: {size}px; font-weight: 500; letter-spacing: -2px; line-height: 1.1; font-variant-numeric: proportional-nums">{sign}{value}</span>{fcfa_tag()}</div>')


def field(label, value=None, placeholder=None, prefix=None, icon=None, hint=None, typ="text", mode=None):
    pre = (f'<span style="display: flex; align-items: center; padding: 0 12px; border-right: 1px solid rgba(15,17,20,0.10); font-size: 15px; font-weight: 600; flex: none">{prefix}</span>' if prefix else "")
    icn = f'<span style="display: flex; align-items: center; padding-left: 14px; color: {MUTED}; flex: none">{ic(icon, 18, "2")}</span>' if icon else ""
    val = f' value="{value}"' if value is not None else ""
    ph = f' placeholder="{placeholder}"' if placeholder else ""
    im = f' inputmode="{mode}"' if mode else ""
    h = f'<span style="font-size: 12px; color: {MUTED}">{hint}</span>' if hint else ""
    lab = f'<span style="font-size: 13px; font-weight: 600">{label}</span>' if label else ""
    return (f'<label style="display: flex; flex-direction: column; gap: 6px">{lab}'
            f'<span style="display: flex; align-items: stretch; height: 52px; border-radius: 16px; border: {FIELD_BORDER}; background: #FFFFFF; overflow: hidden">{pre}{icn}'
            f'<input type="{typ}"{val}{ph}{im} style="flex: 1 1 auto; min-width: 0; border: 0; outline: none; background: transparent; padding: 0 14px; font: inherit; font-size: 15px; color: {INK}"></span>{h}</label>')


def chips(items, active=0, wrap=True):
    out = []
    for i, t in enumerate(items):
        on = i == active if isinstance(active, int) else t in active
        st = (f"background: {ACC}; color: {ACC_INK}; border: 1px solid {ACC}" if on else f"background: {GLASS}; border: {BORDER}; box-shadow: 0 4px 12px rgba(15,17,20,0.05)")
        out.append(f'<button aria-pressed="{"true" if on else "false"}" style="all: unset; cursor: pointer; box-sizing: border-box; height: 38px; padding: 0 14px; border-radius: 19px; {st}; '
                   f'font-size: 13px; font-weight: 600; display: flex; align-items: center; white-space: nowrap">{t}</button>')
    w = "flex-wrap: wrap" if wrap else "overflow-x: auto"
    return f'<div style="display: flex; gap: 8px; {w}">{"".join(out)}</div>'


def segmented(items, active=0):
    out = []
    for i, t in enumerate(items):
        on = i == active
        st = (f"background: #FFFFFF; border: {BORDER}; box-shadow: 0 2px 8px rgba(15,17,20,0.08)" if on else f"border: 1px solid transparent; color: {MUTED}")
        out.append(f'<button aria-pressed="{"true" if on else "false"}" style="all: unset; cursor: pointer; box-sizing: border-box; flex: 1 1 0; height: 38px; border-radius: 19px; {st}; '
                   f'font-size: 13px; font-weight: {600 if on else 500}; display: flex; align-items: center; justify-content: center; text-align: center">{t}</button>')
    return f'<div style="display: flex; gap: 4px; padding: 4px; border-radius: 23px; background: {SOFT}">{"".join(out)}</div>'


def toggle(on, label):
    if on:
        track, knob = f"background: {ACC}; border: 1.5px solid {ACC}", "left: 22px"
    else:
        track, knob = "background: #D9DCE1; border: 1.5px solid #D9DCE1", "left: 2px"
    return (f'<button aria-label="{label}" aria-pressed="{"true" if on else "false"}" style="all: unset; cursor: pointer; box-sizing: border-box; width: 48px; height: 28px; border-radius: 14px; {track}; position: relative; flex: none">'
            f'<span style="position: absolute; top: 1px; {knob}; width: 23px; height: 23px; box-sizing: border-box; border-radius: 12px; background: #FFFFFF; box-shadow: 0 2px 6px rgba(15,17,20,0.20)"></span></button>')


def toggle_row(title, sub, on, last=False, lead=""):
    return row(lead, title, sub, toggle(on, title), last=last)


def cta(label, href=None, kind="primary", icon=None):
    if kind == "primary":
        st = f"background: {ACC}; border: 1px solid {ACC}; color: {ACC_INK}"
    elif kind == "dark":
        st = f"background: {INK}; border: 1px solid {INK}; color: #FFFFFF"
    else:
        st = f"background: #FFFFFF; border: {FIELD_BORDER}; color: {INK}"
    i = ic(icon, 18, "1.8") if icon else ""
    base = (f"box-sizing: border-box; height: 56px; border-radius: 28px; {st}; display: flex; align-items: center; justify-content: center; gap: 8px; "
            f"font-size: 16px; font-weight: 600; text-decoration: none; flex: 1 1 auto")
    if href:
        return f'<a href="{href}" style="{base}">{i}{label}</a>'
    return f'<button style="all: unset; cursor: pointer; {base}">{i}{label}</button>'


def small_btn(label, kind="primary", href=None, icon=None):
    st = (f"background: {ACC}; border: 1px solid {ACC}; color: {ACC_INK}" if kind == "primary" else f"background: #FFFFFF; border: {FIELD_BORDER}; color: {INK}")
    i = ic(icon, 16, "1.8") if icon else ""
    base = f"box-sizing: border-box; height: 40px; padding: 0 16px; border-radius: 20px; {st}; display: inline-flex; align-items: center; justify-content: center; gap: 6px; font-size: 14px; font-weight: 600; text-decoration: none; flex: none; white-space: nowrap"
    if href:
        return f'<a href="{href}" style="{base}">{i}{label}</a>'
    return f'<button style="all: unset; cursor: pointer; {base}">{i}{label}</button>'


def bottom(*buttons, note=None):
    n = f'<p style="margin: 0; font-size: 12px; color: {MUTED}; text-align: center">{note}</p>' if note else ""
    return (f'<div style="position: absolute; left: 0; right: 0; bottom: 0; padding: 12px 18px 30px; background: rgba(242,243,245,0.94); -webkit-backdrop-filter: blur(20px); backdrop-filter: blur(20px); border-top: 1px solid {LINE}; '
            f'display: flex; flex-direction: column; gap: 10px">{n}{"".join(buttons)}</div>')


def bottom_height(n_buttons, note=False):
    return 12 + 30 + n_buttons * 56 + (n_buttons - 1) * 10 + (28 if note else 0)


def progress(pct, color=None, h=8):
    c = color or ACC
    return (f'<div style="height: {h}px; border-radius: {h // 2}px; background: #E1E4E8; overflow: hidden">'
            f'<div style="width: {pct}%; height: 100%; border-radius: {h // 2}px; background: {c}"></div></div>')


def stepper(step, total, label):
    bars = "".join(
        f'<span style="flex: 1 1 0; height: 6px; border-radius: 3px; background: {ACC if i < step else "#E1E4E8"}"></span>'
        for i in range(total))
    return (f'<div style="display: flex; flex-direction: column; gap: 8px"><span style="font-size: 11px; font-weight: 500; letter-spacing: 1.8px; text-transform: uppercase; color: {MUTED}">'
            f'Étape {step} sur {total} · {label}</span><div style="display: flex; gap: 6px">{bars}</div></div>')


def note(text, kind="info", icon="info"):
    bg, fg = {"info": (TINT, INK), "warn": (WARNBG, WARN), "pos": (POSBG, POS), "soft": ("rgba(255,255,255,0.72)", INK)}[kind]
    return (f'<div style="display: flex; gap: 10px; align-items: flex-start; padding: 12px 14px; border-radius: 16px; background: {bg}; color: {fg}">'
            f'<span style="display: flex; flex: none; margin-top: 1px">{ic(icon, 18, "1.8")}</span><span style="font-size: 13px; line-height: 1.45; font-weight: 500">{text}</span></div>')


def bank_card(holder, last4, label, dark=True, small=False):
    bg, fg, sub = (INK, "#FFFFFF", "#A9AFBA") if dark else ("#FFFFFF", INK, MUTED)
    border = "" if dark else f"border: {FIELD_BORDER}; "
    pad = 18 if small else 22
    return (f'<div style="position: relative; overflow: hidden; box-sizing: border-box; width: 100%; aspect-ratio: 1.586; border-radius: 22px; background: {bg}; color: {fg}; {border}'
            f'padding: {pad}px; display: flex; flex-direction: column; justify-content: space-between">'
            f'<span style="position: absolute; right: -60px; top: -60px; width: 190px; height: 190px; border-radius: 95px; background: {ACC}; opacity: 0.9"></span>'
            f'<span style="position: absolute; right: 70px; top: 62px; width: 30px; height: 30px; border-radius: 15px; border: 1.5px solid {fg if dark else INK}; box-sizing: border-box; opacity: 0.6"></span>'
            f'<div style="position: relative; display: flex; align-items: center; justify-content: space-between">{wordmark(14, 9, fg)}</div>'
            f'<div style="position: relative; display: flex; align-items: flex-end; justify-content: space-between">'
            f'<span style="display: flex; flex-direction: column; gap: 4px"><span style="font-size: 12px; color: {sub}">{label}</span>'
            f'<span style="font-size: 14px; font-weight: 600">{holder}</span>'
            f'<span style="font-size: 18px; font-weight: 500; letter-spacing: 2px">•••• {last4}</span></span>'
            f'<span style="font-size: 22px; font-weight: 700; font-style: italic; letter-spacing: 0.5px">VISA</span></div></div>')


def keypad():
    keys = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "000", "0", None]
    out = []
    for k in keys:
        if k is None:
            out.append(f'<button aria-label="Effacer" style="all: unset; cursor: pointer; height: 52px; border-radius: 16px; display: flex; align-items: center; justify-content: center">{ic("back", 22, "2")}</button>')
        else:
            out.append(f'<button style="all: unset; cursor: pointer; height: 52px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 500">{k}</button>')
    return f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 4px">{"".join(out)}</div>'


def success(icon, title, amount_html, sub, kind="pos"):
    bg, fg = (POSBG, POS) if kind == "pos" else (TINT, ACC)
    return (f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 14px; padding-top: 70px">'
            f'<span style="width: 88px; height: 88px; border-radius: 44px; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center">{ic(icon, 40, "2")}</span>'
            f'<h1 style="margin: 6px 0 0; font-size: 28px; font-weight: 600; letter-spacing: -0.8px">{title}</h1>{amount_html}'
            f'<p style="margin: 0; font-size: 15px; line-height: 1.5; color: {MUTED}; max-width: 310px">{sub}</p></div>')


def kv(rows):
    """Label / value list inside a panel."""
    out = []
    for i, r in enumerate(rows):
        label, value = r[0], r[1]
        extra = r[2] if len(r) > 2 else ""
        sep = "" if i == len(rows) - 1 else f"border-bottom: 1px solid {LINE}; "
        out.append(f'<div style="display: flex; align-items: center; gap: 12px; padding: 12px 0; {sep}"><span style="font-size: 13px; color: {MUTED}; flex: none; width: 112px">{label}</span>'
                   f'<span style="font-size: 14px; font-weight: 600; flex: 1 1 auto; min-width: 0; text-align: right">{value}</span>{extra}</div>')
    return panel("".join(out))


def copy_btn(label):
    return f'<button aria-label="Copier {label}" style="all: unset; cursor: pointer; width: 32px; height: 32px; border-radius: 16px; background: {SOFT}; display: flex; align-items: center; justify-content: center; flex: none">{ic("copy", 15, "1.8")}</button>'


def nav(active):
    tabs = [("Accueil", "Main.dc.html", "home"), ("Paiements", "Payments.dc.html", "swap"), ("Cartes", "Cards.dc.html", "card"), ("Plus", "More.dc.html", "dots")]
    out = []
    for label, href, icon in tabs:
        if label == active:
            out.append(f'<a href="{href}" aria-current="page" style="flex: 1 1 0; border-radius: 26px; background: {ACC}; color: {ACC_INK}; text-decoration: none; display: flex; flex-direction: column; '
                       f'align-items: center; justify-content: center; gap: 2px; font-size: 11px; font-weight: 600">{ic(icon, 21, "1.8")}{label}</a>')
        else:
            out.append(f'<a href="{href}" style="flex: 1 1 0; color: {NAVFG}; text-decoration: none; display: flex; flex-direction: column; align-items: center; justify-content: center; '
                       f'gap: 2px; font-size: 11px; font-weight: 600">{ic(icon, 21, "1.5")}{label}</a>')
    return (f'<nav aria-label="Navigation principale" style="position: absolute; left: 22px; right: 22px; bottom: 22px; height: 64px; border-radius: 32px; padding: 6px; box-sizing: border-box; '
            f'background: rgba(255,255,255,0.72); -webkit-backdrop-filter: blur(24px) saturate(180%); backdrop-filter: blur(24px) saturate(180%); border: {BORDER}; box-shadow: {SH_NAV}; '
            f'display: flex; align-items: stretch">{"".join(out)}</nav>')


VOID = {"input", "br", "img", "meta", "link", "hr", "path", "circle", "rect"}


def _balanced(s):
    stack = []
    for m in re.finditer(r"<(/?)([a-zA-Z][a-zA-Z0-9-]*)([^>]*?)(/?)>", s):
        close, tag, _, selfclose = m.groups()
        tag = tag.lower()
        if selfclose or (tag in VOID and not close):
            continue
        if close:
            if not stack or stack[-1] != tag:
                return f"unexpected </{tag}> (open: {stack[-3:]})"
            stack.pop()
        else:
            stack.append(tag)
    return None if not stack else f"unclosed {stack[-3:]}"


STROKE = {"3": "2.4", "2.4": "2", "2.3": "1.8", "2.2": "1.8", "2": "1.6"}


def _on_accent(m):
    """Text on an accent background is white."""
    st = m.group(1)
    if re.search(r"(^|;)\s*background:\s*@ACC@\s*(;|$)", st) and "opacity" not in st:
        if re.search(r"(^|;)\s*color:", st):
            st = re.sub(r"((?:^|;)\s*color:\s*)#0F1114", r"\g<1>#FFFFFF", st)
        else:
            st = st.rstrip("; ") + "; color: #FFFFFF"
    return f'style="{st}"'


def kelenize(html):
    """Map the remaining hard-coded Tabax styles of the screen builder onto Kelen V5."""
    h = html
    h = h.replace("#161616", INK).replace("rgba(22,22,22,", "rgba(15,17,20,")
    h = h.replace("font-weight: 800", "font-weight: 600").replace("font-weight: 700", "font-weight: 600")
    h = re.sub(r"font-size: (\d+)px; font-weight: 600; letter-spacing: -(1|1\.5|2)px", r"font-size: \1px; font-weight: 500; letter-spacing: -\2px", h)
    h = re.sub(r'stroke-width="([0-9.]+)"', lambda m: f'stroke-width="{STROKE.get(m.group(1), m.group(1))}"', h)
    h = h.replace(f"1.5px dashed {INK}", "1.5px dashed #B3B9C2")
    h = h.replace(f"border: 1.5px solid {INK}", "border: 1.5px solid @ACC@").replace(f"border: 2px solid {INK}", "border: 2px solid @ACC@")
    h = h.replace("Tabax", "Kelen").replace("TABAX", "KELEN").replace("TBX", "KLN")
    h = re.sub(r'style="([^"]*)"', _on_accent, h)
    return h


def page(title, body, nav_tab=None, bottom_html=None, bottom_h=0):
    pb = 120 if nav_tab else (bottom_h + 24 if bottom_html else 40)
    extra = (nav(nav_tab) if nav_tab else "") + (bottom_html or "")
    props = json.dumps({"accent": {"editor": "color", "default": ACC_DEFAULT, "options": ACC_OPTIONS}, "$preview": {"width": 390, "height": 844}}, separators=(",", ":"))
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
.scroll{{scrollbar-width:none}}.scroll::-webkit-scrollbar{{display:none}}
input::placeholder{{color:#7A808C}}
</style>
</helmet>
<div style="width: 390px; height: 844px; position: relative; overflow: hidden; box-sizing: border-box; background: #F2F3F5; color: #0F1114; font-family: 'Geist', system-ui, sans-serif; font-variant-numeric: tabular-nums; line-height: 1.25; -webkit-font-smoothing: antialiased">
<div class="scroll" style="position: absolute; inset: 0; overflow-y: auto">
<div style="display: flex; flex-direction: column; gap: 18px; padding: 18px 18px {pb}px">
{body}
</div>
</div>
{extra}
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
    html = kelenize(html).replace(ACC, "{{accent}}")
    inner = html.split("<x-dc>")[1].split("</x-dc>")[0]
    err = _balanced(inner)
    assert err is None, f"{title}: {err}"
    return html
