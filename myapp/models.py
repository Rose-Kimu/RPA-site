from django.db import models
class Report(models.Model):
    expense_id = models.IntegerField()
    employee_name = models.CharField(max_length=200)
    expense_category = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    # currency = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    receipt = models.BooleanField()

    def __str__(self):
        return f"{self.expense_id} - {self.employee_name}"


    
