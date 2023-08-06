from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls.static import static


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.login, name="login"),
    path('logistik/',include(('logistik.urls', 'logistik'),  namespace='logistik')),
    
    # path("__reload__/", include("django_browser_reload.urls")),
    # path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
