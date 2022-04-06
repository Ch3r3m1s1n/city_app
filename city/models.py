from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Citizen(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200)
    city = models.ForeignKey('city.City', on_delete=models.CASCADE, related_name='citizens')

    def __str__(self):
        return f"{self.lastname} {self.firstname} {self.middlename}"
