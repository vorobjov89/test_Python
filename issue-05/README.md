## issue-05

1. Импортируем необходимые модули:
```python
import unittest
from unittest.mock import MagicMock, patch
```

2. Создаем класс для тестирования:
```python
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
```

3. Запускаем в терминале команду:
```
python -m unittest -v what_is_year_now.py 2> result.txt   
```

4. Запускаем команду для сбора статистики по покрытию кода тестами:
```
python -m coverage run -m unittest -v what_is_year_now.py
```

5. Смотрим отчет о покрытии:
```
python -m coverage report  
```

6. Получаем отчет в виде html:
```
python -m coverage html 
```
