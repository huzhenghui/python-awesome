from invoke import task
from invoke import Context


@task
def invoke_list(c):
    c.run("invoke --list")


def _install_jupyterlib_kite(c: Context):
    c.run('/usr/local/opt/jupyterlab/libexec/bin/pip install "jupyterlab-kite>=2.0.2"')


@task
def install_jupyterlib_kite(c):
    _install_jupyterlib_kite(c)
