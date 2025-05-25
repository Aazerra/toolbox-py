import pytest
from toolbox.string import (compress_string, decompress_string, snake_to_camel,
                            camel_to_snake, slugify)


def test_compress_decompress():
    original = "This is a test string."
    compressed = compress_string(original)
    decompressed = decompress_string(compressed)
    assert decompressed == original


def test_camel_to_snake():
    assert camel_to_snake("CamelCase") == "camel_case"
    assert camel_to_snake("camelCase") == "camel_case"


def test_snake_to_camel():
    assert snake_to_camel("snake_case") == "SnakeCase"
    assert snake_to_camel("a_b_c") == "ABC"


def test_slugify():
    assert slugify("This is a test!") == "this-is-a-test"
    assert slugify("Héllô Wørld") == "hello-wrld"
