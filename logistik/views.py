from django.shortcuts import render
from .models import Karyawan
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

def laporan_harian(request):
    no = 1
    no_resi = 'bdo121'
    nama_pengirim = "Yodi"
    nama_penerima = "Yodi"
    tujuan = "Ciamis"
    total_ongkir = 10000
    konteks = {
        'no' : no,
        'no_resi' : no_resi,
        'nama_pengirim' : nama_pengirim,
        'nama_penerima' : nama_penerima,
        'tujuan' : tujuan,
        'total_ongkir' : total_ongkir,
    }
    return render(request, 'laporan_harian.html', konteks)

def data_karyawan(request):
#    //query ambil data Karyawan
    karyawans = Karyawan.objects.all()
    print(karyawans)
    konteks = {
        'title' : 'Data Karyawan',
        'headings' : 'Data Karyawan',
        'karyawans' : karyawans,

    }
    return render(request, 'data_karyawan.html', konteks)

