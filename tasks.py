import json
import os
import platform
import sys

from invoke import task
from invoke.context import Context
from typing import List

@task
def invoke_choose(c):
    result = c.run("invoke --list --list-format=json | jq '.tasks[].name' | /usr/local/opt/choose-gui/bin/choose")
    print("\nChoose Recipe: ", result.stdout)
    c.run("invoke " + result.stdout)

@task
def invoke_fzf(c):
    result = c.run('pwsh -c "invoke --list --list-format=json | ConvertFrom-Json | Select-Object -ExpandProperty tasks | Select-Object -ExpandProperty name | fzf"')
    print("\nChoose Recipe: ", result.stdout)
    c.run("invoke " + result.stdout)

@task
def unknown_os(c):
    print("Unknown OS : ", platform.system())

@task(default=True)
def default_task(c):
    os_default = {
        'Darwin' : invoke_choose,
        'Windows' : invoke_fzf
    }
    os_default.get(platform.system(), unknown_os)(c)

@task
def invoke_list(c):
    c.run("invoke --list")

@task
def invoke_list_nested(c):
    c.run("invoke --list --list-format=nested")

@task
def invoke_list_json(c):
    c.run("invoke --list --list-format=json")

def get_python_draft_dir(c):
    result = c.run("jump cd python-draft")
    return result.stdout

@task
def python_draft_dir(c):
    print(get_python_draft_dir(c))

@task
def code(c):
    cwd = os.getcwd()
    workspace = cwd + "/python.code-workspace"
    if os.path.exists(workspace):
        c.run("code " + workspace)
    else:
        c.run("code " + cwd)

@task
def executable(c):
    print(sys.executable)

@task
def vscode_settings_use_invoke(c):
    settings = {
        "python.pythonPath" : sys.executable
    }
    print(json.dumps(settings))

@task
def project_used_pyenv(c):
    context: Context = c
    result = context.run('jump pins', hide="out")
    pins: List[str] = result.stdout.split("\n")
    for pin in pins:  # type: str
        pin_data = pin.split("\t")
        if (len(pin_data) == 2):
            tag, path = pin_data
            if (os.path.exists(path + "/.python-version")):
                print(tag, path)

@task
def python_commands(c):
    context: Context = c
    context.run('inv executable | xargs dirname | xargs lsd --almost-all --long --color always --icon always --icon-theme fancy')

@task
def python_commands_html_copy(c):
    context: Context = c
    context.run('inv python-commands | ansifilter --encoding=utf-8 --rtf | textutil -stdin -stdout -convert html | copyq copy text/html -')
