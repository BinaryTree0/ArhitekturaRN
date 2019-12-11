from django.shortcuts import render
from django.views import generic
from .forms import PostForm,ImageForm
from .models import Post,Images,CATEGORY_CHOICES
from django.conf import settings
from django.urls import reverse_lazy
from django.http import HttpResponse

class PostView(generic.ListView):
    template_name = "post/post.html"
    model = Post
    def get_queryset(self):
        queryset = []
        posts = Post.objects.all()
        for post in posts:
            post.image = Images.objects.filter(post = post).first().image
            queryset.append(post)
        return queryset

class PostDetailView(generic.DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        object = super().get_context_data(**kwargs)
        object['object'].category = CATEGORY_CHOICES[object['object'].category-1][1]
        object['object'].images = []
        for image in Images.objects.filter(post = object["object"]).all():
            object['object'].images.append(image.image)
        return object

class PostCreateView(generic.edit.CreateView):
    template_name = "post/post_form.html"
    form_class = PostForm

    def get_context_data(self, **kwargs):
        object = super().get_context_data(**kwargs)
        object["image_form"] = ImageForm(None)
        return object

    def post(self, request, *args, **kwargs):
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save()
            for image in request.FILES.getlist('image'):
                instance = Images(post=post, image=image)
                instance.save()
        return super(PostCreateView, self).form_valid(post_form)


class PostUpdateView(generic.edit.UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        object = super().get_context_data(**kwargs)
        object["image_form"] = ImageForm(None)
        return object

    def post(self, request, *args, **kwargs):
        image_form = ImageForm(request.POST, request.FILES)
        post = Post.objects.get(pk = self.kwargs['pk'])
        if image_form.is_valid():
            for image in Images.objects.filter(post = post).all():
                image.delete()

            for image in request.FILES.getlist('image'):
                instance = Images(post=post, image=image)
                instance.save()
        return super(PostUpdateView, self).post(self, request, *args, **kwargs)

class PostDeleteView(generic.edit.DeleteView):
    model = Post
    success_url = reverse_lazy('post:template')
