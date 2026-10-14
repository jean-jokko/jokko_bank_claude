"""Build the Kelen market and competitor analysis page (one HTML file, tabs) from the research packs A-D."""
import sys

OUT = sys.argv[1]


def L(url, label="source"):
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'


def P(level):
    k = level.lower().replace(" ", "").replace("-", "")
    cls = {"high": "high", "mediumhigh": "mh", "medium": "med", "lowmedium": "lm", "low": "low", "none": "none",
           "partner": "ok", "yes": "ok", "verified": "ok", "estimate": "tbc", "unverified": "tbc"}.get(k, "med")
    return f'<span class="pill {cls}">{level}</span>'


def T(head, rows, cls="", first_is_row=True):
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    body = []
    for r in rows:
        if isinstance(r, str):
            body.append(f'<tr class="sec"><th colspan="{len(head)}" scope="colgroup">{r}</th></tr>')
            continue
        cells = []
        for i, c in enumerate(r):
            if i == 0 and first_is_row:
                cells.append(f'<th scope="row">{c}</th>')
            else:
                cells.append(f"<td>{c}</td>")
        body.append("<tr>" + "".join(cells) + "</tr>")
    return f'<div class="tw"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{"".join(body)}</tbody></table></div>'


def KPI(items):
    return '<div class="kpis">' + "".join(
        f'<div class="kpi"><div class="kl">{a}</div><div class="kv">{b}</div><div class="ks">{c}</div></div>' for a, b, c in items) + "</div>"


def CARDS(items):
    return '<div class="cards">' + "".join(f'<div class="card"><h4>{a}</h4><p>{b}</p></div>' for a, b in items) + "</div>"


def UL(items):
    return "<ul class=\"list\">" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def FACTS(rows):
    return '<dl class="facts">' + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in rows) + "</dl>"


# --------------------------------------------------------------------------------------------
# Sources used inline
S = dict(
    bceao_inc="https://www.bceao.int/sites/default/files/2026-06/Rapport_Annuel_Inclusion_Financiere_2024.pdf",
    bceao_dfs="https://www.bceao.int/sites/default/files/2026-03/Rapport%20annuel%20sur%20les%20services%20financiers%20num%C3%A9riques%20dans%20l'UEMOA%20-%202024.pdf",
    bceao_cdb="https://www.bceao.int/sites/default/files/2025-07/Rapport%20sur%20les%20conditions%20de%20banque%20dans%20l'UEMOA%20-%202024_compressed.pdf",
    cb2025="https://www.cb-umoa.org/sites/default/files/RAPPORT%20ANNUEL%202025%20DE%20LA%20COMMISSION%20BANCAIRE.pdf",
    cb_lists="https://www.cb-umoa.org/sites/default/files/Liste%20%20des%20EME%20ET%20EP%20de%20l%27UMOA%202026.pdf",
    ep_list="https://www.bceao.int/sites/default/files/2026-03/LISTE%20DES%20ETABLISSEMENTS%20DE%20PAIEMENT%20AGR%C3%89%C3%89S%20DANS%20L%E2%80%99UMOA%20au%2031%20janvier%202026.pdf",
    wb_api="https://api.worldbank.org/v2/country/SEN;CIV/indicator/NY.GDP.MKTP.CD",
    findex="https://api.worldbank.org/v2/country/SEN;CIV/indicator/account.t.d?source=28",
    wbes_sn="https://www.enterprisesurveys.org/content/dam/enterprisesurveys/documents/country/Senegal-2024.pdf",
    wbes_ci="https://www.enterprisesurveys.org/content/dam/enterprisesurveys/documents/country/Cote-Divoire-2023.pdf",
    mefp="https://www.economie.gouv.sn/sites/default/files/2026-04/SENEGAL_Developpements_economiques_recents_et_Perspectives.pdf",
    imf_sn="https://www.imf.org/en/news/articles/2026/09/01/pr26282-senegal-imf-reaches-sla-ecf-arrangement",
    imf_ci="https://www.imf.org/fr/news/articles/2026/04/30/pr-26132-cote-divoire-imf-reaches-agreement-on-6th-rev-of-eff-ecf-arrange-5th-rev-of-rsf-arrange",
    anstat="https://media-files.abidjan.net/document/docs/document_fb9nxv55e5k.pdf",
    ipres="https://www.senegal24news.com/societe/revenu-salaires-au-senegal-hausse-des-adherents-a-lipres-en-2024/",
    cnps="https://www.gouv.ci/actualite/protection-sociale-environ-12-million-de-travailleurs-du-secteur-prive-et-pres-dun-million-de-travailleurs-independants-declares-a-la-cnps-2374",
    payroll_sn="https://www.sikafinance.com/premium/senegal-la-masse-salariale-du-secteur-prive-formel-a-franchi-1-500-milliards-fcfa-en-2024_60395",
    cepici="https://www.aip.ci/325086/",
    ansd_ninea="https://senego.com/pres-de-22-000-milliards-generes-en-2024-mais-lansd-releve-une-baisse-sur-ce-registre-specifique_1932453.html",
    endes="https://www.ansd.sn/actualite/lansd-presente-les-resultats-de-lenquete-nationale-sur-la-demographie-des-entreprises-du",
    arrears="https://www.capmad.com/article/senegal-le-gouvernement-reconnait-1-956-milliards-fcfa-darrieres-dus-aux-entreprises-et-promet-un-apurement-prioritaire",
    arrears2="https://www.dakaractu.com/Apurement-de-la-dette-interieure-300-milliards-FCFA-envers-les-entreprises-d-ici-fin-2026-MEFP_a276772.html",
    pispi_launch="https://www.bceao.int/fr/content/lancement-officiel-de-la-plateforme-interoperable-du-systeme-de-paiement-instantane-pi-spi",
    pispi_fa="https://www.financialafrik.com/2026/10/04/la-bceao-rend-pi-spi-obligatoire-revoit-ses-tarifs-et-pose-enfin-la-question-de-nouveaux-services-financiers-adosses-a-la-plateforme/",
    pispi_jecos="https://www.lejecos.com/PI-SPI-Le-piege-tarifaire-de-Wave_a31598.html",
    pispi_175="https://www.financialafrik.com/2026/10/01/bceao-liste-des-175-participants-autorises-a-ouvrir-les-services-de-pi-spi-au-public-au-30-septembre-2026/",
    tta="https://www.orange.sn/assistance/tutoriels/informations-sur-lapplication-de-la-loi-sur-la-collecte-de-taxes-sur-le",
    fne="https://www.koaci.com/article/2026/08/26/cote-divoire/economie/cote-divoire-operation-de-controle-de-la-facturation-normalisee-electronique-a-partir-du-1er-septembre-voici-les-entreprises-visees_199883.html",
    usury="https://www.bceao.int/sites/default/files/2026-01/Decision-No19-du-29-12-2025_CMUMOA_fixant_le_taux_de_l-usure.pdf",
    usury_sfd="https://www.bceao.int/fr/documents/taux-dusure-pour-les-operations-de-credit-des-sfd-dans-la-zone-umoa",
    mf_law="https://www.vie-publique.sn/documents/5534/loi-portant-reglementation-de-la-microfinance",
    ep_deadline="https://news.abidjan.net/articles/742142/umoa-la-bceao-prolonge-le-delai-de-mise-en-conformite-pour-les-services-de-paiement-jusquau-31-aout-2025",
    partech="https://partech-admin.prod.unomena.io/media/documents/2025_Partech-Africa-Tech-VC-Report.pdf",
    cash_pay="https://osiris.sn/numerisation-du-paiement-9-travailleurs-sur-10-au-senegal-sont-payes-en-especes.html",
    julaya="https://julaya.co", julaya_px="https://julaya.co/fr/prices", julaya_tx="https://julaya.co/fr/products/transfer",
    julaya_rib="https://julaya.co/fr/features/iban", julaya_acc="https://julaya.co/fr/features/accessibility-levels",
    julaya_cdc="https://www.ecofinagency.com/news-finances/2110-49719-julaya-secures-cfa800mln-from-cdc-ci-capital-for-regional-expansion",
    julaya_5m="https://techcabal.com/2022/09/21/west-african-fintech-julaya-raises-us5m-extension-round-to-expand-its-operations/",
    djamo_b="https://www.djamo.com/fr-ci/compte-business", djamo_px="https://www.djamo.com/fr-ci/tarifs-business",
    djamo_api="https://www.djamo.com/fr-ci/api", djamo_credit="https://www.djamo.com/fr-ci/credit",
    djamo_tc="https://techcrunch.com/2025/04/03/djamo-raises-17m-and-has-1m-users-across-francophone-africa",
    djamo_40="https://itweb.africa/article/djamo-targets-francophone-africa-with-40m-raise/nWJad7bNlr47bjO1",
    djamo_sn="https://directactu.net/2026/04/02/djamo-senegal-la-fintech-qui-revolutionne-linclusion-financiere-par-le-digital/",
    djamo_mfi="https://www.ecofinagency.com/finance/1209-48632-ivorian-fintech-djamo-breaks-new-ground-with-bceao-microfinance-approval",
    wave_b="https://www.wave.com/fr/business/", wave_api="https://docs.wave.com/payout",
    wave_bank="https://www.ecofinagency.com/news-finances/2610-49842-wave-launches-commercial-bank-in-cote-d-ivoire",
    wave_ci="https://www.abidjaneconomie.net/2026/05/04/wave-ci-bilan-2025/",
    wave_fa="https://www.financialafrik.com/2026/08/30/telecoms-et-fintechs-a-lassaut-de-la-banque-lumoa-peut-elle-encore-attendre-la-rupture/",
    wave_int="https://www.financialafrik.com/2026/02/18/entretien-exclusif-avec-el-hadji-malick-gueye-directeur-general-de-wave-digital-finance/",
    wave_debt="https://fintechnews.africa/45533/senegal/wave-137m-debt-funding/",
    wave_card="https://www.financialafrik.com/2026/01/24/senegal-wave-lance-une-carte-virtuelle-avec-visa-et-ecobank/",
    om_sn="https://www.orangebusiness.sn/orange-money", om_ci="https://business.orange.ci/fr/b2b-orangemoney-nossolutions.html",
    om_ci_sal="https://business.orange.ci/business/resources/other/annexes_paiement_salaire.pdf",
    om_business="https://www.agenceecofin.com/actualites-services/2106-139474-orange-money-ci-lance-om-business-pour-accelerer-la-digitalisation-des-commerces-et-pme",
    oba_ifc="https://www.ecofinagency.com/news-finances/0302-52548-ifc-to-provide-30-6m-guarantee-for-orange-bank-digital-lending-in-cote-d-ivoire-senegal",
    oba_sgpme="https://www.ecofinagency.com/news-finances/2607-57726-cote-d-ivoire-s-sme-agency-orange-bank-sign-guarantee-agreements-to-expand-sme-lending",
    sonatel="https://sonatel.sn/wp-content/uploads/2026/03/BRVM-FY-2025-FR-VF.pdf",
    mixx="https://yas.sn/mixx-by-yas/", mtn="https://www.koaci.com/article/2025/09/02/cote-divoire/economie/cote-divoire-mobile-money-pour-contrer-wave-et-se-relancer-mtn-tente-le-pari-du-0-de-frais_189861.html",
    mtn_ecomatin="https://ecomatin.net/mobile-money-mtn-cote-divoire-tente-le-0-de-frais-pour-contrer-wave",
    moov="https://www.koaci.com/article/2026/07/16/cote-divoire/societe/cote-divoire-20-ans-de-moov-africa-cote-divoire-loperateur-voit-grand-et-accelere-sa-revolution-digitale_198629.html",
    wizall="https://www.wearetech.africa/fr/fils/solutions/senegal-wizall-money-propose-des-services-financiers-aux-entreprises-et-aux-particuliers",
    intouch="https://burkina24.com/2025/07/04/communique-le-groupe-intouch-acquiert-des-licences-detablissement-de-paiement-et-detablissement-de-monnaie-electronique-dans-la-zone-uemoa/",
    intouch2="https://www.osiris.sn/intouch-10-ans-d-innovation-pour-revolutionner-les-paiements-en-afrique.html",
    paydunya="https://paydunya.com/service-fees", peach="https://www.peachpayments.com/scale/peach-payments-acquires-west-african-payments-gateway-paydunya",
    cinetpay="https://cinetpay.com/pricing", cinetpay_inc="https://techcabal.com/2026/02/01/cinetpay-cyberattack/",
    paytech="https://paytech.sn/", paystack="https://support.paystack.com/en/articles/2130306",
    flw="https://flutterwave.com/sn/pricing", bizao="https://launchbaseafrica.com/2025/06/18/french-court-orders-compulsory-liquidation-of-ivorian-founded-fintech-bizao/",
    hub2="https://www.financialafrik.com/2026/02/25/ecobank-et-hub2-elargissent-lacces-aux-paiements-numeriques-a-200-millions-dutilisateurs-de-portefeuilles-mobiles-en-afrique-francophone/",
    kkiapay="https://kkiapay.me/tarifs/", naboo="https://naboopay.com/",
    kayfay="https://kayfay.com/", facturesn="https://facturesn.com/",
    fintra="https://www.agenceecofin.com/entreprendre/1710-102091-des-avances-sur-salaires-grace-a-fintra-l-application-concue-par-le-senegalais-oumar-diallo",
    barapay="https://barapay.africa/", flash="https://www.financialafrik.com/2024/11/20/mastercard-collabore-avec-new-africa-technology-pour-lancer-un-programme-de-cartes-fintech-au-senegal-en-cote-divoire-et-au-benin",
    uba_sn="https://comparek.sn/banques/produits/compte-entreprise",
    bnde="https://www.bnde.sn/sites/default/files/2025-03/CONDITIONS%20DE%20BANQUE%20Entreprises%202025%20VF.pdf",
    bis="https://bis-bank.com/wp-content/uploads/2024/09/Conditions-de-banque-Juin-2024.pdf",
    coris="https://senegal.coris.bank/wp-content/uploads/2020/01/Conditions_de_banque-CBI-SN.pdf",
    cbao="https://cbaobank.com/sites/default/files/Conditions%20_de%20_banque_2023.pdf",
    boa="https://www.boasenegal.com/wp-content/uploads/2026/06/Conditions-de-banque-Particuliers-2026.pdf",
    sgci="https://societegenerale.ci/fileadmin/user_upload/SG_Cote_ivoire/Home_Reboot/Pdf/CONDITIONS_BANCAIRES_ENTREPRISES_JANVIER_2026.pdf",
    uba_ci="https://www.ubacotedivoire.com/wp-content/uploads/sites/12/2026/04/Conditions-tarifaires-Entreprises-UBA-CI-2026.pdf",
    orabank="https://www.orabank.net/sites/default/files/2026-06/B-TARIFS%20DES%20PRODUITS%20ET%20SERVICES%20OFFERTS%20%C3%80%20LA%20CLIENT%C3%88LE%20DES%20PROFESSIONNELS,%20ENTREPRISES.pdf",
    sunu="https://www.seneweb.com/fr/news/Economie/changement-de-denomination-sociale-la-bicis-devient-officiellement-sunu-bank-senegal_n_472135.html",
    sg_sn="https://lesoleil.sn/actualites/economie/banque-letat-envisage-lacquisition-de-la-societe-generale-senegal/",
    ecobank_omni="https://ecobank.com/commercial-banking/omni-lite",
    mf_sn="https://fr.allafrica.com/stories/202610020112.html", mf_shares="https://fr.allafrica.com/stories/202602090430.html",
    mf_count="https://fr.allafrica.com/stories/202510310535.html",
    advans="https://www.advanscotedivoire.com/professionnels/emprunter/credits-pme/",
    cofina_ci="https://www.cofinacotedivoire.com/cofina/nos-performances/", cofina_sn="https://www.cofinasenegal.com/nos-produits/offres-de-credits/",
    baobab="https://www.techinafrica.com/beltone-holding-completes-e197-6m-acquisition-of-baobab-group/",
    baobab_kit="https://baobab.com/wp-content/uploads/2026/08/Kit-Presse_2026_800x600_FR.pdf",
    microsen="https://www.financialafrik.com/2025/03/27/senegal-sf-capital-finalise-lacquisition-de-microsen-sa/",
    kajas="https://www.horonyafinance.com/witti-finances-holding-acquiert-kajas-microfinance-au-senegal-et-renforce-sa-strategie-dexpansion-dans-la-zone-uemoa/",
    cgap="https://www.cgap.org/sites/default/files/CGAP-Occasional-Paper-Shedding-Light-on-Microfinance-Equity-Valuation-Past-and-Present-Feb-2009.pdf",
    cms="https://www.cms.sn/qui-sommes-nous/",
    qonto="https://qonto.com/fr/pricing", qonto_res="https://www.boursedescredits.com/actualite-resultats-2025-fintech-francaise-qonto-confirme-rentabilite-voit-benefice-reculer-36-29808.php",
    qonto_s="https://sifted.eu/articles/qonto-results-2024",
    revolut="https://www.revolut.com/en-US/news/revolut_reports_record_profit_of_2_3bn_for_2025_as_revenue_surges_to_6bn/",
    mercury="https://mercury.com/blog/annual-letter-2025", mercury2="https://www.americanbanker.com/news/mercury-raises-200-million-after-occ-bank-charter-approval",
    moniepoint="https://www.techinafrica.com/moniepoint-hits-unicorn-status-massive-250m-series-c/",
    moniepoint2="https://techcabal.com/2026/03/26/nigerias-moniepoint-enters-kenya-with-78-stake-in-sumac-microfinance/",
    moniepoint3="https://www.itedgenews.africa/moniepoint-disburses-₦1t-in-sme-credit-processes-₦412tr-transactions-in-2025/",
    kuda="https://www.techinafrica.com/neobank-kuda-triples-revenue-as-customer-adoption-soars/",
    tyme="https://www.fintechfutures.com/venture-capital-funding/tyme-group-achieves-unicorn-status-with-250m-series-d-led-by-nubank",
    mpesa="https://tech-ish.com/2026/05/07/safaricom-fy26-mpesa-results-explained/",
    stack="https://businessday.ng/technology/article/a-decade-on-flutterwave-paystack-and-moniepoint-compete-for-africas-financial-plumbing/",
    ramp="https://sacra.com/c/ramp/",
    wave_tc="https://techcrunch.com/2021/09/06/sequoia-heritage-stripe-and-others-invest-200m-in-african-fintech-wave-at-1-7b-valuation",
    ci_rge="https://www.koaci.com/article/2025/05/16/cote-divoire/societe/cote-divoire-recensement-general-des-entreprises-et-etablissements-un-peu-plus-de-12-million-dentreprises-formelles-et-informelles-repertoriees_186913.html",
    datareportal_sn="https://datareportal.com/reports/digital-2026-senegal", datareportal_ci="https://datareportal.com/reports/digital-2026-cote-divoire",
    elect="https://www.letemps.ch/monde/en-cote-d-ivoire-le-president-alassane-ouattara-est-reelu-pour-un-4e-mandat-avec-89-77-des-voix",
)
s = lambda k, lab="source": L(S[k], lab)

