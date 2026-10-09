# Payment providers compared: Nilos, Cauridor, Hub2, Bizao, Thunes, Onafriq

Jokko needs two different kinds of payment partner. These six companies split between them:

1. **Local mobile money and payments hubs**: one connection to Wave, Orange Money, Free/Mixx, MTN, Moov and cards inside WAEMU, for collections, payouts to wallets and salary payments. **Hub2, Bizao**, and partly **Cauridor**.
2. **Cross-border and FX providers**: getting euros or dollars in and out of FCFA, for clients' foreign suppliers, freelancers' and exporters' income, and diaspora flows. **Nilos, Thunes, Onafriq**, and partly **Cauridor**.

Neither kind replaces the partner bank (accounts with IBAN, cards, client money) or PI-SPI, the BCEAO's instant-payment system, which becomes mandatory for transfers between providers on 2 November 2026 and is free for small transfers.

**None of the six publishes prices.** The fee ranges below come from a Dakar consultancy's comparison blogs (Kolonell), which may be promotional. Treat them as orders of magnitude and get quotes.

## Side by side

| | **Hub2** | **Bizao** | **Cauridor** | **Nilos** | **Thunes** | **Onafriq** (ex-MFS Africa) |
|---|---|---|---|---|---|---|
| What it is | Single API for mobile money, banks and cards in francophone Africa ("Stripe of francophone Africa") | Payments hub for mobile money, cards and phone credit | Cross-border B2B payment rails, plus a 25,000-agent cash network | Cross-border B2B payments and FX into and out of emerging markets | Global payout network (130+ countries) | Pan-African payments and wallet interoperability network |
| Base | Abidjan | Paris | Guinea / Delaware | France, Israel | Singapore | Mauritius, Africa |
| Countries relevant to Jokko | 12 in West and Central Africa, including Senegal, CI, Benin, Cameroon | 10–15+, including Senegal, CI, Togo, Burkina, Cameroon | Guinea, Senegal, CI, Sierra Leone, Liberia; Mali and Nigeria planned | CI, Senegal, Benin, Togo (since March 2025) | Global; Senegal and CI operators not confirmed | Wide African coverage; XOF details not public |
| Senegal operators | Wave, Orange Money, Free (third-party list) | Orange Money, Wave, MTN, Moov (third-party) | Orange, MTN partnerships | Mobile money "integrated"; operators not listed | Not confirmed | Not confirmed |
| Collect payments | Yes | Yes | Yes | Yes (multi-currency accounts) | No (payouts) | Mainly payouts |
| Pay out to wallets and banks | Yes | Yes | Yes, plus cash pick-up | Yes, instant XOF payouts | Yes | Yes (salaries, remittances, loans) |
| EUR/USD ↔ FCFA | Limited | Limited | Yes (money transfer operators, banks) | **Core product**, plus virtual EU IBANs | **Core product** | Yes, via its network and PAPSS |
| Indicative fees (unverified) | Collection 2.5–3.5%; payout 1–1.5%; settlement T+1 to T+3 | 1.5–3.5% per corridor | Not found | Not public ("FX costs up to 50% lower" claim) | Not public; transaction fee + FX margin per corridor | 2–4% on some non-XOF corridors; XOF not found |
| WAEMU licence | **BCEAO payment institution, Côte d'Ivoire (EP.CI.010/2026)**, according to a LinkedIn post, not yet checked on the BCEAO list | Not found | **BCEAO payment institution in Mali (September 2025)** | None found; Modulr e-money licence in Europe, money services business registration in Canada | None found | None found in WAEMU (licences elsewhere in Africa and the UK) |
| Crypto or stablecoins in the flows | API "covers crypto"; stablecoin remittances planned | None found | None found ("exploring blockchain" for settlement) | **Yes: "stablecoin sandwich" routing**, mixed with FX brokers | **Yes: USDC/USDT payouts and EURC funding offered**; fiat routes also available | None found |
| Funding / scale | $11.7M raised; Ecobank partnership (Feb 2026) | ~€8M Series A (2022); ~100 merchants | $3.5M seed (2025), Series A reported; $500M volume in 2024 | $5.2M seed (2022) | Large, global | $100M+ raised; large network |

## Fit for Jokko

| Need | Best candidates | Why |
|---|---|---|
| **Payouts to every wallet and bank (payroll, suppliers) before Jokko joins PI-SPI** | **Hub2**, then Bizao | Hub2 has a BCEAO licence (to verify), Senegal operators and an Ecobank partnership, and Ecobank is a candidate partner bank |
| **Collections from wallets (payment links)** | **Hub2**, Bizao | Same. Compare with PI-SPI, which is free for the receiver |
| **Clients receiving EUR/USD from abroad, converted to FCFA** | **Cauridor**, Thunes (fiat route), Nilos (only with a written no-stablecoin route) | Cauridor holds a BCEAO licence and works with Western Union, MoneyGram and Ria |
| **Paying foreign suppliers from FCFA** | Partner bank first; then Cauridor or Thunes | Outbound flows need BCEAO FX documentation, which a bank handles best |
| **Diaspora inflows (Senegal module, year 2–3)** | Cauridor, Thunes, Onafriq | Established remittance networks |

