from typing import Any, Dict, List


class DotDict(dict):
    """
    A dictionary that supports attribute-style access (dot notation).

    Example:
        d = DotDict(a=1)
        print(d.a)  # 1
    """

    def __getattr__(self, item: str) -> Any:
        try:
            return self[item]
        except KeyError:
            raise AttributeError(item)

    def __setattr__(self, key: str, value: Any) -> None:
        self[key] = value

    def __delattr__(self, key: str) -> None:
        try:
            del self[key]
        except KeyError:
            raise AttributeError(key)


def flatten_dict(d: Dict[Any, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """
    Flatten a nested dictionary, joining keys with a separator.

    Args:
        d (Dict[Any, Any]): The dictionary to flatten.
        parent_key (str, optional): The base key for recursion. Defaults to ''.
        sep (str, optional): Separator between keys. Defaults to '.'.

    Returns:
        Dict[str, Any]: A flat dictionary with joined key paths.
    """
    items: List[tuple[str, Any]] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def merge_dicts(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Recursively merge two dictionaries.

    Args:
        dict1 (Dict[Any, Any]): The base dictionary.
        dict2 (Dict[Any, Any]): The dictionary to merge into the base.

    Returns:
        Dict[Any, Any]: The merged dictionary.
    """
    result = dict1.copy()
    for k, v in dict2.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = merge_dicts(result[k], v)
        else:
            result[k] = v
    return result


def unflatten_dict(d: Dict[str, Any], sep: str = '.') -> Dict[Any, Any]:
    """
    Unflatten a dictionary with joined keys back into a nested structure.

    Args:
        d (Dict[str, Any]): The flattened dictionary.
        sep (str, optional): Separator used in keys. Defaults to '.'.

    Returns:
        Dict[Any, Any]: A nested dictionary.
    """
    result: Dict[Any, Any] = {}
    for key, value in d.items():
        parts = key.split(sep)
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result


def get_nested(d: Dict[Any, Any], path: str, default: Any = None, sep: str = '.') -> Any:
    """
    Get a value from a nested dictionary using a dotted path.

    Args:
        d (Dict[Any, Any]): The nested dictionary.
        path (str): The dotted path to the value (e.g., 'a.b.c').
        default (Any, optional): Default value if path not found. Defaults to None.
        sep (str, optional): Path separator. Defaults to '.'.

    Returns:
        Any: The value at the path or the default.
    """
    keys = path.split(sep)
    current = d
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def set_nested(d: Dict[Any, Any], path: str, value: Any, sep: str = '.') -> None:
    """
    Set a value in a nested dictionary using a dotted path.

    Args:
        d (Dict[Any, Any]): The nested dictionary to modify.
        path (str): The dotted path to set (e.g., 'a.b.c').
        value (Any): The value to set.
        sep (str, optional): Path separator. Defaults to '.'.
    """
    keys = path.split(sep)
    current = d
    for key in keys[:-1]:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}
        current = current[key]
    current[keys[-1]] = value


def filter_dict(d: Dict[Any, Any], predicate: callable) -> Dict[Any, Any]:
    """
    Filter a dictionary based on a predicate function.

    Args:
        d (Dict[Any, Any]): The dictionary to filter.
        predicate (callable): Function that takes (key, value) and returns bool.

    Returns:
        Dict[Any, Any]: Filtered dictionary.
    """
    return {k: v for k, v in d.items() if predicate(k, v)}


def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Invert a dictionary (swap keys and values).

    Args:
        d (Dict[Any, Any]): The dictionary to invert.

    Returns:
        Dict[Any, Any]: Inverted dictionary with values as keys.
    """
    return {v: k for k, v in d.items()}


def deep_copy_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Create a deep copy of a nested dictionary.

    Args:
        d (Dict[Any, Any]): The dictionary to copy.

    Returns:
        Dict[Any, Any]: A deep copy of the dictionary.
    """
    result: Dict[Any, Any] = {}
    for k, v in d.items():
        if isinstance(v, dict):
            result[k] = deep_copy_dict(v)
        elif isinstance(v, list):
            result[k] = [deep_copy_dict(item) if isinstance(item, dict) else item for item in v]
        else:
            result[k] = v
    return result
