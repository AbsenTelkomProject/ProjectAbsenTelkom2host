# Generated by Django 3.0.3 on 2020-06-19 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('absentelkom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_absen_ami',
            name='id_jampel',
        ),
    ]
