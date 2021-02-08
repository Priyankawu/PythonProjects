from django.db import models


# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    deposit = models.DecimalField(max_digits=15, decimal_places=2)

    # object through which django objects perform database queries
    Accounts = models.Manager()


    # Allows references to a specific account be returned as
    # the owner's name not the primary key
    def __str__(self):
        return self.first_name + ' '+self.last_name
# ____________________________________________________________________________ #

TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal','Withdrawal')]


class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length = 15, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=188)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()


