# Generated by Django 5.0.2 on 2024-03-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_alter_infosheet_description_alter_infosheet_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='descrizione report'),
        ),
        migrations.AlterField(
            model_name='report',
            name='name',
            field=models.CharField(max_length=80, verbose_name='nome report'),
        ),
    ]
