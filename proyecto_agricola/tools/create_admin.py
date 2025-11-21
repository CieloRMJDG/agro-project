import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_agricola.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = 'admin'
password = 'Admin123!'
email = 'admin@example.com'

u = User.objects.filter(username=username).first()
if not u:
    User.objects.create_superuser(username, email, password)
    print('created superuser')
else:
    u.set_password(password)
    u.is_staff = True
    u.is_superuser = True
    u.save()
    print('updated existing user: set password + staff/superuser')

print('done')
