#MenuTitle: Setup current font as Text Italic
# -*- coding: utf-8 -*-
from __future__ import division

from glyphs_build import *
from settings import sf_upm, fs_target_upm, weights_text

print "Setting up current font as System Font Replacement ..."

f = Glyphs.font

setNames(f)
setUPM(f)
deleteGlyphs(f)
fixNotdef(f)
fixAppleLogo(f)
for m in f.masters:
	setVerticalMetrics(m)

f.instances = []

weights = normalizeList(
	weights_text,
	fs_target_upm / sf_upm
)

print weights_text
print weights

f.instances.append(getNewInstance(
	weights[1], "Italic", ".SFNSText-Italic", "SystemFontText-RegularItalic", 400
))
f.instances.append(getNewInstance(
	weights[5], "Medium Italic", ".SFNSText-MediumItalic", "SystemFontText-MediumItalic", 500
))
f.instances.append(getNewInstance(
	weights[6], "Semibold Italic", ".SFNSText-SemiboldItalic", "SystemFontText-SemiboldItalic", 600
))
f.instances.append(getNewInstance(
	weights[7], "Bold Italic", ".SFNSText-BoldItalic", "SystemFontText-BoldItalic", 700
))
f.instances.append(getNewInstance(
	weights[0], "Light Italic", ".SFNSText-LightItalic", "SystemFontText-LightItalic", 300
))
f.instances.append(getNewInstance(
	weights[11], "Heavy Italic", ".SFNSText-HeavyItalic", "SystemFontText-HeavyItalic", 800
))

#for i in f.instances:
#	#setVerticalMetrics(i)
#	setupFeatures(i)

print "Done."

print "Generating fonts ..."
#exportFonts(f)
print "  ** Please export the fonts manually until this function is fixed."
print "Done."
