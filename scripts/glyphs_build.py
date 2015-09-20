# -*- coding: utf-8 -*-
from __future__ import division

from GlyphsApp import GSGlyph, GSInstance, GSNode, GSPath

from settings import fs_target_upm, sf_upm

delete_glyphs = ["uniE000", "uniE001", "uniE002", "uniE003"]

apple = [[((291, -22), 65), ((313, -16), 65), ((341, -5), 35), ((367, 6), 65), ((391, 11), 65), ((413, 11), 35), ((434, 11), 65), ((459, 6), 65), ((488, -4), 35), ((517, -15), 65), ((541, -20), 65), ((559, -20), 35), ((602, -20), 65), ((645, 12), 65), ((688, 77), 35), ((716, 120), 65), ((736, 162), 65), ((749, 202), 35), ((674, 230), 65), ((635, 299), 65), ((635, 372), 35), ((635, 445), 65), ((670, 497), 65), ((725, 540), 35), ((682, 594), 65), ((632, 622), 65), ((566, 622), 35), ((542, 622), 65), ((513, 616), 65), ((479, 605), 35), ((445, 594), 65), ((421, 588), 65), ((408, 588), 35), ((397, 588), 65), ((374, 593), 65), ((339, 603), 35), ((304, 613), 65), ((275, 618), 65), ((250, 618), 35), ((125, 618), 65), ((51, 501), 65), ((51, 359), 35), ((51, 276), 65), ((76, 192), 65), ((125, 107), 35), ((174, 21), 65), ((224, -22), 65), ((275, -22), 35), ], [((439, 611), 65), ((463, 617), 65), ((500, 652), 35), ((541, 695), 65), ((569, 755), 65), ((558, 811), 35), ((441, 784), 65), ((395, 707), 65), ((394, 608), 35)]]

notdef = [[((450, 0), 1), ((450, 696), 1), ((50, 696), 1), ((50, 0), 1), ], [((101, 650), 1), ((399, 650), 1), ((399, 46), 1), ((101, 46), 1)]]


def setNames(font):
	font.familyName      = "System Font"
	font.copyright       = u"Digitized data copyright © 2012-2015, The Mozilla Foundation and Telefonica S.A. System Font Replacement version 2015 by Jens Kutilek."
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
