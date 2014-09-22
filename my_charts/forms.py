from django.forms import ModelForm
from models import *
from django import forms


# class MovieForm(ModelForm):
#     class Meta:
#         model = Movie


from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class PictureForm(forms.Form):
    picture = forms.forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

    # img = forms.ModelChoiceField(queryset=Picture.objects.all())