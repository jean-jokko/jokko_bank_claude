"""Build the two standalone, clickable Kelen prototypes (mobile in a phone frame, web full window) as complete HTML files for static hosting."""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proto_js import JS

KIND, SRC, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
ACCENT = "#0D7377"
FR = {"home": "Accueil et onglets", "onboarding": "Ouverture de compte", "accounts": "Comptes et RIB", "topup": "Recharger", "send": "Envoyer",
      "bulk": "Paie groupée", "bills": "Factures", "team": "Équipe et validations", "soon": "Bientôt"}
HEAD = '<meta name="robots" content="noindex, nofollow">' \
       '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22%3E%3Crect width=%2232%22 height=%2232%22 rx=%228%22 fill=%22%230D7377%22/%3E%3Ccircle cx=%2216%22 cy=%2216%22 r=%225%22 fill=%22%23FFFFFF%22/%3E%3C/svg%3E">'
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' \
       '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&amp;display=swap">'

canvas = json.load(open(os.path.join(SRC, "canvas.json"), encoding="utf-8"))
by_page = {p["id"]: [] for p in canvas["pages"]}
for f in canvas["order"]:
    b = canvas["boards"][f]
    by_page[b["page"]].append((b["x"], f, b["title"]))

screens, nav = [], []
for p in canvas["pages"]:
    items = sorted(by_page[p["id"]])
    links = "".join(f'<li><a href="#{f[:-8]}" data-screen="{f[:-8]}">{html.escape(t)}</a></li>' for _, f, t in items)
    nav.append(f'<section class="flow"><h2>{html.escape(FR.get(p["id"], p["name"]))}</h2><ol>{links}</ol></section>')
    for _, f, t in items:
        src = open(os.path.join(SRC, f), encoding="utf-8").read()
        body = src.split("</helmet>", 1)[1].split("</x-dc>", 1)[0].strip()
        body = body.replace("{{accent}}", ACCENT)
        body = re.sub(r'href="([A-Za-z0-9_]+)\.dc\.html"', r'href="#\1"', body)
        assert "{{" not in body, f
        screens.append(f'<section class="screen" id="s-{f[:-8]}" data-title="{html.escape(t)}" hidden>{body}</section>')

ids = {f[:-8] for f in canvas["order"]}
missing = set(re.findall(r'href="#([A-Za-z0-9_]+)"', "".join(screens))) - ids
assert not missing, missing

MARK = f'<span class="mark"><i></i>kelen</span>'

