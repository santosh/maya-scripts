from mayaGeom import MayaGeom

class MayaSphere(MayaGeom):
    """docstring for MayaSphere."""
    def __init__(self, name='MayaSphere'):
        super(MayaSphere, self).__init__()

        parts = pm.sphere(name=name, object=True, radius=1.0)
        self.name = parts[0]
