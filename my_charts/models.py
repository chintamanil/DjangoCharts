# from audioop import reverse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

from django import forms

# Create your models here.

class Country(models.Model):
    my_country = models.CharField(max_length=20)

    # def __unicode__(self):
    #      return u"Profile for user {0}".format(self.my_country)


class ZipCode(models.Model):
    zip = models.IntegerField(max_length=6)

    # def __unicode__(self):
    #      return u"Profile for user {0}".format(self.zip)


class HealthParameters(models.Model):
    bp_systolic = models.IntegerField(max_length=3, null=True, help_text="Can be blank: Ideal=120")
    bp_diastolic = models.IntegerField(max_length=3, null=True, help_text="Can be blank: Ideal=120")
    weight = models.DecimalField(max_digits=5, decimal_places=2, null='True', help_text='Can Be Bank: Units lbs')
    height = models.DecimalField(max_digits=5, decimal_places=2, null='True', help_text='Can Be Bank: Units cms')
    health_date = models.DateField(null=True, help_text='Date Created')

    # def __unicode__(self):
    #      return u"Profile for user {0}".format(self.id)


class FitnessParameters(models.Model):
    min_light_activity = models.IntegerField(max_length=4, null=True, help_text='Can be bank: User generic Activity')
    min_sedentary_activity = models.IntegerField(max_length=4, null=True,
                                                 help_text='Can be bank: User sitting Activity')
    min_sleep_activity = models.IntegerField(max_length=4, null=True, help_text='Can be bank: User sitting Activity')
    min_awake = models.IntegerField(max_length=4, null=True, help_text='Can be bank: User Awake Activity')
    min_very_awake = models.IntegerField(max_length=4, null=True, help_text='Can be bank: User Awake Activity')
    fitness_date = models.DateField(null=True, help_text='Date Created')
    steps = models.IntegerField(null=True, max_length=5, help_text='Steps taken')
    distance = models.DecimalField(max_digits=5, decimal_places=2, null='True',
                                   help_text='Distance travelled : Units miles')
    activity_score = models.IntegerField(max_length=5, null=True, help_text='Calculated score')
    # def __unicode__(self):
    #     return u"Profile for user {0}".format(self.id)


class NutritionParameters(models.Model):
    calories_in = models.IntegerField(max_length=5, null=True, help_text='Calories consumed')
    calories_burnt = models.IntegerField(max_length=5, null=True, help_text='Calories burnt')
    calories_planned_in = models.IntegerField(max_length=5, null=True, help_text='Calories planned for intake')
    calories_planned_out = models.IntegerField(max_length=5, null=True, help_text='Calories planned for burning')
    nutrition_date = models.DateField(null=True, help_text='Date Created')
    # def __unicode__(self):
    #     return u"Profile for user {0}".format(self.id)


class Picture(models.Model):
    img = models.ImageField(upload_to='user_images',
                              blank=True,
                              null=True)
    description = models.CharField(null=True, max_length=150)

class Player(AbstractUser):
    name = models.CharField(max_length=20)
    image = models.ForeignKey(Picture, related_name='image', null=True)
    street_address = models.TextField(max_length=150, null=True, help_text="Can be Blank")
    zipcode = models.ForeignKey(ZipCode, related_name='zipcode', null=True, help_text="Can be Blank")
    country = models.ForeignKey(Country, related_name='country', null=True, help_text="Can be Blank")
    health_param = models.ForeignKey(HealthParameters, related_name='health_param', null=True)
    fitness_param = models.ForeignKey(FitnessParameters, related_name='fitness_param', null=True)
    nutrition_param = models.ForeignKey(NutritionParameters, related_name='nutrition_param', null=True)
    GENDER_MALE = '1'
    GENDER_FEMALE = '2'
    GENDER = ( (GENDER_MALE, _('Male')), (GENDER_FEMALE, _('Female')), )
    age = models.IntegerField(max_length=2, verbose_name=_('Age'), blank=False, null=True, validators=[MinValueValidator(10), MaxValueValidator(100)])
    gender = models.CharField(max_length=1, choices=GENDER, default=GENDER_MALE, blank=False, null=True)
    # def __unicode__(self):
    #     return u"Profile for user {0}".format(self.id)


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # phone_number = forms.DecimalField(max_digits=9)

    class Meta:
        model = Player
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Player.objects.get(username=username)
        except Player.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


# class MyForm(forms.Form):
# def as_p(self):
# "Returns this form rendered as HTML <p>s."
# return self._html_output(
#             normal_row = u"<p%(html_class_attr)s>%(label)s</p> %(field)s%('Username')s",
#             error_row = u'%s',
#             row_ender = '</p>',
#             help_text_html = u' <span class="helptext">%s</span>',
#             errors_on_separate_row = True)
#
# class MonthlyWeatherByCity(models.Model):
#     month = models.IntegerField()
#     boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
#     houston_temp = models.DecimalField(max_digits=5, decimal_places=1)

from django import forms
from django.forms.widgets import *
# from django.core.mail import send_mail, BadHeaderError

# A simple contact form with four fields.
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    topic = forms.CharField()
    message = forms.CharField(widget=Textarea())