import urllib.request
import json
import unittest
from unittest.mock import MagicMock, patch

API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """

    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


class WhatYearTest(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_if(self, mock_urlopen):
        cm = MagicMock()
        cm.getcode.return_value = 200
        cm.read.return_value = json.dumps({'currentDateTime': '2019-03-01'})
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm
        self.assertEqual(what_is_year_now(), 2019)

    @patch('urllib.request.urlopen')
    def test_elif(self, mock_urlopen):
        cm = MagicMock()
        cm.getcode.return_value = 200
        cm.read.return_value = json.dumps({'currentDateTime': '01.03.2019'})
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm
        self.assertEqual(what_is_year_now(), 2019)

    @patch('urllib.request.urlopen')
    def test_else(self, mock_urlopen):
        cm = MagicMock()
        cm.getcode.return_value = 200
        cm.read.return_value = json.dumps({'currentDateTime': 'smthelse'})
        cm.__enter__.return_value = cm
        mock_urlopen.return_value = cm
        with self.assertRaises(ValueError):
            what_is_year_now()
