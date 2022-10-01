from django.urls import path
from user_application import views


urlpatterns = [
    path('register/',views.UserRegister.as_view()),

]
