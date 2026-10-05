# Project template for hetwiel.dev

A starting point for every new project: a small FastAPI app in Docker
that goes live automatically on `<name>.hetwiel.dev` on every `git push`.

## Starting a new project

### 1. Create the repo
This repo is marked as a template (**Settings → General → Template repository**).
Create each new project with the **Use this template** button.

### 2. Fill in the name
At the top of `.github/workflows/deploy.yml`:
```yaml
PROJECT: myproject   # ← only change this
```
Use only lowercase letters and hyphens, e.g. `whatsapp-bot`.

### 3. Add the secrets
In the new repo: **Settings → Secrets and variables → Actions**, the same
three as in `hetwiel`: `SERVER_HOST`, `SERVER_USER`, `SSH_PRIVATE_KEY`.

### 4. Register the project in the hetwiel repo
In `docker-compose.yml` of **hetwiel**, under `services:`:
```yaml
  myproject:
    image: ghcr.io/<username>/<repo name>:latest
    container_name: myproject
    restart: unless-stopped
    env_file:
      - path: ./env/myproject.env
        required: false
    networks:
      - web
```
In the `Caddyfile` of **hetwiel**:
```
myproject.hetwiel.dev {
	import security
	reverse_proxy myproject:8000
}
```
Push the hetwiel repo, so the server knows the project exists.

### 5. Push
Push this project. Under **Actions** you'll see the build first, then the deploy.
After that it's at `https://myproject.hetwiel.dev`.

> Order for a new project: push the project once first
> (so the image exists), then push the hetwiel repo.

## The Apprentice
Every project keeps a ledger of what it was built with and how well the maker
understands each part: `apprentice.yml` (the levels, shown on hetwiel.dev/apprentice/)
and `APPRENTICE.md` (a card per material, plus the teach-back log). The rules are in
`CLAUDE.md`; the loop itself is the skill in `.claude/skills/apprentice/`.

After creating a project from this template: set `work:` and `opened:` in
`apprentice.yml`, and add the repo to the list in `site/content/apprentice.js`
in the hetwiel repo so its ledger shows up on the site.

## Testing locally
```
docker build -t myproject .
docker run --rm -p 8000:8000 myproject
```
Open http://localhost:8000

## Secrets (passwords, API keys)
Never in Git. Put them on the server in `/opt/hetwiel/env/myproject.env`.
The available settings are listed in `.env.example`.

## Keeping it private
Should the project be for you only? Add `basic_auth` in the Caddyfile
(there's an example in the hetwiel Caddyfile), or leave out the Caddy block
and use Tailscale.

## Not Python?
Replace `app/`, `requirements.txt` and the `Dockerfile` with whatever fits
your project. Just make sure the app listens on port 8000, or change the port in the
Caddyfile. The workflow works for any language.
