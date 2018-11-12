import cx_Freeze
import sys # Imports are automatically detected (normally) in the script to freeze
import os 

base = None 

os.environ["TCL_LIBRARY"] = "C:\\python3.6\\tcl\\tcl8.6"
os.environ["TK_LIBRARY"]
= "C:\\python3.6\\tcl\\tk8.6"

if sys.platform=='win32':
    base = "Win32GUI"
a=cx_Freeze.Executable("bakchodi.py")

executables = [a]

packages = ["tkinter"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

cx_Freeze.setup(
        name = "Molly",
        options = options,
        version="2.0",
        executables=executables)
