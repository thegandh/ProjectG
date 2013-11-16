#!/usr/bin/python

import allData
# Using a template, generate the person files 

hallMembers = allData.allData()

personTemplate = """---
title: %s
layout: person
bio: %s
pic: "%s.jpg"
---
"""

for member in hallMembers:
    with open ('../%s.html'%member, 'w') as memberFile:
        memberFile.write(personTemplate%(hallMembers[member]['name'], hallMembers[member]['bio'], member))
