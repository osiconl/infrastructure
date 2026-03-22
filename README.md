# infrastructure

Manages deployments for [blog](https://github.com/osiconl/blog) and [osiconl](https://github.com/osiconl/osiconl) using [Fabric](https://www.fabfile.org/).

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Deploy the blog to production:

```bash
fab -H user@osico.nl deploy-blog
```

Deploy the osiconl website to production:

```bash
fab -H user@osico.nl deploy-osiconl
```

Deploy all services to production:

```bash
fab -H user@osico.nl deploy
```

## Tasks

| Task | Description |
|---|---|
| `deploy-blog` | Pull latest changes and rebuild the MkDocs site at `blog.osico.nl` |
| `deploy-osiconl` | Pull latest changes, sync dependencies and restart the Reflex app at `osico.nl` |
| `deploy` | Run both `deploy-blog` and `deploy-osiconl` sequentially |