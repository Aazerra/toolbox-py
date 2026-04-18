# Project Guidelines

## Code Style

Follow patterns in [toolbox/dict.py](../toolbox/dict.py), [toolbox/list.py](../toolbox/list.py), and [toolbox/string.py](../toolbox/string.py):

- **Type hints required**: Annotate all parameters and return types using standard typing module
- **Google-style docstrings**: Include `Args:` and `Returns:` sections for all public functions
- **Formatting**: Black (88 char lines) + isort with black profile
- **Prefer explicit defaults**: Use `sep: str = '.'` over `sep: Optional[str] = None`
- **Recursive patterns**: Use recursive functions for nested data structures (see `flatten_dict`, `flatten_list`)

```python
def flatten_dict(d: Dict[Any, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """
    Flatten a nested dictionary, joining keys with a separator.

    Args:
        d (Dict[Any, Any]): The dictionary to flatten.
        parent_key (str): The base key for recursion.
        sep (str): Separator between nested keys.

    Returns:
        Dict[str, Any]: The flattened dictionary.
    """
```

## Architecture

**Standalone utility modules** - each module in [toolbox/](../toolbox/) is independent:

- **No `__init__.py`**: Import directly from modules: `from toolbox.dict import flatten_dict`
- **Internal dependencies**: Only [string.py](../toolbox/string.py) depends on encode/decode modules
- **No circular dependencies**: Keep modules independent

**SerializableDataclass pattern** ([dataclass.py](../toolbox/dataclass.py)):

- Meta-programming with dataclasses for JSON serialization
- Internal fields prefixed with `_` are excluded from serialization
- Supports aliases, preprocessors, and nested SerializableDataclass instances

## Build and Test

**Setup environment**:

```bash
# Install with dev dependencies (requires uv)
uv sync
```

**Run tests**:

```bash
pytest
```

**Format code**:

```bash
black toolbox/ tests/
isort toolbox/ tests/
```

**Type check** (note: not currently enforced on all modules):

```bash
mypy toolbox/
```

**Build documentation**:

```bash
cd docs && make html
```

## Testing Conventions

Follow patterns in [tests/test_dict.py](../tests/test_dict.py):

- **One test file per module**: `test_<module>.py`
- **Naming**: `test_<function_name>()` or `test_<operation>()`
- **Simple assertions**: Direct arrange-act-assert, no fixtures
- **Inline test data**: Define test inputs directly in test functions
- **Import specifics**: `from toolbox.dict import flatten_dict` not `import toolbox.dict`

```python
def test_flatten_dict():
    nested = {'a': {'b': {'c': 1}}, 'd': 2}
    expected = {'a.b.c': 1, 'd': 2}
    assert flatten_dict(nested) == expected
```

When adding new utilities, create corresponding test file and `.rst` doc using the automodule pattern from [docs/dict.rst](../docs/dict.rst).

## Project Conventions

**Error handling**:

- Let exceptions propagate - minimal try/except blocks
- Convert exceptions only when semantically meaningful (see [DotDict.**getattr**](../toolbox/dict.py#L13-L17) converting KeyError → AttributeError)

**Polymorphic functions**:

- Use runtime `isinstance()` checks when functions handle multiple types
- Example: encode/decode modules handle both `str` and `bytes`

**Documentation**:

- Each module has corresponding `.rst` file in [docs/](../docs/)
- Sphinx autodoc generates API docs from docstrings
- Keep docstrings complete - they are the primary documentation
