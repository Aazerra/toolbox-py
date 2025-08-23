"""
Toolbox - A collection of Python utilities.

This package provides various utility functions for common tasks including:
- String manipulation and conversion utilities
- Dictionary operations and flattening
- List processing functions
- Data class utilities
- Base64 encoding/decoding
- JSON handling utilities
"""

__version__ = "0.1.0"
__author__ = "Alireza Rabie"
__email__ = "alireza@aazerra.dev"

# Import main utilities for easy access
from .string import compress_string, decompress_string, camel_to_snake, snake_to_camel, slugify
from .dict import flatten_dict, merge_dicts, DotDict
from .list import flatten_list
from .encode import encode_to_base64
from .decode import decode_from_base64

__all__ = [
    'compress_string',
    'decompress_string', 
    'camel_to_snake',
    'snake_to_camel',
    'slugify',
    'flatten_dict',
    'merge_dicts',
    'DotDict',
    'flatten_list',
    'encode_to_base64',
    'decode_from_base64',
]