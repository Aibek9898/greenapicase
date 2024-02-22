from django.shortcuts import render
import requests


def home(request):
    return render(request, 'greenapi/home.html')


def get_data(request):
    idInstance = request.GET.get('idInstance')
    apiTokenInstance = request.GET.get('apiTokenInstance')
    action = request.GET.get('action')

    if action == "GetSettings":
        url = f'https://api.green-api.com/waInstance{idInstance}/getSettings/{apiTokenInstance}'
    elif action == "GetStateInstance":
        url = f'https://api.green-api.com/waInstance{idInstance}/getStateInstance/{apiTokenInstance}'

    payload = {}
    headers = {}

    response = requests.request('GET', url, headers=headers, data=payload)
    data = response.text.encode('utf8')
    return render(request, 'greenapi/home.html', {'data': data})


def send_message(request):
    idInstance = request.GET.get('idInstance')
    apiTokenInstance = request.GET.get('apiTokenInstance')
    number = request.GET.get('number')
    domain = request.GET.get('domain', '@c.us')
    message = request.GET.get('message')

    url = f"https://api.green-api.com/waInstance{idInstance}/sendMessage/{apiTokenInstance}"

    payload = '''{{
        "chatId": "{}",
        "message": "{}"
    }}'''.format(number+domain, message)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.text.encode('utf8')

    return render(request, 'greenapi/home.html', {'data': data})

def send_file(request):
    idInstance = request.GET.get('idInstance')
    apiTokenInstance = request.GET.get('apiTokenInstance')
    number = request.GET.get('number_file')
    domain = request.GET.get('domain_file', '@c.us')
    file = request.GET.get('path_file')

    url = f"https://api.green-api.com/waInstance{idInstance}/sendFileByUrl/{apiTokenInstance}"

    payload = '''{{
            "chatId": "{}",
            "urlFile": "{}",
            "fileName": "any",
            "caption": "any"
            
        }}'''.format(number + domain, file)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    data = response.text.encode('utf8')

    return render(request, 'greenapi/home.html', {'data': data})

