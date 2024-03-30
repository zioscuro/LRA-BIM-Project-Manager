# Generated by Django 5.0.2 on 2024-03-28 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_report_description_alter_report_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bimproject',
            name='phase',
            field=models.CharField(blank=True, choices=[('RI', 'Rilievo'), ('PF', 'Fattibilità'), ('PD', 'Definitivo'), ('PE', 'Esecutivo'), ('DL', 'Direzione lavori'), ('CS', 'Costruttivo'), ('AB', 'As Built')], max_length=2, null=True, verbose_name='fase progettuale'),
        ),
        migrations.AlterField(
            model_name='clashtest',
            name='clash_active',
            field=models.PositiveIntegerField(verbose_name='interferenze attive'),
        ),
        migrations.AlterField(
            model_name='clashtest',
            name='clash_approved',
            field=models.PositiveIntegerField(verbose_name='interferenze approvate'),
        ),
        migrations.AlterField(
            model_name='clashtest',
            name='clash_new',
            field=models.PositiveIntegerField(verbose_name='interferenze nuove'),
        ),
        migrations.AlterField(
            model_name='clashtest',
            name='clash_resolved',
            field=models.PositiveIntegerField(verbose_name='interferenze risolte'),
        ),
        migrations.AlterField(
            model_name='clashtest',
            name='clash_reviewed',
            field=models.PositiveIntegerField(verbose_name='interferenze riviste'),
        ),
        migrations.AlterField(
            model_name='clashtest',
            name='comments',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='commenti'),
        ),
        migrations.AlterField(
            model_name='clashtest',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='validationtest',
            name='comments',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='commenti'),
        ),
        migrations.AlterField(
            model_name='validationtest',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='validationtest',
            name='issues',
            field=models.PositiveIntegerField(verbose_name='difformità riscontrate'),
        ),
        migrations.AlterField(
            model_name='validationtest',
            name='specification',
            field=models.CharField(max_length=100, verbose_name='specifica di verifica'),
        ),
    ]