# encoding: utf-8
import json
from unittest import TestCase
from unittest.mock import Mock, patch, PropertyMock

import vcr

from putclub import Putclub

def pp(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))

class TestPutclub(TestCase):

    def test_get_links(self):
        with vcr.use_cassette('test/vcr_cassettes/putclubpage.yaml'):
            Putclub().get_links(1)

    def test_get_file_url(self):
        with vcr.use_cassette('test/vcr_cassettes/putclub_get_file.yaml'):
            Putclub().get_file_url('html/download/friends/friends10/20081015/8576.html')
