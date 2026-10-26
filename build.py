#!/usr/bin/env python3
"""Builds the Life in the UK Test Prep website into docs/ (served by GitHub Pages).

    python3 build.py

Each page shares one head (SEO tags, structured data), header and footer. Page bodies live in
pages/*.html; the practice questions page and the FAQ are generated from data below.
"""
from __future__ import annotations

import datetime as dt
import html
import json
import re
import shutil
from pathlib import Path

import seo_pages

ROOT = Path(__file__).parent
PAGES = ROOT / "pages"
OUT = ROOT / "docs"
SITE = "https://lifeintheuktestcoach.co.uk"
DOMAIN = "lifeintheuktestcoach.co.uk"
PLAY = "https://play.google.com/store/apps/details?id=com.myday.litu"
APP = "Life in the UK Test Prep"
EMAIL = "yasantha.hettiarachchi@gmail.com"
TODAY = dt.date.today().isoformat()
ORG = {
    "@type": "Organization",
    "@id": f"{SITE}/#org",
    "name": "Yasantha Hettiarachchi IT Consultancy Service",
    "url": "https://yasantha.github.io/",
    "email": EMAIL,
    "address": {"@type": "PostalAddress", "addressLocality": "Kiribathgoda", "addressCountry": "LK"},
}
NAV = [("/#features", "Features"), ("/demo/", "Demo"), ("/practice-questions/", "Practice questions"),
       ("/study-guide/", "Study guide"), ("/faq/", "FAQ")]
esc = html.escape


def head(title: str, desc: str, path: str, ld: list[dict], og_type: str = "website", robots: str = "index,follow") -> str:
    url = SITE + path
    graph = json.dumps({"@context": "https://schema.org", "@graph": ld}, ensure_ascii=False, indent=1)
    return f"""<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#0F6E6E">
  <link rel="icon" href="/assets/img/app-icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="preload" href="/assets/fonts/plus-jakarta-sans.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/site.css?v={TODAY}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="{APP}">
  <meta property="og:locale" content="en_GB">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/img/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{APP} logo with the words 770+ practice questions and mock tests">
  <meta name="twitter:card" content="summary_large_image">
  <script type="application/ld+json">
{graph}
  </script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(active: str) -> str:
    def links(full: bool) -> str:
        out = []
        for href, label in NAV:
            label = "Interactive demo" if full and label == "Demo" else label
            cur = ' aria-current="page"' if href == active else ""
            out.append(f'<a href="{href}"{cur}>{label}</a>')
        return "\n        ".join(out)
    return f"""<header class="site-head">
  <div class="wrap">
    <a class="brand" href="/"><img src="/assets/img/app-icon.svg" alt="" width="38" height="38">{APP}</a>
    <nav class="menu" aria-label="Main">
        {links(False)}
    </nav>
    <details class="more">
      <summary>Menu</summary>
      <nav aria-label="Main menu">
        {links(True)}
      </nav>
    </details>
    <a class="get" href="{PLAY}">Get the app</a>
  </div>
</header>
"""


FOOTER = f"""<footer class="site-foot">
  <div class="wrap">
    <div>
      <h2>{APP}</h2>
      <p>Practice questions, mock tests and study notes for the Life in the UK Test.</p>
      <p style="margin-top:8px"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p style="margin-top:14px"><a href="{PLAY}">Get it on Google Play</a></p>
    </div>
    <div>
      <h2>Study</h2>
      <ul>
        <li><a href="/demo/">Interactive demo</a></li>
        <li><a href="/practice-questions/">Free practice questions</a></li>
        <li><a href="/study-guide/">Study guide</a></li>
        <li><a href="/life-in-the-uk-test-guides/">Chapter guides</a></li>
        <li><a href="/life-in-the-uk-test-pass-mark/">Pass mark and format</a></li>
        <li><a href="/faq/">FAQ</a></li>
      </ul>
    </div>
    <div>
      <h2>Legal</h2>
      <ul>
        <li><a href="/privacy-policy.html">Privacy policy</a></li>
        <li><a href="/terms.html">Terms of use</a></li>
        <li><a href="/delete-account.html">Delete your data</a></li>
        <li><a href="https://yasantha.github.io/">About the developer</a></li>
      </ul>
    </div>
    <div class="disclaimer">
      <p>Independent study app. Not affiliated with, endorsed by or connected to the Home Office or the UK Government.</p>
      <p>© {dt.date.today().year} Yasantha Hettiarachchi IT Consultancy Service · Reg. no. WP/GAM/KE/2024/00007 · Kiribathgoda, Sri Lanka. Google Play and the Google Play logo are trademarks of Google LLC.</p>
    </div>
  </div>
