#!/bin/sh
export GOOGLE_APPLICATION_CREDENTIALS="/home/azureuser/nftmarket/appdata-320712-a67e4d080257.json"
uvicorn main:app --host=0.0.0.0 --port=8000