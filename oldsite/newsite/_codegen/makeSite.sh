#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Need the password as a command line argument"
    exit
fi

password=$1

# Create raw content
./sidebarGenerator.py $password
./memberGenerator.py $password
./faqGenerator.py $password
./funfactGenerator.py $password
./resourceGenerator.py $password

# Build using liquid/jekyll
jekyll build -s .. -d ../_site

# Clean up for our needs
allNames=`cut -f2 -d"^" ../_data/members.csv`
for member in $allNames; do
    mv ../_site/$member/index.html ../_site/$member.html
    rm -rf ../_site/$member
done
for file in faq resources funfacts; do
    mv ../_site/$file/index.html ../_site/$file.html
    rm -rf ../_site/$file
done

# Move all the files to the correct locations
cp ../_site/*.html ../../..
cp ../_includes/* ../../../_includes/
cp ../_layouts/* ../../../_layouts/
