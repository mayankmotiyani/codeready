from django.urls import path
from navbar_application import views

urlpatterns = [
    path('',views.WebThemes.as_view()),
]
