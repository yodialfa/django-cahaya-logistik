from django.shortcuts import render, redirect,  get_object_or_404
from logistik.models import Karyawan, Branch, Customer, Receiver
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from .forms import * 
from django.core.paginator import Paginator
import time
from dal import autocomplete

# from django.http import HttpResponse

def cs(request):
    if request.method == 'POST':
        form = CSInput(request.POST)
        if form.is_valid():
            customer_phone = form.cleaned_data['no_hp_pengirim']
            name_cust = form.cleaned_data['nama_pengirim']
            customer, created = Customer.objects.get_or_create(
                no_hp_cust=customer_phone, nama_nama=name_cust
            )
            form.instance.customer = customer
            form.save()
            # Redirect or perform other actions
        
    else:
        form = CSInput()

    konteks = {
        'title' : 'CS Input',
        'form' : form,
    }
        
    return render(request, 'cs.html', konteks)


class CustomerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Customer.objects.all()
        if self.q:
            qs = qs.filter(no_hp_cust__icontains=self.q)  # Modify based on your needs
        return qs
    
    def get_result_label(self, item):
        return item.no_hp_cust  # Display the phone number in the autocomplete suggestions

def get_receiver_names(request):
    phone_receiver = request.GET.get('no_hp_receiver')
    matching_customers = Receiver.objects.filter(no_hp_penerima__icontains=phone_receiver)

    receiver_data = []
    for customer in matching_customers:
        customer_data = {
            'cust_phone' : customer.no_hp_penerima,
            'cust_name'  : customer.nama_penerima,
            'cust_address' : customer.alamat_penerima,
        }
        receiver_data.append(customer_data)
    return JsonResponse({'receiver': receiver_data})

def get_customer_names(request):
    phone_number = request.GET.get('no_hp_cust')
    matching_customers = Customer.objects.filter(no_hp_cust__icontains=phone_number)

    customers_data = []
    for customer in matching_customers:
        customer_data = {
            'cust_phone' : customer.no_hp_cust,
            'cust_name'  : customer.nama_cust,
            'cust_address' : customer.alamat_cust,
        }
        customers_data.append(customer_data)
    return JsonResponse({'customers': customers_data})




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




