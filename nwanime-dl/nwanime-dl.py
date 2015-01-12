# coding: utf-8
import requests
from bs4 import BeautifulSoup
import sys
import subprocess
import re
import regexes
from helper import get_soup, get_mirrors, fetch_js, get_vidname
from urlparse import urlparse
from os.path import splitext

def get_ext(video_url):
    components=urlparse(video_url)
    return splitext(components.path)[-1]

if len(sys.argv)>1:
    url=sys.argv[1]
else:
    print 'usage :nwanime-dl <url>'
vidname=get_vidname(url)
print vidname
print 'fetching mirrors'
mirrors=get_mirrors(url)
print 'mirrors found'
for mirror,link in mirrors:
    if mirror in regexes.extractors:
        print 'downloadable mirror found'
        jsfile=fetch_js(link)
        if jsfile:
            r=requests.get(jsfile)
            if r.status_code==200:
                video=re.search(regexes.extractors[mirror],r.content)
                if video:
                    video=video.group(1)
                    outfile=vidname+get_ext(video)
                    print 'attempting download from',mirror
                    wget=subprocess.Popen(['wget','-O',outfile,video])
                    wget.wait()
                    break

print 'File Downloaded'
