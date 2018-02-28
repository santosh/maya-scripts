import os
import maya.cmds as cmds

cmds.polyCube()
cmds.file(rename=os.path.join(os.getenv('HOME'), 'cube.ma'))
cmds.file(save=True)
