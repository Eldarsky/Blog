import datetime

from django.shortcuts import HttpResponse


# Create your views here.
def main(request):
    return  HttpResponse('Hello! Its my project')

def data(request):
    return HttpResponse(f"Дата: {datetime.now().date()}")


def goodby(request):
    return HttpResponse('Goodby user!')

