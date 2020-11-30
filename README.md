# No-Intro RomSet Organizer
Sorts roms that follow the No-Intro naming convention into regional and alphanumeric folders

## Introduction
This script was created for those looking to quickly organize their personally dumped roms that follow the No-Intro naming conventions into regional and alphanumeric folders.  The format of these files are as follows:
> 'ROM NAME (REGION).extension'

Running this script will parse the region specified in the paranthesis from the filename and sort it into a folder with that region name.  The currently supported regions can be seen in the 'countries' list in the script, and more can be added to that list for missing regions.

## Instructions
After installing Python, download and place the 'organize.py' script directly into the folder with your unorganized roms.  Running the script will prompt the user to input a value corresponding to whether they'd like to COPY or MOVE the files into the new directories.  COPYING files is recommended, as MOVING files will result in files with multiple region tags being moved to only one directory.  After choosing an option, the script will create new region folders in the current directory, move or copy each file into the appropriate folder(s), and remove any unused folders that were created during the process.
