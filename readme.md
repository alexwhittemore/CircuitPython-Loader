# CircuitPython Loader
This is a simple script that waits for a CIRCUITPY drive to appear, erases all files from it, then copies the contents of the ./CIRCUITPY folder.

Requires Python 3.8+

## Usage

1) Download loader.py
1) Create a folder alongside it called CIRCUITPY
1) Copy the full set of files your CircuitPython application requires (code.py, 'lib' folder, etc) into `./CIRCUITPY`
1) Run with `python3 loader.py`
1) Plug in a circuitpython board. When the drive mounts, loader.py will erase it, copy all files from `./CIRCUITPY`, eject it, and wait for another. Script will keep track of how many boards have been thusly programmed in a run, in case you're doing a big batch.