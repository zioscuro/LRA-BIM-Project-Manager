# Generated by Django 5.0.2 on 2024-03-25 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_bimproject_address_bimproject_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bimproject',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='descrizione'),
        ),
    ]