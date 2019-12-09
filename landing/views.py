from django.shortcuts import render
from django.views import generic
from .forms import ContactForm
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "landing/index.html"

class AboutView(generic.TemplateView):
    template_name = "landing/about.html"
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

class ContactView(generic.edit.FormView):
    template_name = "landing/contact.html"
    form_class = ContactForm

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
