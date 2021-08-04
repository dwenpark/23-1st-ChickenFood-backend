from django.db          import models

from members.models     import Member
from products.models    import Product, Option

class Inventory(models.Model):
    member   = models.ForeignKey(Member, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    option   = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'inventorys'