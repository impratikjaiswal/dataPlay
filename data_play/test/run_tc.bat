@echo off
echo Iteration 2
@echo on
@echo off
echo Time Stamp is: %DATE% %TIME%
echo %USERNAME%
echo %USERDOMAIN%
ver
@echo on
@echo off
pushd %~dp0
echo.
echo.
echo.
echo.
echo "cli_--help"

cd ..
cd ..
if not exist "data_play/test/logs/" MD "data_play/test/logs/"
cd scripts
call activate_vir_env.bat
cd ..
python -m data_play.main.dataplay --help > data_play\test\logs\cli_--help.log
cd scripts
call deactivate_vir_env.bat
cd ..
echo.
echo.
echo.
echo.
echo "Batch Execution Done"

@echo on