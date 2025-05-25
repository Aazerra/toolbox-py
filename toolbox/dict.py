from typing import Any, Dict


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
