class MayaGeom(object):
    """docstring for MayaGeom."""
    def __init__(self, name="Geometry"):
        self.name = name

    def setName(self, name):
        if name:
            self.name = pm.rename(self.name, name)

    def getTranslation(self):
        return pm.xform(self.name, query=True, translation=True)

    def setTranslation(self, x=None, y=None, z=None):
        if x is None:
            pm.move(x, self.name, x=True, objectSpace=True, absolute=True)
        if y is None:
            pm.move(y, self.name, y=True, objectSpace=True, absolute=True)
        if z is None:
            pm.move(z, self.name, z=True, objectSpace=True, absolute=True)
