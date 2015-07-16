__author__ = "Timo Hanisch"
__version__ = "1.0.0"
__maintainer__ = "Timo Hanisch"
__email__ = "timohanisch@gmail.com"
__version__ = "1.0.0"

import sys
import os
import zipfile
import re


def extract_csv(path, zip_file, regex):
    for root, dirs, files in os.walk(path):
        for f in files:
            if re.match(regex, f):
                root_path = os.path.join(root, f)
                rel_path = os.path.relpath(root_path, path)
                zip_file.write(os.path.join(root, f), rel_path)


def main(path, zip_file_name, regex='.*'):
    zip_file = zipfile.ZipFile(zip_file_name + '.zip', 'w')
    extract_csv(path, zip_file, regex)
    zip_file.close()


if __name__ == '__main__':
	if len(sys.argv) < 3:
		print sys.argv
		print 'Usage of csv2zip: path2zip "<path>" "<name>" ["<regex>"]'
		print '\t<path>: The path of the root folder to zip'
		print '\t<name>: The name of the zip file to create'
		print '\t<regex> (optional): A regex which is matched against all files found in the path\n' \
		  '\tand its sub folders. By default all files (.*) are written to the zip file'
		sys.exit(-1)
	elif len(sys.argv) < 4:
		sys.exit(main(sys.argv[1], sys.argv[2]))
	else:
		sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
