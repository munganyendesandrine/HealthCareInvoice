from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    url(r'^$',views.welcome, name='welcome'),
    url(r'^hpost/hpostform$', views.my_profile, name='myprofile'),

]

