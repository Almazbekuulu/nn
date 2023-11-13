from django.db import models


from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    page_count = models.IntegerField()
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
