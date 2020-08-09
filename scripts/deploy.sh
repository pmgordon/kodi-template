#! /bin/bash
WD=${PWD}
VERSION=$1

echo $WD

#pushd ./local/
zip -r $WD/kodi-dist/plugin.video.template-$1.zip ./source
#popd