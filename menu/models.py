from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200 , unique=True)
    slug = models.SlugField(max_length=25)
    image = models.ImageField(upload_to="static/category/" , blank=True,null=True)
    # def save(self, *args,**kwargs):
    #     self.slug = slugify(self.category_name)
    #     super(Category,self).save(*args , **kwargs)

    def __str__(self):
        return f"{self.category_name}"
    class Meta:
        verbose_name_plural = "Category"
    

class Product(models.Model):  #price ,food_title,food_detail,image
    category = models.ForeignKey(Category, related_name="food_items", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200) 
    image = models.ImageField(upload_to="menu/Food_image/")
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.product_name}"
    class Meta:
        verbose_name_plural = "Product"


class Special_Offer_Model(models.Model):
    product = models.ForeignKey(Product , related_name="special_offers",on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(max_digits=5,decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.discount_percentage}% off on {self.food_item}"
    class Meta:
        verbose_name_plural = "Special Offer"
    