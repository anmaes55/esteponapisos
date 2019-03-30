#from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .forms import ContactForm



def index(request):
    return render(request, 'landing/index.html')


def callesestepona(request):
    return render(request, 'landing/callesestepona.html')


def orquidarioestepona(request):
    return render(request, 'landing/orquidarioestepona.html')


def catalogo_4A(request):
    return render(request, 'landing/catalogo_4A.html')


def catalogo_4B(request):
    return render(request, 'landing/catalogo_4B.html')


def catalogo_4C(request):
    return render(request, 'landing/catalogo_4C.html')


def catalogo_4D(request):
    return render(request, 'landing/catalogo_4D.html')


def contactar(request):
    template = loader.get_template('landing/index.html')

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            subject = form.cleaned_data['asunto']
            from_email = form.cleaned_data['from_email']
            mensaje = 'Mensaje de: ' + nombre + '\nEmail: ' + from_email + '\n\n' + form.cleaned_data['mensaje']
            try:
                send_mail(subject, mensaje, 'contacto@anaruizromero.es', ['juan@quitiweb.com', 'anamail12@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            form = ContactForm()
            return redirect('mensaje-enviado')
        else:
            print('Error en el formulario')

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def carrusel(request):
    return render(request, 'landing/carrusel.html')

