from django.forms import ModelForm
from logistik.models import Karyawan, Customer, Transaksi
from django import forms
from django.utils.text import slugify
# from django.db.models import Max
from dal import autocomplete
# from django.urls import reverse_lazy

class karyawanForms(forms.ModelForm):
    class Meta:
        model = Karyawan
        fields = [
            # 'id_karyawan',
            'nama_karyawan',
            'jabatan',
            'salary',
            'alamat_karyawan',
            'ttl_karyawan',
            'no_hp_karyawan',
            'branch_id',
            'agen_id',
            'kota_karyawan',
            # 'tanggal_masuk',
        ]
        widgets = {
            'nama_karyawan': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'jabatan': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'salary': forms.NumberInput(attrs={'class': 'border rounded p-2 w-full'}),
            'alamat_karyawan': forms.Textarea(attrs={'class': 'border rounded p-2 w-full h-[15px]'}),
            'ttl_karyawan' : forms.DateInput(attrs={'type': 'date'}),
            'no_hp_karyawan' :forms.NumberInput(attrs={'class' : "bg-green-50 border border-green-500 text-green-900 placeholder-green-700 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5" }),

        }
   


class PhoneAutocomplete(autocomplete.Select2ListView):
    def get_list(self):
        q = self.q
        return list(Customer.objects.filter(no_hp_cust__icontains=q).values_list('no_hp_cust', flat=True))

class CSInput(forms.ModelForm):
    class Meta:
        model = Transaksi
        fields = ['do_po',
                  'no_resi',
                  'no_hp_pengirim',
                  'nama_pengirim',
                  'alamat_pengirim',
                  'no_hp_penerima',
                  'nama_penerima',
                  'alamat_penerima',
                  'layanan',
                  'asal',
                  'tujuan',
                  'tujuan_coveran',
                  'harga_id',
                  'berat',
                  'diskon',
                  'biaya_surat',
                  'biaya_packing',
                  'jenis_barang',
                  'taksasi',
                  'premi_asuransi',
                  'total_cash',
                  'total_bayartujuan',
                  'total_transaksi']
        widgets = {
            'no_resi' : forms.TextInput(attrs={'id' : 'resi'}),
            'no_hp_pengirim': forms.TextInput(attrs={'id': 'phone-input', 'data-placeholder': 'Type customer phone number'}),
            'nama_pengirim': forms.TextInput(attrs={'id': 'id_nama_pengirim'}),
            'alamat_pengirim': forms.TextInput(attrs={'id': 'id_alamat_pengirim'}),
            'no_hp_penerima': forms.TextInput(attrs={'id':'receiver-input','data-placeholder':'Type customer phone number'}),
            'nama_penerima': forms.TextInput(attrs={'id':'name_receiver'}),
            'alamat_penerima': forms.TextInput(attrs={'id':'alamat_receiver'}),


            # ... other widgets ...
        }



