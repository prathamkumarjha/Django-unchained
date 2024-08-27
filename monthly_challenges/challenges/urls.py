from . import views
from django.urls import path

urlpatterns = [
    path("<int:month_integer>/", views.monthly_challenge_by_number, name='month_challenge_by_number'),
    path("<str:month_string>/", views.monthly_challenge, name="month_challenge"),
]
