import os
from fnmatch import fnmatch

pattern = ".DS_Store"

for path, subdirs, files in os.walk('.'):
    for name in files:
        if fnmatch(name, pattern):
            os.remove(os.path.join(path, name))

print("All .DS_Store files removed!")

for path, subdirs, files in os.walk('./video'):
    for name in files:
        if fnmatch(name, pattern):
            print os.path.join(path, name)