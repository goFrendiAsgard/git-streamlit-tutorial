#!/bin/bash

if [ ! -d venv ]
then
    python -m venv venv
fi
source venv/bin/activate

pip install -r requirements.txt

echo "Sambutan Kades Sukamaju: Now you are ready!"