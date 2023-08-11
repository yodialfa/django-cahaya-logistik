from django.contrib import admin
from django.urls import path
from logistik.views import *
from django.conf.urls.static import static


urlpatterns = [
    path('admin/',admin.site.urls),
    path('cs/', cs, name="cs"),
    path('keuangan/', keuangan, name="keuangan"),
    path('laporan_harian/', laporan_harian, name="laporan_harian"),
    path('cabang/', cabang, name="cabang"),
    path('karyawan/', data_karyawan, name="karyawan"),
    path('', data_karyawan),
    path('cabang/detail/<slug:slug_branch>/', detailCabang,name="detail_cabang"),
    path('karyawan/detail/<slug:slug_karyawan>/', detailKaryawan, name="detail_karyawan"),
    path('karyawan/tambah_karyawan/', tambah_karyawan, name="tambah_karyawan"),
    path('temp/', temp, name="temp"),
    # url(r'^$', views.index, name='index'),

]
