from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import connect

app = FastAPI(title="Citation Explorer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    with connect() as conn:
        conn.execute("SELECT 1")
    return {"status": "ok"}


# Roadmap endpoints: /search, /papers/{id}, /papers/{id}/related, /papers/{id}/graph
