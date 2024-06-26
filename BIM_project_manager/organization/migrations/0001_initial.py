# Generated by Django 5.0.2 on 2024-05-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthoringSoftware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='nome')),
                ('version', models.CharField(blank=True, max_length=150, null=True, verbose_name='versione')),
            ],
            options={
                'verbose_name': 'Software di Authoring',
                'verbose_name_plural': 'Software di Authoring',
            },
        ),
        migrations.CreateModel(
            name='BimExpert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='nome')),
                ('position', models.CharField(blank=True, max_length=80, null=True, verbose_name='qualifica')),
            ],
            options={
                'verbose_name': 'Professionista',
                'verbose_name_plural': 'Professionisti',
            },
        ),
        migrations.CreateModel(
            name='BimSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='nome')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='descrizione')),
            ],
            options={
                'verbose_name': 'Specifica coordinamento/verifica',
                'verbose_name_plural': 'Specifiche coordinamento/verifica',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='nome')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='descrizione')),
                ('code', models.CharField(blank=True, max_length=3, null=True, verbose_name='codice disiplina')),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Discipline',
            },
        ),
        migrations.CreateModel(
            name='LodReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='nome')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='descrizione')),
            ],
            options={
                'verbose_name': 'Scheda LOD',
                'verbose_name_plural': 'Schede LOD',
            },
        ),
        migrations.CreateModel(
            name='ProjectPhase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='nome')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='descrizione')),
            ],
            options={
                'verbose_name': 'Fase progetto',
                'verbose_name_plural': 'Fasi progetto',
            },
        ),
    ]
