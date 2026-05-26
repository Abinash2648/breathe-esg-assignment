from django.urls import path

from .views import *


urlpatterns = [

    path(
        'upload-csv/', upload_csv ),
     path('emissions/', get_emissions),
     path('approve/<int:id>/',approve_emission),
]