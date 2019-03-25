from django.shortcuts import render


def index(request):
    return render(request, 'landing/index.html')


def callesestepona(request):
    return render(request, 'landing/callesestepona.html')


def orquidarioestepona(request):
    return render(request, 'landing/orquidarioestepona.html')


def catalogo_4B(request):
    return render(request, 'landing/catalogo_4B.html')


