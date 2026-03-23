from fabric import task

# Directories on the production server
BLOG_DIR = "~/workspaces/osiconl/blog"
OSICONL_DIR = "~/workspaces/osiconl/osiconl"

# Local directories
LOCAL_BLOG_DIR = "~/wsp/osiconl/blog"
LOCAL_OSICONL_DIR = "~/wsp/osiconl/osiconl"


@task
def deploy_blog(c):
    """Deploy the blog to production (blog.osico.nl).

    Pulls the latest changes and rebuilds the MkDocs site.
    Run with: fab -H user@osico.nl deploy-blog
    """
    with c.cd(BLOG_DIR):
        c.run("git pull origin main")
        c.run("~/.local/bin/uv sync")
        c.run("~/.local/bin/uv run mkdocs build")


@task
def deploy_osiconl(c):
    """Deploy the osiconl website to production (osico.nl).

    Pulls the latest changes, syncs dependencies and restarts the service.
    Run with: fab -H user@osico.nl deploy-osiconl
    """
    with c.cd(OSICONL_DIR):
        c.run("git pull origin main")
        c.run("~/.local/bin/uv sync")
    c.sudo("systemctl restart osiconl")


@task
def add_commit_blog(c, message="Update blog"):
    """Add, commit and push all changes in the local blog repo.

    Stages all changes, commits with a message and pushes to GitHub.
    Run with: fab add-commit-blog -m "My commit message"
    """
    with c.cd(LOCAL_BLOG_DIR):
        c.local("git add -A")
        c.local(f'git commit -m "{message}"')
        c.local("git push origin main")


@task
def add_commit_osiconl(c, message="Update osiconl"):
    """Add, commit and push all changes in the local osiconl repo.

    Stages all changes, commits with a message and pushes to GitHub.
    Run with: fab add-commit-osiconl -m "My commit message"
    """
    with c.cd(LOCAL_OSICONL_DIR):
        c.local("git add -A")
        c.local(f'git commit -m "{message}"')
        c.local("git push origin main")


@task
def commit_deploy_osiconl(c, message="Update osiconl"):
    """Commit, push and deploy osiconl in one step.

    Combines add-commit-osiconl and deploy-osiconl.
    Run with: fab -H user@osico.nl commit-deploy-osiconl -m "My commit message"
    """
    add_commit_osiconl(c, message)
    deploy_osiconl(c)


@task
def commit_deploy_blog(c, message="Update blog"):
    """Commit, push and deploy the blog in one step.

    Combines add-commit-blog and deploy-blog.
    Run with: fab -H user@osico.nl commit-deploy-blog -m "My commit message"
    """
    add_commit_blog(c, message)
    deploy_blog(c)


@task
def deploy(c):
    """Deploy all services to production.

    Sequentially deploys both the blog and the osiconl website.
    If deploy-blog fails the deployment is aborted and deploy-osiconl is not run.
    Run with: fab -H user@osico.nl deploy
    """
    deploy_blog(c)
    deploy_osiconl(c)