tabs = []

# --------------------------------------------------------------------------------------------
# 1. SUMMARY
summary = KPI([
    ("Formal employers, Senegal", "40,300", f"Contributing to IPRES in 2024, +4.9% a year · {s('ipres')}"),
    ("Formal employers, Côte d'Ivoire", "≈49,000", f"CNPS declared companies, 2025 (unverified) · {s('cnps')}"),
    ("Formal private payroll, Senegal", "1,540bn FCFA", f"€2.35bn a year, 2024 (ANSD) · {s('payroll_sn')}"),
    ("Mobile money flows, 2024", "104,000bn FCFA", f"Senegal 48,500bn + CI 55,700bn · {s('bceao_dfs')}"),
    ("Direct competitors licensed in both", "2", "Julaya and Djamo hold payment licences in Senegal and Côte d'Ivoire"),
]) + """
<h3>Verdict</h3>
<p class="prose">The market is real and the gap Kelen targets still exists, but it is narrower than in 2024 and it is closing. Senegal has about 40,000 formal employers paying 1,540bn FCFA of salaries a year, and roughly two thirds of private wage earners already get paid by phone. Nobody yet combines a business account with its own IBAN, double-signature approvals, payouts to every bank and wallet, cards and SME credit in one subscription. Julaya comes closest on payroll and approvals, Djamo on cards and credit, and Wave owns the payout habit at 1%. Kelen wins only if it is clearly the most complete <em>control</em> product for a finance team, prices below the 1% that SMEs pay today, and reaches companies through accountants and payroll tools rather than through consumer marketing.</p>
<h3>Ten findings that matter</h3>
""" + UL([
    "<b>Julaya is the closest competitor.</b> It is licensed in Senegal and Côte d'Ivoire and already offers payroll and supplier payouts to all banks and wallets (up to 3,000 at once), approval levels, sub-accounts, exports and its own RIB. It has no cards and no credit yet, and it raised 800M FCFA in October 2025 to build SME credit. It charges 0.5–1.5% per payout to wallets, with no subscription.",
    "<b>Djamo is the main price threat.</b> Its business account is free and bulk payouts from its web app are free. It also has employee cards, 2 million users and a microfinance licence in Côte d'Ivoire, and is raising a $40M Series C. Its business tools are thin: no documented roles, approvals or sub-accounts, and its API only pays Djamo accounts.",
    "<b>Wave sets the price SMEs compare against: 1% per payout, free for the recipient.</b> It has no IBAN, no bank payouts, no approvals and no credit. Wave Bank Africa (20bn FCFA capital) is incorporated in Abidjan but not yet licensed. If it is licensed, Wave becomes the biggest long-term threat.",
    "<b>Orange is entering SME banking in Côte d'Ivoire.</b> The OM Business app launched in June 2026 with credit from Orange Bank Africa, which has 3 million clients and a 17bn FCFA SME guarantee line. In Senegal, Orange charges 1% / 1.5% for salary and supplier payments, with settlement in 5 days.",
    "<b>Banks are expensive but not absurd.</b> A 10-employee SARL pays about 35,000–52,500 FCFA a month in account, online banking and transfer fees. Opening takes 7–15 working days and a branch visit. No bank offers self-service onboarding with approvals, invoicing and cards at a flat price.",
    "<b>PI-SPI, the BCEAO's instant-payment system, is the biggest structural change.</b> It is mandatory from 2 November 2026 and connects 175 banks, wallets and payment institutions, Wave included since 30 September 2026. Through its partner bank, Kelen can reach every wallet and bank at low cost. That makes a flat subscription that includes payouts possible.",
    "<b>Payroll in Senegal is already digital; in Côte d'Ivoire it is still cash.</b> About 64% of Senegal's private wage earners are paid by phone, but 57% of Côte d'Ivoire's are paid in cash only. Côte d'Ivoire has more room for payroll digitisation; Senegal has more firms ready to switch provider.",
    "<b>Credit is the SME's first problem.</b> In Senegal, 45.9% of firms name access to finance as their biggest obstacle, against a 30.8% Sub-Saharan average. Only 10.8% of small firms use banks to fund investment. Invoice financing is unoccupied, and the SFD lending cap is 24% all-in (TAEG).",
    "<b>Senegal's macro picture is weaker than when the plan was drafted.</b> Growth is forecast at about 2.5% in 2026 and the IMF programme is still pending Board approval. The State owes companies 1,956bn FCFA in arrears, and only 300bn is promised by end-2026. Expect slower sales cycles, more late payments and stronger demand for working-capital credit.",
    "<b>The plan's Senegal client target looks ambitious.</b> 7,650 active clients in year 5 is 27% of the plan's own target market and 27–38% of the estimated 20,000–28,000 digital-ready Senegalese SMEs. Julaya, after six years, had about 2,800 active users in Senegal in 2024. See the Positioning tab.",
]) + """
<h3>Threat map</h3>
""" + T(["Player", "Type", "What it does best", "Missing for an SME finance team", "Threat"], [
    ["Julaya", "B2B payments, licensed SN + CI", "Payroll and supplier payouts to banks and all wallets, approvals, sub-accounts", "Cards, credit, invoices, employee accounts", P("High")],
    ["Djamo Business", "Neobank, licensed SN + CI, MFI in CI", "Free account, free bulk pay, employee cards, consumer credit", "Roles, approvals, sub-accounts, payouts beyond Djamo accounts", P("High")],
    ["Wave Business", "E-money (EME), bank pending", "1% bulk payouts, free cash-out, merchant QR, API", "IBAN, bank payouts, approvals, invoices, credit", P("High")],
    ["Orange Money + Orange Bank Africa", "Telco wallet + bank", "Reach, SME credit with guarantees (CI), Paiement Pro", "Multi-bank payouts, approvals, banking UX, fast settlement", P("Medium-High")],
    ["Banks (CBAO, SG, Ecobank, BIS, UBA…)", "Banks", "IBAN, cards, credit, trust", "Speed, self-service, wallet payouts, flat pricing", P("Medium")],
    ["InTouch, PayDunya, HUB2, CinetPay…", "Aggregators", "Collections and payouts by API", "Accounts, approvals, payroll product", P("Low")],
    ["Payroll and invoicing SaaS (KayFay, Facture SN)", "Software", "Payslips, IPRES/CSS, invoices", "Payment rail", P("Low")],
])
tabs.append(("summary", "Summary", "What the research says about Kelen's market and competitors, in one page. Research date 14 October 2026; every figure has its source in the detailed tabs.", summary))

