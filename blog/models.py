from django.db import models
from django.urls import reverse
from .validators import alpha
# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100, unique = True)
    text = models.CharField(max_length=10000)
    likes = models.IntegerField(default=0)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/",verbose_name='Image')
    REQUIRED_FIELDS = ['name','date','text','image']
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
