# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electroInv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('action', models.CharField(max_length=100, blank=True)),
                ('qty', models.IntegerField(null=True, blank=True)),
                ('note', models.CharField(max_length=100, blank=True)),
                ('vendor', models.CharField(max_length=100, blank=True)),
                ('invoice', models.CharField(max_length=100, blank=True)),
                ('price', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100, blank=True)),
                ('contact', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('library', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('part_number', models.CharField(max_length=100, blank=True)),
                ('description', models.CharField(max_length=100, blank=True)),
                ('value', models.CharField(max_length=100, blank=True)),
                ('location', models.CharField(max_length=100, blank=True)),
                ('vendor_sku', models.CharField(max_length=100, blank=True)),
                ('qty', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lastupdate', models.DateTimeField(auto_now=True)),
                ('manufacture', models.ForeignKey(blank=True, to='electroInv.Manufacture', null=True)),
                ('package', models.ForeignKey(blank=True, to='electroInv.Package', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100, blank=True)),
                ('contact', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='part',
            name='part_type',
            field=models.ForeignKey(blank=True, to='electroInv.Type', null=True),
        ),
        migrations.AddField(
            model_name='part',
            name='vendor',
            field=models.ForeignKey(blank=True, to='electroInv.Vendor', null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='part',
            field=models.ForeignKey(to='electroInv.Part'),
        ),
    ]
