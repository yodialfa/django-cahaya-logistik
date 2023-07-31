from django.db import models


class Customer(models.Model):
 nama_cust = models.CharField(max_length=50)
 alamat_cust = models.TextField()
 no_hp_cust = models.CharField(max_length=20)
 flag_cust = models.CharField(max_length=10)
 

 def __str__(self):
  return self.nama_cust
 
#  class Foo(models.Model):
#   parent = models.ForeignKey('self')
    

class Branch(models.Model):
  nama_branch = models.CharField(max_length=20)
  alamat_branch = models.TextField(max_length=100)
  alamat_singkat_branch = models.CharField(max_length=20)
  no_telp_branch = models.CharField(max_length=20)

  def __str__(self):
    return self.nama_branch
  
class Agen(models.Model):
  nama_agen = models.CharField(max_length=20)
  alamat_agen = models.TextField(max_length=100)
  alamat_singkat_agen = models.CharField(max_length=20)
  no_telp_agen = models.CharField(max_length=20)
  branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True )

  def __str__(self):
    return self.nama_agen
  
class Karyawan(models.Model):
  nama_karyawan = models.CharField(max_length=50)
  jabatan = models.CharField(max_length=15)
  branch_id = models.ForeignKey(Branch, on_delete = models.CASCADE,null=True)
  agen_id = models.ForeignKey(Agen, on_delete = models.CASCADE,null=True)
  salary = models.IntegerField()
  alamat_karyawan = models.TextField()
  no_hp_karyawan = models.CharField(max_length=15)
  def __str__(self):
    return self.nama_karyawan


class Harga(models.Model):
  asal = models.CharField(max_length=15)
  tujuan_kec = models.CharField(max_length=20)
  tujuan_coveran = models.CharField(max_length=20)
  price_kg = models.IntegerField()
  price_granmax = models.IntegerField()
  price_engkel = models.IntegerField()
  price_cdd = models.IntegerField()
  price_fuso = models.IntegerField()
  price_wing = models.IntegerField()
  price_towing = models.IntegerField()
  price_udara = models.IntegerField()
  estimasi_darat = models.IntegerField()
  estimasi_udara = models.IntegerField()

  def __str__(self):
    return self.asal


# class Transaksi(models.Model):
#     do_po = models.CharField(max_length=50)
#     nama_pengirim = models.CharField(max_length=20)
#     alamat_pengirim = models.CharField(max_length=50)
#     no_hp_pengirim = models.CharField(max_length=15)
#     nama_penerima = models.CharField(max_length=20)
#     alamat_penerima = models.CharField(max_length=50)
#     no_hp_penerima = models.CharField(max_length=15)
#     layanan = models.CharField(max_length=10)
#     harga_id = models.ForeignKey(Customer, on_delete = models.CASCADE, null=True)
#     berat = models.IntegerField()
#     diskon = models.IntegerField()
#     biaya_surat = models.IntegerField()
#     biaya_packing = models.IntegerField()
#     jenis_barang = models.CharField(max_length=20)
#     taksasi = models.IntegerField()
#     premi_asuransi = models.IntegerField()
#     total_cash = models.IntegerField()
#     total_bayartujuan = models.IntegerField()
#     total_transaksi = models.IntegerField()
#     karyawan_id = models.ForeignKey(Karyawan, on_delete = models.CASCADE, null=True)
#     branch_id = models.ForeignKey(Branch, on_delete = models.CASCADE,null=True)

    # def __str__(self):
    #   return self.nama_pengirim
