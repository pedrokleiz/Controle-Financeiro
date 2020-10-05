from django.shortcuts import render


def pagina_entradas(request):
    return render(request, 'entrada.html')
