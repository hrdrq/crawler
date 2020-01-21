# encoding: utf-8
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

    def run(self):
        self.get_episodes()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('drama')
    a = parser.parse_args()

    Springfield(a.drama).run()
