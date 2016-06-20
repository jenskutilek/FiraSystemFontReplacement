#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import remove
from shutil import move
from fontTools.ttLib import TTFont

fonts_text = [
    "SystemFontText-Bold.otf",
    "SystemFontText-BoldItalic.otf",
    "SystemFontText-BoldG1.otf",
    "SystemFontText-BoldItalicG1.otf",
    "SystemFontText-BoldG2.otf",
    "SystemFontText-BoldItalicG2.otf",
    "SystemFontText-BoldG3.otf",
    "SystemFontText-BoldItalicG3.otf",
    "SystemFontText-Heavy.otf",
    "SystemFontText-HeavyItalic.otf",
    "SystemFontText-Light.otf",
    "SystemFontText-LightItalic.otf",
    "SystemFontText-Medium.otf",
    "SystemFontText-MediumItalic.otf",
    "SystemFontText-RegularItalic.otf",
    "SystemFontText-Regular.otf",
    "SystemFontSF-Regular.otf", # FB fix
    "SystemFontText-RegularItalicG1.otf",
    "SystemFontText-RegularG1.otf",
    "SystemFontText-RegularItalicG2.otf",
    "SystemFontText-RegularG2.otf",
    "SystemFontText-RegularItalicG3.otf",
    "SystemFontText-RegularG3.otf",
    "SystemFontText-SemiboldItalic.otf",
    "SystemFontText-Semibold.otf",
]

fonts_display = [
    "SystemFontDisplay-Black.otf",
    "SystemFontDisplay-Bold.otf",
    "SystemFontDisplay-Heavy.otf",
    "SystemFontDisplay-Light.otf",
    "SystemFontDisplay-Medium.otf",
    "SystemFontDisplay-Regular.otf",
    "SystemFontDisplay-Semibold.otf",
    "SystemFontDisplay-Thin.otf",
    "SystemFontDisplay-Ultralight.otf",
]

def addTable(font_file_name, table_file_name):
    f = TTFont(font_file_name)
    f.importXML(table_file_name)
    f.save("temp.otf")
    f.close()
    remove(font_file_name)
    move("temp.otf", font_file_name)

for file_name in fonts_text:
    print "Processing", file_name, "..."
    addTable("../otf/%s" % file_name, "../ttx/text_trak.ttx")

for file_name in fonts_display:
    print "Processing", file_name, "..."
    addTable("../otf/%s" % file_name, "../ttx/disp_trak.ttx")

print "Done."