#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Opens the urls file and counts how many of it's URLs are valid.
#
# urls file generated by running:
# [open("urls-http-"+S, 'w').writelines([m.group('url')+'\n' for m in [re.search('(?P<url>http:\/\/[a-zA-Z0-9_-]+\.(?:[a-zA-Z0-9_-]+\.?)+(?:[a-zA-Z0-9_./-]+)*)', l) for l in open("descrip-http-"+S)] if m != None]) for S in [x[13:] for x in os.listdir(os.getcwd()) if x.startswith('descrip-http-')]]


import sys
import urllib2
import pickle


def test_urls(filename, LIVE, DEAD):
    file = open(filename)
    for url in file:
        url = url.strip()
        try:
            pg = urllib2.urlopen(url)
            LIVE[url] = pg.info()
            print url, "alive"
        except urllib2.URLError, msg:
            DEAD[url] = str(msg)
            print url, "dead"
        except KeyboardInterrupt:
            raise
        except Exception, msg:
            DEAD[url] = str(msg)
            print url, "confusing; presumed dead."
    file.close()

def main():
    for infilename in sys.argv[1:]:
        LIVE = {}
        DEAD = {}
        outfilenamelive = infilename + ".LIVE.pickle"
        outfilenamedead = infilename + ".DEAD.pickle"
        test_urls(infilename, LIVE, DEAD)

        print "LIVE:", [site for site in LIVE]
        outfile = open(outfilenamelive, 'wb')
        pickle.dump(LIVE, outfile)
        outfile.close()

        print "DEAD:", [site for site in DEAD]
        outfile = open(outfilenamedead, 'wb')
        pickle.dump(DEAD, outfile)
        outfile.close()

        print "Live: %d\nDead: %d" % (len(LIVE), len(DEAD))

if __name__ == "__main__":
    main()
