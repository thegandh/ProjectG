#!/usr/bin/python

import csv
# Using a template, generate the about.html file

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
  <div class="col-md-12">
    %s
  </div>
</div>
<br />
"""

with open('../about.html','w') as about:
    about.write('')
with open('faq.csv', 'rb') as csvFile:
    faq = csv.reader(csvFile, delimiter="|", quotechar='"')
    faqCopy = []
    with open('../about.html','a') as about:
        about.write(faqHeader)
        ctr = 0
        for qa in faq:
            faqCopy.append(qa)
            ctr += 1
            question = qa[0]
            about.write('<li><a href="#faq%s">%s</a></li>\n'%(ctr,question))
        about.write('</ul>\n\n')

        ctr = 0
        print "NOW"
        for qa in faqCopy:
            ctr += 1
            question = qa[0]
            answer = qa[1]
            print question
            about.write(faqTemplate%(ctr,question,answer))

