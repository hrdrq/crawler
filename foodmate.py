# encoding: utf-8
import os
import re
from time import sleep
import argparse

from bs4 import BeautifulSoup

from crawler import Crawler

URL = 'http://www.foodmate.net/english/listen/47233.html'
TINGROOM_URL = 'http://www.tingroom.com'

class Foodmate(Crawler):

    def __init__(self):
        super().__init__()
        self.main_url = URL

    def get_links(self):
        r = self.get(self.main_url)
        soup = BeautifulSoup(r.text, 'lxml')
        regex = '.*FriendsMP3 (\d+)[^0-9]+(\d+)'
        res = {}
        tables = soup.select('div#content div.content#article table')
        for table in tables:
            all_a = table.select('td a')
            for a in all_a:
                m = re.match(regex, a.text)
                if m:
                    season = m.group(1)
                    season = '{:02d}'.format(int(season))
                    episode = m.group(2)
                    episode = '{:02d}'.format(int(episode))
                    season_dict = res.get(season, {})
                    season_dict[episode] = a['href']
                    res[season] = season_dict
        return res

    def get_file_url(self, page_url):
        r = self.get(page_url)
        soup = BeautifulSoup(r.text, 'lxml')
        for iframe in soup.find_all('iframe'):
            if iframe['src'].find('.php') != -1:
                page_url = TINGROOM_URL + iframe['src']
                break

        r = self.get(page_url)
        soup = BeautifulSoup(r.text, 'lxml')
        for a in soup.find_all('a'):
            if a.text.find('MP3') != -1:
                page_url = a['href']
                break

        r = self.get(page_url)
        soup = BeautifulSoup(r.text, 'lxml')
        for a in soup.find_all('a'):
            if a['href'].find('.mp3') != -1:
                page_url = a['href']
                # break
        return page_url

    def save(self, links, dest_dir):
        for season, season_dict in links.items():
            season_dir = os.path.join(dest_dir, season)
            os.makedirs(season_dir , exist_ok=True)
            for episode, link in season_dict.items():
                # print(season, episode)
                file_name = os.path.join(season_dir, "{}.mp3".format(episode))
                file_url = self.get_file_url(link)
                print('downloading', file_url)
                res = self.get(file_url)
                print('downloaded')
                with open(file_name, 'wb') as f:
                    f.write(res.content)
                sleep(1)

    def run(self, dest_dir):
        links = self.get_links()
        self.save(links, dest_dir)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dest_dir')
    a = parser.parse_args()

    Foodmate().run(a.dest_dir)
