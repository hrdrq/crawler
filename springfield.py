# encoding: utf-8
import os
from time import sleep
import argparse

from bs4 import BeautifulSoup

from crawler import Crawler

BASE_URL = 'https://www.springfieldspringfield.co.uk/'
URL = BASE_URL + 'episode_scripts.php?tv-show={}'

class Springfield(Crawler):

    def __init__(self, drama):
        super().__init__()
        self.main_url = URL.format(drama)

    def get_episodes(self):
        r = self.get(self.main_url)
        soup = BeautifulSoup(r.text, 'lxml')
        seasons = soup.find_all('div', class_="season-episodes")
        res = [
            {
                # "Season 1" -> "1"
                "season": s.find("h3").text[7:],
                "episodes": [
                    {
                        "episode": a.text[:a.text.find('.')],
                        "link": a['href']
                    }
                    for a in s.find_all("a", class_="season-episode-title")
                ]
            }
            for s in seasons
        ]
        return res

    def get_transcript(self, url):
        r = self.get(BASE_URL + url)
        soup = BeautifulSoup(r.text, 'lxml')
        return soup.find('div', class_='scrolling-script-container').get_text(separator="\n").strip()

    def save(self, dest_dir, ep_dict):
        for d in ep_dict:
            season = d["season"]
            season_dir = os.path.join(dest_dir, "{:02d}".format(int(season)))
            os.makedirs(season_dir , exist_ok=True)
            for ep in d["episodes"]:
                episode = ep["episode"]
                file_name = os.path.join(season_dir, "{:02d}.txt".format(int(episode)))
                with open(file_name, "w") as f:
                    f.write(self.get_transcript(ep["link"]))
                sleep(1)


    def run(self, dest_dir):
        ep_dict = self.get_episodes()
        self.save(dest_dir, ep_dict)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('drama')
    parser.add_argument('dest_dir')
    a = parser.parse_args()

    Springfield(a.drama).run(a.dest_dir)
