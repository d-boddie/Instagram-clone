from django.shortcuts import render
from django.http import HttpResponse


def error_500(request):
    data = {}
    if not data.get('hello'):
        return HttpResponse(status=500)

    return render(request, '500.html', data)
