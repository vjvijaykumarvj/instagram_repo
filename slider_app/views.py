from django.shortcuts import render,redirect
from.models import Washing_Payment
from.forms import Washing_payment_Forms

def Washning_Machine(request):
    return render(request,'slider_app/washing_machine.html')

def washing_payment(request):
    if request.method == 'GET':
        w_payment = Washing_payment_Forms()
        dict = {
            'washing_pay' : w_payment
        }
        return render(request,'slider_app/washing_payment.html',context=dict)
    elif request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        amount = request.POST.get('amount')

        pay = Washing_Payment(name=name,address=address,pincode=pincode,amount=amount)
        pay.save()
        return redirect('/payment_success/')
def payment_success(request):
    return render(request,'slider_app/wash_payment_success.html')