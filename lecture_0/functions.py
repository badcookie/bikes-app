def is_name(word):
    return word[0].isupper()


def normalize_full_name(first_name='', last_name=''):
    full_name = f'{first_name} {last_name}'
    partial_name = f'{first_name}{last_name}'
    return full_name if first_name and last_name else partial_name


def increase_list(*args):
    first_value, second_value, *rest = args
    factor = 2
    return [first_value * factor, second_value * factor]


def filter_list(items):
    return list(filter(lambda item: item > 0, items))


def max_list(items, first_number, second_number):
    if first_number == second_number:
        return

    max_number = first_number if first_number > second_number else second_number
    items.append(max_number)


def get_dictionary(key, value):
    return {key: value}


def set_dictionary(items, key, value):
    items[key] = value


def swap_dictionary(items):
    return {value: key for key, value in items.items()}


def increase(factor):
    return lambda x: x * factor