</footer>
</body>
</html>
"""


def crumbs(path: str, name: str) -> tuple[str, dict]:
    markup = f"""<nav class="crumbs wrap" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">{esc(name)}</li></ol></nav>"""
    ld = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": SITE + path}]}
    return markup, ld


def webpage(path: str, title: str, desc: str) -> dict:
    return {"@type": "WebPage", "@id": SITE + path, "url": SITE + path, "name": title, "description": desc,
            "inLanguage": "en-GB", "isPartOf": {"@id": f"{SITE}/#site"}}


SITE_LD = {"@type": "WebSite", "@id": f"{SITE}/#site", "name": APP, "url": SITE + "/", "inLanguage": "en-GB",
           "publisher": {"@id": f"{SITE}/#org"}}
APP_LD = {
    "@type": "MobileApplication", "@id": f"{SITE}/#app", "name": APP, "operatingSystem": "Android",
    "applicationCategory": "EducationalApplication",
    "description": "Study app for the Life in the UK Test with 770+ practice questions, timed mock tests, study notes and a daily study plan.",
    "url": SITE + "/", "downloadUrl": PLAY, "installUrl": PLAY, "inLanguage": "en-GB",
    "image": f"{SITE}/assets/img/og-image.png", "screenshot": f"{SITE}/assets/img/screen-home.webp",
    "offers": {"@type": "Offer", "price": "0", "priceCurrency": "GBP"}, "publisher": {"@id": f"{SITE}/#org"},
}

# ---------------------------------------------------------------- FAQ
FAQ = [
    ("Is this the official Life in the UK Test app?",
     "No. Life in the UK Test Prep is an independent study app. It is not affiliated with, endorsed by or connected to the Home Office or the UK Government. Its questions are written to help you study the official handbook and are not the questions used in the real test."),
    ("How many questions are in the Life in the UK Test?",
     "The test has 24 multiple-choice questions. You have 45 minutes to answer them and you need at least 18 correct answers, which is 75%, to pass. Every mock test in the app uses the same format."),
    ("What is the Life in the UK Test based on?",
     "The questions come from the official handbook, <i>Life in the United Kingdom: A Guide for New Residents</i> (3rd edition). It covers British values, the countries of the UK, history, modern society, government and the law. Our <a href=\"/study-guide/\">study guide</a> explains each chapter."),
    ("How many practice questions does the app have?",
     "Over 770 practice questions on the chapters used in the test, plus short study notes for every section of the handbook. You can try <a href=\"/practice-questions/\">20 free sample questions</a> on this website."),
    ("Does the app work without the internet?",
     "Yes. All questions, notes and mock tests are stored on your phone, so you can study offline. You only need a connection for optional backup, subscriptions and ads."),
    ("Do I need to create an account?",
     "No. Your progress stays on your phone. You can sign in with Google if you want to back up your progress and restore it on another phone."),
    ("What is free and what is in Pro?",
     "The free version includes a sample quiz, review of the questions you got wrong, your readiness score and your first full mock test. Pro adds practice by chapter and section, mixed and timed practice, study notes, unlimited mock tests and no ads."),
    ("How much does Pro cost and how do I cancel?",
     "Pro is a monthly or 3-month subscription through Google Play. The price for your country is shown in the app before you buy. You can cancel at any time in the Google Play Store under Payments &amp; subscriptions, then Subscriptions."),
    ("How is the readiness score worked out?",
     "It combines your recent mock test results with how many questions you have mastered. Aim to keep it above the 75% pass mark before your test."),
    ("Is there an iPhone version?",
     "Not yet. The app is available for Android phones on Google Play."),
    ("I think a question is wrong. What should I do?",
     f"Tap <b>Report</b> under the question in the app, or email <a href=\"mailto:{EMAIL}\">{EMAIL}</a>. We check every report and correct the question."),
    ("How do I delete my data?",
     "Open the app and go to Settings, then Delete my data. If you no longer have the app, follow the steps on our <a href=\"/delete-account.html\">delete your data</a> page."),
    ("Who makes Life in the UK Test Prep?",
     f"The app is developed by Yasantha Hettiarachchi IT Consultancy Service, a registered business in Sri Lanka. You can contact us at <a href=\"mailto:{EMAIL}\">{EMAIL}</a>."),
]
strip_tags = lambda s: re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")


