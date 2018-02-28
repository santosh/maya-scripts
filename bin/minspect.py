import sys
import pymel.core as pmc

def syspath():
	print('sys.path:')
	for p in sys.path:
		print(' ' + p)

def info(obj):
	"""Prints information about the object."""
	lines = ['Info for {}'.format(obj.name()), 'Attributes:']
	# Get the name of all attributes
	for a in obj.listAttr():
		lines.append(' ' + a.name())
	lines.append('Mel type: {}'.format(obj.type()))
	lines.append('MRO: ')
	lines.extend([' ' + t.__name__ for t in type (obj).__mro__])
	result = '\n'.join(lines)
	print result

def pyto_helpstr(obj):
	if isinstance(obj, basestring):
		return 'search.html?q={}'.format(obj.replace(' ', '+'))
	return None

def testpyto_helpstr():
	def dotest(obj, ideal):
		result = pyto_helpstr(obj)
		assert result == ideal, '{} != {}'.format(result, ideal)
	dotest('maya rocks', 'search.html?q=maya+rocks')
	dotest(pmc.nodetypes,
		'generated/pymel.core.nodetypes.html'
		'#module-pymel.core.nodetypes')
	dotest(pmc.nodetypes.Joint,
		'generated/classes/pymel.core.nodetypes/'
		'pymel.core.nodetypes.Joint.html'
		'#pymel.core.nodetypes.Joint')
	dotest(pmc.nodetypes.Joint(),
		'generated/classes/pymel.core.nodetypes/'
		'pymel.core.nodetypes.Joint.html'
		'#pymel.core.nodetypes.Joint')
	dotest(pmc.nodetypes.Joint().getTranslation,
		'generated/classes/pymel.core.nodetypes/'
		'pymel.core.nodetypes.Joint.html'
		'#pymel.core.nodetypes.Joint.getTranslation')
	dotest(pmc.joint,
		'generated/functions/pymel.core.animation/'
		'pymel.core.animation.joint.html'
		'#pymel.core.animation.joint')