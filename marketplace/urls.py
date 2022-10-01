from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home_page.urls')),
    path('accounts/', include('allauth.urls')),
    path('user/userlogin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/',include('user_application.urls')),
    path('marketapp/',include('market_app.urls')),
    path('navbarapp/',include('navbar_application.urls')),
    path('footerapp/',include('footer_application.urls')),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
