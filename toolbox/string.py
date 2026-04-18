import zlib
import re
import unicodedata
from typing import List

from .encode import encode_to_base64
from .decode import decode_from_base64


def compress_string(text: str) -> str:
    """
    Compress a UTF-8 string using zlib and encode the result in base64.

    Args:
        text (str): The input string to compress.

    Returns:
        str: The base64-encoded compressed string.
    """
    compressed = zlib.compress(text.encode("utf-8"))
    return encode_to_base64(compressed)


def decompress_string(text: str) -> str:
    """
    Decode a base64-encoded string and decompress it using zlib.

    Args:
        text (str): The base64-encoded compressed string.

    Returns:
        str: The decompressed UTF-8 string.
    """
    decoded = decode_from_base64(text)
    return zlib.decompress(decoded).decode("utf-8")


def camel_to_snake(name: str) -> str:
    """
    Convert camelCase or PascalCase to snake_case.

    Args:
        name (str): The camelCase or PascalCase string.

    Returns:
        str: The snake_case representation.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def snake_to_camel(name: str) -> str:
    """
    Convert snake_case to CamelCase.

    Args:
        name (str): The snake_case string.

    Returns:
        str: The CamelCase representation.
    """
    return ''.join(word.capitalize() for word in name.split('_'))


def slugify(value: str) -> str:
    """
    Convert a string to a slug suitable for URLs.

    Args:
        value (str): The input string.

    Returns:
        str: A slugified version of the string.
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)


def truncate(text: str, length: int, suffix: str = '...') -> str:
    """
    Truncate a string to a maximum length, adding a suffix if truncated.

    Args:
        text (str): The text to truncate.
        length (int): Maximum length (including suffix).
        suffix (str, optional): Suffix to add if truncated. Defaults to '...'.

    Returns:
        str: The truncated string.
    """
    if len(text) <= length:
        return text
    return text[:length - len(suffix)] + suffix


def remove_accents(text: str) -> str:
    """
    Remove accents and diacritics from a string.

    Args:
        text (str): The input string.

    Returns:
        str: String with accents removed.
    """
    nfkd = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in nfkd if not unicodedata.combining(c)])


def title_case(text: str) -> str:
    """
    Convert a string to title case, handling special words correctly.

    Args:
        text (str): The input string.

    Returns:
        str: Title-cased string.
    """
    small_words = {'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'in', 'of', 'on', 'or', 'the', 'to', 'with'}
    words = text.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in small_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return ' '.join(result)


def kebab_case(text: str) -> str:
    """
    Convert a string to kebab-case.

    Args:
        text (str): The input string (snake_case, camelCase, or spaces).

    Returns:
        str: The kebab-case representation.
    """
    # Handle camelCase
    text = re.sub(r'(?<!^)(?=[A-Z])', '-', text)
    # Handle spaces and underscores
    text = re.sub(r'[\s_]+', '-', text)
    return text.lower()


def strip_html(text: str) -> str:
    """
    Remove HTML tags from a string.

    Args:
        text (str): The input string with HTML.

    Returns:
        str: String with HTML tags removed.
    """
    return re.sub(r'<[^>]+>', '', text)


def reverse_string(text: str) -> str:
    """
    Reverse a string.

    Args:
        text (str): The input string.

    Returns:
        str: The reversed string.
    """
    return text[::-1]


def count_words(text: str) -> int:
    """
    Count words in a string.

    Args:
        text (str): The input string.

    Returns:
        int: Number of words.
    """
    return len(re.findall(r'\b\w+\b', text))


def wrap_text(text: str, width: int) -> List[str]:
    """
    Wrap text to a specific width.

    Args:
        text (str): The text to wrap.
        width (int): Maximum line width.

    Returns:
        List[str]: List of wrapped lines.
    """
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        word_length = len(word)
        if current_length + word_length + len(current_line) <= width:
            current_line.append(word)
            current_length += word_length
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]
            current_length = word_length
    
    if current_line:
        lines.append(' '.join(current_line))
    
    return lines
