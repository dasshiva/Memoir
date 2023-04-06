from django.db import models

# Create your models here.

class Formula(models.Model):
  formula = models.CharField(max_length=200)
  def __str__(self):
    return self.formula + "\n"
  def html(self): 
    return self.formula + "<br>"
  
class Subject(models.Model):
  name = models.CharField(max_length=200)
  priority = models.IntegerField(default=0)
  formulae = models.ManyToManyField(Formula)
  
  def print(self):
    for i in self.formulae.iterator():
      print(i)
  
