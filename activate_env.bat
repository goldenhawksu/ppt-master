@echo off
setlocal EnableExtensions

set "ROOT_DIR=%~dp0"
set "VENV_DIR=%ROOT_DIR%.venv"
set "VENV_PY=%VENV_DIR%\Scripts\python.exe"
set "VENV_ACTIVATE=%VENV_DIR%\Scripts\activate.bat"
set "PYENV_CFG=%VENV_DIR%\pyvenv.cfg"

if not exist "%VENV_PY%" goto :missing_venv
if not exist "%VENV_ACTIVATE%" goto :missing_activate
if not exist "%PYENV_CFG%" goto :missing_cfg

findstr /i /b "home =" "%PYENV_CFG%" >nul
if errorlevel 1 goto :missing_cfg

set "VENV_PYTHON_HOME="
for /f "tokens=1,* delims==" %%A in ('findstr /i /b "home =" "%PYENV_CFG%"') do (
    set "VENV_PYTHON_HOME=%%B"
)

echo [OK] uv managed venv detected:
echo   %VENV_DIR%
echo [INFO] Activating the environment for this session...
call "%VENV_ACTIVATE%"
if errorlevel 1 goto :activate_failed

echo [OK] Activated: %VENV_PYTHON_HOME%
echo [INFO] Current interpreter:
where python
echo [INFO] Python version:
python --version
echo.
echo [INFO] Use these commands from this shell:
echo   python skills\ppt-master\scripts\project_manager.py init ^<project_name^> --format ppt169
echo   python skills\ppt-master\scripts\image_gen.py --list-backends
echo   python skills\ppt-master\scripts\svg_to_pptx.py ^<project_path^>
echo.
echo [INFO] To leave the virtual environment, run:
echo   deactivate
exit /b 0

:missing_venv
echo [ERROR] The uv created .venv was not found.
echo   %VENV_PY%
echo.
echo Run this first:
echo   uv venv
echo   uv pip install -r requirements.txt
exit /b 1

:missing_activate
echo [ERROR] The venv exists, but activate.bat is missing.
echo   %VENV_ACTIVATE%
exit /b 1

:missing_cfg
echo [ERROR] The venv does not look like a uv managed environment.
echo   %PYENV_CFG%
exit /b 1

:activate_failed
echo [ERROR] Failed to activate the uv managed venv.
exit /b 1
