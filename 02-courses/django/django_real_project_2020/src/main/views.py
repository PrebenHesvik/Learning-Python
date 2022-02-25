from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


def home(request):
    template = 'home-02.html'
    context = {}

    return render(request, template, context)
