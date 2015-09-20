#MenuTitle: Setup current font as Text Roman
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

f.instances.append(getNewInstance(
	weights[0], "Light", ".SFNSText-Light", "SystemFontText-Light", 300
))
f.instances.append(getNewInstance(
	weights[1], "Regular", ".SFNSText-Regular", "SystemFontText-Regular", 400
))
f.instances.append(getNewInstance(
	weights[2], "Regular G1", ".SFNSText-RegularG1", "SystemFontText-RegularG1", 400
))
f.instances.append(getNewInstance(
	weights[3], "Regular G2", ".SFNSText-RegularG2", "SystemFontText-RegularG2", 400
))
f.instances.append(getNewInstance(
	weights[4], "Regular G3", ".SFNSText-RegularG3", "SystemFontText-RegularG3", 400
))
f.instances.append(getNewInstance(
	weights[5], "Medium", ".SFNSText-Medium", "SystemFontText-Medium", 500
))
f.instances.append(getNewInstance(
	weights[6], "Semibold", ".SFNSText-Semibold", "SystemFontText-Semibold", 600
))
f.instances.append(getNewInstance(
	weights[7], "Bold", ".SFNSText-Bold", "SystemFontText-Bold", 700
))
f.instances.append(getNewInstance(
	weights[8], "Bold G1", ".SFNSText-BoldG1", "SystemFontText-BoldG1", 700
))
f.instances.append(getNewInstance(
	weights[9], "Bold G2", ".SFNSText-BoldG2", "SystemFontText-BoldG2", 700
))
f.instances.append(getNewInstance(
	weights[10], "Bold G3", ".SFNSText-BoldG3", "SystemFontText-BoldG3", 700
))
f.instances.append(getNewInstance(
	weights[11], "Heavy", ".SFNSText-Heavy", "SystemFontText-Heavy", 800
))

for i in f.instances:
	#setVerticalMetrics(i)
	setupFeatures(i)

print "Done."

print "Generating fonts ..."
#exportFonts(f)
print "  ** Please export the fonts manually until this function is fixed."
print "Done."