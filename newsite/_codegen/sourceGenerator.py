#!/usr/bin/python

import csv
# Using a template, generate the source.html file

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

sourceTemplate = """<li> <a name="%s">[%s]</a> <i>%s</i> %s </li> """

with open('../sources.html','w') as source:
    source.write('')
with open('../_data/sources.csv', 'rb') as csvFile:
    source = csv.reader(csvFile, delimiter="|", quotechar='"')
    with open('../sources.html','a') as sourceFile:
        sourceFile.write(sourceHeader)
        for src in source:
            anchorName  = src[0]
            shortKey    = src[1]
            title       = src[2]
            author      = src[3]
            sourceFile.write(sourceTemplate%(anchorName, shortKey, title, author))
        sourceFile.write('</ol>\n\n')
