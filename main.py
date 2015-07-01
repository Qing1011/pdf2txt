#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals
from __future__ import print_function

from bs4 import BeautifulSoup
import codecs
import csv  
import sys 
import os

import pdf2txt as p2t

reload(sys) 
# print (sys.getdefaultencoding())
sys.setdefaultencoding("utf-8")

def getallpdffilename(path):
    pdffilenames=[]
    for dirpath,dirnames,filenames in os.walk(path):
        filenames=filter(lambda filename:filename[-4:]=='.PDF',filenames)
        filenames=map(lambda filename:os.path.join(dirpath,filename),filenames)
        pdffilenames.extend(filenames)
    return pdffilenames

names = getallpdffilename('pdf')

data=[('company_name','report')]


for name in names: 
	print (name)

for name in names:
	result = p2t.convert_pdf_to_txt(name)
        soup = BeautifulSoup(result)
        a_text_b = soup.get_text()
        print (len(a_text_b))
	index_s = result.rfind ('第四节', 0, len(a_text_b))
        print (index_s)
	index_e = result.rfind ('第五节', 0, len(a_text_b))
	report = a_text_b[index_s:index_e]
	company_name = a_text_b[0:16]
        a = (company_name.decode('utf-8'),report.decode('utf-8'))
        data.append(a) 

print (sys.getdefaultencoding())

print (type(data))

with open('names.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)


csvfile.close()

