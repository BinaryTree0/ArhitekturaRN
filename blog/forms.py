from .models import Blog
from django import forms

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