# --------------------------------------------------------------------------------------------
# 2. MARKET
market = """<h3>Economy</h3>""" + T(["Indicator", "Senegal", "Côte d'Ivoire", "Year", "Source"], [
    ["Population", "18.9M", "32.7M", "2025", s("wb_api", "World Bank")],
    ["Urban share", "55.8%", "54.5%", "2025", s("wb_api", "World Bank")],
    ["GDP", "21,535bn FCFA ($37.0bn)", "58,061bn FCFA ($99.8bn)", "2025", s("mefp", "MEFP") + " · " + s("wb_api", "WB")],
    ["GDP per person", "$1,955", "$3,050", "2025", s("wb_api", "World Bank")],
    ["Real growth", "6.5–6.7% (oil); 2.2% without hydrocarbons", "6.5%", "2025", s("imf_sn", "IMF") + " · " + s("imf_ci", "IMF")],
    ["Growth forecast", "≈2.5%", "≈6.0%", "2026", s("mefp", "MEFP") + " · " + s("imf_ci", "IMF")],
    ["Inflation", "1.4%", "0.1% (3.3% forecast 2026)", "2025", s("wb_api", "World Bank")],
    ["Public debt", "132% of GDP (IMF, end-2024, before rebasing)", "Moderate, IMF programme on track", "2024", s("imf_sn", "IMF")],
    ["IMF status", "New $2.2bn programme agreed at staff level 1 Sept 2026; Board approval pending", "Final review of 2023–26 programme agreed Apr 2026", "2026", s("imf_sn", "IMF") + " · " + s("imf_ci", "IMF")],
    ["BCEAO policy rate", "3.0% (cut 25bp, Mar 2026)", "same (monetary union)", "2026", s("mefp", "MEFP")],
]) + """
<h3>Businesses: who Kelen can serve</h3>""" + T(["Indicator", "Senegal", "Côte d'Ivoire", "Year", "Source"], [
    ["Formal employers (social security)", "<b>40,300</b> IPRES employers (38,381 in 2023)", "<b>≈49,000</b> CNPS declared companies " + P("Unverified"), "2024–25", s("ipres", "IPRES") + " · " + s("cnps", "gouv.ci")],
    ["Declared private-sector employees", "577,171 IPRES contributors", "≈1.2M declared at CNPS (another source: 975,000)", "2024–25", s("ipres", "IPRES") + " · " + s("cnps", "gouv.ci")],
    ["Formal / modern-sector firms", "20,388 units, 93.7% SMEs", "82,548 formal firms: 67% micro, 28% SME, 5% large", "2022–24", s("ansd_ninea", "ANSD") + " · " + s("anstat", "ANStat")],
    ["All economic units (census)", "407,882 (2016; 97% informal). New census under way", "≈1.2M (2025 census, 75% complete); ≈600k in Abidjan", "2016 / 2025", s("ci_rge", "KOACI")],
    ["New companies a year", "91,936 NINEA registrations (73% sole traders); ≈18,000 companies via APIX", "26,948 companies (CEPICI), 21,538 of them SARL", "2024–25", s("ansd_ninea", "ANSD") + " · " + s("cepici", "CEPICI")],
    ["Geographic concentration", "Dakar share not published", "Abidjan holds 72% of formal firms", "2022", s("anstat", "ANStat")],
    ["Sector mix", "Commerce 64% of new registrations", "Commerce 44%, construction 10%, manufacturing 8%, professional services 7%", "2022–24", s("anstat", "ANStat")],
    ["Firm survival", "57% of 2018 firms still active in 2024; 63% of never-started firms cite lack of financing", "Not found", "2024", s("endes", "ANSD ENDES")],
    ["Formal private payroll", "<b>1,540bn FCFA</b> (≈128bn a month; ≈382,000 FCFA per employee a month)", "≈2,200–4,300bn FCFA " + P("Estimate"), "2024", s("payroll_sn", "ANSD via Sika")],
]) + """
<h3>Market size for Kelen</h3>
<p class="prose">Kelen's core market is formal employers that pay staff every month, sit in a large city and already use a phone for money. The estimates below use formal employers × 60–75%, excluding the 4–5% of large firms. That ratio reflects that about 90% of small formal firms already hold a bank account, and that firms cluster in Dakar and Abidjan. It is a rough figure to test in interviews.</p>
""" + T(["Layer", "Senegal", "Côte d'Ivoire", "Both", "How it is built"], [
    ["Formal employers (total market)", "40,300", "≈49,000", "≈89,000", "IPRES and CNPS counts"],
    ["Digital-ready SMEs (serviceable market)", "20,000–28,000", "25,000–35,000", "45,000–63,000", "Employers × 60–75%, large firms excluded " + P("Estimate")],
    ["Kelen's business plan target market (year 5)", "28,165", "42,213", "70,378", "Plan: formal employers growing 4.9–5% a year × 50%"],
    ["Kelen active clients in the plan (year 5)", "7,652 (27% of plan target)", "3,283 (8% of plan target)", "10,935", "Business plan, base scenario"],
    ["Payroll that would flow through 1,000 clients", "≈3–4bn FCFA a month", "—", "—", "1,000 × 10–15 staff × ≈250–380k FCFA"],
    ["Revenue pool: account fees alone", "≈4.2bn FCFA a year", "—", "—", "Plan's target companies × 15,000 FCFA a month bank fee"],
], cls="sz") + """
<h3>Financial inclusion and payments</h3>""" + T(["Indicator", "Senegal", "Côte d'Ivoire", "Year", "Source"], [
    ["Adults with a bank account (BCEAO strict rate)", "23.1%", "33.6%", "2024", s("bceao_inc", "BCEAO")],
    ["…including microfinance", "62.4%", "46.2%", "2024", s("bceao_inc", "BCEAO")],
    ["…including e-money (all financial services)", "85.9%", "86.7%", "2024", s("bceao_inc", "BCEAO")],
    ["Any account (Findex)", "76.5%", "57.6%", "2024", s("findex", "Findex")],
    ["Mobile money account (Findex)", "66.9%", "53.4%", "2024", s("findex", "Findex")],
    ["Debit card owned", "32.7%", "7.0%", "2024", s("findex", "Findex")],
    ["Borrowed from a formal institution", "17.6%", "3.9%", "2024", s("findex", "Findex")],
    ["E-money accounts opened / active (90 days)", "42.6M / 14.6M", "99.6M / 26.4M", "2024", s("bceao_dfs", "BCEAO")],
    ["E-money transactions", "2.87bn, 48,500bn FCFA (2.5× GDP)", "2.55bn, 55,700bn FCFA (1× GDP)", "2024", s("bceao_dfs", "BCEAO")],
    ["Merchants registered for QR payment", "412,172", "2,719,463", "2024", s("bceao_dfs", "BCEAO")],
    ["Salaries paid by e-wallet (whole union)", "891bn FCFA, 28M payments, average 31,185 FCFA", "", "2024", s("bceao_dfs", "BCEAO")],
    ["Banks / large microfinance institutions", "33 / 81", "33 / 43", "2025", s("cb2025", "Commission Bancaire")],
    ["E-money issuers / payment institutions licensed", "5 / 12", "4 / 10", "Jun 2026", s("cb_lists", "CB-UMOA lists")],
    ["PI-SPI participants", "43", "38", "30 Sep 2026", s("pispi_175", "Financial Afrik")],
]) + """
<h3>Digital readiness</h3>""" + T(["Indicator", "Senegal", "Côte d'Ivoire", "Year", "Source"], [
    ["Adults whose main phone is a smartphone", "60.8%", "45.7%", "2024", s("findex", "Findex")],
    ["Internet users", "60.6% (11.5M)", "40.7% (13.4M)", "2025", s("datareportal_sn", "DataReportal") + " · " + s("datareportal_ci", "DataReportal")],
    ["Mobile connections", "23.3M (122%), 91% on 3G/4G/5G", "49.7M (151%)", "2025", s("datareportal_sn", "DataReportal") + " · " + s("datareportal_ci", "DataReportal")],
]) + """
<h3>Fintech funding</h3>""" + T(["", "Senegal", "Côte d'Ivoire", "Note", "Source"], [
    ["Tech venture funding 2025", "$223M (equity 84, debt 139; mostly one Wave debt facility)", "$22M", "Francophone Africa outside the big four: $252M equity", s("partech", "Partech 2025")],
])
tabs.append(("market", "Market", "Size of the opportunity in Senegal and Côte d'Ivoire: economy, companies, payroll, banking access and payments.", market))

