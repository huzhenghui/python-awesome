import sys

from invoke import task
from invoke import Context

# start snippet invoke_list


@task(default=True)
def invoke_list(c):
    c.run("invoke --list")


# end snippet invoke_list
# start snippet try_import_matplotlib


def try_import_matplotlib():
    try:
        import matplotlib
        print("success: import matplotlib")
    except Exception as e:
        print(str(e))


# end snippet try_import_matplotlib
# start snippet auto_install_matplotlib


def _auto_install_matplotlib(c: Context):
    try:
        import matplotlib
        print("success: import matplotlib")
    except Exception as e:
        print(str(e))
        c.run(sys.executable + ' -m pip install matplotlib')


@task
def auto_install_matplotlib(c):
    _auto_install_matplotlib(c)


# end snippet auto_install_matplotlib
