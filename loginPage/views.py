from django.shortcuts import render, redirect
# from loginPage import form
from django.http import HttpResponsePermanentRedirect 
from django.contrib import messages
# Create your views here.
# def googleLogin(request):
#     # return response
#     return HttpResponse("anything")
def signup_redirect(request):
    messages.error(request, 'Something wrong here it may be that you already have account')
    return redirect('index.html')
def login_redirect(request):
    
    return redirect('')
def form(request):

    return render(request, 'form.html')    
    
