from typing import List

import pytest
from random import randint
from bikes_site.models import Product


def get_company_url(url):
    return ''.join(['/api/v1/company/products/', url])


def get_product_url(url):
    return ''.join(['/api/v1/products/', url])


PRODUCT_URL = get_company_url('{}/')
PRODUCTS_LIST_URL = get_company_url('')
PRODUCTS_BY_TYPE_LIST_URL = get_company_url('category/{}/')

PUBLIC_PRODUCT_URL = get_product_url('{}/')
PUBLIC_PRODUCTS_LIST_URL = get_product_url('category/{}/')


def get_random_id(company):
    product_index = randint(0, len(company.initial_product_ids) - 1)
    product_id = company.initial_product_ids[product_index]
    return product_id


def check_products(company) -> List[dict]:
    """
    Проверяем, что отдаем для каждого менеджера только свой список продуктов и в нужном формате
    :param company: CompanyFixture
    :return:
    """
    http_response = company.client.get(PRODUCTS_LIST_URL)
    assert http_response.status_code == 200, http_response.content
    json_response = http_response.json()
    assert {'id', 'name', 'description', 'category_name'} == set(
        json_response[0].keys()
    )
    assert company.initial_product_ids == [product['id'] for product in json_response]
    return json_response


def check_category_products(company, category_id, products):
    """
    Тут мы проверяем что по id категории получаем только нужные продукты, и потом
    проверяем, что если делаем запрос по не существующей категории получаем 404
    :param company: CompanyFixture
    :param category_id: Category
    :param products: список словарей продуктов для данной категории
    :return:
    """
    http_response = company.client.get(PRODUCTS_BY_TYPE_LIST_URL.format(category_id))
    assert http_response.status_code == 200, http_response.content
    json_response = http_response.json()
    assert products == json_response

    http_response = company.client.get(PRODUCTS_BY_TYPE_LIST_URL.format(10000))
    assert http_response.status_code == 404, http_response.content


@pytest.mark.django_db
def test_manager_view_private_list(ducati, kawasaki, categories):
    """
    В этом тесте мы подготовили фикстуры, которые содержат список Product для двух компаний
    Ducati и Kawasaki, в двух категоряих. Ваш view должен определить, что это за manager
    и отдать нужный список.
    https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    https://www.django-rest-framework.org/api-guide/fields/#source
    https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/#tutorial-4-authentication-permissions
    :param ducati:
    :param kawasaki:
    :return:
    """
    category_id, category_name = categories[0].id, categories[0].name
    for company in [ducati, kawasaki]:
        products = check_products(company)
        category_products = [
            product for product in products if product['category_name'] == category_name
        ]
        check_category_products(company, category_id, category_products)


def check_create(target_company, other_company, category):
    name = 'Created by: {}, category: {}'.format(
        target_company.company.name, category.name
    )
    base_data = {'name': name, 'description': 'Description'}
    payload = {'category': category.id, **base_data}

    # Проверка, создания продукта
    http_response = target_company.client.post(
        PRODUCTS_LIST_URL, payload, format='json'
    )
    assert http_response.status_code == 201, http_response.content
    json_response = http_response.json()
    product_id = json_response.pop('id')
    expected_response = {'category_name': category.name, **base_data}
    assert json_response == expected_response

    # Проверка, доступности продукта по id
    http_response = target_company.client.get(PRODUCT_URL.format(product_id))
    assert http_response.status_code == 200, http_response.content
    json_response = http_response.json()
    assert json_response == {'id': product_id, **expected_response}

    # Проверка валидации запроса
    http_response = target_company.client.post(
        PRODUCTS_LIST_URL, base_data, format='json'
    )
    assert http_response.status_code == 400, http_response.content

    # Проверка, что другим компаниям не доступно
    http_response = other_company.client.get(PRODUCT_URL.format(product_id))
    assert http_response.status_code == 404, http_response.content


@pytest.mark.django_db
def test_manager_add_new_entity(ducati, kawasaki, categories):
    """
    В этом тесте мы создадим для определнной категории и компании новый продукт, проверим что он создался, и
    проверим что не доступен для другой компании.
    https://www.django-rest-framework.org/api-guide/generic-views/#methods
    https://www.django-rest-framework.org/api-guide/generic-views/#get_objectself
    https://www.django-rest-framework.org/api-guide/generic-views/#retrievemodelmixin
    https://www.django-rest-framework.org/api-guide/relations/#primarykeyrelatedfield
    :param ducati:
    :param kawasaki:
    :param categories:
    :return:
    """
    check_create(ducati, kawasaki, categories[0])
    check_create(kawasaki, ducati, categories[0])


