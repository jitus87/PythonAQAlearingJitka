# import class Path from pathlib module

from pathlib import Path
# Absolute path = on harddrive
# c:\Program Files\users

# Relative path = here in pycharm, any directory

path = Path()  # current directory (practice_from_video)
# path = Path("ecommerce") - directory ecommerce

print(path.exists())   # checks if the path exists
# path.mkdir()     make directory - create new
# path.rmdir()     remove directory

for file in path.glob("*.py"):         # search all files .py in whole directory
    print(file)
