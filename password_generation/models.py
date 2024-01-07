from django.db import models


# class PasswordGeneration(models.Model):
#     name = models.CharField(max_length=256)
#     value = models.IntegerField(default=0)
#     email = models.EmailField(max_length=254)
#
#     def __str__(self):
#         return self.name

class PasswordGenerationStats(models.Model):
    generation_count = models.IntegerField(default=0)


class UserGeneratedPassword(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    generated_password = models.CharField(max_length=100)
