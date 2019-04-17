from functions import is_name, normalize_full_name


def test_is_name():
    """
    Реализовать проверку, того что строка начинается с заглавной буквы
    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
    https://docs.python.org/3.4/library/stdtypes.html#string-methods
    :return:
    """
    assert is_name('Ivan')
    assert not is_name('ivan')
    assert not is_name('1 room')


def test_normalize_full_name():
    """
    Реализовать функцию, которая на вход принимает именнованный аргументы,
    а возвращает строку в которой записаны через пробел first_name last_name. В случае
    если нет одного из них возвращать только 1 строку или если нет обоих пустую строку
    https://docs.python.org/3/tutorial/controlflow.html#if-statements
    https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments
    https://docs.python.org/3/library/functions.html#format
    :return:
    """
    assert 'Ivan Petrov' == normalize_full_name(last_name='Petrov', first_name='Ivan')
    assert 'Adam Smith' == normalize_full_name(first_name='Adam', last_name='Smith')
    assert 'Helen' == normalize_full_name(first_name='Helen')
    assert 'Ivanov' == normalize_full_name(last_name='Ivanov')
    assert '' == normalize_full_name()


def test_functions():
    pass


def test_classes():
    pass
