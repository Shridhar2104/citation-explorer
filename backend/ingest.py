"""Fetch papers from OpenAlex, embed their abstracts, and store them.

Usage: python ingest.py "protein folding" "large language models" --per-topic 200
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("topics", nargs="+")
    parser.add_argument("--per-topic", type=int, default=200)
    args = parser.parse_args()
    raise NotImplementedError("ingest is next on the roadmap")


if __name__ == "__main__":
    main()
