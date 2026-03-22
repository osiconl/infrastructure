from fabric import task

# Directories on the production server
BLOG_DIR = "~/blog"
OSICONL_DIR = "~/osiconl"


@task
def deploy_blog(c):
    """Deploy the blog to production (blog.osico.nl).

    Pulls the latest changes and rebuilds the MkDocs site.
    Run with: fab -H user@osico.nl deploy-blog
    """
    with c.cd(BLOG_DIR):
        c.run("git pull origin main")
        c.run("mkdocs build")


@task
def deploy_osiconl(c):
    """Deploy the osiconl website to production (osico.nl).

    Pulls the latest changes, syncs dependencies and restarts the service.
    Run with: fab -H user@osico.nl deploy-osiconl
    """
    with c.cd(OSICONL_DIR):
        c.run("git pull origin main")
        c.run("uv sync")
        c.sudo("systemctl restart osiconl")


@task
def deploy(c):
    """Deploy all services to production.

    Sequentially deploys both the blog and the osiconl website.
    If deploy-blog fails the deployment is aborted and deploy-osiconl is not run.
    Run with: fab -H user@osico.nl deploy
    """
    deploy_blog(c)
    deploy_osiconl(c)
