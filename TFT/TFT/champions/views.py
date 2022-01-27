from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    html = '''
    <h1> It works <h1>
    '''
    return HttpResponse('Here will be displayed all of the champions in the game')
