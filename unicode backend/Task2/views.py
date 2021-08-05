from django.shortcuts import render
from  django.http import HttpResponse
import requests
import json
def index(request):
    response = requests.get('https://pokeapi.co/docs/v2#types')
    return HttpResponse(response)
