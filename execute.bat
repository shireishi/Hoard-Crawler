@echo off
set py_location="./Scripts/python.exe"
%py_location% -c "import sys;sys.path.append('../');from main import Main;Main()"
pause