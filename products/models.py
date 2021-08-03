from django.db import models

class Category(models.Model):
    name         = models.CharField(max_length=200)

    class Meta:
        db_table = 'categorys'

class Brand(models.Model):
    name         = models.CharField(max_length=200)
    category_id  = models.ForeignKey("Category", on_delete=models.CASCADE, db_column="category_id")

    class Meta:
        db_table = 'brands'

class Type(models.Model):
    name         = models.CharField(max_length=200)
    category_id  = models.ForeignKey("Category", on_delete=models.CASCADE, db_column="category_id")

    class Meta:
        db_table = 'types'

class Product(models.Model):
    name         = models.CharField(max_length=200)
    price        = models.DecimalField(max_digits=10, decimal_places=2)
    brand_id     = models.ForeignKey("Brand", on_delete=models.CASCADE, db_column="brand_id")
    type_id      = models.ForeignKey("Type", on_delete=models.CASCADE, db_column="type_id")
    like_number  = models.PositiveIntegerField(default=0)
    thumbnail    = models.CharField(max_length=500)
    detail_image = models.CharField(max_length=500)
    element      = models.TextField()
    weight       = models.TextField()

    class Meta:
        db_table = 'products'

class Image(models.Model):
    product_id   = models.ForeignKey("Product", on_delete=models.CASCADE, db_column="product_id")
    image        = models.CharField(max_length=500)

    class Meta:
        db_table = 'images'

class Option(models.Model):
    name         = models.CharField(max_length=200)

    class Meta:
        db_table = 'options'
