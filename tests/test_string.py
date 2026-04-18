import pytest
from toolbox.string import (
    compress_string, decompress_string, snake_to_camel,
    camel_to_snake, slugify, truncate, remove_accents, title_case,
    kebab_case, strip_html, reverse_string, count_words, wrap_text
)


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


def test_truncate():
    text = "This is a long string"
    assert truncate(text, 10) == "This is..."
    assert truncate(text, 50) == text
    assert truncate(text, 10, suffix='>>') == "This is >>"


def test_remove_accents():
    assert remove_accents("Héllô Wörld") == "Hello World"
    assert remove_accents("café") == "cafe"
    assert remove_accents("naïve") == "naive"


def test_title_case():
    assert title_case("the quick brown fox") == "The Quick Brown Fox"
    assert title_case("a tale of two cities") == "A Tale of Two Cities"
    assert title_case("the lord of the rings") == "The Lord of the Rings"


def test_kebab_case():
    assert kebab_case("CamelCase") == "camel-case"
    assert kebab_case("snake_case") == "snake-case"
    assert kebab_case("spaces in text") == "spaces-in-text"


def test_strip_html():
    assert strip_html("<p>Hello <b>World</b></p>") == "Hello World"
    assert strip_html("<div>Test</div>") == "Test"
    assert strip_html("No tags") == "No tags"


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("12345") == "54321"


def test_count_words():
    assert count_words("Hello world") == 2
    assert count_words("The quick brown fox") == 4
    assert count_words("") == 0


def test_wrap_text():
    text = "The quick brown fox jumps over the lazy dog"
    result = wrap_text(text, 20)
    assert result == ["The quick brown fox", "jumps over the lazy", "dog"]
    
    short_text = "Short"
    assert wrap_text(short_text, 20) == ["Short"]
