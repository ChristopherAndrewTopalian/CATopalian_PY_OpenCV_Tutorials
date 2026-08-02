:: CATopalian_Combine_PY_Files.bat

@echo off
:: set the output file name
set "output=main.py"

:: clear existing output file
type nul > "%output%"

:: loop through all Python files in subdirectories
for /r %%i in (*.py) do (
    :: append the content of each file to the output file
    type "%%i" >> "%output%"
)

echo "Python files combined into %output% successfully."

::::

:: Dedicated to God the Father
:: All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
:: https://github.com/ChristopherTopalian
:: https://github.com/ChristopherAndrewTopalian
:: This .bat File Combines All .py files in all folders of our project folder, into one main.py file.
:: To activate this .bat file, we double click the .bat file, while it is located in our py folder.