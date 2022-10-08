## issue-04

1. Импортируем pytest:
```python
import pytest
```

2. Добавляем тестовые функции:
```python
def test_equal():
    cities = ['Moscow', 'New York', 'Moscow', 'London']

    actual = fit_transform(cities)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_not_in():
    cities = ['Moscow', 'New York', 'Moscow', 'London']

    a = ('Paris', [0, 1, 0])
    b = fit_transform(cities)
    assert a not in b


def test_exception1():
    cities = ['Moscow', 'New York', 'Moscow', 'London']

    actual = fit_transform(cities)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [1, 0, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [0, 1, 0]),
    ]
    try:
        assert actual == expected
    except AssertionError:
        print('Test 3: not equal')


def test_exception2():
    cities = ['Moscow', 'New York', 'Moscow', 'London', [123, 4545]]
    with pytest.raises(Exception):
        fit_transform(cities)
```

3. Запускаем в терминале команду
```
python -m pytest -v one_hot_encoder.py > result.txt
```