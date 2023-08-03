from django.contrib import admin
from django.urls import path, include
from . import views
# from django.conf.urls.static import static


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.login, name="login"),
    path('logistik/',include(('logistik.urls', 'logistik'),  namespace='logistik'))
]
