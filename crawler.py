# encoding: utf-8
from logging import Formatter, handlers, getLogger, StreamHandler, DEBUG
import pdb

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

SP_UA = '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 Mobile/14C92 Safari/602.1'
PC_UA = '--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'

class Crawler():

    def __init__(self, name=None):
        name = name or self.__class__.__name__.rsplit('.', 1)[-1]
        logger = getLogger(name)
        if len(logger.handlers) == 0:
            logger.setLevel(DEBUG)
            formatter = Formatter('\033[32m[%(asctime)s][{}]\033[0m%(message)s'.format(name), 
                                  '%y-%m-%d %H:%M:%S')
            handler = StreamHandler()
            handler.setLevel(DEBUG)
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            self.logger = logger
        self.logger = logger

    def init_chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument(PC_UA)
        self.chrome = webdriver.Chrome(chrome_options = options,
                                       executable_path='/usr/local/chromedriver')

    def get(self, url):
        return requests.get(url, headers={'User-Agent': PC_UA})

    @property
    def d(self):
        return pdb.set_trace

    def p(self, *text):
        if isinstance(text[0], pd.DataFrame):
            self.logger.info("\n" + str(text[0]))
        else:
            self.logger.info(" ".join([str(x) for x in text]))
