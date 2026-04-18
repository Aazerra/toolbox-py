import pytest
from toolbox.dict import (
    flatten_dict, merge_dicts, DotDict, unflatten_dict, get_nested, 
    set_nested, filter_dict, invert_dict, deep_copy_dict
)


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


def test_unflatten_dict():
    flat = {'a.b.c': 1, 'd': 2, 'a.b.e': 3}
    expected = {'a': {'b': {'c': 1, 'e': 3}}, 'd': 2}
    assert unflatten_dict(flat) == expected


def test_get_nested():
    nested = {'a': {'b': {'c': 1}}}
    assert get_nested(nested, 'a.b.c') == 1
    assert get_nested(nested, 'a.b.x', default=99) == 99
    assert get_nested(nested, 'a.b') == {'c': 1}


def test_set_nested():
    d = {}
    set_nested(d, 'a.b.c', 42)
    assert d == {'a': {'b': {'c': 42}}}
    set_nested(d, 'a.b.d', 100)
    assert d == {'a': {'b': {'c': 42, 'd': 100}}}


def test_filter_dict():
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    result = filter_dict(d, lambda k, v: v % 2 == 0)
    assert result == {'b': 2, 'd': 4}


def test_invert_dict():
    d = {'a': 1, 'b': 2, 'c': 3}
    assert invert_dict(d) == {1: 'a', 2: 'b', 3: 'c'}


def test_deep_copy_dict():
    original = {'a': {'b': [1, 2, 3]}, 'c': 4}
    copied = deep_copy_dict(original)
    copied['a']['b'].append(4)
    assert original['a']['b'] == [1, 2, 3]
    assert copied['a']['b'] == [1, 2, 3, 4]
