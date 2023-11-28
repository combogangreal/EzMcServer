"""
Copyright (c) 2023 Combo Gang. All rights reserved.

This work is licensed under the terms of the MIT license.  
For a copy, see <https://opensource.org/licenses/MIT>.
"""
import os
from src.gui import master
from sys import platform
from time import sleep

if platform == "win32":
    os.system("pip install -r requirements.txt")
else:
    os.system("pip3 install -r requirements.txt")
sleep(1)

master.mainloop()