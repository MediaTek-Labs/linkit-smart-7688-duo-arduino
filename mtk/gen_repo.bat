:: !!! Set this version number before running this script !!!
set version=0.1.7

:: generate SDK zip file
set setupname=mediatek_linkit_smart_7688_
set sdk_zip_name=%setupname%%version%.zip
IF EXIST ".\out\%setupname%%version%.zip" del /F /Q ".\out\%setupname%%version%.zip"
IF NOT EXIST ".\out" mkdir out
7z.exe a ".\out\%sdk_zip_name%" ".\avr"

:: generate JSON repository file
python.exe gen_repo_json.py %version% %sdk_zip_name%

:: ask if the user want to update the tags
echo "Files are generated in /out folder and version tag is added to your local git repository. To share this tag, use 'git push --tags'."