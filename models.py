from django.db import models


class User(models.Model):
    username = username = models.CharField('username', max_length=200, default='SOME STRING')
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=True, null=False)
    last_name = models.CharField('Last Name', max_length=255, blank=True, null=False)

    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"


