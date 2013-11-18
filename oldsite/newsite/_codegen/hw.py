#!/usr/bin/python

#import gdata.docs.service
import gdata.spreadsheet.service
import gdata.spreadsheet.text_db

## Create a client class which will make HTTP requests with Google Docs server.
#client = gdata.docs.service.DocsService()
## Authenticate using your Google Docs email address and password.
#client.ClientLogin('thegandh@gmail.com', 'thisisthegandh12##')
#
## Query the server for an Atom feed containing a list of your documents.
#documents_feed = client.GetDocumentListFeed()
## Loop through the feed and extract each document entry.
#for document_entry in documents_feed.entry:
#  # Display the title of the document on the command line.
#  print document_entry.title.text

sclient = gdata.spreadsheet.service.SpreadsheetsService()
sclient.ClientLogin('thegandh@gmail.com', 'thisisthegandh12##')
key='0Ah-dviLqoUPxdEtYYlowaFJWLXJ2cE85eTFtWTFseFE'
feed = sclient.GetListFeed(key)
for row in feed.entry:
    record = gdata.spreadsheet.text_db.Record(row_entry=row)
    print str(record.content)
