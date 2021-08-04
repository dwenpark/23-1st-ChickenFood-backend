from django.db import models

class Coupon(models.Model):
    name     = models.CharField(max_length=200)
    discount = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'coupons'