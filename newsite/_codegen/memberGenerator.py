#!/usr/bin/python

import csv
# Using a template, generate the person files 

personTemplate = """---
title: %s
layout: person
bio: %s
pic: "%s.jpg"
---
"""

with open('../_data/members.csv', 'rb') as csvFile:
    hallMembers = csv.reader(csvFile, delimiter="|", quotechar='"')
    for member in hallMembers:
        memberId = member[0]
        name = member[1]
        bio = member[2]
        with open ('../%s.html'%memberId, 'w') as memberFile:
            memberFile.write(personTemplate%(name, bio, memberId))
