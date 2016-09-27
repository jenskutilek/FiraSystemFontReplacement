#MenuTitle: Print Paths

glyphs = [".notdef", "apple"]

def getPaths(glyph_name):
	layer = Glyphs.font.glyphs[glyph_name].layers[0]

	result = "%s = [" % glyph_name

	for path in layer.paths:
		result += "["
		for node in path.nodes:
			result += "((%i, %i), %r), " % (node.x, node.y, node.type)
		result += "], "
	result += "]"
	return result

for glyph_name in glyphs:
	print getPaths(glyph_name)
