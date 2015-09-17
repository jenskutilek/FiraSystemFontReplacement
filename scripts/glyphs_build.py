# -*- coding: utf-8 -*-
from __future__ import division

tab_figures = "/zero.tf/one.tf/two.tf/three.tf/four.tf/five.tf/six.tf/seven.tf/eight.tf/nine.tf/zero.tf.zero/numbersign.tf/figuredash.tf/cent.tf/currency.tf/dollar.tf/drachma.tf/euro.tf/liraTurkish.tf/ruble.tf/rupeeIndian.tf/sterling.tf/yen.tf/approxequal.tf/asciitilde.tf/divide.tf/equal.tf/greater.tf/greaterequal.tf/infinity.tf/integral.tf/less.tf/lessequal.tf/logicalnot.tf/minus.tf/multiply.tf/notequal.tf/partialdiff.tf/percent.tf/perthousand.tf/plus.tf/plusminus.tf/product.tf/radical.tf/summation.tf/lozenge.tf/section.tf/degree.tf/dagger.tf/daggerdbl.tf"[1:].split("/")

delete_glyphs = ["uniE000", "uniE001", "uniE002", "uniE003"]

apple = [[((291, -22), 65), ((313, -16), 65), ((341, -5), 35), ((367, 6), 65), ((391, 11), 65), ((413, 11), 35), ((434, 11), 65), ((459, 6), 65), ((488, -4), 35), ((517, -15), 65), ((541, -20), 65), ((559, -20), 35), ((602, -20), 65), ((645, 12), 65), ((688, 77), 35), ((716, 120), 65), ((736, 162), 65), ((749, 202), 35), ((674, 230), 65), ((635, 299), 65), ((635, 372), 35), ((635, 445), 65), ((670, 497), 65), ((725, 540), 35), ((682, 594), 65), ((632, 622), 65), ((566, 622), 35), ((542, 622), 65), ((513, 616), 65), ((479, 605), 35), ((445, 594), 65), ((421, 588), 65), ((408, 588), 35), ((397, 588), 65), ((374, 593), 65), ((339, 603), 35), ((304, 613), 65), ((275, 618), 65), ((250, 618), 35), ((125, 618), 65), ((51, 501), 65), ((51, 359), 35), ((51, 276), 65), ((76, 192), 65), ((125, 107), 35), ((174, 21), 65), ((224, -22), 65), ((275, -22), 35), ], [((439, 611), 65), ((463, 617), 65), ((500, 652), 35), ((541, 695), 65), ((569, 755), 65), ((558, 811), 35), ((441, 784), 65), ((395, 707), 65), ((394, 608), 35)]]

notdef = [[((450, 0), 1), ((450, 696), 1), ((50, 696), 1), ((50, 0), 1), ], [((101, 650), 1), ((399, 650), 1), ((399, 46), 1), ((101, 46), 1)]]

sf_upm = 2048
fs_upm = Glyphs.font.upm
fs_target_upm = 1032

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

def fixFigureSets(font):
	font.disableUpdateInterface()
	for glyph_name in tab_figures:
		lf_name = glyph_name.replace(".tf", ".lf")
		default_name = glyph_name.replace(".tf", "")
		if not lf_name in font.glyphs.keys():
			if default_name in font.glyphs.keys():
				# change names for default figure set to LF
				glyph = font.glyphs[default_name]
				glyph.name = lf_name
		if not default_name in font.glyphs.keys():
			# change names for TF figure set to default names
			glyph = font.glyphs[glyph_name]
			for i in range(len(font.masters)):
				layer = glyph.layers[i]
				if layer.width == 560:
					layer.LSB -= 2
					layer.RSB -= 2
				else:
					print "Not setting to new TF width: %s (%i)" % (glyph.name, layer.width)
			glyph.name = default_name
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

def getNewInstance(wt, styleName, psFontName, fileName, weightClass=None):
    instance = GSInstance()
    instance.weightValue = wt
    instance.name = styleName
    instance.customParameters["postscriptFontName"] = psFontName
    instance.customParameters["postscriptFullName"] = "System Font %s" % styleName
    instance.customParameters["fileName"]           = fileName
    instance.customParameters["weightClass"]        = weightClass
    
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
	

if __name__ == "__main__":
	
	print "Setting up current font as System Font Replacement ..."
	
	f = Glyphs.font
	
	setNames(f)
	setUPM(f)
	#fixFigureSets(f)
	deleteGlyphs(f)
	fixNotdef(f)
	fixAppleLogo(f)
	for m in f.masters:
		setVerticalMetrics(m)

	f.instances = []
	
	weights = normalizeList(
		[131, 172, 180, 189, 195, 215, 248, 291],
		fs_target_upm / sf_upm
	)
	
	f.instances.append(getNewInstance(
		weights[0], "Light", ".SFNSText-Light", "SystemFont-Light", 300
	))
	f.instances.append(getNewInstance(
		weights[1], "Regular", ".SFNSText-Regular", "SystemFont-Regular", 400
	))
	f.instances.append(getNewInstance(
		weights[2], "Regular G1", ".SFNSText-RegularG1", "SystemFont-RegularG1", 400
	))
	f.instances.append(getNewInstance(
		weights[3], "Regular G2", ".SFNSText-RegularG2", "SystemFont-RegularG2", 400
	))
	f.instances.append(getNewInstance(
		weights[4], "Regular G3", ".SFNSText-RegularG3", "SystemFont-RegularG3", 400
	))
	f.instances.append(getNewInstance(
		weights[5], "Medium", ".SFNSText-Medium", "SystemFont-Medium", 500
	))
	f.instances.append(getNewInstance(
		weights[6], "Semibold", ".SFNSText-Semibold", "SystemFont-Semibold", 600
	))
	f.instances.append(getNewInstance(
		weights[7], "Bold", ".SFNSText-Bold", "SystemFont-Bold", 700
	))
	
	for i in f.instances:
		#setVerticalMetrics(i)
		setupFeatures(i)
    
	print "Done."
	
	print "Generating fonts ..."
	#exportFonts(f)
	print "  ** Please export the fonts manually until this function is fixed."
	print "Done."