#!/usr/bin/env python

from sys import argv
from fontTools.ttLib import TTFont


instance_values = {
	"Regular":  1.0,
	"Medium":   1.1842,
	"Semibold": 1.32455,
	"Bold":     1.50877,
	"Light":    0.75609,
	"Heavy":    1.7807,

	"Ultrathin": 0.0,
	"Black": 1.999,
}


file_path = argv[1]

f = TTFont(file_path)

# Set sfntVersion, just to be sure. It may come in wrong from any of the merged ttx files.
f.sfntVersion = "\x00\x01\x00\x00"


# Delete unneccessary tables

for tag in ("avar", "HVAR", "MVAR"):
	del f[tag]


# Fix fvar table
# We could fix this in the Glyphs file, but here it is easier.

fvar = f["fvar"]
name = f["name"]

for axis in fvar.axes:
	if axis.axisTag == "wght":
		print "[postprocess] Fixing weight axis range"
		axis.minValue = 0.0
		axis.defaultValue = 1.0
		axis.maxValue = 1.999

for instance in fvar.instances:
	instance_name = name.getName(instance.subfamilyNameID, 1, 0, 0).string
	v = instance_values[instance_name]
	print instance_name, instance.coordinates["wght"], "->", v
	instance.coordinates["wght"] = v


# Fix name table

name.setName(u"System Font", 4, 0, 3, 0)
name.setName(u".SF NS Text", 1, 1, 0, 0)
name.setName(u"System Font", 1, 3, 1, 0x409)
name.setName(u"Regular",     2, 1, 0, 0)
name.setName(u"System Font", 4, 3, 1, 0x409)
name.setName(u".SFNSText",   6, 3, 1, 0x409)


f.save(file_path) # + "_fixed.ttf"
