# Contributing Guidelines

## 📌 Branch Rules
- `main` is protected — no direct commits.
- `dev` is the integration branch.
- Feature branches follow:
  `feature/<person>/<feature-name>`

## 🧪 Before opening a PR
1. Pull latest changes:
   `git pull origin dev`
2. Run local tests.
3. Follow commit format:
   `type: short description`
   Examples:
   - `feat: add material calculator`
   - `fix: scraper price parsing`
   - `docs: update API list`

## ✔️ Review Rules
- Minimum 1 approval required.
- CODEOWNERS have final say.
- No self-approval unless urgent.

## 🚫 Forbidden
- Pushing secrets or API keys.
- Large unreviewed files.
- Breaking CI pipelines.

