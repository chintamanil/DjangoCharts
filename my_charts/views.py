from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
# from django.views.generic import TemplateView
# from chartjs.views.lines import BaseLineChartView
from django.shortcuts import render
from my_charts.forms import ContactForm
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
# from Charts import settings
from forms import *

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def signin(request):
    return render(request, "Signin.html")

def contact(request):
    return render(request, "contact.html")

def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            html_content = '<h2>Thanks {} for signing up!</h2> <div>I hope you enjoy using our site</div>'.format(
                user.username)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("dashboard")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required()
def read(request):
    user = request.user
    print user.id, user.username
    print user.username, user.age, user.gender, user.zipcode.zip, user.country.my_country, user.gender, user.health_param.weight
    return render(request, 'userdata.html', {})

@login_required()
def profile(request):
    return render(request, 'profile.html', {})


@login_required()
def dashboard(request):
    browser_stats = [['Chrome', 52.9], ['Firefox', 27.7], ['Opera', 1.6],
                     ['Internet Explorer', 12.6], ['Safari', 4]]
    # data = HealthParameters.objects.all().select_related('player__id')
    # print len(data), "this is length of data"
    #
    # for each in data:
    #     print each.bp_systolic,'This is the users blood pressure'

    return render(request, 'Dashboard.html', locals())

def hsummary(request):
    browser_stats = [['Chrome', 52.9], ['Firefox', 27.7], ['Opera', 1.6],
                     ['Internet Explorer', 12.6], ['Safari', 4]]
    return render(request, 'Health_Summary.html', locals())

def fsummary(request):
    browser_stats = [['Chrome', 52.9], ['Firefox', 27.7], ['Opera', 1.6],
                     ['Internet Explorer', 12.6], ['Safari', 4]]
    return render(request, 'Fitness_Summary.html', locals())

def nsummary(request):
    browser_stats = [['Chrome', 52.9], ['Firefox', 27.7], ['Opera', 1.6],
                     ['Internet Explorer', 12.6], ['Safari', 4]]
    return render(request, 'Nutrition_Summary.html', locals())

def import_db(request):
    f = open('UserData.csv', 'r')
    count =1
    for line in f:
        if count == 1:
            count += 1
        else :
            #print count
            line = line.split(',')
            #print line[16]
            user = request.user
            date_created = line[0]
            health = HealthParameters.objects.create()
            fitness = FitnessParameters.objects.create()
            nutrition= NutritionParameters.objects.create()
            health.health_date = date_created
            health.bp_systolic = line[1]
            health.bp_diastolic = line[2]
            health.weight = line[3]
            health.height = line[4]
            health.save()
            user.health_param = health
            fitness.min_light_activity = line[5]
            fitness.min_sedentary_activity = line[6]
            fitness.min_sleep_activity = line[7]
            fitness.min_awake = line[8]
            fitness.min_very_awake = line[9]
            fitness.fitness_date = date_created
            fitness.steps = line[10]
            fitness.distance = line[11]
            fitness.activity_score = line[12]
            fitness.save()
            user.fitness_param = fitness
            nutrition.calories_in = line[13]
            nutrition.calories_burnt = line[14]
            nutrition.calories_planned_in = line[15]
            nutrition.calories_planned_out = line[16]
            nutrition.nutrition_date = date_created
            nutrition.save()
            user.nutrition_param = nutrition
            user.save()
            #print count
            count += 1
    f.close()
    return render(request, 'profile.html', {})


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            # user = request.user
            # test_img = Picture(docfile=request.FILES['docfile'])


            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('my_charts.views.profile'))
    else:
        form = PictureForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Picture.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

# class ContactView(FormView):
#     template_name = 'contact'
#     form_class = ContactForm
#     success_url = '/thanks/'
#
#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super(ContactView, self).form_valid(form)

