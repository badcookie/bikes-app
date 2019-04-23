def get_diff(first_number: int, second_number: int) -> int:
    if second_number >= first_number:
        raise ValueError('Max error')

    return first_number - second_number
