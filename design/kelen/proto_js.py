"""Shared behaviour for both Kelen prototypes: selectable chips and switches, the send-amount keypad, and short notices for actions a prototype cannot perform."""
JS = r"""
(function () {
  var host = document.getElementById('phone') || document.body;
  var toast = document.createElement('div');
  toast.className = 'toast'; toast.setAttribute('role', 'status'); toast.setAttribute('aria-live', 'polite'); toast.hidden = true;
  host.appendChild(toast);
  var timer = null;
  function say(msg) {
    toast.textContent = msg; toast.hidden = false;
    clearTimeout(timer); timer = setTimeout(function () { toast.hidden = true; }, 2200);
  }

  /* Chips, option cards and switches: swap the look of the chosen option with the previously chosen one. */
  function tag(e) { return e.tagName.toLowerCase(); }
  function kids(e) { return tag(e) === 'svg' ? [] : [].slice.call(e.children); }
  function onlySvg(e) { return e.children.length > 0 && [].every.call(e.children, function (x) { return tag(x) === 'svg'; }); }
  function setStyle(e, s) { if (s === null) e.removeAttribute('style'); else e.setAttribute('style', s); }
  function swapPair(a, b) {
    var sa = a.getAttribute('style'); setStyle(a, b.getAttribute('style')); setStyle(b, sa);
    if (tag(a) === 'svg' || tag(b) === 'svg') return;
    var ca = kids(a), cb = kids(b);
    if ((!ca.length && onlySvg(b)) || (!cb.length && onlySvg(a))) { var h = a.innerHTML; a.innerHTML = b.innerHTML; b.innerHTML = h; return; }
    for (var i = 0; i < Math.min(ca.length, cb.length); i++) swapPair(ca[i], cb[i]);
  }
  function copyPair(src, dst) {
    setStyle(dst, src.getAttribute('style'));
    if (tag(src) === 'svg' || tag(dst) === 'svg') return;
    var cs = kids(src), cd = kids(dst);
    if (!cd.length && onlySvg(src)) { dst.innerHTML = src.innerHTML; return; }
    if (!cs.length && onlySvg(dst)) { dst.innerHTML = ''; return; }
    for (var i = 0; i < Math.min(cs.length, cd.length); i++) copyPair(cs[i], cd[i]);
  }
  var SKIN = /^\s*(background|color|border|box-shadow|opacity|left|right)\s*:/;
  function shape(e) {
    var s = (e.getAttribute('style') || '').split(';').filter(function (p) { return p.trim() && !SKIN.test(p); }).join(';');
    var inner = onlySvg(e) ? '' : kids(e).map(shape).join(',');
    return tag(e) + '{' + s + '}(' + inner + ')';
  }
  function template(btn, state) {
    var want = shape(btn), all = document.querySelectorAll('section.screen button[aria-pressed="' + state + '"]');
    for (var i = 0; i < all.length; i++) if (all[i] !== btn && shape(all[i]) === want) return all[i];
    return null;
  }
  function choose(btn) {
    var group = [].filter.call(btn.parentElement.children, function (c) { return c.matches('button[aria-pressed]'); });
    var on = group.filter(function (c) { return c.getAttribute('aria-pressed') === 'true'; });
    if (group.length > 1 && on.length <= 1) {
      if (btn.getAttribute('aria-pressed') === 'true') return;
      if (on.length) {
        swapPair(on[0], btn); on[0].setAttribute('aria-pressed', 'false'); btn.setAttribute('aria-pressed', 'true');
        echo(btn.closest('section'), btn.parentElement, firstText(on[0]), firstText(btn)); loan(); return;
      }
    }
    var next = btn.getAttribute('aria-pressed') === 'true' ? 'false' : 'true', t = template(btn, next);
    if (t) { copyPair(t, btn); btn.setAttribute('aria-pressed', next); }
  }

  /* A choice that is repeated elsewhere on the screen (the plan on its button, the top-up amount, the loan simulator) follows it. */
  function leaves(root, skip) {
    return [].filter.call(root.querySelectorAll('*'), function (x) { return !x.children.length && !(skip && skip.contains(x)) && x.textContent.trim(); });
  }
  function firstText(btn) { var l = leaves(btn)[0]; return (l || btn).textContent.trim(); }
  var NUM = /^\d{1,3}( \d{3})+$/;
  function echo(sec, grp, from, to) {
    var nums = NUM.test(from) && NUM.test(to);
    leaves(sec, grp).forEach(function (x) {
      var t = x.textContent.trim();
      if (nums && t === from) x.textContent = to;
      else if (t.indexOf("l'offre " + from) >= 0) x.textContent = t.split("l'offre " + from).join("l'offre " + to);
    });
    if (nums) sec.querySelectorAll('input[data-amount]').forEach(function (i) { i.value = to; });
  }
  var loanSec = document.getElementById('s-LoanOffer'), loanMarks = [];
  if (loanSec) leaves(loanSec).forEach(function (x) {
    var k = { '356 048 FCFA': 'm', '136 288 FCFA': 'c', '2 136 288 FCFA': 'T' }[x.textContent.trim()]; if (k) loanMarks.push([x, k]);
  });
  function loan() {
    if (!loanSec) return;
    var P = 0, n = 0, inp = loanSec.querySelector('input[data-amount]');
    loanSec.querySelectorAll('button[aria-pressed="true"]').forEach(function (b) {
      var t = b.textContent.trim();
      if (/mois$/.test(t)) n = parseInt(t, 10); else if (NUM.test(t)) P = +t.replace(/\D/g, '');
    });
    if (inp) P = +inp.value.replace(/\D/g, '');
    if (!P || !n) return;
    var r = 0.23 / 12, m = Math.round(P * r / (1 - Math.pow(1 + r, -n)));
    loanMarks.forEach(function (x) { x[0].textContent = fmt(x[1] === 'm' ? m : x[1] === 'c' ? m * n - P : m * n) + ' FCFA'; });
  }

  /* Send flow: the keypad (phone) or amount field (web) drives the amount, the 0.5 % transfer tax and the total on the next screens. */
  var amt = 1250000, fresh = true, marks = [], prev = '';
  var KEYS = { '1 250 000': 'a', '1 250 000 FCFA': 'aF', '6 250 FCFA': 'tF', '1 256 250 FCFA': 'TF' };
  ['SendAmount', 'SendReview', 'SendSuccess'].forEach(function (id) {
    var s = document.getElementById('s-' + id); if (!s) return;
    s.querySelectorAll('*').forEach(function (el) {
      if (el.children.length || el.closest('svg')) return;
      var k = KEYS[el.textContent.trim()]; if (k) marks.push([el, k]);
    });
  });
  var field = document.querySelector('#s-SendAmount input[inputmode="numeric"]');
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, ' '); }
  function render() {
    var tax = Math.round(amt * 0.005);
    marks.forEach(function (m) {
      m[0].textContent = m[1] === 'a' ? fmt(amt) : m[1] === 'aF' ? fmt(amt) + ' FCFA' : m[1] === 'tF' ? fmt(tax) + ' FCFA' : fmt(amt + tax) + ' FCFA';
    });
    if (field && document.activeElement !== field) field.value = fmt(amt);
  }
  function key(k) {
    var d = fresh ? '' : String(amt); fresh = false;
    if (k === 'del') d = String(amt).slice(0, -1); else d = (d + k).replace(/^0+/, '');
    if (d.length > 10) return;
    amt = +d || 0; render();
  }
  document.querySelectorAll('section.screen input[inputmode="numeric"]').forEach(function (i) {
    if (i === field || !NUM.test(i.value)) return;
    i.setAttribute('data-amount', '');
    i.addEventListener('input', function () { var d = i.value.replace(/\D/g, '').slice(0, 12); i.value = d ? fmt(+d) : ''; loan(); });
  });
  if (field) {
    field.addEventListener('input', function () {
      amt = +field.value.replace(/\D/g, '').slice(0, 10) || 0;
      field.value = amt ? fmt(amt) : ''; render();
    });
    field.addEventListener('blur', render);
  }
  function onScreen() {
    var id = location.hash.slice(1) || 'Main';
    if (id === 'SendAmount' && prev !== 'SendReview') fresh = true;
    prev = id; toast.hidden = true;
  }
  window.addEventListener('hashchange', onScreen); onScreen();

  /* Everything else a prototype cannot really do gets a short, honest notice. */
  function notice(btn) {
    var label = (btn.getAttribute('aria-label') || btn.textContent).trim();
    var m = /^Copier (?:l'|le |la )(.+)$/.exec(label);
    if (m) return say(m[1].charAt(0).toUpperCase() + m[1].slice(1) + ' copié');
    if (/Me prévenir/.test(label)) { if (!btn.children.length) btn.textContent = 'Vous serez prévenu'; return say("C'est noté : nous vous préviendrons au lancement"); }
    if (label === 'Geler' || label === 'Dégeler') {
      var leaf = [].filter.call(btn.querySelectorAll('*'), function (x) { return !x.children.length && x.textContent.trim() === label; })[0] || (btn.children.length ? null : btn);
      if (leaf) leaf.textContent = label === 'Geler' ? 'Dégeler' : 'Geler';
      return say(label === 'Geler' ? 'Carte gelée' : 'Carte dégelée');
    }
    if (label === 'Tout marquer comme lu') return say('Toutes les notifications sont lues');
    if (/Télécharger|PDF|Exporter|Générer/.test(label)) return say('Téléchargement simulé dans le prototype');
    if (/Partager/.test(label)) return say('Partage simulé dans le prototype');
    if (label === 'Refuser') return say('Refus simulé dans le prototype');
    say("Cette action n'est pas simulée dans le prototype");
  }
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('section.screen button'); if (!btn || btn.closest('a')) return;
    e.preventDefault();
    if (btn.hasAttribute('aria-pressed')) return choose(btn);
    if (btn.closest('#s-SendAmount')) {
      var t = (btn.getAttribute('aria-label') || btn.textContent).trim();
      if (t === 'Effacer') return key('del');
      if (/^(\d|000)$/.test(t)) return key(t);
    }
    notice(btn);
  });
  document.addEventListener('submit', function (e) { e.preventDefault(); });
})();
"""
