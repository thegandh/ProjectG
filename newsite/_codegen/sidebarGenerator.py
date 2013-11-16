#!/usr/bin/python

import csv
# Using a template, generate the hallOfShame.html file
# to be put under the _includes directory

sideTemplate = """
<div class="row">
  <div class="col-md-3">
    <img src="/images/%s.jpg" class="img-responsive" />
  </div>
  <div class="col-md-9">
    <h3><a href="%s.html">%s</a></h3>
  </div>
</div>
<br />
"""
with open('../_includes/hallOfShame.html','w') as hallOfShame:
    hallOfShame.write('')
with open('../_data/members.csv', 'rb') as csvFile:
    hallMembers = csv.reader(csvFile, delimiter="|", quotechar='"')
    for member in hallMembers:
        memberId = member[0]
        name = member[1]
        bio = member[2]
 
        with open('../_includes/hallOfShame.html','a') as hallOfShame:
            hallOfShame.write( sideTemplate%(memberId, memberId, name))

