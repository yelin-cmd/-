@echo off
setlocal

if "%~1"=="" (
  echo Drag an audio file onto this script, or pass the audio path as an argument.
  echo.
  echo Example:
  echo transcribe_audio.bat "C:\path\to\audio.m4a"
  pause
  exit /b 1
)

set "SCRIPT_DIR=%~dp0"
set "PYTHON_EXE=C:\Users\yelin01\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"

"%PYTHON_EXE%" "%SCRIPT_DIR%transcribe_audio.py" "%~1"
set "EXIT_CODE=%ERRORLEVEL%"

if not "%EXIT_CODE%"=="0" (
  echo.
  echo Transcription failed. Check the model, audio file, and ffmpeg path.
  pause
  exit /b %EXIT_CODE%
)

echo.
echo Transcription finished.
pause
