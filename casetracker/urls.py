from django.urls import path
from . import views

app_name = 'casetracker'
urlpatterns = [    
    path('', views.localcasetracker, name='localcasetrackername'),
]
