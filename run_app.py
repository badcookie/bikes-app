import os
import sys
import gunicorn.app.base
from gunicorn.six import iteritems
from django.core.wsgi import get_wsgi_application


sys.path.insert(1, './bikes')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'heroku_settings')
application = get_wsgi_application()


def create_super_user():
    from django.contrib.auth.models import User

    username = 'admin'
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, 'admin@example.com', 'admin')


def create_categories():
    from bikes_site.models import Category

    Category.objects.get_or_create(name='motorcycle'),
    Category.objects.get_or_create(name='motorbike'),


def create_company(company_name, username, password):
    from bikes_site.models import Company

    company, created = Company.objects.get_or_create(name=company_name)
    if created:
        create_manager(company, username, password)


def create_manager(company, username, password):
    from django.contrib.auth.models import User
    from bikes_site.models import Manager

    user = User.objects.create_user(username, 'manager@example.com', password)
    Manager.objects.create(company=company, user=user)


# Взято отсюда https://docs.gunicorn.org/en/stable/custom.html
class PythonIntroApplication(gunicorn.app.base.BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(PythonIntroApplication, self).__init__()

    def load_config(self):
        for key, value in iteritems(self.options):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    from django.core.management import call_command

    call_command('migrate')
    create_super_user()
    create_categories()
    create_company('Osinit Motor Company', 'osinit', 'osinit')
    options = {'workers': 1}
    PythonIntroApplication(application, options).run()
