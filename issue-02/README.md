## issue-02

1. Импортируем модуль pytest в morse.py:
```python
import pytest
```

2. Добавляем тестовую функцию test_decode, которую оборачиваем в декоратор @pytest.mark.parametrize с тремя тестами:

```python
@pytest.mark.parametrize(('test_input', 'expected'),
                         [('... --- ...', 'SOS'),
                          ('...', 'S'),
                          ('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.', 'MAI-PYTHON-2019')
                          ])
def test_decode(test_input, expected):
    assert decode(test_input) == expected
```

3. Запускаем в терминале PyCharm'a команду
```python
python -m pytest -v morse.py > result.txt
```