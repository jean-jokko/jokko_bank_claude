"""Kelen web app: the same flows, features and content as the mobile app, laid out for desktop (Kelen V5 teal)."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from web_lib import *  # noqa: F401,F403

S, TITLES = {}, {}


def add(file, title, body):
    S[file] = web_page(f"Kelen — {title}", body)
    TITLES[file] = title


def soon_btn():
    return btn("Me prévenir au lancement", None, "primary", "bell")


def tx_icon(icon, bg, fg=INK):
    return circ(icon, bg, fg, 36, 16)


# ================================================================== Home and tabs
def balance_card():
    return card(
        f'<div style="display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 20px">'
        f'<div style="display: flex; flex-direction: column; gap: 6px">{eyebrow("Solde total · 3 comptes")}'
        f'<span style="display: flex; align-items: baseline; gap: 12px"><span style="font-size: 52px; font-weight: 500; letter-spacing: -2px; line-height: 1.05; font-variant-numeric: proportional-nums">12 480 350</span>{fcfa_tag(13)}</span>'
        f'<a href="AccountDetails.dc.html" style="align-self: flex-start; margin-top: 6px; height: 34px; padding: 0 14px; border-radius: 17px; background: {SOFT}; color: {INK}; font-size: 12px; font-weight: 600; '
        f'display: inline-flex; align-items: center; gap: 8px; text-decoration: none">IBAN SN08 SN01 •••• 3035 {ic("copy", 14, "1.8")}</a></div>'
        f'<div style="display: flex; flex-wrap: wrap; gap: 10px">{btn("Recharger", "TopUp.dc.html", "primary", "plus")}{btn("Envoyer", "Send.dc.html", "secondary", "send")}'
        f'{btn("Paie groupée", "Bulk.dc.html", "secondary", "users")}{btn("Factures", "Bills.dc.html", "secondary", "receipt")}</div></div>',
        pad="26px 28px", gap=10, radius=28)


def acct_tile(name, color, bal, sub, href):
    return (f'<a href="{href}" style="box-sizing: border-box; border-radius: 20px; padding: 16px 18px; background: {GLASS}; border: {BORDER}; box-shadow: {SH_CARD}; '
            f'display: flex; flex-direction: column; gap: 6px; text-decoration: none; color: {INK}; min-width: 0">'
            f'<span style="display: flex; align-items: center; gap: 8px; font-size: 13px; color: {MUTED}"><span style="width: 8px; height: 8px; border-radius: 4px; background: {color}"></span>{name}</span>'
            f'<span style="font-size: 22px; font-weight: 500; letter-spacing: -0.6px">{bal} <span style="font-size: 12px; font-weight: 600; color: {MUTED}; letter-spacing: 1px">FCFA</span></span>'
            f'<span style="font-size: 12px; color: {MUTED}">{sub}</span></a>')


ACTIVITY = [
    ("receive", POSBG, POS, "Recharge Wave", "Mobile money · Wave", "Aujourd'hui, 09:14", "Principal", 500000),
    ("bolt", TINT, INK, "Facture Senelec", "Facture · contrat 2310 4471 902", "Aujourd'hui, 08:02", "Principal", -84300),
    ("receive", POSBG, POS, "Virement reçu", "SCI Fann Résidence · facture F-2026-127", "Hier, 16:40", "Principal", 2400000),
    ("card", SOFT, INK, "Google Ads", "Carte •••• 9012 · payé en USD", "Hier, 11:02", "Principal", -51712),
    ("send", SOFT, INK, "Imprimerie Ba", "Virement · flyers salon", "Hier, 09:30", "Principal", -145000),
    ("send", SOFT, INK, "Cissé Logistique SARL", "Virement · facture F-2026-118", "10 oct., 15:12", "Principal", -1250000),
    ("card", SOFT, INK, "Station Mermoz", "Carte •••• 5528 · carburant", "10 oct., 08:47", "Principal", -35000),
]


def activity_table(rows, status=True):
    trs = []
    for icon, bg, fg, t, s, d, acc, n in rows:
        r = [cell_main(tx_icon(icon, bg, fg), t, s, "TxDetail.dc.html"), muted(acc), muted(d)]
        if status:
            r.append(pill("Reçu" if n > 0 else "Payé", "pos" if n > 0 else "neutral"))
        r.append(money_cell(n))
        trs.append(r)
    heads = ["Opération", "Compte", "Date"] + (["Statut"] if status else []) + ["Montant"]
    aligns = ["left", "left", "left"] + (["left"] if status else []) + ["right"]
    return table(heads, trs, aligns)


add("Main.dc.html", "Accueil", shell("Main", "Bonjour Aïssatou", "".join([
    balance_card(),
    cols(
        stack(card_title("Comptes", tlink("Tout voir", "Accounts.dc.html")),
              autogrid(acct_tile("Principal", INK, "8 210 000", "Compte courant · cartes et virements", "AccountDetails.dc.html"),
                       acct_tile("Salaires", ACC, "3 500 000", "Alimenté le 25 depuis Principal", "Accounts.dc.html"),
                       acct_tile("Fournisseurs", "#9AA1AD", "770 350", "Paiements fournisseurs", "Accounts.dc.html"), min_w=200, gap=12), gap=12)
        + stack(card_title("Activité récente", tlink("Tout voir", "Payments.dc.html")), activity_table(ACTIVITY[:5]), gap=12),
        card(card_title("À faire")
             + panel(row(circ("calendar", TINT), "Paie d'octobre · 31 oct.", "24 salariés · 3 465 000 FCFA · prête", href="BulkReview.dc.html", chevron=True)
                     + row(circ("shield", WARNBG, WARN), "2 validations en attente", "Virement et paie d'octobre", pill("2", "warn"), href="Approvals.dc.html", chevron=True)
                     + row(circ("bolt", WARNBG, WARN), "Senelec à payer", "126 450 FCFA · échéance 20 oct.", href="BillPay.dc.html", chevron=True)
                     + row(circ("wallet", SOFT), "Choisir votre offre", "Avant le 5 novembre", pill("À choisir", "warn"), href="Plan.dc.html", chevron=True, last=True), pad="0 14px"),
             pad="20px", gap=12)
        + card(card_title("Cartes", tlink("Gérer", "Cards.dc.html"))
               + f'<span style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px"><span style="font-size: 13px; color: {MUTED}">Dépensé en octobre</span>'
               f'<span style="font-size: 14px; font-weight: 600">659 200 <span style="color: {MUTED}; font-weight: 500">FCFA</span></span></span>{progress(38)}'
               + muted("5 cartes actives · 1 gelée"), pad="20px", gap=12)
        + card(card_title("Entrées et sorties · octobre")
               + f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px">'
               f'<span style="display: flex; flex-direction: column; gap: 4px">{muted("Entrées")}<span style="font-size: 20px; font-weight: 500; color: {POS}">+4 870 000</span></span>'
               f'<span style="display: flex; flex-direction: column; gap: 4px">{muted("Sorties")}<span style="font-size: 20px; font-weight: 500">−3 912 400</span></span></div>', pad="20px", gap=12),
        basis=(620, 320)),
]), sub="Atelier Ndiaye SARL · Dakar"))

payments_top = hrow(date_btn("Du 1er au 12 octobre 2026"), chips(["Tout", "Entrées", "Sorties", "Cartes", "Paie", "Factures"], 0),
                    f'<span style="margin-left: auto">{btn("Exporter", None, "secondary", "download", "s")}</span>', gap=12)

add("Payments.dc.html", "Paiements", shell("Payments", "Paiements", "".join([
    autogrid(stat_card("Entrées · octobre", "+4 870 000", POS, "FCFA"), stat_card("Sorties · octobre", "−3 912 400", INK, "FCFA"),
             stat_card("Opérations", "64", INK, "dont 7 sans justificatif"), min_w=220),
    payments_top,
    activity_table(ACTIVITY),
]), right=search_field("Rechercher une opération", 320) + bell() + btn("Envoyer", "Send.dc.html", "primary", "send", "s")))

tx_detail = card(
    hrow(f'<span style="font-size: 13px; font-weight: 600; color: {MUTED}">Détail de l\'opération</span>',
         f'<span style="margin-left: auto; display: flex; gap: 8px">{icon_button("share", "Partager")}{icon_link("x", "Payments.dc.html", "Fermer")}</span>')
    + f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 8px; padding: 6px 0">{circ("bolt", TINT, INK, 56, 24)}'
      f'<span style="font-size: 17px; font-weight: 600">Facture Senelec</span>'
      f'<span style="display: flex; align-items: baseline; gap: 8px"><span style="font-size: 38px; font-weight: 500; letter-spacing: -1.5px">−84 300</span>{fcfa_tag()}</span>{pill("Payée", "pos")}</div>'
    + kv([("Date", "Aujourd'hui, 08:02"), ("Depuis", "Compte principal"), ("Contrat", "2310 4471 902"), ("Référence", "KLN-FAC-77310"), ("Payée par", "Aïssatou Ndiaye")])
    + stack(label("Catégorie"), chips(["Énergie", "Loyer et charges", "Autre"], 0), gap=8)
    + stack(label("Justificatif"), panel(row(circ("file", POSBG, POS), "Reçu Senelec", "Ajouté automatiquement · PDF", btn("Télécharger", None, "secondary", "download", "s"), last=True)), gap=8)
    + field("Note", placeholder="Ajouter une note pour votre comptable"),
    pad="20px", gap=16)

add("TxDetail.dc.html", "Détail d'une opération", shell("Payments", "Paiements", "".join([
    payments_top,
    cols(activity_table(ACTIVITY, status=False), tx_detail, basis=(560, 360)),
]), right=search_field("Rechercher une opération", 320) + bell() + btn("Envoyer", "Send.dc.html", "primary", "send", "s")))

CARDS = [("Aïssatou Ndiaye", "4821", "Carte physique", True, "Carte principale", 412300, 1500000, False),
         ("Moussa Diop", "9012", "Virtuelle · Publicité en ligne", False, "Publicité en ligne", 184500, 300000, False),
         ("Aïssatou Ndiaye", "3370", "Virtuelle · Logiciels", False, "Logiciels", 62000, 150000, False),
         ("Fatou Sarr", "6614", "Virtuelle · Fournitures", False, "Fournitures", 0, 250000, False),
         ("Ibrahima Fall", "5528", "Physique · gelée", True, "Carburant atelier", 0, 200000, True)]


def card_tile(holder, last4, lbl, dark, name, spent, limit, frozen):
    status = pill("Gelée") if frozen else f'<span style="font-size: 13px; font-weight: 600">{money(spent)} <span style="color: {MUTED}; font-weight: 500">/ {money(limit)}</span></span>'
    return (f'<a href="CardDetail.dc.html" style="display: flex; flex-direction: column; gap: 12px; text-decoration: none; color: {INK}; min-width: 0">'
            f'{bank_card(holder, last4, lbl, dark, small=True)}'
            f'<span style="display: flex; align-items: center; justify-content: space-between; gap: 8px"><span style="display: flex; flex-direction: column; gap: 2px">'
            f'<span style="font-size: 14px; font-weight: 600">{name}</span><span style="font-size: 12px; color: {MUTED}">•••• {last4} · {holder}</span></span>{status}</span>'
            f'{"" if frozen else progress(round(spent * 100 / limit), h=6)}</a>')


add("Cards.dc.html", "Cartes", shell("Cards", "Cartes", "".join([
    hrow(segmented(["Toutes · 5", "Physiques · 2", "Virtuelles · 3"], 0), f'<span style="margin-left: auto">{btn("Nouvelle carte", "NewCard.dc.html", "primary", "plus", "s")}</span>'),
    card(f'<span style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px"><span style="font-size: 13px; color: {MUTED}">Dépensé en octobre, toutes cartes</span>'
         f'<span style="font-size: 14px; font-weight: 600">659 200 <span style="color: {MUTED}; font-weight: 500">FCFA</span></span></span>{progress(38)}'
         + muted("Plafonds mensuels remis à zéro le 1er novembre"), pad="18px 20px", gap=10),
    autogrid(*[card_tile(*c) for c in CARDS], min_w=280, gap=24),
    panel(row(circ("tag", TINT), "Cartes budget pour vos salariés", "Transport, carburant, repas", soon_badge(), href="BudgetCards.dc.html", last=True)),
])))


def card_action(label_, icon):
    return (f'<button style="all: unset; cursor: pointer; box-sizing: border-box; flex: 1 1 0; min-width: 96px; border-radius: 18px; padding: 14px 8px; background: {GLASS}; border: {BORDER}; box-shadow: {SH_BTN}; '
            f'display: flex; flex-direction: column; align-items: center; gap: 8px; font-size: 13px; font-weight: 600">{ic(icon, 20, "1.6")}{label_}</button>')


add("CardDetail.dc.html", "Détail d'une carte", shell("Cards", "Carte principale", cols(
    stack(f'<div style="max-width: 420px">{bank_card("Aïssatou Ndiaye", "4821", "Carte physique")}</div>',
          f'<div style="display: flex; flex-wrap: wrap; gap: 10px; max-width: 420px">{card_action("Geler", "snow")}{card_action("Infos", "eye")}{card_action("Code PIN", "lock")}{card_action("Plafonds", "sliders")}</div>',
          card(f'<span style="display: flex; justify-content: space-between; align-items: baseline; gap: 8px"><span style="font-size: 13px; color: {MUTED}">Plafond mensuel</span>'
               f'<span style="font-size: 14px; font-weight: 600">412 300 <span style="color: {MUTED}; font-weight: 500">/ 1 500 000 FCFA</span></span></span>{progress(27)}'
               + muted("Acceptée partout où Visa est acceptée"), pad="18px 20px", gap=10), gap=18),
    stack(card(card_title("Réglages") + panel(toggle_row("Paiements en ligne", "Sites et applications", True) + toggle_row("Sans contact", "Paiements en magasin", True)
                                              + toggle_row("Retraits au distributeur", "Désactivés pour cette carte", False)
                                              + toggle_row("Paiements hors UEMOA", "Publicité en ligne, logiciels, voyages", True, last=True)), pad="20px", gap=12),
          card(card_title("Dernières dépenses") + panel(row(tx_icon("card", SOFT), "Google Ads", "Payé en USD · 10 oct.", amt(-51712))
                                                        + row(tx_icon("card", SOFT), "Quincaillerie Médina", "Fournitures · 9 oct.", amt(-78500))
                                                        + row(tx_icon("card", SOFT), "Station Mermoz", "Carburant · 8 oct.", amt(-35000), last=True)), pad="20px", gap=12), gap=18),
    basis=(420, 420)), sub="Physique •••• 4821 · Aïssatou Ndiaye", back="Cards.dc.html",
    right=bell() + btn("Plus d'options", None, "secondary", "dots", "s")))


def option(title, sub, icon, selected=False, href=None):
    st = (f"border: 1.5px solid {ACC}; background: #FFFFFF; box-shadow: 0 0 0 3px color-mix(in srgb, {ACC} 16%, transparent)" if selected
          else f"border: {BORDER}; background: {GLASS}; box-shadow: {SH_CARD}")
    radio = (f'<span style="width: 22px; height: 22px; border-radius: 11px; box-sizing: border-box; border: 1.5px solid {ACC if selected else "#C5C9D0"}; background: {ACC if selected else "#FFFFFF"}; '
             f'color: #FFFFFF; display: flex; align-items: center; justify-content: center; flex: none">{ic("check", 12, "2.4") if selected else ""}</span>')
    inner = (f'{circ(icon, TINT if selected else SOFT)}<span style="display: flex; flex-direction: column; gap: 2px; flex: 1 1 auto; min-width: 0">'
             f'<span style="font-size: 15px; font-weight: 600">{title}</span><span style="font-size: 13px; line-height: 1.4; color: {MUTED}">{sub}</span></span>{radio}')
    base = f"box-sizing: border-box; border-radius: 20px; padding: 16px; {st}; display: flex; align-items: center; gap: 14px; min-width: 0"
    if href:
        return f'<a href="{href}" style="{base}; color: {INK}; text-decoration: none">{inner}</a>'
    return f'<button aria-pressed="{"true" if selected else "false"}" style="all: unset; cursor: pointer; {base}">{inner}</button>'


def acct_from(name="Depuis : compte principal", sub="8 210 000 FCFA disponibles", color=INK, last=True):
    dot = f'<span style="width: 10px; height: 10px; border-radius: 5px; background: {color}; flex: none; margin: 0 15px"></span>'
    return row(dot, name, sub, chevron=True, last=last)


add("NewCard.dc.html", "Nouvelle carte", flow("Nouvelle carte", "".join([
    flow_h1("Nouvelle carte", "Virtuelle tout de suite, ou physique livrée à l'entreprise."),
    autogrid(option("Carte virtuelle", "Gratuite, prête tout de suite", "card", True),
             option("Carte physique", "Livrée à l'entreprise. La première est offerte, 6 500 FCFA les suivantes.", "truck"), min_w=260, gap=12),
    field("Nom de la carte", "Fournitures bureau"),
    panel(row(av("FS", "#FDE3DB", 36), "Titulaire", "Fatou Sarr · assistante", chevron=True) + acct_from("Compte", "Principal")),
    stack(label("Plafond mensuel"), chips(["100 000", "250 000", "500 000", "Autre"], 1), gap=8),
    panel(toggle_row("Paiements en ligne uniquement", "Ni sans contact, ni retrait", True, last=True)),
]), btn("Annuler", "Cards.dc.html", "secondary") + btn("Créer la carte", "CardDetail.dc.html"), close="Cards.dc.html", back="Cards.dc.html"))

add("Notifications.dc.html", "Notifications", shell("Main", "Notifications", stack(
    hrow(segmented(["Toutes", "À valider · 2", "Paiements", "Comptes"], 0), f'<span style="margin-left: auto">{btn("Tout marquer comme lu", None, "secondary", "check", "s")}</span>'),
    stack(eyebrow("Aujourd'hui"), panel(
        row(circ("clock", WARNBG, WARN), "Paie d'octobre à valider", "Moussa Diop a validé, il manque votre accord · 11:05", btn("Valider", "BulkApproval.dc.html", "primary", None, "s"))
        + row(circ("shield", TINT), "Virement à valider", "2 450 000 FCFA vers Diallo Matériaux, préparé par Fatou Sarr · 10:12", btn("Voir", "Approvals.dc.html", "secondary", None, "s"))
        + row(circ("receive", POSBG, POS), "Recharge Wave reçue", "+500 000 FCFA sur le compte principal · 09:14", href="TxDetail.dc.html", chevron=True, last=True)), gap=8),
    stack(eyebrow("Cette semaine"), panel(
        row(circ("alert", ERRBG, ERR), "Paiement refusé", "Carte Publicité en ligne : plafond mensuel atteint · jeudi", href="CardDetail.dc.html", chevron=True)
        + row(circ("trend", TINT), "Vous approchez d'une limite", "80 % du mobile money inclus utilisé ce mois-ci · mercredi", btn("Voir les offres", "Plan.dc.html", "secondary", None, "s"))
        + row(circ("file", SOFT), "Relevé de septembre disponible", "Compte principal · mardi", href="Statements.dc.html", chevron=True)
        + row(circ("drop", TINT), "Facture Sen'Eau", "41 200 FCFA à payer avant le 5 novembre · lundi", href="Bills.dc.html", chevron=True)
        + row(circ("check", POSBG, POS), "Votre compte est ouvert", "IBAN prêt · choisissez votre offre avant le 5 novembre · 5 oct.", href="Approved.dc.html", chevron=True, last=True)), gap=8),
    gap=20), back="Main.dc.html", right=bell()))

add("Settings.dc.html", "Profil et sécurité", shell("Settings", "Paramètres", "".join([
    card(hrow(av("AN", ACC, 64), stack(f'<span style="font-size: 22px; font-weight: 600">Aïssatou Ndiaye</span>', p("Gérante · administratrice · +221 77 123 45 67", 14), gap=4),
              f'<span style="margin-left: auto">{btn("Modifier le profil", None, "secondary", "edit", "s")}</span>', gap=18), pad="22px 24px"),
    autogrid(
        card(card_title("Entreprise") + panel(row(circ("building", SOFT), "Atelier Ndiaye SARL", "NINEA 006543219 2G3", chevron=True)
                                              + row(circ("wallet", SOFT), "Offre et abonnement", "Premier mois offert jusqu'au 5 novembre · offre à choisir", pill("À choisir", "warn"), href="Plan.dc.html", chevron=True, last=True)), pad="20px", gap=12),
        card(card_title("Sécurité") + panel(row(circ("lock", SOFT), "Code secret", "Pour valider les paiements", chevron=True)
                                            + toggle_row("Double authentification", "Code par SMS à chaque connexion web", True, lead=circ("phone", SOFT))
                                            + row(circ("face", SOFT), "Appareils connectés", "2 appareils · ce navigateur", chevron=True, last=True)), pad="20px", gap=12),
        card(card_title("Préférences") + panel(row(circ("globe", SOFT), "Langue", "Français", chevron=True)
                                               + toggle_row("Notifications", "Paiements, validations, factures", True, last=True, lead=circ("bell", SOFT))), pad="20px", gap=12),
        card(card_title("Aide") + panel(row(circ("msg", SOFT), "Aide sur WhatsApp", "Un conseiller vous répond", chevron=True)
                                        + row(circ("logout", ERRBG, ERR), "Se déconnecter", None, href="Welcome.dc.html", last=True)), pad="20px", gap=12),
        min_w=420, gap=20),
]), sub="Profil, sécurité et préférences", right=bell()))

# ================================================================== Account opening (KYB + KYC)
def check_item(t):
    return (f'<div style="display: flex; gap: 10px; align-items: center"><span style="width: 24px; height: 24px; border-radius: 12px; background: {ACC}; color: #FFFFFF; '
            f'display: flex; align-items: center; justify-content: center; flex: none">{ic("check", 14, "2.2")}</span><span style="font-size: 15px; font-weight: 500">{t}</span></div>')


add("Welcome.dc.html", "Bienvenue", onboarding("".join([
    hrow(f'<span style="margin-left: auto"><button style="all: unset; cursor: pointer; font-size: 13px; font-weight: 600; padding: 8px 14px; border-radius: 16px; background: #FFFFFF; border: {FIELD_BORDER}">Français</button></span>'),
    f'<div style="max-width: 400px">{bank_card("Atelier Ndiaye SARL", "4821", "Carte entreprise")}</div>',
    h1("Ouvrez votre compte pro en ligne", "Sans passer en agence. Un seul abonnement, sans frais cachés.", size=34),
    stack(check_item("Ouverture en ligne, sans passer en agence"), check_item("Salaires payés sur banque, Wave ou Orange Money"), check_item("Cartes Visa physiques et virtuelles"), gap=12),
]), btn("J'ai déjà un compte", "Main.dc.html", "secondary") + btn("Ouvrir un compte", "SignUp.dc.html"), close=None))

consent = (f'<button aria-pressed="true" style="all: unset; cursor: pointer; display: flex; gap: 10px; align-items: flex-start">'
           f'<span style="width: 22px; height: 22px; box-sizing: border-box; border-radius: 7px; background: {ACC}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; flex: none">{ic("check", 13, "2.4")}</span>'
           f'<span style="font-size: 13px; line-height: 1.45; color: {MUTED}">J\'accepte les conditions générales et la politique de confidentialité de Kelen.</span></button>')

add("SignUp.dc.html", "Inscription", onboarding("".join([
    h1("Votre numéro de téléphone", "Nous vous envoyons un code par SMS. Ce numéro servira à vous connecter."),
    field("Téléphone portable", "77 123 45 67", prefix="+221", mode="tel"),
    field("E-mail professionnel", "aissatou@atelierndiaye.sn", typ="email"),
    consent,
]), btn("Recevoir le code", "Otp.dc.html"), back="Welcome.dc.html", close=None))

boxes = "".join(
    f'<input aria-label="Chiffre {i + 1}" inputmode="numeric" value="{d}" style="width: 56px; height: 64px; box-sizing: border-box; border-radius: 16px; '
    f'border: {"1.5px solid " + ACC if i == 4 else FIELD_BORDER}; text-align: center; font: inherit; font-size: 26px; font-weight: 500; color: {INK}; outline: none; background: #FFFFFF">'
    for i, d in enumerate(["4", "8", "2", "1", "", ""]))
add("Otp.dc.html", "Code SMS", onboarding("".join([
    h1("Entrez le code reçu par SMS", "Envoyé au +221 77 123 45 67."),
    f'<div style="display: flex; gap: 10px; flex-wrap: wrap">{boxes}</div>',
    f'<div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px"><span style="font-size: 13px; color: {MUTED}">Nouveau code dans <strong style="color: {INK}">0:42</strong></span>'
    f'{tlink("Changer de numéro", "SignUp.dc.html")}</div>',
]), btn("Vérifier", "Company.dc.html"), back="SignUp.dc.html"))

add("Company.dc.html", "Entreprise", onboarding("".join([
    stepper(1, 4, "Entreprise"),
    h1("Votre entreprise", "Indiquez votre NINEA : nous retrouvons votre entreprise quand c'est possible."),
    field("NINEA ou RCCM", "006543219 2G3", icon="search"),
    panel(row(circ("check", POSBG, POS), "Atelier Ndiaye SARL", "Dakar · vérifiez les informations ci-dessous", last=True)),
    autogrid(field("Raison sociale", "Atelier Ndiaye SARL"), field("RCCM", "SN-DKR-2019-B-12345"), min_w=240, gap=14),
    stack(label("Forme juridique"), chips(["SARL", "SUARL", "SA", "GIE", "Entreprise individuelle"], 0), gap=8),
    autogrid(field("Secteur d'activité", "Menuiserie et ameublement"), stack(label("Nombre de salariés"), chips(["1 à 10", "11 à 50", "51 et plus"], 1), gap=8), min_w=240, gap=14),
    field("Adresse du siège", "Route de Rufisque, zone industrielle, Dakar"),
]), btn("Continuer", "CompanyDocs.dc.html"), step=1, back="Otp.dc.html"))


def doc_row(title, sub, state, last=False):
    if state == "done":
        return row(circ("file", POSBG, POS), title, sub, pill("Ajouté", "pos"), last=last)
    if state == "opt":
        return row(circ("file", SOFT), title, sub, pill("Facultatif"), last=last)
    return row(circ("file", SOFT), title, sub, btn("Ajouter", None, "secondary", "upload", "s"), last=last)


add("CompanyDocs.dc.html", "Documents", onboarding("".join([
    stepper(2, 4, "Documents"),
    h1("Documents de l'entreprise", "PDF ou photo lisible, 10 Mo maximum par fichier. Glissez-déposez vos fichiers ou cliquez sur Ajouter."),
    panel(doc_row("Statuts signés", "statuts_atelier_ndiaye.pdf · 2,4 Mo", "done")
          + doc_row("Extrait RCCM", "Moins de 3 mois · rccm_2026.pdf", "done")
          + doc_row("Attestation NINEA", "PDF ou photo", "todo")
          + doc_row("Justificatif d'adresse", "Facture Senelec ou Sen'Eau de moins de 3 mois", "todo")
          + doc_row("PV de nomination du gérant", "Seulement s'il n'est pas dans les statuts", "opt", last=True)),
    note("Vos documents sont chiffrés et vus uniquement par notre équipe conformité.", "soft", "lock"),
]), btn("Continuer", "Director.dc.html"), step=2, back="Company.dc.html"))


def photo_tile(t, done):
    if done:
        return (f'<div style="border-radius: 18px; border: {BORDER}; background: {SOFT}; aspect-ratio: 1.5; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px">'
                f'{circ("check", POSBG, POS, 36, 16)}<span style="font-size: 14px; font-weight: 600">{t}</span><span style="font-size: 12px; color: {MUTED}">Photo ajoutée</span></div>')
    return (f'<button style="all: unset; cursor: pointer; box-sizing: border-box; border-radius: 18px; border: 1.5px dashed #B3B9C2; background: #FFFFFF; aspect-ratio: 1.5; display: flex; '
            f'flex-direction: column; align-items: center; justify-content: center; gap: 6px">{circ("upload", TINT, INK, 36, 16)}<span style="font-size: 14px; font-weight: 600">{t}</span>'
            f'<span style="font-size: 12px; color: {MUTED}">Importer ou prendre une photo</span></button>')


add("Director.dc.html", "Identité du dirigeant", onboarding("".join([
    stepper(3, 4, "Dirigeant"),
    h1("Votre identité", "Aïssatou Ndiaye, gérante. Une pièce d'identité et un selfie vidéo."),
    segmented(["Carte d'identité CEDEAO", "Passeport"], 0),
    f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px">{photo_tile("Recto", True)}{photo_tile("Verso", False)}</div>',
    panel(row(circ("face", TINT), "Selfie vidéo de 5 secondes", "Sur ce navigateur avec la webcam, ou sur votre téléphone par QR code", btn("Commencer", None, "primary", None, "s"), last=True)),
    note("Bonne lumière, pas de reflet, les quatre coins de la carte visibles.", "soft", "info"),
]), btn("Continuer", "Owners.dc.html"), step=3, back="CompanyDocs.dc.html"))

add("Owners.dc.html", "Bénéficiaires effectifs", onboarding("".join([
    stepper(4, 4, "Actionnaires"),
    h1("Bénéficiaires effectifs", "Toute personne qui détient au moins 25 % du capital ou qui contrôle l'entreprise."),
    panel(row(av("AN", ACC, 40), "Aïssatou Ndiaye", "Vous · gérante · identité vérifiée", right_text("60 %", INK, 16, 600))
          + row(av("CN", SOFT), "Cheikh Ndiaye", "Lien de vérification envoyé par SMS", right_text("40 %", INK, 16, 600), last=True)),
    stack(f'<span style="display: flex; justify-content: space-between; font-size: 13px"><span style="color: {MUTED}">Capital déclaré</span><strong>100 %</strong></span>', progress(100), gap=8),
    f'<button style="all: unset; cursor: pointer; box-sizing: border-box; height: 52px; border-radius: 26px; border: 1.5px dashed #B3B9C2; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 15px; font-weight: 600">{ic("plus", 18, "1.8")}Ajouter une personne</button>',
    stack(label("Une de ces personnes est-elle politiquement exposée ?"), segmented(["Non", "Oui"], 0),
          p("Élu, haut fonctionnaire, dirigeant d'entreprise publique, ou un de leurs proches.", 12), gap=8),
]), btn("Envoyer mon dossier", "Review.dc.html"), step=4, back="Director.dc.html"))

add("Review.dc.html", "Dossier envoyé", onboarding("".join([
    f'<div style="display: flex; flex-direction: column; gap: 12px">{circ("clock", TINT, ACC, 72, 32)}'
    + h1("Dossier envoyé", "Nous vérifions vos informations. Vous pouvez déjà découvrir l'application. Dès que le compte est validé, vous recevez une notification et un e-mail, en général sous 48 h ouvrées.") + '</div>',
    panel(row(circ("check", POSBG, POS, 36, 16), "Compte créé", "12 oct. 2026, 09:02")
          + row(circ("check", POSBG, POS, 36, 16), "Entreprise", "NINEA et RCCM reçus")
          + row(circ("check", POSBG, POS, 36, 16), "Identité de la gérante", "Vérifiée")
          + row(circ("clock", WARNBG, WARN, 36, 16), "Documents", "En cours d'analyse", pill("En cours", "warn"))
          + row(circ("clock", WARNBG, WARN, 36, 16), "Cheikh Ndiaye (40 %)", "Attend sa vérification", pill("En attente", "warn"))
          + row(circ("bank", SOFT, INK, 36, 16), "Ouverture du compte et IBAN", "Dès la validation", last=True)),
]), btn("Parler à un conseiller", None, "secondary", "msg") + btn("Découvrir l'application", "Main.dc.html"), close="Main.dc.html",
    aside_title="Merci, votre dossier est entre de bonnes mains.", aside_text="Notre équipe conformité vérifie chaque dossier. Vous êtes prévenu par notification et par e-mail."))

add("Approved.dc.html", "Compte ouvert", onboarding("".join([
    f'<div style="display: flex; flex-direction: column; gap: 12px">{circ("check", POSBG, POS, 72, 32)}'
    + h1("Votre compte est ouvert", "Atelier Ndiaye SARL est validée. Vous avez aussi reçu un e-mail de confirmation avec votre RIB.") + '</div>',
    f'<span style="align-self: flex-start; height: 36px; padding: 0 16px; border-radius: 18px; background: {SOFT}; font-size: 14px; font-weight: 600; display: inline-flex; align-items: center; gap: 8px">IBAN SN08 SN01 •••• 3035 {ic("copy", 14, "1.8")}</span>',
    note("Le premier mois est offert. Choisissez votre offre avant le 5 novembre pour garder votre compte.", "info", "calendar"),
]), btn("Aller à l'accueil", "Main.dc.html", "secondary") + btn("Choisir mon offre", "Plan.dc.html"), close="Main.dc.html",
    aside_title="Bienvenue chez Kelen.", aside_text="Votre IBAN est prêt : partagez-le, recevez vos premiers paiements et payez vos salariés."))


def plan_card(name, size_, price, selected=False, tag="", points=()):
    st = (f"border: 1.5px solid {ACC}; background: #FFFFFF; box-shadow: 0 0 0 3px color-mix(in srgb, {ACC} 16%, transparent)" if selected
          else f"border: {BORDER}; background: {GLASS}; box-shadow: {SH_CARD}")
    t = pill(tag, "info") if tag else ""
    pts = "".join(f'<div style="display: flex; gap: 8px; font-size: 13px; line-height: 1.4"><span style="color: {POS}; display: flex; flex: none">{ic("check", 16, "2")}</span>{x}</div>' for x in points)
    cta_ = btn(f"Activer l'offre {name}", "Main.dc.html", "primary" if selected else "secondary", None, "s")
    return (f'<div style="box-sizing: border-box; border-radius: 24px; padding: 22px; {st}; display: flex; flex-direction: column; gap: 14px; min-width: 0">'
            f'<div style="display: flex; align-items: center; justify-content: space-between; gap: 8px"><span style="font-size: 18px; font-weight: 600">{name}</span>{t}</div>'
            f'<span style="font-size: 13px; color: {MUTED}">{size_}</span>'
            f'<span style="display: flex; align-items: baseline; gap: 6px"><span style="font-size: 36px; font-weight: 500; letter-spacing: -1.2px">{price}</span><span style="font-size: 13px; color: {MUTED}">FCFA / mois</span></span>'
            f'<div style="display: flex; flex-direction: column; gap: 8px">{pts}</div><div style="display: flex; margin-top: auto">{cta_}</div></div>')


def inc(t):
    return f'<div style="display: flex; gap: 10px; align-items: flex-start; font-size: 14px; line-height: 1.4"><span style="color: {POS}; display: flex; flex: none">{ic("check", 16, "2")}</span><span>{t}</span></div>'


add("Plan.dc.html", "Offre et abonnement", shell("Plan", "Choisissez votre offre", "".join([
    hrow(segmented(["Mensuel", "Annuel · 2 mois offerts"], 0), pill("Premier mois offert, jusqu'au 5 novembre", "info")),
    autogrid(plan_card("Essentiel", "Pour démarrer", "9 900", points=("2 utilisateurs", "30 virements bancaires par mois", "200 000 FCFA par mois vers Wave et Orange Money", "Une carte Visa physique et 2 virtuelles")),
             plan_card("Pro", "Pour les équipes", "19 500", True, "Recommandé pour vous", ("3 utilisateurs et double validation", "100 virements bancaires par mois", "1 000 000 FCFA par mois vers Wave et Orange Money", "Module comptable et 10 cartes virtuelles")),
             plan_card("Business", "Pour les grandes équipes", "69 500", points=("10 utilisateurs et validations sur mesure", "400 virements bancaires par mois", "5 000 000 FCFA par mois vers Wave et Orange Money", "API, plusieurs sociétés, cartes virtuelles illimitées")), min_w=280, gap=20),
    card(card_title("Inclus dans toutes les offres")
         + f'<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 12px">'
         + inc("Compte avec IBAN, sous-comptes et relevés") + inc("Salaires vers toutes les banques, Wave et Orange Money") + inc("Une carte Visa physique offerte")
         + inc("Virements et paiements PI-SPI reçus gratuits") + inc("Une alerte avant d'atteindre une limite") + inc("Sans engagement, changement d'offre à tout moment")
         + '</div>', pad="22px 24px", gap=14),
    p("Premier prélèvement le 5 novembre. Sans engagement.", 13),
]), sub="Le premier mois est offert. Choisissez une offre avant le 5 novembre pour garder votre compte.", right=bell()))

# ================================================================== Accounts and bank details
add("Accounts.dc.html", "Comptes", shell("Accounts", "Comptes", "".join([
    autogrid(acct_tile("Principal", INK, "8 210 000", "IBAN •••• 3035 · compte courant, cartes et virements", "AccountDetails.dc.html"),
             acct_tile("Salaires", ACC, "3 500 000", "IBAN •••• 3043 · alimenté le 25 de chaque mois depuis Principal", "AccountDetails.dc.html"),
             acct_tile("Fournisseurs", "#9AA1AD", "770 350", "IBAN •••• 3051 · réservé aux paiements fournisseurs", "AccountDetails.dc.html"),
             f'<a href="NewSubAccount.dc.html" style="box-sizing: border-box; min-height: 110px; border-radius: 20px; border: 1.5px dashed #B3B9C2; display: flex; align-items: center; justify-content: center; gap: 8px; font-size: 15px; font-weight: 600; color: {INK}; text-decoration: none">{ic("plus", 18, "1.8")}Nouveau sous-compte</a>',
             min_w=260, gap=16),
    card(card_title("Documents") + panel(row(circ("file", SOFT), "Relevés et attestations", "Relevés mensuels, RIB, attestation de solde", href="Statements.dc.html", chevron=True, last=True)), pad="20px", gap=12),
]), sub="3 comptes · 12 480 350 FCFA au total", right=bell() + btn("Nouveau sous-compte", "NewSubAccount.dc.html", "primary", "plus", "s")))

rib_kv = kv([("Titulaire", "Atelier Ndiaye SARL"), ("IBAN", "SN08 SN01 0015 2000 0253 0001 3035", copy_btn("l'IBAN")), ("BIC", "[BIC banque partenaire]", copy_btn("le BIC")),
             ("Banque", "[Banque partenaire], Dakar"), ("Code banque", "SN010"), ("Code guichet", "01520"), ("N° de compte", "000253000130"), ("Clé RIB", "35")])

add("AccountDetails.dc.html", "Compte principal", shell("Accounts", "Compte principal", cols(
    stack(card(f'{eyebrow("Solde disponible")}<span style="display: flex; align-items: baseline; gap: 10px"><span style="font-size: 46px; font-weight: 500; letter-spacing: -1.8px; font-variant-numeric: proportional-nums">8 210 000</span>{fcfa_tag()}</span>'
               + hrow(btn("Partager le RIB", None, "primary", "share", "s"), btn("RIB en PDF", None, "secondary", "download", "s"), btn("Relevés", "Statements.dc.html", "secondary", "file", "s"), gap=10),
               pad="24px", gap=10),
          stack(card_title("Dernières opérations", tlink("Tout voir", "Payments.dc.html")), activity_table(ACTIVITY[:4], status=False), gap=12), gap=20),
    stack(card(card_title("Coordonnées bancaires") + rib_kv, pad="20px", gap=12),
          note("Les virements reçus sont gratuits, depuis toutes les banques de l'UEMOA. Compatible PI-SPI pour les virements instantanés.", "info"), gap=16),
    basis=(520, 400)), sub="IBAN •••• 3035 · compte courant", back="Accounts.dc.html", right=bell()))

swatches = "".join(
    f'<button aria-label="{n}" aria-pressed="{"true" if i == 1 else "false"}" style="all: unset; cursor: pointer; width: 42px; height: 42px; border-radius: 21px; box-sizing: border-box; '
    f'border: 2px solid {ACC if i == 1 else "transparent"}; display: flex; align-items: center; justify-content: center"><span style="width: 28px; height: 28px; border-radius: 14px; background: {c}"></span></button>'
    for i, (c, n) in enumerate([(INK, "Graphite"), (ACC, "Sarcelle"), ("#E2543B", "Corail"), ("#12804E", "Émeraude"), ("#6A4BF2", "Violet"), ("#B97600", "Ambre")]))
add("NewSubAccount.dc.html", "Nouveau sous-compte", flow("Nouveau sous-compte", "".join([
    flow_h1("Nouveau sous-compte", "Mettez de côté par usage : impôts, salaires, projets. Chaque sous-compte a son IBAN."),
    field("Nom du sous-compte", "Impôts et TVA"),
    stack(label("Usage"), chips(["Impôts", "Épargne", "Projet", "Fournisseurs", "Autre"], 0), gap=8),
    stack(label("Couleur"), f'<div style="display: flex; gap: 8px; flex-wrap: wrap">{swatches}</div>', gap=8),
    panel(toggle_row("Mettre de côté automatiquement", "18 % de chaque paiement reçu, pour la TVA", True)
          + row(circ("users", SOFT), "Qui peut l'utiliser", "Administrateurs uniquement", chevron=True, last=True)),
]), btn("Annuler", "Accounts.dc.html", "secondary") + btn("Créer le sous-compte", "Accounts.dc.html"), close="Main.dc.html", back="Accounts.dc.html"))


def dl_btn():
    return btn("Télécharger", None, "secondary", "download", "s")


add("Statements.dc.html", "Relevés et attestations", shell("Statements", "Relevés et attestations", "".join([
    hrow(segmented(["Principal", "Salaires", "Fournisseurs"], 0), chips(["3 derniers mois", "2026", "2025", "Personnalisée"], 0), date_btn("Du 1er juillet au 30 septembre 2026"), gap=12),
    cols(
        stack(card_title("Relevés mensuels"),
              table(["Relevé", "Opérations", "Format", ""],
                    [[cell_main(circ("file", SOFT, INK, 36, 16), m), muted(n), muted("PDF"), dl_btn()] for m, n in
                     [("Septembre 2026", "42 opérations"), ("Août 2026", "38 opérations"), ("Juillet 2026", "45 opérations"), ("Juin 2026", "40 opérations")]],
                    ["left", "left", "left", "right"]), gap=12),
        stack(card(card_title("Attestations") + panel(row(circ("bank", SOFT), "RIB", "Avec IBAN et BIC", btn("Générer", None, "secondary", None, "s"))
                                                      + row(circ("wallet", SOFT), "Attestation de solde", "À la date de votre choix", btn("Générer", None, "secondary", None, "s"))
                                                      + row(circ("building", SOFT), "Attestation de domiciliation", "Pour vos clients et l'administration", btn("Générer", None, "secondary", None, "s"), last=True)), pad="20px", gap=12),
              panel(row(circ("book", TINT), "Export pour votre comptable", "Excel ou CSV, plan SYSCOHADA", soon_badge(), href="Accounting.dc.html", last=True)), gap=16),
        basis=(520, 400)),
]), back="AccountDetails.dc.html", right=bell()))

# ================================================================== Top up
def method_tile(title, sub, icon, href, bg=SOFT, text=None):
    return (f'<a href="{href}" style="box-sizing: border-box; border-radius: 20px; padding: 18px; background: {GLASS}; border: {BORDER}; box-shadow: {SH_CARD}; display: flex; align-items: center; gap: 14px; '
            f'text-decoration: none; color: {INK}; min-width: 0">{circ(icon, bg, INK, 44, 20, text=text)}<span style="display: flex; flex-direction: column; gap: 2px; flex: 1 1 auto; min-width: 0">'
            f'<span style="font-size: 15px; font-weight: 600">{title}</span><span style="font-size: 13px; color: {MUTED}">{sub}</span></span><span style="color: {SUBTLE}; display: flex">{ic("chev_r", 18, "1.8")}</span></a>')


add("TopUp.dc.html", "Recharger", flow("Recharger", "".join([
    flow_h1("Recharger", "Choisissez comment ajouter de l'argent."),
    stack(label("Vers"), panel(acct_from("Compte principal", "8 210 000 FCFA")), gap=8),
    stack(eyebrow("Mobile money"), autogrid(method_tile("Wave", "Instantané", "phone", "TopUpWave.dc.html", TINT, "W"),
                                             method_tile("Orange Money", "Instantané", "phone", "TopUpWave.dc.html", "#FDE3DB", "OM"), min_w=260, gap=12), gap=10),
    stack(eyebrow("Banque et carte"), autogrid(method_tile("Virement bancaire", "Gratuit · instantané avec PI-SPI", "bank", "TopUpBank.dc.html"),
                                                method_tile("Carte Visa ou Mastercard", "Instantané", "card", "TopUpCard.dc.html"), min_w=260, gap=12), gap=10),
    stack(eyebrow("Espèces"), method_tile("Dépôt d'espèces", "En agence partenaire, avec un code", "cash", "CashDeposit.dc.html"), gap=10),
]), close="Main.dc.html"))


def amount_input(value):
    return (f'<label style="display: flex; flex-direction: column; gap: 6px">{label("Montant")}<span style="display: flex; align-items: baseline; gap: 10px; height: 76px; box-sizing: border-box; padding: 0 20px; border-radius: 20px; '
            f'border: {FIELD_BORDER}; background: #FFFFFF; align-items: center"><input inputmode="numeric" value="{value}" style="flex: 1 1 auto; min-width: 0; border: 0; outline: none; background: transparent; '
            f'font: inherit; font-size: 40px; font-weight: 500; letter-spacing: -1.5px; color: {INK}">{fcfa_tag(13)}</span></label>')


add("TopUpWave.dc.html", "Recharge Wave", flow("Recharger avec Wave", "".join([
    flow_h1("Recharger avec Wave", size=28),
    amount_input("500 000"),
    chips(["100 000", "250 000", "500 000", "1 000 000"], 2),
    field("Numéro Wave", "77 123 45 67", prefix="+221", mode="tel"),
    panel(acct_from("Vers : compte principal", "Solde 8 210 000 FCFA")),
]), btn("Continuer", "TopUpConfirm.dc.html"), close="Main.dc.html", back="TopUp.dc.html"))

add("TopUpConfirm.dc.html", "Validation Wave", flow("Recharger avec Wave", "".join([
    f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 12px; padding-top: 10px">{circ("phone", TINT, ACC, 80, 36)}'
    f'<h1 style="margin: 6px 0 0; font-size: 28px; font-weight: 600; letter-spacing: -0.8px">Validez dans Wave</h1>'
    + p("Une demande de 500 000 FCFA a été envoyée au +221 77 123 45 67. Ouvrez Wave sur votre téléphone et confirmez avec votre code.", 15)
    + pill("En attente · expire dans 4:52", "warn") + '</div>',
    kv([("Montant", "500 000 FCFA"), ("Depuis", "Wave · 77 123 45 67"), ("Vers", "Compte principal"), ("Référence", "KLN-REC-8821")]),
]), btn("Annuler", "TopUp.dc.html", "secondary") + btn("J'ai confirmé dans Wave", "TopUpSuccess.dc.html"), close="Main.dc.html", back="TopUpWave.dc.html"))


def success_block(icon, title, amount_html, sub, kind="pos"):
    bg, fg = (POSBG, POS) if kind == "pos" else (TINT, ACC)
    return (f'<div style="display: flex; flex-direction: column; align-items: center; text-align: center; gap: 14px; padding-top: 40px">'
            f'<span style="width: 88px; height: 88px; border-radius: 44px; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center">{ic(icon, 40, "2")}</span>'
            f'<h1 style="margin: 6px 0 0; font-size: 30px; font-weight: 600; letter-spacing: -0.8px">{title}</h1>{amount_html}'
            f'<p style="margin: 0; font-size: 15px; line-height: 1.5; color: {MUTED}; max-width: 440px">{sub}</p></div>')


def big(t, color=INK):
    return f'<span style="font-size: 36px; font-weight: 500; letter-spacing: -1.2px; color: {color}">{t}</span>'


add("TopUpSuccess.dc.html", "Recharge reçue", flow("Recharger", success_block("check", "Recharge reçue", big("+500 000 FCFA", POS), "Ajoutée au compte principal. Nouveau solde : 8 710 000 FCFA."),
    btn("Voir le reçu", "TxDetail.dc.html", "secondary") + btn("Retour à l'accueil", "Main.dc.html"), close="Main.dc.html"))

add("TopUpCard.dc.html", "Recharge par carte", flow("Recharger par carte", "".join([
    flow_h1("Recharger par carte", size=28),
    amount_input("250 000"),
    field("Numéro de carte", placeholder="1234 5678 9012 3456", icon="card", mode="numeric"),
    f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px">{field("Expiration", placeholder="MM/AA", mode="numeric")}{field("CVC", placeholder="123", mode="numeric")}</div>',
    field("Nom sur la carte", "Aissatou Ndiaye"),
    note("Votre banque peut vous demander de confirmer avec 3-D Secure.", "soft", "shield"),
]), btn("Payer 250 000 FCFA", "TopUpSuccess.dc.html"), close="Main.dc.html", back="TopUp.dc.html"))


def steps(items):
    out = []
    for i, (t, s) in enumerate(items):
        num = (f'<span style="width: 32px; height: 32px; border-radius: 16px; background: {ACC}; color: #FFFFFF; display: flex; align-items: center; justify-content: center; '
               f'font-size: 14px; font-weight: 600; flex: none">{i + 1}</span>')
        out.append(row(num, t, s, last=i == len(items) - 1))
    return panel("".join(out))


add("TopUpBank.dc.html", "Recevoir un virement", flow("Recevoir un virement", "".join([
    flow_h1("Recevoir un virement", "Partagez votre RIB. Les virements reçus sont gratuits."),
    kv([("Titulaire", "Atelier Ndiaye SARL"), ("IBAN", "SN08 SN01 0015 2000 0253 0001 3035", copy_btn("l'IBAN")), ("BIC", "[BIC banque partenaire]", copy_btn("le BIC")), ("Banque", "[Banque partenaire]")]),
    stack(card_title("Comment ça marche"), steps([("Partagez votre RIB", "À votre client ou à votre banque"), ("Le virement part de n'importe quelle banque", "Partout dans l'UEMOA"),
                                                  ("L'argent arrive sur votre compte", "Instantané avec PI-SPI, sinon en général 1 jour ouvré")]), gap=10),
]), btn("Télécharger le RIB (PDF)", None, "secondary", "download") + btn("Partager le RIB", None, "primary", "share"), close="Main.dc.html", back="TopUp.dc.html"))

add("CashDeposit.dc.html", "Dépôt d'espèces", flow("Dépôt d'espèces", "".join([
    flow_h1("Dépôt d'espèces", "Présentez ce code et votre pièce d'identité au guichet."),
    card(f'<div style="display: flex; flex-direction: column; align-items: center; gap: 8px">{eyebrow("Votre code de dépôt")}'
         f'<span style="font-size: 40px; font-weight: 500; letter-spacing: 4px; margin: 4px 0">KLN 4821 77</span>{pill("Valable 24 h", "info")}'
         f'<span style="margin-top: 8px">{btn("Copier le code", None, "secondary", "copy", "s")}</span></div>', pad="26px", radius=28),
    stack(card_title("Où déposer"), panel(row(circ("pin", SOFT), "[Banque partenaire] · Plateau", "2,1 km · ouvert jusqu'à 16 h", chevron=True)
                                          + row(circ("pin", SOFT), "[Banque partenaire] · Point E", "3,4 km · ouvert jusqu'à 16 h", chevron=True)
                                          + row(circ("pin", SOFT), "[Banque partenaire] · Parcelles Assainies", "7,8 km · ouvert le samedi matin", chevron=True, last=True)), gap=10),
    note("L'argent arrive sur votre compte dès que le guichet valide le dépôt.", "soft", "info"),
]), close="Main.dc.html", back="TopUp.dc.html"))

# ================================================================== Send
add("Send.dc.html", "Envoyer", flow("Envoyer", "".join([
    flow_h1("Envoyer"),
    field(None, placeholder="Nom, IBAN ou numéro", icon="search"),
    segmented(["Tous", "Banque", "Mobile money"], 0),
    panel(row(circ("plus", ACC, "#FFFFFF"), "Nouveau bénéficiaire", "Banque, Wave ou Orange Money", href="NewRecipient.dc.html", chevron=True)
          + row(circ("swap", SOFT), "Entre vos comptes", "Principal, Salaires, Fournisseurs", href="SendAmount.dc.html", chevron=True, last=True)),
    stack(card_title("Récents"), panel(row(av("CL", TINT), "Cissé Logistique SARL", "Banque · SN12 •••• 7781", href="SendAmount.dc.html", chevron=True)
                                       + row(av("SD", "#FDE3DB"), "Sow Distribution", "Wave · 77 ••• •• 12", href="SendAmount.dc.html", chevron=True)
                                       + row(av("DM", "#DDF4EA"), "Diallo Matériaux", "Orange Money · 78 ••• •• 40", href="SendAmount.dc.html", chevron=True)
                                       + row(av("IB", "#ECE6FD"), "Imprimerie Ba", "Banque · SN08 •••• 2209", href="SendAmount.dc.html", chevron=True, last=True)), gap=10),
    panel(row(circ("globe", SOFT), "Virement international", "EUR, USD, CNY…", soon_badge(), href="Intl.dc.html", last=True)),
]), close="Main.dc.html"))


def type_btn(t, icon, on=False):
    st = f"background: {ACC}; color: #FFFFFF; border: 1px solid {ACC}" if on else f"background: {GLASS}; border: {BORDER}; box-shadow: {SH_CARD}"
    return (f'<button aria-pressed="{"true" if on else "false"}" style="all: unset; cursor: pointer; box-sizing: border-box; border-radius: 18px; padding: 16px 8px; {st}; display: flex; '
            f'flex-direction: column; align-items: center; gap: 8px; text-align: center">{ic(icon, 22, "1.8")}<span style="font-size: 14px; font-weight: 600">{t}</span></button>')


add("NewRecipient.dc.html", "Nouveau bénéficiaire", flow("Envoyer", "".join([
    flow_h1("Nouveau bénéficiaire"),
    f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px">{type_btn("Banque", "bank", True)}{type_btn("Wave", "phone")}{type_btn("Orange Money", "phone")}</div>',
    field("Nom du bénéficiaire", "Cissé Logistique SARL"),
    field("IBAN", "SN12 SN05 4010 1700 0458 1200 7781"),
    stack(label("Type de bénéficiaire"), segmented(["Fournisseur", "Salarié", "Autre"], 0), p("Les salaires sont exonérés de la taxe de 0,5 % sur les transferts.", 12), gap=8),
    panel(toggle_row("Ajouter aux favoris", "Pour le retrouver en haut de la liste", True, last=True)),
]), btn("Continuer", "SendAmount.dc.html"), close="Main.dc.html", back="Send.dc.html"))

send_summary = card(card_title("Récapitulatif") + kv([("À", "Cissé Logistique SARL"), ("Montant", "1 250 000 FCFA"), ("Arrivée", "Instantanée (PI-SPI)")])
                    + note("Virement fournisseur n° 15 sur les 200 inclus ce mois-ci.", "soft", "info"), pad="20px", gap=12)

add("SendAmount.dc.html", "Montant", flow("Envoyer", "".join([
    panel(row(av("CL", TINT), "Cissé Logistique SARL", "Banque · SN12 •••• 7781", tlink("Changer", "Send.dc.html"), last=True)),
    amount_input("1 250 000"),
    panel(acct_from()),
    field("Motif", "Facture F-2026-118, transport septembre"),
    stack(label("Date"), segmented(["Maintenant", "Programmer"], 0), gap=8),
]), btn("Vérifier", "SendReview.dc.html"), close="Main.dc.html", back="Send.dc.html", aside=send_summary))

add("SendReview.dc.html", "Vérification", flow("Envoyer", "".join([
    flow_h1("Vérifiez le virement", size=28),
    card(f'<div style="display: flex; flex-direction: column; align-items: center; gap: 6px">{eyebrow("Montant")}'
         f'<span style="display: flex; align-items: baseline; gap: 10px"><span style="font-size: 46px; font-weight: 500; letter-spacing: -1.8px">1 250 000</span>{fcfa_tag()}</span></div>', pad="22px", radius=26),
    kv([("À", "Cissé Logistique SARL"), ("IBAN", "SN12 •••• 7781"), ("Depuis", "Compte principal"), ("Arrivée", "Instantanée (PI-SPI)"), ("Motif", "Facture F-2026-118")]),
    kv([("Taxe sur les transferts (0,5 %)", "6 250 FCFA"), ("Total débité", "1 256 250 FCFA")]),
    note("Inclus dans votre offre. La taxe de 0,5 % est reversée à l'État.", "soft", "info"),
    field("Code secret", placeholder="Votre code à 6 chiffres", typ="password", mode="numeric", hint="Ou validez sur votre téléphone avec Face ID."),
]), btn("Modifier", "SendAmount.dc.html", "secondary") + btn("Confirmer le virement", "SendSuccess.dc.html", "primary", "lock"), close="Main.dc.html", back="SendAmount.dc.html"))

add("SendSuccess.dc.html", "Virement envoyé", flow("Envoyer", success_block("check", "Virement envoyé", big("1 250 000 FCFA"), "À Cissé Logistique SARL. Arrivé instantanément · réf. KLN-VIR-55120."),
    btn("Partager le justificatif", None, "secondary", "share") + btn("Retour à l'accueil", "Main.dc.html"), close="Main.dc.html"))

# ================================================================== Bulk payouts
add("Bulk.dc.html", "Paie groupée", shell("Bulk", "Paie groupée", "".join([
    card(card_title("À valider") + panel(row(circ("calendar", TINT), "Paie d'octobre", "24 salariés · 3 465 000 FCFA · 31 oct.", pill("Prête", "info"), href="BulkReview.dc.html", chevron=True, last=True)), pad="20px", gap=12),
    stack(card_title("Historique"), table(["Paiement", "Date", "Bénéficiaires", "Statut", "Montant"],
                                          [[cell_main(circ("check", POSBG, POS, 36, 16), "Paie de septembre"), muted("Payée le 30 sept."), muted("24 salariés"), pill("Payée", "pos"), money_cell(3420000, sign=False)],
                                           [cell_main(circ("check", POSBG, POS, 36, 16), "Prestataires chantier"), muted("Payés le 12 sept."), muted("6 prestataires"), pill("Payée", "pos"), money_cell(1180000, sign=False)],
                                           [cell_main(circ("check", POSBG, POS, 36, 16), "Paie d'août"), muted("Payée le 29 août"), muted("23 salariés"), pill("Payée", "pos"), money_cell(3310000, sign=False)]],
                                          ["left", "left", "left", "left", "right"]), gap=12),
    note("Les salaires sont exonérés de la taxe sur les transferts.", "pos", "check"),
]), sub="Salaires et prestataires en une fois, vers toutes les banques, Wave et Orange Money.",
    right=bell() + btn("Nouveau paiement groupé", "BulkNew.dc.html", "primary", "plus", "s")))

add("BulkNew.dc.html", "Nouveau paiement groupé", flow("Paie groupée", "".join([
    flow_h1("Nouveau paiement groupé", size=28),
    field("Nom", "Paie d'octobre 2026"),
    stack(label("Type"), segmented(["Salaires", "Prestataires"], 0), gap=8),
    panel(acct_from("Depuis : compte Salaires", "3 500 000 FCFA disponibles", ACC, last=False)
          + row(circ("calendar", SOFT), "Date de paiement", "Vendredi 31 octobre 2026, 08:00", chevron=True, last=True)),
    stack(card_title("Bénéficiaires"), autogrid(
        option("Choisir parmi vos bénéficiaires", "Salariés et fournisseurs déjà enregistrés", "users", True, href="BulkPick.dc.html"),
        option("Reprendre la paie de septembre", "24 salariés, montants modifiables", "refresh"),
        option("Importer un fichier Excel ou CSV", "Un modèle est fourni", "upload"),
        option("Ajouter à la main", "Un par un", "plus"), min_w=280, gap=12), gap=10),
]), btn("Continuer", "BulkPick.dc.html"), close="Main.dc.html", back="Bulk.dc.html", width=760))


def pick_box(on):
    return (f'<span style="width: 22px; height: 22px; box-sizing: border-box; border-radius: 7px; border: 1.5px solid {ACC if on else "#C5C9D0"}; background: {ACC if on else "#FFFFFF"}; '
            f'color: #FFFFFF; display: flex; align-items: center; justify-content: center; flex: none">{ic("check", 13, "2.4") if on else ""}</span>')


PEOPLE = [("IF", TINT, "Ibrahima Fall", "Chef d'atelier", "Banque", "SN08 •••• 4410", 420000), ("MD", "#FDE3DB", "Mariama Diop", "Menuisière", "Wave", "77 ••• •• 18", 165000),
          ("OF", WARNBG, "Ousmane Faye", "Menuisier", "Orange Money", "78 ••• •• 03", 120000), ("AS", "#DDF4EA", "Awa Sène", "Finition", "Wave", "76 ••• •• 52", 150000),
          ("MG", "#ECE6FD", "Modou Gueye", "Livraison", "Banque", "SN12 •••• 0918", 210000), ("KN", TINT, "Khady Ndiaye", "Vente", "Wave", "77 ••• •• 64", 140000)]

add("BulkPick.dc.html", "Choisir les bénéficiaires", flow("Paie groupée", "".join([
    flow_h1("Choisir les bénéficiaires", "Parmi les salariés et fournisseurs déjà enregistrés. Les montants de la dernière paie sont repris et modifiables.", size=28),
    hrow(search_field("Rechercher un nom ou un numéro", 360), segmented(["Salariés · 24", "Fournisseurs · 12"], 0), gap=12),
    table([pick_box(True), "Bénéficiaire", "Moyen de paiement", "Compte", "Montant"],
          [[pick_box(True), cell_main(av(i, bg, 36), n, r), muted(m), muted(acc), f'<input aria-label="Montant {n}" inputmode="numeric" value="{money(a)}" style="width: 120px; height: 38px; box-sizing: border-box; padding: 0 12px; border-radius: 12px; border: {FIELD_BORDER}; background: #FFFFFF; font: inherit; font-size: 14px; font-weight: 600; text-align: right; color: {INK}">']
           for i, bg, n, r, m, acc, a in PEOPLE],
          ["left", "left", "left", "left", "right"]),
    f'<div style="display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap"><span style="font-size: 14px; color: {MUTED}">Affichés : 6 sur 24 · {tlink("Voir les 24")}</span>'
    f'<span style="font-size: 15px; font-weight: 600">24 bénéficiaires sélectionnés · 3 465 000 FCFA</span></div>',
]), btn("Continuer", "BulkReview.dc.html"), close="Main.dc.html", back="BulkNew.dc.html", width=1040))


def chan(n, t):
    return card(f'<span style="font-size: 26px; font-weight: 500">{n}</span><span style="font-size: 13px; color: {MUTED}">{t}</span>', pad="16px 18px", gap=2)


add("BulkReview.dc.html", "Paie d'octobre", flow("Paie groupée", "".join([
    hrow(flow_h1("Paie d'octobre", "Vendredi 31 octobre 2026 · depuis le compte Salaires"), f'<span style="margin-left: auto">{btn("Modifier", "BulkPick.dc.html", "secondary", "edit", "s")}</span>', align="flex-start"),
    cols(card(f'{eyebrow("Total à payer")}<span style="display: flex; align-items: baseline; gap: 10px"><span style="font-size: 46px; font-weight: 500; letter-spacing: -1.8px">3 465 000</span>{fcfa_tag()}</span>'
              f'<span>{pill("Solde suffisant : 3 500 000 FCFA", "info")}</span>', pad="24px", gap=8, radius=26),
         f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px">{chan("9", "Banque")}{chan("11", "Wave")}{chan("4", "Orange Money")}</div>',
         basis=(420, 360)),
    note("1 numéro à vérifier : Ousmane Faye, Orange Money 78 ••• •• 03.", "warn", "alert"),
    stack(card_title("Salariés · 24", tlink("Voir les 24")),
          table(["Salarié", "Moyen de paiement", "Compte", "Montant"],
                [[cell_main(av(i, bg, 36), n, r), muted(m) if n != "Ousmane Faye" else pill("À vérifier", "warn"), muted(acc), money_cell(a, sign=False)] for i, bg, n, r, m, acc, a in PEOPLE[:5]],
                ["left", "left", "left", "right"]), gap=12),
    kv([("Taxe sur les transferts", "Exonérée (salaires)")]),
]), btn("Envoyer pour validation", "BulkApproval.dc.html"), close="Main.dc.html", back="Bulk.dc.html", width=1040))

add("BulkApproval.dc.html", "Validation de la paie", flow("Paie groupée", "".join([
    flow_h1("Validation", "La double validation est activée pour les paiements groupés."),
    panel(row(circ("calendar", TINT), "Paie d'octobre", "24 salariés · 31 oct.", amt(3465000), href="BulkReview.dc.html", last=True)),
    stack(card_title("Circuit de validation"), panel(
        row(circ("check", POSBG, POS), "Préparée par Fatou Sarr", "Assistante · 12 oct., 10:42")
        + row(circ("check", POSBG, POS), "Validée par Moussa Diop", "Comptable · 12 oct., 11:05")
        + row(circ("clock", WARNBG, WARN), "Votre validation", "Aïssatou Ndiaye · gérante", pill("En attente", "warn"), last=True)), gap=10),
    note("Après votre accord, la paie part le 31 octobre à 08:00. Chaque salarié reçoit un SMS.", "soft", "info"),
    field("Code secret", placeholder="Votre code à 6 chiffres", typ="password", mode="numeric"),
]), btn("Refuser", None, "danger") + btn("Valider et programmer", "BulkDone.dc.html", "primary", "lock"), close="Main.dc.html", back="BulkReview.dc.html"))

add("BulkDone.dc.html", "Paie programmée", flow("Paie groupée", success_block("check", "Paie programmée", big("3 465 000 FCFA"),
    "24 salariés seront payés le vendredi 31 octobre à 08:00, sur leur banque, Wave ou Orange Money."),
    btn("Voir la paie groupée", "Bulk.dc.html", "secondary") + btn("Retour à l'accueil", "Main.dc.html"), close="Main.dc.html"))

# ================================================================== Bills
def biller(name, sub, icon, bg=SOFT):
    return (f'<a href="BillPay.dc.html" style="box-sizing: border-box; border-radius: 20px; padding: 18px 10px; background: {GLASS}; border: {BORDER}; box-shadow: {SH_CARD}; display: flex; flex-direction: column; '
            f'align-items: center; gap: 8px; text-decoration: none; color: {INK}; text-align: center">{circ(icon, bg)}<span style="font-size: 14px; font-weight: 600">{name}</span>'
            f'<span style="font-size: 12px; color: {MUTED}">{sub}</span></a>')


add("Bills.dc.html", "Factures", shell("Bills", "Factures", cols(
    stack(stack(card_title("À payer"), panel(row(circ("bolt", WARNBG, WARN), "Senelec", "Septembre · échéance 20 oct.", amt(126450), href="BillPay.dc.html", chevron=True)
                                             + row(circ("drop", TINT), "Sen'Eau", "Septembre · échéance 5 nov.", amt(41200), href="BillPay.dc.html", chevron=True, last=True)), gap=10),
          stack(card_title("Facturiers"), autogrid(biller("Senelec", "Électricité", "bolt"), biller("Woyofal", "Prépayé", "bolt"), biller("Sen'Eau", "Eau", "drop"),
                                                    biller("Orange", "Internet, mobile", "wifi"), biller("Yas", "Internet, mobile", "wifi"), biller("Canal+", "Télévision", "tv"), min_w=150, gap=12), gap=10),
          panel(row(circ("building", SOFT), "Impôts et taxes", "Paiement à la DGID", soon_badge(), last=True)), gap=20),
    stack(card(card_title("Payées récemment") + panel(row(circ("bolt", POSBG, POS), "Senelec", "Payée aujourd'hui, 08:02", amt(-84300), href="TxDetail.dc.html", last=True)), pad="20px", gap=12),
          note("Enregistrez vos contrats : nous vous rappelons chaque facture avant l'échéance.", "info", "bell"), gap=16),
    basis=(560, 340)), right=search_field("Rechercher un facturier", 300) + bell()))

add("BillPay.dc.html", "Payer une facture", flow("Factures", "".join([
    f'<div style="display: flex; align-items: center; gap: 14px">{circ("bolt", WARNBG, WARN, 56, 26)}{h1("Senelec", "Électricité · facture mensuelle", size=28)}</div>',
    field("Numéro de contrat", "2310 4471 902", mode="numeric"),
    stack(card_title("Facture trouvée"), kv([("Titulaire", "Atelier Ndiaye SARL"), ("Période", "Septembre 2026"), ("Échéance", "20 octobre 2026"), ("Montant", "126 450 FCFA")]), gap=10),
    panel(acct_from(last=False) + toggle_row("Enregistrer ce contrat", "Rappel chaque mois avant l'échéance", True, last=True)),
]), btn("Payer 126 450 FCFA", "BillSuccess.dc.html", "primary", "lock"), close="Main.dc.html", back="Bills.dc.html"))

add("BillSuccess.dc.html", "Facture payée", flow("Factures", success_block("check", "Facture payée", big("126 450 FCFA"), "Senelec · contrat 2310 4471 902. Le reçu est rangé avec l'opération."),
    btn("Payer une autre facture", "Bills.dc.html", "secondary") + btn("Retour à l'accueil", "Main.dc.html"), close="Main.dc.html"))

# ================================================================== Team and permissions
TEAM = [("AN", ACC, "Aïssatou Ndiaye", "Gérante", "Administratrice", pill("Vous", "info"), None),
        ("MD", TINT, "Moussa Diop", "Comptable", "Exports et 1re validation", pill("Actif", "pos"), "Permissions.dc.html"),
        ("FS", "#FDE3DB", "Fatou Sarr", "Assistante", "Paiements jusqu'à 500 000 FCFA", pill("Actif", "pos"), "Permissions.dc.html"),
        ("IF", "#DDF4EA", "Ibrahima Fall", "Chef d'atelier", "Carte uniquement", pill("Actif", "pos"), "Permissions.dc.html"),
        ("CN", SOFT, "Cheikh Ndiaye", "Associé", "Lecture seule", pill("Invitation envoyée", "warn"), None)]

add("Team.dc.html", "Équipe et droits", shell("Team", "Équipe et droits", "".join([
    table(["Membre", "Rôle", "Droits", "Statut", ""],
          [[cell_main(av(i, bg, 36), n, r, href), muted(r), muted(d), st, (tlink("Modifier", href) if href else "")] for i, bg, n, r, d, st, href in TEAM],
          ["left", "left", "left", "left", "right"]),
    autogrid(card(card_title("Double validation") + p("Virements de plus de 1 000 000 FCFA et toutes les paies.", 14) + f'<span>{btn("Modifier la règle", None, "secondary", None, "s")}</span>', pad="20px", gap=10),
             card(card_title("Validations en attente", pill("2", "warn")) + p("Un virement et la paie d'octobre attendent votre accord.", 14) + f'<span>{btn("Voir", "Approvals.dc.html", "primary", None, "s")}</span>', pad="20px", gap=10),
             min_w=320, gap=16),
]), sub="Invitez votre équipe et choisissez les droits de chacun.", right=bell() + btn("Inviter", "Invite.dc.html", "primary", "plus", "s")))

add("Invite.dc.html", "Inviter un membre", flow("Équipe et droits", "".join([
    flow_h1("Inviter un membre"),
    f'<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 14px">{field("Prénom et nom", "Khady Mbaye")}{field("Téléphone", "76 555 21 09", prefix="+221", mode="tel")}</div>',
    field("E-mail", placeholder="Facultatif", typ="email"),
    stack(card_title("Rôle"), autogrid(option("Administrateur", "Tout faire, y compris gérer l'équipe", "shield"),
                                       option("Comptable", "Voir, exporter, valider les paiements", "book"),
                                       option("Payeur", "Préparer des paiements, toujours validés", "send", True),
                                       option("Lecture seule", "Voir les comptes et les opérations", "eye"),
                                       option("Carte uniquement", "Utiliser sa carte, envoyer ses justificatifs", "card"), min_w=280, gap=12), gap=10),
]), btn("Continuer", "Permissions.dc.html"), close="Team.dc.html", back="Team.dc.html", width=760))

add("Permissions.dc.html", "Droits", flow("Équipe et droits", "".join([
    flow_h1("Droits de Khady Mbaye", "Rôle Payeur. Ajustez chaque droit si besoin."),
    autogrid(
        stack(card_title("Comptes"), panel(toggle_row("Voir les soldes et opérations", None, True) + row("", "Comptes accessibles", "Principal, Fournisseurs", chevron=True, last=True)), gap=10),
        stack(card_title("Paiements"), panel(toggle_row("Préparer des virements", "Toujours validés par un administrateur", True) + row("", "Plafond par virement", "500 000 FCFA", chevron=True)
                                             + toggle_row("Préparer une paie groupée", None, False) + toggle_row("Payer des factures", None, True, last=True)), gap=10),
        stack(card_title("Validation et cartes"), panel(toggle_row("Valider les paiements des autres", None, False) + toggle_row("Demander une carte", "Virtuelle, avec plafond", True)
                                                        + toggle_row("Exporter les relevés", None, False, last=True)), gap=10),
        min_w=320, gap=16),
]), btn("Envoyer l'invitation", "Team.dc.html", "primary", "send"), close="Team.dc.html", back="Invite.dc.html", width=1040))


def approval(init, bg, who, when, kind, amount, lines, actions):
    return card(row(av(init, bg, 36), who, when, pill(kind, "info"), last=True, pad="0")
                + f'<span style="font-size: 30px; font-weight: 500; letter-spacing: -1px">{amount} <span style="font-size: 13px; color: {MUTED}; letter-spacing: 1px">FCFA</span></span>'
                + "".join(f'<span style="font-size: 14px; color: {MUTED}">{l}</span>' for l in lines)
                + f'<div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 4px">{actions}</div>', pad="20px", gap=8)


add("Approvals.dc.html", "Validations", shell("Approvals", "Validations", "".join([
    autogrid(approval("FS", "#FDE3DB", "Fatou Sarr", "Aujourd'hui, 10:12", "Virement", "2 450 000", ["À Diallo Matériaux · Banque", "Motif : commande de bois rouge"],
                      btn("Refuser", None, "danger", None, "s") + btn("Valider", "SendSuccess.dc.html", "primary", None, "s")),
             approval("MD", TINT, "Moussa Diop", "Validée en 1er · 11:05", "Paie", "3 465 000", ["Paie d'octobre · 24 salariés · 31 oct."],
                      btn("Détail", "BulkApproval.dc.html", "secondary", None, "s") + btn("Valider", "BulkDone.dc.html", "primary", None, "s")),
             min_w=380, gap=20),
    note("Règle actuelle : double validation pour les virements de plus de 1 000 000 FCFA et pour toutes les paies.", "soft", "shield"),
]), sub="2 opérations attendent votre accord.", right=bell()))

# ================================================================== Coming soon
def soon_page(file, active, title, sub, content):
    add(file, title, shell(active, title, f'{content}<div style="display: flex">{soon_btn()}</div>', sub=sub, right=bell() + soon_badge()))


soon_page("Intl.dc.html", "Intl", "Virement international", "Payez vos fournisseurs hors de la zone UEMOA.", "".join([
    cols(stack(panel(row(circ("globe", TINT), "Vers : France", "Euro (EUR)", chevron=True, last=True)),
               autogrid(card(f'<span style="font-size: 13px; color: {MUTED}">Vous envoyez</span><span style="font-size: 30px; font-weight: 500; letter-spacing: -1px">6 559 570 FCFA</span>', pad="18px 20px", gap=4),
                        card(f'<span style="font-size: 13px; color: {MUTED}">Le fournisseur reçoit</span><span style="font-size: 30px; font-weight: 500; letter-spacing: -1px">10 000,00 EUR</span>', pad="18px 20px", gap=4), min_w=240, gap=12),
               kv([("Taux", "1 EUR = 655,957 FCFA (parité fixe)"), ("Délai", "Affiché avant l'envoi")]), gap=14),
         stack(note("Une pièce justificative (facture, contrat) est demandée pour chaque transfert hors UEMOA, selon la réglementation des changes de la BCEAO.", "soft", "file"),
               stack(card_title("Pays envisagés"), chips(["France · EUR", "Chine · CNY", "Émirats · AED", "Turquie · TRY", "Maroc · MAD", "Nigeria · NGN", "Ghana · GHS"], -1), gap=10), gap=16),
         basis=(520, 380)),
]))

soon_page("PayLinks.dc.html", "PayLinks", "Liens de paiement", "Faites-vous payer par Wave, Orange Money, carte ou virement avec un simple lien.", cols(
    card(card_title("Nouveau lien") + field("Montant", "350 000", mode="numeric") + field("Description", "Acompte table en acajou, commande 212")
         + f'<div style="display: flex; gap: 6px; flex-wrap: wrap">{pill("Wave", "info")}{pill("Orange Money", "info")}{pill("Carte", "info")}{pill("Virement", "info")}</div>'
         + f'<div style="display: flex">{btn("Créer et partager", None, "primary", "share", "s")}</div>', pad="22px", gap=12),
    stack(card_title("Vos liens"), table(["Lien", "Statut", "Montant"],
                                         [[cell_main(circ("link", WARNBG, WARN, 36, 16), "Acompte commande 212", "Créé aujourd'hui · envoyé sur WhatsApp"), pill("En attente", "warn"), money_cell(350000, sign=False)],
                                          [cell_main(circ("link", POSBG, POS, 36, 16), "Chaises salle de réunion", "Payé par Wave le 8 oct."), pill("Payé", "pos"), money_cell(780000, sign=False)],
                                          [cell_main(circ("link", SOFT, INK, 36, 16), "Devis 198", "Expiré le 30 sept."), pill("Expiré"), money_cell(1150000, sign=False)]],
                                         ["left", "left", "right"]), gap=12),
    basis=(380, 560)))


def budget_row(init, bg, name, cat, spent, total):
    return [cell_main(av(init, bg, 36), name, cat), f'<div style="min-width: 160px">{progress(round(spent * 100 / total), h=6)}</div>',
            f'<span style="font-size: 14px; font-weight: 600; white-space: nowrap">{money(spent)} <span style="color: {MUTED}; font-weight: 500">/ {money(total)}</span></span>']


soon_page("BudgetCards.dc.html", "BudgetCards", "Cartes budget", "Une carte par salarié avec un budget précis : transport, carburant, repas.", "".join([
    card(f'<span style="display: flex; justify-content: space-between; align-items: baseline"><span style="font-size: 13px; color: {MUTED}">Budget d\'octobre</span>'
         f'<span style="font-size: 14px; font-weight: 600">157 500 <span style="color: {MUTED}; font-weight: 500">/ 240 000 FCFA</span></span></span>{progress(66)}'
         + muted("Rechargé automatiquement le 1er de chaque mois"), pad="18px 20px", gap=10),
    cols(stack(card_title("Salariés"), table(["Salarié", "Utilisé", "Budget"], [budget_row("IF", TINT, "Ibrahima Fall", "Carburant", 75000, 100000),
                                                                               budget_row("MD", "#FDE3DB", "Mariama Diop", "Transport", 18000, 40000),
                                                                               budget_row("MG", "#ECE6FD", "Modou Gueye", "Repas chantier", 52000, 60000),
                                                                               budget_row("AS", "#DDF4EA", "Awa Sène", "Transport", 12500, 40000)], ["left", "left", "right"]), gap=12),
         card(card_title("Règles") + panel(row(circ("refresh", SOFT), "Recharge automatique", "Le 1er de chaque mois") + row(circ("tag", SOFT), "Dépenses autorisées", "Carburant, transport, restauration")
                                           + row(circ("receipt", SOFT), "Justificatifs", "Photo du reçu demandée après chaque paiement", last=True)), pad="20px", gap=12),
         basis=(560, 340)),
]))

soon_page("Accounting.dc.html", "Accounting", "Comptabilité", "Justificatifs, catégories et exports pour votre comptable, sans ressaisie.", "".join([
    autogrid(stat_card("Justificatifs manquants", "7", WARN, "sur 64 opérations"), stat_card("Opérations catégorisées", "92 %", INK, "en octobre"),
             stat_card("TVA collectée en octobre", "612 400", INK, "FCFA · taux normal de 18 %"), min_w=240),
    cols(stack(card_title("Octobre par catégorie"), table(["Catégorie", "Détail", "Montant"],
                                                          [[cell_main(circ("users", SOFT, INK, 36, 16), "Salaires"), muted("24 salariés"), money_cell(3465000, sign=False)],
                                                           [cell_main(circ("brief", SOFT, INK, 36, 16), "Achats et matières"), muted("Bois, quincaillerie"), money_cell(1840000, sign=False)],
                                                           [cell_main(circ("truck", SOFT, INK, 36, 16), "Transport"), muted("Livraisons"), money_cell(1250000, sign=False)],
                                                           [cell_main(circ("bolt", SOFT, INK, 36, 16), "Énergie"), muted("Senelec"), money_cell(84300, sign=False)]],
                                                          ["left", "left", "right"]), gap=12),
         card(card_title("Exports et accès") + panel(row(circ("download", SOFT), "Export pour le comptable", "Excel ou CSV · plan SYSCOHADA", chevron=True)
                                                     + row(circ("user", SOFT), "Accès comptable", "Moussa Diop · lecture et exports", chevron=True, last=True)), pad="20px", gap=12),
         basis=(560, 340)),
]))


def product(title, sub, meta, icon, href=None):
    chev = f'<span style="display: flex; flex: none; color: {SUBTLE}">{ic("chev_r", 18, "1.8")}</span>' if href else ""
    inner = (f'<span style="display: flex; align-items: center; gap: 12px">{circ(icon, TINT)}<span style="font-size: 16px; font-weight: 600; flex: 1 1 auto">{title}</span>{chev}</span>'
             f'<span style="font-size: 14px; line-height: 1.45; color: {MUTED}">{sub}</span><span>{pill(meta)}</span>')
    st = f"box-sizing: border-box; border-radius: 22px; padding: 20px; background: {GLASS}; border: {BORDER}; box-shadow: {SH_CARD}; display: flex; flex-direction: column; gap: 10px; color: {INK}; text-decoration: none; min-width: 0"
    return f'<a href="{href}" style="{st}">{inner}</a>' if href else f'<div style="{st}">{inner}</div>'


soon_page("Financing.dc.html", "Financing", "Financement", "Un seul prix : 0,063 % par jour sur le montant utilisé, soit 23 % par an (TEG). Pas de frais de dossier.", "".join([
    autogrid(product("Affacturage", "Recevez 80 à 90 % de vos factures clients sans attendre l'échéance.", "30 à 90 jours · 1,9 % pour 30 jours", "percent", "Factoring.dc.html"),
             product("Financement de factures", "Avancez sur une facture ; votre client vous paie comme d'habitude.", "Remboursement automatique", "file", "Factoring.dc.html"),
             product("Prêt équipement", "Véhicules, machines, téléphones : de 1 à 50 millions de FCFA.", "6 à 24 mois", "truck", "LoanOffer.dc.html"),
             product("Pont de paie", "Payez les salaires à l'heure, même si un client paie en retard.", "Jusqu'à 1 mois de paie · 45 jours", "users"),
             product("Ligne de crédit", "Une réserve de trésorerie calculée sur vos encaissements.", "Après 6 mois d'activité", "trend"), min_w=300, gap=16),
    note("Crédits accordés par notre partenaire de microfinance agréé. Le coût en FCFA est affiché avant chaque utilisation.", "soft", "shield"),
]))

add("LoanOffer.dc.html", "Prêt équipement", shell("Financing", "Prêt équipement", "".join([
    cols(card(amount_input("2 000 000") + chips(["1 000 000", "2 000 000", "5 000 000", "10 000 000"], 1)
              + stack(label("Durée"), segmented(["6 mois", "12 mois", "18 mois", "24 mois"], 0), gap=8), pad="22px", gap=16),
         stack(kv([("Mensualité", "356 048 FCFA"), ("Coût total du crédit", "136 288 FCFA"), ("Taux (TEG)", "23 % par an"), ("Total remboursé", "2 136 288 FCFA")]),
               note("Prélèvement automatique le 5 de chaque mois sur le compte principal. Remboursement anticipé sans pénalité.", "soft", "calendar"), gap=14),
         basis=(480, 400)),
    f'<div style="display: flex">{soon_btn()}</div>',
]), sub="Simulez votre prêt. Mensualités fixes, sans frais de dossier.", back="Financing.dc.html", right=bell() + soon_badge()))

add("Factoring.dc.html", "Affacturage", shell("Financing", "Affacturage", "".join([
    segmented(["Affacturage", "Financement de factures"], 0),
    p("Affacturage : votre client paie la facture sur votre compte Kelen à l'échéance. Financement de factures : il vous paie comme d'habitude et le remboursement est automatique.", 14),
    cols(stack(panel(row(circ("file", TINT), "Facture F-2026-131", "Société Immobilière Keur Gorgui · échéance 11 déc.", amt(4800000), last=True)),
               kv([("Avance (85 %)", "4 080 000 FCFA"), ("Durée", "60 jours"), ("Coût (0,063 % par jour)", "154 224 FCFA"), ("Reversé au paiement", "565 776 FCFA")]), gap=14),
         stack(card_title("Comment ça marche"), steps([("Importez la facture", "PDF ou photo"), ("Nous vérifions votre client", "Sous 48 h"),
                                                       ("Vous recevez 85 %", "Sur le compte principal"), ("Votre client paie à l'échéance", "Le solde vous est reversé")]), gap=10),
         basis=(480, 400)),
    f'<div style="display: flex">{soon_btn()}</div>',
]), sub="Transformez vos factures clients en trésorerie.", back="Financing.dc.html", right=bell() + soon_badge()))

# ================================================================== canvas index
ROWS = [
    ("home", "1 · Home & tabs", "rHome", "Home, payments, cards, notifications, settings", ["Main", "Payments", "TxDetail", "Cards", "CardDetail", "NewCard", "Notifications", "Settings"]),
    ("onboarding", "2 · Account opening", "rOnb", "Account opening (KYB + KYC), then approval and plan",
     ["Welcome", "SignUp", "Otp", "Company", "CompanyDocs", "Director", "Owners", "Review", "Approved", "Plan"]),
    ("accounts", "3 · Accounts & RIB", "rAcc", "Accounts and bank details", ["Accounts", "AccountDetails", "NewSubAccount", "Statements"]),
    ("topup", "4 · Top up", "rTop", "Top up: Wave, Orange Money, card, bank transfer, cash", ["TopUp", "TopUpWave", "TopUpConfirm", "TopUpSuccess", "TopUpCard", "TopUpBank", "CashDeposit"]),
    ("send", "5 · Send money", "rSend", "Send money", ["Send", "NewRecipient", "SendAmount", "SendReview", "SendSuccess"]),
    ("bulk", "6 · Bulk payouts", "rBulk", "Bulk payouts and payroll", ["Bulk", "BulkNew", "BulkPick", "BulkReview", "BulkApproval", "BulkDone"]),
    ("bills", "7 · Bills", "rBills", "Bill payments", ["Bills", "BillPay", "BillSuccess"]),
    ("team", "8 · Team & approvals", "rTeam", "Team, permissions and approvals", ["Team", "Invite", "Permissions", "Approvals"]),
    ("soon", "9 · Coming soon", "rSoon", "Coming soon: international, payment links, budget cards, accounting, financing",
     ["Intl", "PayLinks", "BudgetCards", "Accounting", "Financing", "LoanOffer", "Factoring"]),
]


def links_ok():
    bad = []
    for f, h in S.items():
        for href in re.findall(r'href="([^"#][^"]*\.dc\.html)"', h):
            if href not in S:
                bad.append((f, href))
    assert not bad, bad


def index(created_at, heights):
    boards, order, notes = {}, [], {}
    for pid, pname, rid, title, names in ROWS:
        for i, n in enumerate(names):
            f = f"{n}.dc.html"
            assert f in S, f
            boards[f] = {"x": i * (W + 80), "y": 0, "w": W, "h": heights.get(f, 900), "title": TITLES[f], "radius": 16,
                         "is_interactive": True, "expand": "fill", "page": pid}
            order.append(f)
        notes[rid] = {"x": 0, "y": -300, "text": title, "kind": "title1", "maxW": max(len(names) * (W + 80) - 80, 1400), "page": pid}
    notes["nPlay"] = {"x": 0, "y": -900, "w": 520, "fill": "blue", "page": "home",
                      "text": "Kelen web app: the same flows, features and content as the Kelen mobile app, laid out for a computer.\n\n"
                              "Open 'Accueil' and press Play to click through. The side menu reaches every section; tasks (send, top up, payroll, bills, new card, invitations) open full screen with a close button, like on mobile.\n\n"
                              "Style: Kelen V5 teal (light grey, glass cards, graphite text, teal #0D7377, Geist). The teal can be changed on any screen with Tweaks."}
    notes["nOnb"] = {"x": 0, "y": -900, "w": 520, "fill": "yellow", "page": "onboarding",
                     "text": "Account opening on the web: brand panel on the left with the 4 steps, form on the right. Same steps and documents as on mobile; the selfie can be done with the webcam or on the phone by QR code."}
    missing = set(S) - set(order)
    assert not missing, missing
    return {"v": 3, "createdOnFiles": {"v": 1, "at": created_at}, "title": "Kelen Web App", "launch": {"view": "canvas", "page": "home"},
            "pages": [{"id": pid, "name": pname} for pid, pname, *_ in ROWS], "boards": boards, "order": order, "notes": notes, "designSystems": []}


if __name__ == "__main__":
    root = sys.argv[1]
    created = sys.argv[2]
    heights = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else {}
    os.makedirs(os.path.join(root, "project"), exist_ok=True)
    links_ok()
    for f, h in S.items():
        if f in heights:
            h = h.replace('"$preview":{"width":1440,"height":900}', f'"$preview":{{"width":1440,"height":{heights[f]}}}')
        open(os.path.join(root, "project", f), "w").write(h)
    json.dump(index(created, heights), open(os.path.join(root, "project", "canvas.json"), "w"), ensure_ascii=False, indent=2)
    print(len(S), "screens")