## The crypto question

You want Jokko's product to stay clear of crypto, and the BCEAO has no framework for it. The providers sort into three groups:

- **Fiat only, as far as public sources show: Cauridor, Bizao, Onafriq.** Cauridor is only "exploring" blockchain for settlement.
- **Fiat by default, with crypto available: Thunes** (stablecoin payouts are an option you don't have to use) **and Hub2** (crypto mentioned in its API and stablecoin remittances planned). Ask for a contract clause that Jokko's flows are fiat only.
- **Stablecoins in the routing itself: Nilos.** Your clients never see crypto, but some flows may pass through stablecoins and a local partner. Only use Nilos if it guarantees a fiat-only route in writing.

## Recommendation

1. **Shortlist Hub2 for local payouts and collections**, and check that its licence number EP.CI.010/2026 appears on the BCEAO list. Get a Senegal quote, and ask whether it has a Senegal licence or how it serves Senegal from Côte d'Ivoire.
2. **Keep Bizao as the second quote** for local flows. BCEAO rules ban exclusivity, so a backup is easy.
3. **For EUR/USD flows, start with Cauridor**, which is licensed in WAEMU and fiat only, and **compare with Thunes** on a fiat-only route.
4. **Nilos only if** it commits in writing to a fiat-only route for Jokko and names its licensed local payout partner.
5. **Plan to rely less on aggregators over time.** Once Jokko joins PI-SPI, transfers to other wallets and banks become cheaper or free. Aggregators then mainly serve wallets not yet on PI-SPI and cross-border flows.

## Questions to send every provider

1. Fees for payouts and collections in Senegal, by operator, with volume tiers and monthly minimums.
2. Settlement time, and whether pre-funding or a deposit is required.
3. Which Senegalese operators are supported (Wave, Orange Money, Free/Mixx, banks).
4. Their BCEAO licence number, or the licensed partner they rely on in Senegal.
5. Whether any of Jokko's flows would pass through crypto or stablecoins, and whether they will exclude it by contract.
6. FX margin on EUR/USD → XOF, and how quickly money arrives.
7. Whether they are on PI-SPI themselves.

## Sources

- Hub2: [TechCrunch](https://techcrunch.com/2024/12/02/hub2-a-stripe-for-francophone-africa-banks-8m); [Financial Afrik, Ecobank partnership](https://www.financialafrik.com/2026/02/25/ecobank-et-hub2-elargissent-lacces-aux-paiements-numeriques-a-200-millions-dutilisateurs-de-portefeuilles-mobiles-en-afrique-francophone); [Kolonell (indicative fees)](https://kolonell.com/fr/blog/hub2-agregateur-paiement-afrique-ouest-2026); [LinkedIn post on the BCEAO licence](https://ci.linkedin.com/in/camille-biraben)
- Bizao: [Logistafrica](https://logistafrica.com/en/e-commerce-en/fintech-company-bizao-raises-e8-million-to-become-a-leading-payment-hub-in-africa/); [Kolonell (indicative fees)](https://kolonell.com/en/blog/bizao-multi-country-payment-aggregator-integration-africa-2026)
- Cauridor: [TechCrunch](https://techcrunch.com/2025/01/29/cauridor-has-a-fix-for-cross-border-payments-issues-in-francophone-africa); [AllAfrica](https://fr.allafrica.com/stories/202501300148.html); [Financial Afrik, BCEAO licences September 2025](https://www.financialafrik.com/2025/09/11/inclusion-financiere-dix-nouveaux-etablissements-de-paiement-agrees-par-la-bceao/)
- Nilos: [nilos.io](https://www.nilos.io); [API docs](https://nilos.readme.io/llms.txt); [Condia](https://thecondia.com/nilos-west-africa-payments/); [Tekedia](https://www.tekedia.com/b2b-payment-platform-nilos-expands-into-west-africa-bringing-instant-payouts-and-mobile-money-integration/)
- Thunes: [stablecoin payouts](https://fintechnews.sg/120676/digitalassets/thunes-instant-stablecoin-payouts/); [EURC funding](https://www.prnewswire.com/fr/communiques-de-presse/thunes-etend-son-infrastructure-web3-avec-leurc-afin-de-permettre-un-financement-de-tresorerie-instantane-en-euros-302851004.html); [pricing model (unofficial)](https://wiki.private.law/en/thunes)
- Onafriq: [Briter](https://www.briter.co/companies/onafriq-formerly-mfs-africa); [Lendsqr directory](https://lendsqr.com/providers/onafriq); [Kolonell (corridor fees)](https://kolonell.com/en/blog/cross-border-pan-african-settlement-2026)
