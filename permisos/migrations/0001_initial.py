# Generated by Django 2.2 on 2021-04-13 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_permiso', models.CharField(max_length=200)),
                ('fecha_expedicion', models.DateField()),
                ('fecha_expiracion', models.DateField()),
                ('empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empleado', to='empleados.Empleados')),
            ],
        ),
    ]