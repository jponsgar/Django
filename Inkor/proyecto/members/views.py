from django.shortcuts import render
from django.http import HttpResponse

def members(request):
  
  # html = """
  # <h1>Hola, mundo</h1>
  # <p>Esto es un HTML</p>
  # """
  # return HttpResponse(html) # admite texto o HTML: "<h1>Hello world!</h1>"
  
  # Devolvemos HTML por archivo:
  return render(request, "index.html")
