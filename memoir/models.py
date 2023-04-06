from django.db import models

# Create your models here.

class Formula(models.Model):
  formula = models.CharField(max_length=200)
  
class Subject(models.Model):
  name = models.CharField(max_length=200)
  priority = models.IntegerField(default=0)
  formulae = models.ForeignKey(Formula, on_delete=models.CASCADE)
  
