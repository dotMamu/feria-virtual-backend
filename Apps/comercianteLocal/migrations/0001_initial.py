# Generated by Django 4.0 on 2022-12-08 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Publicada', 'Publicada'), ('En camino', 'En camino'), ('Finalizado', 'Finalizado')], default='Publicada', max_length=255)),
                ('orderDate', models.DateField(auto_now_add=True)),
                ('transport', models.BooleanField(default=True)),
                ('localClient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cuentas.comerciantelocal')),
                ('productor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cuentas.productor')),
            ],
        ),
    ]
