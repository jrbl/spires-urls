#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Extract http urls from a file.  Assumes roughly one url per line.

import os
import re
import sys

def get_http_files():
    for filename in os.listdir(prefix):
        if filename.endswith('-http.spi'):
            yield filename

def get_file_urls(filename, urlmatch):
    file = open(filename)
    print "Opened %s" % filename
    for line in file:
        m = urlmatch.search(line)
        if m:
            yield m.group('url')

def main(prefix):
    urlmatch = re.compile('(?P<url>http:\/\/[a-zA-Z0-9_-]+\.(?:[a-zA-Z0-9_-]+\.?)+(?:[a-zA-Z0-9_./-]+)*)')
    for filename in get_http_files(prefix):
        year = filename[12:]
        urlfile = open(prefix+'/'+year+"-urls.spi" + year, 'w')
        for url in get_file_urls(prefix+'/'+filename, urlmatch):
            urlfile.write(url + '\n')
        print "done writing", year+"-urls.spi"

if __name__ == "__main__":
    main(sys.argv[1])
