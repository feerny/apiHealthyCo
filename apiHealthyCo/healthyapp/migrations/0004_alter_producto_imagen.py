# Generated by Django 4.0.6 on 2022-09-01 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthyapp', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
