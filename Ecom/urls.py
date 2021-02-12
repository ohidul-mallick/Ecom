from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.signUp,name='signup'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)