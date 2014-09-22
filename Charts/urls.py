from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Charts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'my_charts.views.home', name='home'),
    url(r'^register/$', 'my_charts.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^profile$', 'my_charts.views.profile', name='profile'),
    url(r'^dashboard/$', 'my_charts.views.dashboard', name='dashboard'),
    url(r'^charts/$', 'my_charts.views.charts', name='charts'),
    url(r'^about/$', 'my_charts.views.about', name='about'),
    url(r'^home/$', 'my_charts.views.home', name='home'),
    url(r'^signin/$', 'my_charts.views.signin', name='signin'),
    url(r'^contact/$', 'my_charts.views.contact', name='contact'),
    url(r'^contact/thankyou/', 'my_charts.views.thankyou', name='thankyou'),
    url(r'^contactme/', 'my_charts.views.contactview',name='contactme'),
    url(r'^read/', 'my_charts.views.read',name='read'),
    url(r'^list/$', 'my_charts.views.list', name='list'),
    url(r'^import_db/$', 'my_charts.views.import_db', name='import_db'),
    url(r'^hsummary/$', 'my_charts.views.hsummary', name='hsummary'),
    url(r'^fsummary/$', 'my_charts.views.fsummary', name='fsummary'),
    url(r'^nsummary/$', 'my_charts.views.nsummary', name='nsummary'),



)
