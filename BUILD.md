### Notes on building the replacement system fonts

I have switched to using [fontmake](https://github.com/googlei18n/fontmake) to build the fonts, this should make the process somewhat more transparent.

In any case you need to start from a [Glyphs](https://glyphsapp.com) source file with a large enough design range and character set to accommodate all the weights and characters that macOS uses. Some of the additional glyphs that I found are required are included in [additions.glyphs](https://github.com/jenskutilek/FiraSystemFontReplacement/blob/sierra/source_glyphs/additions.glyphs). These need to be copied to your Glyphs file, and matched to the design and dimensions of your font.

The Glyphs source then must be modified to contain the correct font instances in the correct order. I used to do this by running [text_roman.py](https://github.com/jenskutilek/FiraSystemFontReplacement/blob/sierra/scripts/text_roman.py) inside Glyphs, but I didn’t check if the results are still OK. I fiddled a lot manually for the latest release.

If you have the modified Glyphs file, you must enter its path at the beginning of [build.sh](https://github.com/jenskutilek/FiraSystemFontReplacement/blob/sierra/build.sh), and then execute `build.sh`. If you have fontmake and all dependencies installed, the rest of the build process should go smoothly and you will find the final font in `ttf/FSText.ttf`.
