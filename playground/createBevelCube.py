import pymel.core as pm


polyToBevel = pm.polyCube(w=1, h=1, d=1, sx=1, sy=1, sz=1, ax=(0,1,0), cuv=4, ch=1)
pm.scale(3.208979, 3.208979, 3.208979, r=True)
pm.polyBevel(polyToBevel[0], fraction=0.3, offsetAsFraction=1, autoFit=1,
            segments=1, worldSpace=1, smoothingAngle=30, fillNgons=1, mergeVertices=1,
            mergeVertexTolerance=0.0001, miteringAngle=180, angleTolerance=180, ch=1)

# create slider to select bevel fraction value