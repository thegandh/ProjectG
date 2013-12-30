#!/usr/bin/python

import gdata.spreadsheet.service
import gdata.spreadsheet.text_db
import sys
# Using a template, generate the person files 

if len(sys.argv) != 2:
    print "Need the password as the first argument"
    sys.exit(1)

PASSWORD = sys.argv[1]


personHeader = """---
title: %s
layout: person
bio: %s
pic: "%s.jpg"
---

  <div class="col-md-8 col-md-offset-3">
    <ul>
"""

personFooter = """
    </ul>
  </div>
  <div class="col-md-1">&nbsp;</div>
"""

gandhTemplate = """
    <li>
      <p class="lead">%s</p>
      <p>%s</p> {<a href="resources.html#%s">Source: %s %s</a>}
    </li>
    <br />
"""

sclient = gdata.spreadsheet.service.SpreadsheetsService()
sclient.ClientLogin('thegandh@gmail.com', PASSWORD)
key='0Ah-dviLqoUPxdEo1Qm90eDA0cVBhdml1ckpGNVJJUVE'
feed = sclient.GetListFeed(key)
for row in feed.entry:
    record = gdata.spreadsheet.text_db.Record(row_entry=row)
    memberId = record.content['id']
    name = record.content['name']
    bio = record.content['bio']
    docKey = record.content['dockey']
    with open ('../%s.html'%memberId, 'w') as memberFile:
        memberFile.write(personHeader%(name, bio, memberId))
        memberDetailFeed = sclient.GetListFeed(docKey)
        for memberPoint in memberDetailFeed.entry:
            mRecord = gdata.spreadsheet.text_db.Record(row_entry=memberPoint)
            if mRecord.content['point']:
                point = mRecord.content['point'].encode('utf-8')
                blurb = mRecord.content['blurb'].encode('utf-8')
                source = ''
                if mRecord.content['source']:
                    source = mRecord.content['source'].encode('utf-8')
                detail = ''
                if mRecord.content['detail']:
                    detail = mRecord.content['detail'].encode('utf-8')
                    if len(detail) >0:
                        detail = '('+detail+')'
                memberFile.write(gandhTemplate%(point, blurb, source, source, detail))

        memberFile.write(personFooter)
