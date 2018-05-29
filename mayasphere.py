import pymel.core as pm
from mayaGeom import MayaGeom


class MayaSphere(MayaGeom):
    """Sphere class inherited from MayaGeom."""
    def __init__(self, name='Sphere', **kwargs):
        super(MayaSphere, self).__init__()

        kwargs['name'] = name
        kwargs['object'] = True

        self._create(kwargs)

    def __del__(self):
        self.delete()

    def __str__(self):
        return self.name

    def _create(self, opts={}):
        parts = pm.sphere(**opts)
        self.name = parts[0]

    def delete(self):
        if self.exists():
            pm.delete(self.name)

    def exists(self):
        return pm.objExists(self.name)

    def setTranslation(self, x=None, y=None, z=None):
        self._doTransform(pm.move, x, y, z)

    def getRotation(self):
        return pm.xform(self.name, q=1, ro=1)  # ro=rotation

    def setRotation(self, x=None, y=None, z=None):
        self._doTransform(pm.rotate, x, y, x)

    def getScale(self):
        return pm.xform(self.name, q=1, scale=1)

    def setScale(self, x=None, y=None, z=None):
        self._doTransform(pm.scale, x, y, z)

    def _doTransform(self, func, x, y, z):
        for name in ('x', 'y', 'z'):
            val = locals()[name]
            if val is not None:
                opts = {name: True, 'objectSpace': True, 'absolute': True}
                func(val, self.name, **opts)


class PolySphere(MayaSphere):

    def __init__(self, name="PolySphere", **kwargs):
        MayaSphere.__init__(self, name, **kwargs)

    def _create(self, opts={}):
        parts = pm.polySphere(**opts)
        self.name = parts[0]