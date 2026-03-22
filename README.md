# infrastructure

Fabric-based deployment management for the `blog` (MkDocs, `blog.osico.nl`) and `osiconl` (Reflex, `osico.nl`) projects. Both projects run on the same Hetzner machine.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Deploy blog only
fab -H user@osico.nl deploy-blog

# Deploy osiconl only
fab -H user@osico.nl deploy-osiconl

# Deploy both (blog first, then osiconl)
fab -H user@osico.nl deploy
```

## Tasks

- **`deploy-blog`** — `git pull` + `mkdocs build` in `~/blog`
- **`deploy-osiconl`** — `git pull` + `uv sync` + `systemctl restart osiconl` in `~/osiconl`
- **`deploy`** — runs both sequentially