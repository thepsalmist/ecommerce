from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(default="default.jpeg", upload_to="products %Y%M%d")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-name",)

    def __str__(self):
        return self.name
