import sys

from invoke import task

@task
def invoke_list(c):
    c.run("invoke --list")

def try_import_pandas():
    try:
        import pandas
        print("import success")
    except Exception as reason:
        print(str(reason))

@task
def auto_install_pandas(c):
    try:
        import pandas
        print("import success")
    except Exception as reason:
        print(str(reason))
        c.run(sys.executable + " -m pip install pandas")

def read_csv_kite_pris():
    try:
        import pandas
        url = 'https://kite.com/kite-public/iris.csv'
        df = pandas.read_csv(url)
        return df.head()
    except Exception as reason:
        print(str(reason))

@task()
def read_csv_kite_pris_task(c):
    print(read_csv_kite_pris())
