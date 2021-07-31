
from django.urls import path
from .views import *

app_name = 'jobs'

urlpatterns = [

    path('contact/', contact, name='contact'),
    path('about/', about_us, name='about'),
    path('service/', service, name='service'),
    path('service/service-single.html/',service_single,name="service-single"),
    # path('service/design', service, name='design'),
    path('job-post/', job_post, name='job-post'),
    path('job-listing/', job_listing, name='job-listing'),
    path('job-single/<int:id>/', job_single, name='job-single'),
    path('search/', SearchView.as_view(), name='search'),
    path('apply/', apply_job, name='apply'),
    path('apply/succesful/', succesful,name='succesful'),


]