if KIND == "mobile":
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Kelen — prototype mobile</title>
{HEAD}
{FONT}
<style>
/* A quiet viewer around one phone: screen list on the left, the phone centred and scaled to fit, a top bar with shortcuts. */
:root {{ --bg: #E9ECEF; --panel: #FFFFFF; --ink: #0F1114; --muted: #5E6470; --line: rgba(15,17,20,0.10); --accent: {ACCENT}; --frame: #0F1114;
  --font: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg: #0E1114; --panel: #171B20; --ink: #ECEFF3; --muted: #9AA3AF; --line: rgba(255,255,255,0.10); --frame: #2A3038; color-scheme: dark; }} }}
* {{ box-sizing: border-box; }}
html, body {{ height: 100%; margin: 0; }}
body {{ background: var(--bg); color: var(--ink); font-family: var(--font); font-size: 14px; overflow: hidden; -webkit-font-smoothing: antialiased; }}
[hidden] {{ display: none !important; }}
.app {{ height: 100%; display: grid; grid-template-rows: auto minmax(0, 1fr); padding: env(safe-area-inset-top, 0px) 16px env(safe-area-inset-bottom, 0px); }}
.bar {{ display: flex; align-items: center; gap: 12px; flex-wrap: wrap; padding-block: 12px; border-bottom: 1px solid var(--line); }}
.mark {{ display: inline-flex; align-items: center; gap: 6px; font-weight: 700; font-size: 18px; letter-spacing: -0.2px; }}
.mark i {{ width: 9px; height: 9px; border-radius: 5px; background: var(--accent); }}
.tag {{ font-size: 11px; font-weight: 500; letter-spacing: 1.6px; text-transform: uppercase; color: var(--muted); }}
.where {{ flex: 1 1 auto; min-width: 0; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
.btn {{ font: inherit; font-size: 13px; font-weight: 600; color: var(--ink); background: var(--panel); border: 1px solid var(--line);
  height: 36px; padding: 0 14px; border-radius: 18px; display: inline-flex; align-items: center; text-decoration: none; cursor: pointer; }}
.btn.primary {{ background: var(--accent); color: #FFFFFF; border-color: var(--accent); }}
.btn:focus-visible, .flow a:focus-visible {{ outline: 3px solid var(--accent); outline-offset: 2px; }}
.body {{ display: grid; grid-template-columns: 280px minmax(0, 1fr); gap: 16px; min-height: 0; position: relative; }}
.list {{ overflow-y: auto; padding-block: 16px; display: flex; flex-direction: column; gap: 18px; min-height: 0; }}
.list p {{ margin: 0; color: var(--muted); line-height: 1.5; max-width: 32ch; }}
.flow h2 {{ margin: 0 0 6px; font-size: 11px; font-weight: 500; letter-spacing: 1.6px; text-transform: uppercase; color: var(--muted); }}
.flow ol {{ list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 2px; }}
.flow a {{ display: block; padding: 7px 10px; border-radius: 10px; color: var(--ink); text-decoration: none; font-weight: 500; }}
.flow a:hover {{ background: var(--panel); }}
.flow a[aria-current="page"] {{ background: var(--accent); color: #FFFFFF; font-weight: 600; }}
.stage {{ position: relative; min-height: 0; display: flex; align-items: center; justify-content: center; padding-block: 16px; }}
.phone {{ position: relative; flex: none; border-radius: calc(54px * var(--s, 1)); box-shadow: 0 0 0 calc(10px * var(--s, 1)) var(--frame), 0 30px 60px rgba(0,0,0,0.18); overflow: hidden; background: #F2F3F5; }}
.phone-inner {{ width: 390px; height: 844px; transform: scale(var(--s, 1)); transform-origin: top left; color: #0F1114; }}
.phone a {{ color: #0F1114; }}
.phone a:hover {{ color: {ACCENT}; }}
.phone .scroll {{ scrollbar-width: none; }}
.phone .scroll::-webkit-scrollbar {{ display: none; }}
.phone input::placeholder {{ color: #7A808C; }}
.toggle {{ display: none; }}
.toast {{ position: absolute; left: 50%; bottom: calc(118px * var(--s, 1)); transform: translateX(-50%); z-index: 5; max-width: 88%; width: max-content;
  background: #0F1114; color: #FFFFFF; font-size: 13px; font-weight: 500; line-height: 1.35; padding: 10px 14px; border-radius: 14px; box-shadow: 0 10px 24px rgba(15,17,20,0.25); text-align: center; }}
@media (max-width: 900px) {{
  .body {{ grid-template-columns: minmax(0, 1fr); }}
  .list {{ position: absolute; inset: 0; z-index: 5; background: var(--bg); padding-inline: 4px; }}
  .toggle {{ display: inline-flex; }}
  .hide-narrow {{ display: none; }}
}}
@media (max-width: 520px) {{
  .phone {{ box-shadow: 0 10px 30px rgba(0,0,0,0.16); border-radius: calc(36px * var(--s, 1)); }}
  .stage {{ padding-block: 10px; }}
  .tag {{ display: none; }}
}}
@media (prefers-reduced-motion: no-preference) {{
  .screen:not([hidden]) {{ animation: in 160ms ease-out; }}
  @keyframes in {{ from {{ opacity: 0.4; }} to {{ opacity: 1; }} }}
}}
</style>
</head>
<body>
<div class="app">
  <header class="bar">
    {MARK}
    <span class="tag">Prototype mobile</span>
    <span class="where" id="where" aria-live="polite">Accueil</span>
    <a class="btn primary" href="#Main">Accueil</a>
    <a class="btn hide-narrow" href="#Welcome">Ouverture de compte</a>
    <button class="btn toggle" id="toggle" type="button" aria-expanded="false" aria-controls="list">Écrans</button>
  </header>
  <div class="body">
    <nav class="list" id="list" aria-label="Tous les écrans">
      <p>Touchez les boutons dans le téléphone pour naviguer, ou choisissez un écran ici. Les montants, noms et entreprises sont des exemples.</p>
      {"".join(nav)}
    </nav>
    <main class="stage" id="stage">
      <div class="phone" id="phone"><div class="phone-inner">
        {"".join(screens)}
      </div></div>
    </main>
  </div>
</div>
<script>
(function () {{
  var phone = document.getElementById('phone'), stage = document.getElementById('stage');
  var list = document.getElementById('list'), toggle = document.getElementById('toggle'), where = document.getElementById('where');
  var current = null;
  function fit() {{
    var w = stage.clientWidth, h = stage.clientHeight - 32;
    var pad = window.innerWidth <= 520 ? 4 : 28;
    var s = Math.max(Math.min((w - pad) / 390, (h - pad) / 844, 1), 0.3);
    phone.style.setProperty('--s', s.toFixed(4));
    phone.style.width = (390 * s) + 'px';
    phone.style.height = (844 * s) + 'px';
  }}
  function setList(open) {{
    if (window.innerWidth > 900) {{ list.hidden = false; toggle.setAttribute('aria-expanded', 'false'); return; }}
    list.hidden = !open;
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    toggle.textContent = open ? 'Fermer' : 'Écrans';
  }}
  function show(id) {{
    var el = document.getElementById('s-' + id) || document.getElementById('s-Main');
    if (current && current !== el) current.hidden = true;
    el.hidden = false; current = el;
    var sc = el.querySelector('.scroll'); if (sc) sc.scrollTop = 0;
    where.textContent = el.getAttribute('data-title');
    document.querySelectorAll('.flow a').forEach(function (a) {{
      if (a.getAttribute('data-screen') === el.id.slice(2)) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    }});
    setList(false);
  }}
  toggle.addEventListener('click', function () {{ setList(list.hidden); }});
  window.addEventListener('hashchange', function () {{ show(location.hash.slice(1)); }});
  window.addEventListener('resize', function () {{ fit(); setList(false); }});
  fit(); show(location.hash.slice(1) || 'Main');
}})();
</script>
<script>{JS}</script>
</body>
</html>
"""
else:
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Kelen — prototype web</title>
{HEAD}
{FONT}
<style>
/* Each screen fills the window like the real web app; a small "Écrans" button opens the list of all screens by flow. */
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; }}
body {{ background: #F2F3F5; color: #0F1114; font-family: 'Geist', system-ui, -apple-system, 'Segoe UI', sans-serif; -webkit-font-smoothing: antialiased; }}
[hidden] {{ display: none !important; }}
a {{ color: #0F1114; }} a:hover {{ color: {ACCENT}; }}
input::placeholder {{ color: #7A808C; }}
.fab {{ position: fixed; right: 18px; bottom: calc(18px + env(safe-area-inset-bottom, 0px)); z-index: 50; font: inherit; font-size: 13px; font-weight: 600;
  height: 40px; padding: 0 16px; border-radius: 20px; border: 1px solid rgba(15,17,20,0.12); background: #0F1114; color: #FFFFFF; cursor: pointer;
  display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 10px 30px rgba(15,17,20,0.25); }}
.fab i {{ width: 8px; height: 8px; border-radius: 4px; background: {ACCENT}; }}
.fab:focus-visible, .drawer a:focus-visible, .drawer button:focus-visible {{ outline: 3px solid {ACCENT}; outline-offset: 2px; }}
.scrim {{ position: fixed; inset: 0; background: rgba(15,17,20,0.35); z-index: 60; }}
.drawer {{ position: fixed; top: 0; right: 0; bottom: 0; width: min(340px, 100%); z-index: 70; background: #FFFFFF; color: #0F1114;
  box-shadow: -20px 0 40px rgba(15,17,20,0.18); display: flex; flex-direction: column; padding: calc(18px + env(safe-area-inset-top, 0px)) 18px calc(18px + env(safe-area-inset-bottom, 0px)); gap: 14px; }}
.drawer header {{ display: flex; align-items: center; justify-content: space-between; gap: 10px; }}
.mark {{ display: inline-flex; align-items: center; gap: 6px; font-weight: 700; font-size: 18px; letter-spacing: -0.2px; }}
.mark i {{ width: 9px; height: 9px; border-radius: 5px; background: {ACCENT}; }}
.tag {{ font-size: 11px; font-weight: 500; letter-spacing: 1.6px; text-transform: uppercase; color: #5E6470; }}
.close {{ font: inherit; width: 36px; height: 36px; border-radius: 18px; border: 1px solid rgba(15,17,20,0.12); background: #FFFFFF; cursor: pointer; font-size: 18px; line-height: 1; }}
.drawer p {{ margin: 0; color: #5E6470; font-size: 13px; line-height: 1.5; }}
.lists {{ overflow-y: auto; display: flex; flex-direction: column; gap: 16px; min-height: 0; }}
.flow h2 {{ margin: 0 0 6px; font-size: 11px; font-weight: 500; letter-spacing: 1.6px; text-transform: uppercase; color: #5E6470; }}
.flow ol {{ list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 2px; }}
.flow a {{ display: block; padding: 7px 10px; border-radius: 10px; color: #0F1114; text-decoration: none; font-size: 14px; font-weight: 500; }}
.flow a:hover {{ background: #F2F3F5; color: #0F1114; }}
.flow a[aria-current="page"] {{ background: {ACCENT}; color: #FFFFFF; font-weight: 600; }}
.toast {{ position: fixed; left: 50%; bottom: calc(24px + env(safe-area-inset-bottom, 0px)); transform: translateX(-50%); z-index: 80; max-width: calc(100% - 32px); width: max-content;
  background: #0F1114; color: #FFFFFF; font-size: 14px; font-weight: 500; line-height: 1.35; padding: 12px 16px; border-radius: 14px; box-shadow: 0 10px 24px rgba(15,17,20,0.25); text-align: center; }}
</style>
</head>
<body>
<main id="screens">
{"".join(screens)}
</main>
<button class="fab" id="fab" type="button" aria-expanded="false" aria-controls="drawer"><i></i>Écrans</button>
<div class="scrim" id="scrim" hidden></div>
<nav class="drawer" id="drawer" aria-label="Tous les écrans" hidden>
  <header>{MARK}<span class="tag">Prototype web</span><button class="close" id="close" type="button" aria-label="Fermer la liste">×</button></header>
  <p>Cliquez dans l'application pour naviguer, ou choisissez un écran ici. Les montants, noms et entreprises sont des exemples.</p>
  <div class="lists">{"".join(nav)}</div>
</nav>
<script>
(function () {{
  var fab = document.getElementById('fab'), drawer = document.getElementById('drawer'), scrim = document.getElementById('scrim'), closeBtn = document.getElementById('close');
  var current = null;
  function setDrawer(open) {{
    drawer.hidden = !open; scrim.hidden = !open;
    fab.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) {{ var a = drawer.querySelector('[aria-current="page"]') || drawer.querySelector('a'); if (a) a.focus(); }}
  }}
  function show(id) {{
    var el = document.getElementById('s-' + id) || document.getElementById('s-Main');
    if (current && current !== el) current.hidden = true;
    el.hidden = false; current = el;
    document.title = el.getAttribute('data-title') + ' — Kelen';
    window.scrollTo(0, 0);
    document.querySelectorAll('.flow a').forEach(function (a) {{
      if (a.getAttribute('data-screen') === el.id.slice(2)) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    }});
    setDrawer(false);
  }}
  fab.addEventListener('click', function () {{ setDrawer(drawer.hidden); }});
  closeBtn.addEventListener('click', function () {{ setDrawer(false); fab.focus(); }});
  scrim.addEventListener('click', function () {{ setDrawer(false); }});
  document.addEventListener('keydown', function (e) {{ if (e.key === 'Escape' && !drawer.hidden) {{ setDrawer(false); fab.focus(); }} }});
  window.addEventListener('hashchange', function () {{ show(location.hash.slice(1)); }});
  show(location.hash.slice(1) || 'Main');
}})();
</script>
<script>{JS}</script>
</body>
</html>
"""

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(doc)
print(KIND, len(screens), "screens,", round(len(doc) / 1024), "KB")
