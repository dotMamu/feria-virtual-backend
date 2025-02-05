# Generated by Django 4.0 on 2022-11-18 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VentaLocal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('productor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuentas.productor')),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('productorDescription', models.CharField(blank=True, max_length=255)),
                ('offer', models.BooleanField(default=False)),
                ('unitPrice', models.IntegerField()),
                ('adminArchives', models.CharField(blank=True, max_length=255)),
                ('techArchives', models.CharField(blank=True, max_length=255)),
                ('economicArchives', models.CharField(blank=True, max_length=255)),
                ('productor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuentas.productor')),
            ],
        ),
    ]
