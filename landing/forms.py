from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        subject = self.cleaned_data['subject']
        email = self.cleaned_data['email']
        text = self.cleaned_data['text']
        text = name+"\n"+text
        print(settings.EMAIL_HOST)
        send_mail(subject=subject, message=text, from_email=email, recipient_list = [settings.EMAIL_HOST,])
