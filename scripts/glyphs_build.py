# -*- coding: utf-8 -*-
from __future__ import division

from GlyphsApp import GSGlyph, GSInstance, GSNode, GSPath

from settings import fs_target_upm, sf_upm

delete_glyphs = ["uniE000", "uniE001", "uniE002", "uniE003"]

apple = [[((291, -22), "offcurve"), ((313, -16), "offcurve"), ((341, -5), "curve"), ((367, 6), "offcurve"), ((391, 11), "offcurve"), ((413, 11), "curve"), ((434, 11), "offcurve"), ((459, 6), "offcurve"), ((488, -4), "curve"), ((517, -15), "offcurve"), ((541, -20), "offcurve"), ((559, -20), "curve"), ((602, -20), "offcurve"), ((645, 12), "offcurve"), ((688, 77), "curve"), ((716, 120), "offcurve"), ((736, 162), "offcurve"), ((749, 202), "curve"), ((674, 230), "offcurve"), ((635, 299), "offcurve"), ((635, 372), "curve"), ((635, 445), "offcurve"), ((670, 497), "offcurve"), ((725, 540), "curve"), ((682, 594), "offcurve"), ((632, 622), "offcurve"), ((566, 622), "curve"), ((542, 622), "offcurve"), ((513, 616), "offcurve"), ((479, 605), "curve"), ((445, 594), "offcurve"), ((421, 588), "offcurve"), ((408, 588), "curve"), ((397, 588), "offcurve"), ((374, 593), "offcurve"), ((339, 603), "curve"), ((304, 613), "offcurve"), ((275, 618), "offcurve"), ((250, 618), "curve"), ((125, 618), "offcurve"), ((51, 501), "offcurve"), ((51, 359), "curve"), ((51, 276), "offcurve"), ((76, 192), "offcurve"), ((125, 107), "curve"), ((174, 21), "offcurve"), ((224, -22), "offcurve"), ((275, -22), "curve"), ], [((439, 611), "offcurve"), ((463, 617), "offcurve"), ((500, 652), "curve"), ((541, 695), "offcurve"), ((569, 755), "offcurve"), ((558, 811), "curve"), ((441, 784), "offcurve"), ((395, 707), "offcurve"), ((394, 608), "curve")]]

notdef = [[((450, 0), "line"), ((450, 696), "line"), ((50, 696), "line"), ((50, 0), "line"), ], [((101, 650), "line"), ((399, 650), "line"), ((399, 46), "line"), ((101, 46), "line")]]


def setNames(font):
	font.familyName      = "System Font"
	font.copyright       = u"Digitized data copyright © 2012-2015, The Mozilla Foundation and Telefonica S.A. System Font Replacement version 2015-2016 by Jens Kutilek."
	font.designerURL     = "http://www.carrois.com/"
	font.manufacturer    = "Jens Kutilek"
	font.manufacturerURL = "http://www.kutilek.de/"
	font.customParameters["vendorID"] = "jens"

def setUPM(font):
	if font.upm != fs_target_upm:
		try:
			font.upm = fs_target_upm
		except:
			font.setUnitsPerEm_(fs_target_upm)

def drawPathsInLayer(layer, paths, clear=True):
	scale = fs_target_upm / 984
	if clear:
		layer.paths = []
	for path in paths:
		p = GSPath()
		for node in path:
			n = GSNode(* node)
			n.x = int(round(n.x * scale))
			n.y = int(round(n.y * scale))
			p.nodes.append(n)
		p.closed = True
		layer.paths.append(p)

def fixNotdef(font):
	font.disableUpdateInterface()
	n = font.glyphs[".notdef"]
	for i in range(len(font.masters)):
		layer = n.layers[i]
		layer.width = int(round(500 * fs_target_upm / 984))
		drawPathsInLayer(layer, notdef)
	font.enableUpdateInterface()

def fixAppleLogo(font):
	font.disableUpdateInterface()
	font.glyphs["apple"] = GSGlyph("apple")
	a = font.glyphs["apple"]
	for i in range(len(font.masters)):
		layer = a.layers[i]
		layer.width = int(round(790 * fs_target_upm / 984))
		drawPathsInLayer(layer, apple)
	font.enableUpdateInterface()

def normalizeList(the_list, factor, do_round=True):
	if do_round:
		return [int(round(element * factor)) for element in the_list]
	else:
		return [element * factor for element in the_list]

def deleteGlyphs(font):
	font.disableUpdateInterface()
	for glyph_name in delete_glyphs:
		del(font.glyphs[glyph_name])
	font.enableUpdateInterface()

def setVerticalMetrics(instance):
	
	metrics = normalizeList([
		1980,
		-432,
	], fs_target_upm / sf_upm)
	
	# hhea
	instance.customParameters["hheaAscender"]  =   metrics[0]
	instance.customParameters["hheaDescender"] =   metrics[1]
	instance.customParameters["hheaLineGap"]   =   0
	# OS/2
	instance.customParameters["typoAscender"]  =   metrics[0]
	instance.customParameters["typoDescender"] =   metrics[1]
	instance.customParameters["typoLineGap"]   =   0
	# Win
	instance.customParameters["winAscent"]     =   metrics[0]
	instance.customParameters["winDescent"]    =  -metrics[1]

def setupFeatures(instance):
	instance.customParameters["Remove Features"] = "sups, subs, dnom, numr, frac"

def getNewInstance(wt, styleName, psFontName, fileName, weightClass=None, adjustSpacing=0):
    instance = GSInstance()
    instance.weightValue = wt
    instance.name = styleName
    instance.customParameters["postscriptFontName"] = psFontName
    instance.customParameters["postscriptFullName"] = "System Font %s" % styleName
    instance.customParameters["fileName"]           = fileName
    instance.customParameters["weightClass"]        = weightClass
    if adjustSpacing:
        step = int(round(adjustSpacing / 2))
        instance.customParameters["Filter"]         = "Transformations;LSB:%i;RSB:%i" % (step, step)
    
    #setVerticalMetrics(instance)
    setupFeatures(instance)
    
    return instance

def exportFonts(font):
	for instance in font.instances:
		if instance.active:
			out_path = "~/Quellen/FiraSystemFontReplacement/ttf/SystemFont-%s.ttf" % instance.name
			print out_path
			instance.generate(
				Format = "OTF",
				FontPath = out_path,
				AutoHint = False,
				RemoveOverlap = True,
				UseSubroutines = False,
				UseProductionNames = True
			)
