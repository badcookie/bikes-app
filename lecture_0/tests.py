import pytest
from functions import (
    is_name,
    normalize_full_name,
    get_dictionary,
    set_dictionary,
    swap_dictionary,
    increase_list,
    filter_list,
    max_list,
    increase,
)
from modules import to_json
from exceptions import get_diff
from classes import Student, StudentCourseError


def test_is_name():
    """
    Реализовать проверку, того что строка начинается с заглавной буквы
    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
    https://docs.python.org/3/library/stdtypes.html#string-methods
    :return:
    """
    assert is_name('Ivan')
    assert not is_name('ivan')
    assert not is_name('1 room')


def test_normalize_full_name():
    """
    Реализовать функцию functions.normalize_full_name, которая на вход принимает именнованный аргументы,
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


def test_lists():
    """
    Реализовать следующие функции:
    - functions.increase_list, принимает на вход 3 аргумента, возвращает список из двух элементов,
    которые являются первыми 2
    аргументами умножиными на 3.
    - functions.filter_list принимает список, возвращает список, в котором все элементы больше 0
    - functions.max_list принимает на вход 3 аргумента. 1-ый список, 2-ой и 3-ий числа. В список добавляет
    наибольший элемент.
    Если элементы равны ничего не добавляет.
    https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    https://docs.python.org/3/tutorial/controlflow.html#if-statements
    :return:
    """
    assert increase_list(10, 20, 2) == [20, 40]
    assert increase_list(0, 3, 2) == [0, 6]

    assert filter_list([1, -1, -2, 3, 0, 4, -10]) == [1, 3, 4]
    assert filter_list([0, -1, -2, -10]) == []
    assert filter_list([10, 1, 5, 4]) == [10, 1, 5, 4]

    list_1 = [1, 2, 3]
    max_list(list_1, 4, 5)
    assert list_1 == [1, 2, 3, 5]

    list_2 = [1, 2, 3]
    max_list(list_2, 4, 4)
    assert list_2 == [1, 2, 3]


def test_dictionary():
    """
    Реализовать функции:
    - functions.get_dictionary принимает на вход два аргумента, ключ и значение. Возвращает словаь с ключом
      и значением в нем
    - functions.set_dictionary принимает на вход 3 аргумента, словарь, ключ и значение, которые добавляет
      в словарь, ничего не
    - functions.swap_dictionary принимает на вход словарь, а возвращает другой словарь в котором ключ и значение
      поменялись местами.
    возвращает.
    https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    :return:
    """
    assert get_dictionary('foo', 'bar') == {'foo': 'bar'}

    dictionary_1 = {'foo': 'bar'}
    set_dictionary(dictionary_1, 'key', 'value')
    assert dictionary_1 == {'foo': 'bar', 'key': 'value'}

    dictionary_2 = {'key_1': 'value_1', 'key_2': 'value_2'}
    assert swap_dictionary(dictionary_2) == {'value_1': 'key_1', 'value_2': 'key_2'}

    dictionary_3 = {}
    assert swap_dictionary(dictionary_3) == {}


def test_functions():
    """
    Реализовать функцию functions.increase, которая на вход принимает аргумент число и возращает другую функцию,
    которая на вход принимает аргумент число и возвращает чилсо умноженное на аргумент переданный в первой функции:
    https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
    :return:
    """
    increase_1 = increase(10)
    assert increase_1(2) == 20
    assert increase_1(3) == 30

    increase_2 = increase(2)
    assert increase_2(2) == 4
    assert increase_2(3) == 6


def test_modules():
    """
    Добавить модуль modules и реализовать функцию modules.to_json которая на вход принимает
    один из встроенных типов Python, а возвращает json строку
    https://docs.python.org/3/tutorial/modules.html
    https://docs.python.org/3/library/json.html
    :return:
    """
    assert to_json({'foo': 'bar'}) == '{"foo": "bar"}'
    assert to_json([1, 2, 3]) == '[1, 2, 3]'
    assert to_json('hello world') == '"hello world"'


def test_exceptions():
    """
    Добавить модуль exceptions и реализовать функцию exceptions.get_diff которая на вход принимает
    два числа, и возращает их разность если второе меньше первого, в противном случае "бросает" ValueError,
    с текстом "Max error"
    https://docs.python.org/3/tutorial/errors.html
    :return:
    """
    assert get_diff(100, 10) == 90
    assert get_diff(10, 9) == 1
    with pytest.raises(ValueError, match=r'Max error'):
        get_diff(10, 11)
    with pytest.raises(ValueError, match=r'Max error'):
        get_diff(0, 1)


def test_classes():
    """
    Добавить модуль classes и реализовать класс classes.Student, который в конструкторе принимаем полное имя студента
    (full_name) и название курса, опционально (course_name), в инициалзаторе студенту присваивается атрибут
    course_num = 1. Дополнительно надо реализовать exception classes.StudentCourseError  Класс имеет 3 метода:
    - next_course(), который увиличивает текущий курс на один. Если в конструкторое не было передан курс в конструкторе,
      "бросает" ошибку StudentCourseError('Not have course'). Если курс равен 3 "бросает" ошибку
      StudentCourseError('Student have degree')
    - change_course(course_name), меняет название курса и сбрасывает course_num в 1
    - get_diploma(), возвращает строчку в которой через запятую full_name и course_name, если курс меньше 3 "бросает"
      ошибку StudentCourseError('Student not have degree')
    два числа, и возращает их разность если второе меньше первого, в противном случае "бросает" ValueError,
    с текстом "Max error"
    https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
    https://docs.python.org/3/tutorial/classes.html
    :return:
    """
    # Case 1
    lucy_smith = Student('Lucy Smith')
    assert lucy_smith.full_name == 'Lucy Smith'
    assert lucy_smith.course_name is None
    assert lucy_smith.course_num == 1

    with pytest.raises(StudentCourseError, match=r'Not have course'):
        lucy_smith.next_course()

    lucy_smith.change_course('Python')
    assert lucy_smith.course_name == 'Python'

    lucy_smith.next_course()
    assert lucy_smith.course_num == 2

    with pytest.raises(StudentCourseError, match=r'Student not have degree'):
        lucy_smith.get_diploma()

    lucy_smith.next_course()
    assert lucy_smith.course_num == 3
    with pytest.raises(StudentCourseError, match=r'Student have degree'):
        lucy_smith.next_course()

    assert lucy_smith.get_diploma() == 'Lucy Smith,Python'

    # Case 2
    joe_smith = Student('Joe Smith', 'NodeJS')
    assert joe_smith.full_name == 'Joe Smith'
    assert joe_smith.course_name == 'NodeJS'
    assert joe_smith.course_num == 1

    joe_smith.next_course()
    assert joe_smith.course_num == 2
    joe_smith.change_course('Python')
    assert lucy_smith.course_name == 'Python'
    assert joe_smith.course_num == 1
