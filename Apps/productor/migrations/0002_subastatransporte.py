# Generated by Django 4.0 on 2022-12-02 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_delete_subastatransporte'),
        ('productor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubastaTransporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('origin', models.CharField(blank=True, max_length=255)),
                ('destination', models.CharField(blank=True, max_length=255)),
                ('processStatus', models.CharField(choices=[('Publicada', 'Publicada'), ('Cerrada', 'Cerrada'), ('Adjudicada', 'Adjudicada'), ('Cancelada', 'Cancelada'), ('Rechazada', 'Rechazada')], default='Publicada', max_length=255)),
                ('initDate', models.DateField(auto_now_add=True)),
                ('expectedCloseDate', models.DateField()),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cuentas.comercianteextranjero')),
                ('oferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productor.oferta')),
                ('productor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cuentas.productor')),
            ],
        ),
    ]
