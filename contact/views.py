from django.shortcuts import render, redirect
from .forms import contactForm
from django.contrib import messages

# Create your views here.

app_name = 'contact'

def contact(request):
    template = 'contact/contact.html'
    context = {}
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'wiadomosc wyslana masno fest')
            return redirect('/contact/')
    else:
        form = contactForm()
    context = {'form': form}
    #print(f'{form}')
    return render(request, template, context)
