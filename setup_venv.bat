python -m venv aird-venv
cd aird-venv\Scripts
activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller
deactivate
pause
