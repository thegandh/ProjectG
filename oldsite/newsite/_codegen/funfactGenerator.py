#!/usr/bin/python

import gdata.spreadsheet.service
import gdata.spreadsheet.text_db
import sys
# Using a template, generate the funfacts.html file

if len(sys.argv) != 2:
    print "Need the password as the first argument"
    sys.exit(1)

PASSWORD = sys.argv[1]

funfactHeader = """---
layout: default
title: "Fun Facts"
---

<div class="page-header">
  <h1>Fun Facts</h1>
</div>

<div class="row">
  <div class="col-md-8 col-md-offset-3">
    <ul>
"""

funfactFooter = """
    </ul>
  </div>
  <div class="col-md-1">&nbsp;</div>
</div>
"""

funTemplate = """
<li>%s <i>{Source: <a href="sources.html#%s">%s</a>}</i> </li>
<br />\n
"""

with open('../funfacts.html','w') as funfact:
    funfact.write('')

sclient = gdata.spreadsheet.service.SpreadsheetsService()
sclient.ClientLogin('thegandh@gmail.com', PASSWORD)
key='0Ah-dviLqoUPxdG5kbFFBcENuZDNJb2xRMWIxNjRDZlE'
feed = sclient.GetListFeed(key)
with open('../funfacts.html','a') as funfact:
    funfact.write(funfactHeader)
    for row in feed.entry:
        record = gdata.spreadsheet.text_db.Record(row_entry=row)
        blurb = record.content['blurb'].encode('utf-8')
        source = record.content['source']
        funfact.write(funTemplate%(blurb,source,source))
    funfact.write(funfactFooter)
