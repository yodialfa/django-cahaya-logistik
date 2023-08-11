# Generated by Django 4.1.7 on 2023-08-10 05:28

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_agen', models.CharField(max_length=10)),
                ('nama_agen', models.CharField(max_length=20)),
                ('alamat_agen', models.TextField(max_length=100)),
                ('alamat_singkat_agen', models.CharField(max_length=20)),
                ('no_telp_agen', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_branch', models.CharField(max_length=10)),
                ('nama_branch', models.CharField(max_length=20)),
                ('alamat_branch', models.TextField(max_length=100)),
                ('kota', models.CharField(max_length=20)),
                ('no_telp_branch', models.CharField(max_length=20)),
                ('slug_branch', models.SlugField(blank=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_cust', models.CharField(max_length=50)),
                ('alamat_cust', models.TextField()),
                ('no_hp_cust', models.CharField(max_length=20)),
                ('flag_cust', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Harga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asal', models.CharField(max_length=15)),
                ('tujuan_kec', models.CharField(max_length=20)),
                ('tujuan_coveran', models.CharField(max_length=20)),
                ('price_kg', models.IntegerField()),
                ('price_granmax', models.IntegerField()),
                ('price_engkel', models.IntegerField()),
                ('price_cdd', models.IntegerField()),
                ('price_fuso', models.IntegerField()),
                ('price_wing', models.IntegerField()),
                ('price_towing', models.IntegerField()),
                ('price_udara', models.IntegerField()),
                ('estimasi_darat', models.IntegerField()),
                ('estimasi_udara', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_karyawan', models.CharField(blank=True, max_length=10, null=True)),
                ('nama_karyawan', models.CharField(max_length=50)),
                ('jabatan', models.CharField(max_length=15)),
                ('salary', models.IntegerField()),
                ('alamat_karyawan', models.TextField()),
                ('tanggal_masuk', models.DateField(null=True)),
                ('kota_karyawan', models.CharField(max_length=30, null=True)),
                ('ttl_karyawan', models.DateField(null=True)),
                ('tanggal_resign', models.DateField(blank=True, null=True)),
                ('no_hp_karyawan', models.CharField(max_length=15)),
                ('slug_karyawan', autoslug.fields.AutoSlugField(editable=False, populate_from='id_karyawan')),
                ('agen_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logistik.agen')),
                ('branch_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logistik.branch')),
            ],
        ),
        migrations.AddField(
            model_name='agen',
            name='branch_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='logistik.branch'),
        ),
    ]
