from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def member1(request):
    template=loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def sample():
    pass
# Create your views here.
