# Kelen market analysis: research pack A (Senegal and Côte d'Ivoire)

Compiled on 2026-10-14. Primary sources were downloaded and read where possible: BCEAO financial inclusion report 2024, BCEAO digital financial services report 2024, BCEAO banking conditions report 2024, Commission Bancaire key figures 2024, BCEAO payment-institution and EME lists (Feb 2026), the World Bank API (WDI and Global Findex 2025), World Bank Enterprise Survey profiles, the ANStat Répertoire national des entreprises 2024, the Senegal MEFP outlook (April 2026), and the Partech 2025 report.

**Confidence labels**
- **verified**: read in the primary document or the official dataset/API.
- **verified (secondary)**: a reputable press report that cites an official source; the primary document was not opened.
- **estimate**: derived by me (the method is shown) or from a source of uncertain quality.
- **not found**: searched for but not located.

**Search limit.** The web-search budget ran out during this session. Some items (Senegal e-invoicing, the IFC finance gap, the CI mobile-money tax, CNPS employer counts) are therefore marked *not found / not verified* and should be re-checked.

FX used for conversions: 2024 ≈ 606 FCFA/USD and 2025 ≈ 582 FCFA/USD. These are implied by the World Bank GDP series (FCFA vs USD).

---

## 1. Macro

| Indicator | Senegal | Côte d'Ivoire | Year | Source URL | Confidence |
|---|---|---|---|---|---|
| Population | 18.50 M (2024); 18.93 M (2025) | 31.93 M (2024); 32.71 M (2025) | 2024-25 | https://api.worldbank.org/v2/country/SEN;CIV/indicator/SP.POP.TOTL | verified |
| Urban share of population | 55.2% (2024); 55.8% (2025) | 54.0% (2024); 54.5% (2025) | 2024-25 | https://api.worldbank.org/v2/country/SEN;CIV/indicator/SP.URB.TOTL.IN.ZS | verified |
| Nominal GDP (FCFA) | 19,506 bn (2024); 21,535 bn (2025); 22,306 bn proj. 2026 (MEFP, "hors rebasing") | 52,821 bn (2024); 58,061 bn (2025) | 2024-26 | SN: https://www.economie.gouv.sn/sites/default/files/2026-04/SENEGAL_Developpements_economiques_recents_et_Perspectives.pdf ; CI: https://api.worldbank.org/v2/country/CIV/indicator/NY.GDP.MKTP.CN | verified |
| Nominal GDP (USD) | 32.2 bn (2024); 37.0 bn (2025) | 87.1 bn (2024); 99.8 bn (2025); IMF ~112 bn in 2026 (via Worldometer) | 2024-26 | https://api.worldbank.org/v2/country/SEN;CIV/indicator/NY.GDP.MKTP.CD ; https://www.worldometers.info/fr/pib/cote-d-ivoire-pib/ | verified (2026: secondary) |
| GDP per capita (USD) | 1,739 (2024); 1,955 (2025) | 2,728 (2024); 3,050 (2025) | 2024-25 | https://api.worldbank.org/v2/country/SEN;CIV/indicator/NY.GDP.PCAP.CD | verified |
| Real GDP growth 2024 | 6.3-6.5% (ANSD 6.3%; MEFP 6.5%; WB 6.46%) | 6.0% (WB) | 2024 | https://www.ansd.sn/ ; https://api.worldbank.org/v2/country/SEN;CIV/indicator/NY.GDP.MKTP.KD.ZG | verified |
| Real GDP growth 2025 | 6.5% (ANSD prov.) / 6.7% (IMF, MEFP). First full year of oil. Non-hydrocarbon growth only 2.2% (IMF); growth excluding hydrocarbons and agriculture was 1.6% (MEFP) | 6.5% (IMF/WB); WB country page says 6.3% | 2025 | https://www.imf.org/en/news/articles/2026/09/01/pr26282-senegal-imf-reaches-sla-ecf-arrangement ; https://www.imf.org/fr/news/articles/2026/04/30/pr-26132-cote-divoire-imf-reaches-agreement-on-6th-rev-of-eff-ecf-arrange-5th-rev-of-rsf-arrange | verified |
| Real GDP growth 2026 (forecast) | 2.5% (MEFP, Apr 2026). Excluding hydrocarbons and agriculture: 3.0%. IMF/WEO about 2.2% (secondary). Q1-2026 non-hydrocarbon growth 4.7% y/y (IMF). ANSD Q2-2026 real GDP +0.1% q/q (SA) | 6.0% (IMF SLA, Apr 2026); 6.2% (IMF WEO Apr 2026); WB downside 5.8% | 2026 | MEFP PDF above; https://www.ansd.sn/flash-stats ; IMF CI release above | verified (WEO figures: secondary) |
| Medium-term growth | Nominal GDP growth only 3.5% in 2026, then 6-8% from 2030 (MEFP DSA) | About 6.7% average (IMF); national plan PND 2026-30 targets 7.2% | 2026-30 | MEFP PDF; IMF CI release | verified |
| Inflation (CPI) | 0.8% (2024); 1.4% (2025) | 3.5% (2024); 0.1% (2025); 3.3% proj. 2026 (IMF) | 2024-26 | https://api.worldbank.org/v2/country/SEN;CIV/indicator/FP.CPI.TOTL.ZG ; IMF CI release | verified |
| BCEAO policy rate | Corridor cut 25 bp in March 2026 (minimum rate 3.0%, marginal lending rate 5.0%) | same (WAEMU) | 2026 | MEFP PDF (p.33-34) | verified (secondary in MEFP) |
| Oil/gas weight | Hydrocarbons 2.8% of GDP (2024) and 5.2% (2025). Expected to decline to 4.6% (2026) and 1.7% by 2033. Hydrocarbons contributed +4.5 pp to 2025 growth | n/a | 2024-33 | MEFP PDF (annex table) | verified |
| Public debt | IMF: 132% of GDP end-2024, including about 4% of GDP domestic arrears; this is pre-GDP-rebasing. MEFP DSA: 121.3% (2024), falling to 114.9% (2027) and ~84% (2034). Moody's: ~108% | not collected (moderate; under IMF programme) | 2024-34 | https://www.imf.org/en/news/articles/2025/11/06/pr-25360-senegal-imf-concludes-visit ; MEFP PDF | verified |
| Fiscal deficit | 13.4% of GDP (2024); 7.8% proj. (2025); 5.4% target (2026) | not collected | 2024-26 | IMF Nov-2025 release; MEFP PDF | verified |
| Gross financing needs | 27.5% of GDP (2025); 26.1% (2026). Debt service up to 24.1% of GDP in 2026 | n/a | 2025-26 | MEFP PDF | verified |
| Domestic market borrowing | Senegal raised 2,225 bn FCFA on the WAEMU regional market in 2025 (998 bn in 2024; +122.8%). Large participation by Ivorian banks | n/a | 2025 | MEFP PDF | verified |
| IMF programme status | The 2023 programme was frozen in 2025 after the misreporting (hidden debt) was revealed. A **staff-level agreement on a new 36-month ECF of ~US$2.2 bn (SDR 1,537 m) was reached on 1 Sept 2026**. It still needs Board approval, which is conditional on corrective actions on misreporting (waiver) and financing assurances. The government is seeking a "debt treatment" via an enhanced G20 Common Framework; FCFA debt is reportedly excluded | The 2023-26 EFF/ECF (SDR 2.6 bn) reached SLA on its **6th and final review** in April 2026 (about US$844 m disbursement) | 2025-26 | https://www.imf.org/en/news/articles/2026/09/01/pr26282-senegal-imf-reaches-sla-ecf-arrangement ; https://www.imf.org/fr/news/articles/2026/04/30/pr-26132-cote-divoire-imf-reaches-agreement-on-6th-rev-of-eff-ecf-arrange-5th-rev-of-rsf-arrange | verified |
| Labour force | 5.93 M (2024) | 12.67 M (2024) | 2024 | https://api.worldbank.org/v2/country/SEN;CIV/indicator/SL.TLF.TOTL.IN | verified (ILO modelled) |
| Wage and salaried workers, % of employment | 35.3% (2024) | 28.7% (2024) | 2024 | https://api.worldbank.org/v2/country/SEN;CIV/indicator/SL.EMP.WORK.ZS | verified (ILO modelled) |
| Unemployment | 21.6% (ANSD national definition) | not collected | 2024 | https://senego.com/rapport-de-lansd-2024-le-chomage-franchit-la-barre-des-21-et-revele-une-fracture-precise-sur-le-marche-de-lemploi_1932269.html | verified (secondary) |

