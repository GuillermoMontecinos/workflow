# Generated by Django 3.1 on 2020-10-11 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('run_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('razon_social', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField()),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('comuna', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainwork.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='ProcesoTipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainwork.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='TareaTipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('duracion_dias', models.IntegerField()),
                ('cargo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainwork.cargo')),
                ('procesotipo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainwork.procesotipo')),
            ],
        ),
        migrations.AddField(
            model_name='procesotipo',
            name='unidad',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainwork.unidad'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainwork.region'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='unidad',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainwork.unidad'),
        ),
    ]