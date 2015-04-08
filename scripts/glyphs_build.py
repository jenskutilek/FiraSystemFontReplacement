tab_figures = "/zero.tf/one.tf/two.tf/three.tf/four.tf/five.tf/six.tf/seven.tf/eight.tf/nine.tf/zero.tf.zero/numbersign.tf/figuredash.tf/cent.tf/currency.tf/dollar.tf/drachma.tf/euro.tf/liraTurkish.tf/ruble.tf/rupeeIndian.tf/sterling.tf/yen.tf/approxequal.tf/asciitilde.tf/divide.tf/equal.tf/greater.tf/greaterequal.tf/infinity.tf/integral.tf/less.tf/lessequal.tf/logicalnot.tf/minus.tf/multiply.tf/notequal.tf/partialdiff.tf/percent.tf/perthousand.tf/plus.tf/plusminus.tf/product.tf/radical.tf/summation.tf/lozenge.tf/section.tf/degree.tf/dagger.tf/daggerdbl.tf"[1:].split("/")

#print tab_figures

def setNames(font):
	font.familyName      = "System Font"
	font.copyright      += " System Font Replacement version 2015 by Jens Kutilek."
	font.manufacturer    = "Jens Kutilek"
	font.manufacturerURL = "http://www.kutilek.de/"

def setUPM(font):
	if font.upm != 984:
		font.upm = 984

def fixNotdef(font):
	pass

def fixAppleLogo(font):
	pass

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
	instance.customParameters["Remove Features"] = "sups, subs"


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

def generateFonts(font):
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
	#generateFonts(f)
	print "  ** Please generate the fonts manually until this function is fixed."
	print "Done."