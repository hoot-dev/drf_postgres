from django.db import models

from films.models import Film
from customers.models import Customer, Address


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    email = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.SmallIntegerField()
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField()
    picture = models.ImageField(upload_to='images/', blank=True, null=True)

    class Meta:
        db_table = 'staff'
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.ForeignKey(Staff, models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'store'
    
    def __str__(self):
        return f'Store {self.store_id}'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, models.DO_NOTHING)
    store = models.ForeignKey(Store, models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'inventory'
    
    def __str__(self):
        return self.film.title

class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey(Staff, models.DO_NOTHING)
    last_update = models.DateTimeField()

    class Meta:
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)
        ordering = ['-rental_id']
    
    def __str__(self):
        return f'Rental Date: {self.rental_date}'
    
    @property
    def payments(self):
        return self.payment_set.all()


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    staff = models.ForeignKey(Staff, models.DO_NOTHING)
    rental = models.ForeignKey(Rental, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    class Meta:
        db_table = 'payment'
    
    def __str__(self):
        return f'{self.amount}'
