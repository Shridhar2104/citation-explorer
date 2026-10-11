CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS papers (
    id              TEXT PRIMARY KEY,          -- OpenAlex work id, e.g. W2741809807
    doi             TEXT,
    title           TEXT NOT NULL,
    abstract        TEXT,
    publication_year INT,
    cited_by_count  INT NOT NULL DEFAULT 0,
    authors         TEXT[] NOT NULL DEFAULT '{}',
    venue           TEXT,
    embedding       vector(384)                -- all-MiniLM-L6-v2
);

-- citing_id cites cited_id. cited_id may not be in papers yet (outside our ingested set).
CREATE TABLE IF NOT EXISTS citations (
    citing_id TEXT NOT NULL REFERENCES papers(id) ON DELETE CASCADE,
    cited_id  TEXT NOT NULL,
    PRIMARY KEY (citing_id, cited_id)
);

CREATE INDEX IF NOT EXISTS citations_cited_idx ON citations (cited_id);
CREATE INDEX IF NOT EXISTS papers_embedding_idx ON papers USING hnsw (embedding vector_cosine_ops);
