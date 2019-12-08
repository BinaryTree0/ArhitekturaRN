from .models import Post,Images,CATEGORY_CHOICES
from django import forms

class PostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    category = forms.ChoiceField(choices = CATEGORY_CHOICES, label="", initial='', widget=forms.Select(), required=True)
    class Meta:
        model = Post
        fields = ['name','description','date','category']
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['date'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['description'].widget.attrs['placeholder'] = 'Ovdje ide tekst....'

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = Images
        fields = ('image', )

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form-control-file'
        self.fields['image'].widget.attrs['multiple'] = True
