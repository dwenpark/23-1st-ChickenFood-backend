from django.db import models

class Brand(models.Model):
    name  = models.CharField(max_length=200)
    image = models.CharField(max_length=2000)

    class Meta:
        db_table  = 'brands'

class Type(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table  = 'types'

class Product(models.Model):
    name          = models.CharField(max_length=200)
    price         = models.DecimalField(max_digits=10, decimal_places=2)
    brand         = models.ForeignKey("Brand", on_delete=models.CASCADE)
    type          = models.ForeignKey("Type", on_delete=models.CASCADE)
    like_number   = models.PositiveIntegerField(default=0)
    thumbnail     = models.CharField(max_length=2000)
    detail_image  = models.CharField(max_length=2000)
    element       = models.CharField(max_length=200)
    weight        = models.CharField(max_length=200)
    register_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table  = 'products'

class Image(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    image   = models.CharField(max_length=2000)

    class Meta:
        db_table  = 'images'

class Option(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table  = 'options'
