import zlib
import re
import unicodedata

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
