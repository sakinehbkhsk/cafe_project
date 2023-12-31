from django.db import models
from core.models import BaseModel
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    category_name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        # Generate the slug from the title
        self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)    
    
    def __str__(self) -> str:
        return self.category_name

    def get_absolute_url(self):
        return reverse('category_filter', args=[self.slug,])


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image_src = models.ImageField()
    discount = models.PositiveSmallIntegerField()
    serving_time = models.DurationField()
    estimated_cooking_time = models.DurationField()
    # discount_price = models.PositiveBigIntegerField()
    is_available = models.BooleanField(default=True)
    
    @property
    def discount_to_price(self):
        if self.discount > 0:
            total_price = self.price - (self.price * self.discount / 100)
            return float(total_price)
        return 0

    # def save(self, *args, **kwargs):
    #     self.discount_price = self.discount_to_price() 
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name
