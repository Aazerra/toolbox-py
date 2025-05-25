import pytest
from toolbox.list import flatten_list


def test_flatten_list():
    nested = [1, [2, [3, 4], 5], 6]
    assert flatten_list(nested) == [1, 2, 3, 4, 5, 6]
