# Generated by Django 3.0.4 on 2020-03-30 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIs_in_a_nutshell', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoecolor',
            old_name='style',
            new_name='color_name',
        ),
    ]
