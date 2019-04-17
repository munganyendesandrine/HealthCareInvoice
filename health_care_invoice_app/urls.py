from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[

    url(r'^$',views.welcome, name='welcome'),
    url(r'^hpost/hpostform$', views.hcpost_info, name='hcpost_info'),
    url(r'^hpost/patientform$', views.patient_info, name='patient_info'),
    url(r'^hpost/serviceDetailsform$', views.service_details, name='service_details'),
]

