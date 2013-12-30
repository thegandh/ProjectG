#!/usr/bin/python

import gdata.spreadsheet.service
import gdata.spreadsheet.text_db
import sys
# Using a template, generate the resource.html file

if len(sys.argv) != 2:
    print "Need the password as the first argument"
    sys.exit(1)

PASSWORD = sys.argv[1]

resourceHeader = """---
layout: default
title: Resources
---
<div><h1>Resources</h1></div>

<div class="row">
  <div class="col-md-8">
    <ul>
"""

resourceFooter = """
    </ul>
  </div>
</div>
"""

resourceTemplate = """<li> <a name="%s">[%s]</a> <i>%s</i> %s </li> \n """

with open('../resources.html','w') as resource:
    resource.write('')

sclient = gdata.spreadsheet.service.SpreadsheetsService()
sclient.ClientLogin('thegandh@gmail.com', PASSWORD)
key='0Ah-dviLqoUPxdGp3aXNGLXNJRnN5VkR3SzhsY3hlTXc'
feed = sclient.GetListFeed(key)
mySourceList = []
with open('../resources.html','a') as resource:
    resource.write(resourceHeader)
    for row in feed.entry:
        record = gdata.spreadsheet.text_db.Record(row_entry=row)
        shortKey = record.content['shortkey']
        title = record.content['title'].encode('utf-8')
        author = record.content['author'].encode('utf-8')
        resource.write(resourceTemplate%(shortKey, shortKey, title, author))
    resource.write('</ul>\n\n')
 
