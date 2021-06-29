import os, django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miicms.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
if User.objects.filter(username='admin').exists() != True:
    password = User.objects.make_random_password()
    User.objects.create_superuser('admin', 'tienv2i@gmail.com', password)
    print('Created user \'admin\' with password: ', password)
else:
    print('Superuser existed..! >>')