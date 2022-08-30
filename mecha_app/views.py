import email
from unicodedata import name
from django.shortcuts import render

# Create your views here.
from .models import userForm

def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'service.html')
def team(request):
    return render(request, 'team.html')
def homepage(request):
    return render(request, 'index.html')
def contact(request):
    if request.method == 'POST':
        user_name = request.POST['name']
        user_subject = request.POST['subject']
        user_email = request.POST['email']
        user_select = request.POST.get('user_select', False)
        user_message = request.POST['message']
        
        
        user_input = userForm(name= user_name, subject =user_subject, email =user_email , select =user_select ,message= user_message)
        user_input.save()
        
        
    return render(request, 'contact.html')