Notes:
- Senegal rebased its GDP in December 2025. Debt ratios and WB GDP series may mix pre- and post-rebasing bases.
- The AfDB Senegal page quotes growth of 8.3% (2025) and 5.9% (2026). These figures look outdated and were not retained.

---

## 2. Businesses

| Indicator | Senegal | Côte d'Ivoire | Year | Source URL | Confidence |
|---|---|---|---|---|---|
| Total economic units (formal and informal census) | 407,882 units (RGE 2016; units with fixed premises only). 97% informal under the ANSD definition (no SYSCOA accounts); 85.4% informal under the ILO definition. About 12,200 formal. A second RGE was in the field in 2026, with no results yet | Just over 1.2 M enterprises (RGEE census, 75% complete at 15 May 2025), of which about 600,000 in Abidjan. Final results not found | 2016 / 2025 | https://africacheck.org/fr/fact-checks/articles/senegal-des-donnees-sur-le-secteur-informel-examinees ; https://www.koaci.com/article/2025/05/16/cote-divoire/societe/cote-divoire-recensement-general-des-entreprises-et-etablissements-un-peu-plus-de-12-million-dentreprises-formelles-et-informelles-repertoriees_186913.html | verified (secondary) |
| Formal / modern-sector enterprises | 20,388 "modern sector" units, 93.7% of them SMEs (ANSD Situation économique et sociale 2024) | 82,548 formal enterprises in the RSE (ANStat, BDF 2022 data, published 2024): 95.4% SMEs, 4.6% large | 2022-24 | https://senego.com/pres-de-22-000-milliards-generes-en-2024-mais-lansd-releve-une-baisse-sur-ce-registre-specifique_1932453.html ; https://media-files.abidjan.net/document/docs/document_fb9nxv55e5k.pdf | SN verified (secondary); CI verified |
| Size split, by turnover | n/a | Micro/TPE (≤30 M FCFA turnover): 55,641 (67.4%); SMEs (30 M-1 bn): 22,890 (27.7%); large (>1 bn): 3,817 (4.6%). Large firms make over 90% of turnover | 2022 | ANStat RSE 2024 PDF (above) | verified |
| Size split, by headcount | n/a | <5 employees: 60.8%; 5-50: 17.8%; 50-200: 1.5%; 200-500: 0.4%; 500+: 0.3%; not available: 19.3% | 2022 | ANStat RSE 2024 PDF | verified |
| Employment in formal firms | 335,653 jobs in the modern sector excluding public administration (2024, -0.6%); 341,945 at Q4-2025 | 896,191 persons in RSE firms (642,711 internal staff + 253,480 external) | 2024-25 | senego ANSD 2024 article (above); https://fr.allafrica.com/stories/202602030415.html ; ANStat RSE PDF | SN verified (secondary); CI verified |
| Formal employers (social security) | IPRES members (employers): 40,300 in 2024 (38,381 in 2023). IPRES contributors: 577,171 (2024) | CNPS: "près de 49,000 entreprises déclarées", 23 agencies (gov.ci, April 2025; from a search snippet, page not fully read) | 2024-25 | https://www.senegal24news.com/societe/revenu-salaires-au-senegal-hausse-des-adherents-a-lipres-en-2024/ ; https://www.gouv.ci/actualite/protection-sociale-environ-12-million-de-travailleurs-du-secteur-prive-et-pres-dun-million-de-travailleurs-independants-declares-a-la-cnps-2374 | SN verified (secondary); CI estimate (unverified) |
| Declared private-sector employees | 577,171 IPRES contributors (2024). The ANSD modern-sector count is 335,653 (different scope) | About 1.2 M private-sector workers declared at CNPS (gov.ci headline), plus ~1 M independent workers. Another gov.ci flash cites 975,000 declared workers. Formal jobs stock: 1,426,303 in 2023 (all sectors, +117,401) | 2023-25 | as above; https://www.sikafinance.com/marches/cote-divoire-le-nombre-demplois-formels-progresse-de-117-401-en-2023_46805 | verified (secondary); figures inconsistent |
| New company registrations / year | NINEA registrations: 91,936 in 2024 (95,982 in 2023; -4.2%). 72.7% individual enterprises, 6.7% GIE, 2.9% SARL; commerce 64.1%. APIX: ~9,200 companies created in H1-2025 | CEPICI: 26,948 created in 2025 (25,477 in 2024), of which SARL 21,538 | 2024-25 | senego ANSD article; https://www.agenceecofin.com/actualites/2409-131764-senegal-9-7-milliards-d-investissements-prives-enregistres-en-2024-selon-l-apix ; https://www.aip.ci/325086/ ; https://cepici.ci/nos-statistiques | verified (secondary) |
| Firm survival | ENDES (2018 cohort followed to 2024): 57.0% active, 16.8% closed, 26.2% never started. 63.1% of never-started firms cite lack of financing | not found | 2024-26 | https://www.ansd.sn/actualite/lansd-presente-les-resultats-de-lenquete-nationale-sur-la-demographie-des-entreprises-du | verified (secondary) |
| Sector mix of formal firms | NINEA new registrations: commerce 64.1%. Enterprise turnover 21,927 bn FCFA (2024, +4.9%) | Commerce 43.9%; construction 9.5%; manufacturing 8.2%; professional/scientific 6.7%; support services 5.3%; education 4.8%; hospitality 4.8% | 2022-24 | as above | verified |
| Geographic concentration | Dakar share: **not found** in 2024-26 sources (RGE 2016 detail not retrieved) | Abidjan holds 72.3% of formal firms (59,700). The Abidjan district holds 73.4%; Cocody alone is 30.8% of Abidjan firms. About 600k of 1.2 M census units are in Abidjan | 2022-25 | ANStat RSE PDF; KOACI | CI verified; SN not found |
| Formal-sector payroll | Private formal wage bill **1,540.4 bn FCFA (2024)**, +6.9%; 1,440.4 bn (2023); 92% to permanent staff. Personnel costs of all enterprises: 2,263.9 bn | not found (see section 7 estimate) | 2024 | https://www.sikafinance.com/premium/senegal-la-masse-salariale-du-secteur-prive-formel-a-franchi-1-500-milliards-fcfa-en-2024_60395 ; senego ANSD article | verified (secondary) |
| Pro-SME share of economy | n/a | SMEs are ~98% of firms (Côte d'Ivoire PME agency, gov.ci) and about 20% of value added (BCEAO FAQ / press) | 2025 | gov.ci page above | estimate |

---

## 3. Financial inclusion

### 3a. BCEAO indicators (2024, published April 2026)

Source: https://www.bceao.int/sites/default/files/2026-06/Rapport_Annuel_Inclusion_Financiere_2024.pdf (annex tables 3-8).

| Indicator | Senegal | Côte d'Ivoire | WAEMU | Year | Confidence |
|---|---|---|---|---|---|
| Strict banking rate (TBS, bank accounts / adults) | 23.1% (22.4% in 2023) | 33.6% (31.2% in 2023) | 25.2% | 2024 | verified |
| Extended banking rate (TBE, + microfinance) | 62.4% | 46.2% | 47.4% | 2024 | verified |
| Overall use of financial services (TGUSF, + e-money, adjusted for multi-banking) | 85.9% | 86.7% | 73.6% | 2024 | verified |
| Synthetic financial inclusion index (0-1) | 0.643 | 0.636 | 0.600 | 2024 | verified |
| Points of service per 100,000 adults (TGPSFd) | 201 | 224 | 193 | 2024 | verified |
| Average bank lending rate (TINc) | 5.93% | 6.45% | 6.76% | 2024 | verified |
| Average bank deposit rate (TINd) | 5.56% | 4.87% | 5.26% | 2024 | verified |
| E-money usage rate (WAEMU) | - | - | 57.2% of adults (microfinance 22.2%, banks 21.8%) | 2024 | verified |

### 3b. Global Findex 2025 (survey year 2024, adults 15+)

Source: World Bank API, source 28: https://api.worldbank.org/v2/country/SEN;CIV/indicator/account.t.d?source=28

| Indicator | Senegal | Côte d'Ivoire | Year | Confidence |
|---|---|---|---|---|
| Account (any) | 76.5% (56.0% in 2021) | 57.6% (50.8% in 2021) | 2024 | verified |
| Bank or similar financial-institution account | 48.0% | 16.8% | 2024 | verified |
| Mobile money account | 66.9% | 53.4% | 2024 | verified |
| Owns a debit card | 32.7% | 7.0% | 2024 | verified |
| Saved at a FI or via mobile money | 58.3% | 35.6% | 2024 | verified |
| Borrowed from a formal FI | 17.6% | 3.9% | 2024 | verified |

### 3c. E-money (BCEAO DFS report 2024, Commission Bancaire 2024)

Sources: https://www.bceao.int/sites/default/files/2026-03/Rapport%20annuel%20sur%20les%20services%20financiers%20num%C3%A9riques%20dans%20l'UEMOA%20-%202024.pdf and https://www.bceao.int/sites/default/files/inline-files/Chiffres_cl%C3%A9s_du_Rapport_annuel_2024_de_la_Commission_Bancaire.pdf

| Indicator | Senegal | Côte d'Ivoire | WAEMU | Year | Confidence |
|---|---|---|---|---|---|
| E-money accounts opened | ≈42.5 M (17.12% of the WAEMU total) | 99 M (40.07%) | 248 M (+19%) | 2024 | verified (SN derived from share) |
| Active accounts (90 days) | not split by country in report | not split | 76.86 M (31% activity rate) | 2024 | verified |
| Transaction volume | ≈2.65 bn (24.1% of WAEMU; #1) | ≈2.35 bn (21.4%) | 11 bn (33 M/day) | 2024 | verified (country derived from shares) |
| Transaction value | ≈48,400 bn FCFA (30.2%), about 2.5x GDP | ≈55,700 bn FCFA (34.7%), about 1.05x GDP | 160,415 bn FCFA (119% of GDP) | 2024 | verified (country derived) |
| Volume growth | +24.8% | +19.9% | +27% | 2024 | verified |
| Registered merchants (QR) | +66% | 2.72 M (from 1.13 M) | 3.7 M registered; 1.7 M active | 2024 | verified |
| Salary payments via e-wallet | n/a | n/a | 28 M transactions, 891 bn FCFA, average 31,185 FCFA (0.57% of value) | 2024 | verified |
| Wallet↔bank transfers | n/a | n/a | 29.2 M ops (+97.5%), 2,384 bn FCFA (+73.8%) | 2024 | verified |
| P2P transfers | n/a | n/a | 2.3 bn ops, 42,762 bn FCFA, average 18,220 FCFA | 2024 | verified |
| Cash-out ratio | n/a | n/a | About 88% of e-money deposits are withdrawn (net digitalisation ratio 7.5%) | 2024 | verified |
| Market share, WAEMU volume | - | - | Orange 38.4%, Wave 28.4%, MTN 17.4%, Moov 6.9%, YAS 3% | 2024 | verified |
| Market share, WAEMU value | - | - | Orange 41.3%, **Wave 38.2%**, MTN 11.7% | 2024 | verified |
| E-money float outstanding (EMEs only) | - | - | 1,411.7 bn FCFA | 2024 | verified |
| Mobile money accounts (ARTCI) | - | 26.88 M (Q1-2026) | - | 2026 | estimate (secondary, unverified) |

### 3d. Institutions

| Indicator | Senegal | Côte d'Ivoire | WAEMU | Year | Source URL | Confidence |
|---|---|---|---|---|---|---|
| Credit institutions | 33 (29 banks + 4 bank-like FIs), end-2025 | 32 (28 banks + 4), end-2024; 33 (29 + 4) end-2025 | 160 (135 banks), 2024; 161 end-2025 | 2024-25 | https://www.financialafrik.com/2026/04/01/uemoa-banques-161-etablissements-de-credit-agrees-a-la-fin-2025/ ; https://economie-ivoirienne.ci/banques-et-finances/presentation-du-systeme-bancaire-ivoirien.html ; CB key figures | verified (secondary for country) |
| Bank balance sheet | ~15,700 bn FCFA (2025); CBAO #1 at ~11% | 25,645 bn FCFA (2024; 35.6% of WAEMU) | 72,068 bn (2024) | 2024-25 | as above | verified (secondary) |
| Bank accounts | n/a | 7,744,745 (2024) | 22.2 M (2024) | 2024 | as above; CB key figures | verified |
| Microfinance (SFD) | per-country count **not found** | per-country count not found | 286 SFD supervised by the Commission Bancaire (large SFDs) | 2024 | CB key figures | verified (WAEMU only) |
| E-money institutions (EME) | 5: Orange Finances Mobiles, Mobile Cash (Free Money / Mixx), Wave Digital Finance, QuickPay, Touchpoint | 4: Orange Money CI, MTN MFS, Moov Money, Djogana Pay | 18 | Feb 2026 | https://www.bceao.int/fr/content/etablissements-de-monnaie-electronique | verified |
| E-money initiatives (all issuers including bank partnerships) | 11 | 19 | 69 | 2024 | BCEAO DFS 2024 | verified |
| Payment institutions licensed (Instr. 001-01-2024) | **11**: Dunya, Mikaty, Bictorys, Flutterwave SN, Samir Money, Versus Finances Tech, Copay, Sesa Digital Finance, Julaya SN, Djamo SN, African Financial Agent | **9**: Syca, Touchpoint, Firstcom, Julaya CI, Djamo CI, FeexPay, CinetPay, Dunya, Paymetrust | 31 (Feb 2026); ~34 (list at 31 Aug 2026, secondary) | 2026 | https://www.bceao.int/sites/default/files/2026-03/LISTE%20DES%20ETABLISSEMENTS%20DE%20PAIEMENT%20AGR%C3%89%C3%89S%20DANS%20L%E2%80%99UMOA%20au%2031%20janvier%202026.pdf | verified (Feb 2026) |
| PI-SPI participants authorised | 43 | 38 | 175 (at 30 Sept 2026; 104 two months earlier) | 2026 | https://www.financialafrik.com/2026/10/01/bceao-liste-des-175-participants-autorises-a-ouvrir-les-services-de-pi-spi-au-public-au-30-septembre-2026/ | verified (secondary) |
| Card penetration | Debit card ownership 32.7% of adults | 7.0% | Cards are 1.74% of e-payment transactions; e-money is 98% | 2024 | Findex; BCEAO DFS 2024 | verified |

---

## 4. SME finance

| Indicator | Senegal | Côte d'Ivoire | Year | Source URL | Confidence |
|---|---|---|---|---|---|
| Firms naming access to finance as **biggest obstacle** (WBES) | **45.9%** (small 49.6%, medium 36.5%); SSA average 30.8%. It is the #1 obstacle | 21.6% (small 27.6%, medium 17.8%). Political instability (19.5%) and crime (13.4%) are next | SN 2024; CI 2023 | https://www.enterprisesurveys.org/content/dam/enterprisesurveys/documents/country/Senegal-2024.pdf ; https://www.enterprisesurveys.org/content/dam/enterprisesurveys/documents/country/Cote-Divoire-2023.pdf | verified |
| Firms with checking/savings account | 90.7% (small 88.0%) | 89.9% (small 87.3%) | 2024/2023 | as above | verified |
| Firms using banks to finance investment | 34.7% (small **10.8%**) | 38.4% (small 31.1%) | 2024/2023 | as above | verified |
| Investment financed internally | 66.9% (small 86.0%) | 70.0% | 2024/2023 | as above | verified |
| Firms using supplier/customer credit for working capital | 35.4% | 31.4% | 2024/2023 | as above | verified |
| Firms competing with informal firms | 55.2% | 76.5% | 2024/2023 | as above | verified |
| Collateral requirements (value of collateral / loan) | not extracted (not in profile appendix) | not extracted | - | WBES microdata: https://microdata.worldbank.org/index.php/catalog/6699 | not found |
| MSME share of bank credit to legal entities (WAEMU) | - | - | 52% in 2024 (49% in 2023) | https://www.bceao.int/sites/default/files/2025-07/Rapport%20sur%20les%20conditions%20de%20banque%20dans%20l'UEMOA%20-%202024_compressed.pdf | verified |
| Average lending rate, MSMEs vs large firms (WAEMU) | - | - | MSME 7.07% vs large firms 6.06% (2024) | same | verified |
| New bank loans, total | 5,699.6 bn FCFA (2024); avg rate 5.93% | 7,377.4 bn FCFA (2024); avg rate 6.45% | 2024 | same (country annex tables 4.x for CI and 8.x for SN) | verified |
| New loans to private productive firms | 3,877.3 bn FCFA at 4.87% | 5,582.1 bn at 6.37% | 2024 | same | verified |
| New loans to individual enterprises (proxy for micro/sole traders) | 97.1 bn FCFA at 7.11% | 440.6 bn at 6.93% | 2024 | same | verified |
| SME credit outstanding (WAEMU) | - | - | 6,844 bn FCFA (2025, +22%), about 17.6% of bank credit (derived). BCEAO SME support scheme: 4,053 SMEs financed in 2025 (118 bn FCFA) | https://afrikinfos-mali.com/2026/08/10/appui-bceao-2025-6-844-milliards-de-fcfa-accordes-aux-pme/ | verified (secondary) |
| Effective SME loan rates in practice | Consultant claims of 10-18% and collateral of 150-200% are unsourced | same | 2026 | https://ccarree.com/financement-pme-uemoa-dispositifs-bceao-2026/ | estimate (low quality) |
| SME financing gap (IFC/AfDB) | **not found** (search budget exhausted) | IFC states that 78% of SMEs cite financing constraints as a major obstacle | 2025 | https://www.ifc.org/en/pressroom/2025/ifc-partners-with-financial-institutions-in-c-te-d-ivoire-to-boost-access-to-finan | gap figure not found |
| Credit to economy / GDP | 33.9% (2026 projection); credit growth +8.4% (2025) | not collected | 2025-26 | MEFP PDF | verified |
| How salaries are paid: private-sector wage earners, % of adults | 25.6% of adults receive private wages | 16.9% | 2024 | Findex (fin32.n33) | verified |
| Private wages paid into a bank/FI account (% of adults) | 8.4% | 1.9% | 2024 | Findex fin32.n33.34a | verified |
| Private wages paid via mobile phone (% of adults) | 16.4%, i.e. **64% of private wage recipients** | 5.5% (≈33% of recipients) | 2024 | Findex fin32.n33.34b(.s) | verified (CI share derived) |
| Private wages paid in cash only (% of adults) | 7.2% (≈28% of recipients) | 9.7% (**≈57% of recipients**) | 2024 | Findex fin32.n33.34c | verified (shares derived) |
| All wages received into an account (% of wage recipients) | 74.3% | ≈46% (9.4/20.3) | 2024 | Findex fin32.acc(.s) | verified (CI derived) |
| Cash usage among firms (survey) | not found | not found | - | - | not found |

Note on the Findex wage data: it covers *all* wage earners, including informal ones. Senegal is unusually advanced on mobile payroll, with about two-thirds of private wage earners paid by phone, probably via Wave. In CI, cash still dominates private payroll, so the payroll-digitisation headroom is larger there.

---

## 5. Digital infrastructure

| Indicator | Senegal | Côte d'Ivoire | Year | Source URL | Confidence |
|---|---|---|---|---|---|
| Own a mobile phone (adults) | 87.3% | 89.2% | 2024 | Findex (con1) via WB API | verified |
| **Main phone is a smartphone** (adults) | **60.8%** | **45.7%** | 2024 | Findex (con9a) via WB API | verified |
| Internet users (% population) | 60.1% (ITU, 2024); 60.6% / 11.5 M (DataReportal, end-2025) | 41.4% (ITU, 2024); 40.7% / 13.4 M (DataReportal) | 2024-25 | https://api.worldbank.org/v2/country/SEN;CIV/indicator/IT.NET.USER.ZS ; https://datareportal.com/reports/digital-2026-senegal ; https://datareportal.com/reports/digital-2026-cote-divoire | verified |
| Mobile subscriptions per 100 | 123.9 (2024) | 183.9 (2024) | 2024 | https://api.worldbank.org/v2/country/SEN;CIV/indicator/IT.CEL.SETS.P2 | verified |
| Mobile connections | 23.3 M (122%), 91.3% on 3G/4G/5G (end-2025, GSMA via DataReportal). ARTP: 24.15 M lines (Q4-2024) | 49.7 M (151%) per DataReportal. ARTCI: 60.5 M subscriptions (Q1-2025) | 2024-25 | DataReportal; https://artp.sn/sites/default/files/2025-03/RAPPORT%20MARCHE%20TELECOMS%20T4%202024_0.pdf ; ARTCI via https://digitalmag.ci/rapport-artci-1er-trimestre-2025-les-statistiques-du-marche-des-telecoms-en-cote-divoire/ | verified (secondary for regulators) |
| Mobile internet subscriptions | 23.39 M internet subs (96% mobile), 125.8% penetration (ARTP, 31 Dec 2025) | 38.5 M (Q4-2025) / 40.9 M (Q1-2026) | 2025-26 | https://www.osiris.sn/senegal-le-taux-de-penetration-de-l-internet-estime-a-108-31.html ; https://aristechnologies.ci/blog/rapport-artci-internet-cote-divoire-2025.html | estimate (secondary) |
| 4G coverage | **not found** (ARTP 3G/4G broadband penetration 89.8% at Q3-2023) | 91% geographic 4G coverage (ARTCI Q1-2023 via Logistics Cluster); other sources give 63.7-80% | 2023 | https://lca.logcluster.org/fr/print-preview/5980 | estimate |

---

## 6. Payments market structure and regulation

| Topic | Senegal | Côte d'Ivoire | Year | Source URL | Confidence |
|---|---|---|---|---|---|
| **PI-SPI** (BCEAO instant payments) | Pilot started 22 Jul 2024 (25 institutions). **Official launch 30 Sept 2025 (Dakar)**. 24/7 interoperability across banks, EMEs, MFIs and payment institutions. 175 participants (30 Sept 2026; SN 43, CI 38); >38 M people with access. An "API Business" list of 24 names exists (mid-Sept 2026). **Wave has joined** (Ecofin headline, Oct 2026). From **2 Nov 2026**, interoperable e-money transfers must route via PI-SPI. Domestic sends free up to a cumulative 8,000 FCFA/day per user per participant (about 75% of transactions); 0-0.8% excl. tax above that; receiving is free. Cross-border on the same terms from 1 Jun 2027 | same (regional) | 2024-27 | https://www.bceao.int/fr/content/lancement-officiel-de-la-plateforme-interoperable-du-systeme-de-paiement-instantane-pi-spi ; https://www.financialafrik.com/2026/10/04/la-bceao-rend-pi-spi-obligatoire-revoit-ses-tarifs-et-pose-enfin-la-question-de-nouveaux-services-financiers-adosses-a-la-plateforme/ ; https://www.agenceecofin.com/actualites/0510-142111-paiements-numeriques-la-bceao-revoit-les-regles-de-pi-spi-alors-que-wave-rejoint-le-reseau | verified (BCEAO launch); secondary (tariffs) |
| PI-SPI volumes | not published / not found | not found | - | - | not found |
| Wave effect on pricing | Wave launched in SN in 2018 with a 1% send fee and free deposits, withdrawals and bill pay. Orange Money previously charged about 6-10% on some flows. Orange cut fees, made withdrawals free and set an 0.8% send fee (late 2021). Orange Money's share of Sonatel revenue fell from 12% (2021) to 9.1% (H1-2022) | Orange, MTN and Moov cut transfer fees; 1% benchmark | 2018-22 | https://osiris.sn/wave-vs-orange-money-la-guerre-des-tarifs-au-bonheur-des-clients.html ; https://connectionivoirienne.net/2021/10/27/transfert-dargent-en-cote-divoire-qui-veut-tuer-la-concurrence/ | verified (secondary) |
| Current tariff level | Benchmark about 1% send (Wave), with a regulatory ceiling of 0-0.8% on PI-SPI interop above 8,000 FCFA/day | similar | 2026 | as above | estimate |
| Transfer tax | **TTA 0.5%** of the amount, **capped at 2,000 FCFA per operation**, on transfers, payments and withdrawals over 20,000 FCFA/24h. **Exempt: deposits, salary and scholarship payments**, distribution-network flows. Law 2025-17 of 27 Sept 2025 (PRES), in force 16-17 Dec 2025. A 1.5% rate on merchant payments was mooted but not confirmed | CI mobile-money tax: **not verified** | 2025-26 | https://www.seneweb.com/en/news/Societe/orange-money-la-taxe-sur-les-transferts-dargent-tta-de-05-entre-en-vigueur-des-le-17-decembre_n_477669.html ; https://www.orange.sn/assistance/tutoriels/informations-sur-lapplication-de-la-loi-sur-la-collecte-de-taxes-sur-le | verified (secondary, operator notice) |
| E-invoicing / tax digitalisation | DGID e-invoicing: **not verified** (search budget exhausted) | **FNE (facture normalisée électronique)**: Arrêté 0337 of 9 May 2025. Phased from June 2025 and reportedly mandatory for all regimes from Dec 2025 (secondary). About 52,000 firms registered by 24 Feb 2026, of which 60-70% had issued at least one invoice. DGI nationwide controls from **1 Sept 2026** (RNI, RSI, RME and entreprenant regimes); FENACCI asked for suspension. Fines up to 10 M FCFA (secondary). Registration is required for the tax-compliance certificate (ARF) used in public tenders | 2025-26 | https://www.pulse.ci/article/facture-normalisee-electronique-fne-tout-ce-qui-change-pour-les-entreprises-ivoiriennes-en-2026-2026022802421220085 ; https://www.koaci.com/article/2026/08/26/cote-divoire/economie/cote-divoire-operation-de-controle-de-la-facturation-normalisee-electronique-a-partir-du-1er-septembre-voici-les-entreprises-visees_199883.html | CI verified (secondary); SN not found |
| Electronic salary payment obligation | **not found** | **not found** | - | - | not found |
| Payment services regulation | BCEAO **Instruction 001-01-2024** (in force 23 Jan 2024): payment services require an EP licence, with minimum capital by service type. The transition deadline was extended several times (31 Jul 2024, then 31 Jan 2025, then 1 May 2025, then **31 Aug 2025**). From 1 Sept 2025, unlicensed fintechs must stop. The e-money instruction 008-05-2015 is under revision | same | 2024-26 | https://www.agenceecofin.com/finance/0602-115903-la-bceao-definit-les-conditions-et-modalites-de-fourniture-de-services-de-paiement-au-sein-de-l-umoa ; https://news.abidjan.net/articles/742142/umoa-la-bceao-prolonge-le-delai-de-mise-en-conformite-pour-les-services-de-paiement-jusquau-31-aout-2025 ; BCEAO DFS 2024 §67 | verified (secondary) |

---

## 7. Market-sizing inputs for Kelen

| Input | Senegal | Côte d'Ivoire | Year | Basis / Source | Confidence |
|---|---|---|---|---|---|
| Formal employers (core payroll TAM) | ~40,300 (IPRES) | ~49,000 (CNPS, unverified) | 2024-25 | section 2 | SN verified; CI estimate |
| Formal enterprises (incl. non-employers) | 20,388 modern-sector units; ~92k new NINEA registrations per year (mostly sole traders) | 82,548 (RSE); 26,948 new companies per year; 52,000 on FNE | 2022-26 | section 2 | verified |
| **Digital-ready SMEs (estimate)** | **≈20,000-28,000** | **≈25,000-35,000** | 2026 | Method: formal employers × ~60-75%. The ratio reflects that ~88-90% of small formal firms already have a bank account (WBES), and that firms are concentrated in Dakar/Abidjan (CI 72%), where smartphone and mobile-money use are highest. Large firms (~4-5%) are excluded. Very rough; validate with interviews | estimate |
| **Annual formal private payroll** | **1,540 bn FCFA (≈US$2.5 bn) in 2024**. Implied average ≈4.6 M FCFA/yr (≈382k FCFA/month) per modern-sector employee (1,540.4 bn / 335,653) | **≈2,200-4,300 bn FCFA (≈US$3.6-7.1 bn)**, assuming 0.9-1.2 M declared private workers × 200-300k FCFA/month. No official wage bill found | 2024 | SN: ANSD via Sikafinance/Senego; CI: own estimate | SN verified (secondary); CI estimate |
| Monthly payroll flow (for payout-volume modelling) | ≈128 bn FCFA/month | ≈180-360 bn FCFA/month | 2024 | derived from the line above | estimate |
| Salary flows already on e-money | WAEMU-wide only 891 bn FCFA/yr (28 M payments, avg 31k FCFA). This suggests most formal payroll still goes bank-to-bank or in cash, and e-wallet payroll is mostly low-wage | same | 2024 | BCEAO DFS 2024 | verified |
| B2B payments flows | not found. Proxies: WAEMU e-money merchant + bill payments 13,710 bn FCFA (2024); wallet↔bank 2,384 bn FCFA | - | 2024 | BCEAO DFS 2024 | verified (proxy) |
| Fintech / tech VC funding | **US$223 M** in 2025 (equity 84, debt 139; #5 in Africa). Debt is dominated by one Wave facility; 12 deals. 2024: ~US$36 M | **US$22 M** in 2025 (equity 10, debt 11). 2024: ~US$30 M | 2024-25 | https://partech-admin.prod.unomena.io/media/documents/2025_Partech-Africa-Tech-VC-Report.pdf | 2025 verified; 2024 secondary |
| Francophone context | Francophone "rest of Africa" equity was US$252 M in 2025, 68% of equity outside the big four. Africa total US$4.1 B; fintech US$1.49 B | - | 2025 | Partech 2025 | verified |
| Direct licensed competitors (EP/EME) | Julaya, Djamo, Bictorys, Flutterwave, Dunya, Mikaty, Copay, Sesa etc. (EP); Wave, Orange, Free/Mixx (EME) | Julaya, Djamo, CinetPay, FeexPay, Paymetrust, Syca etc. (EP); Orange, MTN, Moov (EME); Wave CI via bank partnership | 2026 | BCEAO lists (section 3d) | verified |

---

## 8. Trends and risks

| Topic | Senegal | Côte d'Ivoire | Year | Source URL | Confidence |
|---|---|---|---|---|---|
| Fiscal / hidden-debt crisis | Misreported debt revealed in 2024-25; the Court of Auditors revised the end-2023 debt to ~100-111% of GDP; IMF 132% end-2024. Old programme frozen; new ECF SLA in Sept 2026 is pending Board approval. A debt "treatment" via the G20 Common Framework has domestic political opposition. Growth slows to ~2.5% in 2026 and investment is falling | n/a | 2024-26 | IMF links above; https://www.cnbcafrica.com/2026/senegal-agrees-to-restore-debt-sustainability-in-return-for-imf-programme ; https://www.riotimesonline.com/senegal-imf-debt-treatment-plan-2026/ | verified (IMF) / secondary |
| **Government arrears to firms** | The PM cited **1,956 bn FCFA** of arrears owed to companies (stock at end-March 2025; speech of 8 Sept 2026). The employers' body CNES estimates ~1,400 bn FCFA. **300 bn FCFA** to be paid by end-2026 (Finance Minister, 7 Oct 2026); a 3-year plan, while employers ask for 2. BTP (construction) is most exposed, with warnings of cascading defaults. IMF: arrears ≈4% of GDP at end-2024 | not found | 2025-26 | https://www.capmad.com/article/senegal-le-gouvernement-reconnait-1-956-milliards-fcfa-darrieres-dus-aux-entreprises-et-promet-un-apurement-prioritaire ; https://www.dakaractu.com/Apurement-de-la-dette-interieure-300-milliards-FCFA-envers-les-entreprises-d-ici-fin-2026-MEFP_a276772.html ; https://www.seneplus.com/article/dette-interieure-le-secteur-prive-senegalais-veut-un-remboursement-en-deux-ans | verified (secondary) |
| Bank / credit impact | MEFP says no significant crowding-out in 2025: private credit grew +8.4%. But the State's heavy regional borrowing (2,225 bn FCFA in 2025) is absorbing bank liquidity, with Ivorian banks among the buyers. WAEMU bank NPL gross ratio 8.5% (2024). Large-SFD NPLs rose to 6.6% and the sector made a loss (2024) | - | 2024-25 | MEFP PDF; CB key figures | verified |
| New taxes (PRES) | TTA 0.5% on mobile-money transfers (salaries exempt), plus higher excise on gambling, tobacco and alcohol | - | 2025-26 | section 6 | verified (secondary) |
| Elections / politics | Next presidential election 2029 (not researched) | **Ouattara re-elected 25 Oct 2025 with 89.77%** (turnout 50.1%); Gbagbo and Thiam excluded; validated 4 Nov 2025. Some protest deaths reported (unverified count). The IMF still projects ~6% growth for 2026; WBES shows political instability as a top-3 obstacle (19.5%) | 2025-26 | https://www.letemps.ch/monde/en-cote-d-ivoire-le-president-alassane-ouattara-est-reelu-pour-un-4e-mandat-avec-89-77-des-voix | verified (secondary) |
| Regulatory tightening | EP licensing has been mandatory since 1 Sept 2025. PI-SPI is mandatory for interoperable e-money from 2 Nov 2026, with free tiers compressing P2P fee revenue. E-money instruction revision is pending | same; plus FNE enforcement since 1 Sept 2026 | 2025-27 | sections 3d and 6 | verified |
| BCEAO dormant-account rule | Dormant-account closures pushed the WAEMU strict banking rate down (Mali -9.6 pts) | same | 2024 | BCEAO inclusion 2024 | verified |
| SME pain points | Access to finance is the #1 obstacle (45.9%); electricity 11.7%; informal competition 7.4% (WBES 2024) | Access to finance 21.6%; political instability 19.5%; crime 13.4%; corruption 12.0% | 2023-24 | WBES profiles | verified |
| Late payments, bank fees, account-opening time | **not found** (no survey located) | not found | - | - | not found |

---

## Gaps to close (priority order)
1. CNPS Côte d'Ivoire: official contributing-employer count and declared employees. Read the gov.ci article fully or the CNPS annual report. The ~49,000 employers figure is unverified.
2. CI private-sector average wage / wage bill (INS-ANStat ENE, or the CNPS contribution base) to replace the payroll range estimate.
3. Senegal DGID e-invoicing timetable; any CI mobile-money transfer tax; any electronic salary-payment obligations.
4. IFC/AfDB SME finance gap figures; WBES collateral indicators (microdata).
5. PI-SPI transaction statistics; final BCEAO EP list at 31 Aug 2026 (country counts).
6. Per-country SFD counts (BCEAO SFD statistics) and 4G population coverage (GSMA/ARTP).
7. Dakar share of Senegalese firms (ANSD RGE-2 when published).
