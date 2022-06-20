#!/usr/bin/env python3
# common log format to tsv

import sys
import re
import datetime
import argparse
import gzip

time_ptn = re.compile(r'\[(.*)\]')

def parse_file(f):
    for l in f:
        items = re.findall(r'(\[.+?\]|".+?"|[^ ]+)',l.strip())
        new_items = []
        for item in items:
            m = time_ptn.match(item)
            if m:
                # [20/Jun/2022:21:24:11 +0900]
                item = datetime.datetime.strptime(m.group(1), '%d/%b/%Y:%H:%M:%S %z').isoformat()
            else:
                item = item.strip('"')
            new_items.append(item)
        print("\t".join(new_items))

parser = argparse.ArgumentParser()
parser.add_argument('files', nargs='*')
args = parser.parse_args()

files = args.files

if len(files) == 0:
    parse_file(sys.stdin)
else:
    for f in files:
        if f.endswith('.gz'):
            with gzip.open(f, mode='rt') as logfile:
                parse_file(logfile)
        else:
            with open(f) as logfile:
                parse_file(logfile)

