from django.shortcuts import render
# from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from . forms import *
from . models import *
from django.views import generic
from django.contrib import messages

# Create your views here.
    
# class ContactSuccessView(generic.TemplateView):
#     template_name = 'contact/success.html'
    
# Contact
class ContactView(generic.FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/contact/"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.'); messages.get_messages(self.request).used = True
        email = self.request.POST.get('email')
        # Now you can use the 'email' variable as needed
        # For example, you can store it in a session variable or a class attribute
        self.email = email
        send_mail(
            subject="Response from TalentServe",
            message="We recieved your message, you'll be contacted soon by our team.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        return super().form_valid(form)
    
    