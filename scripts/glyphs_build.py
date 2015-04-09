tab_figures = "/zero.tf/one.tf/two.tf/three.tf/four.tf/five.tf/six.tf/seven.tf/eight.tf/nine.tf/zero.tf.zero/numbersign.tf/figuredash.tf/cent.tf/currency.tf/dollar.tf/drachma.tf/euro.tf/liraTurkish.tf/ruble.tf/rupeeIndian.tf/sterling.tf/yen.tf/approxequal.tf/asciitilde.tf/divide.tf/equal.tf/greater.tf/greaterequal.tf/infinity.tf/integral.tf/less.tf/lessequal.tf/logicalnot.tf/minus.tf/multiply.tf/notequal.tf/partialdiff.tf/percent.tf/perthousand.tf/plus.tf/plusminus.tf/product.tf/radical.tf/summation.tf/lozenge.tf/section.tf/degree.tf/dagger.tf/daggerdbl.tf"[1:].split("/")

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
	if font.upm != 984:
		try:
			font.upm = 984
		except:
			font.setUnitsPerEm_(984)

def drawPathsInLayer(layer, paths, clear=True):
	if clear:
		layer.paths = []
	for path in paths:
		p = GSPath()
		for node in path:
			n = GSNode(* node)
			p.nodes.append(n)
		p.closed = True
		layer.paths.append(p)

def fixNotdef(font):
	font.disableUpdateInterface()
	n = font.glyphs[".notdef"]
	for i in range(len(font.masters)):
		layer = n.layers[i]
		layer.width = 500
		drawPathsInLayer(layer, notdef)
	font.enableUpdateInterface()

def fixAppleLogo(font):
	font.disableUpdateInterface()
	font.glyphs["apple"] = GSGlyph("apple")
	a = font.glyphs["apple"]
	for i in range(len(font.masters)):
		layer = a.layers[i]
		layer.width = 790
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

def deleteGlyphs(font):
	font.disableUpdateInterface()
	for glyph_name in delete_glyphs:
		del(font.glyphs[glyph_name])
	font.enableUpdateInterface()

def setVerticalMetricsLight(instance):
	# hhea
	instance.customParameters["hheaAscender"]  =  780

def setVerticalMetrics(instance):
	# hhea
	instance.customParameters["hheaAscender"]  =  900
	instance.customParameters["hheaDescender"] = -200
	instance.customParameters["hheaLineGap"]   =    0
	# OS/2
	instance.customParameters["typoAscender"]  =  951
	instance.customParameters["typoDescender"] = -200
	instance.customParameters["typoLineGap"]   =    0
	instance.customParameters["winAscent"]     =  951
	instance.customParameters["winDescent"]    =  200

def setupFeatures(instance):
	instance.customParameters["Remove Features"] = "sups, subs, dnom, numr, frac"


def setupInstanceUltraLight(instance):
	# Neue Helvetica: LC 24, UC 24
	instance.weightValue = 24 # New in 4.1
	
	setVerticalMetrics(instance)
	
	setupFeatures(instance)
	
	instance.customParameters["postscriptFontName"] = ".HelveticaNeueDeskInterface-UltraLightP2"
	instance.customParameters["postscriptFullName"] = "System Font UltraLight"
	instance.customParameters["weightClass"]        =  100

def setupInstanceThin(instance):
	# Neue Helvetica: LC 38, UC 44
	instance.weightValue = 38 # New in 4.1
	
	setVerticalMetrics(instance)
	
	setupFeatures(instance)
	
	instance.customParameters["postscriptFontName"] = ".HelveticaNeueDeskInterface-Thin"
	instance.customParameters["postscriptFullName"] = "System Font Thin"
	instance.customParameters["weightClass"]        =  250

def setupInstanceLight(instance):
	
	# Neue Helvetica: LC 63, UC 68
	instance.weightValue = 62 # Fira System 3.1: 56
	
	setVerticalMetrics(instance)
	setVerticalMetricsLight(instance)
	
	setupFeatures(instance)
	
	instance.customParameters["postscriptFontName"] = ".HelveticaNeueDeskInterface-Light"
	instance.customParameters["postscriptFullName"] = "System Font Light"

def setupInstanceRegular(instance):
	# Neue Helvetica: LC 85, UC 95
	instance.weightValue = 86 # Fira System 3.1: 92
	
	setVerticalMetrics(instance)
	
	setupFeatures(instance)
	
	instance.customParameters["postscriptFontName"] = ".HelveticaNeueDeskInterface-Regular"
	instance.customParameters["postscriptFullName"] = "System Font Regular"

def setupInstanceMedium(instance):
	# Neue Helvetica: LC 120, UC 132
	instance.weightValue = 120
	
	setVerticalMetrics(instance)
	
	setupFeatures(instance)
	
	instance.customParameters["postscriptFontName"] = ".HelveticaNeueDeskInterface-MediumP4"
	instance.customParameters["postscriptFullName"] = "System Font Medium P4"

def setupInstanceBold(instance):
	# Neue Helvetica: LC 157, UC 95
	instance.weightValue = 142 # Fira System 3.1: 150
	
	setVerticalMetrics(instance)
	
	setupFeatures(instance)
	
	instance.customParameters["postscriptFontName"] = ".HelveticaNeueDeskInterface-Bold"
	instance.customParameters["postscriptFullName"] = "System Font Bold"

def setupInstanceHeavy(instance):
	# Neue Helvetica: LC 170, UC 186
	instance.weightValue = 170 # New in 4.1
	
	setVerticalMetrics(instance)
	
	setupFeatures(instance)
	
	instance.customParameters["postscriptFontName"] = ".HelveticaNeueDeskInterface-Heavy"
	instance.customParameters["postscriptFullName"] = "System Font Heavy"
	instance.customParameters["weightClass"]        =  750

def exportFonts(font):
	for instance in font.instances:
		if instance.active:
			out_path = "~/Quellen/FiraSystemFontReplacement/ttf/SystemFont-%s.ttf" % instance.name
			print out_path
			instance.generate(
				Format = "TTF",
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
	fixFigureSets(f)
	deleteGlyphs(f)
	fixNotdef(f)
	fixAppleLogo(f)

	for instance in f.instances:
		if instance.name == "UltraLight":
			setupInstanceUltraLight(instance)
		elif instance.name == "Thin":
			setupInstanceThin(instance)
		elif instance.name == "Light":
			setupInstanceLight(instance)
		elif instance.name == "Regular":
			setupInstanceRegular(instance)
		elif instance.name == "Medium":
			setupInstanceMedium(instance)
		elif instance.name == "Bold":
			setupInstanceBold(instance)
		elif instance.name == "Heavy":
			setupInstanceHeavy(instance)
		else:
			instance.active = False
	print "Done."
	
	print "Generating fonts ..."
	#exportFonts(f)
	print "  ** Please export the fonts manually until this function is fixed."
	print "Done."