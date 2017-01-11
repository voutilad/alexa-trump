#!/bin/bash

# This script works for macOS, but should work for *nix systems as well.
# Make sure to run it from the directory you're packaging.
# Lastly, it assumes you use virtual environments and have a environment var
# called VIRTUAL_ENV pointing to the location of the active virtual env.
# (This should be the case if using virtualenvwrapper)

# clear out existing package
mkdir -p build
rm build/Lambda.zip

# package out python module and any dependencies installed in the virtual env
PWD = $(pwd)
zip -r9 ./build/Lambda.zip *.py
cd $VIRTUAL_ENV/lib/python2.7/site-packages
zip -r9 $PWD/build/Lambda.zip .
cd $PWD
