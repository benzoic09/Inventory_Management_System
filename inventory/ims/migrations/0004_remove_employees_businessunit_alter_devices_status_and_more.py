# Generated by Django 4.2.11 on 2024-03-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0003_alter_devices_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='BusinessUnit',
        ),
        migrations.AlterField(
            model_name='devices',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('D', 'Damaged'), ('Q', 'Dead')], default='A', max_length=1),
        ),
        migrations.AlterField(
            model_name='devicetype',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('D', 'Inactive')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='employees',
            name='Department',
            field=models.CharField(choices=[('1', 'sales'), ('2', 'Delivery'), ('3', 'Warehouse')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='employees',
            name='branch',
            field=models.CharField(choices=[('NBI', 'NAIRONI'), ('KSM', 'KISUMU'), ('MSA', 'MOMBASA')], max_length=3),
        ),
        migrations.DeleteModel(
            name='branch',
        ),
    ]
