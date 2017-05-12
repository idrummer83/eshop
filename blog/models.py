from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls.base import reverse


class Post(models.Model):
    user = models.ForeignKey(User, verbose_name='Avtor')
    name = models.CharField('Title', max_length=200)
    date = models.DateField('Data', auto_now_add=True)
    text = models.TextField('Post')
    slug = models.SlugField(unique_for_date='date', max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={
            'date': self.date,
            'slug': self.slug
        })
