from django.shortcuts import render

# from django.http import HttpResponse

def login(request):
    id_agen = 22222
    id_karyawan = 12222
    nama_karyawan = "Yodi"
    
    konteks = {
        'title' : 'CS Input',
        'id_agen' : id_agen,
        'id_karyawan' : id_karyawan,
        'nama_karyawan' : nama_karyawan,
    }
    return render(request,'login.html',konteks)