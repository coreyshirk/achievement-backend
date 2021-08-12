from django.http import HttpResponse


def healthcheck(request):
    return HttpResponse('Api health check success')