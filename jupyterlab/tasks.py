import platform
import sys
from distutils.sysconfig import get_python_lib

from invoke import task
from invoke.context import Context


@task
def invoke_choose(c):
    result = c.run(
        "invoke --list --list-format=json | jq '.tasks[].name' | /usr/local/opt/choose-gui/bin/choose")
    print("\nChoose Recipe: ", result.stdout)
    c.run("invoke " + result.stdout)


@task
def invoke_fzf(c):
    result = c.run(
        'pwsh -c "invoke --list --list-format=json | ConvertFrom-Json | Select-Object -ExpandProperty tasks | Select-Object -ExpandProperty name | fzf"')
    print("\nChoose Recipe: ", result.stdout)
    c.run("invoke " + result.stdout)


@task
def unknown_os(c):
    print("Unknown OS : ", platform.system())


@task(default=True)
def default_task(c):
    os_default = {
        'Darwin': invoke_choose,
        'Windows': invoke_fzf
    }
    os_default.get(platform.system(), unknown_os)(c)


@task
def invoke_list(c):
    c.run("invoke --list")


def get_executable():
    return sys.executable


@task
def executable(c):
    print(get_executable())


def get_python_lib_wrapper():
    return get_python_lib()


@task()
def python_lib(c):
    print(get_python_lib_wrapper())


@task()
def jupyterlab(c):
    context:  Context = c
    context.run(
        "jupyter lab", env={'PYTHONPATH': get_python_lib_wrapper()})
    print(type(c))
