from django.contrib import admin
from django.urls import path
from logistik.views import cs, keuangan, laporan_harian, data_karyawan
from django.conf.urls.static import static


urlpatterns = [
    path('admin/',admin.site.urls),
    path('cs/', cs),
    path('keuangan/', keuangan),
    path('', laporan_harian),
    path('karyawan', data_karyawan),
]
