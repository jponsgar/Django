from django.http import JsonResponse
from .models import User

def user_list(request):
    users = User.objects.all().values('username', 'email', 'first_name', 'last_name')
    users_list = list(users)
    return JsonResponse(users_list, safe=False)


