## issue-03

1. Импортируем unittest:
```python
import unittest
```

2. Создаем класс для тестирующих функций и четыре тестовых функции в нем:
```python
class TestOneHotEncoder(unittest.TestCase):
    def test_equal(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']

        actual = fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_not_in(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']

        a = ('Paris', [0, 1, 0])
        b = fit_transform(cities)
        self.assertNotIn(a, b)

    def test_exception1(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']

        actual = fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [1, 0, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [0, 1, 0]),
        ]
        try:
            self.assertEqual(actual, expected)
        except AssertionError:
            print('Test 3: not equal')

    def test_exception2(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London', [123, 4545]]
        with self.assertRaises(TypeError):
            fit_transform(cities)
```

3. В терминале запускаем команду:
```
python -m unittest -v one_hot_encoder.py 2> result.txt
```