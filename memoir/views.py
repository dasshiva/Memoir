from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from memoir.models import Subject, Formula

# Create your views here.

def index(request):
  return HttpResponse("Hello World")

def formula(req, subject, formula_id):
  try:
    sub = Subject.objects.filter(name = subject).get()
    formula = sub.formulae.filter(id = formula_id).get()
    return HttpResponse(f"Requested formula is: {formula}")
  except Formula.DoesNotExist:
    raise HttpResponseNotFound("Formula Does not exist")
  except Subject.DoesNotExist:
    raise HttpResponseNotFound(f"Subject {subject} does not exist")
    
def show_all_formulae(req, subject):
   try:
     sub = Subject.objects.filter(name = subject).get()
     formulae = "Available formulae are:<br>"
     for formula in sub.formulae.iterator():
       formulae += formula.html()
     return HttpResponse(formulae)
   except Subject.DoesNotExist:
     return HttpResponseNotFound(f"Subject {subject} does not exist")
 
def handler404(req, excep, template="404.html"):
  return HttpResponseNotFound(excep)
