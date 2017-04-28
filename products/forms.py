from django import forms
from django.core.exceptions import ValidationError


def name_validator(name):
    if not name.startswith('Mr.'):
        raise ValidationError('Only for men')
    return name


class FeedbackForm(forms.Form):
    feedback = forms.CharField(label='Отзыв', help_text='aaaa', widget=forms.Textarea())
    nick = forms.CharField(label='Имя', validators=(name_validator,))

    def clean_feedback(self):
        if 'windows' in self.cleaned_data['feedback'].lower():
            raise ValidationError('Windows is in form')
        return self.cleaned_data['feedback']