# --------------------------------------------------------------------------------------------
# 3. SME NEEDS
needs = """<h3>What SMEs say holds them back</h3>""" + T(["Indicator (World Bank Enterprise Survey)", "Senegal (2024)", "Côte d'Ivoire (2023)", "What it means for Kelen"], [
    ["Access to finance is the biggest obstacle", "<b>45.9%</b> (small firms 49.6%); #1 obstacle; Sub-Saharan average 30.8%", "21.6%; then political instability 19.5%, crime 13.4%", "Credit is the hook in Senegal. Payroll and cash-flow data can underwrite it."],
    ["Firms with a checking or savings account", "90.7%", "89.9%", "Formal SMEs are already banked. Kelen replaces or sits beside a bank; it does not bank the unbanked."],
    ["Small firms using banks to finance investment", "<b>10.8%</b>", "31.1%", "Banks lend to the top of the market. Small firms finance themselves."],
    ["Investment financed internally", "66.9% (small 86.0%)", "70.0%", "Working-capital products (invoice, payroll advance) fit better than term loans."],
    ["Firms using supplier or customer credit", "35.4%", "31.4%", "Late payment is normal; invoice financing has room."],
    ["Firms competing with informal firms", "55.2%", "76.5%", "Cost pressure: SMEs will compare every fee."],
], cls="wide") + f'<p class="cite">Sources: {s("wbes_sn", "WBES Senegal 2024")} · {s("wbes_ci", "WBES Côte d’Ivoire 2023")}</p>' + """
<h3>How salaries are paid today</h3>""" + T(["Private-sector wage earners (Findex 2024)", "Senegal", "Côte d'Ivoire", "Reading"], [
    ["Paid into a bank or financial institution account", "≈33% of earners (8.4% of adults)", "≈11% (1.9% of adults)", "Bank payroll is the minority."],
    ["Paid by mobile phone", "<b>≈64%</b> (16.4% of adults)", "≈33% (5.5% of adults)", "Senegal: payroll is already on wallets, mostly Wave. Kelen must pay out to wallets at least as cheaply."],
    ["Paid in cash only", "≈28% (7.2% of adults)", "<b>≈57%</b> (9.7% of adults)", "Côte d'Ivoire: the bigger digitisation opportunity, and a reason for agent cash-out codes."],
], cls="wide") + f'<p class="cite">Source: {s("findex", "Global Findex 2025")}. Includes informal wage earners. Older data (2018–21) found 9 in 10 Senegalese workers paid in cash and estimated the cost of cash payroll at 2–7% of the wage bill: {s("cash_pay", "World Bank / ANSD / BTCA")}.</p>' + """
<h3>Pain points Kelen's product answers</h3>""" + CARDS([
    ("Slow, paper-heavy account opening", "RCCM extract, notarised statutes, NINEA, IDs, signature specimens and a branch visit; 7–15 working days to a working card and RIB. A KYB in under 48 hours for registered companies beats every bank."),
    ("Fees billed line by line", "Banks bill account keeping (8,500–25,000), online banking (5,000–10,000) and 3,000–15,000 per interbank transfer. Bulk salary files cost 1,000 per line. Wallets take 1–1.5% of payroll."),
    ("Double signature on paper", "Senegalese firms run two-signature mandates. Wave and Orange business tools document no approval workflow; banks do it on paper or in corporate e-banking."),
    ("Paying staff on many rails", "Employees use Wave, Orange Money, Mixx, banks. Payroll tools (KayFay, Sage, Odoo) produce files but no payment."),
    ("Waiting to be paid", "The Senegalese State owes companies 1,956bn FCFA (end-March 2025 stock); construction is most exposed. Supplier credit is common."),
    ("No working capital", "Banks lend at about 7% to the SMEs they accept and require collateral; most small firms are refused and fund themselves."),
    ("E-invoicing obligations", "Côte d'Ivoire's normalised e-invoice (FNE) is enforced from 1 September 2026, with 52,000 firms registered. Senegal's timetable is still being set."),
    ("Spending control", "No local spend-management product (a Ramp or Spendesk equivalent) was found; field allowances still move as cash."),
]) + f'<p class="cite">Sources: {s("bnde", "BNDE tariffs 2025")} · {s("bis", "BIS tariffs 2024")} · {s("arrears", "arrears")} · {s("fne", "FNE")} · account opening (third-party guide, unverified).</p>' + """
<h3>Gaps in the evidence</h3>
<p class="prose">No survey was found on SME late payments, bank fees or account-opening time. Willingness to pay a monthly subscription has never been measured. Twenty to thirty interviews with Dakar SMEs and accountants would close this before launch.</p>"""
tabs.append(("needs", "SME needs", "What formal SMEs struggle with, how they pay salaries, and which of those problems Kelen solves.", needs))

# --------------------------------------------------------------------------------------------
# 4. RULES & SHIFTS
rules = T(["Change", "What it is", "Impact on Kelen", "Source"], [
    "Payments infrastructure",
    ["PI-SPI (BCEAO instant payments)", "Launched 30 Sept 2025. 175 participants at 30 Sept 2026, Wave included. <b>Mandatory for interoperable transfers from 2 Nov 2026.</b> Sends free up to 8,000 FCFA a day per user, 0–0.8% above (BCEAO communiqué via Financial Afrik). Another report: receivers get 30 free receipts a month, then fees capped at 1%. Cross-border on the same terms from 1 June 2027.", "Kelen can reach every bank and wallet through its partner bank at low cost. That makes a flat subscription that includes payouts viable. Confirm the business-sender tariff with the partner bank: the two reports differ.", s("pispi_launch", "BCEAO") + " · " + s("pispi_fa", "Financial Afrik") + " · " + s("pispi_jecos", "Le Jecos")],
    ["Payment-services licensing", "BCEAO Instruction 001-01-2024: any payment service needs a payment-institution (EP) licence. Unlicensed fintechs had to stop on 1 Sept 2025. Senegal: 12 EPs; Côte d'Ivoire: 10.", "Kelen launches as the partner's agent or technical provider, then needs its own licence or the SFD. Competitors already hold theirs.", s("ep_deadline", "Abidjan.net") + " · " + s("cb_lists", "CB-UMOA")],
    "Taxes and invoicing",
    ["Senegal transfer tax (TTA)", "0.5% on transfers, payments and withdrawals above 20,000 FCFA in 24 hours, capped at 2,000 FCFA per operation. In force Dec 2025. <b>Salary payments are exempt.</b>", "Helps payroll; supplier payouts carry the tax.", s("tta", "Orange notice")],
    ["Côte d'Ivoire e-invoicing (FNE)", "Normalised electronic invoice, phased since June 2025; controls from 1 Sept 2026; fines up to 10M FCFA. 52,000 firms registered by Feb 2026.", "Kelen's invoices must plug into FNE before the CI launch. Senegal's DGID timetable: reception 2026, issuing 2027 (unverified).", s("fne", "KOACI")],
    "Credit",
    ["Usury caps", "Banks: 15% → <b>14% from 1 June 2026</b>. Microfinance (SFD): <b>24%</b>, measured as an all-in rate (TAEG) including fees and insurance.", "Kelen's 23% loans leave about 1 point for all fees. Model loans on the all-in rate.", s("usury", "BCEAO decision 19") + " · " + s("usury_sfd", "BCEAO SFD")],
    ["Senegal microfinance law 2025", "SFDs become 'institutions de microfinance'; only SA or cooperative forms; licence from the Minister of Finance on a binding BCEAO opinion.", "Shapes the 2029 SFD acquisition: target an SA, plan the change-of-control file.", s("mf_law", "Vie publique")],
    "Market moves",
    ["Wave Bank Africa", "Incorporated in Abidjan, 20bn FCFA capital, Oct 2025. Licence 'still under review' (Apr 2026). Credit and savings announced Feb 2026, not launched.", "If licensed, Wave can offer accounts and SME credit to its whole base.", s("wave_bank", "Ecofin") + " · " + s("wave_ci", "Abidjan Économie")],
    ["Orange OM Business (CI)", "Launched 19 June 2026: QR, payment links, dashboard, credit via Orange Bank Africa.", "Orange targets the same SMEs in Côte d'Ivoire before Kelen arrives.", s("om_business", "Ecofin")],
    ["MTN exploring bank licences", "Announced Aug 2026; 0% app fees in CI since Aug 2025; MoMo Helep Pro salary advance (June 2026).", "Telcos are becoming banks.", s("wave_fa", "Financial Afrik")],
    "Macro",
    ["Senegal debt and arrears", "Hidden-debt crisis; new IMF programme pending Board approval; 1,956bn FCFA of arrears owed to firms, 300bn to be paid by end-2026.", "Slower sales cycles and higher credit risk in 2027; stronger demand for cash-flow tools and working capital.", s("imf_sn", "IMF") + " · " + s("arrears2", "MEFP via Dakaractu")],
    ["Côte d'Ivoire politics", "President re-elected Oct 2025 (89.77%); growth steady near 6%.", "Stable base for the month-19 launch.", s("elect", "Le Temps")],
], cls="wide")
tabs.append(("rules", "Regulation & shifts", "Rules and market moves that change the competitive picture between now and Kelen's launch.", rules))

# --------------------------------------------------------------------------------------------
# 5. LANDSCAPE (positioning map)
pts = [  # x = business control (approvals, roles, sub-accounts, accounting); y = banking depth (IBAN, cards, credit, deposits)
    ("Payment gateways", 18, 12, "o"), ("Wave Business", 26, 30, "o"), ("Orange Money + OBA", 22, 58, "o"),
    ("Djamo Business", 36, 64, "o"), ("Julaya", 72, 30, "o"), ("Banks", 50, 82, "o"), ("Kelen (target)", 84, 80, "k"),
]
W, H, PAD = 640, 420, 56
def px(x): return PAD + x / 100 * (W - PAD - 24)
def py(y): return H - PAD - y / 100 * (H - PAD - 24)
marks = []
for lab, x, y, k in pts:
    anchor = "end" if x > 70 else "start"
    dx = -14 if x > 70 else 14
    marks.append(f'<g class="pt {k}"><title>{lab}</title><circle cx="{px(x):.0f}" cy="{py(y):.0f}" r="{9 if k == "k" else 7}"/>'
                 f'<text x="{px(x) + dx:.0f}" y="{py(y) + 4:.0f}" text-anchor="{anchor}">{lab}</text></g>')
svg = f'''<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="pm-t pm-d">
<title id="pm-t">Positioning map</title><desc id="pm-d">Business control tools on the horizontal axis, banking depth on the vertical axis. Kelen targets the top right, where no competitor sits today.</desc>
<rect class="q" x="{px(50):.0f}" y="{py(100):.0f}" width="{px(100) - px(50):.0f}" height="{py(50) - py(100):.0f}"/>
<line class="grid" x1="{px(50):.0f}" x2="{px(50):.0f}" y1="{py(0):.0f}" y2="{py(100):.0f}"/>
<line class="grid" x1="{px(0):.0f}" x2="{px(100):.0f}" y1="{py(50):.0f}" y2="{py(50):.0f}"/>
<line class="axis" x1="{px(0):.0f}" x2="{px(100):.0f}" y1="{py(0):.0f}" y2="{py(0):.0f}"/>
<line class="axis" x1="{px(0):.0f}" x2="{px(0):.0f}" y1="{py(0):.0f}" y2="{py(100):.0f}"/>
<text class="ax" x="{px(50):.0f}" y="{H - 18}" text-anchor="middle">Business control: approvals, roles, sub-accounts, accounting →</text>
<text class="ax" transform="translate(18 {py(50):.0f}) rotate(-90)" text-anchor="middle">Banking depth: IBAN, cards, credit →</text>
<text class="qt" x="{px(98):.0f}" y="{py(97):.0f}" text-anchor="end">Open space</text>
{"".join(marks)}
</svg>'''
landscape = f"""<div class="split"><figure class="chart map">{svg}<figcaption>Positions are a qualitative reading of the feature matrix (see Features tab), not measured scores.</figcaption></figure>
<div class="prose-side"><h3 class="top">How to read it</h3><p>Every competitor is strong on one axis only. Julaya has the controls a finance team wants but no cards or credit. Djamo, Orange and the banks bring banking depth but little workflow. Wave and the gateways are rails. The top-right corner, a full business account with controls, is empty today.</p>
<p>The corner will not stay empty. Julaya is building credit, Djamo is raising $40M and Wave is waiting for a bank licence. Kelen's launch window is 2027–2028.</p></div></div>
<h3>Players by category</h3>""" + T(["Category", "Players in Senegal", "Players in Côte d'Ivoire", "Role for Kelen"], [
    ["SME payments and neobanks", "Julaya, Djamo Business", "Julaya, Djamo Business", "Direct competitors"],
    ["Mobile money and telco banks", "Wave, Orange Money, Mixx by Yas; Orange Bank Africa branch", "Orange Money, Wave, MTN MoMo, Moov Money; Orange Bank Africa", "Competitors for payouts and credit; also Kelen's payout rails"],
    ["Banks", "CBAO, SG Sénégal, BIS, Ecobank, BNDE, BOA, SUNU Bank (ex-BICIS), Coris, BHS, NSIA, UBA, Banque Atlantique, Orabank (29 banks)", "SGCI, BNI, NSIA, Banque Atlantique, Ecobank, SIB, Bridge, AFG, Coris, BGFI, BICICI, BOA, UBA (29 banks)", "Incumbents and partner-bank candidates"],
    ["Microfinance", "Crédit Mutuel (CMS), Baobab, PAMECAS, ACEP, Cofina (81 large institutions)", "Baobab, Advans, Cofina, UNACOOPEC, FIDRA (43)", "Credit competitors; SFD acquisition targets"],
    ["Aggregators and gateways", "InTouch, PayDunya, Bictorys, Flutterwave, PayTech, NabooPay, Wizall", "CinetPay, InTouch, PayDunya, Sycapay, Paystack, HUB2, Kkiapay", "Mostly partners (collections, payout back-up)"],
    ["Adjacent software", "KayFay, Sage Paie, SunuPayRH, Odoo; Facture SN; Fintra (salary advance)", "BaraPay (salary advance); FNE invoicing tools", "Integration partners and distribution"],
    ["Foreign models to watch", "Moniepoint (enters markets by buying an MFI), Qonto, Revolut", "same", "No WAEMU entry signals found"],
])
tabs.append(("landscape", "Landscape", "Where every type of player sits, and the empty space Kelen aims for.", landscape))

