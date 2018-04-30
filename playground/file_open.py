import os
import maya.cmds as cmds

cmds.file(os.path.join(os.getenv('HOME'), 'cube.ma'), open=True)
