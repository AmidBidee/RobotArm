#!/usr/bin/env bash
# TEMPORARY INSTALL SCRIPT
# This scripts adds the robotarm directory
# to users bin PATH
# and adds robotarm to PYTHONPATH

# current working directory of this scripts
PATH_TO_PACKAGE="$(pwd)"

# collect the current paths to a file
echo "$PATH" > paths.txt

# check if the robotarm directory is aleady on path
# if not add it to the .bashrc file
# if true echo "already on path"
if ! grep $PATH_TO_PACKAGE ./paths.txt
    then
        echo "export PATH="\"\$PATH:$PATH_TO_PACKAGE/robotarm"\"" >> ~/.bashrc
	    echo "export PYTHONPATH="\"\$PYHTONPATH:$PATH_TO_PACKAGE"\"" >> ~/.bashrc
else
    echo "Already On Path"
fi

# delete the paths collected to file
rm paths.txt