# --------------------------------------------------------------------------------------------
# 6. DIRECT COMPETITORS (profiles)
def profile(name, threat, tagline, facts, strengths, weaknesses, watch):
    return f"""<section class="prof"><header><h3>{name}</h3>{P(threat)}</header><p class="tag">{tagline}</p>
{FACTS(facts)}<div class="sw"><div><h4>Strengths</h4>{UL(strengths)}</div><div><h4>Weaknesses</h4>{UL(weaknesses)}</div></div>
<p class="watch"><b>What to watch:</b> {watch}</p></section>"""

direct = profile("Julaya", "High", "B2B payments and payroll platform for medium and large companies. Founded 2018 in Abidjan.", [
    ("Countries and licences", f"Côte d'Ivoire (EP.CI.004/2025), Senegal (EP.SN.009/2025, Sept 2025), Benin, Togo · {s('ep_list', 'BCEAO list')}"),
    ("Funding", f"$2M (2021), $5M extension led by Speedinvest (2022), 800M FCFA convertible bonds from CDC-CI Capital (Oct 2025) for SME credit and expansion · {s('julaya_5m', 'TechCabal')} · {s('julaya_cdc', 'Ecofin')}"),
    ("Scale", f"&gt;10,000 professionals, &gt;1,000 medium and large companies, &gt;1,000bn FCFA a year. Senegal 2024: 820,000 transactions, ≈2,800 active users · {s('julaya_cdc', 'Ecofin')}"),
    ("Clients", "Jumia, SODECI, Ministère de l'Éducation CI, World Bank, Kamtar, InTouch"),
    ("Product", f"Up to 3,000 payouts in one click to all wallets and banks; custom approval levels, delegation, 2FA; sub-accounts and multi-company; per-user caps; exports; new 'RIB Julaya' for UEMOA transfers; bill pay and invoice collection; free cash deposit at partner banks · {s('julaya_tx', 'product')} · {s('julaya_acc', 'access levels')} · {s('julaya_rib', 'RIB')}"),
    ("Pricing", f"Payouts to wallets 0.5–1.5% depending on volume; bills 0.5%; bank transfers 'by volume'; invoice collection 0.1–0.5%; no subscription shown · {s('julaya_px', 'price page')}"),
], ["B2B-native, built for a CFO", "Licensed in both launch countries", "Pays to banks and every wallet", "Approvals and sub-accounts already live"],
   ["No cards, no credit, no employee accounts", "No invoice creation or payment links", "Small Senegal base", "Percentage pricing gets expensive on large payrolls", "Debt-funded since 2022"],
   "the SME credit product funded by CDC-CI, and any card programme. Julaya is the default alternative for Kelen's Moyenne and Grande plans.")

direct += profile("Djamo and Djamo Business", "High", "Consumer neobank (YC W21) with a free business account for small companies, sole traders and associations.", [
    ("Countries and licences", f"Côte d'Ivoire (EP.CI.005/2025, microfinance licence for Djamo Finances SA, Sept 2025), Senegal (EP.SN.010/2025; microfinance 'coming') · {s('djamo_mfi', 'Ecofin')} · {s('djamo_sn', 'Directactu')}"),
    ("Funding", f"$14M Series A (2022), $17M (Apr 2025, Janngo, Partech, SANAD, Oikocredit, YC); targeting a $40M Series C (July 2026, not confirmed closed) · {s('djamo_tc', 'TechCrunch')} · {s('djamo_40', 'ITWeb')}"),
    ("Scale", "2M users (July 2026); &gt;500,000 in Senegal with ≈700 agents; ≈10,000 small businesses onboarded; &gt;$4.5bn processed; 25% on premium"),
    ("Business product", f"Bulk payments by file, bank transfers to any UEMOA bank, employee Djamo cards, collections by QR, link and API, exports · {s('djamo_b', 'Djamo Business')}"),
    ("Pricing", f"Account free; bulk pay and bank transfers from the web app free; API payouts 0.5%; collections 1% · {s('djamo_px', 'price page')}"),
    ("Limits", f"10M FCFA per transaction and 100M a month for companies; API pays only Djamo accounts; credit (up to 1M FCFA) for consumers only · {s('djamo_api', 'API')} · {s('djamo_credit', 'credit')}"),
], ["Brand and 2M users", "Free business account", "Cards, microfinance licence and a live credit engine", "Strong investors, raising again"],
   ["Business features are shallow: no documented roles, approvals or sub-accounts", "API limited to Djamo accounts", "No accountant features", "Only 5–10% of users get their salary on Djamo"],
   "the Series C. With $40M Djamo can build roles, approvals and SME credit within a year. Its free account sets the price ceiling for Kelen's Petite plan.")

direct += profile("Wave and Wave Business", "High", "The dominant mobile-money wallet in Senegal and Côte d'Ivoire, with a business offer for payouts and merchant collections.", [
    ("Licence", f"E-money institution in Senegal (2022). Wave Bank Africa S.A. incorporated in Abidjan with 20bn FCFA capital (Oct 2025); bank licence under review (Apr 2026) · {s('wave_bank', 'Ecofin')} · {s('wave_ci', 'Abidjan Économie')}"),
    ("Funding", f"$200M Series A at $1.7bn (2021); €117M debt (June 2025) · {s('wave_tc', 'TechCrunch')} · {s('wave_debt', 'Fintech News')}"),
    ("Scale", "38.2% of WAEMU e-money value (2024); ≈11M clients in Senegal; &gt;20M accounts and 70% of merchant payments in Côte d'Ivoire"),
    ("Business product", f"Bulk payments (recipients cash out at any agent without a Wave account), merchant QR, Checkout and Payout APIs with batch sending, multi-user business accounts; virtual Visa card with Ecobank (consumer, Jan 2026) · {s('wave_b', 'Wave Business')} · {s('wave_api', 'API docs')} · {s('wave_card', 'card')}"),
    ("Pricing", "Bulk payments 1% paid by the sender, free for the recipient; merchant collections free up to 20,000 FCFA a day, then 1%; no subscription"),
    ("Next", f"Credit and savings announced Feb 2026 (not launched); insurance live June 2026; joined PI-SPI 30 Sept 2026 · {s('wave_int', 'interview')}"),
], ["Ubiquity and trust", "Lowest price, free cash-out", "Simple API", "A bank in preparation"],
   ["No IBAN, no payouts to banks", "No documented approvals, invoices or accounting", "Single rail", "Balance caps"],
   "the Wave Bank Africa licence and the credit launch. Kelen should treat Wave as a must-have payout rail and price against its 1%.")

direct += profile("Orange Money and Orange Bank Africa", "Medium-High", "Largest telco wallet in the union, plus Orange's digital bank (headquartered in Abidjan, Senegal branch since 2023–25).", [
    ("Scale", f"Orange Money Senegal 13.0M active clients (2025); Côte d'Ivoire 16.2M subscribers and a claimed 58% share; 41.3% of WAEMU e-money value · {s('sonatel', 'Sonatel FY2025')}"),
    ("Business product, Senegal", f"Paiement Pro for salaries and suppliers, merchant and internet payments, salary sub-accounts · {s('om_sn', 'Orange Business SN')}"),
    ("Pricing, Senegal", "Paiement Pro 1% if the recipient has Orange Money, 1.5% if not; merchant 1%; settlement to the bank after 5 days; free subscription"),
    ("Business product, Côte d'Ivoire", f"OM Business app (June 2026) with QR, links, dashboard and Orange Bank credit; salary payments at 2.0% / 1.5% / 1.0% by volume (2016 grid) · {s('om_business', 'Ecofin')} · {s('om_ci_sal', 'salary grid')}"),
    ("Orange Bank Africa", f"&gt;3.6M customers (80% CI), &gt;747bn FCFA lent since 2020; IFC guarantee on a $60M SME working-capital book (Feb 2026); SGPME guarantees for 17bn FCFA of SME credit in CI (July 2026) · {s('oba_ifc', 'IFC')} · {s('oba_sgpme', 'SGPME')}"),
], ["Largest base and agent network", "A bank in the group with SME credit and guarantees", "B2B sales force"],
   ["Pays out to Orange Money only", "No approvals or multi-bank payouts", "Slow settlement in Senegal", "Telco-style tools"],
   "Orange Bank Africa's SME lending in Senegal. It is the most credible competitor for Kelen's later loan product.")
tabs.append(("direct", "Direct competitors", "Detailed profiles of the four players Kelen will meet in every sales conversation.", direct))

