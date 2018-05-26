from __future__ import absolute_import, unicode_literals, print_function
import os
import pymel.core as pm
import maya.cmds as cmds


def texturePathFixer():
    # TODO: Make it pymel (OO, replace setAttr with set)
    print("Info: set project before executing")

    file_nodes = cmds.ls(type="file", long=True)

    for f in file_nodes:
        old_texture_path = cmds.getAttr(f + ".fileTextureName")
        # use os module for compat, and not string.split()
        new_texture_path = os.path.join("textures", os.path.split(old_texture_path)[-1])
        print("Old:", old_texture_path)
        print("New:", new_texture_path)
        cmds.setAttr(f + ".fileTextureName", new_texture_path, type="string")


def gainLights(gain):
    """
    Changes the intensity of the available lights at once.

    Multiplies the value of gain, into the intensity of every
    light in the scene.
    """
    # select all lights

    lights = pm.ls(lights=True)
    pm.select(lights)

    for light in lights:
        old_inten = light.get("intensity")
        new_inten = old_inten * gain
        cmds.setAttr(light + ".intensity", new_inten)
        print(light, "Old: ", old_inten, "New: ", new_inten)