# Generated by Django 5.0.2 on 2024-03-31 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_alter_bimproject_phase_alter_clashtest_clash_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bimmodel',
            name='discipline',
            field=models.CharField(blank=True, choices=[('ARC', 'Architettonico'), ('STR', 'Strutture'), ('MEC', 'Impianti meccanici'), ('ELE', 'Impianti elettrici'), ('COO', 'Coordinamento')], max_length=50, null=True, verbose_name='disciplina'),
        ),
        migrations.AlterField(
            model_name='infosheet',
            name='sheet_type',
            field=models.CharField(choices=[('Coordination', 'Coordinamento'), ('Validation', 'Verifica')], max_length=20, verbose_name='tipo scheda'),
        ),
    ]