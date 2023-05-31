from django import forms
from django.conf import settings
from django.core.mail import send_mail
from .models import *

# class ContactForm(forms.Form):

#     name = forms.CharField(max_length=120)
#     email = forms.EmailField()
#     inquiry = forms.CharField(max_length=70)
#     message = forms.CharField(widget=forms.Textarea)

#     def get_info(self):
#         """
#         Method that returns formatted information
#         :return: subject, msg
#         """
#         # Cleaned data
#         cl_data = super().clean()

#         name = cl_data.get('name').strip()
#         from_email = cl_data.get('email')
#         subject = cl_data.get('inquiry')

#         msg = f'{name} with email {from_email} said:'
#         msg += f'\n"{subject}"\n\n'
#         msg += cl_data.get('message')

#         return subject, msg

#     def send(self):

#         subject, msg = self.get_info()

#         send_mail(
#             subject=subject,
#             message=msg,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[settings.RECIPIENT_ADDRESS]
#         )



class ContactForm(forms.ModelForm):
	class Meta:
		model = ContactProfile
		fields = [
			'name',
			'email',
			'message',
			'subject',
		]
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'style':
				"padding: 10px; \
				margin-bottom: 20px; \
				border-bottom: 1px solid grey; \
				outline: none; \
				font-size: 18px; \
				background-color: #a7c9de;"}),

   
			'email': forms.TextInput(attrs={'class': 'form-control', 'style':
				"padding: 10px; \
				margin-bottom: 20px; \
				border-bottom: 1px solid grey; \
				outline: none; \
				font-size: 18px; \
				background-color: #a7c9de;"}),
   
			'message': forms.Textarea(attrs={'class': 'form-control', 'style':
				"padding: 10px; \
				margin-bottom: 20px; \
				border-bottom: 1px solid grey; \
				outline: none; \
				font-size: 18px; \
				background-color: #a7c9de;"}),
   
			'subject': forms.TextInput(attrs={'class': 'form-control', 'style':
				"padding: 10px; \
				margin-bottom: 20px; \
				border-bottom: 1px solid grey; \
				outline: none; \
				font-size: 18px; \
				background-color: #a7c9de;"}),
		}