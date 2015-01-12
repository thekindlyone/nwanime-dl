# coding: utf-8
import requests
from bs4 import BeautifulSoup as bs
from itertools import chain
import random
import pickle
from pprint import pprint
from os.path import exists

mirror_table = 'mirror_table.p'
allanimes = 'allanimes.p'
reject_list = ['facebook', 'bit.ly']


def get_soup(url):
    r = requests.get(url)
    if r.status_code == 200:
        return bs(r.content)
    else:
        return False

# results > div:nth-child(10) > a:nth-child(1)


def make_pickle():
    url = 'http://www.nwanime.com/categories/'
    soup = get_soup(url)
    tuples = [(anchor.text, anchor.get('href'))
              for anchor in soup.select('#results > div > a:nth-of-type(1)')]
    with open('allanimes.p', 'w') as f:
        pickle.dump(tuples, f)


def get_animes_sample():
    f = open(allanimes)
    animes = pickle.load(f)
    return random.sample(animes, 10)


def get_random_episode(url):
    soup = get_soup(url)
    try:
        episodes = [anchor.get('href') for anchor in soup.select(
            '#resultstats_large > div > a') if anchor.text.strip()]
        episode = random.choice(episodes)
    except:
        episode = None
    return episode


def get_mirrors(url):
    soup = get_soup(url)
    try:
        mirrors = [(anchor.text.split()[0], anchor.get('href'))
                   for anchor in soup.select('#video_mirrors > div > span.link > a') if '[US only]' not in anchor.text]
    except:
        mirrors = None
    return mirrors


class Table(object):

    def __init__(self):
        self.table = self.get_table()

    def get_table(self):
        if exists(mirror_table):
            with open(mirror_table) as f:
                table = pickle.load(f)
        else:
            table = {}
        return table

    def update(self):
        with open(mirror_table, 'w') as f:
            pickle.dump(self.table, f)


def fetch_js(url):
    soup = get_soup(url)
    try:
        js = soup.select('#embed_holder > iframe')[0].get('src', None)
    except:
        js = None
    return js


def get_vidname(url):
    soup = get_soup(url)
    try:
        name = soup.select('#content_head > a:nth-of-type(3)')[0].text
    except:
        name = None
    return name


def main():
    if not exists(allanimes):
        make_pickle()
    animes = get_animes_sample()
    t = Table()
    for anime, url in animes:
        episode = get_random_episode(url)
        if episode:
            print '\n', episode
            mirrors = get_mirrors(episode)
            if mirrors:
                for name, murl in mirrors:
                    if name not in t.table.keys():
                        js = fetch_js(murl)
                        if js and all(rejectable not in js for rejectable in reject_list):
                            t.table[name] = js
                            print name, '   ', t.table[name]

    t.update()


if __name__ == '__main__':
    main()
