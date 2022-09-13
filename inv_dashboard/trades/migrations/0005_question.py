# Generated by Django 3.2.15 on 2022-09-13 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0004_auto_20220912_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
