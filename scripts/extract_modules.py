import sys, os
from pathlib import Path

# True only if the SDK is built using the default configurations of setup_project.bat. 
# If not, change the path to the directory that leads to this file structure
# <sdk-folder>
#   +-- aditof.dll
#   +-- aditof.exp
#   +-- aditof.lib

TOF_SDK_PATH = Path(__file__).parent.parent / 'ToF' / 'scripts' / 'windows' / 'build' / 'sdk' / 'Release'

TOF_PYTHON_BINDINGS_PATH = Path(__file__).parent.parent / "ToF" / 'scripts' / 'windows' / 'build' / 'bindings' / 'python' / 'Release'

MODULES_PATH =  Path(__file__).parent.parent / 'modules'

LIBS_PATH = Path(__file__).parent.parent / 'libs'

if __name__ == "__main__":
    import shutil

    # TEST SDK CONTENTS
    contents = set(['aditof.dll', 'aditof.exp', 'aditof.lib'])
    if contents.issubset(set(os.listdir(TOF_SDK_PATH))):
        print("Valid SDK contents")
    else:
        print("Invalid SDK contents")

    for file in os.listdir(TOF_SDK_PATH):
        shutil.copy2(TOF_SDK_PATH / file, MODULES_PATH / file)

    for file in os.listdir(TOF_PYTHON_BINDINGS_PATH):
        shutil.copy2(TOF_PYTHON_BINDINGS_PATH / file, MODULES_PATH / file)

    for file in os.listdir(LIBS_PATH):
        shutil.copy2(LIBS_PATH / file, MODULES_PATH / file)
