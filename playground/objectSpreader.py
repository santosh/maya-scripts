import random
import pymel.core as pm

if pm.window(spreaderWindow, exists=True):
    pm.deleteUI(spreaderWindow)

spreaderWindow = pm.window(title="Spreader", wh=(200, 100))
layout = pm.columnLayout()
pm.button(label="Spread Selected", command="spread()")
pm.showWindow(spreaderWindow)


def spread():
    selList = pm.ls(sl=True)
    for obj in selList:
        rangeX = random.uniform(-10.0, 10.0)
        rangeZ = random.uniform(-10.0, 10.0)
        obj.setAttr('translateX', rangeX)
        obj.setAttr('translateZ', rangeZ)

