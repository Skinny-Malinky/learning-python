import os
import sys
import argparse
#
def write_to_file_from_cl(path, write):
    try:
        os.path.exists(path)
    except IOError as e:
        return e, 'hello in error'

    with open(path, 'wb') as open_file:
        open_file.write(write)

parser = argparse.ArgumentParser('Read from CL and write to path')

parser.add_argument('path', type=str)
parser.add_argument('write', type=str)
parser.add_argument('-u', type=str)

def clr():
    args = parser.parse_args()
    path = args.path
    write = args.write
    return path, write
    # print parser.path
    # print parser.write

if __name__ == '__main__':
    path, write = clr()
    write_to_file_from_cl(path, write)
    print 'done writing'



# if __name__ == '__main__':
#     write_to_file_from_cl()
#
#
#
#
#
#
# virtualenv
# cd to project directory
# virtualenv [name] env
# cwd -
#     - name of venv
#         - project file
# source name of venv/bin/activate
# deactivate
# (name of venc)path-to-cwd:~
# pip install requests
# requirements.txt
# pip install requirements.txt
