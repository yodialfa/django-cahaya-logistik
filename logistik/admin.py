from django.contrib import admin
from logistik.models import Branch, Agen, Karyawan

class KaryawanAdmin(admin.ModelAdmin):
    list_display = ['id','nama_karyawan', 'jabatan','salary','no_hp_karyawan']
    search_fields = ['jabatan']
    list_filter = ['jabatan']
    list_per_page = 10
   
# class BranchAdmin(admin.ModelAdmin):
#      readonly_fields = ['slug_branch',
#                         'id_branch',
#                         'nama_branch']

admin.site.register(Branch)
admin.site.register(Agen)
admin.site.register(Karyawan, KaryawanAdmin)

