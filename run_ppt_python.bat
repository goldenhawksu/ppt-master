@echo off
setlocal EnableExtensions

set "ROOT_DIR=%~dp0"
set "VENV_DIR=%ROOT_DIR%.venv"
set "VENV_PY=%VENV_DIR%\Scripts\python.exe"
set "PYENV_CFG=%VENV_DIR%\pyvenv.cfg"

if not exist "%VENV_PY%" goto :missing_venv
if not exist "%PYENV_CFG%" goto :missing_cfg

findstr /i /b "home =" "%PYENV_CFG%" >nul
if errorlevel 1 goto :missing_cfg

"%VENV_PY%" %*
exit /b %errorlevel%

:missing_venv
echo [ERROR] The uv created .venv was not found.
echo   %VENV_PY%
echo.
echo Run this first:
echo   uv venv
echo   uv pip install -r requirements.txt
exit /b 1

:missing_cfg
echo [ERROR] The venv does not look like a uv managed environment.
echo   %PYENV_CFG%
exit /b 1
