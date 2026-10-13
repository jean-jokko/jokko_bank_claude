"""All Kelen app screens (Kelen V5 teal style) as linked artboards: same screens, flows and links as the Tabax app."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kelen_lib import *

S = {}       # file -> html
TITLES = {}  # file -> board title


def add(file, title, body, nav_tab=None, btns=None, note_txt=None):
    if btns:
        b, h = bottom(*btns, note=note_txt), bottom_height(len(btns), bool(note_txt))
    else:
        b, h = None, 0
    S[file] = page(f"Tabax — {title}", body, nav_tab, b, h)
    TITLES[file] = title


def av(init, bg=SOFT, size=40, ring=False):
    return circ("user", bg, INK, size, text=init, ring=ring)


def label(t):
    return f'<span style="font-size: 13px; font-weight: 700">{t}</span>'


def day(t, inner):
    return (f'<div style="display: flex; flex-direction: column; gap: 8px"><span style="font-size: 12px; font-weight: 700; letter-spacing: 1.2px; '
            f'text-transform: uppercase; color: {MUTED}">{t}</span>{inner}</div>')


def stack(*parts, gap=10):
    return f'<div style="display: flex; flex-direction: column; gap: {gap}px">{"".join(parts)}</div>'


def dot(color):
    return f'<span style="width: 10px; height: 10px; border-radius: 5px; background: {color}; {RING}; flex: none; margin: 0 15px"></span>'


def acct_from(name="Depuis : compte principal", sub="8 210 000 FCFA disponibles", color=INK, last=True):
    return row(dot(color), name, sub, chevron=True, last=last)


def action(label_, href, icon, primary=False):
    cst = (f"background: {ACC}; border: 1.5px solid {INK}" if primary else f"background: {GLASS}; border: {BORDER}; box-shadow: {SH_BTN}")
    inner = (f'<span style="width: 56px; height: 56px; box-sizing: border-box; border-radius: 28px; {cst}; display: flex; align-items: center; justify-content: center">'
             f'{ic(icon, 20, "2.3" if primary else "2")}</span><span style="font-size: 12px; font-weight: 700; text-align: center">{label_}</span>')
    base = "display: flex; flex-direction: column; align-items: center; gap: 8px; text-decoration: none; color: #161616"
    if href:
        return f'<a href="{href}" style="{base}">{inner}</a>'
    return f'<button style="all: unset; cursor: pointer; {base}">{inner}</button>'


def actions(*items):
    return f'<div style="display: grid; grid-template-columns: repeat({len(items)}, minmax(0, 1fr)); gap: 6px">{"".join(items)}</div>'


def option(title, sub, icon, selected=False, extra="", href=None):
    st = f"border: 1.5px solid {INK}; background: #FFFFFF" if selected else f"border: {BORDER}; background: {GLASS}"
    radio = (f'<span style="width: 22px; height: 22px; border-radius: 11px; box-sizing: border-box; border: 1.5px solid {ACC if selected else "#C5C9D0"}; background: {ACC if selected else "#FFFFFF"}; '
             f'display: flex; align-items: center; justify-content: center; flex: none">{ic("check", 12, "3") if selected else ""}</span>')
    inner = (f'{circ(icon, TINT if selected else SOFT)}'
             f'<span style="display: flex; flex-direction: column; gap: 2px; flex: 1 1 auto; min-width: 0"><span style="font-size: 15px; font-weight: 800">{title}</span>'
             f'<span style="font-size: 12px; line-height: 1.4; color: {MUTED}">{sub}</span></span>{extra}{radio}')
    base = f"box-sizing: border-box; border-radius: 20px; padding: 14px; {st}; display: flex; align-items: center; gap: 12px"
    if href:
        return f'<a href="{href}" style="{base}; color: {INK}; text-decoration: none">{inner}</a>'
    return f'<button aria-pressed="{"true" if selected else "false"}" style="all: unset; cursor: pointer; {base}">{inner}</button>'


def steps(items):
    out = []
    for i, (t, s) in enumerate(items):
        num = (f'<span style="width: 32px; height: 32px; border-radius: 16px; background: {ACC}; {RING}; display: flex; align-items: center; justify-content: center; '
               f'font-size: 14px; font-weight: 800; flex: none">{i + 1}</span>')
        out.append(row(num, t, s, last=i == len(items) - 1))
    return panel("".join(out))


def tab_title(t, right=""):
    return (f'<div style="display: flex; align-items: center; justify-content: space-between; min-height: 44px">'
            f'<h1 style="margin: 0; font-size: 30px; font-weight: 800; letter-spacing: -0.8px">{t}</h1>{right}</div>')


def stat(lbl, value, color=INK, sub=None):
    s = f'<span style="font-size: 12px; color: {MUTED}">{sub}</span>' if sub else ""
    return panel(f'<span style="font-size: 12px; color: {MUTED}">{lbl}</span><span style="font-size: 20px; font-weight: 800; color: {color}; letter-spacing: -0.5px">{value}</span>{s}',
                 pad="14px", radius=20, gap=4)


def grid(n, *items, gap=8):
    return f'<div style="display: grid; grid-template-columns: repeat({n}, minmax(0, 1fr)); gap: {gap}px">{"".join(items)}</div>'


def stacked_right(*parts):
    return f'<span style="display: flex; flex-direction: column; align-items: flex-end; gap: 4px; flex: none">{"".join(parts)}</span>'


def center(*parts, gap=10, pt=0):
    return f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: {gap}px; padding-top: {pt}px">{"".join(parts)}</div>'


def soon_btn():
    return cta("Me prévenir au lancement", icon="bell")


def p(t, size=14, color=MUTED, w=400):
    return f'<p style="margin: 0; font-size: {size}px; line-height: 1.45; color: {color}; font-weight: {w}">{t}</p>'


def date_filter(text, export=True):
    btn = (f'<button style="all: unset; cursor: pointer; box-sizing: border-box; flex: 1 1 auto; height: 44px; padding: 0 14px; border-radius: 22px; border: {BORDER}; '
           f'background: #FFFFFF; display: flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700">{ic("calendar", 18, "2")}'
           f'<span style="flex: 1 1 auto">{text}</span>{ic("chev_d", 16, "2.2")}</button>')
    exp = icon_button("download", "Exporter") if export else ""
    return f'<div style="display: flex; gap: 8px; align-items: center">{btn}{exp}</div>'


# ------------------------------------------------------------------ Home and tabs
def acct_chip(name, color, amount, href):
    return (f'<a href="{href}" style="flex: 1 1 0; min-width: 0; border-radius: 18px; padding: 12px; background: {GLASS}; border: {BORDER}; box-shadow: {SH_CARD}; '
            f'display: flex; flex-direction: column; gap: 4px; text-decoration: none; color: {INK}">'
            f'<span style="display: flex; align-items: center; gap: 6px; font-size: 12px; color: {MUTED}"><span style="width: 8px; height: 8px; border-radius: 4px; background: {color}; {RING}"></span>{name}</span>'
            f'<span style="font-size: 15px; font-weight: 700">{amount}</span></a>')


home_header = (
    f'<div style="display: flex; align-items: center; justify-content: space-between">'
    f'<a href="Settings.dc.html" style="display: flex; align-items: center; gap: 10px; text-decoration: none; color: {INK}">'
    f'<span style="width: 44px; height: 44px; border-radius: 22px; background: {ACC}; color: {INK}; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; {RING}">AN</span>'
    f'<span style="display: flex; flex-direction: column; gap: 1px"><span style="font-size: 15px; font-weight: 700">Atelier Ndiaye SARL</span>'
    f'<span style="font-size: 12px; color: {MUTED}; display: flex; align-items: baseline; gap: 5px">{wordmark(12, 8)} Business · Dakar</span></span></a>'
    f'{icon_link("bell", "Notifications.dc.html", "Notifications", dot=True)}</div>')

home_tile = tile(
    f'<span style="font-size: 12px; font-weight: 600; letter-spacing: 1.2px; text-transform: uppercase; color: {MUTED}">Solde total · 3 comptes</span>'
    f'<span style="font-size: 46px; font-weight: 800; letter-spacing: -2px; line-height: 1.1; font-variant-numeric: proportional-nums">12 480 350</span>{fcfa_tag()}'
    f'<a href="AccountDetails.dc.html" style="margin-top: 10px; height: 34px; padding: 0 14px; border-radius: 17px; background: {TINT}; color: {INK}; font-size: 12px; font-weight: 700; '
    f'display: flex; align-items: center; gap: 8px; text-decoration: none">IBAN SN08 SN01 •••• 3035 {ic("copy", 14, "2.3")}</a>')

add("Main.dc.html", "Accueil", "".join([
    home_header, home_tile,
    actions(action("Recharger", "TopUp.dc.html", "plus", True), action("Envoyer", "Send.dc.html", "send"),
            action("Paie groupée", "Bulk.dc.html", "users"), action("Factures", "Bills.dc.html", "receipt")),
    group("Comptes",
          f'<div style="display: flex; gap: 8px">{acct_chip("Principal", INK, "8 210 000", "AccountDetails.dc.html")}'
          f'{acct_chip("Salaires", ACC, "3 500 000", "Accounts.dc.html")}{acct_chip("Fournisseurs", "#BDBDBD", "770 350", "Accounts.dc.html")}</div>'
          + panel(row(circ("calendar", TINT), "Paie d'octobre · 31 oct.", "24 salariés · 3 465 000 FCFA · prête", href="BulkReview.dc.html", chevron=True, last=True), pad="0 14px"),
          "Tout voir", "Accounts.dc.html"),
    group("Activité", panel(
        row(circ("receive", POSBG, POS, 36, 16), "Recharge Wave", "Aujourd'hui · 09:14", amt(500000, POS, sign=True), href="TxDetail.dc.html")
        + row(circ("bolt", TINT, INK, 36, 16), "Facture Senelec", "Aujourd'hui · 08:02", amt(-84300), href="TxDetail.dc.html", last=True)),
        "Tout voir", "Payments.dc.html"),
]), nav_tab="Accueil")


def tx(icon, bg, fg, title, sub, n, href="TxDetail.dc.html", last=False):
    return row(circ(icon, bg, fg, 36, 16), title, sub, amt(n, POS if n > 0 else INK, sign=True), href=href, last=last)


add("Payments.dc.html", "Paiements", "".join([
    tab_title("Paiements", icon_button("search", "Rechercher")),
    date_filter("Du 1er au 12 octobre 2026"),
    grid(2, stat("Entrées · octobre", "+4 870 000", POS), stat("Sorties · octobre", "−3 912 400")),
    chips(["Tout", "Entrées", "Sorties", "Cartes", "Paie", "Factures"], 0, wrap=False),
    day("Aujourd'hui", panel(tx("receive", POSBG, POS, "Recharge Wave", "09:14 · compte principal", 500000)
                             + tx("bolt", TINT, INK, "Facture Senelec", "08:02 · compte principal", -84300, last=True))),
    day("Hier", panel(tx("receive", POSBG, POS, "Virement reçu", "SCI Fann Résidence · facture F-2026-127", 2400000)
                      + tx("card", SOFT, INK, "Google Ads", "Carte •••• 9012 · payé en USD", -51712)
                      + tx("send", SOFT, INK, "Imprimerie Ba", "Virement · flyers salon", -145000, last=True))),
    day("10 octobre", panel(tx("send", SOFT, INK, "Cissé Logistique SARL", "Virement · facture F-2026-118", -1250000)
                            + tx("card", SOFT, INK, "Station Mermoz", "Carte •••• 5528 · carburant", -35000, last=True))),
]), nav_tab="Paiements")

add("TxDetail.dc.html", "Détail d'une opération", "".join([
    header("Payments.dc.html", icon_button("share", "Partager"), close="Payments.dc.html"),
    center(circ("bolt", TINT, INK, 64, 28), f'<span style="font-size: 18px; font-weight: 800">Facture Senelec</span>',
           f'<span style="font-size: 40px; font-weight: 800; letter-spacing: -1.5px; font-variant-numeric: proportional-nums">−84 300</span>{fcfa_tag()}', pill("Payée", "pos"), gap=8),
    kv([("Date", "Aujourd'hui, 08:02"), ("Depuis", "Compte principal"), ("Contrat", "2310 4471 902"), ("Référence", "TBX-FAC-77310"), ("Payée par", "Aïssatou Ndiaye")]),
    group("Catégorie", chips(["Énergie", "Loyer et charges", "Autre"], 0)),
    group("Justificatif", panel(row(circ("file", POSBG, POS), "Reçu Senelec", "Ajouté automatiquement · PDF",
                                    f'<button aria-label="Télécharger le reçu" style="all: unset; cursor: pointer; width: 36px; height: 36px; border-radius: 18px; background: {TINT}; display: flex; align-items: center; justify-content: center; flex: none">{ic("download", 16)}</button>',
                                    last=True))),
    field("Note", placeholder="Ajouter une note pour votre comptable"),
    f'<div style="display: flex">{cta("Télécharger le reçu", kind="secondary", icon="download")}</div>',
]))

add("Cards.dc.html", "Cartes", "".join([
    tab_title("Cartes", icon_link("plus", "NewCard.dc.html", "Nouvelle carte")),
    segmented(["Toutes · 5", "Physiques · 2", "Virtuelles · 3"], 0),
    f'<div class="scroll" style="display: flex; gap: 12px; overflow-x: auto; scroll-snap-type: x mandatory; margin: 0 -18px; padding: 2px 18px; scroll-padding: 0 18px">'
    + "".join(f'<a href="CardDetail.dc.html" style="flex: none; width: 300px; scroll-snap-align: start; display: block; text-decoration: none; color: inherit">{bank_card(h, n, l, d)}</a>'
              for h, n, l, d in [("Aïssatou Ndiaye", "4821", "Carte physique", True), ("Moussa Diop", "9012", "Virtuelle · Publicité en ligne", False),
                                 ("Aïssatou Ndiaye", "3370", "Virtuelle · Logiciels", False), ("Fatou Sarr", "6614", "Virtuelle · Fournitures", False),
                                 ("Ibrahima Fall", "5528", "Physique · gelée", True)]) + '</div>',
    f'<div style="display: flex; justify-content: center; gap: 6px" aria-hidden="true"><span style="width: 18px; height: 6px; border-radius: 3px; background: {ACC}; {RING}"></span>'
    + "".join('<span style="width: 6px; height: 6px; border-radius: 3px; background: #CFCFCB"></span>' for _ in range(4)) + '</div>',
    actions(action("Geler", None, "snow"), action("Infos", None, "eye"), action("Code PIN", None, "lock"), action("Plafonds", None, "sliders")),
    panel(f'<span style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px"><span style="font-size: 13px; color: {MUTED}">Dépensé en octobre</span>'
          f'<span style="font-size: 14px; font-weight: 800">412 300 <span style="color: {MUTED}; font-weight: 600">/ 1 500 000 FCFA</span></span></span>{progress(27)}'
          f'<span style="font-size: 12px; color: {MUTED}">Plafond mensuel · remis à zéro le 1er novembre</span>', pad="14px 16px", gap=10),
    group("Toutes les cartes · 5", panel(
        row(circ("card", TINT), "Carte principale", "Physique •••• 4821 · Aïssatou Ndiaye", right_text("412 300<br>/ 1 500 000", INK, 12, 700), href="CardDetail.dc.html")
        + row(circ("card", TINT), "Publicité en ligne", "Virtuelle •••• 9012 · Moussa Diop", right_text("184 500<br>/ 300 000", INK, 12, 700), href="CardDetail.dc.html")
        + row(circ("card", TINT), "Logiciels", "Virtuelle •••• 3370 · Aïssatou Ndiaye", right_text("62 000<br>/ 150 000", INK, 12, 700), href="CardDetail.dc.html")
        + row(circ("card", SOFT), "Fournitures", "Virtuelle •••• 6614 · Fatou Sarr", right_text("0<br>/ 250 000", INK, 12, 700), href="CardDetail.dc.html")
        + row(circ("snow", SOFT), "Carburant atelier", "Physique •••• 5528 · Ibrahima Fall", pill("Gelée"), href="CardDetail.dc.html", last=True))),
    panel(row(circ("tag", SOFT), "Cartes budget pour vos salariés", "Transport, carburant, repas", soon_badge(), href="BudgetCards.dc.html", last=True)),
]), nav_tab="Cartes")

add("CardDetail.dc.html", "Détail d'une carte", "".join([
    header("Cards.dc.html", icon_button("dots", "Plus d'options"), close="Cards.dc.html"),
    bank_card("Aïssatou Ndiaye", "4821", "Carte physique"),
    actions(action("Geler", None, "snow"), action("Infos", None, "eye"), action("Code PIN", None, "lock"), action("Plafonds", None, "sliders")),
    panel(f'<span style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px"><span style="font-size: 13px; color: {MUTED}">Plafond mensuel</span>'
          f'<span style="font-size: 14px; font-weight: 800">412 300 <span style="color: {MUTED}; font-weight: 600">/ 1 500 000 FCFA</span></span></span>{progress(27)}'
          f'<span style="font-size: 12px; color: {MUTED}">Paiements en FCFA gratuits · autres devises : 1 %</span>', pad="14px 16px", gap=10),
    group("Réglages", panel(toggle_row("Paiements en ligne", "Sites et applications", True) + toggle_row("Sans contact", "Paiements en magasin", True)
                            + toggle_row("Retraits au distributeur", "Désactivés pour cette carte", False) + toggle_row("Paiements hors UEMOA", "1 % de frais hors FCFA", True, last=True))),
    group("Dernières dépenses", panel(
        tx("card", SOFT, INK, "Google Ads", "Payé en USD · dont 512 FCFA de frais (1 %)", -51712)
        + tx("card", SOFT, INK, "Quincaillerie Médina", "Fournitures · 9 oct.", -78500)
        + tx("card", SOFT, INK, "Station Mermoz", "Carburant · 8 oct.", -35000, last=True))),
]))

add("NewCard.dc.html", "Nouvelle carte", "".join([
    header("Cards.dc.html", close="Cards.dc.html"), h1("Nouvelle carte"),
    stack(option("Carte virtuelle", "Gratuite et illimitée, prête tout de suite", "card", True),
          option("Carte physique", "5 000 FCFA une fois, livrée à l'entreprise. La première est offerte au gérant.", "truck")),
    field("Nom de la carte", "Fournitures bureau"),
    panel(row(av("FS", "#FDE3DB", 36), "Titulaire", "Fatou Sarr · assistante", chevron=True)
          + acct_from("Compte", "Principal")),
    stack(label("Plafond mensuel"), chips(["100 000", "250 000", "500 000", "Autre"], 1), gap=8),
    panel(toggle_row("Paiements en ligne uniquement", "Ni sans contact, ni retrait", True, last=True)),
]), btns=[cta("Créer la carte", "CardDetail.dc.html")])

add("More.dc.html", "Plus", "".join([
    tab_title("Plus"),
    panel(row(av("AN", ACC, 48, True), "Atelier Ndiaye SARL", "Essai gratuit jusqu'au 12 janvier 2027", href="Settings.dc.html", chevron=True, last=True)),
    group("Entreprise", panel(
        row(circ("bank", SOFT), "Comptes et RIB", "3 comptes", href="Accounts.dc.html", chevron=True)
        + row(circ("users", SOFT), "Équipe et droits", "5 membres", href="Team.dc.html", chevron=True)
        + row(circ("shield", SOFT), "Validations", "Opérations à approuver", pill("2", "warn"), href="Approvals.dc.html", chevron=True)
        + row(circ("wallet", SOFT), "Offre et abonnement", "Essai gratuit · à choisir avant le 12 janvier", pill("À choisir", "warn"), href="Plan.dc.html", chevron=True)
        + row(circ("file", SOFT), "Relevés et attestations", "RIB, relevés, attestations", href="Statements.dc.html", chevron=True, last=True))),
    group("Bientôt", panel(
        row(circ("globe", TINT), "Virements internationaux", "EUR, USD, CNY…", soon_badge(), href="Intl.dc.html")
        + row(circ("link", TINT), "Liens de paiement", "Wave, Orange Money, carte", soon_badge(), href="PayLinks.dc.html")
        + row(circ("tag", TINT), "Cartes budget salariés", "Transport, carburant, repas", soon_badge(), href="BudgetCards.dc.html")
        + row(circ("book", TINT), "Comptabilité", "Justificatifs et exports", soon_badge(), href="Accounting.dc.html")
        + row(circ("trend", TINT), "Financement", "Prêts, affacturage, factures", soon_badge(), href="Financing.dc.html", last=True))),
    group("Compte", panel(
        row(circ("user", SOFT), "Profil et sécurité", None, href="Settings.dc.html", chevron=True)
        + row(circ("help", SOFT), "Aide et contact", "WhatsApp, e-mail, téléphone", chevron=True)
        + row(circ("logout", ERRBG, ERR), "Se déconnecter", None, href="Welcome.dc.html", last=True))),
]), nav_tab="Plus")

add("Notifications.dc.html", "Notifications", "".join([
    header("Main.dc.html", small_btn("Tout marquer comme lu", "secondary")), h1("Notifications"),
    day("Aujourd'hui", panel(
        row(circ("clock", WARNBG, WARN), "Paie d'octobre à valider", "Moussa Diop a validé, il manque votre accord · 11:05", href="BulkApproval.dc.html")
        + row(circ("shield", TINT), "Virement à valider", "2 450 000 FCFA vers Diallo Matériaux, préparé par Fatou Sarr · 10:12", href="Approvals.dc.html")
        + row(circ("receive", POSBG, POS), "Recharge Wave reçue", "+500 000 FCFA sur le compte principal · 09:14", href="TxDetail.dc.html", last=True))),
    day("Cette semaine", panel(
        row(circ("alert", ERRBG, ERR), "Paiement refusé", "Carte Publicité en ligne : plafond mensuel atteint · jeudi", href="CardDetail.dc.html")
        + row(circ("file", SOFT), "Relevé de septembre disponible", "Compte principal · mardi", href="Statements.dc.html")
        + row(circ("drop", TINT), "Facture Sen'Eau", "41 200 FCFA à payer avant le 5 novembre · lundi", href="Bills.dc.html")
        + row(circ("check", POSBG, POS), "Votre compte est ouvert", "IBAN prêt · choisissez votre offre avant le 12 janvier · 5 oct.", href="Approved.dc.html", last=True))),
]))

add("Settings.dc.html", "Profil et sécurité", "".join([
    header("More.dc.html"),
    center(av("AN", ACC, 72, True), f'<span style="font-size: 22px; font-weight: 800">Aïssatou Ndiaye</span>', p("Gérante · administratrice · +221 77 123 45 67", 13), gap=8),
    group("Entreprise", panel(
        row(circ("building", SOFT), "Atelier Ndiaye SARL", "NINEA 006543219 2G3", chevron=True)
        + row(circ("wallet", SOFT), "Offre et abonnement", "Essai gratuit jusqu'au 12 janvier · offre à choisir", href="Plan.dc.html", chevron=True, last=True))),
    group("Sécurité", panel(
        row(circ("lock", SOFT), "Code secret", "Pour valider les paiements", chevron=True)
        + toggle_row("Face ID", "Pour se connecter et valider", True, lead=circ("face", SOFT))
        + row(circ("phone", SOFT), "Appareils connectés", "2 appareils", chevron=True, last=True))),
    group("Préférences", panel(
        row(circ("globe", SOFT), "Langue", "Français", chevron=True)
        + toggle_row("Notifications", "Paiements, validations, factures", True, last=True, lead=circ("bell", SOFT)))),
    panel(row(circ("msg", SOFT), "Aide sur WhatsApp", "Un conseiller vous répond", chevron=True)
          + row(circ("logout", ERRBG, ERR), "Se déconnecter", None, href="Welcome.dc.html", last=True)),
]))

# ------------------------------------------------------------------ Account opening (KYB + KYC)
def check_item(t):
    return (f'<div style="display: flex; gap: 10px; align-items: center"><span style="width: 24px; height: 24px; border-radius: 12px; background: {ACC}; {RING}; '
            f'display: flex; align-items: center; justify-content: center; flex: none">{ic("check", 14, "2.6")}</span><span style="font-size: 14px; font-weight: 600">{t}</span></div>')


add("Welcome.dc.html", "Bienvenue", "".join([
    f'<div style="display: flex; align-items: center; justify-content: space-between; height: 44px">{wordmark(20, 12)}'
    f'<button style="all: unset; cursor: pointer; font-size: 13px; font-weight: 700; padding: 8px 12px; border-radius: 16px; border: {BORDER}">Français</button></div>',
    bank_card("Atelier Ndiaye SARL", "4821", "Carte entreprise"),
    h1("Le compte pro qui construit avec vous.", "IBAN, cartes Visa, paie des salariés et paiements par banque, Wave ou Orange Money. Un seul abonnement, sans frais cachés.", size=30),
    stack(check_item("Ouverture en ligne, sans passer en agence"), check_item("Salaires payés sur banque, Wave ou Orange Money"), check_item("Cartes Visa virtuelles illimitées")),
]), btns=[cta("Ouvrir un compte", "SignUp.dc.html"), cta("J'ai déjà un compte", "Main.dc.html", "secondary")])

consent = (f'<button aria-pressed="true" style="all: unset; cursor: pointer; display: flex; gap: 10px; align-items: flex-start">'
           f'<span style="width: 22px; height: 22px; box-sizing: border-box; border-radius: 7px; background: {ACC}; border: 1.5px solid {INK}; display: flex; align-items: center; justify-content: center; flex: none">{ic("check", 13, "3")}</span>'
           f'<span style="font-size: 13px; line-height: 1.45; color: {MUTED}">J\'accepte les conditions générales et la politique de confidentialité de Tabax.</span></button>')

add("SignUp.dc.html", "Inscription", "".join([
    header("Welcome.dc.html"),
    h1("Votre numéro de téléphone", "Nous vous envoyons un code par SMS. Ce numéro servira à vous connecter."),
    field("Téléphone portable", "77 123 45 67", prefix="+221", mode="tel"),
    field("E-mail professionnel", "aissatou@atelierndiaye.sn", typ="email"),
    consent,
]), btns=[cta("Recevoir le code", "Otp.dc.html")])

boxes = "".join(
    f'<input aria-label="Chiffre {i + 1}" inputmode="numeric" value="{d}" style="width: 48px; height: 58px; box-sizing: border-box; border-radius: 16px; '
    f'border: {"1.5px solid #161616" if i == 4 else "1px solid rgba(22,22,22,0.16)"}; text-align: center; font: inherit; font-size: 24px; font-weight: 800; color: {INK}; outline: none; background: #FFFFFF">'
    for i, d in enumerate(["4", "8", "2", "1", "", ""]))
add("Otp.dc.html", "Code SMS", "".join([
    header("SignUp.dc.html", close="Welcome.dc.html"),
    h1("Entrez le code reçu par SMS", "Envoyé au +221 77 123 45 67."),
    f'<div style="display: flex; justify-content: space-between">{boxes}</div>',
    f'<div style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 13px; color: {MUTED}">Nouveau code dans <strong style="color: {INK}">0:42</strong></span>'
    f'<a href="SignUp.dc.html" style="{link_style()}">Changer de numéro</a></div>',
]), btns=[cta("Vérifier", "Company.dc.html")])

add("Company.dc.html", "Entreprise", "".join([
    header("Otp.dc.html", close="Welcome.dc.html"), stepper(1, 4, "Entreprise"),
    h1("Votre entreprise", "Indiquez votre NINEA : nous retrouvons votre entreprise quand c'est possible."),
    field("NINEA ou RCCM", "006543219 2G3", icon="search"),
    panel(row(circ("check", POSBG, POS), "Atelier Ndiaye SARL", "Dakar · vérifiez les informations ci-dessous", last=True)),
    field("Raison sociale", "Atelier Ndiaye SARL"),
    stack(label("Forme juridique"), chips(["SARL", "SUARL", "SA", "GIE", "Entreprise individuelle"], 0), gap=8),
    field("RCCM", "SN-DKR-2019-B-12345"),
    field("Secteur d'activité", "Menuiserie et ameublement"),
    stack(label("Nombre de salariés"), chips(["1 à 10", "11 à 50", "51 et plus"], 1), gap=8),
    field("Adresse du siège", "Route de Rufisque, zone industrielle, Dakar"),
]), btns=[cta("Continuer", "CompanyDocs.dc.html")])


def doc_row(title, sub, state, last=False):
    if state == "done":
        return row(circ("file", POSBG, POS), title, sub, pill("Ajouté", "pos"), last=last)
    if state == "opt":
        return row(circ("file", SOFT), title, sub, pill("Facultatif"), last=last)
    return row(circ("file", SOFT), title, sub, small_btn("Ajouter", "secondary", icon="upload"), last=last)


add("CompanyDocs.dc.html", "Documents", "".join([
    header("Company.dc.html", close="Welcome.dc.html"), stepper(2, 4, "Documents"),
    h1("Documents de l'entreprise", "PDF ou photo lisible, 10 Mo maximum par fichier."),
    panel(doc_row("Statuts signés", "statuts_atelier_ndiaye.pdf · 2,4 Mo", "done")
          + doc_row("Extrait RCCM", "Moins de 3 mois · rccm_2026.pdf", "done")
          + doc_row("Attestation NINEA", "PDF ou photo", "todo")
          + doc_row("Justificatif d'adresse", "Facture Senelec ou Sen'Eau de moins de 3 mois", "todo")
          + doc_row("PV de nomination du gérant", "Seulement s'il n'est pas dans les statuts", "opt", last=True)),
    note("Vos documents sont chiffrés et vus uniquement par notre équipe conformité.", "soft", "lock"),
]), btns=[cta("Continuer", "Director.dc.html")])


def photo_tile(t, done):
    if done:
        return (f'<div style="border-radius: 18px; border: {BORDER}; background: {SOFT}; aspect-ratio: 1.4; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px">'
                f'{circ("check", POSBG, POS, 36, 16)}<span style="font-size: 14px; font-weight: 800">{t}</span><span style="font-size: 12px; color: {MUTED}">Photo ajoutée</span></div>')
    return (f'<button style="all: unset; cursor: pointer; box-sizing: border-box; border-radius: 18px; border: 1.5px dashed {INK}; background: #FFFFFF; aspect-ratio: 1.4; display: flex; '
            f'flex-direction: column; align-items: center; justify-content: center; gap: 6px">{circ("camera", TINT, INK, 36, 16)}<span style="font-size: 14px; font-weight: 800">{t}</span>'
            f'<span style="font-size: 12px; color: {MUTED}">Prendre la photo</span></button>')


add("Director.dc.html", "Identité du dirigeant", "".join([
    header("CompanyDocs.dc.html", close="Welcome.dc.html"), stepper(3, 4, "Dirigeant"),
    h1("Votre identité", "Aïssatou Ndiaye, gérante. Une pièce d'identité et un selfie vidéo."),
    segmented(["Carte d'identité CEDEAO", "Passeport"], 0),
    grid(2, photo_tile("Recto", True), photo_tile("Verso", False), gap=10),
    panel(row(circ("face", TINT), "Selfie vidéo de 5 secondes", "Pour vérifier que c'est bien vous", small_btn("Commencer"), last=True)),
    note("Bonne lumière, pas de reflet, les quatre coins de la carte visibles.", "soft", "info"),
]), btns=[cta("Continuer", "Owners.dc.html")])

add("Owners.dc.html", "Bénéficiaires effectifs", "".join([
    header("Director.dc.html", close="Welcome.dc.html"), stepper(4, 4, "Actionnaires"),
    h1("Bénéficiaires effectifs", "Toute personne qui détient au moins 25 % du capital ou qui contrôle l'entreprise."),
    panel(row(av("AN", ACC, 40, True), "Aïssatou Ndiaye", "Vous · gérante · identité vérifiée", right_text("60 %", INK, 16, 800))
          + row(av("CN", SOFT), "Cheikh Ndiaye", "Lien de vérification envoyé par SMS", right_text("40 %", INK, 16, 800), last=True)),
    stack(f'<span style="display: flex; justify-content: space-between; font-size: 13px"><span style="color: {MUTED}">Capital déclaré</span><strong>100 %</strong></span>', progress(100), gap=8),
    f'<button style="all: unset; cursor: pointer; box-sizing: border-box; height: 52px; border-radius: 26px; border: 1.5px dashed {INK}; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 15px; font-weight: 800">{ic("plus", 18, "2.3")}Ajouter une personne</button>',
    stack(label("Une de ces personnes est-elle politiquement exposée ?"), segmented(["Non", "Oui"], 0),
          p("Élu, haut fonctionnaire, dirigeant d'entreprise publique, ou un de leurs proches.", 12), gap=8),
]), btns=[cta("Envoyer mon dossier", "Review.dc.html")])


def plan_card(name, size_, price, selected=False, tag=""):
    st = f"border: 1.5px solid {INK}; background: #FFFFFF" if selected else f"border: {BORDER}; background: {GLASS}"
    radio = (f'<span style="width: 22px; height: 22px; border-radius: 11px; box-sizing: border-box; border: 1.5px solid {ACC if selected else "#C5C9D0"}; background: {ACC if selected else "#FFFFFF"}; '
             f'display: flex; align-items: center; justify-content: center; flex: none">{ic("check", 12, "3") if selected else ""}</span>')
    t = f'<span style="margin-top: 6px">{pill(tag, "info")}</span>' if tag else ""
    return (f'<button aria-pressed="{"true" if selected else "false"}" style="all: unset; cursor: pointer; box-sizing: border-box; border-radius: 20px; padding: 16px; {st}; display: flex; align-items: center; gap: 12px">'
            f'{radio}<span style="display: flex; flex-direction: column; align-items: flex-start; gap: 2px; flex: 1 1 auto"><span style="font-size: 17px; font-weight: 800">{name}</span>'
            f'<span style="font-size: 13px; color: {MUTED}">{size_}</span>{t}</span>'
            f'<span style="display: flex; flex-direction: column; align-items: flex-end"><span style="font-size: 20px; font-weight: 800">{price}</span><span style="font-size: 12px; color: {MUTED}">FCFA / mois</span></span></button>')


def inc(t):
    return f'<div style="display: flex; gap: 10px; align-items: flex-start; font-size: 13px; line-height: 1.4"><span style="color: {POS}; display: flex; flex: none">{ic("check", 16, "2.6")}</span><span>{t}</span></div>'


add("Plan.dc.html", "Offre et abonnement", "".join([
    header("More.dc.html"),
    h1("Choisissez votre offre", "Les 3 premiers mois sont offerts. Choisissez une offre avant le 12 janvier 2027 pour garder votre compte."),
    segmented(["Mensuel", "Annuel · 2 mois offerts"], 0),
    stack(plan_card("Petite", "1 à 10 salariés", "9 900"), plan_card("Moyenne", "11 à 50 salariés", "29 900", True, "Pour vos 24 salariés"), plan_card("Grande", "51 salariés et plus", "79 900")),
    group("Inclus dans toutes les offres", panel(stack(
        inc("Compte avec IBAN, sous-comptes et relevés"), inc("Utilisateurs illimités et double validation"), inc("Cartes virtuelles illimitées"),
        inc("Salaires vers toutes les banques et wallets, sans limite"), inc("200 virements fournisseurs par mois (offre Moyenne), puis 100 FCFA"),
        inc("Virements et paiements PI-SPI reçus gratuits")), pad="14px 16px")),
    p("Autres frais : carte physique 5 000 FCFA une fois · paiements par carte hors FCFA 1 %. Rien d'autre.", 12),
]), btns=[cta("Activer l'offre Moyenne", "Main.dc.html")], note_txt="Premier prélèvement le 12 janvier 2027. Sans engagement.")

add("Approved.dc.html", "Compte ouvert", "".join([
    header(None, close="Main.dc.html"),
    success("check", "Votre compte est ouvert",
            f'<span style="height: 34px; padding: 0 14px; border-radius: 17px; background: {TINT}; font-size: 13px; font-weight: 700; display: inline-flex; align-items: center">IBAN SN08 SN01 •••• 3035</span>',
            "Atelier Ndiaye SARL est validée. Vous avez aussi reçu un e-mail de confirmation avec votre RIB."),
    note("Les 3 premiers mois sont offerts. Choisissez votre offre avant le 12 janvier 2027 pour garder votre compte.", "info", "calendar"),
]), btns=[cta("Choisir mon offre", "Plan.dc.html"), cta("Aller à l'accueil", "Main.dc.html", "secondary")])

add("Review.dc.html", "Dossier envoyé", "".join([
    center(circ("clock", TINT, INK, 88, 40), f'<h1 style="margin: 6px 0 0; font-size: 28px; font-weight: 800; letter-spacing: -0.6px">Dossier envoyé</h1>',
           p("Nous vérifions vos informations. Vous pouvez déjà découvrir l'application. Dès que le compte est validé, vous recevez une notification et un e-mail, en général sous 48 h ouvrées.", 15), gap=12, pt=40),
    panel(row(circ("check", POSBG, POS, 36, 16), "Compte créé", "12 oct. 2026, 09:02")
          + row(circ("check", POSBG, POS, 36, 16), "Entreprise", "NINEA et RCCM reçus")
          + row(circ("check", POSBG, POS, 36, 16), "Identité de la gérante", "Vérifiée")
          + row(circ("clock", WARNBG, WARN, 36, 16), "Documents", "En cours d'analyse", pill("En cours", "warn"))
          + row(circ("clock", WARNBG, WARN, 36, 16), "Cheikh Ndiaye (40 %)", "Attend sa vérification", pill("En attente", "warn"))
          + row(circ("bank", SOFT, INK, 36, 16), "Ouverture du compte et IBAN", "Dès la validation", last=True)),
]), btns=[cta("Découvrir l'application", "Main.dc.html"), cta("Parler à un conseiller", kind="secondary", icon="msg")])

# ------------------------------------------------------------------ Accounts and bank details
def acct_card(name, color, iban4, bal, sub, href):
    return (f'<a href="{href}" style="border-radius: 22px; padding: 16px; background: {GLASS}; border: {BORDER}; box-shadow: {SH_CARD}; display: flex; flex-direction: column; gap: 8px; text-decoration: none; color: {INK}">'
            f'<span style="display: flex; align-items: center; justify-content: space-between; gap: 8px"><span style="display: flex; align-items: center; gap: 8px; font-size: 15px; font-weight: 800">'
            f'<span style="width: 10px; height: 10px; border-radius: 5px; background: {color}; {RING}"></span>{name}</span><span style="font-size: 12px; color: {MUTED}">IBAN •••• {iban4}</span></span>'
            f'<span style="font-size: 26px; font-weight: 800; letter-spacing: -0.8px">{bal} <span style="font-size: 12px; font-weight: 700; color: {MUTED}; letter-spacing: 1px">FCFA</span></span>'
            f'<span style="font-size: 12px; color: {MUTED}">{sub}</span></a>')


add("Accounts.dc.html", "Comptes", "".join([
    header("Main.dc.html", icon_link("plus", "NewSubAccount.dc.html", "Nouveau sous-compte")),
    h1("Comptes", "3 comptes · 12 480 350 FCFA au total"),
    acct_card("Principal", INK, "3035", "8 210 000", "Compte courant · cartes et virements", "AccountDetails.dc.html"),
    acct_card("Salaires", ACC, "3043", "3 500 000", "Alimenté le 25 de chaque mois depuis Principal", "AccountDetails.dc.html"),
    acct_card("Fournisseurs", "#BDBDBD", "3051", "770 350", "Réservé aux paiements fournisseurs", "AccountDetails.dc.html"),
    f'<a href="NewSubAccount.dc.html" style="box-sizing: border-box; height: 52px; border-radius: 26px; border: 1.5px dashed {INK}; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 15px; font-weight: 800; color: {INK}; text-decoration: none">{ic("plus", 18, "2.3")}Nouveau sous-compte</a>',
    group("Documents", panel(row(circ("file", SOFT), "Relevés et attestations", "Relevés mensuels, RIB, attestation de solde", href="Statements.dc.html", chevron=True, last=True))),
]))

add("AccountDetails.dc.html", "Compte principal", "".join([
    header("Accounts.dc.html", icon_button("share", "Partager le RIB"), close="Main.dc.html"), h1("Compte principal"),
    tile(f'<span style="font-size: 12px; font-weight: 600; letter-spacing: 1.2px; text-transform: uppercase; color: {MUTED}">Solde disponible</span>'
         f'<span style="font-size: 42px; font-weight: 800; letter-spacing: -1.5px; line-height: 1.1; font-variant-numeric: proportional-nums">8 210 000</span>{fcfa_tag()}'),
    actions(action("Partager le RIB", None, "share", True), action("RIB en PDF", None, "download"), action("Relevés", "Statements.dc.html", "file")),
    group("Coordonnées bancaires", kv([
        ("Titulaire", "Atelier Ndiaye SARL"), ("IBAN", "SN08 SN01 0015 2000 0253 0001 3035", copy_btn("l'IBAN")), ("BIC", "[BIC banque partenaire]", copy_btn("le BIC")),
        ("Banque", "[Banque partenaire], Dakar"), ("Code banque", "SN010"), ("Code guichet", "01520"), ("N° de compte", "000253000130"), ("Clé RIB", "35")])),
    note("Les virements reçus sont gratuits, depuis toutes les banques de l'UEMOA. Compatible PI-SPI pour les virements instantanés.", "info"),
]))

swatches = "".join(
    f'<button aria-label="{n}" aria-pressed="{"true" if i == 2 else "false"}" style="all: unset; cursor: pointer; width: 42px; height: 42px; border-radius: 21px; box-sizing: border-box; '
    f'border: 2px solid {INK if i == 2 else "transparent"}; display: flex; align-items: center; justify-content: center"><span style="width: 28px; height: 28px; border-radius: 14px; background: {c}; {RING}"></span></button>'
    for i, (c, n) in enumerate([(INK, "Noir"), (ACC, "Sarcelle"), ("#F7876A", "Corail"), ("#5DC79B", "Jade"), ("#A792F2", "Lavande"), ("#F5B731", "Souci")]))
add("NewSubAccount.dc.html", "Nouveau sous-compte", "".join([
    header("Accounts.dc.html", close="Main.dc.html"),
    h1("Nouveau sous-compte", "Mettez de côté par usage : impôts, salaires, projets. Chaque sous-compte a son IBAN."),
    field("Nom du sous-compte", "Impôts et TVA"),
    stack(label("Usage"), chips(["Impôts", "Épargne", "Projet", "Fournisseurs", "Autre"], 0), gap=8),
    stack(label("Couleur"), f'<div style="display: flex; gap: 8px">{swatches}</div>', gap=8),
    panel(toggle_row("Mettre de côté automatiquement", "18 % de chaque paiement reçu, pour la TVA", True)
          + row(circ("users", SOFT), "Qui peut l'utiliser", "Administrateurs uniquement", chevron=True, last=True)),
]), btns=[cta("Créer le sous-compte", "Accounts.dc.html")])

dl = f'<button aria-label="Télécharger" style="all: unset; cursor: pointer; width: 36px; height: 36px; border-radius: 18px; background: {TINT}; display: flex; align-items: center; justify-content: center; flex: none">{ic("download", 16)}</button>'
add("Statements.dc.html", "Relevés et attestations", "".join([
    header("AccountDetails.dc.html", close="Main.dc.html"), h1("Relevés et attestations"),
    segmented(["Principal", "Salaires", "Fournisseurs"], 0),
    stack(label("Période"), chips(["3 derniers mois", "2026", "2025", "Personnalisée"], 0), date_filter("Du 1er juillet au 30 septembre 2026", export=False), gap=8),
    group("Relevés mensuels", panel(row(circ("file", SOFT), "Septembre 2026", "PDF · 42 opérations", dl) + row(circ("file", SOFT), "Août 2026", "PDF · 38 opérations", dl)
                                    + row(circ("file", SOFT), "Juillet 2026", "PDF · 45 opérations", dl) + row(circ("file", SOFT), "Juin 2026", "PDF · 40 opérations", dl, last=True))),
    group("Attestations", panel(row(circ("bank", SOFT), "RIB", "Avec IBAN et BIC", small_btn("Générer", "secondary"))
                                + row(circ("wallet", SOFT), "Attestation de solde", "À la date de votre choix", small_btn("Générer", "secondary"))
                                + row(circ("building", SOFT), "Attestation de domiciliation", "Pour vos clients et l'administration", small_btn("Générer", "secondary"), last=True))),
    panel(row(circ("book", TINT), "Export pour votre comptable", "Excel ou CSV, plan SYSCOHADA", soon_badge(), href="Accounting.dc.html", last=True)),
]))

# ------------------------------------------------------------------ Top up
add("TopUp.dc.html", "Recharger", "".join([
    header("Main.dc.html"), h1("Recharger", "Choisissez comment ajouter de l'argent."),
    stack(label("Vers"), panel(acct_from("Compte principal", "8 210 000 FCFA"))),
    group("Mobile money", panel(row(circ("phone", TINT, INK, text="W"), "Wave", "Instantané", href="TopUpWave.dc.html", chevron=True)
                                + row(circ("phone", "#FDE3DB", INK, text="OM"), "Orange Money", "Instantané", href="TopUpWave.dc.html", chevron=True, last=True))),
    group("Banque et carte", panel(row(circ("bank", SOFT), "Virement bancaire", "Gratuit · instantané avec PI-SPI", href="TopUpBank.dc.html", chevron=True)
                                   + row(circ("card", SOFT), "Carte Visa ou Mastercard", "Instantané", href="TopUpCard.dc.html", chevron=True, last=True))),
    group("Espèces", panel(row(circ("cash", SOFT), "Dépôt d'espèces", "En agence partenaire, avec un code", href="CashDeposit.dc.html", chevron=True, last=True))),
]))

add("TopUpWave.dc.html", "Recharge Wave", "".join([
    header("TopUp.dc.html", close="Main.dc.html"), h1("Recharger avec Wave", size=24),
    big_amount("500 000"),
    chips(["100 000", "250 000", "500 000", "1 000 000"], 2),
    field("Numéro Wave", "77 123 45 67", prefix="+221", mode="tel"),
    panel(acct_from("Vers : compte principal", "Solde 8 210 000 FCFA")),
]), btns=[cta("Continuer", "TopUpConfirm.dc.html")])

add("TopUpConfirm.dc.html", "Validation Wave", "".join([
    header("TopUpWave.dc.html", close="Main.dc.html"),
    center(circ("phone", TINT, INK, 88, 40), f'<h1 style="margin: 6px 0 0; font-size: 26px; font-weight: 800; letter-spacing: -0.6px">Validez dans Wave</h1>',
           p("Une demande de 500 000 FCFA a été envoyée au +221 77 123 45 67. Ouvrez Wave et confirmez avec votre code.", 15), pill("En attente · expire dans 4:52", "warn"), gap=12, pt=10),
    kv([("Montant", "500 000 FCFA"), ("Depuis", "Wave · 77 123 45 67"), ("Vers", "Compte principal"), ("Référence", "TBX-REC-8821")]),
]), btns=[cta("J'ai confirmé dans Wave", "TopUpSuccess.dc.html"), cta("Annuler", "TopUp.dc.html", "secondary")])

add("TopUpSuccess.dc.html", "Recharge reçue", header(None, close="Main.dc.html") + success("check", "Recharge reçue",
    f'<span style="font-size: 34px; font-weight: 800; letter-spacing: -1px; color: {POS}">+500 000 FCFA</span>',
    "Ajoutée au compte principal. Nouveau solde : 8 710 000 FCFA."),
    btns=[cta("Retour à l'accueil", "Main.dc.html"), cta("Voir le reçu", "TxDetail.dc.html", "secondary")])

add("TopUpCard.dc.html", "Recharge par carte", "".join([
    header("TopUp.dc.html", close="Main.dc.html"), h1("Recharger par carte", size=24),
    big_amount("250 000"),
    field("Numéro de carte", placeholder="1234 5678 9012 3456", icon="card", mode="numeric"),
    grid(2, field("Expiration", placeholder="MM/AA", mode="numeric"), field("CVC", placeholder="123", mode="numeric"), gap=10),
    field("Nom sur la carte", "Aissatou Ndiaye"),
    note("Votre banque peut vous demander de confirmer avec 3-D Secure.", "soft", "shield"),
]), btns=[cta("Payer 250 000 FCFA", "TopUpSuccess.dc.html")])

add("TopUpBank.dc.html", "Recevoir un virement", "".join([
    header("TopUp.dc.html", close="Main.dc.html"), h1("Recevoir un virement", "Partagez votre RIB. Les virements reçus sont gratuits."),
    kv([("Titulaire", "Atelier Ndiaye SARL"), ("IBAN", "SN08 SN01 0015 2000 0253 0001 3035", copy_btn("l'IBAN")), ("BIC", "[BIC banque partenaire]", copy_btn("le BIC")), ("Banque", "[Banque partenaire]")]),
    group("Comment ça marche", steps([("Partagez votre RIB", "À votre client ou à votre banque"), ("Le virement part de n'importe quelle banque", "Partout dans l'UEMOA"),
                                      ("L'argent arrive sur votre compte", "Instantané avec PI-SPI, sinon en général 1 jour ouvré")])),
]), btns=[cta("Partager le RIB", icon="share"), cta("Télécharger le RIB (PDF)", kind="secondary", icon="download")])

add("CashDeposit.dc.html", "Dépôt d'espèces", "".join([
    header("TopUp.dc.html", close="Main.dc.html"), h1("Dépôt d'espèces", "Présentez ce code et votre pièce d'identité au guichet."),
    tile(f'<span style="font-size: 12px; font-weight: 600; letter-spacing: 1.2px; text-transform: uppercase; color: {MUTED}">Votre code de dépôt</span>'
         f'<span style="font-size: 36px; font-weight: 800; letter-spacing: 3px; margin: 4px 0">TBX 4821 77</span>{pill("Valable 24 h", "info")}'
         f'<span style="margin-top: 10px">{small_btn("Copier le code", "secondary", icon="copy")}</span>'),
    group("Où déposer", panel(row(circ("pin", SOFT), "[Banque partenaire] · Plateau", "2,1 km · ouvert jusqu'à 16 h", chevron=True)
                              + row(circ("pin", SOFT), "[Banque partenaire] · Point E", "3,4 km · ouvert jusqu'à 16 h", chevron=True)
                              + row(circ("pin", SOFT), "[Banque partenaire] · Parcelles Assainies", "7,8 km · ouvert le samedi matin", chevron=True, last=True))),
    note("L'argent arrive sur votre compte dès que le guichet valide le dépôt.", "soft", "info"),
]))

# ------------------------------------------------------------------ Send
add("Send.dc.html", "Envoyer", "".join([
    header("Main.dc.html"), h1("Envoyer"),
    field(None, placeholder="Nom, IBAN ou numéro", icon="search"),
    segmented(["Tous", "Banque", "Mobile money"], 0),
    panel(row(circ("plus", ACC, INK, ring=True), "Nouveau bénéficiaire", "Banque, Wave ou Orange Money", href="NewRecipient.dc.html", chevron=True)
          + row(circ("swap", SOFT), "Entre vos comptes", "Principal, Salaires, Fournisseurs", href="SendAmount.dc.html", chevron=True, last=True)),
    group("Récents", panel(row(av("CL", TINT), "Cissé Logistique SARL", "Banque · SN12 •••• 7781", href="SendAmount.dc.html", chevron=True)
                           + row(av("SD", "#FDE3DB"), "Sow Distribution", "Wave · 77 ••• •• 12", href="SendAmount.dc.html", chevron=True)
                           + row(av("DM", "#DDF4EA"), "Diallo Matériaux", "Orange Money · 78 ••• •• 40", href="SendAmount.dc.html", chevron=True)
                           + row(av("IB", "#ECE6FD"), "Imprimerie Ba", "Banque · SN08 •••• 2209", href="SendAmount.dc.html", chevron=True, last=True))),
    panel(row(circ("globe", SOFT), "Virement international", "EUR, USD, CNY…", soon_badge(), href="Intl.dc.html", last=True)),
]))


def type_btn(t, icon, on=False):
    st = f"background: {ACC}; border: 1.5px solid {INK}" if on else f"background: {GLASS}; border: {BORDER}"
    return (f'<button aria-pressed="{"true" if on else "false"}" style="all: unset; cursor: pointer; box-sizing: border-box; border-radius: 18px; padding: 14px 8px; {st}; display: flex; '
            f'flex-direction: column; align-items: center; gap: 8px; text-align: center">{ic(icon, 22, "2.2")}<span style="font-size: 13px; font-weight: 800">{t}</span></button>')


add("NewRecipient.dc.html", "Nouveau bénéficiaire", "".join([
    header("Send.dc.html", close="Main.dc.html"), h1("Nouveau bénéficiaire"),
    grid(3, type_btn("Banque", "bank", True), type_btn("Wave", "phone"), type_btn("Orange Money", "phone")),
    field("Nom du bénéficiaire", "Cissé Logistique SARL"),
    field("IBAN", "SN12 SN05 4010 1700 0458 1200 7781"),
    stack(label("Type de bénéficiaire"), segmented(["Fournisseur", "Salarié", "Autre"], 0),
          p("Les salaires sont exonérés de la taxe de 0,5 % sur les transferts.", 12), gap=8),
    panel(toggle_row("Ajouter aux favoris", "Pour le retrouver en haut de la liste", True, last=True)),
]), btns=[cta("Continuer", "SendAmount.dc.html")])

add("SendAmount.dc.html", "Montant", "".join([
    header("Send.dc.html", close="Main.dc.html"),
    panel(row(av("CL", TINT), "Cissé Logistique SARL", "Banque · SN12 •••• 7781", last=True)),
    big_amount("1 250 000"),
    panel(acct_from()),
    field("Motif", "Facture F-2026-118, transport septembre"),
    keypad(),
]), btns=[cta("Vérifier", "SendReview.dc.html")])

add("SendReview.dc.html", "Vérification", "".join([
    header("SendAmount.dc.html", close="Main.dc.html"), h1("Vérifiez le virement", size=24),
    big_amount("1 250 000"),
    kv([("À", "Cissé Logistique SARL"), ("IBAN", "SN12 •••• 7781"), ("Depuis", "Compte principal"), ("Arrivée", "Instantanée (PI-SPI)"), ("Motif", "Facture F-2026-118")]),
    kv([("Frais Tabax", "0 FCFA"), ("Taxe sur les transferts (0,5 %)", "6 250 FCFA"), ("Total débité", "1 256 250 FCFA")]),
    note("Virement fournisseur n° 15 sur les 200 inclus ce mois-ci. La taxe de 0,5 % est reversée à l'État.", "soft", "info"),
]), btns=[cta("Confirmer avec Face ID", "SendSuccess.dc.html", icon="face")])

add("SendSuccess.dc.html", "Virement envoyé", header(None, close="Main.dc.html") + success("check", "Virement envoyé",
    f'<span style="font-size: 34px; font-weight: 800; letter-spacing: -1px">1 250 000 FCFA</span>',
    "À Cissé Logistique SARL. Arrivé instantanément · réf. TBX-VIR-55120."),
    btns=[cta("Retour à l'accueil", "Main.dc.html"), cta("Partager le justificatif", kind="secondary", icon="share")])

# ------------------------------------------------------------------ Bulk payouts
add("Bulk.dc.html", "Paie groupée", "".join([
    header("Main.dc.html"),
    h1("Paie groupée", "Salaires et prestataires en une fois, vers toutes les banques, Wave et Orange Money."),
    f'<div style="display: flex">{cta("Nouveau paiement groupé", "BulkNew.dc.html", icon="plus")}</div>',
    group("À valider", panel(row(circ("calendar", TINT), "Paie d'octobre", "24 salariés · 3 465 000 FCFA · 31 oct.", pill("Prête", "info"), href="BulkReview.dc.html", chevron=True, last=True))),
    group("Historique", panel(row(circ("check", POSBG, POS), "Paie de septembre", "Payée le 30 sept. · 24 salariés", amt(3420000))
                              + row(circ("check", POSBG, POS), "Prestataires chantier", "Payés le 12 sept. · 6 prestataires", amt(1180000))
                              + row(circ("check", POSBG, POS), "Paie d'août", "Payée le 29 août · 23 salariés", amt(3310000), last=True))),
    note("Salaires gratuits et sans limite, exonérés de la taxe sur les transferts.", "pos", "check"),
]))

add("BulkNew.dc.html", "Nouveau paiement groupé", "".join([
    header("Bulk.dc.html", close="Main.dc.html"), h1("Nouveau paiement groupé", size=24),
    field("Nom", "Paie d'octobre 2026"),
    stack(label("Type"), segmented(["Salaires", "Prestataires"], 0), gap=8),
    panel(acct_from("Depuis : compte Salaires", "3 500 000 FCFA disponibles", ACC, last=False)
          + row(circ("calendar", SOFT), "Date de paiement", "Vendredi 31 octobre 2026, 08:00", chevron=True, last=True)),
    group("Bénéficiaires", stack(
        option("Choisir parmi vos bénéficiaires", "Salariés et fournisseurs déjà enregistrés", "users", True, href="BulkPick.dc.html"),
        option("Reprendre la paie de septembre", "24 salariés, montants modifiables", "refresh"),
        option("Importer un fichier Excel ou CSV", "Un modèle est fourni", "upload"),
        option("Ajouter à la main", "Un par un", "plus"))),
]), btns=[cta("Continuer", "BulkPick.dc.html")])


def pick_box(on):
    return (f'<span style="width: 22px; height: 22px; box-sizing: border-box; border-radius: 7px; border: 1.5px solid {ACC if on else "#C5C9D0"}; background: {ACC if on else "#FFFFFF"}; '
            f'display: flex; align-items: center; justify-content: center; flex: none">{ic("check", 13, "3") if on else ""}</span>')


def pick_row(init, bg, name, sub, amount, on=True, last=False):
    sep = "" if last else f"border-bottom: 1px solid {LINE}; "
    return (f'<button aria-pressed="{"true" if on else "false"}" style="all: unset; cursor: pointer; box-sizing: border-box; display: flex; align-items: center; gap: 12px; padding: 12px 0; {sep}">'
            f'{pick_box(on)}{av(init, bg, 36)}<span style="display: flex; flex-direction: column; gap: 2px; flex: 1 1 auto; min-width: 0"><span style="font-size: 14px; font-weight: 700">{name}</span>'
            f'<span style="font-size: 12px; color: {MUTED}">{sub}</span></span>{amt(amount)}</button>')


add("BulkPick.dc.html", "Choisir les bénéficiaires", "".join([
    header("BulkNew.dc.html", close="Main.dc.html"),
    h1("Choisir les bénéficiaires", "Parmi les salariés et fournisseurs déjà enregistrés. Les montants de la dernière paie sont repris et modifiables.", size=24),
    field(None, placeholder="Rechercher un nom ou un numéro", icon="search"),
    segmented(["Salariés · 24", "Fournisseurs · 12"], 0),
    panel(f'<button aria-pressed="true" style="all: unset; cursor: pointer; box-sizing: border-box; display: flex; align-items: center; gap: 12px; padding: 12px 0">{pick_box(True)}'
          f'<span style="font-size: 14px; font-weight: 800; flex: 1 1 auto">Tout sélectionner</span><span style="font-size: 13px; color: {MUTED}">24 sur 24</span></button>'),
    panel(pick_row("IF", TINT, "Ibrahima Fall", "Banque · chef d'atelier", 420000)
          + pick_row("MD", "#FDE3DB", "Mariama Diop", "Wave · menuisière", 165000)
          + pick_row("OF", WARNBG, "Ousmane Faye", "Orange Money · menuisier", 120000)
          + pick_row("AS", "#DDF4EA", "Awa Sène", "Wave · finition", 150000)
          + pick_row("MG", "#ECE6FD", "Modou Gueye", "Banque · livraison", 210000)
          + pick_row("KN", TINT, "Khady Ndiaye", "Wave · vente", 140000, last=True)),
]), btns=[cta("Continuer", "BulkReview.dc.html")], note_txt="24 bénéficiaires sélectionnés · 3 465 000 FCFA")


def chan(n, t):
    return panel(f'<span style="font-size: 22px; font-weight: 800">{n}</span><span style="font-size: 12px; color: {MUTED}">{t}</span>', pad="12px", radius=18, gap=2)


add("BulkReview.dc.html", "Paie d'octobre", "".join([
    header("Bulk.dc.html", icon_button("edit", "Modifier"), close="Main.dc.html"),
    h1("Paie d'octobre", "Vendredi 31 octobre 2026 · depuis le compte Salaires"),
    tile(f'<span style="font-size: 12px; font-weight: 600; letter-spacing: 1.2px; text-transform: uppercase; color: {MUTED}">Total à payer</span>'
         f'<span style="font-size: 42px; font-weight: 800; letter-spacing: -1.5px; line-height: 1.1; font-variant-numeric: proportional-nums">3 465 000</span>{fcfa_tag()}'
         f'<span style="margin-top: 10px">{pill("Solde suffisant : 3 500 000 FCFA", "info")}</span>'),
    grid(3, chan("9", "Banque"), chan("11", "Wave"), chan("4", "Orange Money")),
    note("1 numéro à vérifier : Ousmane Faye, Orange Money 78 ••• •• 03.", "warn", "alert"),
    group("Salariés · 24", panel(
        row(av("IF", TINT), "Ibrahima Fall", "Banque · chef d'atelier", amt(420000))
        + row(av("MD", "#FDE3DB"), "Mariama Diop", "Wave · menuisière", amt(165000))
        + row(av("OF", WARNBG), "Ousmane Faye", "Orange Money · à vérifier", amt(120000))
        + row(av("AS", "#DDF4EA"), "Awa Sène", "Wave · finition", amt(150000))
        + row(av("MG", "#ECE6FD"), "Modou Gueye", "Banque · livraison", amt(210000), last=True)), "Voir les 24"),
    kv([("Frais", "0 FCFA"), ("Taxe sur les transferts", "Exonérée (salaires)")]),
]), btns=[cta("Envoyer pour validation", "BulkApproval.dc.html")])

add("BulkApproval.dc.html", "Validation de la paie", "".join([
    header("BulkReview.dc.html", close="Main.dc.html"),
    h1("Validation", "La double validation est activée pour les paiements groupés."),
    panel(row(circ("calendar", TINT), "Paie d'octobre", "24 salariés · 31 oct.", amt(3465000), last=True)),
    group("Circuit de validation", panel(
        row(circ("check", POSBG, POS), "Préparée par Fatou Sarr", "Assistante · 12 oct., 10:42")
        + row(circ("check", POSBG, POS), "Validée par Moussa Diop", "Comptable · 12 oct., 11:05")
        + row(circ("clock", WARNBG, WARN), "Votre validation", "Aïssatou Ndiaye · gérante", pill("En attente", "warn"), last=True))),
    note("Après votre accord, la paie part le 31 octobre à 08:00. Chaque salarié reçoit un SMS.", "soft", "info"),
]), btns=[cta("Valider et programmer", "BulkDone.dc.html", icon="face"), cta("Refuser", kind="secondary")])

add("BulkDone.dc.html", "Paie programmée", header(None, close="Main.dc.html") + success("check", "Paie programmée",
    f'<span style="font-size: 34px; font-weight: 800; letter-spacing: -1px">3 465 000 FCFA</span>',
    "24 salariés seront payés le vendredi 31 octobre à 08:00, sur leur banque, Wave ou Orange Money."),
    btns=[cta("Retour à l'accueil", "Main.dc.html"), cta("Voir la paie groupée", "Bulk.dc.html", "secondary")])

# ------------------------------------------------------------------ Bills
def biller(name, sub, icon, bg=SOFT):
    return (f'<a href="BillPay.dc.html" style="border-radius: 18px; padding: 14px 8px; background: {GLASS}; border: {BORDER}; box-shadow: {SH_CARD}; display: flex; flex-direction: column; '
            f'align-items: center; gap: 6px; text-decoration: none; color: {INK}; text-align: center">{circ(icon, bg)}<span style="font-size: 13px; font-weight: 800">{name}</span>'
            f'<span style="font-size: 11px; color: {MUTED}">{sub}</span></a>')


add("Bills.dc.html", "Factures", "".join([
    header("Main.dc.html"), h1("Factures"),
    field(None, placeholder="Rechercher un facturier", icon="search"),
    group("À payer", panel(row(circ("bolt", WARNBG, WARN), "Senelec", "Septembre · échéance 20 oct.", amt(126450), href="BillPay.dc.html", chevron=True)
                           + row(circ("drop", TINT), "Sen'Eau", "Septembre · échéance 5 nov.", amt(41200), href="BillPay.dc.html", chevron=True, last=True))),
    group("Facturiers", grid(3, biller("Senelec", "Électricité", "bolt"), biller("Woyofal", "Prépayé", "bolt"), biller("Sen'Eau", "Eau", "drop"),
                             biller("Orange", "Internet, mobile", "wifi"), biller("Yas", "Internet, mobile", "wifi"), biller("Canal+", "Télévision", "tv"))),
    panel(row(circ("building", SOFT), "Impôts et taxes", "Paiement à la DGID", soon_badge(), last=True)),
    group("Payées récemment", panel(row(circ("bolt", POSBG, POS), "Senelec", "Payée aujourd'hui, 08:02", amt(-84300), href="TxDetail.dc.html", last=True))),
]))

add("BillPay.dc.html", "Payer une facture", "".join([
    header("Bills.dc.html", close="Main.dc.html"),
    f'<div style="display: flex; align-items: center; gap: 14px">{circ("bolt", WARNBG, WARN, 56, 26)}{h1("Senelec", "Électricité · facture mensuelle", size=26)}</div>',
    field("Numéro de contrat", "2310 4471 902", mode="numeric"),
    group("Facture trouvée", kv([("Titulaire", "Atelier Ndiaye SARL"), ("Période", "Septembre 2026"), ("Échéance", "20 octobre 2026"), ("Montant", "126 450 FCFA"), ("Frais", "0 FCFA")])),
    panel(acct_from(last=False) + toggle_row("Enregistrer ce contrat", "Rappel chaque mois avant l'échéance", True, last=True)),
]), btns=[cta("Payer 126 450 FCFA", "BillSuccess.dc.html", icon="face")])

add("BillSuccess.dc.html", "Facture payée", header(None, close="Main.dc.html") + success("check", "Facture payée",
    f'<span style="font-size: 34px; font-weight: 800; letter-spacing: -1px">126 450 FCFA</span>',
    "Senelec · contrat 2310 4471 902. Le reçu est rangé avec l'opération."),
    btns=[cta("Retour à l'accueil", "Main.dc.html"), cta("Payer une autre facture", "Bills.dc.html", "secondary")])

# ------------------------------------------------------------------ Team and permissions
add("Team.dc.html", "Équipe et droits", "".join([
    header("More.dc.html", small_btn("Inviter", "primary", "Invite.dc.html", "plus")),
    h1("Équipe et droits", "Utilisateurs illimités, inclus dans votre offre."),
    panel(row(av("AN", ACC, 40, True), "Aïssatou Ndiaye", "Gérante · administratrice", pill("Vous", "info"))
          + row(av("MD", TINT), "Moussa Diop", "Comptable · exports et 1re validation", href="Permissions.dc.html", chevron=True)
          + row(av("FS", "#FDE3DB"), "Fatou Sarr", "Assistante · paiements jusqu'à 500 000 FCFA", href="Permissions.dc.html", chevron=True)
          + row(av("IF", "#DDF4EA"), "Ibrahima Fall", "Chef d'atelier · carte uniquement", href="Permissions.dc.html", chevron=True)
          + row(av("CN", SOFT), "Cheikh Ndiaye", "Invitation envoyée · lecture seule", pill("En attente", "warn"), last=True)),
    group("Règles", panel(row(circ("shield", SOFT), "Double validation", "Virements de plus de 1 000 000 FCFA et toutes les paies", chevron=True)
                          + row(circ("clock", WARNBG, WARN), "Validations en attente", "2 opérations", pill("2", "warn"), href="Approvals.dc.html", chevron=True, last=True))),
]))

add("Invite.dc.html", "Inviter un membre", "".join([
    header("Team.dc.html", close="More.dc.html"), h1("Inviter un membre"),
    field("Prénom et nom", "Khady Mbaye"),
    field("Téléphone", "76 555 21 09", prefix="+221", mode="tel"),
    field("E-mail", placeholder="Facultatif", typ="email"),
    group("Rôle", stack(option("Administrateur", "Tout faire, y compris gérer l'équipe", "shield"),
                        option("Comptable", "Voir, exporter, valider les paiements", "book"),
                        option("Payeur", "Préparer des paiements, toujours validés", "send", True),
                        option("Lecture seule", "Voir les comptes et les opérations", "eye"),
                        option("Carte uniquement", "Utiliser sa carte, envoyer ses justificatifs", "card"))),
]), btns=[cta("Continuer", "Permissions.dc.html")])

add("Permissions.dc.html", "Droits", "".join([
    header("Invite.dc.html", close="More.dc.html"), h1("Droits de Khady Mbaye", "Rôle Payeur. Ajustez chaque droit si besoin."),
    group("Comptes", panel(toggle_row("Voir les soldes et opérations", None, True) + row("", "Comptes accessibles", "Principal, Fournisseurs", chevron=True, last=True))),
    group("Paiements", panel(toggle_row("Préparer des virements", "Toujours validés par un administrateur", True)
                             + row("", "Plafond par virement", "500 000 FCFA", chevron=True)
                             + toggle_row("Préparer une paie groupée", None, False)
                             + toggle_row("Payer des factures", None, True, last=True))),
    group("Validation et cartes", panel(toggle_row("Valider les paiements des autres", None, False)
                                        + toggle_row("Demander une carte", "Virtuelle, avec plafond", True)
                                        + toggle_row("Exporter les relevés", None, False, last=True))),
]), btns=[cta("Envoyer l'invitation", "Team.dc.html", icon="send")])


def approval(init, bg, who, when, kind, amount, lines, left, right):
    return panel(
        row(av(init, bg, 36), who, when, pill(kind, "info"), last=True, pad="0")
        + f'<span style="font-size: 28px; font-weight: 800; letter-spacing: -1px">{amount} <span style="font-size: 13px; color: {MUTED}; letter-spacing: 1px">FCFA</span></span>'
        + "".join(f'<span style="font-size: 13px; color: {MUTED}">{l}</span>' for l in lines)
        + f'<div style="display: flex; gap: 10px; margin-top: 4px">{left}{right}</div>', pad="16px", gap=8)


add("Approvals.dc.html", "Validations", "".join([
    header("More.dc.html"), h1("Validations", "2 opérations attendent votre accord."),
    approval("FS", "#FDE3DB", "Fatou Sarr", "Aujourd'hui, 10:12", "Virement", "2 450 000",
             ["À Diallo Matériaux · Banque", "Motif : commande de bois rouge"], cta("Refuser", kind="secondary"), cta("Valider", "SendSuccess.dc.html")),
    approval("MD", TINT, "Moussa Diop", "Validée en 1er · 11:05", "Paie", "3 465 000",
             ["Paie d'octobre · 24 salariés · 31 oct."], cta("Détail", "BulkApproval.dc.html", "secondary"), cta("Valider", "BulkDone.dc.html")),
    note("Règle actuelle : double validation pour les virements de plus de 1 000 000 FCFA et pour toutes les paies.", "soft", "shield"),
]))

# ------------------------------------------------------------------ Coming soon
add("Intl.dc.html", "Virement international", "".join([
    header("More.dc.html"), h1("Virement international", "Payez vos fournisseurs hors de la zone UEMOA.", size=26, badge=True),
    panel(row(circ("globe", TINT), "Vers : France", "Euro (EUR)", chevron=True, last=True)),
    panel(f'<span style="font-size: 12px; color: {MUTED}">Vous envoyez</span><span style="font-size: 28px; font-weight: 800; letter-spacing: -1px">6 559 570 FCFA</span>', pad="14px 16px", gap=4),
    panel(f'<span style="font-size: 12px; color: {MUTED}">Le fournisseur reçoit</span><span style="font-size: 28px; font-weight: 800; letter-spacing: -1px">10 000,00 EUR</span>', pad="14px 16px", gap=4),
    kv([("Taux", "1 EUR = 655,957 FCFA (parité fixe)"), ("Frais", "Affichés avant l'envoi"), ("Délai", "Affiché avant l'envoi")]),
    note("Une pièce justificative (facture, contrat) est demandée pour chaque transfert hors UEMOA, selon la réglementation des changes de la BCEAO.", "soft", "file"),
    group("Pays envisagés", chips(["France · EUR", "Chine · CNY", "Émirats · AED", "Turquie · TRY", "Maroc · MAD", "Nigeria · NGN", "Ghana · GHS"], -1)),
]), btns=[soon_btn()])

add("PayLinks.dc.html", "Liens de paiement", "".join([
    header("More.dc.html"), h1("Liens de paiement", "Faites-vous payer par Wave, Orange Money, carte ou virement avec un simple lien.", size=26, badge=True),
    panel(field("Montant", "350 000", mode="numeric") + field("Description", "Acompte table en acajou, commande 212")
          + f'<div style="display: flex; gap: 6px; flex-wrap: wrap">{pill("Wave", "info")}{pill("Orange Money", "info")}{pill("Carte", "info")}{pill("Virement", "info")}</div>'
          + p("Frais : 1 % sur les paiements mobile money.", 12)
          + f'<div style="display: flex">{small_btn("Créer et partager", icon="share")}</div>', pad="16px", gap=12),
    group("Vos liens", panel(
        row(circ("link", WARNBG, WARN), "Acompte commande 212", "Créé aujourd'hui · envoyé sur WhatsApp", stacked_right(amt(350000), pill("En attente", "warn")))
        + row(circ("link", POSBG, POS), "Chaises salle de réunion", "Payé par Wave le 8 oct.", stacked_right(amt(780000), pill("Payé", "pos")))
        + row(circ("link", SOFT), "Devis 198", "Expiré le 30 sept.", stacked_right(amt(1150000), pill("Expiré")), last=True))),
]), btns=[soon_btn()])


def budget_row(init, bg, name, cat, spent, total, last=False):
    sep = "" if last else f"border-bottom: 1px solid {LINE}; "
    return (f'<div style="display: flex; flex-direction: column; gap: 8px; padding: 12px 0; {sep}"><div style="display: flex; align-items: center; gap: 12px">{av(init, bg, 36)}'
            f'<span style="display: flex; flex-direction: column; gap: 2px; flex: 1 1 auto; min-width: 0"><span style="font-size: 14px; font-weight: 700">{name}</span>'
            f'<span style="font-size: 12px; color: {MUTED}">{cat}</span></span><span style="font-size: 13px; font-weight: 800; flex: none">{money(spent)} '
            f'<span style="color: {MUTED}; font-weight: 600">/ {money(total)}</span></span></div>{progress(round(spent * 100 / total), h=6)}</div>')


add("BudgetCards.dc.html", "Cartes budget salariés", "".join([
    header("More.dc.html"), h1("Cartes budget", "Une carte par salarié avec un budget précis : transport, carburant, repas.", size=26, badge=True),
    panel(f'<span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 13px; color: {MUTED}">Budget d\'octobre</span>'
          f'<span style="font-size: 14px; font-weight: 800">157 500 <span style="color: {MUTED}; font-weight: 600">/ 240 000 FCFA</span></span></span>{progress(66)}'
          f'<span style="font-size: 12px; color: {MUTED}">Rechargé automatiquement le 1er de chaque mois</span>', pad="14px 16px", gap=10),
    group("Salariés", panel(budget_row("IF", TINT, "Ibrahima Fall", "Carburant", 75000, 100000) + budget_row("MD", "#FDE3DB", "Mariama Diop", "Transport", 18000, 40000)
                            + budget_row("MG", "#ECE6FD", "Modou Gueye", "Repas chantier", 52000, 60000) + budget_row("AS", "#DDF4EA", "Awa Sène", "Transport", 12500, 40000, last=True))),
    group("Règles", panel(row(circ("refresh", SOFT), "Recharge automatique", "Le 1er de chaque mois") + row(circ("tag", SOFT), "Dépenses autorisées", "Carburant, transport, restauration")
                          + row(circ("receipt", SOFT), "Justificatifs", "Photo du reçu demandée après chaque paiement", last=True))),
]), btns=[soon_btn()])

add("Accounting.dc.html", "Comptabilité", "".join([
    header("More.dc.html"), h1("Comptabilité", "Justificatifs, catégories et exports pour votre comptable, sans ressaisie.", size=26, badge=True),
    grid(2, stat("Justificatifs manquants", "7", WARN, "sur 64 opérations"), stat("Opérations catégorisées", "92 %", INK, "en octobre")),
    group("Octobre par catégorie", panel(row(circ("users", SOFT, INK, 36, 16), "Salaires", "24 salariés", amt(3465000)) + row(circ("brief", SOFT, INK, 36, 16), "Achats et matières", "Bois, quincaillerie", amt(1840000))
                                         + row(circ("truck", SOFT, INK, 36, 16), "Transport", "Livraisons", amt(1250000)) + row(circ("bolt", SOFT, INK, 36, 16), "Énergie", "Senelec", amt(84300), last=True))),
    group("TVA", panel(row(circ("percent", TINT), "TVA collectée en octobre", "Taux normal de 18 %", amt(612400), last=True))),
    panel(row(circ("download", SOFT), "Export pour le comptable", "Excel ou CSV · plan SYSCOHADA", chevron=True)
          + row(circ("user", SOFT), "Accès comptable", "Moussa Diop · lecture et exports", chevron=True, last=True)),
]), btns=[soon_btn()])


def product(title, sub, meta, icon, href=None):
    chev = '<span style="display: flex; flex: none">' + ic("chev_r", 18, "2.2") + '</span>' if href else ""
    inner = (f'<span style="display: flex; align-items: center; gap: 12px">{circ(icon, TINT)}<span style="font-size: 16px; font-weight: 800; flex: 1 1 auto">{title}</span>'
             f'{chev}</span>'
             f'<span style="font-size: 13px; line-height: 1.45; color: {MUTED}">{sub}</span><span>{pill(meta)}</span>')
    st = f"border-radius: 22px; padding: 16px; background: {GLASS}; border: {BORDER}; box-shadow: {SH_CARD}; display: flex; flex-direction: column; gap: 8px; color: {INK}; text-decoration: none"
    return f'<a href="{href}" style="{st}">{inner}</a>' if href else f'<div style="{st}">{inner}</div>'


add("Financing.dc.html", "Financement", "".join([
    header("More.dc.html"),
    h1("Financement", "Un seul prix : 0,063 % par jour sur le montant utilisé, soit 23 % par an (TEG). Pas de frais de dossier.", size=26, badge=True),
    product("Affacturage", "Recevez 80 à 90 % de vos factures clients sans attendre l'échéance.", "30 à 90 jours · 1,9 % pour 30 jours", "percent", "Factoring.dc.html"),
    product("Financement de factures", "Avancez sur une facture ; votre client vous paie comme d'habitude.", "Remboursement automatique", "file", "Factoring.dc.html"),
    product("Prêt équipement", "Véhicules, machines, téléphones : de 1 à 50 millions de FCFA.", "6 à 24 mois", "truck", "LoanOffer.dc.html"),
    product("Pont de paie", "Payez les salaires à l'heure, même si un client paie en retard.", "Jusqu'à 1 mois de paie · 45 jours", "users"),
    product("Ligne de crédit", "Une réserve de trésorerie calculée sur vos encaissements.", "Après 6 mois d'activité", "trend"),
    note("Crédits accordés par notre partenaire de microfinance agréé. Le coût en FCFA est affiché avant chaque utilisation.", "soft", "shield"),
]), btns=[soon_btn()])

add("LoanOffer.dc.html", "Prêt équipement", "".join([
    header("Financing.dc.html", close="More.dc.html"), h1("Prêt équipement", "Simulez votre prêt. Mensualités fixes, sans frais de dossier.", size=26, badge=True),
    big_amount("2 000 000", label="Montant"),
    chips(["1 000 000", "2 000 000", "5 000 000", "10 000 000"], 1),
    stack(label("Durée"), segmented(["6 mois", "12 mois", "18 mois", "24 mois"], 0), gap=8),
    kv([("Mensualité", "356 048 FCFA"), ("Coût total du crédit", "136 288 FCFA"), ("Taux (TEG)", "23 % par an"), ("Total remboursé", "2 136 288 FCFA")]),
    note("Prélèvement automatique le 5 de chaque mois sur le compte principal. Remboursement anticipé sans pénalité.", "soft", "calendar"),
]), btns=[soon_btn()])

add("Factoring.dc.html", "Affacturage", "".join([
    header("Financing.dc.html", close="More.dc.html"), h1("Affacturage", "Transformez vos factures clients en trésorerie.", size=26, badge=True),
    segmented(["Affacturage", "Financement de factures"], 0),
    p("Affacturage : votre client paie la facture sur votre compte Tabax à l'échéance. Financement de factures : il vous paie comme d'habitude et le remboursement est automatique.", 13),
    panel(row(circ("file", TINT), "Facture F-2026-131", "Société Immobilière Keur Gorgui · échéance 11 déc.", amt(4800000), last=True)),
    kv([("Avance (85 %)", "4 080 000 FCFA"), ("Durée", "60 jours"), ("Coût (0,063 % par jour)", "154 224 FCFA"), ("Reversé au paiement", "565 776 FCFA")]),
    group("Comment ça marche", steps([("Importez la facture", "PDF ou photo"), ("Nous vérifions votre client", "Sous 48 h"),
                                      ("Vous recevez 85 %", "Sur le compte principal"), ("Votre client paie à l'échéance", "Le solde vous est reversé")])),
]), btns=[soon_btn()])

# ------------------------------------------------------------------ canvas index
ROWS = [
    ("rHome", "Home and tabs", ["Main", "Payments", "TxDetail", "Cards", "CardDetail", "NewCard", "More", "Notifications", "Settings"]),
    ("rOnb", "Account opening (KYB + KYC), then approval and plan", ["Welcome", "SignUp", "Otp", "Company", "CompanyDocs", "Director", "Owners", "Review", "Approved", "Plan"]),
    ("rAcc", "Accounts and bank details", ["Accounts", "AccountDetails", "NewSubAccount", "Statements"]),
    ("rTop", "Top up: Wave, Orange Money, card, bank transfer, cash", ["TopUp", "TopUpWave", "TopUpConfirm", "TopUpSuccess", "TopUpCard", "TopUpBank", "CashDeposit"]),
    ("rSend", "Send money", ["Send", "NewRecipient", "SendAmount", "SendReview", "SendSuccess"]),
    ("rBulk", "Bulk payouts and payroll", ["Bulk", "BulkNew", "BulkPick", "BulkReview", "BulkApproval", "BulkDone"]),
    ("rBills", "Bill payments", ["Bills", "BillPay", "BillSuccess"]),
    ("rTeam", "Team, permissions and approvals", ["Team", "Invite", "Permissions", "Approvals"]),
    ("rSoon", "Coming soon: international, payment links, budget cards, accounting, financing", ["Intl", "PayLinks", "BudgetCards", "Accounting", "Financing", "LoanOffer", "Factoring"]),
]


def index(created_at):
    boards, order, notes = {}, [], {}
    for r, (rid, title, names) in enumerate(ROWS):
        y = r * 1244
        for i, n in enumerate(names):
            f = f"{n}.dc.html"
            assert f in S, f
            boards[f] = {"x": i * 470, "y": y, "w": 390, "h": 844, "title": TITLES[f], "radius": 36, "is_interactive": True}
            order.append(f)
        notes[rid] = {"x": 0, "y": y - 300, "text": title, "kind": "title1", "maxW": max(len(names) * 470 - 80, 1330)}
    notes["nPlay"] = {"x": 9 * 470, "y": 0, "w": 380, "fill": "blue",
                      "text": "Clickable prototype: open 'Accueil' and press Play, then tap through. Every button that leads somewhere is linked: tabs, actions, accounts, payroll, bills, cards, team, and the 'Bientôt' screens.\n\nStart the sign-up flow from 'Bienvenue' (second row).\n\nStyle: Tabax 18 (white, sky blue, Epilogue). The sky blue can be changed on any screen with Tweaks."}
    notes["nData"] = {"x": 9 * 470, "y": 1244, "w": 380, "fill": "yellow",
                      "text": "Prices come from the business model v2: plans at 9 900 / 29 900 / 79 900 FCFA a month, physical card 5 000 FCFA, 1 % on foreign card spending and on mobile money payment links, credit at 0,063 % a day (23 % a year).\n\nPlaceholders in [brackets] (partner bank, BIC) are still to be decided. Names, companies and amounts are sample data."}
    missing = set(S) - set(order)
    assert not missing, missing
    return {"v": 3, "createdOnFiles": {"v": 1, "at": created_at}, "title": "Tabax App", "launch": {"view": "canvas"}, "pages": [],
            "boards": boards, "order": order, "notes": notes, "designSystems": []}


def links_ok():
    import re as _re
    bad = []
    for f, h in S.items():
        for href in _re.findall(r'href="([^"#][^"]*\.dc\.html)"', h):
            if href not in S:
                bad.append((f, href))
    assert not bad, bad


if __name__ == "__main__":
    root = sys.argv[1]
    os.makedirs(os.path.join(root, "project"), exist_ok=True)
    links_ok()
    for f, h in S.items():
        open(os.path.join(root, "project", f), "w").write(h)
    created = sys.argv[2] if len(sys.argv) > 2 else "2026-10-12T12:00:00Z"
    idx_path = os.path.join(root, "project", "canvas.json")
    json.dump(index(created), open(idx_path, "w"), ensure_ascii=False, indent=2)
    print(len(S), "screens")
    for rid, title, names in ROWS:
        print(rid, " ".join(names))
