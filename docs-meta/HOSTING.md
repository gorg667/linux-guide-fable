# Hosting the site on GitHub Pages

The site is generated with **MkDocs Material** from the Markdown in `guide/`. Two ways to publish:

## Option A — gh-pages branch (works now, no Actions needed)

```bash
pip install mkdocs-material
./build/deploy-pages.sh        # builds and force-pushes ./site to the gh-pages branch
```

Then, once: **GitHub → repo → Settings → Pages → Source: "Deploy from a branch" → Branch: `gh-pages` / `(root)` → Save.**
The site appears at https://gorg667.github.io/linux-guide-fable/ within a minute or two.

## Option B — GitHub Actions (auto-deploy on every push to main)

1. Copy `docs-meta/pages.yml.example` to `.github/workflows/pages.yml` and commit it
   (this must be done by a user/token with the `workflow` scope — the automation token used to
   write this repo didn't have it, which is why the file lives here as an example).
2. **Settings → Pages → Source: "GitHub Actions".**
3. Every push to `main` rebuilds and deploys.

## Local preview

```bash
mkdocs serve      # http://127.0.0.1:8000, live-reloads on edits
```

## Notes

- `guide/index.md` is the landing page; `guide/full.md` stitches every chapter into one page via snippets.
- `guide/FULL_GUIDE.md` (the raw concatenation) is excluded from the site to avoid duplication.
- Fonts (Inter, JetBrains Mono) load from Google Fonts; set `theme.font: false` in `mkdocs.yml` for a fully self-hosted build.
