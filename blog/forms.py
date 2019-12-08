from .models import Comment,Blog
from django import forms
class CommentForm(forms.ModelForm):
    hidden = forms.CharField(required = False,widget=forms.HiddenInput(attrs={'id': "comment-reply"}))
    class Meta:
        model = Comment
        fields = ['name','email','text','hidden', ]
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['text'].widget.attrs['placeholder'] = 'Comment'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'example@example.com'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name','date','text','image' ]
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['date'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['text'].widget.attrs['placeholder'] = 'Ovdje ide tekst....'
        self.fields['image'].widget.attrs['class'] = 'form-control-file'
