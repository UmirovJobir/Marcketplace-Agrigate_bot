from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            for user in settings.ADMINS:
                username = user[0].replace(' ', '')
                email = user[1]
                password = '123'
                self.stdout.write('Creating account for %s (%s)' % (username, email))
                admin = User.objects.create_superuser(email=email, username=username, password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
                self.stdout.write(f"Created user '{admin}'")
        else:
            self.stdout.write('Admin accounts can only be initialized if no Accounts exist')


