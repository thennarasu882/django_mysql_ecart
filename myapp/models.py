from django.db import models
# Create your models here.


class customers(models.Model):
    person_id = models.IntegerField(unique=True, default=100)
    first_name = models.CharField(max_length=120, default=" ")
    last_name = models.CharField(max_length=120, default=" ")
    mobile_no = models.IntegerField(default=0)
    address = models.TextField(max_length=600, default=" ")

    def __str__(self):
        return self.first_name + " " + self.last_name


class products(models.Model):
    product_id = models.IntegerField(unique=True, default=1)
    product_name = models.CharField(max_length=150, default=" ")
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=600, default=" ")
    image = models.CharField(max_length=400, default=" ")

    def __str__(self):
        return self.product_name


class orders_data(models.Model):
    order_id = models.IntegerField(unique=True, default=1)
    customer = models.ForeignKey(customers, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.order_id)
