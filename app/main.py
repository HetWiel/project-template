from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="My project")


@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>It's running!</h1><p>Replace this with your own project.</p>"


@app.get("/health")
def health():
    # Handy for checking the project is still alive (e.g. with Uptime Kuma)
    return {"status": "ok"}
