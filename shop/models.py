from django.db import models
from django.urls import reverse


# Custom Queryset
class ProductQuerysSet(models.query.QuerySet):
    def available(self):
        return self.filter(available=True)

    def featured(self):
        return self.filter(featured=True, available=True)


# Custom Model Manager
class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerysSet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().available()

    def featured(self):
        return self.get_queryset().featured()


class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(default="default.jpeg", upload_to="products %Y%M%d")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    featured = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    class Meta:
        ordering = ("-name",)

    def get_absolute_url(self, *args, **kwargs):
        return reverse("shop:product-detail", kwargs={"slug": "slug"})

    def __str__(self):
        return self.name
