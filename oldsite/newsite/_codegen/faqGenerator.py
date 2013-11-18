#!/usr/bin/python

import gdata.spreadsheet.service
import gdata.spreadsheet.text_db
import sys
# Using a template, generate the about.html file

if len(sys.argv) != 2:
    print "Need the password as the first argument"
    sys.exit(1)

PASSWORD = sys.argv[1]

faqHeader = """---
layout: default
title: About
---
<div><h1>About</h1></div>

<ul>
"""

faqTemplate = """
<div class="row">
  <div class="col-md-12">
    <h3><a name="faq%s">%s</a></h3>
  </div>
  <div class="col-md-8 col-md-offset-1">
    %s
  </div>
  <div class="col-md-3">&nbsp;</div>
</div>
<br />
"""

srcTemplate = """
<li><a href="#faq%s">%s</a></li>\n
"""

with open('../about.html','w') as about:
    about.write('')

sclient = gdata.spreadsheet.service.SpreadsheetsService()
sclient.ClientLogin('thegandh@gmail.com', PASSWORD)
key='0Ah-dviLqoUPxdEtYYlowaFJWLXJ2cE85eTFtWTFseFE'
feed = sclient.GetListFeed(key)
with open('../about.html','a') as about:
    about.write(faqHeader)
    ctr = 0
    for row in feed.entry:
        ctr += 1
        record = gdata.spreadsheet.text_db.Record(row_entry=row)
        question = record.content['question']
        about.write(srcTemplate%(ctr,question))
    about.write('</ul>\n\n')

    ctr = 0
    for row in feed.entry:
        ctr += 1
        record = gdata.spreadsheet.text_db.Record(row_entry=row)
        question = record.content['question']
        answer = record.content['answer'].encode('utf-8')
        about.write(faqTemplate%(ctr,question,answer))
