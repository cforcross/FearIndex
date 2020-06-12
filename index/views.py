from django.shortcuts import render
import requests
import json
# Create your views here.
def home(request):
    api_request = requests.get(' https://api.alternative.me/fng/?limit=10')
    api = json.loads(api_request.content)

    context ={
        "api":api,
    }
    return render(request,'index.html',context=context)