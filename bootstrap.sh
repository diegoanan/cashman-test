#!/bin/sh
export FLASK_APP=./cashman/index.py #llama nuestro archivo ejecutor
source $(pipenv --venv)/bin/activate #implementa el complemento pipenv para ejecutart en el ambiente virtual
flask run -h 0.0.0.0 #la salida sera por la ip publica 

