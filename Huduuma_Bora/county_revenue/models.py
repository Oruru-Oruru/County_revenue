from django.db import models

# Create your models here.

from django.db import models

class CountyCustomer(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    enterprises = models.ManyToManyField('Enterprise', related_name='county_customers')

    def __str__(self):
        return self.name

class Enterprise(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20)
    address = models.TextField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Revenue(models.Model):
    county_customer = models.ForeignKey(CountyCustomer, on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f'Revenue #{self.id}'

class Defaulter(models.Model):
    revenue=models.ForeignKey(Revenue, default ='1',on_delete=models.CASCADE)
    enterprise=models.ForeignKey(Enterprise,default ='1', on_delete=models.CASCADE)
    service=models.ForeignKey(Service, default ='1', on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    def __str__(self):
        return self.name



class Invoice(models.Model):
    customer = models.ForeignKey(CountyCustomer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    invoice_number = models.CharField(max_length=20)
    issued_date = models.DateField()

    def __str__(self):
        return self.invoice_number


class MpesaExpressResponse(models.Model):
    party_a = models.CharField(max_length=12)
    transaction_time = models.DateTimeField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add more fields as needed to store other response data

    def __str__(self):
        return f'M-Pesa Express Response - ID: {self.id}'



class MpesaResponse(models.Model):
    response_code = models.CharField(max_length=10)
    response_description = models.CharField(max_length=255)
    customer_message = models.CharField(max_length=255)
    merchant_request_id = models.CharField(max_length=50)
    checkout_request_id = models.CharField(max_length=50)
    response_json = models.JSONField()

    def __str__(self):
        return f'M-Pesa Response - ID: {self.id}'

