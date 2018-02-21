from django.conf.urls import include, url
from django.contrib.auth.views import login
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^measure', hello.views.measure, name='measure'),
    url(r'^savemeasurements', hello.views.savemeasurements, name='savemeasurements'),
    url(r'^register', hello.views.register, name='register'),
    url(r'^logout', hello.views.logout, name='logout'),
    url(r'^login', login, {'template_name': 'login.html'}),
    url(r'^welcome', hello.views.welcome, name='welcome'),
    url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
]
