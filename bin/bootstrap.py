from __future__ import print_function, division, absolute_import, \
with_statement, unicode_literals
import sys
import logging

logging.basicConfig(
	# need time data? : %(asctime)s
    format='%(levelname)s: %(lineno)d %(funcName)s [%(thread)d] %(message)s',
    level=logging.INFO
    )

# import the maya things
sys.path.append("C:\\Program Files\\Autodesk\\Maya2016\\Python\\Lib\\site-packages")

logging.info("importing maya")
import maya.cmds
logging.info("importing pymel")
import pymel
logging.info("importing PySide")
import PySide