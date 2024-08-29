import requests
from django.conf import settings
from django.http import JsonResponse

def chatgpt(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input')
        response = get_chatgpt_response(user_input)
        return JsonResponse(response)
    # return render(request, 'chatgpt.html')

def get_chatgpt_response(user_input):
    api_key = settings.OPENAI_API_KEY
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ],
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    return response.json()
