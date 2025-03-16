from django.db import models
from django.db.models import CharField


# Create your models here.
class Reader(models.Model):
    def __str__(self):
        return self.reader_name
    reader_name=models.CharField(max_length=200)
    reader_password=models.CharField(max_length=200, blank=True)
    active = models.BooleanField(default=True)

class Borrowed_history(models.Model):
    history=CharField(max_length=400, blank=True)

class Book(models.Model):
    book_title = models.CharField(max_length=300)
    book_isbn = models.CharField(max_length=200)
    book_borrower_name = models.CharField(max_length=200, blank=True)
    book_stock_number=models.IntegerField(default=1)
    active = models.BooleanField(default=True)

class Textbook(models.Model):
    def __str__(self):
        return self.textbook_title
    textbook_isbn = models.CharField(max_length=200)
    textbook_title = models.CharField(max_length=300)
    textbook_purchased_number = models.IntegerField(default=0)
    textbook_current_number = models.IntegerField(default=0)
    textbook_sold_number = models.IntegerField(default=0)
    textbook_lost_number = models.IntegerField(default=0)
    active = models.BooleanField(default=True)