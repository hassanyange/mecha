from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'service.html')
def team(request):
    return render(request, 'team.html')
def homepage(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
