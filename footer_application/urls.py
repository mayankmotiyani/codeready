from django.urls import path
from footer_application import views

urlpatterns = [
    path('',views.Footerviews.as_view()),
]
