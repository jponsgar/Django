from django.shortcuts import render
from django.http import HttpResponse

from members.models import Member

def index(request):
  # Devolvemos el HTML de templates/index.html:
  return render(request, "index.html")

def members(request):
  lista_de_members = Member.objects.all()
  context = {
    "members": list(lista_de_members)
  }
  # Devolvemos el HTML de templates/members/index.html:
  return render(request, "members/index.html", context=context)
