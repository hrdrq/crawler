# encoding: utf-8
import os
import re
from time import sleep
import argparse

from bs4 import BeautifulSoup

from crawler import Crawler

BASE_URL = 'https://www.putclub.com/'
URL = BASE_URL + 'portal.php?mod=list&catid=57&page={}'

class Putclub(Crawler):

    def __init__(self):
        super().__init__()

    def get_links(self, page):
        r = self.get(URL.format(page))
        soup = BeautifulSoup(r.text, 'lxml')
        res = []
        regex = '(\d+)-(\d+)'
        a_all = soup.select('div.articlelist-listleftmain a')
        for a in a_all:
            if a.find('h4'):
                m = re.search(regex, a.text)
                try:
                    episode = '{:02d}{:02d}'.format(int(m.group(1)), int(m.group(2)))
                    res.append((episode, a['href']))
                except Exception as e:
                    print('a.text: ', a.text)
                    raise e
        return res

    def get_file_url(self, link):
        r = self.get(BASE_URL + link)
        soup = BeautifulSoup(r.text, 'lxml')
        file_url = soup.find('audio')['src']
        return file_url

    def run(self, dest_dir):
        os.makedirs(dest_dir , exist_ok=True)
        for i in range(1, 16 + 1):
            links = self.get_links(i)
            for episode, link in links:
                file_name = os.path.join(dest_dir, "{}.mp3".format(episode))
                file_url = self.get_file_url(link)
                print('downloading', file_url)
                res = self.get(file_url)
                print('downloaded')
                with open(file_name, 'wb') as f:
                    f.write(res.content)
                sleep(1)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dest_dir')
    a = parser.parse_args()

    Putclub().run(a.dest_dir)
