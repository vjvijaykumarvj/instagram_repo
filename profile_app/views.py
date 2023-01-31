from django.shortcuts import render

def Profile(request):
    return render(request,'profile_app/profile.html')