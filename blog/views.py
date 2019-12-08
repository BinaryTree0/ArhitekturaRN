from django.shortcuts import render
from django.views import generic
from .models import Blog, Comment
from .forms import CommentForm, BlogForm
from django.urls import reverse
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpRequest

# Create your views here.

class BlogView(generic.ListView):
    template_name = "blog/blog.html"
    model = Blog

class BlogDetailView(generic.DetailView):
    model = Blog
    form_class = CommentForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(blog = context["object"]).all()
        main_comments = []
        replies = []
        for comment in comments:
            if comment.parent == None:
                main_comments.append(comment)
            else:
                replies.append(comment)

        for comment in main_comments:
            comment.replies = []
            for reply in replies:
                if comment == reply.parent:
                    comment.replies.append(reply)

        context["comments"] = main_comments
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        view = CommentFormView.as_view()
        return view(request, *args, **kwargs)

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


class CommentFormView(generic.FormView):
    template_name = 'blog/comment_form_error.html'
    form_class = CommentForm
    model = Blog
    def form_valid(self, form):
        parent_id = form.cleaned_data['hidden']
        if parent_id:
            parent_post = Comment.objects.get(id = parent_id)
        else:
            parent_post = None
        blog_id = self.kwargs["pk"]
        blog = Blog.objects.get(id = blog_id)
        object = form.save(commit=False)
        object.parent = parent_post
        object.blog = blog
        object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.kwargs["pk"]})

class CommentDeleteView(generic.edit.DeleteView):
    model = Comment
    template_name = "blog/confirm_delete.html"
    success_url = reverse_lazy('blog:detail')

    def get_success_url(self):
        comment = Comment.objects.get(id = self.kwargs["pk"])
        return reverse('blog:detail', kwargs={'pk': comment.blog.id})
