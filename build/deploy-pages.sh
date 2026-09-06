#!/usr/bin/env bash
# Build the MkDocs site and force-push it to the gh-pages branch.
# Usage: ./build/deploy-pages.sh   (requires: pip install mkdocs-material; push rights to the repo)
set -euo pipefail
cd "$(dirname "$0")/.."
REPO_URL=$(git remote get-url origin)
mkdocs build --strict
touch site/.nojekyll
cd site
rm -rf .git
git init -q
git checkout -q -b gh-pages
git add -A
git -c user.name="${GIT_AUTHOR_NAME:-$(git -C .. config user.name)}" \
    -c user.email="${GIT_AUTHOR_EMAIL:-$(git -C .. config user.email)}" \
    commit -qm "Deploy site $(date -u +%Y-%m-%dT%H:%MZ)"
git push -q -f "$REPO_URL" gh-pages
rm -rf .git
echo "Deployed to gh-pages. Site: https://gorg667.github.io/linux-guide-fable/"
