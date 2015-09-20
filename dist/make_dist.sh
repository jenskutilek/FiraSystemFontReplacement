#!/bin/sh

# clean up old dist files

rm "Fira System Fonts.pkg"
rm "fonts.pkg"

sudo rm Fira\ System\ Fonts/*.otf

cp "../otf/SystemFontText-Light.otf"           "Fira System Fonts/FSText-Light.otf"
cp "../otf/SystemFontText-Regular.otf"         "Fira System Fonts/FSText-Regular.otf"
cp "../otf/SystemFontText-RegularG1.otf"       "Fira System Fonts/FSText-RegularG1.otf"
cp "../otf/SystemFontText-RegularG2.otf"       "Fira System Fonts/FSText-RegularG2.otf"
cp "../otf/SystemFontText-RegularG3.otf"       "Fira System Fonts/FSText-RegularG3.otf"
cp "../otf/SystemFontText-Medium.otf"          "Fira System Fonts/FSText-Medium.otf"
cp "../otf/SystemFontText-Semibold.otf"        "Fira System Fonts/FSText-Semibold.otf"
cp "../otf/SystemFontText-Bold.otf"            "Fira System Fonts/FSText-Bold.otf"
cp "../otf/SystemFontText-BoldG1.otf"          "Fira System Fonts/FSText-BoldG1.otf"
cp "../otf/SystemFontText-BoldG2.otf"          "Fira System Fonts/FSText-BoldG2.otf"
cp "../otf/SystemFontText-BoldG3.otf"          "Fira System Fonts/FSText-BoldG3.otf"
cp "../otf/SystemFontText-Heavy.otf"           "Fira System Fonts/FSText-Heavy.otf"

cp "../otf/SystemFontText-LightItalic.otf"     "Fira System Fonts/FSText-LightItalic.otf"
cp "../otf/SystemFontText-RegularItalic.otf"   "Fira System Fonts/FSText-RegularItalic.otf"
cp "../otf/SystemFontText-RegularItalicG1.otf" "Fira System Fonts/FSText-RegularItalicG1.otf"
cp "../otf/SystemFontText-RegularItalicG2.otf" "Fira System Fonts/FSText-RegularItalicG2.otf"
cp "../otf/SystemFontText-RegularItalicG3.otf" "Fira System Fonts/FSText-RegularItalicG3.otf"
cp "../otf/SystemFontText-MediumItalic.otf"    "Fira System Fonts/FSText-MediumItalic.otf"
cp "../otf/SystemFontText-SemiboldItalic.otf"  "Fira System Fonts/FSText-SemiboldItalic.otf"
cp "../otf/SystemFontText-BoldItalic.otf"      "Fira System Fonts/FSText-BoldItalic.otf"
cp "../otf/SystemFontText-BoldItalicG1.otf"    "Fira System Fonts/FSText-BoldItalicG1.otf"
cp "../otf/SystemFontText-BoldItalicG2.otf"    "Fira System Fonts/FSText-BoldItalicG2.otf"
cp "../otf/SystemFontText-BoldItalicG3.otf"    "Fira System Fonts/FSText-BoldItalicG3.otf"
cp "../otf/SystemFontText-HeavyItalic.otf"     "Fira System Fonts/FSText-HeavyItalic.otf"

cp "../otf/SystemFontDisplay-Ultralight.otf"   "Fira System Fonts/FSDisplay-Ultralight.otf"
cp "../otf/SystemFontDisplay-Thin.otf"         "Fira System Fonts/FSDisplay-Thin.otf"
cp "../otf/SystemFontDisplay-Light.otf"        "Fira System Fonts/FSDisplay-Light.otf"
cp "../otf/SystemFontDisplay-Regular.otf"      "Fira System Fonts/FSDisplay-Regular.otf"
cp "../otf/SystemFontDisplay-Medium.otf"       "Fira System Fonts/FSDisplay-Medium.otf"
cp "../otf/SystemFontDisplay-Semibold.otf"     "Fira System Fonts/FSDisplay-Semibold.otf"
cp "../otf/SystemFontDisplay-Bold.otf"         "Fira System Fonts/FSDisplay-Bold.otf"
cp "../otf/SystemFontDisplay-Heavy.otf"        "Fira System Fonts/FSDisplay-Heavy.otf"
cp "../otf/SystemFontDisplay-Black.otf"        "Fira System Fonts/FSDisplay-Black.otf"

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