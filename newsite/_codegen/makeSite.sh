#!/bin/bash

./sidebarGenerator.py
./memberGenerator.py
jekyll build -s .. -d ../_site
allNames=`cut -f2 -d"\"" members.csv`
for member in $allNames; do
    mv ../_site/$member/index.html ../_site/$member.html
    rm -rf ../_site/$member
done
