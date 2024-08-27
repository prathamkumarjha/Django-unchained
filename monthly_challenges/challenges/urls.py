from . import views
from django.urls import path

urlpatterns = [
    # path("january", views.index),
    # path("feburary", views.feb),
    path("<month>",views.monthly_challenge)
]