from django.shortcuts import render, redirect
from logistik.models import Karyawan, Branch
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from .forms import * 
from django.core.paginator import Paginator
import time

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
        'heading' : 'Laporan Harian',
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
    karyawans = Karyawan.objects.all().order_by('nama_karyawan')
    items_per_page = 15
    paginator  = Paginator(karyawans,items_per_page)
    page_list = request.GET.get('page')
    page = paginator.get_page(page_list)
    karyawan_form = karyawanForms(request.POST or None)

    if request.method == 'POST':
        if karyawan_form.is_valid():
            karyawan_form.save()
            messages.success(request, 'Input was successful!')
            time.sleep(2)
            return redirect('logistik:karyawan')
            
        
#         # redirect('logistik:karyawan')
        else:
            karyawan_form = KaryawanForm()

    konteks = {
        'title' : 'Data Karyawan',
        'headings' : 'Data Karyawan',
        'page' : page,
        'karyawan_form': karyawan_form,
        'items_per_page': items_per_page,

    }
    if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return JsonResponse({'success': False, 'errors': karyawan_form.errors})
    else:
        return render(request, 'data_karyawan.html', konteks)
    # return render(request, 'data_karyawan.html', konteks)


def detailKaryawan(request,slug_karyawan):
#    //query ambil data Karyawan
    Karyawans = Karyawan.objects.get( slug_karyawan=slug_karyawan)
    konteks = {
        'title' : 'Data Karyawan',
        'headings' : 'Detail Karyawan',
        'Karyawans' : Karyawans,
    }
    return  render(request, 'detail_karyawan.html', konteks)




def cabang(request):
#    
    cabangs = Branch.objects.all()
    cabs = {
        'title' : 'Data Cabang',
        'headings' : 'Data Cabang',
        'cabangs' : cabangs,

    }
    return render(request, 'cabang.html', cabs)

def detailCabang(request,slug_branch):
    Cabangs = Branch.objects.get( slug_branch=slug_branch)
    cabs = {
        'title' : 'Data Cabang',
        'headings' : 'Detail Cabang',
        'Cabangs' : Cabangs,
    }
    return  render(request, 'detail_cabang.html', cabs)

def temp(request):
    return  render(request, 'temp.html')

# def tambah_karyawan(request):
#     formTambahKaryawan = forms.karyawanMain()
#     konteks = {
#         'title' : 'Data Karyawan',
#         'headings' : 'Tambah Data Karyawan',
#         'karyawan_form' : formTambahKaryawan,

#     }
#     return  render(request, 'form_tambah_karyawan.html',konteks)


def tambah_karyawan(request):
    karyawan_form = karyawanForms(request.POST or None)
    print(request.POST)
    if request.method == 'POST':
        if karyawan_form.is_valid():
            karyawan_form.save()
            return redirect('logistik:karyawan')
        else:
            karyawan_form = KaryawanForm()

    context = {
        'page_title': 'create post',
        'karyawan_form': karyawan_form
    }
    return render(request, 'form_tambah_karyawan.html', context)




