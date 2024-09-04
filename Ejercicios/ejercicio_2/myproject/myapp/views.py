import requests
from django.http import JsonResponse

def fetch_data(request):
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        formatted_data = [{'id': item['id'], 'title': item['title']} for item in data]
        return JsonResponse({'data': formatted_data})
    else:
        return JsonResponse({'error': 'Unable to fetch data from external API'}, status=500)
