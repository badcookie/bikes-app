def get_diff(first_num: int, second_num: int) -> int:
    if second_num >= first_num:
        raise ValueError('Max error')

    return first_num - second_num
