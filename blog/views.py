from django.shortcuts import render
from django.views import generic
from .models import Blog
from .forms import BlogForm
from django.urls import reverse_lazy
# Create your views here.

class BlogView(generic.ListView):
    template_name = "blog/blog.html"
    model = Blog

class BlogDetailView(generic.DetailView):
    model = Blog
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BlogCreateView(generic.edit.CreateView):
    template_name = "blog/blog_form.html"
    form_class = BlogForm

class BlogUpdateView(generic.edit.UpdateView):
    form_class = BlogForm
    model = Blog
    template_name = 'blog/blog_form.html'

class BlogDeleteView(generic.edit.DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:template')
    template_name = "blog/confirm_delete.html"
