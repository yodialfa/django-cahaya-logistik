from django.shortcuts import render
from logistik.models import Karyawan, Branch
# from django.http import HttpResponse

def cs(request):
    id_agen = 1
    id_karyawan = 1
    nama_karyawan = "Yodi"
    
    konteks = {
        'title' : 'CS Input',
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
        'title' : 'Laporan Harian',
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

def detailKaryawan(request,slug_karyawan):
#    //query ambil data Karyawan
    Karyawans = Karyawan.objects.get( slug_karyawan=slug_karyawan)
    konteks = {
        'title' : 'Detail Karyawan',
        'headings' : 'Detail Karyawan',
        'Karyawans' : Karyawans,
    }
    return  render(request, 'detail_karyawan.html', konteks)

def cabang(request):
#    //query ambil data Karyawan
    cabangs = Branch.objects.all()
    print(cabangs)
    cabs = {
        'title' : 'Data Cabang',
        'headings' : 'Data Cabang',
        'cabangs' : cabangs,

    }
    return render(request, 'cabang.html', cabs)

def detailCabang(request,slug_branch):
    Cabangs = Branch.objects.get( slug_branch=slug_branch)
    print(Cabangs)
    print(request)
    cabs = {
        'title' : 'Detail Cabang',
        'headings' : 'Detail Cabang',
        'Cabangs' : Cabangs,
    }
    return  render(request, 'detail_cabang.html', cabs)


