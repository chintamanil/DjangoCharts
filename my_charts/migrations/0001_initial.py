# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=20)),
                ('street_address', models.TextField(help_text=b'Can be Blank', max_length=150, null=True)),
                ('age', models.IntegerField(max_length=2, null=True, verbose_name='Age', validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(100)])),
                ('gender', models.CharField(default=b'1', max_length=1, null=True, choices=[(b'1', 'Male'), (b'2', 'Female')])),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('my_country', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FitnessParameters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min_light_activity', models.IntegerField(help_text=b'Can be bank: User generic Activity', max_length=4, null=True)),
                ('min_sedentary_activity', models.IntegerField(help_text=b'Can be bank: User sitting Activity', max_length=4, null=True)),
                ('min_sleep_activity', models.IntegerField(help_text=b'Can be bank: User sitting Activity', max_length=4, null=True)),
                ('min_awake', models.IntegerField(help_text=b'Can be bank: User Awake Activity', max_length=4, null=True)),
                ('min_very_awake', models.IntegerField(help_text=b'Can be bank: User Awake Activity', max_length=4, null=True)),
                ('fitness_date', models.DateField(help_text=b'Date Created', null=True)),
                ('steps', models.IntegerField(help_text=b'Steps taken', max_length=5, null=True)),
                ('distance', models.DecimalField(help_text=b'Distance travelled : Units miles', null=b'True', max_digits=5, decimal_places=2)),
                ('activity_score', models.IntegerField(help_text=b'Calculated score', max_length=5, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HealthParameters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bp_systolic', models.IntegerField(help_text=b'Can be blank: Ideal=120', max_length=3, null=True)),
                ('bp_diastolic', models.IntegerField(help_text=b'Can be blank: Ideal=120', max_length=3, null=True)),
                ('weight', models.IntegerField(help_text=b'Can be bank: Units lb', max_length=3, null=True)),
                ('height', models.DecimalField(help_text=b'Can Be Bank: Units cms', null=b'True', max_digits=5, decimal_places=2)),
                ('health_date', models.DateField(help_text=b'Date Created', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NutritionParameters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calories_in', models.IntegerField(help_text=b'Calories consumed', max_length=5, null=True)),
                ('calories_burnt', models.IntegerField(help_text=b'Calories burnt', max_length=5, null=True)),
                ('calories_planned_in', models.IntegerField(help_text=b'Calories planned for intake', max_length=5, null=True)),
                ('calories_planned_out', models.IntegerField(help_text=b'Calories planned for burning', max_length=5, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(null=True, upload_to=b'travel_images', blank=True)),
                ('description', models.CharField(max_length=150, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip', models.IntegerField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='country',
            field=models.ForeignKey(related_name=b'country', to='my_charts.Country', help_text=b'Can be Blank', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='fitness_param',
            field=models.ForeignKey(related_name=b'fitness_param', to='my_charts.FitnessParameters', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='health_param',
            field=models.ForeignKey(related_name=b'health_param', to='my_charts.HealthParameters', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='image',
            field=models.ForeignKey(related_name=b'image', to='my_charts.Picture', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='nutrition_param',
            field=models.ForeignKey(related_name=b'nutrition_param', to='my_charts.NutritionParameters', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='zipcode',
            field=models.ForeignKey(related_name=b'zipcode', to='my_charts.ZipCode', help_text=b'Can be Blank', null=True),
            preserve_default=True,
        ),
    ]
