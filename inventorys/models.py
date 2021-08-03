from django.db          import models

from members.models     import Member
from products.models    import Product, Option

class Inventory(models.Model):
    member_id  = models.ForeignKey(Member, on_delete=models.CASCADE, db_column="member_id")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column="product_id")
    quantity   = models.PositiveIntegerField(default=0)
    option_id  = models.ForeignKey(Option, on_delete=models.CASCADE, db_column="option_id")

    class Meta:
        db_table = 'inventorys'