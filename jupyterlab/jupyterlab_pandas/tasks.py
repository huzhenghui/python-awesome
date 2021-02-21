import sys

from invoke import task
from invoke import Context

# start snippet invoke_list


@task
def invoke_list(c):
    c.run("invoke --list")


# end snippet invoke_list
# start snippet try_import_pandas


def try_import_pandas():
    try:
        import pandas
        print("success: import pandas")
    except Exception as e:
        print(str(e))


# end snippet try_import_pandas
# start snippet auto_install_pandas


def _auto_install_pandas(c: Context):
    try:
        import pandas
        print("success: import pandas")
    except Exception as e:
        print(str(e))
        c.run(sys.executable + " -m pip install pandas")


@task
def auto_install_pandas(c):
    _auto_install_pandas(c)


# end snippet auto_install_pandas
