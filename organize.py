import os
import fnmatch
import shutil
from pathlib import Path
import string

basepath = os.getcwd()

# The 'countries' list defines the initial directories to make, while the 'alphaCategories' list defines the
# alphanumeric categories within each region.  Adding new values to the 'countries' list will allow you to sort
# any regions not included here.
countries = ('USA', 'Japan', 'Europe', 'Asia', 'Spain', 'Germany', 'Brazil', 'World', 'Unknown', 'Australia', 'Korea', 'France', 'Italy', 'Canada', 'Sweden', 'China', 'Taiwan', 'Netherlands', 'Mexico', 'Russia', 'Argentina', 'Hong Kong')
alphaStrings = ('\'0123456789', 'AaBbCcDdEeFf', 'GgHhIiJjKk', 'LlMmNnOoPp', 'QqRrSsTtUu', 'VvWwXxYyZz')
alphaCategories = ('0 - 9', 'A - F', 'G - K', 'L - P', 'Q - U', 'V - Z')

selection=0
while (selection<1) or (selection>2):
    print("Before using this script, make sure it's located in the directory with the unorganized roms.")
    print("Current path: " + basepath)
    print("")
    print("Select an option by inputting a number and pressing enter")
    print("1 - COPIES files into new directories in the current working directory")
    print("2 - MOVES files into new directories in the current working directory")
    print(" ")
    print("    WARNING - MOVING files will result in files with multiple region tags only being moved to one directory.")
    print("              The MOVE file option should only be used with sets that have one region tag per file.")
    print("")
    selection=int(input("Input your selection: ")) 

# Creates the initial region directories
for i in countries:
    try:
        os.mkdir(i)
    except FileExistsError as err:
        print(i + " already exists, skipping")

# Creates the alphanumeric ranges within each region
for i in countries:
    for z in alphaCategories:
        try:
            os.mkdir(os.path.join(i, z))
        except FileExistsError as err:
            print(z + " already exists in " + i + ", skipping")

# For each region and alphanumeric range, checks each file's name and sorts into the correct directory
for i in countries:
    for file_name in os.listdir(basepath):
        if fnmatch.fnmatch(file_name, '*(*{}*)*'.format(i)):
            for z in alphaStrings:
                if any(file_name.startswith(x) for x in z):
                    if selection==1:
                        print('Copying ' + file_name + " to " + z + " in " + i)
                        try:
                            shutil.copy(file_name, os.path.join(os.path.join(basepath, i), alphaCategories[alphaStrings.index(z)]))
                        except FileExistsError as err:
                            print(file_name + " already exists in sorted folder, skipping")
                    elif selection==2:
                        print('Moving ' + file_name + " to " + z + " in " + i)
                        try:
                            shutil.move(file_name, os.path.join(os.path.join(basepath, i), alphaCategories[alphaStrings.index(z)]))
                        except FileExistsError as err:
                            print(file_name + " already exists in sorted folder, skipping")

# First removes empty alphanumeric range directories, followed by empty region directories
for i in countries:
    for z in alphaCategories:
        try:
            os.rmdir(os.path.join(os.path.join(basepath, i), z))
        except Exception as err:
            print(os.path.join(os.path.join(basepath, i), z) + " not empty, skipping")
    try:
        os.rmdir(os.path.join(basepath, i))
    except Exception as err:
        print(os.path.join(basepath, i) + " not empty, skipping")