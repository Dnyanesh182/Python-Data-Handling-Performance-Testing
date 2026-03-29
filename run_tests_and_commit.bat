@echo off
cd /d "c:\Users\Dnyaneshwar\Desktop\Test\Python-Data-Handling-Performance-Testing"

echo === Running pytest ===
python -m pytest test_algorithms.py -v
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Pytest failed or not installed. Installing pytest...
    python -m pip install pytest
    echo.
    echo Running pytest again...
    python -m pytest test_algorithms.py -v
)

echo.
echo === Git Operations ===
git add .
git status
echo.
git commit -m "test: implement unit testing using pytest for search algorithms with edge case coverage"
echo.
git push origin UC9-unit-testing-pytest

echo.
echo === Done ===
pause
