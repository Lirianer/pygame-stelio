import cx_Freeze
import os

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Stelio",                 # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]Stelio.exe",  # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     ),
                  
    ("StartupShortcut",        # Shortcut
     "StartupFolder",          # Directory_
     "Stelio",                 # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]Stelio.exe",  # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     ),

    ]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

executables = [
    cx_Freeze.Executable(
        "main.py",
        base="Win32GUI",
        targetName="Stelio.exe",
        shortcutDir=shortcut_table,
        icon="stelio.ico"
    )
]
os.environ['TCL_LIBRARY'] = r'C:\\Users\\Gabriel\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\\Users\\Gabriel\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6'

cx_Freeze.setup(
    name = "Stelio",
    options = {
        "build_exe": {
                "packages": ["pygame", "random", "game"],
                "includes": ["game", "api"],
                "include_files": [
                    "assets"
                ]
            },
        "bdist_msi": {
            "data": msi_data
        }
    },
    executables = executables,
    version = "0.0.1"

    )