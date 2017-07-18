#!/bin/sh

# clean up old dist files

rm "Fira System Fonts.pkg"
rm "fonts.pkg"

sudo rm Fira\ System\ Fonts/*.ttf

cp "../ttf/FSDisplay.ttf"    "Fira System Fonts/FSDisplay.ttf"
cp "../ttf/FSText.ttf"       "Fira System Fonts/FSText.ttf"
cp "../ttf/FSTextItalic.ttf" "Fira System Fonts/FSTextItalic.ttf"

sudo chown root:wheel Fira\ System\ Fonts/*.ttf

# Disable non-installer download for now because people don't pay attention
# to the correct file permissions
#rm "fira-system-fonts.zip"
#zip -x \*.DS\* -r "fira-system-fonts.zip" "Fira System Fonts"

chmod 755 "scripts/preinstall"

# build packages

pkgbuild \
  --root "Fira System Fonts" \
  --version "4.106" \
  --scripts "scripts" \
  --filter ".txt" \
  --filter "._" \
  --identifier "de.kutilek.fonts.firasystem.pkg" \
  --install-location "/Library/Fonts" \
  "fonts.pkg"

productbuild \
  --distribution distribution.xml \
    --resources resources \
  "Fira System Fonts.pkg"

zip "fira-system-fonts-installer.zip" "Fira System Fonts.pkg"

# clean up intermediate packages

#rm "Fira System Fonts.pkg"
#rm "fonts.pkg"
