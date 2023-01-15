@echo off 
   
set venv=email

python -m venv %venv%
echo %venv%/Scripts/Activate.ps1 		

echo %venv% > .gitignore
echo __pycache__ >> .gitignore
echo Download >> .gitignore

echo #"--Sua documentação--" > README.md

set list=imap-tools tqdm pyinstaller

for %%a in (%list%) do (
echo pip install %%a >> ./%venv%/Scripts/INSTALL_LIBS_VENV.bat
)
echo pip freeze ^> requeriments.txt >> ./%venv%/Scripts/INSTALL_LIBS_VENV.bat
	   