def check_edit(target_company, other_company):
    product_id = get_random_id(target_company)
    update_data = {'name': 'Edited name'}

    # Проверка, изменения продукта
    http_response = target_company.client.put(
        PRODUCT_URL.format(product_id), update_data, format='json'
    )
    assert http_response.status_code == 200, http_response.content

    # Проверка, доступности продукта по id
    http_response = target_company.client.get(PRODUCT_URL.format(product_id))
    assert http_response.status_code == 200, http_response.content
    json_response = http_response.json()
    assert json_response['name'] == update_data['name']

    http_response = other_company.client.put(
        PRODUCT_URL.format(product_id), update_data, format='json'
    )
    assert http_response.status_code == 404, http_response.content


@pytest.mark.django_db
def test_manager_edit_entity(ducati, kawasaki):
    """
    В этом тесте мы будем изменять название продукта и проверять что действительно
    изменилось, как обычно проверим на недоступность на изменение менеджером другой
    компании
    https://www.django-rest-framework.org/api-guide/generic-views/#get_objectself
    https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    https://www.django-rest-framework.org/api-guide/generic-views/#updatemodelmixin
    https://www.django-rest-framework.org/api-guide/generic-views/#updateapiview
    https://www.django-rest-framework.org/api-guide/requests/#method
    :param ducati:
    :param kawasaki:
    :return:
    """
    check_edit(ducati, kawasaki)
    check_edit(kawasaki, ducati)


def check_delete(target_company, other_company):
    product_id = get_random_id(target_company)
    http_response = target_company.client.delete(PRODUCT_URL.format(product_id))
    assert http_response.status_code == 204, http_response.content

    http_response = target_company.client.get(PRODUCTS_LIST_URL)
    assert http_response.status_code == 200, http_response.content
    json_response = http_response.json()
    assert product_id not in list(map(lambda x: x['id'], json_response))
    assert len(target_company.initial_product_ids) - 1 == len(json_response)

    http_response = other_company.client.delete(PRODUCT_URL.format(product_id))
    assert http_response.status_code == 404, http_response.content


@pytest.mark.django_db
def test_manager_delete_entity(ducati, kawasaki):
    """
    В этом тесте мы будем удалять продукт и проверять что действительно
    удалилось, как обычно проверим на недоступность на удаление менеджером другой
    компании
    https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    https://www.django-rest-framework.org/api-guide/generic-views/#destroymodelmixin
    https://www.django-rest-framework.org/api-guide/generic-views/#destroyapiview
    https://www.django-rest-framework.org/api-guide/generic-views/#get_objectself
    :param ducati:
    :param kawasaki:
    :return:
    """
    check_delete(ducati, kawasaki)
    check_delete(kawasaki, ducati)


def check_public_product_list(client, category):
    page_size = 5
    http_response = client.get(PUBLIC_PRODUCTS_LIST_URL.format(category.id))
    products = Product.objects.filter(category=category).values(
        'id', 'name', 'description'
    )[:5]
    assert http_response.status_code == 200, http_response.content
    json_response = http_response.json()
    assert json_response['next']
    assert not json_response['previous']
    assert len(json_response['results']) == page_size
    assert json_response['results'] == list(products)

    http_response = client.get(json_response['next'])
    assert http_response.status_code == 200, http_response.content
    json_response = http_response.json()
    assert json_response['previous']


@pytest.mark.django_db
def test_user_get_list_of_entities(ducati, user_client, categories):
    """
    Получаем список продуктов по категориям, на каждой странице должно быть 5 элементов
    https://www.django-rest-framework.org/api-guide/generic-views/#get_serializer_classself
    https://www.django-rest-framework.org/api-guide/generic-views/#get_querysetself
    https://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
    https://www.django-rest-framework.org/api-guide/permissions/#isauthenticatedorreadonly
    :param ducati:
    :param user_client:
    :param categories:
    :return:
    """
    for category in categories:
        check_public_product_list(user_client, category)


def check_public_product(company, client):
    product_id = get_random_id(company)
    product = Product.objects.get(pk=product_id)
    expected_result = {
        'name': product.name,
        'description': product.description,
        'company_name': product.company.name,
    }
    http_response = client.get(PUBLIC_PRODUCT_URL.format(product_id))
    assert http_response.status_code == 200, http_response.content
    json_response = http_response.json()
    assert expected_result == json_response


@pytest.mark.django_db
def test_user_get_entity_detail(ducati, kawasaki, user_client):
    """
    Проверим получение деталей продукта по id
    https://www.django-rest-framework.org/api-guide/generic-views/#get_objectself
    https://www.django-rest-framework.org/api-guide/generic-views/#retrievemodelmixin
    https://www.django-rest-framework.org/api-guide/relations/#primarykeyrelatedfield
    :param ducati:
    :param kawasaki:
    :param user_client:
    :return:
    """
    check_public_product(ducati, user_client)
    check_public_product(kawasaki, user_client)
