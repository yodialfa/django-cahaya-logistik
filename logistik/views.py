from django.shortcuts import render
# from django.http import HttpResponse

def cs(request):
    id_agen = 1
    id_karyawan = 1
    nama_karyawan = "Yodi"
    
    konteks = {
        'id_agen' : id_agen,
        'id_karyawan' : id_karyawan,
        'nama_karyawan' : nama_karyawan,
    }
    return render(request,'cs.html',konteks)

def keuangan(request):
    return render(request,'keuangan.html')


