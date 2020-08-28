:: build game
cd aird-venv\Scripts
activate.bat
cd ../..
pyinstaller game.py --onefile --noconsole
deactivate
move dist\game.exe game.exe
pause
