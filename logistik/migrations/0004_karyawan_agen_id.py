# Generated by Django 4.1.7 on 2023-07-31 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistik', '0003_remove_branch_flag_branch_remove_branch_nama_agen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyawan',
            name='agen_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='logistik.agen'),
        ),
    ]