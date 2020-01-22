# encoding: utf-8
import json
from unittest import TestCase
from unittest.mock import Mock, patch, PropertyMock

import vcr

from springfield import Springfield

def pp(data):
    print(json.dumps(data, indent=2, ensure_ascii=False))

EPISODES = [
  {
    "season": "1",
    "episodes": [
      {
        "episode": "1",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e01"
      },
      {
        "episode": "2",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e02"
      },
      {
        "episode": "3",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e03"
      },
      {
        "episode": "4",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e04"
      },
      {
        "episode": "5",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e05"
      },
      {
        "episode": "6",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e06"
      },
      {
        "episode": "7",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e07"
      },
      {
        "episode": "8",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e08"
      },
      {
        "episode": "9",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e09"
      },
      {
        "episode": "10",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e10"
      },
      {
        "episode": "11",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e11"
      },
      {
        "episode": "12",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e12"
      },
      {
        "episode": "13",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e13"
      },
      {
        "episode": "14",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e14"
      },
      {
        "episode": "15",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e15"
      },
      {
        "episode": "16",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e16"
      },
      {
        "episode": "17",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e17"
      },
      {
        "episode": "18",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e18"
      },
      {
        "episode": "19",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e19"
      },
      {
        "episode": "20",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e20"
      },
      {
        "episode": "21",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e21"
      },
      {
        "episode": "22",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e22"
      },
      {
        "episode": "23",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e23"
      },
      {
        "episode": "24",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s01e24"
      }
    ]
  },
  {
    "season": "2",
    "episodes": [
      {
        "episode": "1",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e01"
      },
      {
        "episode": "2",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e02"
      },
      {
        "episode": "3",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e03"
      },
      {
        "episode": "4",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e04"
      },
      {
        "episode": "5",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e05"
      },
      {
        "episode": "6",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e06"
      },
      {
        "episode": "7",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e07"
      },
      {
        "episode": "8",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e08"
      },
      {
        "episode": "9",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e09"
      },
      {
        "episode": "10",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e10"
      },
      {
        "episode": "11",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e11"
      },
      {
        "episode": "12",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e12"
      },
      {
        "episode": "14",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e14"
      },
      {
        "episode": "15",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e15"
      },
      {
        "episode": "16",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e16"
      },
      {
        "episode": "17",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e17"
      },
      {
        "episode": "18",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e18"
      },
      {
        "episode": "19",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e19"
      },
      {
        "episode": "20",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e20"
      },
      {
        "episode": "21",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e21"
      },
      {
        "episode": "22",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e22"
      },
      {
        "episode": "23",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e23"
      },
      {
        "episode": "24",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s02e24"
      }
    ]
  },
  {
    "season": "3",
    "episodes": [
      {
        "episode": "1",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e01"
      },
      {
        "episode": "2",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e02"
      },
      {
        "episode": "3",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e03"
      },
      {
        "episode": "4",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e04"
      },
      {
        "episode": "5",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e05"
      },
      {
        "episode": "6",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e06"
      },
      {
        "episode": "7",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e07"
      },
      {
        "episode": "8",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e08"
      },
      {
        "episode": "9",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e09"
      },
      {
        "episode": "10",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e10"
      },
      {
        "episode": "11",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e11"
      },
      {
        "episode": "12",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e12"
      },
      {
        "episode": "13",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e13"
      },
      {
        "episode": "14",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e14"
      },
      {
        "episode": "15",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e15"
      },
      {
        "episode": "16",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e16"
      },
      {
        "episode": "17",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e17"
      },
      {
        "episode": "18",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e18"
      },
      {
        "episode": "19",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e19"
      },
      {
        "episode": "20",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e20"
      },
      {
        "episode": "21",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e21"
      },
      {
        "episode": "22",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e22"
      },
      {
        "episode": "23",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e23"
      },
      {
        "episode": "24",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e24"
      },
      {
        "episode": "25",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s03e25"
      }
    ]
  },
  {
    "season": "4",
    "episodes": [
      {
        "episode": "1",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e01"
      },
      {
        "episode": "2",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e02"
      },
      {
        "episode": "3",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e03"
      },
      {
        "episode": "4",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e04"
      },
      {
        "episode": "5",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e05"
      },
      {
        "episode": "6",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e06"
      },
      {
        "episode": "7",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e07"
      },
      {
        "episode": "8",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e08"
      },
      {
        "episode": "9",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e09"
      },
      {
        "episode": "10",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e10"
      },
      {
        "episode": "11",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e11"
      },
      {
        "episode": "12",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e12"
      },
      {
        "episode": "13",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e13"
      },
      {
        "episode": "14",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e14"
      },
      {
        "episode": "15",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e15"
      },
      {
        "episode": "16",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e16"
      },
      {
        "episode": "17",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e17"
      },
      {
        "episode": "18",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e18"
      },
      {
        "episode": "19",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e19"
      },
      {
        "episode": "20",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e20"
      },
      {
        "episode": "21",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e21"
      },
      {
        "episode": "22",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e22"
      },
      {
        "episode": "23",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s04e23"
      }
    ]
  },
  {
    "season": "5",
    "episodes": [
      {
        "episode": "1",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e01"
      },
      {
        "episode": "2",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e02"
      },
      {
        "episode": "3",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e03"
      },
      {
        "episode": "4",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e04"
      },
      {
        "episode": "5",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e05"
      },
      {
        "episode": "6",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e06"
      },
      {
        "episode": "7",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e07"
      },
      {
        "episode": "8",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e08"
      },
      {
        "episode": "9",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e09"
      },
      {
        "episode": "10",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e10"
      },
      {
        "episode": "11",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e11"
      },
      {
        "episode": "12",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e12"
      },
      {
        "episode": "13",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e13"
      },
      {
        "episode": "14",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e14"
      },
      {
        "episode": "15",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e15"
      },
      {
        "episode": "16",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e16"
      },
      {
        "episode": "17",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e17"
      },
      {
        "episode": "18",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e18"
      },
      {
        "episode": "19",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e19"
      },
      {
        "episode": "20",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e20"
      },
      {
        "episode": "21",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e21"
      },
      {
        "episode": "22",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e22"
      },
      {
        "episode": "23",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e23"
      },
      {
        "episode": "24",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s05e24"
      }
    ]
  },
  {
    "season": "6",
    "episodes": [
      {
        "episode": "1",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e01"
      },
      {
        "episode": "2",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e02"
      },
      {
        "episode": "3",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e03"
      },
      {
        "episode": "4",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e04"
      },
      {
        "episode": "5",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e05"
      },
      {
        "episode": "6",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e06"
      },
      {
        "episode": "7",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e07"
      },
      {
        "episode": "8",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e08"
      },
      {
        "episode": "9",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e09"
      },
      {
        "episode": "10",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e10"
      },
      {
        "episode": "11",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e11"
      },
      {
        "episode": "12",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e12"
      },
      {
        "episode": "13",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e13"
      },
      {
        "episode": "14",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e14"
      },
      {
        "episode": "15",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e15"
      },
      {
        "episode": "16",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e16"
      },
      {
        "episode": "17",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e17"
      },
      {
        "episode": "18",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e18"
      },
      {
        "episode": "19",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e19"
      },
      {
        "episode": "20",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e20"
      },
      {
        "episode": "21",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e21"
      },
      {
        "episode": "22",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e22"
      },
      {
        "episode": "23",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e23"
      },
      {
        "episode": "24",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e24"
      },
      {
        "episode": "25",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s06e25"
      }
    ]
  },
  {
    "season": "7",
    "episodes": [
      {
        "episode": "1",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e01"
      },
      {
        "episode": "2",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e02"
      },
      {
        "episode": "3",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e03"
      },
      {
        "episode": "4",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e04"
      },
      {
        "episode": "5",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e05"
      },
      {
        "episode": "6",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e06"
      },
      {
        "episode": "7",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e07"
      },
      {
        "episode": "8",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e08"
      },
      {
        "episode": "9",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e09"
      },
      {
        "episode": "10",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e10"
      },
      {
        "episode": "11",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e11"
      },
      {
        "episode": "12",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e12"
      },
      {
        "episode": "13",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e13"
      },
      {
        "episode": "14",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e14"
      },
      {
        "episode": "15",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e15"
      },
      {
        "episode": "16",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e16"
      },
      {
        "episode": "17",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e17"
      },
      {
        "episode": "18",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e18"
      },
      {
        "episode": "19",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e19"
      },
      {
        "episode": "20",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e20"
      },
      {
        "episode": "21",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e21"
      },
      {
        "episode": "22",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e22"
      },
      {
        "episode": "23",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e23"
      },
      {
        "episode": "24",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s07e24"
      }
    ]
  },
  {
    "season": "8",
    "episodes": [
      {
        "episode": "1",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e01"
      },
      {
        "episode": "2",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e02"
      },
      {
        "episode": "3",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e03"
      },
      {
        "episode": "4",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e04"
      },
      {
        "episode": "5",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e05"
      },
      {
        "episode": "6",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e06"
      },
      {
        "episode": "7",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e07"
      },
      {
        "episode": "8",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e08"
      },
      {
        "episode": "9",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e09"
      },
      {
        "episode": "10",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e10"
      },
      {
        "episode": "11",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e11"
      },
      {
        "episode": "12",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e12"
      },
      {
        "episode": "13",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e13"
      },
      {
        "episode": "14",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e14"
      },
      {
        "episode": "15",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e15"
      },
      {
        "episode": "16",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e16"
      },
      {
        "episode": "17",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e17"
      },
      {
        "episode": "18",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e18"
      },
      {
        "episode": "19",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e19"
      },
      {
        "episode": "20",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e20"
      },
      {
        "episode": "21",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e21"
      },
      {
        "episode": "22",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e22"
      },
      {
        "episode": "23",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e23"
      },
      {
        "episode": "24",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s08e24"
      }
    ]
  },
  {
    "season": "9",
    "episodes": [
      {
        "episode": "1",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e01"
      },
      {
        "episode": "2",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e02"
      },
      {
        "episode": "3",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e03"
      },
      {
        "episode": "4",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e04"
      },
      {
        "episode": "5",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e05"
      },
      {
        "episode": "6",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e06"
      },
      {
        "episode": "7",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e07"
      },
      {
        "episode": "8",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e08"
      },
      {
        "episode": "9",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e09"
      },
      {
        "episode": "10",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e10"
      },
      {
        "episode": "11",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e11"
      },
      {
        "episode": "12",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e12"
      },
      {
        "episode": "13",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e13"
      },
      {
        "episode": "14",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e14"
      },
      {
        "episode": "15",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e15"
      },
      {
        "episode": "16",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e16"
      },
      {
        "episode": "17",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e17"
      },
      {
        "episode": "18",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e18"
      },
      {
        "episode": "19",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e19"
      },
      {
        "episode": "20",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e20"
      },
      {
        "episode": "21",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e21"
      },
      {
        "episode": "22",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e22"
      },
      {
        "episode": "23",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e23"
      },
      {
        "episode": "24",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s09e24"
      }
    ]
  },
  {
    "season": "10",
    "episodes": [
      {
        "episode": "1",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e01"
      },
      {
        "episode": "2",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e02"
      },
      {
        "episode": "3",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e03"
      },
      {
        "episode": "4",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e04"
      },
      {
        "episode": "5",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e05"
      },
      {
        "episode": "6",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e06"
      },
      {
        "episode": "7",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e07"
      },
      {
        "episode": "8",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e08"
      },
      {
        "episode": "9",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e09"
      },
      {
        "episode": "10",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e10"
      },
      {
        "episode": "11",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e11"
      },
      {
        "episode": "12",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e12"
      },
      {
        "episode": "13",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e13"
      },
      {
        "episode": "14",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e14"
      },
      {
        "episode": "15",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e15"
      },
      {
        "episode": "16",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e16"
      },
      {
        "episode": "17",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e17"
      },
      {
        "episode": "18",
        "link": "view_episode_scripts.php?tv-show=friends&episode=s10e18"
      }
    ]
  }
]

