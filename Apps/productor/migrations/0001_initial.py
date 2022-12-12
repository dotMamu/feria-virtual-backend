# Generated by Django 4.0 on 2022-12-12 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuentas', '0001_initial'),
        ('comercianteExtranjero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PUBLISHED', 'published'), ('HAS_OFFER', 'hasOffer'), ('CLOSED', 'closed')], default='PUBLISHED', max_length=30)),
                ('sold', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=255)),
                ('producer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuentas.producer')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('offerDescription', models.CharField(blank=True, max_length=255)),
                ('offerValue', models.IntegerField()),
                ('offerFileName', models.FileField(default=None, upload_to='')),
                ('assigned', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('ACCEPTED', 'accepted'), ('REJECTED', 'rejected'), ('STANDBY', 'standby')], default='STANDBY', max_length=30)),
                ('closed', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('bid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='offers', to='comercianteExtranjero.bid')),
                ('producer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuentas.producer')),
            ],
        ),
        migrations.CreateModel(
            name='LocalSaleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('localSale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localsaleimage', to='productor.localsale')),
            ],
        ),
    ]
