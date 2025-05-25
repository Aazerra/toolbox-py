from typing import List, Any


def flatten_list(lst: List[Any]) -> List[Any]:
    """
    Recursively flatten a list of arbitrarily nested lists.

    Args:
        lst (List[Any]): The nested list.

    Returns:
        List[Any]: A single flattened list.
    """
    result: List[Any] = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result
