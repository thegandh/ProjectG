#!/usr/bin/python

import csv
# Using a template, generate the person files 

personHeader = """---
title: %s
layout: person
bio: %s
pic: "%s.jpg"
---

<ul>
"""

gandhTemplate = """
    <li>
      <p class="lead">%s</p>
      <p>%s</p> <a href="sources.html#%s">%s</a>
    </li>
"""

with open('../_data/members.csv', 'rb') as csvFile:
    hallMembers = csv.reader(csvFile, delimiter="|", quotechar='"')
    for member in hallMembers:
        memberId = member[0]
        name = member[1]
        bio = member[2]
        with open ('../%s.html'%memberId, 'w') as memberFile:
            memberFile.write(personHeader%(name, bio, memberId))

            try:
                with open ('../_data/%s.csv'%(memberId), 'rb') as detailFile:
                    gandh = csv.reader(detailFile, delimiter="|", quotechar='"')
                    for line in gandh:
                        point = line[0]
                        blurb = line[1]
                        source = line[2]
                        memberFile.write(gandhTemplate%(point, blurb, source, source))
            except:
                dummy=1
