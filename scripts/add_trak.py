#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import remove
from shutil import move
from fontTools.ttLib import TTFont

fonts_text = [
    "FSText.ttf",
    "FSTextItalic.ttf",
]

fonts_display = [
    "FSDisplay.ttf",
]

def addTable(font_file_name, table_file_name):
    f = TTFont(font_file_name)
    f.importXML(table_file_name)
    f.save("temp.ttf")
    f.close()
    remove(font_file_name)
    move("temp.ttf", font_file_name)

for file_name in fonts_text:
    print "Processing", file_name, "..."
    addTable("../ttf/%s" % file_name, "../ttx/text_trak.ttx")

for file_name in fonts_display:
    print "Processing", file_name, "..."
    addTable("../ttf/%s" % file_name, "../ttx/disp_trak.ttx")

print "Done."
