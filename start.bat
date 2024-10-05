@echo off
C:/Users/tmax/AppData/Local/Programs/Python/Python312/python.exe -m black .
C:/Users/tmax/AppData/Local/Programs/Python/Python312/python.exe -m isort .
cls

echo Starting server
cd src/
C:/Users/tmax/AppData/Local/Programs/Python/Python312/python.exe c:/Users/tmax/Downloads/skeleton_dicegame/src/DicegameServer.py
PAUSE