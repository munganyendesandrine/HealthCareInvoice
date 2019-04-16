from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    url(r'^$',views.welcome, name='welcome'),
    # url(r'^$', views.profile_page, name='myprofilepage'),
    # url(r'^new/profileform$', views.my_profile, name='myprofile'),

]

