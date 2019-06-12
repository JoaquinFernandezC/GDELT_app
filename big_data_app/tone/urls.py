from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),

    path('tone_by_date', views.tone_by_date, name='tone_by_date'),
    path('count_resume', views.count_resume, name='count_resume'),
    path('tone_count', views.tone_count, name='count'),
    path('events', views.event_counts_resume, name='event_count'),

    path('events_percentage', views.events_counts, name='event_percetage')
]
