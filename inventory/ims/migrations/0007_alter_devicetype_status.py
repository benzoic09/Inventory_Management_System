# Generated by Django 4.2.11 on 2024-03-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0006_alter_devices_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicetype',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default=1, max_length=20),
        ),
    ]
