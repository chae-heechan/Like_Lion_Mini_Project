from django.db import models
from django.db.models.fields.files import ImageField

class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_university = models.CharField(max_length=50)
    user_profile = models.ImageField(upload_to = "user/", blank=True, null=True)

    def __str__(self):
        return self.user_name

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_content = models.TextField()
    product_profile = models.ImageField(upload_to = "product/", blank=True, null=True)

    def __str__(self):
        return self.product_name