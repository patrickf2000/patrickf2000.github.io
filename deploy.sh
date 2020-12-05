#!/bin/bash

rm -rf ./output
pelican content

rm -r ../patrickf2000.github.io/*
cp -r ./output/* ../patrickf2000.github.io

cd ../patrickf2000.github.io
git add .
git commit
git push -u origin master

echo "Done"

