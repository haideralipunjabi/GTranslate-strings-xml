#!/usr/bin/env python
# -*- coding: utf-8 -*-


INFILE='teststrings.xml'
OUTFILE='teststrings.txt'

import xml.etree.ElementTree as ET

tree = ET.parse(INFILE)
root = tree.getroot()
file = open(OUTFILE,'w') 

counter=0
    
for i in range(len(root)):
    isTranslatable = root[i].get('translatable')
    if(root[i].tag=='string') & (isTranslatable!='false'):
        counter=counter+1
        file.write(str(counter)+':'+root[i].text+'\n')
    if(root[i].tag=='string-array') & (isTranslatable!='false'):
        for j in range(len(root[i])):	
            if(root[i][j].tag=='item'):
                counter=counter+1
                file.write(str(counter)+':'+root[i][j].text+'\n')
file.close()
