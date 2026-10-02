# Projectsjabloon voor hetwiel.dev

Een startpunt voor elk nieuw project: een kleine FastAPI-app in Docker,
die bij elke `git push` automatisch online komt op `<naam>.hetwiel.dev`.

## Nieuw project starten

### 1. Repo maken
Zet dit sjabloon één keer op GitHub als repo `project-sjabloon` en vink bij
**Settings → General** de optie **Template repository** aan. Daarna maak je
elk nieuw project met de knop **Use this template**.

### 2. Naam invullen
In `.github/workflows/deploy.yml` staat bovenaan:
```yaml
PROJECT: mijnproject   # ← alleen dit aanpassen
```
Gebruik alleen kleine letters en streepjes, bijv. `whatsapp-bot`.

### 3. Secrets toevoegen
In de nieuwe repo: **Settings → Secrets and variables → Actions**, dezelfde
drie als bij `hetwiel`: `SERVER_HOST`, `SERVER_USER`, `SSH_PRIVATE_KEY`.

### 4. Project aanmelden in de hetwiel-repo
In `docker-compose.yml` van **hetwiel**, onder `services:`:
```yaml
  mijnproject:
    image: ghcr.io/<gebruikersnaam>/<reponaam>:latest
    container_name: mijnproject
    restart: unless-stopped
    env_file:
      - path: ./env/mijnproject.env
        required: false
    networks:
      - web
```
In de `Caddyfile` van **hetwiel**:
```
mijnproject.hetwiel.dev {
	reverse_proxy mijnproject:8000
}
```
Push de hetwiel-repo, zodat de server weet dat het project bestaat.

### 5. Pushen
Push dit project. Bij **Actions** zie je eerst het bouwen en daarna de deploy.
Daarna staat het op `https://mijnproject.hetwiel.dev`.

> Volgorde bij een nieuw project: eerst één keer het project pushen
> (zodat het image bestaat), dan de hetwiel-repo pushen.

## Lokaal testen
```
docker build -t mijnproject .
docker run --rm -p 8000:8000 mijnproject
```
Open http://localhost:8000

## Geheimen (wachtwoorden, API-keys)
Nooit in Git. Zet ze op de server in `/opt/hetwiel/env/mijnproject.env`.
Welke instellingen er zijn, staat in `.env.example`.

## Privé houden
Moet het project alleen voor jou zijn? Zet in de Caddyfile `basic_auth`
erbij (voorbeeld staat in de Caddyfile van hetwiel), of laat het Caddy-blok
weg en gebruik Tailscale.

## Geen Python?
Vervang `app/`, `requirements.txt` en de `Dockerfile` door wat bij je project
past. Zorg alleen dat de app op poort 8000 luistert, of pas de poort aan in de
Caddyfile. De workflow werkt voor elke taal.
