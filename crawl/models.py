from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, default="", unique=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200, default="", unique=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=200, default="", unique=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=2000, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    size = models.ManyToManyField(Size)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='product/products', blank=True, null=True, max_length=2000)

    def __str__(self):
        return self.title
