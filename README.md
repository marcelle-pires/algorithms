# Algorithms

This is a Python CLI developed during my algorithms content review guided by the book Grokking Algorithms.

## Getting started

All required dependencies are declared in requirements.txt file, you can install of them by executing:

```bash
python -m pip install -r requirements.txt
```

This script has a virtual environment, you can activate it executing:

```bash
source env/bin/activate
```

## Installing new packages

You can install new packages using pip, as normal, but remember to include this new packages in requirements file:

```bash
python -m pip freeze > requirements.txt
```

## Run
To execute this cli, based in [fire library](https://google.github.io/python-fire/guide/), you will execute following the stardard:

```bash
python -m algorithms [name_algorithm] [param1] [param2] 
```

For example, to execute a binary search passing as parameter a list and a value to be searched, you need to execute:

```bash
python -m algorithms binary_search_algorithm "[1, 2, 3, 7, 8]" 2
```

If you need help, execute the command below and find options:
```bash
python -m algorithms --help
```

## Test

To execute all tests generated in this script, you can execute:

```bash
python -m pytest
```

## Interesting Links

[Know more about me - Linkeding: Marcelle Pires](www.linkedin.com/in/marcelle-reis-pires)

[[Book] Grokking Algorithms: An illustrated guide for programmers and other curious people](https://www.amazon.com/-/pt/gp/product/B09781V6F7/ref=dbs_a_def_rwt_hsch_vapi_tkin_p1_i0)

