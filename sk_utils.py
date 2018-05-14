import os
import maya.cmds as cmds

def createSphereSpiral(no_of_spheres):
    for i in range(no_of_spheres):
        sphere = cmds.sphere(name="SpiralSphere#", pivot=[3, i*(0.5), 0])
        cmds.setAttr(sphere[0] + ".rotateY", i*30)



def texturePathFixer():
    print "Info: set project before executing"

    fileNodes = cmds.ls(type="file", long=True)

    for f in fileNodes:
        oldTexturePath = cmds.getAttr(f + ".fileTextureName")
        # use os module for compat, and not string.split()
        newTexturePath = os.path.join("textures", os.path.split(oldTexturePath)[-1])
        print "Old:", oldTexturePath
        print "New:", newTexturePath
        cmds.setAttr(f + ".fileTextureName", newTexturePath, type="string")


def gainLights(gain):
    """
    Changes the intensity of the available lights at once.
    """
    # select all lights
    lights = cmds.ls(lights=True)
    cmds.select(lights)

    for light in lightsList:
        oldInten = cmds.getAttr(light + ".intensity")
        newInten = oldInten * gain
        cmds.setAttr(light + ".intensity", newInten)
        print light, "Old: ", oldInten, "New: ", newInten