#! /bin/bash
# Set this version number before running this script !!!
version=0.1.7

# generate SDK zip file
setupname=mediatek_linkit_smart_7688_
sdk_zip_name=${setupname}${version}.zip
if [[ -f  "./out/${setupname}${version}.zip" ]]; then 
    rm -f "./out/${setupname}${version}.zip"
fi

if ! [[ -e "./out" ]]; then
    mkdir "./out"
fi
zip -r "./out/${sdk_zip_name}" avr

# generate JSON repository file
python2 gen_repo_json.py $version $sdk_zip_name

# ask if the user want to update the tags
echo 'Files are generated in /out folder and version tag is added to your local git repository. To share this tag, use "git push --tags".'

