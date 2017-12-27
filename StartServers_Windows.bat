@ECHO OFF
:: Author: tintinmovie <https://github.com/tintinmovie>

::This .bat script will run the backend (python) and frontend (node) servers with the click of a file
::Before doing this it checks to see whether the following dependicies below (add any new ones that are added):
:: * Python
:: * NodeJS
:: * NPM (which is should be bundled with NodeJS)
:: * Gulp


::=========================================================================================
::CHECK DEPENDENCIES
::=========================================================================================



::PYTHON

:: PYTHON NOT FOUND ERROR MESSAGE
:: Sets the variables for the error message that will be displayed if the Python command will not run  
SET Line1PythonErr=*********************************************************
SET Line2PythonErr=		   PYTHON CANNOT BE FOUND 
SET Line3PythonErr=Python is is either not installed or it is just
SET Line4PythonErr=not in the PATH environment variable.
SET Line5PythonErr=Download Python 3 from https://www.python.org/downloads
SET Line6PythonErr=*********************************************************

::CHECK FOR PYTHON
:: This command will display the error message above and pause & then exit if the Python command does not exist
WHERE >nul 2>nul python
IF %ERRORLEVEL% NEQ 0 ECHO %Line1PythonErr% & ECHO %Line2PythonErr% & ECHO %Line3PythonErr% & ECHO %Line4PythonErr% & ECHO %Line5PythonErr% & ECHO %Line6PythonErr% & PAUSE & EXIT


::NODEJS

::NODEJS NOT FOUND ERROR MESSAGE
:: Sets the variables for the error message that will be displayed if the node command will not run  
SET Line1NodeErr=*********************************************************
SET Line2NodeErr=		   NODEJS CANNOT BE FOUND 
SET Line3NodeErr=NodeJS is is either not installed or it is just
SET Line4NodeErr=not in the PATH environment variable.
SET Line5NodeErr=Download NodeJS from https://nodejs.org/en/
SET Line6NodeErr=*********************************************************

::CHECK FOR NODEJS
:: This command will display error message above and pause & then exit if the nodejs command does not exist
WHERE >nul 2>nul node
IF %ERRORLEVEL% NEQ 0 ECHO %Line1NodeErr% & ECHO %Line2NodeErr% & ECHO %Line3NodeErr% & ECHO %Line4NodeErr% & ECHO %Line5NodeErr% & ECHO %Line6NodeErr% & PAUSE & EXIT



::NPM

::NPM NOT FOUND ERROR MESSAGE
:: Sets the variables for the error message that will be displayed if the NPM command will not run  
SET Line1NPMErr=*********************************************************
SET Line2NPMErr=		   NPM CANNOT BE FOUND 
SET Line3NPMErr=NPM is is either not installed or it is just
SET Line4NPMErr=not in the PATH environment variable.
SET Line5NPMErr=NPM is bundled with nodejs NodeJS which can be downloaded
Set Line6NPMErr=from https://nodejs.org/en/ , however you have nodejs 
Set Line7NPMErr=installed meaning that the installation of node may of failed
SET Line8NPMErr=*********************************************************

::CHECK FOR NPM
:: This command will display error message above and pause & then exit if the npm command does not exist
WHERE >nul 2>nul npm
IF %ERRORLEVEL% NEQ 0 ECHO %Line1NPMErr% & ECHO %Line2NPMErr% & ECHO %Line3NPMErr% & ECHO %Line4NPMErr% & ECHO %Line5NPMErr% & ECHO %Line6NPMErr% & ECHO %Line7NPMErr% & ECHO %Line8NPMErr% & PAUSE & EXIT



::GULP

::GULP NOT FOUND ERROR MESSAGE
:: Sets the variables for the error message that will be displayed if the gulp command will not run
SET Line1GulpErr=*********************************************************
SET Line2GulpErr=		   GULP CANNOT BE FOUND 
SET Line3GulpErr=Gulp cannot be found.
SET Line4GulpErr=Install Gulp through `npm install --global gulp`
SET Line5GulpErr=Rememeber this requires npm which is bundled with nodejs
SET Line6GulpErr=*********************************************************


::CHECK FOR GULP
:: This command will display error message above and pause & then exit if the gulp command does not exist
WHERE >nul 2>nul gulp
IF %ERRORLEVEL% NEQ 0 ECHO %Line1GulpErr% & ECHO %Line2GulpErr% & ECHO %Line3GulpErr% & ECHO %Line4GulpErr% & ECHO %Line5GulpErr% & ECHO %Line6GulpErr% & PAUSE & EXIT

::=========================================================================================
::START SERVERS
::=========================================================================================

:: If the script has made it this far then you can be pretty sure that the user has required dependicies

ECHO STARTING TEST PYTHON SERVER...
start cmd /k "ECHO Python Test Server & python components/core/Main.py"
ECHO SUCCESSFULLY STARTED TEST SERVER

ECHO STARTING UI
START cmd /k "ECHO Frontend Node Module & cd ui & gulp serve"
ECHO SUCCESSFULLY STARTED UI
ECHO *END OF SCRIPT*
pause

