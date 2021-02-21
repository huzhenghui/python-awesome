# jupyterlab-pandas

<!-- markdownlint-disable MD007 MD030 -->

-   [jupyterlab-pandas](#jupyterlab-pandas)
-   [tasks.py](#taskspy)
-   [pandas.ipynb](#pandasipynb)
-   [Mask SubCommands](#mask-subcommands)
    -   [inv-invoke-list](#inv-invoke-list)
        -   [def invoke\_list](#def-invoke_list)
        -   [inv-invoke-list-output](#inv-invoke-list-output)
    -   [begin: mask task in template : build
        content](#begin-mask-task-in-template--build-content)
    -   [ninja-rules](#ninja-rules)
        -   [ninja custom-rule](#ninja-custom-rule)
        -   [ninja-rules-output](#ninja-rules-output)
    -   [ninja-targets](#ninja-targets)
        -   [ninja build-all](#ninja-build-all)
        -   [ninja custom-build](#ninja-custom-build)
        -   [ninja report-build](#ninja-report-build)
        -   [ninja-targets-output](#ninja-targets-output)
    -   [readme-md](#readme-md)
        -   [ninja readme-build](#ninja-readme-build)
    -   [end: mask task in template : build
        content](#end-mask-task-in-template--build-content)
    -   [begin: mask task in template : ninja
        command](#begin-mask-task-in-template--ninja-command)
    -   [ninja-browse](#ninja-browse)
    -   [ninja-graph-png](#ninja-graph-png)
    -   [ninja-graph-dot-xdot](#ninja-graph-dot-xdot)
    -   [ninja-graph-dot](#ninja-graph-dot)
        -   [ninja-graph-dot-output](#ninja-graph-dot-output)
    -   [ninja-all](#ninja-all)
        -   [build.ninja](#buildninja)
    -   [end: mask task in template : ninja
        command](#end-mask-task-in-template--ninja-command)

<!-- markdownlint-enable MD007 MD030 -->

# tasks.py

[tasks.py](./tasks.py)

``` python

def try_import_pandas():
    try:
        import pandas
        print("success: import pandas")
    except Exception as e:
        print(str(e))


```

# pandas.ipynb

[pandas.ipynb](/pandas.ipynb)

<!-- markdownlint-disable MD012 MD033 MD046 -->

``` python
import tasks
```

``` python
tasks.try_import_pandas()
```

    success: import pandas

``` python
import pandas as pd
```

``` python
url = 'https://kite.com/kite-public/iris.csv'
df = pd.read_csv(url)
df.head()
```

<div>

<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th>
</th>
<th>
sepal\_length
</th>
<th>
sepal\_width
</th>
<th>
petal\_length
</th>
<th>
petal\_width
</th>
<th>
species
</th>
</tr>
</thead>
<tbody>
<tr>
<th>
0
</th>
<td>
5.1
</td>
<td>
3.5
</td>
<td>
1.4
</td>
<td>
0.2
</td>
<td>
setosa
</td>
</tr>
<tr>
<th>
1
</th>
<td>
4.9
</td>
<td>
3.0
</td>
<td>
1.4
</td>
<td>
0.2
</td>
<td>
setosa
</td>
</tr>
<tr>
<th>
2
</th>
<td>
4.7
</td>
<td>
3.2
</td>
<td>
1.3
</td>
<td>
0.2
</td>
<td>
setosa
</td>
</tr>
<tr>
<th>
3
</th>
<td>
4.6
</td>
<td>
3.1
</td>
<td>
1.5
</td>
<td>
0.2
</td>
<td>
setosa
</td>
</tr>
<tr>
<th>
4
</th>
<td>
5.0
</td>
<td>
3.6
</td>
<td>
1.4
</td>
<td>
0.2
</td>
<td>
setosa
</td>
</tr>
</tbody>
</table>

</div>

<!-- markdownlint-enable MD012 MD033 MD046 -->

# Mask SubCommands

[Mask Awesome](https://github.com/huzhenghui/mask-awesome)

## inv-invoke-list

``` bash
inv invoke-list
```

### def `invoke_list`

``` python

@task
def invoke_list(c):
    c.run("invoke --list")


```

### inv-invoke-list-output

``` plain
Available tasks:

  auto-install-pandas
  invoke-list

```

## inv-auto-install-pandas

``` bash
inv auto-install-pandas
```

### def `auto_install_pandas`

``` python

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


```

## begin: mask task in template : build content

## ninja-rules

``` bash
ninja -t rules
```

### ninja custom-rule

``` ninja
# custom rule here

```

### ninja-rules-output

``` plain
cmdshelf-repository
copy_alternate
dot
ghq
github-markdown-toc
jupyter-nbconvert-markdown
mask
mask-man-markdown
mask-screenshot
mask-stderr-tee
mask-stdout-csv-markdown
mask-stdout-json
mask-stdout-tee
mask-tee
pandocomatic
phony
```

## ninja-targets

``` bash
ninja -t targets all
```

### ninja build-all

``` ninja
build all: phony README.md

default all

```

### ninja custom-build

``` ninja
# custom build here

```

### ninja report-build

``` ninja
# report build here

```

### ninja-targets-output

``` plain
all: phony
build/pandoc-lua-filters/include-files/include-files.lua: ghq
build/ninja/ninja-rules-output.txt: mask-stdout-tee
build/ninja/ninja-targets-output.txt: mask-stdout-tee
build/ninja/ninja.graph.dot: mask-tee
build/ninja/ninja.graph.png: mask
build/temp/README.md: copy_alternate
build/README.TOC/README.TOC.md: github-markdown-toc
README-template: phony
pandas.md: jupyter-nbconvert-markdown
build/inv-invoke-list-output.txt: mask-stdout-tee
README-custom: phony
README.md: pandocomatic
```

## readme-md

``` bash
ninja --verbose README.md
```

### ninja readme-build

``` ninja
build ./pandas.md : jupyter-nbconvert-markdown ./pandas.ipynb

build ./build/inv-invoke-list-output.txt : mask-stdout-tee ./maskfile.md
  mask_subcommand = inv-invoke-list

build README-custom : phony $
  ./pandas.md $
  ./build/inv-invoke-list-output.txt

```

``` ninja
build README.md : pandocomatic maskfile.md | README-template README-custom

```

## end: mask task in template : build content

## begin: mask task in template : ninja command

## ninja-browse

``` bash
ninja -t browse
```

## ninja-graph-png

``` bash
dot -Tpng -o./build/ninja/ninja.graph.png ./build/ninja/ninja.graph.dot
```

![ninja](./build/ninja/ninja.graph.png)

## ninja-graph-dot-xdot

``` bash
detach -- xdot "${MASKFILE_DIR}/build/ninja/ninja.graph.dot"
```

## ninja-graph-dot

``` bash
ninja -t graph
```

### ninja-graph-dot-output

``` dot
digraph ninja {
rankdir="LR"
node [fontsize=10, shape=box, height=0.25]
edge [fontsize=10]
"0x7fa81c408a80" [label="all"]
"0x7fa81c408c00" -> "0x7fa81c408a80" [label=" phony"]
"0x7fa81c408c00" [label="README.md"]
"0x7fa81c40a390" [label="pandocomatic", shape=ellipse]
"0x7fa81c40a390" -> "0x7fa81c408c00"
"0x7fa81c409170" -> "0x7fa81c40a390" [arrowhead=none]
"0x7fa81c409ed0" -> "0x7fa81c40a390" [arrowhead=none]
"0x7fa81c40a2a0" -> "0x7fa81c40a390" [arrowhead=none]
"0x7fa81c409170" [label="maskfile.md"]
"0x7fa81c409ed0" [label="README-template"]
"0x7fa81c409c20" [label="phony", shape=ellipse]
"0x7fa81c409c20" -> "0x7fa81c409ed0"
"0x7fa81c408ee0" -> "0x7fa81c409c20" [arrowhead=none]
"0x7fa81c409f30" -> "0x7fa81c409c20" [arrowhead=none]
"0x7fa81c4090b0" -> "0x7fa81c409c20" [arrowhead=none]
"0x7fa81c409320" -> "0x7fa81c409c20" [arrowhead=none]
"0x7fa81c409580" -> "0x7fa81c409c20" [arrowhead=none]
"0x7fa81c4097c0" -> "0x7fa81c409c20" [arrowhead=none]
"0x7fa81c409ac0" -> "0x7fa81c409c20" [arrowhead=none]
"0x7fa81c408ee0" [label="build/pandoc-lua-filters/include-files/include-files.lua"]
"0x7fa81c408e70" [label="ghq", shape=ellipse]
"0x7fa81c408e70" -> "0x7fa81c408ee0"
"0x7fa81c409f30" [label="build.ninja"]
"0x7fa81c4090b0" [label="build/ninja/ninja-rules-output.txt"]
"0x7fa81c409170" -> "0x7fa81c4090b0" [label=" mask-stdout-tee"]
"0x7fa81c409320" [label="build/ninja/ninja-targets-output.txt"]
"0x7fa81c409170" -> "0x7fa81c409320" [label=" mask-stdout-tee"]
"0x7fa81c409580" [label="build/ninja/ninja.graph.dot"]
"0x7fa81c409170" -> "0x7fa81c409580" [label=" mask-tee"]
"0x7fa81c4097c0" [label="build/ninja/ninja.graph.png"]
"0x7fa81c409750" [label="mask", shape=ellipse]
"0x7fa81c409750" -> "0x7fa81c4097c0"
"0x7fa81c409170" -> "0x7fa81c409750" [arrowhead=none]
"0x7fa81c409580" -> "0x7fa81c409750" [arrowhead=none]
"0x7fa81c409ac0" [label="build/README.TOC/README.TOC.md"]
"0x7fa81c409950" -> "0x7fa81c409ac0" [label=" github-markdown-toc"]
"0x7fa81c409950" [label="build/temp/README.md"]
"0x7fa81c409170" -> "0x7fa81c409950" [label=" copy_alternate"]
"0x7fa81c40a2a0" [label="README-custom"]
"0x7fa81c40a230" [label="phony", shape=ellipse]
"0x7fa81c40a230" -> "0x7fa81c40a2a0"
"0x7fa81c409b90" -> "0x7fa81c40a230" [arrowhead=none]
"0x7fa81c40a0f0" -> "0x7fa81c40a230" [arrowhead=none]
"0x7fa81c409b90" [label="pandas.md"]
"0x7fa81c409cf0" -> "0x7fa81c409b90" [label=" jupyter-nbconvert-markdown"]
"0x7fa81c409cf0" [label="pandas.ipynb"]
"0x7fa81c40a0f0" [label="build/inv-invoke-list-output.txt"]
"0x7fa81c409170" -> "0x7fa81c40a0f0" [label=" mask-stdout-tee"]
}
```

## ninja-all

``` bash
ninja --verbose
```

### build.ninja

``` ninja
builddir=./build
mask_subcommand = --help
mask_stdout_csv_markdowndelimiter = ","
jupyter_nbconvert_markdown_output_files_dir=./build/jupyter-nbconvert-markdown-output-files

#######################################
# begin: rule in template

rule mask
  command = mask --maskfile $in $mask_subcommand

rule mask-tee
  command = mask --maskfile $in $mask_subcommand 2>&1 | tee $out 1> /dev/null

rule mask-stdout-tee
  command = mask --maskfile $in $mask_subcommand 2>/dev/null | tee $out 1> /dev/null

rule mask-stderr-tee
  command = bash -c 'mask $mask_subcommand 1>/dev/null 2> >(tee $out)' || echo $$?

# <!-- markdownlint-disable MD013 -->
rule mask-man-markdown
  command = set -e && set -o pipefail && $
    mask --maskfile $in $mask_subcommand | $
    ul | $
    ansifilter --bbcode | $
    inv --search-root="$$(ghq list --full-path https://github.com/huzhenghui/pyinvoke-awesome)/bbcode" bbcode-parser-format | $
    pandoc --from=html --to=markdown | $
    tee $out 1> /dev/null
# <!-- markdownlint-enable MD013 -->

rule mask-stdout-csv-markdown
  command = mask --maskfile $in $mask_subcommand 2>/dev/null | $
    csvtomd --delimiter "$$(echo $mask_stdout_csv_markdowndelimiter)" | $
    tee $out 1> /dev/null

rule mask-stdout-json
  command = mask --maskfile $in $mask_subcommand 2>/dev/null | $
    jq | $
    tee $out 1> /dev/null

rule mask-screenshot
  command = $
    regular_logfile="./build/temp/$$(basename $out).mask-screenshot.logfile" && $
    rm -f -v "$${regular_logfile}" && $
    until [[ -s "$${regular_logfile}" ]]; do $
      screen_logfile="$$(mktemp -d)/logfile"; $
      echo "$${screen_logfile}"; $
      mkfifo "$${screen_logfile}"; $
      screen -L -Logfile "$${screen_logfile}" $
        -dmS mask-screenshot-"$$(basename $out)" $
        sh -c "stdbuf -o0 mask --maskfile $in $mask_subcommand; $
          date +'%F %T %Z %z - %+ https://github.com/huzhenghui' | lolcat;"; $
      dd bs=1 if="$${screen_logfile}" of="$${regular_logfile}"; $
    done && $
    ansifilter --html --encoding=utf8 --input="$${regular_logfile}" | $
      tee ./build/temp/"$$(basename $out)".mask-screenshot.html | $
      wkhtmltoimage --format png - "$out"

rule pandocomatic
  command = pandocomatic --input $in --output $out

rule github-markdown-toc
  command = gh-md-toc --hide-header --hide-footer --no-escape $in > $out

rule copy_alternate
  command = if [[ -f "$alternate" ]]; $
    then $
      cp "$alternate" "$out"; $
    else $
      cp "$in" "$out"; $
    fi;

rule dot
  command = dot -Tpng -o$out $in

rule ghq
  command = ghq get --update "$repository" && $
    find -d "$link_dirname" -exec rmdir {} \; && $
    ln -Fs "$$(ghq list --full-path $repository)" "$link_dirname"
  generator = 1

rule cmdshelf-repository
  command = $$( $
    cmdshelf remote list | ack "^$cmdshelf_name" 1>&2 || $
    cmdshelf remote add "$cmdshelf_name" "$cmdshelf_url" 1>&2 $
    ) && $
    repository_path="$$(realpath $${HOME}/.cmdshelf/remote/$cmdshelf_name)" && $
    echo "$${repository_path}" && $
    stub_path="$$(realpath ./build/$cmdshelf_name)" && $
    echo "$${stub_path}" && $
    find -d "$${stub_path}" -exec rmdir {} \; && $
    ln -Fs "$${repository_path}" "$${stub_path}"
  generator = 1

# <!-- markdownlint-disable MD013 -->
rule jupyter-nbconvert-markdown
  command = jupyter nbconvert $
    --to=markdown $
    --NbConvertApp.output_files_dir="$jupyter_nbconvert_markdown_output_files_dir" $
    --output="$out" $
    "$in"
# <!-- markdownlint-enble MD013 -->

# end: rule in template
#######################################

#######################################
# start snippet custom-rule

# custom rule here

# end snippet custom-rule
#######################################

#######################################
# start snippet build-all

build all: phony README.md

default all

# end snippet build-all
#######################################

#######################################
# start snippet custom-build

# custom build here

# end snippet custom-build
#######################################

#######################################
# start snippet report-build

# report build here

# end snippet report-build
#######################################

#######################################
# begin: readme-build in template

# ninja will create ./build/pandoc-lua-filters/include-files/ automatically
build ./build/pandoc-lua-filters/include-files/include-files.lua : ghq
  repository = https://github.com/pandoc/lua-filters
  link_dirname = ./build/pandoc-lua-filters

build ./build/ninja/ninja-rules-output.txt : mask-stdout-tee ./maskfile.md
  mask_subcommand = ninja-rules

build ./build/ninja/ninja-targets-output.txt : mask-stdout-tee ./maskfile.md
  mask_subcommand = ninja-targets

build ./build/ninja/ninja.graph.dot : mask-tee ./maskfile.md
  mask_subcommand = ninja-graph-dot

build ./build/ninja/ninja.graph.png : mask ./maskfile.md | ./build/ninja/ninja.graph.dot
  mask_subcommand = ninja-graph-png

build ./build/temp/README.md : copy_alternate ./maskfile.md
  alternate = ./README.md

build ./build/README.TOC/README.TOC.md : github-markdown-toc ./build/temp/README.md

build README-template : phony $
  ./build/pandoc-lua-filters/include-files/include-files.lua $
  ./build.ninja $
  ./build/ninja/ninja-rules-output.txt $
  ./build/ninja/ninja-targets-output.txt $
  ./build/ninja/ninja.graph.dot $
  ./build/ninja/ninja.graph.png $
  ./build/README.TOC/README.TOC.md $

# end: readme-build in template
#######################################

#######################################
# start snippet custom-readme-build

build ./pandas.md : jupyter-nbconvert-markdown ./pandas.ipynb

build ./build/inv-invoke-list-output.txt : mask-stdout-tee ./maskfile.md
  mask_subcommand = inv-invoke-list

build README-custom : phony $
  ./pandas.md $
  ./build/inv-invoke-list-output.txt

# end snippet custom-readme-build
#######################################

#######################################
# $ followed by a newline
# escape the newline (continue the current line across a line break).
# start snippet readme-build

build README.md : pandocomatic maskfile.md | README-template README-custom

# end snippet readme-build
#######################################
```

## end: mask task in template : ninja command
