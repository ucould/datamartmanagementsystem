from django.db import models

# Create your models here.


class Customer(models.Model):
    cust_num = models.IntegerField(unique=True)
    company = models.CharField(max_length=100)
    cust_rep = models.IntegerField()
    credit_limit=models.IntegerField()

    class Meta:
        db_table ='Customer'

class Product(models.Model):
    mfr_id = models.IntegerField(unique=True)
    product_id = models.IntegerField(unique=True)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    qty_in_hand = models.IntegerField()

    class Meta:
        db_table ='Product'

class Office(models.Model):
    office=models.IntegerField(unique='True')
    city=models.CharField(max_length=100)
    region=models.CharField(max_length=100)
    mgr=models.IntegerField()
    target_sales=models.IntegerField()

    class Meta:
        db_table ='Office'

class Salesrep(models.Model):
    emp_num=models.IntegerField(unique='True')
    mgr=models.IntegerField()
    rep_office=models.ForeignKey(Office,on_delete=models.CASCADE)
    hire_date=models.DateTimeField('hire date')
    age=models.IntegerField()
    quota=models.IntegerField()
    sales=models.IntegerField()
    name=models.CharField(max_length=10)

    class Meta:
        db_table ='Salesrep'

class Order(models.Model):
    mfr_id = models.IntegerField()
    product_id = models.IntegerField()
    order_date=models.DateTimeField('order date')
    order_num=models.IntegerField()
    qty=models.IntegerField()
    amount=models.IntegerField()
    sales_rep=models.ForeignKey(Salesrep,on_delete=models.CASCADE)
    cust=models.ForeignKey(Customer,on_delete=models.CASCADE)

    class Meta:
        db_table='Order'
