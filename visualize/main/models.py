from django.db import models

# Create your models here.

class data(models.Model):
    """
    Represents a data entry.

    Attributes:
        date (str): The date of the data entry.
        trade_code (str): The trade code of the data entry.
        high (str): The high value of the data entry.
        low (str): The low value of the data entry.
        open (str): The open value of the data entry.
        close (str): The close value of the data entry.
        volume (str): The volume of the data entry.
    """

    date = models.CharField(max_length=100)
    trade_code = models.CharField(max_length=100)
    high = models.CharField(max_length=100)
    low = models.CharField(max_length=100)
    open = models.CharField(max_length=100)
    close = models.CharField(max_length=100)
    volume = models.CharField(max_length=100)

    def __str__(self):
        return self.trade_code