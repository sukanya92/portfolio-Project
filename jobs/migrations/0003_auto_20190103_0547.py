# Generated by Django 2.1.3 on 2019-01-03 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190103_0546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imageFun',
            new_name='image',
        ),
    ]