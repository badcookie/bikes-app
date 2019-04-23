def get_diff(first_number: int, second_number: int) -> int:
    """Calculates difference between two numbers.

    Parameters
    ----------
    first_number
        Value to subtract from.
    second_number
        Subtracted value.

    Raises
    ------
    ValueError
        Raised if subtracted value is greater
        or equal to one to subtract from.

    Returns
    -------
    int
        Difference.

    """

    if second_number >= first_number:
        raise ValueError('Max error')

    return first_number - second_number
