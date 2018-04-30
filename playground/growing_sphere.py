import maya.cmds as cmds

class GrowingSphere(object):
	def __init__(self):
		self.sphere = cmds.polySphere(n="sphere")[0]

	def grow(self):
		scaleX = cmds.getAttr("{}.scaleX".format(self.sphere))
		scaleZ = cmds.getAttr("{}.scaleZ".format(self.sphere))
		newScaleX = scaleX * 1.5
		newScaleX = scaleX * 1.5
		cmds.setAttr("{}.scaleX".format(self.sphere, newScaleX))
		cmds.setAttr("{}.scaleZ".format(self.sphere, newScaleZ))


testSphere1 = GrowingSphere()
testSphere2 = GrowingSphere()

testSphere1.grow()
testSphere2.grow()