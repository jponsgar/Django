from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  # Devolvemos el HTML de templates/index.html:
  return render(request, "index.html")

def members(request):
  # Devolvemos el HTML de templates/members/index.html:
  return render(request, "members/index.html")
