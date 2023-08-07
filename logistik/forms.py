from django.forms import ModelForm
from logistik.models import Karyawan, Branch
from django import forms

class karyawanMain(forms.Form):
    # jabatan_choices = Karyawan.objects.all().distinct()
    # branch_choices = Karyawan.objects.all().distinct()
    # agent_choices = Karyawan.objects.all().distinct()


    id_karyawan = forms.CharField()
    nama_karyawan = forms.CharField()
    jabatan = forms.ChoiceField()
    salary = forms.IntegerField()
    alamat_karyawan = forms.CharField()
    no_hp_karyawan = forms.CharField()
    branch_id = forms.ChoiceField(choices=[('a','a'),('b','b'),('c','c')])
    agen_id = forms.ChoiceField(choices=[('a','a'),('b','b'),('c','c')])
    kota_karyawan = forms.ChoiceField()
    slug_karyawan = forms.IntegerField()




class cabangMain(forms.Form):
    title = 'Data Cabang'
    
