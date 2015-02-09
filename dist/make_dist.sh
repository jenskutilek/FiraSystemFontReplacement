#!/bin/sh

rm "fira-system-fonts.zip"
ftxmakettc ../ttf/FiraSystem-Regular.ttf ../ttf/FiraSystem-Bold.ttf ../ttf/FiraSystem-Light.ttf ../ttf/FiraSystem-Medium.ttf "Fira System Fonts/FiraSystem.ttc"
zip -x \*.DS\* -r "fira-system-fonts.zip" "Fira System Fonts"