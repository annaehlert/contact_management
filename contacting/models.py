from django.db import models

TYPES = (
    (1, "Mobile"),
    (2, "Home"),
    (3, "Work")
)
EMAILS = (
    (1, "Home"),
    (2, "Work")
)


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house_nr = models.IntegerField(default=1)
    flat_nr = models.IntegerField(null=True)
    code = models.CharField(max_length=6, default="00-000")


class User(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    description = models.CharField(max_length=500, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='address_person')


class Phone(models.Model):
    number = models.CharField(max_length=9, null=True)
    type = models.IntegerField(choices=TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_phone')


class Email(models.Model):
    email = models.CharField(max_length=64)
    email_type = models.IntegerField(choices=EMAILS)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_email')


class Group(models.Model):
    group = models.ManyToManyField(User)
