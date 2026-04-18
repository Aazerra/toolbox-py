from typing import List, Any, TypeVar, Callable, Dict


T = TypeVar('T')


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


def chunk_list(lst: List[T], size: int) -> List[List[T]]:
    """
    Split a list into chunks of a specified size.

    Args:
        lst (List[T]): The list to chunk.
        size (int): Size of each chunk.

    Returns:
        List[List[T]]: List of chunks.
    """
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def unique(lst: List[T]) -> List[T]:
    """
    Return unique elements from a list while preserving order.

    Args:
        lst (List[T]): The input list.

    Returns:
        List[T]: List with duplicates removed, order preserved.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def partition(lst: List[T], predicate: Callable[[T], bool]) -> tuple[List[T], List[T]]:
    """
    Partition a list into two lists based on a predicate.

    Args:
        lst (List[T]): The list to partition.
        predicate (Callable[[T], bool]): Function that returns True or False.

    Returns:
        tuple[List[T], List[T]]: Tuple of (matching, non-matching) items.
    """
    matching = []
    non_matching = []
    for item in lst:
        if predicate(item):
            matching.append(item)
        else:
            non_matching.append(item)
    return matching, non_matching


def group_by(lst: List[T], key: Callable[[T], Any]) -> Dict[Any, List[T]]:
    """
    Group list items by a key function.

    Args:
        lst (List[T]): The list to group.
        key (Callable[[T], Any]): Function that returns the grouping key.

    Returns:
        Dict[Any, List[T]]: Dictionary mapping keys to lists of items.
    """
    result: Dict[Any, List[T]] = {}
    for item in lst:
        k = key(item)
        if k not in result:
            result[k] = []
        result[k].append(item)
    return result


def dedupe(lst: List[T], key: Callable[[T], Any] = None) -> List[T]:
    """
    Remove duplicates from a list based on a key function.

    Args:
        lst (List[T]): The list to deduplicate.
        key (Callable[[T], Any], optional): Function to extract comparison key. Defaults to None (use item itself).

    Returns:
        List[T]: List with duplicates removed, order preserved.
    """
    if key is None:
        return unique(lst)
    
    seen = set()
    result = []
    for item in lst:
        k = key(item)
        if k not in seen:
            seen.add(k)
            result.append(item)
    return result


def interleave(*lists: List[T]) -> List[T]:
    """
    Interleave multiple lists element by element.

    Args:
        *lists: Variable number of lists to interleave.

    Returns:
        List[T]: Interleaved list.
    """
    result = []
    max_len = max(len(lst) for lst in lists) if lists else 0
    for i in range(max_len):
        for lst in lists:
            if i < len(lst):
                result.append(lst[i])
    return result


def compact(lst: List[Any]) -> List[Any]:
    """
    Remove None, empty strings, and False values from a list.

    Args:
        lst (List[Any]): The list to compact.

    Returns:
        List[Any]: List with falsy values removed.
    """
    return [item for item in lst if item is not None and item != '' and item is not False and (item or item == 0)]
