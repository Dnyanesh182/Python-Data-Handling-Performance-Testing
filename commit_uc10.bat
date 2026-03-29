@echo off
echo ================================================
echo UC10 - Clean Commit Script
echo ================================================

cd /d "c:\Users\Dnyaneshwar\Desktop\Test\Python-Data-Handling-Performance-Testing"

echo.
echo === Checking Git Status ===
git status

echo.
echo === Adding All Files ===
git add .

echo.
echo === Showing What Will Be Committed ===
git status

echo.
echo === Creating Commit ===
git commit -m "refactor: modularize file handling and testing into reusable utility modules with clean architecture" -m "UC10 - Refactor file handling and testing logic using clean code and reusable utility modules" -m "Changes:" -m "- Create file_utils.py for CSV/JSON file I/O operations with FileReader, FileWriter, and DataConverter classes" -m "- Create algorithms.py with SearchAlgorithms, SortAlgorithms, and DataAnalyzer classes" -m "- Create performance_utils.py for benchmarking with PerformanceTimer, Benchmarker, and DatasetGenerator" -m "- Create data_loader.py for application-specific data loading integration" -m "- Update data_processing_and_testing.py to use modular architecture" -m "- Add demo_refactored_modules.py demonstrating all features" -m "- Add test_refactored_modules.py with comprehensive unit tests" -m "- Update README.md with complete documentation" -m "- Add REFACTORING_SUMMARY.md documenting the refactoring process" -m "- Update requirements.txt with pytest and development tools" -m "" -m "Benefits:" -m "- Clean code following SOLID principles" -m "- Reusable utility modules" -m "- Comprehensive documentation and type hints" -m "- Proper error handling" -m "- 50+ test cases covering all modules"

echo.
echo === Pushing to Remote ===
git push origin UC10-refactor-utils-testing

echo.
echo ================================================
echo Commit Complete!
echo ================================================
pause
