from django.db         import models

from members.models    import Member
from products.models   import Product

class Like(models.Model):
    member  = models.ForeignKey(Member, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'