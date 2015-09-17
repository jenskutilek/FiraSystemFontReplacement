#!/bin/sh

# clean up old dist files

rm "Fira System Fonts.pkg"
rm "fonts.pkg"

sudo rm Fira\ System\ Fonts/*.otf

cp ../otf/SystemFont-Light.otf     "Fira System Fonts/FSText-Light.otf"
cp ../otf/SystemFont-Regular.otf   "Fira System Fonts/FSText-Regular.otf"
cp ../otf/SystemFont-RegularG1.otf "Fira System Fonts/FSText-RegularG1.otf"
cp ../otf/SystemFont-RegularG2.otf "Fira System Fonts/FSText-RegularG2.otf"
cp ../otf/SystemFont-RegularG3.otf "Fira System Fonts/FSText-RegularG3.otf"
cp ../otf/SystemFont-Medium.otf    "Fira System Fonts/FSText-Medium.otf"
cp ../otf/SystemFont-Semibold.otf  "Fira System Fonts/FSText-Semibold.otf"
cp ../otf/SystemFont-Bold.otf      "Fira System Fonts/FSText-Bold.otf"

sudo chown root:wheel Fira\ System\ Fonts/*.otf

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

rm "Fira System Fonts.pkg"
rm "fonts.pkg"