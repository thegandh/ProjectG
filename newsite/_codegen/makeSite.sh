#!/bin/bash

# Create raw content
./sidebarGenerator.py
./memberGenerator.py
./faqGenerator.py

# Build using liquid/jekyll
jekyll build -s .. -d ../_site

# Clean up for our needs
allNames=`cut -f2 -d"\"" members.csv`
for member in $allNames; do
    mv ../_site/$member/index.html ../_site/$member.html
    rm -rf ../_site/$member
done
