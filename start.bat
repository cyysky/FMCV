cd %~dp0
setx PYTHONPYCACHEPREFIX %temp%
echo %PYTHONPYCACHEPREFIX%
start "AI" /realtime cmd /k python run.py
