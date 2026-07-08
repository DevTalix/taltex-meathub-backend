from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('completed', 'Completed'),
    ]

    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.TextField()  # We will store the cart items as a JSON text
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"