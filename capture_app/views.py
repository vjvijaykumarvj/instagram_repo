import json
import urllib
import urllib3
from django.shortcuts import render, redirect
from .forms import Contact_Form

import requests

def contact(request):
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            data = {
                'secret': '6LcaxHwiAAAAAKrqTPN8rJJWH_HKQtk55JWs1Tr6',
                'response': recaptcha_response
            }
            # r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            # result = r.json()
            data = urllib.parse.urlencode(data).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            if result['success']:
                form.save()
                return redirect('/success/')
            else:
                return redirect('/contactt/')
    else:
        form = Contact_Form()
    return render(request, 'capture_app/contactt.html', {'form': form})


def success(request):
    return render(request,'capture_app/success.html')
