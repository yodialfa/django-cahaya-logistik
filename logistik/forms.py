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
            # 'ttl_karyawan',
            'no_hp_karyawan',
            'branch_id',
            'agen_id',
            'kota_karyawan',
            # 'tanggal_masuk',

        ]

    

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
    
