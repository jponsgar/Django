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


def members_detail(request, id):
  
  # debug:
  print("Se ha pedido el id:", id)
  
  # Sacamos de la lista de members el del id que me piden:
  member = Member.objects.all().filter(id=id).first() # deberíamos tener solo un resultado
  
  # debug:
  print(member)
  
  context = {
    "member": member,
  }
  return render(request, "members/detail.html", context=context)