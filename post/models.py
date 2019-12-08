from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
CATEGORY_CHOICES = (
    (1, ("Kuca")),
    (2, ("Zgrada")),
    (3, ("Hotel")),
    (4, ("Restoran")),
)

class Post(models.Model):
    name = models.CharField(max_length=100, unique = True)
    description = models.CharField(max_length=4000)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['name','date','description','category']
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'pk': self.pk})

class Images(models.Model):
    post = models.ForeignKey(Post, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/",verbose_name='Image')
