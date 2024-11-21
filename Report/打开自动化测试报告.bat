@echo  off  
echo  %~dp0

start  ""  %~dp0\..\Tools\allure-2.27.0\bin\allure open %~dp0\report_allure
pause