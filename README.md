# toolbox-py

A comprehensive collection of Python utilities for everyday programming tasks.

## Features

### Dictionary Utilities (`toolbox.dict`)
- **DotDict**: Dictionary with dot notation access
- **flatten_dict**: Flatten nested dictionaries with customizable separators
- **unflatten_dict**: Convert flattened dicts back to nested structure
- **merge_dicts**: Recursively merge dictionaries
- **get_nested/set_nested**: Access nested values using dot notation paths
- **filter_dict**: Filter dictionaries with predicate functions
- **invert_dict**: Swap keys and values
- **deep_copy_dict**: Deep copy nested dictionaries

### List Utilities (`toolbox.list`)
- **flatten_list**: Recursively flatten nested lists
- **chunk_list**: Split lists into fixed-size chunks
- **unique**: Remove duplicates while preserving order
- **partition**: Split lists based on predicate
- **group_by**: Group items by key function
- **dedupe**: Advanced deduplication with custom key functions
- **interleave**: Merge multiple lists element by element
- **compact**: Remove falsy values (None, '', False, etc.)

### String Utilities (`toolbox.string`)
- **Case conversion**: camel_to_snake, snake_to_camel, kebab_case, title_case
- **Compression**: compress_string/decompress_string with base64 encoding
- **Formatting**: slugify, truncate, wrap_text
- **Text processing**: remove_accents, strip_html, reverse_string, count_words

### Encoding/Decoding (`toolbox.encode`, `toolbox.decode`)
- Base64 encoding and decoding
- Support for both str and bytes

### Data Serialization (`toolbox.dataclass`)
- **SerializableDataclass**: Enhanced dataclass with JSON serialization
- Alias support for field name mapping
- Preprocessors for data transformation
- Nested dataclass handling

## Installation

```bash
pip install toolbox-py
```

Or with uv:
```bash
uv add toolbox-py
```

## Usage Examples

### Dictionary Operations

```python
from toolbox.dict import flatten_dict, get_nested, DotDict

# Flatten nested dictionary
nested = {'user': {'name': 'John', 'address': {'city': 'NYC'}}}
flat = flatten_dict(nested)
# {'user.name': 'John', 'user.address.city': 'NYC'}

# Access nested values safely
city = get_nested(nested, 'user.address.city', default='Unknown')

# Dot notation access
config = DotDict({'database': {'host': 'localhost'}})
print(config.database.host)  # localhost
```

### List Operations

```python
from toolbox.list import chunk_list, group_by, dedupe

# Split into chunks
items = [1, 2, 3, 4, 5, 6, 7]
chunks = chunk_list(items, 3)  # [[1, 2, 3], [4, 5, 6], [7]]

# Group by key
words = ['apple', 'apricot', 'banana', 'blueberry']
by_first = group_by(words, lambda w: w[0])
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}

# Deduplicate with custom key
users = [{'id': 1, 'name': 'Alice'}, {'id': 1, 'name': 'Bob'}]
unique_users = dedupe(users, key=lambda u: u['id'])
```

### String Operations

```python
from toolbox.string import slugify, truncate, camel_to_snake

# Create URL-friendly slugs
slug = slugify('Hello World!')  # 'hello-world'

# Truncate with ellipsis
text = truncate('Long text here', 10)  # 'Long te...'

# Convert naming conventions
snake = camel_to_snake('CamelCase')  # 'camel_case'
```

## Development

```bash
# Setup environment
uv sync

# Run tests
pytest

# Format code
black toolbox/ tests/
isort toolbox/ tests/

# Type check
mypy toolbox/

# Build docs
cd docs && make html
```

## Requirements

- Python >= 3.11

## License

MIT License - see LICENSE file for details
