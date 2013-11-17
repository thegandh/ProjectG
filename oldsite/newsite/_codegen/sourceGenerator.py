#!/usr/bin/python

import csv
# Using a template, generate the source.html file

DELIMITER='|'
QUOTECHAR='^'

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
with open('../_data/sources.csv', 'rb') as csvFile:
    source = csv.reader(csvFile, delimiter=DELIMITER, quotechar=QUOTECHAR)
    source = sorted(source, key=lambda tag: tag[0])
    with open('../sources.html','a') as sourceFile:
        sourceFile.write(sourceHeader)
        for src in source:
            shortKey    = src[0]
            title       = src[1]
            author      = src[2]
            sourceFile.write(sourceTemplate%(shortKey, shortKey, title, author))
        sourceFile.write('</ol>\n\n')
