# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    context['mess'] = 'Hello index'
    return render(request, 'index.html', context)

def hello(request):
    context = {}
    context['mess'] = 'Hello'
    return render(request, 'hello.html', context)