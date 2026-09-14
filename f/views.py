from django.http import HttpResponse,JsonResponse

def http_test(request):
    return HttpResponse(t'http_test')

def json_test(request):
    return JsonResponse({'name':'mohammad'})