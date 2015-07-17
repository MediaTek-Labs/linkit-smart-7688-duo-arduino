::init value
set version=0.1.1

set setupname=mediatek_linkit_smart_7688_
set sdk_zip_name=%setupname%%version%.zip

del .\out\%setupname%%version%.zip /q
mkdir out

7z.exe a ".\out\%sdk_zip_name%" ".\avr"

:: generate JSON repository file
python.exe gen_repo_json.py %version% %sdk_zip_name%