def faq_page() -> tuple[str, list]:
    items = "\n".join(f"<details><summary>{esc(q)}</summary><div><p>{a}</p></div></details>" for q, a in FAQ)
    body = f"""<div class="wrap page-head"><p class="eyebrow">FAQ</p><h1>Life in the UK Test Prep: frequently asked questions</h1>
<p class="lead">Answers about the Life in the UK Test and about the app. Can't find what you need? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div>
<section style="padding-top:24px"><div class="wrap"><div class="faq">{items}</div></div></section>
{CTA}"""
    ld = {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in FAQ]}
    return body, [ld]


CTA = f"""<section class="band"><div class="wrap final">
  <h2>Practise with 770+ questions</h2>
  <p>Download {APP} free from Google Play and take your first mock test in the next ten minutes.</p>
  <a class="badge-link" href="{PLAY}"><img src="/assets/img/google-play-badge.png" alt="Get it on Google Play" width="212" height="82" loading="lazy"></a>
</div></section>"""

# ---------------------------------------------------------------- practice questions
CH_NAMES = {2: "What is the UK?", 3: "A long and illustrious history", 4: "A modern, thriving society",
            5: "The UK government, the law and your role"}


def questions_page() -> tuple[str, list]:
    qs = json.loads((PAGES / "practice-questions.json").read_text())
    letters = "ABCD"
    cards = []
    ld_q = []
    for i, q in enumerate(qs):
        opts = q["opts"][i % len(q["opts"]):] + q["opts"][: i % len(q["opts"])]  # vary where the answer sits
        right = next(k for k, o in enumerate(opts) if o["ok"])
        lis = "".join(f'<li><span class="l">{letters[k]}</span>{esc(o["t"])}</li>' for k, o in enumerate(opts))
        cards.append(f"""<li class="q" id="q{i + 1}">
  <p class="q-meta">Question {i + 1} · Chapter {q["ch"]}: {esc(q["section"])}</p>
  <h2 class="qh">{esc(q["stem"])}</h2>
  <ol class="opts">{lis}</ol>
  <details><summary>Show answer</summary><div><p><b>{letters[right]}: {esc(opts[right]["t"])}</b></p><p>{esc(q["exp"])}</p></div></details>
</li>""")
        ld_q.append({"@type": "Question", "name": q["stem"], "eduQuestionType": "Multiple choice",
                     "acceptedAnswer": {"@type": "Answer", "text": opts[right]["t"]},
                     "suggestedAnswer": [{"@type": "Answer", "text": o["t"]} for o in opts if not o["ok"]]})
    body = f"""<div class="wrap page-head"><p class="eyebrow">Free practice</p><h1>Life in the UK Test practice questions</h1>
<p class="lead">20 free sample questions covering every chapter used in the test. Pick your answer, then open "Show answer" to check it and read why. The app has over 770 more, with timed mock tests.</p></div>
<section style="padding-top:24px"><div class="wrap">
<ol class="qlist">{''.join(cards)}</ol>
<div class="teaser" style="margin-top:40px"><div><h2>How did you do?</h2><p>The real test has 24 questions and you need 18 right. Practise with 770+ questions and full 45-minute mock tests in the app, or try the interactive demo first.</p></div>
<div class="cta-row"><a class="btn" href="/demo/">Try the demo →</a></div></div>
</div></section>
{CTA}"""
    ld = {"@type": "Quiz", "name": "Life in the UK Test practice questions", "about": "Life in the UK Test",
          "educationalLevel": "Adult", "inLanguage": "en-GB", "hasPart": ld_q}
    return body, [ld]



# ---------------------------------------------------------------- guide pages (seo_pages.py)
def related_block(current: str) -> str:
    items = [(f"/{c['slug']}/", f"Chapter {c['n']}: {c['name']}") for c in seo_pages.CHAPTERS]
    items += [(f"/{t['slug']}/", t["crumb"]) for t in seo_pages.TOPICS]
    lis = "".join(f'<li><a href="{u}">{esc(n)}</a></li>' for u, n in items if u != current)
    return f'<div class="callout"><p><b>More Life in the UK Test guides</b></p><ul class="related">{lis}</ul></div>'


