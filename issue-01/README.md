## issue-01

1. Заносим тесты в docstring:

```python
def encode(message: str) -> str:
    """
    Кодирует строку в соответсвии с таблицей азбуки Морзе
    
    Тест с вызовом message='SOS'
    >>> encode('SOS')
    '... --- ...'

    Тест с исключением
    >>> encode('sos')
    Traceback (most recent call last):
    KeyError: 's'

    Тест, с использованием директивы SKIP, которая пропускает данный тест
    >>> encode('sos') #doctest: +SKIP
    ...
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
```

2. Открываем вкладку Terminal в PyCharm, запускаем команду:
```
python -m doctest -o NORMALIZE_WHITESPACE -v morse.py > result.txt
```
