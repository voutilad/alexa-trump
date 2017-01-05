#!/bin/bash

mkdir -p build
PWD = $(pwd)
zip -r9 ./build/Trump.zip trump.py
cd $VIRTUAL_ENV/lib/python2.7/site-packages
zip -r9 ~/src/alexa/alexa-trump/lambda/build/Trump.zip .
cd $PWD
