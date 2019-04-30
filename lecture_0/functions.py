from typing import List, Dict, Any, Callable


def is_name(word: str) -> bool:
    """Checks if string starts with upper letter.

    Parameters
    ----------
    word
        String to check.

    Returns
    -------
    bool
        First letter of a string is/isn't capital.

    """

    return word[0].isupper()


def normalize_full_name(first_name: str = '', last_name: str = '') -> str:
    """Builds a full name string.

    Parameters
    ----------
    first_name
        One's first name.
    last_name
        One's second name.

    Returns
    -------
    str
        Normalized full name string with
        given first and/or last name.

    """

    full_name = f'{first_name} {last_name}'
    partial_name = f'{first_name}{last_name}'
    return full_name if first_name and last_name else partial_name


def increase_list(first_item: int, second_item: int, factor: int) -> List[int]:
    """Builds a list of two elements multiplied by input factor.

    Parameters
    ----------
    first_item
        First value in output list.
    second_item
        Second value in output list.
    factor
        Value to multiply the first two
        numbers by.

    Returns
    -------
    list
        List of the first two modified
        input arguments.

    """
    return [first_item * factor, second_item * factor]


def filter_list(items: List[int]) -> List[int]:
    """Picks all the positive numbers from a list.

    Parameters
    ----------
    items
        List to filter on.

    Returns
    -------
    list
        Filtered list.

    """

    return list(filter(lambda item: item > 0, items))


def max_list(items: List[int], first_number: int, second_number: int) -> None:
    """Appends the greater value to a given list.

    Parameters
    ----------
    items
        List to append to.
    first_number
        First possible value to append.
    second_number
        Second possible value to append.

    Notes
    -----
    Doesn't append anything to a list if given
    values are equal.

    """

    if first_number == second_number:
        return

    max_number = first_number if first_number > second_number else second_number
    items.append(max_number)


def get_dictionary(key: Any, value: Any) -> Dict[Any, Any]:
    """Builds a dictionary.

    Parameters
    ----------
    key
        Key to insert.
    value
        Value to insert to a given key.

    Returns
    -------
    dict
        Dictionary with given key and value.

    """

    return {key: value}


def set_dictionary(items: Dict[Any, Any], key: Any, value: Any) -> None:
    """Sets a key-value pair to a given dictionary.

    Parameters
    ----------
    items
        Dictionary to set to.
    key
        Key to set.
    value
        Value to set to a given key.

    """

    items[key] = value


def swap_dictionary(items: Dict[Any, Any]) -> Dict[Any, Any]:
    """Builds a dictionary with swapped keys and values.

    Parameters
    ----------
    items
        Source dictionary.

    Returns
    -------
    dict
        Dictionary with swapped keys and values given
        from an input dictionary.

    """

    return {value: key for key, value in items.items()}


def increase(factor: int) -> Callable[[int], int]:
    """Creates a scaling function.

    Parameters
    ----------
    factor
        Number to scale by.

    Returns
    -------
    function
        Function that accepts an integer
        and multiplies it with given factor.

    """

    return lambda x: x * factor
