# Generated by Django 3.2.15 on 2022-09-12 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0003_auto_20220912_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='date',
            new_name='trade_date',
        ),
        migrations.RenameField(
            model_name='trade',
            old_name='deadline',
            new_name='trade_deadline',
        ),
        migrations.RenameField(
            model_name='trade',
            old_name='is_active',
            new_name='trade_is_active',
        ),
    ]
