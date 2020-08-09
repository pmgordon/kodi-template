#! /bin/bash
WD=${PWD}
PLUGIN_NAME=template

rm -rf "${HOME}/Library/Application Support/Kodi/addons/plugin.video.${PLUGIN_NAME}"
cp -R ./source "${HOME}/Library/Application Support/Kodi/addons/plugin.video.${PLUGIN_NAME}"