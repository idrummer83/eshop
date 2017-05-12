from django import forms
from django.contrib.auth.models import User

from blog.models import Post


class PostForm(forms.ModelForm):
    user = forms.ModelChoiceField(label='avtor', queryset=User.objects.all())
    class Meta:
        model = Post
        fields = ('name', 'text',)
