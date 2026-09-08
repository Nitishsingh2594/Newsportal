from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('faqs/',views.faqs),
    path('jobs/',views.jobs),
    path('news/',views.news),
    path('videonews/',views.videonews),
    path('newsdetails/',views.newsdetail),
    path('aboutme/',views.self),
    path('privacy/',views.policy),
    path('investor/',views.investor),
    path('knowmore/',views.knowmore),
]