from django.shortcuts import render
from django.http import JsonResponse
from .models import Member

def index(request):
    return render(request, 'index.html')

def save_score(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        score = request.POST.get('score')
        member = Member(name=name, score=score)
        member.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

def top_scores(request):
    top_players = Member.objects.order_by('-score')[:10]
    top_scores_list = [{'name': player.name, 'score': player.score} for player in top_players]
    return JsonResponse(top_scores_list, safe=False)


