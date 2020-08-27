:: build game
cd aird-venv\Scripts
activate.bat
cd ../..
pyinstaller game.py --onefile --noconsole
move dist\game.exe game.exe
pause
