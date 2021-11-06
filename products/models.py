from django.db import models
from django.db.models import Avg
from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254,  null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    avg_rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024,  null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def calculate_rating(self):
        """
        The average product rating
        from all related reviews ratings
        """
        self.avg_rating = self.reviews.aggregate(Avg("rate"))["rate__avg"]
        self.save()


class Review(models.Model):

    RATE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, null=True, blank=True,
        related_name='reviews',
        on_delete=models.SET_NULL)
    comment = models.TextField(max_length=500)
    rate = models.IntegerField(choices=RATE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def save(self, *args, **kwargs):
        self.product.calculate_rating()
        super().save(*args, **kwargs)
