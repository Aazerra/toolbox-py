# Toolbox

A collection of Python utilities for common programming tasks.

## Installation

```bash
pip install toolbox-py
```

## Features

This package provides various utility functions organized into different modules:

### String Utilities
- `compress_string` / `decompress_string` - String compression using zlib
- `camel_to_snake` / `snake_to_camel` - Case conversion utilities  
- `slugify` - Convert strings to URL-friendly slugs

### Dictionary Utilities
- `flatten_dict` - Flatten nested dictionaries with dot notation
- `merge_dicts` - Recursively merge dictionaries
- `DotDict` - Dictionary with dot notation access

### List Utilities  
- `flatten_list` - Flatten nested lists

### Encoding/Decoding
- `encode_to_base64` / `decode_from_base64` - Base64 encoding utilities

### Other Utilities
- JSON handling
- Data class utilities

## Usage Examples

```python
import toolbox

# String utilities
camel_case = toolbox.snake_to_camel("hello_world")  # "HelloWorld"
snake_case = toolbox.camel_to_snake("HelloWorld")   # "hello_world"
slug = toolbox.slugify("Hello World!")              # "hello-world"

# Dictionary utilities
nested = {'a': {'b': {'c': 1}}, 'd': 2}
flat = toolbox.flatten_dict(nested)                 # {'a.b.c': 1, 'd': 2}

# Dot notation dictionary
dot_dict = toolbox.DotDict(x=1, y=2)
print(dot_dict.x)                                   # 1

# Base64 encoding
encoded = toolbox.encode_to_base64("Hello")
```

## Development

```bash
# Clone the repository
git clone https://github.com/Aazerra/toolbox-py.git
cd toolbox-py

# Install development dependencies
pip install -e .[dev]

# Run tests
pytest

# Build the package
python -m build
```

## License

MIT License - see [LICENSE](LICENSE) file for details.
