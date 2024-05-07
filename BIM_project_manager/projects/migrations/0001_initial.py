# Generated by Django 5.0.2 on 2024-05-07 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BimProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nome')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='descrizione')),
                ('customer', models.CharField(blank=True, max_length=50, null=True, verbose_name='committente')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='indirizzo')),
                ('default_bim_coordinator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bim_coordinator_role_projects', to='organization.bimexpert', verbose_name='bim coordinator progetto')),
                ('default_bim_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bim_manager_role_projects', to='organization.bimexpert', verbose_name='bim manager progetto')),
                ('default_bim_specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bim_specialist_role_projects', to='organization.bimexpert', verbose_name='bim specialist progetto')),
                ('default_designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designer_role_projects', to='organization.bimexpert', verbose_name='responsabile progetto')),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='organization.projectphase', verbose_name='fase progettuale')),
            ],
            options={
                'verbose_name': 'Progetto',
                'verbose_name_plural': 'Progetti',
            },
        ),
        migrations.CreateModel(
            name='BimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='nome')),
                ('discipline', models.CharField(blank=True, choices=[('ARC', 'Architettonico'), ('STR', 'Strutture'), ('MEC', 'Impianti meccanici'), ('ELE', 'Impianti elettrici'), ('COO', 'Coordinamento')], max_length=50, null=True, verbose_name='disciplina')),
                ('designer', models.CharField(blank=True, max_length=50, null=True, verbose_name='progettista')),
                ('default_coordination', models.BooleanField(default=False)),
                ('default_validation', models.BooleanField(default=False)),
                ('authoringSoftware', models.CharField(blank=True, max_length=50, null=True, verbose_name='software di authoring')),
                ('lodReference', models.CharField(blank=True, max_length=100, null=True, verbose_name='scheda LOD')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bim_models', to='projects.bimproject')),
            ],
            options={
                'verbose_name': 'Modello',
                'verbose_name_plural': 'Modelli',
            },
        ),
        migrations.CreateModel(
            name='InfoSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_type', models.CharField(choices=[('Coordination', 'Coordinamento'), ('Validation', 'Verifica')], max_length=20, verbose_name='tipo scheda')),
                ('name', models.CharField(max_length=80, verbose_name='nome')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='disciplina')),
                ('bim_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_sheets', to='projects.bimmodel')),
            ],
            options={
                'verbose_name': 'Scheda informativa',
                'verbose_name_plural': 'Schede informative',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='nome report')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='descrizione report')),
                ('info_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='projects.infosheet')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
        migrations.CreateModel(
            name='ClashTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='data')),
                ('comments', models.CharField(blank=True, max_length=150, null=True, verbose_name='commenti')),
                ('clash_new', models.PositiveIntegerField(verbose_name='interferenze nuove')),
                ('clash_active', models.PositiveIntegerField(verbose_name='interferenze attive')),
                ('clash_reviewed', models.PositiveIntegerField(verbose_name='interferenze riviste')),
                ('clash_approved', models.PositiveIntegerField(verbose_name='interferenze approvate')),
                ('clash_resolved', models.PositiveIntegerField(verbose_name='interferenze risolte')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clash_tests', to='projects.report')),
            ],
            options={
                'verbose_name': 'Test interferenze',
                'verbose_name_plural': 'Tests interferenze',
            },
        ),
        migrations.CreateModel(
            name='ValidationTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='data')),
                ('comments', models.CharField(blank=True, max_length=150, null=True, verbose_name='commenti')),
                ('specification', models.CharField(max_length=100, verbose_name='specifica di verifica')),
                ('issues', models.PositiveIntegerField(verbose_name='difformità riscontrate')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='validation_tests', to='projects.report')),
            ],
            options={
                'verbose_name': 'Test verifica',
                'verbose_name_plural': 'Tests verifica',
            },
        ),
    ]
