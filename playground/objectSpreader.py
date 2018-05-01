import random
import pymel.core as pm

spreaderWindow = pm.window(title="Spreader", wh=(300, 200))
layout = pm.columnLayout()
pm.button(label="Spread Selected", command="spread()")
pm.showWindow(spreaderWindow)

def spread():
    selList = pm.ls(sl=True)
    for obj in selList:
        rangeX = random.randint(-10, 10)
        rangeZ = random.randint(-10, 10)
        pm.setAttr(obj + ".translateX", rangeX)
        pm.setAttr(obj + ".translateZ", rangeZ)