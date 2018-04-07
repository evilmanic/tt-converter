#!/usr/bin/env python

from __future__ import print_function, unicode_literals

import os
import time
import sys
import requests
import csv
import collections


# Load the file

with open('ClicksOnlyByClient.csv', encoding="latin-1") as infile:
    counts = collections.Counter(l.strip() for l in infile)
for line, count in counts.most_common():
    print (line, count, sep=',')
		
	

