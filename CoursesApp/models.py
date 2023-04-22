from django.db import models
from django.contrib.postgres.fields import ArrayField
from django import forms


class Category(models.Model):
    name = models.CharField(max_length=500)
    imgpath = models.CharField(max_length=500)


class Branch(models.Model):
    latitude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)
    address = models.CharField(max_length=500)


CONTACTS = (
    (1, "PHONE"),
    (2, "FACEBOOK"),
    (3, "EMAIL"),
)


class Contact(models.Model):
    type = models.IntegerField(choices=CONTACTS, default=1)


class Course(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(
        Category, related_name="models", on_delete=models.CASCADE
    )
    logo = models.CharField(max_length=500)
    contacts = models.ManyToManyField(Contact, related_name="models")
    # Array<Contact>
    branches = models.ManyToManyField(Branch, related_name="models")
    # Array<Branch>
