from django.shortcuts import render

def index(request):
    return render(request, 'snake_project/index.html')




