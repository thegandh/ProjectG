#!/usr/bin/python

import allData
# Using a template, generate the hallOfShame.html file
# to be put under the _includes directory

hallMembers = allData.allData()

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
    for member in hallMembers:
        hallOfShame.write( sideTemplate%(member, member, hallMembers[member]['name']))

