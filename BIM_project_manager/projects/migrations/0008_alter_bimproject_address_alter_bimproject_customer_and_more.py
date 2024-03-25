# Generated by Django 5.0.2 on 2024-03-25 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_bimproject_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bimproject',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='indirizzo'),
        ),
        migrations.AlterField(
            model_name='bimproject',
            name='customer',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='committente'),
        ),
        migrations.AlterField(
            model_name='bimproject',
            name='logo_img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='immagine copertina'),
        ),
        migrations.AlterField(
            model_name='bimproject',
            name='name',
            field=models.CharField(max_length=80, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='bimproject',
            name='phase',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='fase progettuale'),
        ),
    ]
