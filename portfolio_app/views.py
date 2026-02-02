from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Contact
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages

def ContactView(request):
    
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']

            email = form.cleaned_data['email']

            message = form.cleaned_data['message']

            Contact.objects.create(
                name = name,
                email = email,
                message = message
            )

            send_mail(
                subject = f"New message from {name}",
                message = f"Sender : {name}\nEmail : {email}\nMessage : \n{message}",
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = ['ssk2k05@gmail.com'],
                fail_silently = False,
            )

        messages.success(request, "Message sent successfully!")

        return redirect("/#message")
        
    else:

        context = {
            "form" : ContactForm
        }

    return render(request, "index.html", context)
