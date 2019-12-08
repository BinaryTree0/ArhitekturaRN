from django.shortcuts import render
from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "landing/index.html"

class AboutView(generic.TemplateView):
    template_name = "landing/about.html"

class ContactView(generic.TemplateView):
    template_name = "landing/contact.html"
