#!/bin/sh

rm "fira-system-fonts.zip"
sudo rm "Fira System Fonts/FiraSystem.ttc"
ftxmakettc ../ttf/FiraSystem-Regular.ttf ../ttf/FiraSystem-Bold.ttf ../ttf/FiraSystem-Light.ttf ../ttf/FiraSystem-Medium.ttf "Fira System Fonts/FiraSystem.ttc"
sudo chown root:wheel "Fira System Fonts/FiraSystem.ttc"

zip -x \*.DS\* -r "fira-system-fonts.zip" "Fira System Fonts"

pkgbuild --root "Fira System Fonts" \
  --version "3.113" \
  --filter ".txt" \
  --filter "._" \
  --identifier "de.kutilek.fonts.firasystem" \
  --install-location "/Library/Fonts" \
  "Fira System Fonts.pkg"

zip "fira-system-fonts-installer.zip" "Fira System Fonts.pkg"
