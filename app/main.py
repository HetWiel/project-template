from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Mijn project")


@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>Het draait!</h1><p>Vervang dit door je eigen project.</p>"


@app.get("/health")
def health():
    # Handig voor controle of het project nog leeft (bijv. met Uptime Kuma)
    return {"status": "ok"}
