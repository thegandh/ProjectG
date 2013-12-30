#!/usr/bin/python

import gdata.spreadsheet.service
import gdata.spreadsheet.text_db
import sys
# Using a template, generate the faq.html file

if len(sys.argv) != 2:
    print "Need the password as the first argument"
    sys.exit(1)

PASSWORD = sys.argv[1]

faqHeader = """---
layout: default
title: Frequently Asked Questions
---
<div><h1>Frequently Asked Questions</h1></div>

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

with open('../faq.html','w') as faq:
    faq.write('')

sclient = gdata.spreadsheet.service.SpreadsheetsService()
sclient.ClientLogin('thegandh@gmail.com', PASSWORD)
key='0Ah-dviLqoUPxdEtYYlowaFJWLXJ2cE85eTFtWTFseFE'
feed = sclient.GetListFeed(key)
with open('../faq.html','a') as faq:
    faq.write(faqHeader)
    ctr = 0
    for row in feed.entry:
        ctr += 1
        record = gdata.spreadsheet.text_db.Record(row_entry=row)
        question = record.content['question']
        faq.write(srcTemplate%(ctr,question))
    faq.write('</ul>\n\n')

    ctr = 0
    for row in feed.entry:
        ctr += 1
        record = gdata.spreadsheet.text_db.Record(row_entry=row)
        question = record.content['question']
        answer = record.content['answer'].encode('utf-8')
        faq.write(faqTemplate%(ctr,question,answer))
