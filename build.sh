#!/bin/bash

glyphs_file=source_glyphs/FiraSans_4-1_150908_GX.glyphs


# Clean up

rm ttf/FSText.ttf
rm ttf/FSText.ttx
rm ttx/text_trak.ttf
rm master_ufo/FiraSystem-VF.ttf
rm variable_ttf/.SFNSText-VF.ttf


# If the Glyphs file is present, build the UFOs and designspace.

# The Glyphs file is not part of the GitHub repository.
# You can get it from <https://github.com/mozilla/Fira/tree/master/source/glyphs>.

if [ -f "$glyphs_file" ]
	then
		fontmake -o variable --keep-overlaps -g "$glyphs_file"
		#fontmake -o ttf-interpolatable --keep-overlaps -g "$glyphs_file"
		mv master_ufo/.SFNSText.designspace master_ufo/FiraSystem.designspace
		mv variable_ttf/.SFNSText-VF.ttf master_ufo/FiraSystem-VF.ttf
	else
		# We have no Glyphs file, just try to build the variable font from the designspace.
		fonttools varLib master_ufo/FiraSystem.designspace
fi


# Merge the trak table which controls the automatic tracking of the font.

ttx -m master_ufo/FiraSystem-VF.ttf ttx/text_trak.ttx
mv ttx/text_trak.ttf ttf/FSText.ttf


# Postprocess and dump the font(s) for inspection

python scripts/postprocess.py ttf/FSText.ttf
ttx -l ttf/FSText.ttf
ttx ttf/FSText.ttf
