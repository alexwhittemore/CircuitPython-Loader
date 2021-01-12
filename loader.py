""" loader.py waits for a CIRCUITPY drive to appear, erases it, copies the contents of ./CIRCUITPY to it, and waits for another. """
import os
import time
import platform
import shutil

DRIVE_NAME = "CIRCUITPY"        # Look for a drive named CIRCUITPY to load
SOFTWARE_DIR = "./CIRCUITPY"    # Load files from a local directory also called CIRCUITPY

if platform.system() == "Darwin":
    TARGET_DIR = f"/Volumes/{DRIVE_NAME}" 
    def eject_command():
        ''' Eject the drive however works right for the system '''
        os.popen(f"""osascript -e 'tell application "Finder" to eject "{DRIVE_NAME}"'""")
else:
    print("Only MacOS is supported at the moment, sorry.")
    exit()

print("Waiting for CircuitPython device...")

PROG_COUNT = 0
while True:
    # time.sleep(.2) # Let the thread do some other stuff I mean come on.
    if os.path.isdir(TARGET_DIR):
        print(f"Found {TARGET_DIR}")
        print(f"Copying {SOFTWARE_DIR}")
        # The rmtree and copytree operations aren't blocking, so it's not always the case that the
        # drive is READY for what we're about to do. TRY the operation until it succeeds. 
        while True:
            try:
                shutil.rmtree(TARGET_DIR, ignore_errors=True)
                break
            except shutil.Error:
                pass
        while True:
            try:
                shutil.copytree(SOFTWARE_DIR, TARGET_DIR, dirs_exist_ok=True)
                break
            except shutil.Error:
                pass
        print("Ejecting")
        eject_command()
        # Block until the drive is actually ejected.
        while os.path.isdir(TARGET_DIR):
            pass
        PROG_COUNT += 1
        print(f"Done - Programmed {PROG_COUNT}")
