from typing import List

import pytest
from rest_framework.test import APIClient
from bikes_site.models import Manager, Company, Category, Product
from django.contrib.auth.models import User
from dataclasses import dataclass


@dataclass
class CompanyFixture(object):
    username: str
    password: str
    user: User
    company: Company
    manager: Manager
    client: APIClient
    initial_product_ids: List[int]


def create_company_product(
    count: int, company: 'Company', category: 'Category'
) -> List[int]:
    base_name = company.name.split()[0]

    def get_name(num: int):
        return f'{base_name} {category.name} {num}'

    ids = []
    for i in range(count):
        product = Product.objects.create(
            name=get_name(i),
            category=category,
            company=company,
            description='description',
        )
        ids.append(product.id)
    return ids


def create_company_fixture(
    username: str, password: str, company_name: str, categories: List[Category]
) -> 'CompanyFixture':
    user = User.objects.create(username=username, password=password)
    company = Company.objects.create(name=company_name)
    manager = Manager.objects.create(company=company, user=user)
    count_motorcycle = 16
    count_motorbike = 8
    product_ids = [
        *create_company_product(count_motorcycle, company, categories[0]),
        *create_company_product(count_motorbike, company, categories[1]),
    ]
    client = APIClient()
    return CompanyFixture(
        username=username,
        password=password,
        user=user,
        company=company,
        manager=manager,
        client=client,
        initial_product_ids=product_ids,
    )


@pytest.fixture
def categories():
    return [
        Category.objects.create(name='motorcycle'),
        Category.objects.create(name='motorbike'),
    ]


@pytest.fixture
def ducati(categories):
    company = create_company_fixture(
        'Antonio', '12345', 'Ducati Motor Holding S.p.A.', categories
    )
    company.client.force_authenticate(company.user)
    yield company
    company.client.logout()


@pytest.fixture
def kawasaki(categories):
    company = create_company_fixture(
        'Kawasaki', '12345', 'Kawasaki Heavy Industries, Ltd.', categories
    )
    company.client.force_authenticate(company.user)
    yield company
    company.client.logout()


@pytest.fixture
def user_client():
    return APIClient()
