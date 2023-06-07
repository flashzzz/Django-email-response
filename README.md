# Django-email-response
An app to automatically reply to a query via email

# Setup
1. Create a venv and install all dependencies listed in requirements.txt in python=3.10 environment
2. Create a .env file in the mail/mail directory where the `settings.py` file is present.
3. Add the following in it -
```
EMAIL_HOST='your email service host'
EMAIL_HOST_USER='your email account that will send email'
EMAIL_HOST_PASSWORD='your email app password'
```
4. Now head to the mail directory where the file `manage.py` is present. 
5. Run the command `python manage.py runserver`.
6. Head to the link `http://localhost:8000/contact/`, you should be able to see the contact form.
7. Just fill it up correctly and an email should be waiting in your inbox.
