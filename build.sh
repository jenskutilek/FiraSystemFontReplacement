#!/bin/sh

rm ttf/FSText.ttf
rm ttf/FSText.ttx
fonttools varLib master_ufo/FiraSystem.designspace
ttx -m master_ufo/FiraSystem-VF.ttf ttx/text_trak.ttx
mv ttx/text_trak.otf ttf/FSText.ttf
ttx -l ttf/FSText.ttf
ttx ttf/FSText.ttf
