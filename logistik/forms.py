from django.forms import ModelForm
from logistik.models import Karyawan
from django import forms
from django.utils.text import slugify
from django.db.models import Max

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
   

    

    # def save(self, *args, **kwargs):  # new
    # if not self.slug_karyawan:
    #   self.slug_karyawan = slugify(self.id)
    #   super(Karyawan, self).save(*args, **kwargs)


    # def save(self, commit=True):
    #     instance = super(karyawanForms, self).save(commit=False)
    #     instance.slug_karyawan = str(instance.id)
    #     if commit:
    #         instance.save()
    #     return instance


class cabangMain(forms.Form):
    title = 'Data Cabang'
    
