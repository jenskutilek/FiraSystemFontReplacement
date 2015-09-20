#MenuTitle: Setup current font as Display Roman
# -*- coding: utf-8 -*-
from __future__ import division

from glyphs_build import *
from settings import sf_upm, fs_target_upm, weights_disp

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
	weights_disp,
	fs_target_upm / sf_upm
)

f.instances.append(getNewInstance(
	weights[0], "UltraLight", ".SFNSDisplay-Ultralight", "SystemFontDisplay-Ultralight", 100, adjustSpacing = -40
))
f.instances.append(getNewInstance(
	weights[1], "Thin", ".SFNSDisplay-Thin", "SystemFontDisplay-Thin", 200, adjustSpacing = -32
))
f.instances.append(getNewInstance(
	weights[2], "Light", ".SFNSDisplay-Light", "SystemFontDisplay-Light", 300, adjustSpacing = -28
))
f.instances.append(getNewInstance(
	weights[3], "Regular", ".SFNSDisplay-Regular", "SystemFontDisplay-Regular", 400, adjustSpacing = -20
))
f.instances.append(getNewInstance(
	weights[4], "Medium", ".SFNSDisplay-Medium", "SystemFontDisplay-Medium", 500, adjustSpacing = -20
))
f.instances.append(getNewInstance(
	weights[5], "Semibold", ".SFNSDisplay-Semibold", "SystemFontDisplay-Semibold", 600, adjustSpacing = -20
))
f.instances.append(getNewInstance(
	weights[6], "Bold", ".SFNSDisplay-Bold", "SystemFontDisplay-Bold", 700, adjustSpacing = -20
))
f.instances.append(getNewInstance(
	weights[7], "Heavy", ".SFNSDisplay-Heavy", "SystemFontDisplay-Heavy", 800, adjustSpacing = -12
))
f.instances.append(getNewInstance(
	weights[8], "Black", ".SFNSDisplay-Black", "SystemFontDisplay-Black", 900
))


for i in f.instances:
	#setVerticalMetrics(i)
	setupFeatures(i)

print "Done."

print "Generating fonts ..."
#exportFonts(f)
print "  ** Please export the fonts manually until this function is fixed."
print "Done."