# --------------------------------------------------------------------------------------------
# 7. PAYMENTS & OTHER PLAYERS
payments = """<h3>Mobile money market shares (WAEMU, BCEAO 2024)</h3>""" + T(["Network", "Accounts opened", "Transaction volume", "Transaction value", "Trend"], [
    ["Orange", "23.0%", "38.4%", "41.3%", "Losing value share (43.3% in 2023)"],
    ["Wave", "22.1%", "28.4% (another paragraph of the report says 23%)", "38.2%", "Gaining fast (34.0% in 2023)"],
    ["MTN", "16.6%", "17.4%", "11.7%", "Falling; 0% app fees since Aug 2025"],
    ["Moov", "18.4%", "6.9%", "2.6%", "Small in value"],
    ["Yas (Mixx)", "5.1%", "3.0%", "2.0%", "Small"],
]) + f'<p class="cite">Source: {s("bceao_dfs", "BCEAO digital financial services report 2024")}. No official Wave-versus-Orange split exists for Senegal; in Côte d\'Ivoire Wave holds 70% of merchant payments and 31% of transfers (INS survey, Apr 2024, via {s("mtn_ecomatin", "Ecomatin")}).</p>' + """
<h3>Other payment players</h3>""" + T(["Player", "What it does for businesses", "Licence and status", "Business pricing", "Threat", "Partner?"], [
    ["Mixx by Yas (ex-Free Money), SN", "Business Suite: salaries, suppliers, invoices, loans; Mixx Mastercard with Ecobank", "Mobile Cash SA; PI-SPI participant", f"Merchant 1%; bulk not published · {s('mixx', 'Yas')}", P("Low-Medium"), "Rail"],
    ["MTN MoMo, CI", "MoMo Pay, API, MoMo Helep Pro salary advance (up to 100,000 FCFA)", "PI-SPI participant; exploring bank licences", f"Not published; 0% in app for consumers · {s('mtn', 'KOACI')}", P("Low-Medium"), "Rail; salary-advance partner"],
    ["Moov Money, CI", "Merchant payment; microcredit 'soon'", "PI-SPI since 30 Sept 2026", f"Not published · {s('moov', 'KOACI')}", P("Low"), "Rail"],
    ["Wizall Money (BCP group), SN", "Wizall Money Pro: salaries, invoices, bulk payments, SMS cash-out codes", "Licence unclear; not on PI-SPI; looks dormant", f"Not published · {s('wizall', 'We Are Tech')}", P("Low-Medium"), "Low"],
    ["InTouch (TouchPay), SN-based", "Collections and business payouts across all wallets, cash network, salary-advance ('Crédit Digital'); ≈4,000 large clients", f"E-money in SN, payment institution in CI, Mali, Burkina; says it is profitable · {s('intouch', 'Burkina24')}", "Not published (third party: 250,000 set-up + 50,000 a month)", P("Medium"), P("Partner") + " aggregator, cash network"],
    ["PayDunya, SN", "Pay-in, pay-out API, links, invoices; &gt;4,000 B2B clients", f"First EP in Senegal; being acquired by Peach Payments · {s('peach', 'Peach')}", f"Collections 2.25%; payouts 2.00% (SN), cards 3.5%; no subscription · {s('paydunya', 'fee grid')}", P("Medium-Low"), P("Partner") + " collections"],
    ["CinetPay, CI", "Gateway and mass payout", f"EP in CI; fraud incidents and ≈$1.1M settlement backlog (2025–26) · {s('cinetpay_inc', 'TechCabal')}", f"Collections 1.8–3.5%; payouts 1.3–2% · {s('cinetpay', 'pricing')}", P("Low-Medium"), "Risky"],
    ["PayTech, SN", "E-commerce gateway, POS terminal", "Licence not stated", f"Mobile money 1.5–2%; POS 11,800 a month · {s('paytech', 'paytech.sn')}", P("Low"), "Medium"],
    ["Flutterwave, SN", "Collections, bulk payouts to bank and wallet, invoices", "EP in Senegal (2025)", f"Wallet 2%, card 4.8%, bank payout 1,500 FCFA · {s('flw', 'pricing')}", P("Low-Medium"), "Cross-border, cards"],
    ["Paystack, CI", "Developer gateway", "Licence not found", f"Mobile money 1.95%, cards 3.2–3.8% · {s('paystack', 'support page')}", P("Low"), "Cards"],
    ["HUB2, CI", "One API for wallets, banks and cards; sells to fintechs (Djamo, Julaya, CinetPay)", f"$8.5M Series A (Dec 2024); MoU with Ecobank to link 200M wallets (Feb 2026) · {s('hub2', 'Financial Afrik')}", "Not published", P("Low"), P("Partner") + " payout back-end"],
    ["Kkiapay, Benin", "Gateway, POS, payouts", "EP in Benin", f"9,900 FCFA a month for the API plan + 1.3–1.9% · {s('kkiapay', 'tarifs')}", P("Low"), "Low"],
    ["NabooPay, SN", "Checkout, escrow", "Licence not stated", f"3% wallets, 6% cards · {s('naboo', 'site')}", P("Low"), "Low"],
    ["Bizao", "B2B payment hub", f"French parent liquidated May 2025 · {s('bizao', 'Launch Base')}", "—", P("None"), "A warning on thin payment margins"],
]) + """
<h3>Fintech and software players next to Kelen</h3>""" + T(["Player", "What it does", "Price", "Threat", "Role for Kelen"], [
    ["KayFay (Dakar)", "Payroll software: IPRES, IPM, IR, TRIMF; payslips; salary advances; no payment rail", f"2,500 to 1,500 FCFA per payslip, minimum 15,000 a month · {s('kayfay', 'kayfay.com')}", P("Low-Medium"), "Integration: payroll file to Kelen bulk pay"],
    ["Sage Paie, SunuPayRH, CloudPaie, Odoo", "Payroll and IPRES/CSS declarations; no payments", "Sage ≈40–100k FCFA a year (unverified)", P("Low"), "Integrations"],
    ["Facture SN", "Invoices with NINEA and VAT; Wave/OM collection links without commission; accountant summary", f"3,900 FCFA a month · {s('facturesn', 'facturesn.com')}", P("Low-Medium"), "Covers Kelen's invoicing cheaply; partner or price reference"],
    ["Fintra (SN) and BaraPay (CI)", "Employer-enrolled salary advance to mobile money", f"Fintra: 6% fee, up to 20% of salary · {s('fintra', 'Ecofin')} · {s('barapay', 'BaraPay')}", P("Low-Medium"), "Proof of demand for Kelen's salary advance"],
    ["Flash / New Africa Technology", "Mastercard prepaid cards; 'Flash in Business' for companies", f"— · {s('flash', 'Financial Afrik')}", P("Low-Medium"), "Only local B2B card programme announced"],
    ["Bictorys, Mikaty, Samir Money, SesaPay, Copay", "New Senegalese payment institutions on PI-SPI", "Not profiled", P("Low"), "Follow up"],
], cls="wide")
tabs.append(("payments", "Payments & others", "Mobile-money operators, payment gateways and adjacent software: most are rails or partners rather than rivals.", payments))

# --------------------------------------------------------------------------------------------
# 8. BANKS & MICROFINANCE
banks = """<h3>Largest banks by assets, end-2025</h3>""" + '<div class="two">' + T(["Senegal", "Assets (bn FCFA)", "Share"], [
    ["CBAO (Attijariwafa)", "1,791", "11.4%"], ["Société Générale Sénégal", "1,615", "10.3%"], ["Banque Islamique du Sénégal", "1,291", "8.2%"],
    ["Ecobank Sénégal", "1,248", "8.0%"], ["BNDE (State)", "853", "5.4%"], ["Bank of Africa Sénégal", "835", "5.3%"],
    ["SUNU Bank Sénégal (ex-BICIS)", "807", "5.1%"], ["Coris Bank Sénégal", "787", "5.0%"], ["BHS", "659", "4.2%"], ["NSIA Banque Sénégal", "586", "3.7%"],
]) + T(["Côte d'Ivoire", "Assets (bn FCFA)", "Share"], [
    ["Société Générale CI", "3,783", "12.2%"], ["BNI (State)", "3,210", "10.3%"], ["NSIA Banque CI", "3,076", "9.9%"],
    ["Banque Atlantique CI", "2,419", "7.8%"], ["Ecobank CI", "2,048", "6.6%"], ["SIB (Attijariwafa)", "1,882", "6.1%"],
    ["Bridge Bank", "1,429", "4.6%"], ["AFG Bank", "1,374", "4.4%"], ["Coris Bank CI", "1,324", "4.3%"], ["Orange Bank Africa (2.39M accounts)", "301", "1.0%"],
]) + "</div>" + f'<p class="cite">Source: {s("cb2025", "Commission Bancaire annual report 2025")}. Concentration is low (top 4 hold 38% of bank assets in Senegal, 40% in Côte d\'Ivoire). BICIS became SUNU Bank Sénégal on 23 Oct 2025 ({s("sunu", "Seneweb")}); the State\'s planned purchase of SG Sénégal is unconfirmed ({s("sg_sn", "Le Soleil")}).</p>' + """
<h3>Published business tariffs</h3>""" + T(["Bank", "Account keeping a month", "Online banking a month", "Transfer to another bank", "Bulk salary file", "Source"], [
    "Senegal",
    ["BNDE (Mar 2025)", "12,500 company; 8,500 pros and micro; pack PME 15,000", "5,000", "5,000 (RTGS 15,000)", "1,000 a line, min 5,000, max 50,000", s("bnde", "PDF")],
    ["BIS (June 2024)", "12,000 SARL/SA; 8,500 sole trader", "Not shown", "4,000 (RTGS 15,000)", "1,000 a line, min 5,000, max 30,000", s("bis", "PDF")],
    ["CBAO (2023)", "Based on movements", "10,000", "4,000", "On request", s("cbao", "PDF")],
    ["UBA Sénégal (Oct 2026)", "25,000 SA/PME; 10,000 micro", "Included", "Not published", "Grouped transfers included", s("uba_sn", "Comparek")],
    ["Coris (2020, may be outdated)", "10,000 company", "In packs", "3,000 (RTGS 10,000)", "On request", s("coris", "PDF")],
    ["BOA Sénégal (2026)", "Free; movement fee applies", "1,000", "—", "Salary domiciliation free; Wave ↔ account 1%, max 500", s("boa", "PDF")],
    "Côte d'Ivoire",
    ["SGCI (Jan 2026)", "PME packs 25,000–35,000", "MyBusiness 6,000", "5,000 at branch; 250 a line online", "250 a line online", s("sgci", "PDF")],
    ["UBA CI (Apr 2026)", "20,000 SARL; 25,000 SA; 10,000 sole trader", "5,000", "10,000 (online 750)", "On request", s("uba_ci", "PDF")],
    ["Orabank (2026)", "PME 20,000; pros 15,000 (excl. tax)", "10,000", "Online 250", "—", s("orabank", "PDF")],
], cls="wide") + """
<h3>What a 10-employee SARL pays its bank each month</h3>""" + T(["Item", "BNDE (SN)", "BIS (SN)", "SGCI (CI)", "Kelen Moyenne"], [
    ["Account keeping", "12,500", "12,000", "25,000", "29,900, all included"],
    ["Online banking", "5,000", "not shown", "6,000", "included"],
    ["Salary file, 10 lines", "10,000", "10,000", "2,500", "included"],
    ["5 supplier transfers", "25,000", "20,000", "1,250", "included (quota to define)"],
    ["<b>Total before tax and movement fees</b>", "<b>≈52,500</b>", "<b>≈42,000</b>", "<b>≈34,750</b>", "<b>29,900</b>"],
]) + """
<h3>Digital offers</h3>""" + T(["Bank", "SME digital offer", "App rating (Google Play)"], [
    ["Ecobank", f"Omni Lite for SMEs: bulk salary upload, transfers, bills · {s('ecobank_omni', 'Ecobank')}", "3.7 (51k reviews)"],
    ["Société Générale", "MyBusiness (6,000 a month); SG Connect app", "4.1"],
    ["CBAO", "Business web banking (10,000 a month)", "4.1"],
    ["BOA", "BOAweb, MyBOA; Wave and Orange Money to account", "4.5"],
    ["UBA", "UBA Mobile; online transfer 750 FCFA (CI)", "4.4"],
    ["Wave Business (benchmark)", "Bulk payouts 1%, QR", "4.4 (11k reviews)"],
]) + """
<p class="prose">No bank in either country offers self-service SME onboarding with approvals, invoicing and multi-user cards at a flat price. Bank lending to the SMEs they accept averages 7.07% (WAEMU, 2024), against 6.06% for large firms (""" + s("bceao_cdb", "BCEAO") + """).</p>
<h3>Microfinance</h3>""" + T(["Indicator", "Senegal", "Côte d'Ivoire", "Source"], [
    ["Large microfinance institutions", "81 (7 companies, 74 cooperatives)", "43 (13 companies, 30 cooperatives)", s("cb2025", "CB 2025")],
    ["Total assets of large institutions", "1,234bn FCFA", "1,227bn FCFA", s("cb2025", "CB 2025")],
    ["Loans outstanding, whole sector", "887bn FCFA (Q2 2026, +9.8%); 4.7M clients", "723bn FCFA (end-2025)", s("mf_sn", "APS")],
    ["Bad loans", "7.7% (Q2 2026), norm 3%", "6.3% (large institutions)", s("mf_sn", "APS")],
    ["Licensed institutions", "297 (many small, isolated or inactive)", "—", s("mf_count", "AllAfrica")],
]) + T(["Institution", "Size", "SME offer", "Source"], [
    ["Baobab (SN and CI)", "Baobab CI #1 and Baobab SN #2 large MFIs in the union; SN 23% of loans and 32% of disbursements; group 1.66M clients, €963M book, ≈50% of loans disbursed digitally", "Nano to SME loans up to €300k", s("baobab_kit", "press kit")],
    ["Crédit Mutuel du Sénégal (CMS)", "1.5M members, 210 branches; 42% of SN microfinance deposits", "Member loans, online loan request", s("cms", "CMS")],
    ["PAMECAS, ACEP (SN)", "13% and 14% of SN loans", "Production-oriented SME lending", s("mf_shares", "AllAfrica")],
    ["Cofina (SN and CI)", "CI: 76bn loans, 90k clients; SN 109.8bn assets", "'Mésofinance' from 3M FCFA; up to 18% a year", s("cofina_ci", "Cofina") + " · " + s("cofina_sn", "Cofina SN")],
    ["Advans CI", "85bn loans, 250k clients, 27 branches", "SME loans up to 300M FCFA, 3–36 months, 1.6% a month (≈19% a year)", s("advans", "Advans")],
]) + """
<h3>Recent microfinance deals (relevant to Kelen's SFD purchase)</h3>""" + T(["Deal", "Date", "Size", "Price", "Source"], [
    ["Beltone buys 100% of Baobab Group", "Feb 2026", "€849M loan book, 1.6M clients", "€197.6M, ≈0.23× loan book", s("baobab", "TechInAfrica")],
    ["SF Capital takes 100% of Microsen (SN)", "Feb 2025", "9.3bn FCFA assets, 12k clients", "Not disclosed", s("microsen", "Financial Afrik")],
    ["Witti Finances takes 85% of Kajas (SN)", "2024–26", "5.75bn FCFA assets, 30k clients", "Capital increase, amount not disclosed", s("kajas", "Horonya")],
    ["Historical benchmark", "2009", "144 private MFI deals", "Median 1.3–1.9× book", s("cgap", "CGAP")],
]) + '<p class="prose">Small Senegalese SFDs change hands mostly through recapitalisation. Expect a price at or below 1× book value, plus the capital Kelen injects. This is analyst judgement, not a published figure.</p>'
tabs.append(("banks", "Banks & microfinance", "Incumbent banks, their SME pricing, the microfinance sector and recent SFD deals.", banks))

