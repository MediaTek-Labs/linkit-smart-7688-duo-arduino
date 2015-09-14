from string import Template
import sys
import os
import hashlib


def main():
    version_str = sys.argv[1]
    
    # fix malformed version name
    version_digits = version_str.split(".")
    arg_sdk_version = ".".join([str(int(v)) for v in version_digits])
    
    arg_sdk_zip_name = sys.argv[2]

    sdk_zip_path = "out\\" + arg_sdk_zip_name

    s = Template(open("package_linkit_index.json.template", "rb").read())
    jsonContent = s.substitute(sdk_version=arg_sdk_version,
                 sdk_zip_name=arg_sdk_zip_name,
                 sdk_zip_checksum=hashlib.sha256(open(sdk_zip_path, "rb").read()).hexdigest(),
                 sdk_zip_size=os.stat(sdk_zip_path).st_size)
    f = open("out\\package_mtk_linkit_smart_7688_index.json", "wb")
    f.write(jsonContent)
    f.close
    f = None

if __name__ == '__main__':
    main()
