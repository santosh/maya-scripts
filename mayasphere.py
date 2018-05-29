import pymel.core as pm
from mayaGeom import MayaGeom

class MayaSphere(MayaGeom):
    """Sphere class inherited from MayaGeom."""
    def __init__(self, name='Sphere', **kwargs):
        super(MayaSphere, self).__init__()

        kwargs['name'] = name
        kwargs['object'] = True

        parts = pm.sphere(**kwargs)
        self.name = parts[0]

    def setTranslation(self, x=None, y=None, z=None):
        for name in ('x', 'y', 'z'):
            val = locals()[name]
            if val is not None:
                opts = {name: True, 'objectSpace': True, 'absolute': True}
                pm.move(val, self.name, **opts)

    def getRotation(self):
        return pm.xform(self.name, q=1, ro=1)  # ro=rotation

    def setRotation(self, x=None, y=None, z=None):
        for name in ('x', 'y', 'z'):
            val = locals()[name]
            if val is not None:
                opts = {name: True, 'objectSpace': True, 'absolute': True}
                pm.rotate(val, self.name, **opts)

    def getScale(self):
        return pm.xform(self.name, q=1, scale=1)

    def setScale(self, x=None, y=None, z=None):
        for name in ('x', 'y', 'z'):
            val = locals()[name]
            if val is not None:
                opts = {name: True, 'objectSpace': True, 'absolute': True}
                pm.scale(val, self.name, **opts)
