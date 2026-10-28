from django.shortcuts import render
from django.http import HttpResponse
from .forms import PaymentCreateForm
from .models import Payment
from orders.models import Order

# Create your views here.
def dashboard(request):
    order = Order(request)
    if request.method =='POST':
        form = PaymentCreateForm(request.POST)
        PaymentCreateForm.amount = order.get_total_cost
        if form.is_valid():
            PaymentCreateForm = form.save(commit=False)
            PaymentCreateForm.status = 'pending'
            PaymentCreateForm.save()
    else:
        form = PaymentCreateForm()
    payments = Payment.objects.all().order_by('-created_at')
    context ={
        'form':form,
        'payments':payments,
        'Total_payments':payments.count(),
        'successful_payments':payments.filter(status='succesful').count(),
        'pending_payments':payments.filter(status='pending').count(),
        'failed_payments':payments.filter(status='failed').count()
    }

    return render(request,'payments/dashboard.html',context)
