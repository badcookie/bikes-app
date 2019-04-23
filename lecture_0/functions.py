from typing import List, Dict, Any, Callable


def is_name(word: str) -> bool:
    return word[0].isupper()


def normalize_full_name(first_name: str = '', last_name: str = '') -> str:
    full_name = f'{first_name} {last_name}'
    partial_name = f'{first_name}{last_name}'
    return full_name if first_name and last_name else partial_name


def increase_list(*args: int) -> List[int]:
    first_value, second_value, *rest = args
    factor = 2
    return [first_value * factor, second_value * factor]


def filter_list(items: List[int]) -> List[int]:
    return list(filter(lambda item: item > 0, items))


def max_list(items: List[int], first_number: int, second_number: int) -> None:
    if first_number == second_number:
        return

    max_number = first_number if first_number > second_number else second_number
    items.append(max_number)


def get_dictionary(key: Any, value: Any) -> Dict[Any, Any]:
    return {key: value}


def set_dictionary(items: Dict[Any, Any], key: Any, value: Any) -> None:
    items[key] = value


def swap_dictionary(items: Dict[Any, Any]) -> Dict[Any, Any]:
    return {value: key for key, value in items.items()}


def increase(factor: int) -> Callable[[int], int]:
    return lambda x: x * factor
