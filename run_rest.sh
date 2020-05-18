#!/bin/bash
echo "Starting Rest Services..."
cd "$(dirname "${BASH_SOURCE[0]}")"
cd venv/bin
. activate
cd ../../
python ./rest_api.py 
echo "Local Flask Rest stopped."
echo ""
