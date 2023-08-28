from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField




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
  id_branch = models.CharField(max_length=10,null=False,)
  nama_branch = models.CharField(max_length=20)
  alamat_branch = models.TextField(max_length=100)
  kota = models.CharField(max_length=20)
  no_telp_branch = models.CharField(max_length=20)
  slug_branch = models.SlugField(blank=True,editable=False)


  def br_id(self):
    return self.nama_branch


  # def save(self):
  #   self.slug_branch = slugify(self.id_branch)
  #   super(Branch, self).save()

  def __str__(self):
    # template = '{0.nama_branch}'
    return self.nama_branch
  # "{}. {}".format(self.id_branch, self.nama_branch)
  
  
class Agen(models.Model):
  id_agen = models.CharField(max_length=10,null=False)
  nama_agen = models.CharField(max_length=20)
  alamat_agen = models.TextField(max_length=100)
  alamat_singkat_agen = models.CharField(max_length=20)
  no_telp_agen = models.CharField(max_length=20)
  branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)


  def __str__(self):
    # template = '{0.nama_agen}'
    return self.nama_agen
  # template.format(self)


class Karyawan(models.Model):
  id_karyawan = models.CharField(max_length=20, blank=True,null=True)
  nama_karyawan = models.CharField(max_length=50)
  jabatan = models.CharField(max_length=15)
  branch_id = models.ForeignKey(Branch, on_delete = models.CASCADE,blank=True, null=True)
  agen_id = models.ForeignKey(Agen, on_delete = models.CASCADE, blank=True, null=True)
  salary = models.IntegerField()
  alamat_karyawan = models.TextField()
  tanggal_masuk = models.DateField(null=True)
  kota_karyawan = models.CharField(max_length=30, null=True)
  ttl_karyawan = models.DateField(null=True)
  tanggal_resign = models.DateField(null=True,blank=True)
  no_hp_karyawan = models.CharField(max_length=15)
  slug_karyawan = AutoSlugField(populate_from='id_karyawan')

  def save(self, *args, **kwargs):
    super(Karyawan, self).save()
    if not self.id_karyawan:
      if self.branch_id:
        # Access the related Branch object
        related_branch = self.branch_id

        # Access the id_branch field of the related Branch
        self.id_karyawan = str(related_branch.id_branch) + str(self.id)
        self.slug_karyawan = self.id_karyawan

    super(Karyawan, self).save(*args, **kwargs)

  # def save(self, *args, **kwargs):
  #   if not self.slug_karyawan:
  #       self.slug_karyawan = str(self.id)
  #   super().save(*args, **kwargs)
  # def get_absolute_url(self):
  #   return reverse ("karyawan",kwargs={'slug_karyawan':self.slug_karyawan})
  
  

  def kar_id(self):
    return self.id

  def __str__(self):
    # template = '{0.nama_karyawan}'
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
  price_bl = models.IntegerField()
  estimasi_darat = models.IntegerField()
  estimasi_udara = models.IntegerField()


  def __str__(self):
    return "{}. {}".format(self.asal, self.tujuan_coveran)
  
class Customer(models.Model):
  flag = (
        ('ret', 'Retail'),
        ('comp', 'Company'),
    )
  no_hp_cust = models.CharField(max_length=15)
  nama_cust = models.CharField(max_length=30)
  alamat_cust = models.TextField(max_length=50)
  flag_cust = models.CharField(max_length=10 ,choices=flag, default='ret')

  def __str__(self):
    return self.no_hp_cust
  
class Receiver(models.Model):
  no_hp_penerima = models.CharField(max_length=15)
  nama_penerima = models.CharField(max_length=30)
  alamat_penerima = models.CharField(max_length=50)

  def __str__(self):
    return self.no_hp_penerima



class Transaksi(models.Model):
    flag_layanan = (
          ('darat', 'darat'),
          ('laut','laut'),
          ('udara','udara'),
          ('towing','towing'),
          ('trucking','trucking'),
          ('city','city'),
    )
    do_po = models.CharField(max_length=50, null=True)
    no_resi = models.CharField(max_length=20, primary_key=True)
    no_hp_pengirim = models.ForeignKey(Customer, on_delete = models.CASCADE, null=True)
    nama_pengirim = models.CharField(max_length=20)
    alamat_pengirim = models.CharField(max_length=50)
    no_hp_penerima = models.CharField(max_length=15)
    nama_penerima = models.CharField(max_length=20)
    alamat_penerima = models.CharField(max_length=50)
    layanan = models.CharField(max_length=10, choices=flag_layanan, default='darat')
    asal = models.CharField(max_length=20)
    tujuan = models.CharField(max_length=20)
    tujuan_coveran = models.CharField(max_length=20)
    harga_id = models.IntegerField(default=0)
    berat = models.IntegerField(default=0)
    diskon = models.IntegerField(default=0)
    biaya_surat = models.IntegerField(default=0)
    biaya_packing = models.IntegerField(default=0)
    jenis_barang = models.CharField(max_length=20)
    taksasi = models.IntegerField(default=0)
    premi_asuransi = models.IntegerField(default=0)
    total_cash = models.IntegerField(default=0)
    total_bayartujuan = models.IntegerField(default=0)
    total_transaksi = models.IntegerField(default=0)
    status_trx = models.CharField(max_length=25, default='1')
    no_manivest = models.CharField(max_length=25, null=True)
    karyawan_id = models.ForeignKey(Karyawan, on_delete = models.CASCADE, null=True)
    id_agen = models.ForeignKey(Agen, on_delete = models.CASCADE,null=True)
    id_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True)
    slug_transkasi = AutoSlugField(populate_from='no_transaksi', null=True )

    # def save(self, *args, **kwargs):
    # super(Transaksi, self).save()
    # if not self.no_resi:
    #   if self.branch_id:
    #     # Access the related Branch object
    #     related_branch = self.branch_id

    #     # Access the id_branch field of the related Branch
    #     self.no_resi = str(related_branch.id_branch) + str(self.no_resi)
    #     self.slug_transaksi = self.id_karyawan

    # super(Transaksi, self).save(*args, **kwargs)

    def __str__(self):
      return self.no_resi
