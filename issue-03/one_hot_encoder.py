from typing import List, Tuple
import unittest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


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


if __name__ == '__main__':
    from pprint import pprint

    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    pprint(transformed_cities)
    assert transformed_cities == exp_transformed_cities