def charts(request):
    exchange = {'2001-01-31': 1.064, '2002-01-31': 1.1305,
                '2003-01-31': 0.9417, '2004-01-31': 0.7937,
                '2005-01-31': 0.7609, '2006-01-31': 0.827,
                '2007-01-31': 0.7692, '2008-01-31': 0.6801,
                '2009-01-31': 0.7491, '2010-01-31': 0.7002,
                '2011-01-31': 0.7489, '2012-01-31': 0.7755,
                '2013-01-31': 0.7531,
    }

    browser_stats = [['Chrome', 52.9], ['Firefox', 27.7], ['Opera', 1.6],
                     ['Internet Explorer', 12.6], ['Safari', 4]]

    temperature = [{u'data': {'2012-00-01 00:00:00 -0700': 7,
                              '2012-01-01 00:00:00 -0700': 6.9,
                              '2012-02-01 00:00:00 -0700': 9.5,
                              '2012-03-01 00:00:00 -0700': 14.5,
                              '2012-04-01 00:00:00 -0700': 18.2,
                              '2012-05-01 00:00:00 -0700': 21.5,
                              '2012-06-01 00:00:00 -0700': 25.2,
                              '2012-07-01 00:00:00 -0700': 26.5,
                              '2012-08-01 00:00:00 -0700': 23.3,
                              '2012-09-01 00:00:00 -0700': 18.3,
                              '2012-10-01 00:00:00 -0700': 13.9,
                              '2012-11-01 00:00:00 -0700': 9.6},
                    u'name': u'Tokyo'},
                   {u'data': {'2012-00-01 00:00:00 -0700': -0.2,
                              '2012-01-01 00:00:00 -0700': 0.8,
                              '2012-02-01 00:00:00 -0700': 5.7,
                              '2012-03-01 00:00:00 -0700': 11.3,
                              '2012-04-01 00:00:00 -0700': 17,
                              '2012-05-01 00:00:00 -0700': 22,
                              '2012-06-01 00:00:00 -0700': 24.8,
                              '2012-07-01 00:00:00 -0700': 24.1,
                              '2012-08-01 00:00:00 -0700': 20.1,
                              '2012-09-01 00:00:00 -0700': 14.1,
                              '2012-10-01 00:00:00 -0700': 8.6,
                              '2012-11-01 00:00:00 -0700': 2.5},
                    u'name': u'New York'},
                   {u'data': {'2012-00-01 00:00:00 -0700': -0.9,
                              '2012-01-01 00:00:00 -0700': 0.6,
                              '2012-02-01 00:00:00 -0700': 3.5,
                              '2012-03-01 00:00:00 -0700': 8.4,
                              '2012-04-01 00:00:00 -0700': 13.5,
                              '2012-05-01 00:00:00 -0700': 17,
                              '2012-06-01 00:00:00 -0700': 18.6,
                              '2012-07-01 00:00:00 -0700': 17.9,
                              '2012-08-01 00:00:00 -0700': 14.3,
                              '2012-09-01 00:00:00 -0700': 9,
                              '2012-10-01 00:00:00 -0700': 3.9,
                              '2012-11-01 00:00:00 -0700': 1},
                    u'name': u'Berlin'},
                   {u'data': {'2012-00-01 00:00:00 -0700': 3.9,
                              '2012-01-01 00:00:00 -0700': 4.2,
                              '2012-02-01 00:00:00 -0700': 5.7,
                              '2012-03-01 00:00:00 -0700': 8.5,
                              '2012-04-01 00:00:00 -0700': 11.9,
                              '2012-05-01 00:00:00 -0700': 15.2,
                              '2012-06-01 00:00:00 -0700': 17,
                              '2012-07-01 00:00:00 -0700': 16.6,
                              '2012-08-01 00:00:00 -0700': 14.2,
                              '2012-09-01 00:00:00 -0700': 10.3,
                              '2012-10-01 00:00:00 -0700': 6.6,
                              '2012-11-01 00:00:00 -0700': 4.8},
                    u'name': u'London'}]

    sizes = [['X-Small', 5], ['Small', 27], ['Medium', 10],
             ['Large', 14], ['X-Large', 10]]

    areas = {'2013-07-27 07:08:00 UTC': 4, '2013-07-27 07:09:00 UTC': 3,
             '2013-07-27 07:10:00 UTC': 2, '2013-07-27 07:04:00 UTC': 2,
             '2013-07-27 07:02:00 UTC': 3, '2013-07-27 07:00:00 UTC': 2,
             '2013-07-27 07:06:00 UTC': 1, '2013-07-27 07:01:00 UTC': 5,
             '2013-07-27 07:05:00 UTC': 5, '2013-07-27 07:03:00 UTC': 3,
             '2013-07-27 07:07:00 UTC': 3}

    return render(request, 'charts.html', locals())

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import ContactForm
from django.template import RequestContext, Context
from django.core.mail import send_mail, BadHeaderError

def contactview(request):
    subject = request.POST.get('topic', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')

    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['chintamani.lonkar@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thankyou/')
    else:
        return render_to_response('contactme.html', {'form': ContactForm()})

    return render_to_response('contactme.html', {'form': ContactForm()}, Context(request))


def thankyou(request):
    return render_to_response('thankyou.html')