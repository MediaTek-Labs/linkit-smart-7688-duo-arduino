'''
This file generates the Arduino Board Manager .json file for SDK releases.
You will need internet connection to download the latest repostiory JSON file.
'''
import sys
import os
import hashlib
from string import Template
import json
import subprocess
import requests

TEMP_JSON_PATH = 'out\\current_version.json'
CURRENT_JSON_URL = 'http://download.labs.mediatek.com/package_mtk_linkit_smart_7688_test_index.json'
MERGED_JSON_PATH = 'out\\package_mtk_linkit_smart_7688_index.json'

def get_current_version_content(new_entry):
    '''
    load the newly generated JSON string
    and returns the platform object
    '''
    j = json.loads(new_entry)
    platforms = j['packages'][0]['platforms']
    assert len(platforms) == 1
    return j['packages'][0]['platforms'][0]

def merge_with_existing_json(new_entry):
    '''
    grabs JSON content from online repostiory and
    insert the newly generated platform object
    to its platform list
    '''
    req = requests.get(CURRENT_JSON_URL)
    repo_content = json.loads(req.text)
    platforms = repo_content['packages'][0]['platforms']
    print "how many versions (online repo):", len(platforms)

    platforms.append(get_current_version_content(new_entry))
    print "how many version(merged):", len(platforms)
    json.dump(repo_content,
              open(MERGED_JSON_PATH, 'wb'),
              sort_keys=True,
              indent=4,
              separators=(',', ': '))

def get_sdk_version_string():
    '''
    Parse input arg and gives "sanitized" version string.
    Arduino IDE does not accepts version string like "1.1.05",
    where the "05" causes problems.
    '''
    version_str = sys.argv[1]
    # fix malformed version name
    version_digits = version_str.split(".")
    arg_sdk_version = ".".join([str(int(v)) for v in version_digits])
    return arg_sdk_version

def generate_new_json_entry():
    '''
    Parse cmdline arguments and generate a new repo entry
    and return the resulting string
    '''
    arg_sdk_zip_name = sys.argv[2]
    sdk_zip_path = "out\\" + arg_sdk_zip_name

    template_str = Template(open("package_linkit_index.json.template", "rb").read())
    file_check_sum = hashlib.sha256(open(sdk_zip_path, "rb").read()).hexdigest()
    json_content = template_str.substitute(sdk_version=get_sdk_version_string(),
                                           sdk_zip_name=arg_sdk_zip_name,
                                           sdk_zip_checksum=file_check_sum,
                                           sdk_zip_size=os.stat(sdk_zip_path).st_size)
    return json_content

def tag_version():
    '''
    Add a git tag of current version
    '''
    sdk_version = get_sdk_version_string()
    if not sdk_version:
        print "SDK Version not found"
        return
    cmd = "git tag -f " + sdk_version
    print "Add git tag:", cmd
    print subprocess.check_output(cmd, shell=True)

def main():
    '''
    Generate a new JSON repo for new version,
    insert into existing repo, and update git tag
    '''
    new_entry = generate_new_json_entry()
    merge_with_existing_json(new_entry)
    tag_version()

if __name__ == '__main__':
    main()
