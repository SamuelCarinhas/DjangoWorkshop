from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(req):
    context = {
        'message': 'This is a message from python'
    }
    return render(req, 'home_page.html', context)
