from django.shortcuts import render
# from django.http import HttpResponse

def test(request):
    context = {'name': request.GET['name']}
    return render(request, 'mysite/test.html', context)
# request.GET['name']
def form(request):
    return render(request, 'mysite/form.html')