from django.db import models


class User(models.Model):
    """ User model """

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        """ Return username """

        return self.username

    class Meta:
        """ Meta class """

        ordering = ['username']
