# Citation Explorer

Search research papers by meaning and see how they connect through citations.

Type a topic like "protein folding" and get the most relevant papers, ranked by what they're about rather than keyword matches. Open any paper to see its details, related work, and a graph of its citation neighbors.

> Status: work in progress. See the roadmap below.

## Why

Literature reviews take weeks because finding papers is only half the job. The other half is understanding how they relate. This project explores both: semantic search over abstracts, plus citation links to surface papers that keyword search misses.

## How it works

1. **Data:** papers come from [OpenAlex](https://openalex.org), a free and open catalog of scholarly works.
2. **Abstracts:** OpenAlex stores abstracts as an inverted index; the ingest step rebuilds them into plain text.
3. **Embeddings:** each abstract is embedded with a small open-source model (`all-MiniLM-L6-v2`) and stored in Postgres with pgvector.
4. **Search:** the query is embedded the same way and matched to the nearest papers by cosine similarity.
5. **Related papers:** content similarity is combined with citation signals. Papers that cite each other, or share many references, get a boost.

```
OpenAlex API ──> ingest ──> Postgres + pgvector ──> FastAPI ──> Next.js UI
```

## Tech stack

| Layer | Tools |
|---|---|
| Frontend | Next.js, React, TypeScript, Tailwind |
| Backend | Python, FastAPI |
| Database | PostgreSQL + pgvector |
| Embeddings | sentence-transformers |
| Infra | Docker Compose |

## Project structure

```
citation-explorer/
├── docker-compose.yml   # Postgres + pgvector
├── backend/
│   ├── main.py          # FastAPI app
│   ├── ingest.py        # fetch, embed, and store papers
│   └── requirements.txt
└── frontend/            # Next.js app
```

## Getting started

### Prerequisites

Git, Docker, Python 3.11+, Node 20+.

### 1. Start the database

```bash
docker compose up -d
```

### 2. Run the backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

API docs: http://localhost:8000/docs

### 3. Load papers

```bash
python ingest.py "protein folding" "large language models" --per-topic 200
```

### 4. Run the frontend

```bash
cd frontend
npm install
npm run dev
```

App: http://localhost:3000

## API

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/search?q=...` | Papers ranked by semantic similarity |
| GET | `/papers/{id}` | Paper details |
| GET | `/papers/{id}/related` | Related papers (similarity + citation boost) |
| GET | `/papers/{id}/graph` | Citation neighbors for the graph view |

## Roadmap

- [x] Project skeleton (database, backend, frontend)
- [ ] Ingest papers from OpenAlex
- [ ] Semantic search endpoint
- [ ] Related papers with citation boost
- [ ] Search and detail UI
- [ ] Citation graph view
- [ ] Deploy (Vercel + Railway/Render)

## Design notes

- **Postgres + pgvector instead of a separate vector database:** one system for papers, citations, and vectors keeps the stack simple and lets search and citation queries run together.
- **Small local embedding model:** free, fast, and good enough for abstracts. Easy to swap for a larger model later.
- **Hybrid ranking:** pure similarity misses papers that are closely linked but worded differently. Citation signals catch those.

## What I'd build next

- AI summaries comparing a set of selected papers
- Clustering results into subtopics
- Exporting a reading list with formatted citations

## License

MIT