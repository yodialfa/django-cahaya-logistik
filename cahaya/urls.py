from django.contrib import admin
from django.urls import path
from logistik.views import cs, keuangan, laporan_harian, data_karyawan, cabang
from django.conf.urls.static import static


urlpatterns = [
    path('admin/',admin.site.urls),
    path('cs/', cs),
    path('keuangan/', keuangan),
    path('laporan_harian/', laporan_harian),
    path('cabang/', cabang),
    path('karyawan/', data_karyawan),
    path('', data_karyawan),
]
