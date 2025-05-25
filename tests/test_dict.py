import pytest
from toolbox.dict import flatten_dict, merge_dicts, DotDict


def test_flatten_dict():
    nested = {'a': {'b': {'c': 1}}, 'd': 2}
    expected = {'a.b.c': 1, 'd': 2}
    assert flatten_dict(nested) == expected


def test_merge_dicts():
    d1 = {'a': 1, 'b': {'x': 10}}
    d2 = {'b': {'y': 20}, 'c': 3}
    merged = merge_dicts(d1, d2)
    assert merged == {'a': 1, 'b': {'x': 10, 'y': 20}, 'c': 3}


def test_dotdict():
    d = DotDict(a=1, b=2)
    assert d.a == 1
    d.c = 3
    assert d['c'] == 3
    del d.b
    assert 'b' not in d
