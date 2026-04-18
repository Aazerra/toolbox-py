import pytest
from toolbox.list import (
    flatten_list, chunk_list, unique, partition, group_by, 
    dedupe, interleave, compact
)


def test_flatten_list():
    nested = [1, [2, [3, 4], 5], 6]
    assert flatten_list(nested) == [1, 2, 3, 4, 5, 6]


def test_chunk_list():
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    assert chunk_list(lst, 3) == [[1, 2, 3], [4, 5, 6], [7, 8]]
    assert chunk_list(lst, 4) == [[1, 2, 3, 4], [5, 6, 7, 8]]


def test_unique():
    lst = [1, 2, 2, 3, 1, 4, 3, 5]
    assert unique(lst) == [1, 2, 3, 4, 5]


def test_partition():
    lst = [1, 2, 3, 4, 5, 6]
    evens, odds = partition(lst, lambda x: x % 2 == 0)
    assert evens == [2, 4, 6]
    assert odds == [1, 3, 5]


def test_group_by():
    lst = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
    result = group_by(lst, lambda x: x[0])
    assert result == {
        'a': ['apple', 'apricot'],
        'b': ['banana', 'blueberry'],
        'c': ['cherry']
    }


def test_dedupe():
    lst = [1, 2, 2, 3, 1, 4]
    assert dedupe(lst) == [1, 2, 3, 4]
    
    # Test with key function
    dicts = [{'id': 1, 'val': 'a'}, {'id': 2, 'val': 'b'}, {'id': 1, 'val': 'c'}]
    result = dedupe(dicts, key=lambda x: x['id'])
    assert result == [{'id': 1, 'val': 'a'}, {'id': 2, 'val': 'b'}]


def test_interleave():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = [10, 20]
    assert interleave(list1, list2) == [1, 'a', 2, 'b', 3, 'c']
    assert interleave(list1, list2, list3) == [1, 'a', 10, 2, 'b', 20, 3, 'c']


def test_compact():
    lst = [1, None, 2, '', 3, False, 0, 'hello', []]
    assert compact(lst) == [1, 2, 3, 0, 'hello']
