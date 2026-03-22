from fabric import task


@task
def deploy_blog(c):
    """Deploy the blog project (MkDocs) on the remote host."""
    with c.cd("~/blog"):
        c.run("git pull")
        c.run("mkdocs build")


@task
def deploy_osiconl(c):
    """Deploy the osiconl project (Reflex) on the remote host."""
    with c.cd("~/osiconl"):
        c.run("git pull")
        c.run("uv sync")
        c.run("sudo systemctl restart osiconl")


@task
def deploy(c):
    """Deploy both blog and osiconl sequentially."""
    deploy_blog(c)
    deploy_osiconl(c)
