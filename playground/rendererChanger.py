import pymel.core as pm
import pymel.core.uitypes as pmui

modelPanelList = []

# all the editors, including hypershade and stuffs
modelEditorList = pm.lsUI(editors=True)

for editors in modelEditorList:
    print editors

for myModelPanel in modelEditorList:
	if myModelPanel.find('modelPanel') != -1: # this will give only 4 viewports
		modelPanelList.append(myModelPanel)

# get the last (perspective) viewport
modelPanelList[-1].setRendererName('vp2Renderer')
# get available renderers with getRendererList()
