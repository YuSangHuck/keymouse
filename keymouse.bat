@echo off
setlocal

set PROCESS_NAME=keymouse.exe
set DIST_DIR=%~dp0dist

:: Check if the process is running
tasklist /FI "IMAGENAME eq %PROCESS_NAME%" | find /I "%PROCESS_NAME%" >nul
if %ERRORLEVEL% EQU 0 (
    echo Process %PROCESS_NAME% is running. Terminating all instances...
    :: Terminate all instances of the process
    taskkill /F /IM %PROCESS_NAME%
) else (
    echo Process %PROCESS_NAME% is not running. Starting it...
    :: Start the process from the dist directory
    start "" "%DIST_DIR%\%PROCESS_NAME%"
)

endlocal