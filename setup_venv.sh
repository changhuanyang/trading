#!/bin/bash

set -e
VENV_PATH="./venv"
echo "----------------------------"
echo "Building virtual environment"
echo "----------------------------"
python3 -m venv $VENV_PATH
source ${VENV_PATH}/bin/activate

pip install pip --upgrade

pip install -r requirements.txt 

echo "---------"
echo "All done!"
echo "---------"
echo "Please now run 'source ${VENV_PATH}/bin/activate' to open the virtual environmnet"