TRANSCRIPT = \
"""The One Where It All Began (Pilot) There's nothing to tell.
 It's just some guy I work with.
 You're going out with the guy.
 There has to be something wrong with him.
 All right, Joey.
 Be nice.
 So does he have a hump and a hairpiece? Wait, does he eat chalk? I don't want her to go through what I did with Carl.
 Okay, everybody relax.
 This is not even a date.
 It's just two people going out to dinner and not having sex.
 Sounds like a date to me.
 I'm in high school, in the cafeteria.
.
 and I realize I'm totally naked.
 I've had that dream.
 Then I look down and I realize there is a phone.
.
 there.
 - Instead of - That's right! Never had that one.
 All of a sudden, the phone starts to ring.
 What do I do? Everyone starts looking at me.
 They weren't looking at you before? Finally, I figure I'd better answer it.
 And it turns out it's my mother.
 Which is very, very weird because she never calls me.
 Hi.
 He says, "Hello," I want to kill myself.
 You okay? I feel like someone pulled my intestine out of my mouth.
.
 - and tied it around my neck.
 - Cookie? Carol moved her stuff out today.
 - Let me get you some coffee.
 - Thanks.
 No, don't! Stop cleansing my aura.
 - Just leave my aura alone, okay? - Fine, be murky.
 - I'll be fine.
 I hope she'll be happy.
 - No, you don't.
 No, I don't.
 To hell with her.
 She left me! You never knew she was a lesbian? No! Okay? Why does everyone keep fixating on that? She didn't know.
 How should I know? Sometimes I wish I was a lesbian.
 Did I say that out loud? I told Mom and Dad last night.
 They took it pretty well.
 Oh, really? So that hysterical phone call from a woman sobbing.
.
 "I'll never have grandchildren," was what? A wrong number? Sorry.
 Look, you're feeling a lot of pain right now.
 You're angry.
 You're hurting.
 Can I tell you what the answer is? Strip joints! Hey, you're single.
 Have some hormones.
 But I don't want to be single, okay? I just want to be married again.
 And I just want a million dollars! - Rachel? - Oh, Monica! Thank God! I went to your building.
.
 and a guy with a hammer said you'd be here, and you are.
 - Can I get you some coffee? - Decaf.
 Everybody, this is Rachel, a Lincoln High survivor.
 This is everybody.
 Chandler and Phoebe.
.
 Joey.
 Remember my brother, Ross? Sure! You want to tell us now, or are we waiting for four wet bridesmaids? Well, it started about a half-hour before the wedding.
 I was in the room with all the presents.
.
 and I was looking at this really gorgeous Limoges gravy boat.
 When all of a sudden Sweet 'N Low? I realized I was more turned on by this gravy boat than Barry.
 I got freaked out, and it hit me: How much Barry looks like Mr.
 Potato Head.
 I always knew he looked familiar, but.
.
 I had to get out of there, and I started wondering.
.
 "Why am I doing this," and "Who am I doing it for?" I didn't know where to go, and I know we've drifted apart.
.
 but you're the only person I know here.
 - Who wasn't invited to the wedding.
 - I hoped that wouldn't be an issue.
 I guess he bought her the pipe organ, and she's really not happy about it.
 "Tuna or egg salad! Decide!" "I'll have whatever Christina's having.
" Daddy, I just I can't marry him.
 I'm sorry.
 I just don't love him.
 Well, it matters to me! "If I let go of my hair, my head will fall off.
" She should not be wearing those pants.
 Push her down the stairs! Push her! Push her down the stairs! Come on, Daddy, listen! All my life, everyone's always told me, "You're a shoe!" "You're a shoe!" What if I don't want to be a shoe? What if I want to be a purse? Or a hat? No, I don't want you to buy me a hat! It's a metaphor, Daddy! You can see where he'd have trouble.
 Look, Daddy, it's my life.
 Well, maybe I'll just stay here with Monica.
 I guess we've established she's staying with Monica.
 Well, maybe that's my decision.
 Maybe I don't need your money.
 Wait! I said maybe! Just breathe.
 That's it.
 Try to think of nice, calm things.
 Raindrops on roses And whiskers on kittens Doorbells and sleigh bells And something with mittens La la la something And noodles with string I'm all better now.
 I helped.
 This is probably for the best.
 Independence.
 Controlling your life.
 The whole hat thing.
 You can always come to Joey.
 Me and Chandler live across the hall.
 He's away a lot.
 Stop hitting on her! It's her wedding day.
 Like there's a rule, or something? I got it.
 Please don't do that again.
 It's a horrible sound.
 It's Paul.
 Oh, God, is it 6:30? Buzz him in.
 - Who's Paul? - Paul, the wine guy? Maybe.
 Your "not a real date" is with Paul, the wine guy? - He finally asked you out? - Yes! It's a "Dear Diary" moment.
 - Rach, I can cancel.
 - Please, go, I'll be fine.
 Ross, are you okay? Do you want me to stay? That'd be good.
 - Really?- Go on! It's Paul, the wine guy! Does he sell it, drink it? Or he just complains a lot? Hi, come in! Paul, this is.
.
 everybody.
 Everybody, this is Paul.
 - The wine guy.
 - I didn't catch your name.
 Paul? I'll be right back.
 I've just gotta go A-wandering? Change.
 Sit down.
 Two seconds.
 I just pulled out four eyelashes.
 That can't be good.
 Hey, Paul, here's a tip.
 She really likes it when you rub her neck in the same spot.
.
 until it starts to get red.
 Shut up, Joey! What are you up to tonight? I was supposed to be headed for Aruba on my honeymoon.
.
 so, nothing.
 Right.
 You're not even getting your honeymoon.
 Although, Aruba.
 This time of year? Talk about your.
.
 big lizards.
 If you don't want to be alone tonight.
.
 Joey and Chandler are helping me with my furniture.
 We're very excited about it.
 Thanks.
 But I'm just going to hang out here.
 - It's been a long day.
 - Oh, sure.
 Phoebe, wanna help? I wish I could, but I don't want to.
 Love is sweet as summer showers Love is a wondrous work of art But your love Oh, your love, your love Is like a giant pigeon Crapping on my heart Thank you.
 I'm supposed to attach a bracket-y thing to the side things.
.
 using a bunch of these little worm guys.
 I have no bracket-y thing.
 I see no worm guys whatsoever.
.
 and I cannot feel my legs.
 - We got a bookcase.
 - It's beautiful.
 What's this? I would have to say that is an L-shaped bracket.
 - Which goes where? - I have no idea.
 - Done with the bookcase.
 - All finished.
 This was Carol's favorite beer.
 She always drank it out of the can.
 I should have known.
 - Start with that, we're out of here.
 - Please don't spoil all this fun.
 Let me ask you.
 She got the furniture, the stereo, the good TV.
 What did you get? - You guys.
 - You got screwed.
 - Oh, my God.
 - I know.
 I'm such an idiot.
 I should've known when she went to the dentist five times a week.
 I mean, how clean can teeth get? My brother's going through that.
 How did you get over it? He might accidentally break something valuable of hers.
 - Say her - Leg? That's one way of doing it.
 I went for the watch.
 You actually broke her watch? The worst I ever did was shred my old boyfriend's favorite towel.
 - Steer clear of you.
 - That's right.
 Barry, I'm sorry.
 I am so sorry.
 You probably think it's about making love with your socks on, but it isn't.
 It's about me.
 And I just The machine cut me off again.
 Anyway.
.
 I know that some lucky girl is going to become Mrs.
 Barry Finkel.
 But it isn't me.
 It's not me.
 Not that I have any idea who "me" is right now, but you just I'm divorced.
 - I'm only 26, and I'm divorced! - Shut up! That only took me an hour.
 We haven't had a relationship that's lasted longer than a Mento.
 You have had the love of a woman for four years.
 Four years of closeness and sharing, after which she ripped your heart out.
 That is why we don't do it! I don't think that was my point! Know what's scary? What if there's only one woman for everybody? I mean, what if you get one woman, and that's it? Unfortunately, in my case, there was only one woman for her.
 What are you talking about? One woman.
 That's like saying there's only one flavor of ice cream.
 Let me tell you something.
 There's lots of flavors out there.
 Rocky road and cookie dough and bing cherry vanilla.
 You can get them with jimmies or nuts or whipped cream.
 It's the best thing to happen to you! You got married.
 You were like, what, 8? Welcome back to the world.
 Grab a spoon! - I don't know if I'm hungry or horny.
 - Then stay out of my freezer.
 Ever since she walked out on me.
.
 What? You wanna spell it out with noodles? It's more of a fifth date kind of revelation.
 So there's going to be a fifth date? Isn't there? Yeah, yeah.
 I think there is.
 What were you going to say? Ever since she left me.
.
 I haven't been able to perform.
.
 sexually.
 Oh, God! I'm so sorry.
 Being spit on is probably not what you need right now.
 How long? - Two years.
 - Wow.
 I'm glad you smashed her watch.
 So you still think you might want that fifth date? Yeah.
 Yeah, I do.
 We are gathered here to join Joanie Louise Cunningham.
.
 and Charles.
 Chachi, Chachi, Chachi.
.
 in the bonds of holy matrimony.
 See! But Joanie loved Chachi.
 That's the difference.
 "Grab a spoon.
" Do you know how long it's been since I grabbed a spoon? Do the words, "Billy, don't be a hero," mean anything to you? Great story.
 But I gotta go.
 I got a date with Andrea.
 Angela.
 No, Andrea.
 Andrea's the screamer.
 Angela has cats.
 Right, thanks.
 It's Julie.
 I'm out of here.
 Here's the thing.
 Even if I could get it together enough.
.
 to ask a woman out.
.
 who am I going to ask? Isn't this amazing? I've never made coffee in my life.
 - That is amazing.
 - Congratulations.
 If I can make coffee, there isn't anything I can't do.
 I think it's, "If I can invade Poland, there's nothing I can't do.
" If you feel like you have to make a Western omelet or something.
.
 Although, actually I'm really not that hungry.
 Oh, good.
 Lenny and Squiggy are here.
 - Good morning.
 - Good morning.
 - Morning.
 - Morning, Paul.
 - Hello, Paul.
 - Hi.
 Paul, is it? - Thank you so much.
 - Stop.
 Last night was like all my birthdays, both graduations.
.
 plus the barn-raising scene in Witness.
 We'll talk later.
 Thank you.
 That wasn't a real date.
 What the hell do you do on a real date? Shut up and put my table back.
 I've got to get to work.
 If I don't input those numbers, it doesn't make much of a difference.
 So, like, you guys all have jobs? Yeah, we all have jobs.
 That's how we buy stuff.
 - Yeah, I'm an actor.
 - Have I seen you in anything? I doubt it.
 Mostly regional work.
 Unless you saw the Wee One's production of Pinocchio.
.
 at the little theater in the park? It was a job! "Look, Geppetto.
 I'm a real live boy.
" - I will not take this abuse.
 - You're right, I'm sorry.
 Once I was a wooden boy A little wooden boy You should both know that he's a dead man.
 Oh, Chandler! How are you doing today? Sleep okay? Did you talk to Barry? I can't stop smiling.
 I see that.
 You look like you slept with a hanger in your mouth.
 I know.
 He's just so.
.
 - Remember you and Tony Demarco? - Oh, yeah.
 Well, it's like that.
 With feelings.
 - Wow, are you in trouble! - Big time! Want a wedding dress? Hardly used.
 I think we're getting a little ahead of ourselves.
 I'm going to get up, go to work, and not think about him all day.
 Or else I'm going to get up and go to work.
 - Wish me luck! - What for? I'm gonna go get one of those job things.
 - Hi, Monica.
 - Franny, welcome back.
 - How was Florida? - You had sex, didn't you? - How do you do that? - I hate you.
 I'm pushing my aunt through Parrot Jungle, you're having sex.
 So, who? You know Paul? Paul, the wine guy? Yeah, I know Paul.
 You mean, you know Paul like I know Paul? What? I take credit for Paul.
 Before me, there was no snap in his turtle for two years.
 Of course it was a line.
 Why would anybody do something like that? I assume we want an answer more sophisticated than: "To get you into bed.
" I hate men.
 Don't hate.
 You don't want to put that out into the universe.
 Is it me? Is it like I have some sort of beacon that only dogs.
.
 and men with emotional problems can hear? Come here.
 Give me your feet.
 I just thought he was nice, you know? I can't believe you didn't know it was a line.
 - Guess what? - You got a job? Are you kidding? I'm trained for nothing.
 - I was laughed out of 12 interviews.
 - You're surprisingly upbeat.
 You'd be too, if you found these boots on sale.
.
 How well you know me.
 They're my "I don't need a job.
.
 I've got great boots" boots.
 - How did you pay? - Credit card.
 And who pays for that? My father.
 Is this really necessary? I can stop charging any time.
 You can't live off your parents.
 I know that.
 That's why I was getting married.
 Give her a break.
 It's hard being on your own.
 Thank you.
 I remember when I first came to this city, I was 14.
 Mom had killed herself, stepdad was in jail.
 I didn't know anybody here.
 I ended up living with this albino guy who was cleaning windshields.
 And then he killed himself.
 Then I found aromatherapy.
 So I know exactly how you feel.
 The word you're looking for is: "Anyway.
.
" - You ready? - No, how can I be ready? "Ready to jump out of the plane with no parachute?" - I can't do this.
 - I know you can.
 - No.
 - You made coffee, you can do anything.
 Cut.
 Cut.
 Cut.
 You know what? I think we can leave it at that.
 - Kind of a symbolic gesture.
 - Rachel, that was a library card.
 If you listen closely, you can hear a thousand retailers scream.
 Welcome to the real world! It sucks.
 You're gonna love it.
 That's it.
 Are you going to crash on the couch? - No, I gotta go home sometime.
 - Are you gonna be okay? Look what I just found on the floor.
 What? That's Paul's watch.
 Just put it back where you found it.
 Oh, boy! All right.
 - Good night, everybody.
 - Good night.
 - I'm sorry.
 Have it, I don't want it.
 - Split it? You probably didn't know this, but in high school.
.
 I had a major crush on you.
 I knew.
 You did? I figured you thought I was Monica's geeky brother.
 I did.
 Listen, do you think.
.
? Try not to let my vulnerability become a factor here.
 Do you think it would be okay if I asked you out sometime? Yeah.
 Maybe.
 Okay.
 Okay, maybe I will.
 - Good night.
 - Good night.
 See you.
 Wait, wait.
 What's with you? I just grabbed a spoon.
 - I can't believe what I'm hearing.
 - Can't believe what I'm hearing - What? I said -  What? I said - Would you stop? - Was I doing it again? Yes! I said you had a nice butt.
 It's just not a great butt.
 - You won't know a butt if it bit you.
 - There's an image.
 Would anybody like more coffee? You made it, or you're serving it? - I'm just serving it.
 - I'll have a cup of coffee.
 Kids, new dream.
 I'm in Las Vegas.
 Miss, more coffee? Could you give this to that guy over there? Go ahead.
 Thank you.
 Sorry.
 Okay, Las Vegas.
 I'm in Las Vegas.
 I'm Liza Minnelli.
."""

