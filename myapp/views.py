from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'page1.html')

@login_required
def admin_only(request):
    return render(request, 'page2.html')