def article_ld(path: str, headline: str, desc: str) -> dict:
    return {"@type": "Article", "headline": headline, "description": desc, "inLanguage": "en-GB",
            "author": {"@id": f"{SITE}/#org"}, "publisher": {"@id": f"{SITE}/#org"}, "dateModified": TODAY,
            "mainEntityOfPage": SITE + path, "image": f"{SITE}/assets/img/og-image.png"}


def faq_ld(pairs: list[tuple[str, str]]) -> dict:
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}


def guide_body(h1: str, lead: str, eyebrow: str, body: str, faq: list, path: str, extra: str = "") -> str:
    items = "\n".join(f"<details><summary>{esc(q)}</summary><div><p>{a}</p></div></details>" for q, a in faq)
    return f"""<div class="wrap page-head"><p class="eyebrow">{esc(eyebrow)}</p><h1>{esc(h1)}</h1>
<p class="lead">{esc(lead)}</p></div>
<section style="padding-top:24px"><div class="wrap"><article class="prose">
{body}
{extra}
<h2>Quick questions</h2>
<div class="faq">{items}</div>
{related_block(path)}
</article></div></section>
{CTA}"""


def chapter_questions(n: int) -> str:
    qs = [q for q in json.loads((PAGES / "practice-questions.json").read_text()) if q["ch"] == n]
    if not qs:
        return ""
    cards = []
    for q in qs:
        right = next(o for o in q["opts"] if o["ok"])
        opts = "".join(f'<li>{esc(o["t"])}</li>' for o in q["opts"])
        cards.append(f'<li class="q"><h3 class="qh">{esc(q["stem"])}</h3><ul class="plainopts">{opts}</ul>'
                     f'<details><summary>Show answer</summary><div><p><b>{esc(right["t"])}</b></p><p>{esc(q["exp"])}</p></div></details></li>')
    return f'<h2>Practice questions from this chapter</h2><ol class="qlist">{"".join(cards)}</ol><p>The app has many more for every chapter. Try the <a href="/practice-questions/">20 free questions</a> too.</p>'