class TestSpringfield(TestCase):

    def test_get_episodes(self):
        with vcr.use_cassette('test/vcr_cassettes/springfield_friends.yaml'):
            res = Springfield('friends').get_episodes()
            self.assertEqual(res, EPISODES)

    def test_get_transcript(self):
        with vcr.use_cassette('test/vcr_cassettes/springfield_friends_0101.yaml'):
            url = 'view_episode_scripts.php?tv-show=friends&episode=s01e01'
            res = Springfield('friends').get_transcript(url)
            self.assertEqual(res, TRANSCRIPT)

    @patch("springfield.sleep", lambda x: 0)
    def test_save(self):
        with vcr.use_cassette('test/vcr_cassettes/springfield_friends_save.yaml'):
            ep_dict = [
              {
                "season": "1",
                "episodes": [
                  {
                    "episode": "1",
                    "link": "view_episode_scripts.php?tv-show=friends&episode=s01e01"
                  },
                  {
                    "episode": "2",
                    "link": "view_episode_scripts.php?tv-show=friends&episode=s01e02"
                  }
                ]
              },
              {
                "season": "2",
                "episodes": [
                  {
                    "episode": "1",
                    "link": "view_episode_scripts.php?tv-show=friends&episode=s02e01"
                  }
                ]
              }
            ]
            Springfield('friends').save('test/results/friends', ep_dict)
