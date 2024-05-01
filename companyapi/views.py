from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("homepage requested")
    friends=[
        'sumitra',
        'partima',
        'jidan'
    ]
    return JsonResponse(friends, safe=False)