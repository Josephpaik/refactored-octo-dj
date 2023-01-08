from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    # image_url = models.CharField(max_length=2083)
    # products 

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now_add=True)

class Collection(models.Model):
    title = models.CharField(max_length=255)
    # description = models.TextField()
    # products = models.ManyToManyField(Product)
    # last_updated = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now_add=True)
    # image_url = models.CharField(max_length=2083)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)
    promotion = models.ManyToManyField(Promotion) # , related_name='products')
    
class Customer(models.Model):
    MEMBERSHIP_PLATINUM = 'P'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_BRONZE = 'B'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_PLATINUM, 'Platinum'),
        (MEMBERSHIP_GOLD, 'Gold'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_BRONZE, 'Bronze'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    # address = models.CharField(max_length=255) # django creates a foreign key for us
    last_updated = models.DateTimeField(auto_now_add=True)

   
class Order(models.Model):
    ORDER_STATUS_PENDING = 'P'
    ORDER_STATUS_SHIPPED = 'S'
    ORDER_STATUS_DELIVERED = 'D'
    ORDER_STATUS_CANCELLED = 'C'
    
    ORDER_STATUS_CHOICES = [
        (ORDER_STATUS_PENDING, 'Pending'),
        (ORDER_STATUS_SHIPPED, 'Shipped'),
        (ORDER_STATUS_DELIVERED, 'Delivered'),
        (ORDER_STATUS_CANCELLED, 'Cancelled'),
    ]
    placed_ad = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    last_updated = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

# class CustomerAddress
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)  # primary_key=True removed. one to many relationship
