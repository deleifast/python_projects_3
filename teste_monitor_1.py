import os
import os.path

import mss


def on_exists(fname):
    # type: (str) -> None
    """
    Callback example when we try to overwrite an existing screenshot.
    """

    if os.path.isfile(fname):
        newfile = fname + ".old"
        print("{} -> {}".format(fname, newfile))
        os.rename(fname, newfile)


with mss.mss() as sct:
    filename = sct.shot(output="mon-{mon}.png", callback=on_exists)
    print(filename)
