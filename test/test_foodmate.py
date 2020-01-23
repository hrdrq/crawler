# encoding: utf-8
import json
from unittest import TestCase
from unittest.mock import Mock, patch, PropertyMock

import vcr

from foodmate import Foodmate

def pp(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))

class TestFoodmate(TestCase):

    def test_get_links(self):
        with vcr.use_cassette('test/vcr_cassettes/foodmate.yaml'):
            Foodmate().get_links()

    def test_get_file_url(self):
        with vcr.use_cassette('test/vcr_cassettes/foodmate_get_file.yaml'):
            Foodmate().get_file_url('http://www.tingroom.com/lesson/sixpeople1/23951.html')

    # def test_run(self):
    #     fm = Foodmate()
    #     with vcr.use_cassette('test/vcr_cassettes/foodmate.yaml'):
    #         links = fm.get_links()
    #
    #     fm.init_chrome()
    #     fm.save(links)