# ---------------------------------------------------------------- page list
def page_body(name: str) -> str:
    return (PAGES / f"{name}.html").read_text()


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT)
    sitemap = []

    def write(path: str, title: str, desc: str, active: str, body: str, ld: list, crumb: str | None = None,
              robots: str = "index,follow", in_sitemap: bool = True, priority: str = "0.8") -> None:
        extra = [SITE_LD, ORG, webpage(path, title, desc)] + ld
        top = ""
        if crumb:
            top, bc = crumbs(path, crumb)
            extra.append(bc)
        doc = head(title, desc, path, extra, robots=robots) + header(active) + f'<main id="main">\n{top}\n{body}\n</main>\n' + FOOTER
        target = OUT / (path.strip("/") + "/index.html" if path.endswith("/") and path != "/" else path.lstrip("/") or "index.html")
        if path == "/":
            target = OUT / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(doc)
        if in_sitemap:
            sitemap.append((SITE + path, priority))

    write("/", f"{APP}: Practice Questions & Mock Tests",
          "Practise for the Life in the UK Test with 770+ questions and timed mock tests (24 questions, 45 minutes). Free Android app with a daily study plan.",
          "/", page_body("home"), [APP_LD], priority="1.0")
    write("/demo/", f"{APP} Demo: Try Mock Test Questions Free",
          "Try the Life in the UK Test Prep app in your browser. Answer real practice questions, read the explanations and study notes, and take a short timed mock test.",
          "/demo/", page_body("demo"), [], crumb="Interactive demo")
    body, ld = questions_page()
    write("/practice-questions/", "Life in the UK Test Practice Questions: 20 Free with Answers",
          "Try 20 free Life in the UK Test practice questions with answers and explanations, covering history, the UK today, government and the law. 770+ more in the app.",
          "/practice-questions/", body, ld, crumb="Practice questions", priority="0.9")
    write("/study-guide/", "How to Pass the Life in the UK Test: 4-Week Study Plan",
          "How the Life in the UK Test works, what each handbook chapter covers, a simple 4-week study plan and tips for test day.",
          "/study-guide/", page_body("study-guide"), [{"@type": "Article", "headline": "How to pass the Life in the UK Test: study guide and 4-week plan",
          "inLanguage": "en-GB", "author": {"@id": f"{SITE}/#org"}, "publisher": {"@id": f"{SITE}/#org"}, "dateModified": TODAY,
          "mainEntityOfPage": SITE + "/study-guide/", "image": f"{SITE}/assets/img/og-image.png"}],
          crumb="Study guide", priority="0.9")
    body, ld = faq_page()
    write("/faq/", "Life in the UK Test Prep FAQ: the Test and the App",
          "Answers to common questions about the Life in the UK Test (24 questions, 45 minutes, 75% to pass) and the Life in the UK Test Prep app.",
          "/faq/", body, ld, crumb="FAQ")

    # long-tail guide pages
    hub_items = []
    for c in seo_pages.CHAPTERS:
        path = f"/{c['slug']}/"
        faq = [(q, a) for q, a in c["quick"]]
        body = guide_body(f"Life in the UK Test chapter {c['n']}: {c['name']}", c["lead"], f"Chapter {c['n']} guide",
                          c["body"], faq, path, chapter_questions(c["n"]) if c["n"] > 1 else "")
        write(path, c["title"], c["desc"], "", body,
              [article_ld(path, c["title"], c["desc"]), faq_ld(faq)], crumb=f"Chapter {c['n']}", priority="0.8")
        hub_items.append((path, f"Chapter {c['n']}: {c['name']}", c["lead"]))
    for t in seo_pages.TOPICS:
        path = f"/{t['slug']}/"
        body = guide_body(t["h1"], t["lead"], "Guide", t["body"], t["faq"], path)
        write(path, t["title"], t["desc"], "", body,
              [article_ld(path, t["title"], t["desc"]), faq_ld(t["faq"])], crumb=t["crumb"], priority="0.8")
        hub_items.append((path, t["crumb"], t["lead"]))
    cards = "".join(f'<li><a href="{u}"><b>{esc(n)}</b><span>{esc(d)}</span></a></li>' for u, n, d in hub_items)
    hub = seo_pages.HUB
    hbody = f"""<div class="wrap page-head"><p class="eyebrow">Guides</p><h1>Life in the UK Test guides</h1>
<p class="lead">Short guides to each handbook chapter and to the test itself: format, cost, booking, exemptions, results, retakes and how long to study.</p></div>
<section style="padding-top:24px"><div class="wrap"><ul class="guidegrid">{cards}</ul></div></section>
{CTA}"""
    write(f"/{hub['slug']}/", hub["title"], hub["desc"], "", hbody, [], crumb="Guides", priority="0.9")

    for slug, title, desc, crumb in [
        ("privacy-policy", f"Privacy Policy: {APP}", f"How {APP} handles your information: data on your device, optional backup, analytics, crash reports and ads.", "Privacy policy"),
        ("delete-account", f"Delete Your Account and Data: {APP}", f"How to delete your {APP} account and data, in the app or by email.", "Delete your data"),
        ("terms", f"Terms of Use: {APP}", f"Terms of use for {APP}, including study content and subscriptions.", "Terms of use"),
    ]:
        write(f"/{slug}.html", title, desc, "", f'<div class="wrap"><article class="prose doc">{page_body(slug)}</article></div>', [],
              crumb=crumb, priority="0.3")
    write("/404.html", f"Page not found: {APP}", "This page does not exist.", "",
          f'<section><div class="wrap final"><h1>Page not found</h1><p>The page you are looking for has moved or does not exist.</p><a class="btn" href="/">Go to the home page</a></div></section>',
          [], robots="noindex", in_sitemap=False)

    # interactive demo app, framed by /demo/
    tpl = page_body("demo-app.template")
    data = json.dumps(json.loads((PAGES / "demo-data.json").read_text()), ensure_ascii=False).replace("</", "<\\/")
    app = tpl.replace("__DATA__", data)
    (OUT / "demo" / "app.html").write_text(app)

    (OUT / "CNAME").write_text(DOMAIN + "\n")
    (OUT / ".nojekyll").write_text("")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /demo/app.html\n\nSitemap: {SITE}/sitemap.xml\n")
    urls = "\n".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><priority>{p}</priority></url>" for u, p in sitemap)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    (OUT / "site.webmanifest").write_text(json.dumps({
        "name": APP, "short_name": "UK Test Prep", "start_url": "/", "display": "browser",
        "background_color": "#FAF7F1", "theme_color": "#0F6E6E",
        "icons": [{"src": "/assets/img/app-icon.svg", "sizes": "any", "type": "image/svg+xml"},
                  {"src": "/assets/img/apple-touch-icon.png", "sizes": "180x180", "type": "image/png"}]}, indent=1))
    print(f"Built {len(sitemap)} indexed pages into {OUT}")


if __name__ == "__main__":
    build()
