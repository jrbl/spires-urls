#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Extract http urls from a file.  Assumes roughly one url per line.
#
# Original version was a 1-liner:
# [open("urls-http-"+S, 'w').writelines([m.group('url')+'\n' for m in [re.search('(?P<url>http:\/\/[a-zA-Z0-9_-]+\.(?:[a-zA-Z0-9_-]+\.?)+(?:[a-zA-Z0-9_./-]+)*)', l) for l in open("descrip-http-"+S)] if m != None]) for S in [x[13:] for x in os.listdir(os.getcwd()) if x.startswith('descrip-http-')]]

import os
import re
import sys

def get_http_files(prefix):
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
        year = filename[:4]
        urlfile = open(prefix+year+"-urls.spi", 'w')
        for url in get_file_urls(prefix+filename, urlmatch):
            urlfile.write(url + '\n')
        print "done writing", year+"-urls.spi"

if __name__ == "__main__":
    prefix = sys.argv[1]
    if prefix[-1] != '/':
        prefix += '/'
    main(sys.argv[1])
