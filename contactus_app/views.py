from django.shortcuts import render, redirect
from.models import ContactUS,Blog_model
from.forms import ContactForm,BlogForm

def Contactus(request):
    if request.method == 'GET':
        contact_form = ContactForm()
        dict = {
            'contact_form' : contact_form
        }
        return render(request,'contactus_app/contactus.html',context=dict)

    elif request.method == 'POST':
        contactform = ContactForm(request.POST)
        if contactform.is_valid():
            contactform.save()
        return redirect('/contactus_success/')

def contactus_success(request):
    return render(request,'contactus_app/contact_success.html')

def aboutus(request):
    return render(request,'contactus_app/aboutus.html')


def Blog(request):
    if request.method == 'GET':
        blog = BlogForm()
        dict = {
            'blog' : blog
        }
        return render(request,'contactus_app/blog.html',context=dict)
    elif request.method == 'POST':
        blog = BlogForm(request.POST)
        if blog.is_valid():
            blog.save()
        return redirect('/home/')
