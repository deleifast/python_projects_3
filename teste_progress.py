import time
from tqdm import *

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    time.sleep(.5)
    pbar.set_description("Processing %s" % char)