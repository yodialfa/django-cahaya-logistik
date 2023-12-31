from django.contrib import admin
from logistik.models import Branch, Agen, Karyawan,Customer, Receiver, Harga

class KaryawanAdmin(admin.ModelAdmin):
    list_display = ['id','nama_karyawan', 'jabatan','salary','no_hp_karyawan']
    search_fields = ['jabatan']
    list_filter = ['jabatan']
    list_per_page = 10
    readonly_fields = ['slug_karyawan']
   
class BranchAdmin(admin.ModelAdmin):
     readonly_fields = ['slug_branch',
                        'id_branch',
                        'nama_branch']
     

# class CustomerAdmin(admin.ModelAdmin):
#      readonly_fields = ['slug_branch',
#                         'id_branch',
#                         'nama_branch']

admin.site.register(Branch, BranchAdmin)
admin.site.register(Agen)
admin.site.register(Customer)
admin.site.register(Karyawan, KaryawanAdmin)
admin.site.register(Receiver)
admin.site.register(Harga)

