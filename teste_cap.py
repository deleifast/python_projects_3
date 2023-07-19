from __future__ import print_function
import desktopmagic
from desktopmagic.screengrab_win32 \
import(getDisplayRects,saveScreenToBmp,getScreenAsImage,getRectAsImage,getDisplaysAsImages)

""" getDisplayRects functions returns a list with all displays, in display order, like  [(0, 0, 1280, 1024), (-1280, 0, 0, 1024), (1280, -176, 3200, 1024)]  : (left, top, right, bottom)"""

screens=(getDisplayRects())

rect = getRectAsImage(screens[0]) 
