from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name="user"
urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.loginuser,name="login"),
    path('logout/',views.logoutuser,name="logout"),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)