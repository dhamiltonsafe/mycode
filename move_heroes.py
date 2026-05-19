#!/usr/bin/env python3
"""Move and rename files with shutil"""

import shutil
import os

def main():
    """Main Logic"""
    os.chdir("/home/student/mycode")
    shutil.move("raynor.obj", "battlecruiser/")
    xname = input("What is the new name for kerrigan.obj? ")
    if os.path.exists(battlecruiser/{xname}):
        yn = str(input("A file with that name already exists.  Do you wish to overwrite?"))
        if yn=="y":
        shutil.move("battlecruiser/kerrigan.obj", f"battlecruiser/{xname}")

main()

