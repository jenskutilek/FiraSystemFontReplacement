#!/bin/sh

# clean up old dist files

rm "Fira System Fonts.pkg"
rm "fira-system-fonts.zip"
rm "fonts.pkg"

sudo rm "Fira System Fonts/FiraSystem.ttc"

# build TrueType collection

ftxmakettc \
  ../ttf/FiraSystem-Regular.ttf \
  ../ttf/FiraSystem-Bold.ttf \
  ../ttf/FiraSystem-Light.ttf \
  ../ttf/FiraSystem-Medium.ttf \
  "Fira System Fonts/FiraSystem.ttc"

sudo chown root:wheel "Fira System Fonts/FiraSystem.ttc"

zip -x \*.DS\* -r "fira-system-fonts.zip" "Fira System Fonts"

# build packages

pkgbuild \
  --root "Fira System Fonts" \
  --version "3.112" \
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

rm "Fira System Fonts.pkg"
rm "fonts.pkg"