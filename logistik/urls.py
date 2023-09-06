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
    path('customer-autocomplete/', CustomerAutocomplete.as_view(), name='customer-autocomplete'),
    path('get-customer-names/', get_customer_names, name='get-customer-names'),
    path('get-receiver-names/', get_receiver_names, name='get-receiver-names'),
    path('get_distinct_city/', get_distinct_city, name='get_distinct_city'),
    path('get_distinct_tujuan/', get_distinct_tujuan, name='get_distinct_tujuan'),
    path('get_coverage/', get_coverage, name='get_coverage'),
    # url(r'^$', views.index, name='index'),

]
