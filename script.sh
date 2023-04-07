#!/bin/bash

python3 -m venv env

source env/bin/active

pip install -r requiremets.txt

python3 main.py

deactiavate

