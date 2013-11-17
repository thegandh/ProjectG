#!/usr/bin/python

import csv
# Using a template, generate the hallOfShame.html file
# to be put under the _includes directory

DELIMITER='|'
QUOTECHAR='^'

sideTemplate = """
<div class="row">
  <a href="%s.html">
    <div class="col-md-3">
      <img src="/images/%s.jpg" class="img-responsive" />
    </div>
    <div class="col-md-9">
      <h3>%s</h3>
    </div>
  </a>
</div>
<br />
"""
with open('../_includes/hallOfShame.html','w') as hallOfShame:
    hallOfShame.write('')
with open('../_data/members.csv', 'rb') as csvFile:
    hallMembers = csv.reader(csvFile,delimiter=DELIMITER, quotechar=QUOTECHAR)
    for member in hallMembers:
        memberId = member[0]
        name = member[1]
        bio = member[2]
 
        with open('../_includes/hallOfShame.html','a') as hallOfShame:
            hallOfShame.write( sideTemplate%(memberId, memberId, name))