# --------------------------------------------------------------------------------------------
# 9. FEATURES
Y, Pp, N, Q = '<span class="f y" title="Yes">Yes</span>', '<span class="f p" title="Partial">Partial</span>', '<span class="f n" title="No">No</span>', '<span class="f q" title="Unknown">?</span>'
feat = T(["Feature", "Julaya", "Djamo Business", "Wave Business", "Orange Money (SN)", "Typical bank", "Kelen (plan)"], [
    "Account",
    ["Business account with IBAN / RIB", Pp + " RIB to receive", Pp, N, N, Y, Y],
    ["Online onboarding (KYB)", Y, Y, Y, Pp, N + " branch visit", Y],
    ["Sub-accounts", Y, N, Pp, Pp, Pp, Y],
    ["Cash deposit", Y + " partner banks", Y + " agents", Y + " agents", Y + " agents", Y + " branch", Q],
    "Control",
    ["Multi-user roles", Y, Q, Pp, Pp, Y, Y],
    ["Approval workflow (double signature)", Y, N, N, N, Pp, Y],
    ["Accountant access and exports", Pp + " exports", Pp, Pp, Pp, Pp, Y],
    "Paying out",
    ["Bulk payroll to banks", Y, Pp, N, N, Y, Y],
    ["Bulk payroll to all wallets", Y, Pp + " Djamo", Pp + " Wave", Pp + " Orange", N, Y],
    ["Payroll file import from payroll software", Y, Y, Y, Y, Pp, Y],
    ["API", Q, Y, Y, Y, Pp, Q],
    "Getting paid",
    ["Invoices", Pp + " collection only", N, N, N, N, Y],
    ["Payment links and QR", N, Y, Y, Y, N, Y],
    "Cards",
    ["Virtual cards", N, Pp, Pp + " consumer", N, Pp, Y],
    ["Physical cards per employee", N, Y, N, N, Y, Y],
    "Credit and employees",
    ["SME credit", N + " planned", N, N + " announced", Y + " via OBA", Y, "Later (own SFD)"],
    ["Employee salary accounts", N, Pp, Pp, Pp, Y, Y],
    ["Salary advance", N, Pp, N, N, Pp, Y],
    "Pricing model",
    ["How it charges", "% per payout (0.5–1.5%)", "Free account; 0.5% API; 1% collections", "1% per payout", "1–1.5% per payout; 1% merchant", "10–25k a month + fees", "9,900 / 29,900 / 79,900 a month"],
], cls="fm") + f'<p class="cite">Sources: {s("julaya_tx", "Julaya")} · {s("julaya_acc", "Julaya access")} · {s("djamo_b", "Djamo Business")} · {s("djamo_api", "Djamo API")} · {s("wave_b", "Wave Business")} · {s("wave_api", "Wave API")} · {s("om_sn", "Orange Business SN")} · {s("uba_sn", "UBA via Comparek")}. "Typical bank" mixes UBA Sénégal\'s published offer with general practice.</p>' + """
<h3>Features nobody offers yet</h3>""" + UL([
    "Double-signature approvals combined with payouts to banks and every wallet from one balance.",
    "Employee salary accounts with a salary advance tied to the employer's payroll.",
    "Accountant access with exports in the Senegalese format (SYSCOHADA), across several client companies.",
    "Spend control: cards with limits, receipts and approvals for field staff.",
    "SME working capital bundled with the account: invoice and payroll advances.",
])
tabs.append(("features", "Features", "Feature-by-feature comparison of Kelen's planned product against the four direct competitors and a typical bank.", feat))

# --------------------------------------------------------------------------------------------
# 10. PRICING
def bars(title, rows, maxv):
    out = [f'<figure class="bars"><figcaption>{title}</figcaption>']
    for lab, v, k in rows:
        w = v / maxv * 100
        out.append(f'<div class="br {k}" title="{lab}: {v:,.0f} FCFA a month"><span class="bl">{lab}</span>'
                   f'<span class="bt"><i style="width:{w:.1f}%"></i></span><span class="bv">{v:,.0f}</span></div>')
    out.append("</figure>")
    return "".join(out)

def scen(pay, plan, planname):
    rows = [("Wave Business, 1%", pay * 0.01, "o"), ("Orange Paiement Pro, 1.5% (non-Orange)", pay * 0.015, "o"),
            ("Julaya, 0.5–1.5% (midpoint 1%)", pay * 0.01, "o"), ("PayDunya payouts, 2%", pay * 0.02, "o"), (f"Kelen {planname}, flat", plan, "k")]
    return bars(f"Payroll of {pay / 1e6:g}M FCFA a month", rows, max(r[1] for r in rows))

pricing = """<p class="prose">SMEs already pay for payroll as a percentage. The question for Kelen is whether a flat plan with payouts included beats that. Djamo Business is free for bulk pay to Djamo accounts and is left out of the bars.</p>
<div class="bargrid">""" + scen(1e6, 9900, "Petite") + scen(3e6, 29900, "Moyenne") + scen(15e6, 79900, "Grande") + """</div>
<p class="cite">Kelen beats the 1% wallet benchmark once a client pays more than about 1M (Petite), 3M (Moyenne) or 8M FCFA (Grande) of payroll a month, and only if its own payout cost through PI-SPI stays near zero. Bars use published rates; account fees and the Senegal transfer tax (salaries exempt) are left out.</p>
<h3>All published business prices</h3>""" + T(["Provider", "Account / subscription", "Payouts and payroll", "Collections", "Other"], [
    "Direct competitors",
    ["Julaya", "None shown", "0.5–1.5% to wallets; bank 'by volume'", "Invoices 0.1–0.5%", "Bills 0.5%; deposits free"],
    ["Djamo Business", "Free", "Web bulk free; API 0.5%", "1% (QR, link, API)", "Limits 10M per transaction"],
    ["Wave Business", "None", "1% sender, free for recipient", "Free to 20,000 a day, then 1%", "Cash-out free"],
    ["Orange Money (SN)", "Free", "1% (Orange recipient) / 1.5% (other)", "1%, settled after 5 days", "—"],
    ["Orange Money (CI)", "Not published", "Salaries 2.0% / 1.5% / 1.0% by volume (2016)", "Not published", "—"],
    "Banks",
    ["Senegalese banks", "8,500–25,000 a month", "Bulk 1,000 a line; interbank 3,000–5,000; RTGS 15,000", "—", "Online banking 1,000–10,000"],
    ["Ivorian banks", "15,000–35,000 a month (packs)", "Online 250–750 a line; branch 5,000–10,000", "—", "Online banking 3,000–10,000"],
    "Gateways",
    ["PayDunya", "None", "2.00% (SN), 1.5–2.0% (CI)", "2.25%; cards 3.5%", "—"],
    ["CinetPay", "None", "1.3–2%", "1.8–3.5%", "Trust issues"],
    ["Flutterwave SN", "None", "Wallet 2%; bank 1,500", "2%; cards 4.8%", "—"],
    ["PayTech", "POS 11,800 a month", "No fee stated", "1.5–2%; cards 2.5–3%", "Opening 10,000"],
    ["Kkiapay", "1,000 / 4,900 / 9,900 a month", "Not published", "1–1.9%", "Model similar to Kelen's"],
    "Infrastructure",
    ["PI-SPI (BCEAO)", "—", "Free up to 8,000 FCFA a day per user, then 0–0.8% (other report: receiver pays ≤1% after 30 free receipts a month)", "Free for the payer", "Mandatory from 2 Nov 2026"],
    "Software",
    ["KayFay payroll", "Minimum 15,000 a month", "None (no rail)", "—", "1,500–2,500 per payslip"],
    ["Facture SN invoicing", "3,900 a month", "—", "Wave/OM links without commission", "—"],
], cls="wide") + """
<h3>Pricing implications for Kelen</h3>""" + UL([
    "<b>Include payouts in every plan.</b> A quota of free payouts (for example 30 / 150 / 600 a month) turns the subscription into a saving against Wave's 1%.",
    "<b>Sell against the bank, not against Djamo.</b> Petite at 9,900 costs less than a bank's micro-business fee alone (10,000) and far less than the 35,000–52,500 a 10-person SARL pays its bank.",
    "<b>Keep a free or near-free entry.</b> Djamo's free account sets the floor for very small firms. A free trial of three months (already in the design) answers it; the paid case is approvals, roles and multi-rail payouts.",
    "<b>Invoicing alone is worth 3,900 FCFA a month</b> (Facture SN). It is a feature inside a plan, not a reason to pay 29,900.",
    "<b>Check the PI-SPI business tariff with the partner bank</b> before fixing quotas: the two published readings differ.",
])
tabs.append(("pricing", "Pricing", "What SMEs pay today for accounts and payroll, and where Kelen's 9,900 / 29,900 / 79,900 FCFA plans land.", pricing))

# --------------------------------------------------------------------------------------------
# 11. COMPARABLES
comps = T(["Company", "Key figures", "Lessons for Kelen", "Source"], [
    ["Qonto (France, SME neobank)", "≈600–750k business clients; NBI €495M (2025); first profit 2023, €92.8M in 2025 (−36% as rates fell); team plans €49 / 109 / 199 a month; 6,000 accounting firms as clients", "Tier by users, cards, transfer quotas and approvals, as Kelen's plans do. Accountants are the channel. Do not build the plan on deposit interest.", s("qonto", "pricing") + " · " + s("qonto_res", "results")],
    ["Revolut Business", "767k business customers (2025, +33%); 16% of $6.0bn group revenue", "Business follows a large consumer base. Kelen's employee accounts can run that funnel in reverse.", s("revolut", "Revolut")],
    ["Mercury (US)", "$650M annualised revenue (2025); valued $5.2bn; conditional bank charter", "Start on partner banks, take your own licence at scale. Own the account data and the IBAN relationship from day one.", s("mercury", "letter") + " · " + s("mercury2", "American Banker")],
    ["Moniepoint (Nigeria)", "Valued $1bn (2025); ≥₦1trn (≈$700M) SME credit in 2025; entered Kenya by buying 78% of a microfinance bank", "Payments first, then lend on payment data. Buying a licensed MFI is a proven entry route, as Kelen plans.", s("moniepoint", "TechInAfrica") + " · " + s("moniepoint2", "TechCabal")],
    ["Kuda (Nigeria)", "7M+ customers; 2022 revenue $22M, net loss $32M", "Free accounts without fee or credit revenue burn cash. Kelen's paid B2B model avoids it.", s("kuda", "TechInAfrica")],
    ["TymeBank / GoTyme", "≈15M customers; valued $1.5bn (Nubank-led round, Dec 2024); profitable from end-2023", "Physical onboarding points (kiosks) cut acquisition cost. Kelen's equivalent: accountants and partner-bank branches.", s("tyme", "Fintech Futures")],
    ["M-Pesa and Fuliza (Kenya)", "M-Pesa revenue KSh 182.7bn (FY to Mar 2026, 45.6% of Safaricom service revenue); Fuliza overdraft disbursed KSh 1.47trn", "Credit embedded at the moment of payment scales. A payroll or supplier-payment advance can work the same way.", s("mpesa", "Tech-ish")],
    ["Paystack / Flutterwave", "Both moved toward licences and lending as payment margins fell", "Payments alone do not make a business. Win Dakar first, then expand.", s("stack", "BusinessDay")],
    ["Ramp / Brex (US)", "Ramp ≈$1.5bn annualised revenue, valued $44bn (2026); Brex sold to Capital One for $5.15bn", "Card interchange plus spend control earns more than account fees. Push cards with approvals and receipts.", s("ramp", "Sacra")],
    ["Wave (regional)", "$1.7bn valuation (2021); €117M debt (2025); 38% of WAEMU e-money value", "Price cuts plus agent density took share from Orange. Kelen cannot out-price Wave on payouts; it should use Wave as a rail.", s("wave_tc", "TechCrunch")],
], cls="wide")
tabs.append(("comparables", "Comparables", "International companies with a similar model, their numbers, and what Kelen can learn from them.", comps))

