
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def sumar(request, operando1, suma, operando2):
    resultado= int(operando1) + int(operando2)
    return HttpResponse(str(operando1)+ ' + ' + str(operando2)+' = '+ str(resultado))

def restar(request, operando1, resta, operando2):
    resultado= int(operando1) - int(operando2)
    return HttpResponse(str(operando1)+ ' - ' + str(operando2)+' = '+ str(resultado))

def multiplicar(request,operando1, mult, operando2):
    resultado= int(operando1) * int(operando2)
    return HttpResponse(str(operando1)+ ' * ' + str(operando2)+' = '+ str(resultado))

def division(request, operando1, div, operando2):
    try:
        resultado= float(operando1) / float(operando2)
        return HttpResponse(str(operando1)+ ' / ' + str(operando2)+' = '+ str(resultado))
    except ZeroDivisionError:
        return HttpResponse(' Indeterminacion: no se puede dividir entre 0')
def Error404(request):
    return HttpResponse("Error : Not Found")
