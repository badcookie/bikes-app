def is_name(word):
    return word[0].isupper()


def normalize_full_name(first_name='', last_name=''):
    full_name = f'{first_name} {last_name}'
    partial_name = f'{first_name}{last_name}'
    return full_name if first_name and last_name else partial_name


def increase_list(*args):
    first, second, *rest = args
    factor = 2
    return [first * factor, second * factor]


def filter_list(lst):
    return list(filter(lambda item: item > 0, lst))


def max_list(lst, first_num, second_num):
    if first_num == second_num:
        return

    max_num = first_num if first_num > second_num else second_num
    lst.append(max_num)


def get_dictionary(key, value):
    return {key: value}


def set_dictionary(dct, key, value):
    dct[key] = value


def swap_dictionary(dct):
    return {value: key for key, value in dct.items()}


def increase(factor):
    return lambda x: x * factor
