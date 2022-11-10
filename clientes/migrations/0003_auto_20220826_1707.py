# Generated by Django 3.2.5 on 2022-08-26 20:07

import clientes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.BinaryField()),
                ('branch_name', models.TextField()),
                ('branch_address_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='cliente',
            name='img_profile',
            field=models.ImageField(upload_to=clientes.models.upload_to),
        ),
    ]
