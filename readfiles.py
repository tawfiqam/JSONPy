import bz2
import json
import datetime
import os
import profile
import psycopg2
from pprint import pprint
import gzip
#end imports


filename = "2007/RC_2007-10.bz2"
with gzip.GzipFile(filename, 'r') as newFile:
	for line in newFile:
		obj = json.loads(line)
		if obj['parenting']:
			print(obj)


#bz_file = bz2.BZ2File(filename)
#line_list = bz_file.readlines()
#print(line_list)
