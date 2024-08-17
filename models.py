from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):

  title = models.CharField(max_length=100)
  price = models.FloatField()
  description = models.TextField()  
  expiry_date = models.DateField() 
  mg = models.IntegerField()  
  net_quantity = models.PositiveIntegerField()
  batch_no = models.CharField(max_length=50)
  brand = models.CharField(max_length=100)
  item_weight = models.DecimalField(max_digits=10, decimal_places=2)
  item_form = models.CharField(max_length=50)
  age_range = models.CharField(max_length=20)
  item_dimension = models.CharField(max_length=50)
  availability_status = models.CharField(max_length=20)
  product_image = models.ImageField(upload_to='product')



class CartItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
  


  def __str__(self):
    return self.title

