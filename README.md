# lifeintheuktestcoach.co.uk

Website for the Android app **Life in the UK Test Prep**, served by GitHub Pages from `docs/`.

```sh
python3 build.py      # rebuilds docs/ from pages/ and static/
cd docs && python3 -m http.server 8765   # preview at http://localhost:8765
```

- `pages/`: page bodies, the practice questions (`practice-questions.json`) and the interactive demo.
- `static/`: CSS, self-hosted fonts (SIL Open Font License) and images.
- `build.py`: shared head with SEO tags and structured data, header, footer, FAQ, sitemap and robots.txt.

Independent study app. Not affiliated with the Home Office.
