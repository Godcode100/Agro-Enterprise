from django.db import models

# Create your models here.
class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending',"Pending"),
        ('successful',"Successful"),
        ('failed',"Failed")
    ]
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    phone_number = models.CharField(max_length=15)
    checkout_request_id = models.CharField(max_length=100,blank=True,null=True)
    receipt_number = models.CharField(max_length=100,blank=True,null=True)
    result_code = models.IntegerField(blank=True,null=True)
    result_description = models.TextField(blank=True,null=True)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} {self.phone_number}"