# --------------------------------------------------------------------------------------------
# 12. POSITIONING & STRATEGY
strategy = """<h3>Kelen's position</h3>
<p class="prose"><b>The business account for SMEs that pay people.</b> One account with its own IBAN, where the manager prepares and the owner approves, and salaries and suppliers go to any bank or wallet in one run. Cards for staff, invoices for clients and an accountant who sees everything. A flat monthly price that costs less than the bank and less than 1% of payroll.</p>
""" + CARDS([
    ("1. Control, not just payments", "Approvals, roles, sub-accounts and accountant access are what Julaya has and Djamo, Wave and Orange lack. Put them in every plan, including Petite."),
    ("2. Every rail from one balance", "Banks and all wallets through PI-SPI, with Wave and Orange as payout rails, not rivals. Recipients choose where they are paid."),
    ("3. Flat price with payouts included", "Undercut 1% of payroll and the bank's fee stack. Make the saving visible in the onboarding flow."),
    ("4. Payroll in, employees out", "Import from KayFay, Sage, Odoo and accountants' files; employees get salary accounts and a salary advance. This is the moat Julaya and Wave do not have."),
    ("5. Credit from payment data", "Underwrite on payroll and collections history before the SFD (Moniepoint's playbook). Start with invoice and payroll advances, inside the 24% all-in cap."),
    ("6. Accountants as the channel", "Qonto grew through 6,000 accounting firms. In Senegal many SMEs' payroll is run by accountants: give them free multi-client access."),
]) + """
<h3>How competitors will react</h3>""" + T(["Competitor", "Likely move by 2027–28", "Kelen's answer"], [
    ["Julaya", "Launches SME credit; may add cards", "Cards, invoices, employee accounts and a flat price; win smaller SMEs Julaya does not target"],
    ["Djamo", "Uses its Series C to add roles, approvals and SME credit; keeps the account free", "Depth of controls and multi-rail payouts; accountant channel; payroll integrations"],
    ["Wave", "Bank licence, savings and credit; keeps 1% payouts", "Use Wave as a rail; sell IBAN, approvals, bank payouts and invoices"],
    ["Orange / Orange Bank Africa", "Brings OM Business and SME credit to Senegal", "Faster settlement, multi-bank payouts, banking UX"],
    ["Banks", "Improve corporate e-banking; partner with fintechs", "Choose the partner bank carefully: it may serve competitors (Ecobank already issues cards for Wave, Mixx and Djamo)"],
], cls="wide") + """
<h3>Business plan check</h3>""" + T(["Assumption in the plan", "What the research says", "Suggested action"], [
    ["Senegal: 7,652 active clients in year 5 (27% of target market)", "20,000–28,000 digital-ready SMEs, so 27–38% share. Julaya had ≈2,800 active users in Senegal in 2024 after six years; Djamo ≈10,000 small businesses across both countries.", "Treat the base case as ambitious. Add a scenario at 3,000–4,000 Senegalese clients in year 5 and check the cash need."],
    ["Côte d'Ivoire: 60,000 formal employers", "CNPS: ≈49,000 declared companies (unverified); 82,548 formal firms including non-employers.", "Lower to 49,000 once the CNPS figure is confirmed."],
    ["Senegal employer growth 4.9% a year", "Growth forecast falls to ≈2.5% in 2026; State arrears weigh on SMEs.", "Keep 4.9% in base; test 2.5% in prudent."],
    ["Loans at 23% a year", "SFD cap is 24% all-in (TAEG), including fees and insurance.", "Already noted in the Regulatory path; keep fees inside the 1-point gap."],
    ["Payout costs (partner bank and aggregators)", "PI-SPI mandatory from 2 Nov 2026 with free or ≤0.8% tiers.", "Ask the partner bank for its PI-SPI business tariff; it may lower cost of revenue."],
    ["Account fee benchmark 15,000 FCFA a month", "Senegal banks charge 8,500–25,000 plus online banking and transfers; a 10-person SARL pays ≈35,000–52,500 in total.", "Consistent; the full fee stack strengthens Kelen's price case."],
], cls="wide") + """
<h3>Risks</h3>""" + UL([
    "<b>Wave gets its bank licence</b> and bundles accounts and credit for its whole base.",
    "<b>Djamo closes $40M</b> and copies the control features while staying free.",
    "<b>Partner-bank dependence</b>: the bank may also serve competitors, change prices or slow integration.",
    "<b>Senegal's slowdown</b>: State arrears and weak growth in 2026–27 lengthen sales cycles and raise credit losses.",
    "<b>Willingness to pay</b> a monthly subscription has never been measured in this market.",
]) + """
<h3>What to verify before launch</h3>""" + UL([
    "Mystery-shop Ecobank, SG Sénégal, CBAO and NSIA for their SME tariffs (not published online).",
    "20–30 interviews with Dakar SMEs and accountants on payroll practice, bank fees and willingness to pay.",
    "Confirm the CNPS employer count and the Ivorian private wage bill.",
    "Get the PI-SPI tariff for business senders from the partner bank.",
    "Track Wave Bank Africa's licence and Djamo's Series C.",
    "Profile the new Senegalese payment institutions on PI-SPI (Bictorys, Mikaty, Samir Money, SesaPay).",
])
tabs.append(("strategy", "Positioning", "Where Kelen should stand, how competitors will react, and what this means for the business plan.", strategy))

# --------------------------------------------------------------------------------------------
# 13. SOURCES
groups = [
    ("Regulators and official statistics", ["bceao_inc", "bceao_dfs", "bceao_cdb", "cb2025", "cb_lists", "ep_list", "pispi_launch", "usury", "usury_sfd", "mf_law", "wb_api", "findex", "wbes_sn", "wbes_ci", "mefp", "imf_sn", "imf_ci", "anstat", "endes"]),
    ("Market data and press", ["ipres", "cnps", "payroll_sn", "cepici", "ansd_ninea", "ci_rge", "arrears", "arrears2", "pispi_fa", "pispi_jecos", "pispi_175", "tta", "fne", "ep_deadline", "partech", "cash_pay", "datareportal_sn", "datareportal_ci", "elect"]),
    ("Direct competitors", ["julaya", "julaya_px", "julaya_tx", "julaya_rib", "julaya_acc", "julaya_cdc", "julaya_5m", "djamo_b", "djamo_px", "djamo_api", "djamo_credit", "djamo_tc", "djamo_40", "djamo_sn", "djamo_mfi", "wave_b", "wave_api", "wave_bank", "wave_ci", "wave_fa", "wave_int", "wave_debt", "wave_card", "om_sn", "om_ci", "om_ci_sal", "om_business", "oba_ifc", "oba_sgpme", "sonatel"]),
    ("Payment players and software", ["mixx", "mtn", "mtn_ecomatin", "moov", "wizall", "intouch", "intouch2", "paydunya", "peach", "cinetpay", "cinetpay_inc", "paytech", "paystack", "flw", "bizao", "hub2", "kkiapay", "naboo", "kayfay", "facturesn", "fintra", "barapay", "flash"]),
    ("Banks and microfinance", ["uba_sn", "bnde", "bis", "coris", "cbao", "boa", "sgci", "uba_ci", "orabank", "sunu", "sg_sn", "ecobank_omni", "mf_sn", "mf_shares", "mf_count", "advans", "cofina_ci", "cofina_sn", "baobab", "baobab_kit", "microsen", "kajas", "cgap", "cms"]),
    ("Comparables", ["qonto", "qonto_res", "qonto_s", "revolut", "mercury", "mercury2", "moniepoint", "moniepoint2", "moniepoint3", "kuda", "tyme", "mpesa", "stack", "ramp", "wave_tc"]),
]
import urllib.parse
def host(u):
    h = urllib.parse.urlparse(u).netloc.replace("www.", "")
    path = urllib.parse.unquote(urllib.parse.urlparse(u).path).rstrip("/").split("/")[-1][:70]
    return h, path
src_html = '<p class="prose">Research carried out on 14 October 2026 from official reports, regulators\' lists, company websites and price pages, and the press. Figures marked "unverified" or "estimate" rest on one secondary source or on a calculation. The full research notes, with every figure and its confidence level, are in the project files.</p>'
for g, keys in groups:
    items = []
    for k in keys:
        h, p = host(S[k])
        items.append(f'<li><a href="{S[k]}" target="_blank" rel="noopener">{h}</a> <span class="pth">{p}</span></li>')
    src_html += f"<h3>{g}</h3><ul class=\"src\">{''.join(items)}</ul>"
tabs.append(("sources", "Sources", "Where every figure comes from.", src_html))

# --------------------------------------------------------------------------------------------
nav = "".join(f'<button type="button" role="tab" id="t-{k}" aria-controls="p-{k}" data-tab="{k}" aria-selected="{"true" if i == 0 else "false"}">{lab}</button>'
              for i, (k, lab, _, _) in enumerate(tabs))
panels = "".join(f'<section class="panel" id="p-{k}" role="tabpanel" aria-labelledby="t-{k}"{"" if i == 0 else " hidden"}>'
                 f'<div class="ph"><h2>{lab}</h2><p class="lead">{lead}</p></div>{body}</section>'
                 for i, (k, lab, lead, body) in enumerate(tabs))

CSS = open(sys.argv[2]).read() if len(sys.argv) > 2 else ""
page = """<title>Kelen Market Analysis</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap">
<style>""" + CSS + """</style>
<div class="wrap">
<header class="top">
  <div class="eyebrow"><span class="mark"><i></i>kelen</span><span>Market and competitor analysis</span></div>
  <h1>Kelen market analysis</h1>
  <p class="sub">The SME banking market in Senegal and Côte d'Ivoire, and every player Kelen will compete with or rely on. Research as of 14 October 2026. Amounts in FCFA; 1 € = 655.957 FCFA.</p>
</header>
<nav class="tabs" role="tablist" aria-label="Sections">""" + nav + """</nav>
""" + panels + """
<footer>Prepared for Kelen's business plan. Positions on the landscape map and threat levels are judgements based on the cited facts. Competitor prices are as published on the research date and change often.</footer>
</div>
<script>
(function () {
  var tabs = Array.prototype.slice.call(document.querySelectorAll('nav.tabs button'));
  function show(key) {
    var found = tabs.some(function (b) { return b.getAttribute('data-tab') === key; });
    if (!found) key = 'summary';
    tabs.forEach(function (b) {
      var on = b.getAttribute('data-tab') === key;
      b.setAttribute('aria-selected', on ? 'true' : 'false');
      b.tabIndex = on ? 0 : -1;
      document.getElementById('p-' + b.getAttribute('data-tab')).hidden = !on;
      if (on) { var n = b.parentNode; if (n.scrollWidth > n.clientWidth) n.scrollLeft = Math.max(0, b.offsetLeft - n.offsetLeft - 16); }
    });
  }
  tabs.forEach(function (b, i) {
    b.addEventListener('click', function () {
      show(b.getAttribute('data-tab'));
      try { history.replaceState(null, '', '#' + b.getAttribute('data-tab')); } catch (e) {}
      var top = document.querySelector('nav.tabs').getBoundingClientRect().top;
      if (top < 0) window.scrollTo(0, window.scrollY + top);
    });
    b.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      var t = tabs[(i + d + tabs.length) % tabs.length]; t.click(); t.focus();
    });
  });
  show((location.hash || '').slice(1));
})();
</script>
"""
open(OUT, "w").write(page)
print(len(tabs), "tabs", round(len(page) / 1024), "KB")
