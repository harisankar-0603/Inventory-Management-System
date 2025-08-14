from django.db import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_crispy_helper(self):
        helper = FormHelper()
        helper.add_input(Submit('submit', 'Submit'))
        return helper