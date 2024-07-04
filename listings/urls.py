from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexpage, name='home'),
    path('sign-up', views.signup, name='signup'),
    path('homepage', views.homepage, name='homepage'),
    path('jobs', views.jobposting, name='jobs'),
    path('internships', views.internshipposting, name='internships'),
    path('about us', views.aboutus, name='aboutus'),
    path('privacy policy', views.privacypolicy, name='privacypolicy'),
    path('report issue', views.reportissue, name='reportissue'),
    path('techolution internship', views.techolution, name='techolution internship'),
    path('axiom internship', views.axiom, name='axiom internship'),
    path('happyfox internship', views.happyfox, name='happyfox internship'),
    path('cadence internship', views.cadence, name='cadence internship'),
    path('loreal job', views.loreal, name='loreal job'),
    path('sarlabirla job', views.sarlabirla, name='sarlabirla job'),
    path('detailjobs', views.jobdetailpage, name='detailjobs'),
    path('internshipform', views.savedata, name='internshipform'),
    path('apollo job', views.apollo, name='apollo job'),
    path('contact us', views.contactus, name='contactus'),
    path('filter', views.filter, name='filter'),
    path('detailpage',views.detailpage, name="detailpage"),
    path('jobform',views.savejobdata, name="jobform"),
    path('base',views.base, name="base"),
    path('applyhere', views.saveApplicationForm, name='saveApplicationForm')
]