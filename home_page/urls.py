from django.urls import path
from home_page import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('product/',views.ProductCategory.as_view()),
    path('banner/',views.HomeBanner.as_view()),
]+ static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)