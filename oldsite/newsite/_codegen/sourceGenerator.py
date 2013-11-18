#!/usr/bin/python

import gdata.spreadsheet.service
import gdata.spreadsheet.text_db
import sys
# Using a template, generate the source.html file

if len(sys.argv) != 2:
    print "Need the password as the first argument"
    sys.exit(1)

PASSWORD = sys.argv[1]

sourceHeader = """---
layout: default
title: Sources
---
<div><h1>Sources</h1></div>

<div class="row">
  <div class="col-md-8">
    <ol>
"""

sourceFooter = """
    </ol>
  </div>
</div>
"""

sourceTemplate = """<li> <a name="%s">[%s]</a> <i>%s</i> %s </li> \n """

with open('../sources.html','w') as source:
    source.write('')

sclient = gdata.spreadsheet.service.SpreadsheetsService()
sclient.ClientLogin('thegandh@gmail.com', PASSWORD)
key='0Ah-dviLqoUPxdGp3aXNGLXNJRnN5VkR3SzhsY3hlTXc'
feed = sclient.GetListFeed(key)
mySourceList = []
with open('../sources.html','a') as source:
    source.write(sourceHeader)
    for row in feed.entry:
        record = gdata.spreadsheet.text_db.Record(row_entry=row)
        shortKey = record.content['shortkey']
        title = record.content['title'].encode('utf-8')
        author = record.content['author'].encode('utf-8')
        source.write(sourceTemplate%(shortKey, shortKey, title, author))
    source.write('</ol>\n\n')
 
