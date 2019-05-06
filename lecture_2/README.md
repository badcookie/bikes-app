# Lecture 2
### Django Rest Framework, why? (3 минуты)
- [сайт](https://www.django-rest-framework.org/)
- [tutorial](https://www.django-rest-framework.org/tutorial/quickstart/)

### Serializers (10 минут)
### ViewSets (10 минут)
### URLs (10 минут)
### Permissions (10 минут)

### Задание, порядок работы (10 минут)
Для того чтобы CI сработал название ветки `lecture_2`.
Из задания `lecture_1` вам надо перенести ваш каталог bikes 
на уровень выше, чтобы он оказался в корне папки. Чтобы проверить надо смотреть вкладку `CI/CD-Pipelines`
Локальный запуск Code Quality
```bash
black --exclude=\venv bikes/
flake8 bikes/
```
Локальный запуск Tests
```bash
cd bikes
pytest ../lecture_2/tests.py
```
Локальный запуск Tests, конкректного теста. Чтобы не было ошибок, 
можно закомментировать строки импорта
```bash
cd bikes
pytest ../lecture_2/tests.py::test_is_name
```
