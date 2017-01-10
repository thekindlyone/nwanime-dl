#!/usr/bin/python
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
import logging

def get_ext(video_url):
    """get extention of file from video url"""
    components = urlparse(video_url)
    return splitext(components.path)[-1]



def download(url):
    """
    Downloads video in url. 
    download(url)
    """
    vidname = get_vidname(url)
    logging.info(vidname)
    logging.debug('fetching mirrors')
    mirrors = get_mirrors(url)
    logging.debug('mirrors found')
    for mirror, link in mirrors:
        if mirror in regexes.extractors:
            logging.debug('downloadable mirror found '+mirror)
            jsfile = fetch_js(link)
            logging.debug('JS link: '+jsfile)
            if jsfile:
                r = requests.get(jsfile)
                if r.status_code == 200:
                    video = re.search(regexes.extractors[mirror], r.content)
                    if video:
                        video = video.group(1)
                        outfile = vidname + get_ext(video)
                        logging.info('attempting download from '+ mirror)
                        wget = subprocess.Popen(['wget','--continue','-O', outfile, video])
                        wget.wait()
                        return wget.returncode,vidname
    else:
        logging.error( "Can't Download. No downloadable mirrors found. Sorry.")
        return 1,vidname

def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
        download(url)
    else:
        print 'usage :nwanime-dl <url>'
        sys.exit(1)



if __name__ == '__main__':
    main()
