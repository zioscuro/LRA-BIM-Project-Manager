from django.db import models
from django.urls import reverse
from organization.models import AuthoringSoftware, BimExpert, Discipline, LodReference, ProjectPhase, BimSpecification

# Create your models here.

class BimProject(models.Model):
  name = models.CharField(max_length=50, verbose_name="nome")
  description = models.CharField(max_length=150, verbose_name="descrizione", default='-')
  customer = models.CharField(max_length=50, verbose_name="committente", default='-')
  address = models.CharField(max_length=150, verbose_name="indirizzo", default='-')  
  phase = models.ForeignKey(ProjectPhase, on_delete=models.SET_DEFAULT,  related_name='projects', verbose_name="fase progettuale", default=1)
  
  default_designer = models.ForeignKey(BimExpert, on_delete=models.SET_DEFAULT, related_name='designer_role_projects', verbose_name="responsabile progetto", default=1)
  default_bim_manager = models.ForeignKey(BimExpert, on_delete=models.SET_DEFAULT, related_name='bim_manager_role_projects', verbose_name="bim manager progetto", default=1)
  default_bim_coordinator = models.ForeignKey(BimExpert, on_delete=models.SET_DEFAULT, related_name='bim_coordinator_role_projects', verbose_name="bim coordinator progetto", default=1)
  default_bim_specialist = models.ForeignKey(BimExpert, on_delete=models.SET_DEFAULT, related_name='bim_specialist_role_projects', verbose_name="bim specialist progetto", default=1)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('manage_project', kwargs={'pk': self.pk})
  
  class Meta:
    verbose_name = 'Progetto'
    verbose_name_plural = 'Progetti'

class BimModel(models.Model):
  name = models.CharField(max_length=50, verbose_name="nome")
  description = models.CharField(max_length=150, verbose_name="descrizione")
  
  discipline = models.ForeignKey(Discipline, on_delete=models.SET_DEFAULT, related_name='bim_models', verbose_name="disciplina", default=1)
  authoringSoftware = models.ForeignKey(AuthoringSoftware, on_delete=models.SET_DEFAULT, related_name='bim_models', verbose_name="software di authoring", default=1)
  lodReference = models.ForeignKey(LodReference, on_delete=models.SET_DEFAULT, related_name='bim_models', verbose_name="scheda LOD", default=1)

  designer =  models.ForeignKey(BimExpert, on_delete=models.SET_DEFAULT, related_name='designer_role_models', verbose_name="progettista", default=1)
  bim_manager = models.ForeignKey(BimExpert, on_delete=models.SET_DEFAULT, related_name='bim_manager_role_models', verbose_name="bim manager", default=1)
  bim_coordinator = models.ForeignKey(BimExpert, on_delete=models.SET_DEFAULT, related_name='bim_coordinator_role_models', verbose_name="bim coordinator", default=1)
  bim_specialist = models.ForeignKey(BimExpert, on_delete=models.SET_DEFAULT, related_name='bim_specialist_role_models', verbose_name="bim specialist", default=1)
  
  bim_project = models.ForeignKey(BimProject, on_delete=models.CASCADE, related_name='bim_models', verbose_name="progetto", default=1)
  
  default_coordination = models.BooleanField(default=False)
  default_validation = models.BooleanField(default=False)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('manage_bim_model', kwargs={'pk': self.pk})
  
  class Meta:
    verbose_name = 'Modello'
    verbose_name_plural = 'Modelli'

class InfoSheet(models.Model):
  SHEET_TYPE_CHOICES = {
    'Coordination': 'Coordinamento',
    'Validation': 'Verifica',
  }
  sheet_type = models.CharField(max_length=20, choices=SHEET_TYPE_CHOICES, verbose_name="tipo scheda")  
  name = models.CharField(max_length=80, verbose_name="nome")
  description = models.CharField(max_length=150, verbose_name="disciplina", default='-')
  bim_model = models.ForeignKey(BimModel, on_delete=models.CASCADE, related_name='info_sheets')

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('manage_info_sheet', kwargs={'pk': self.pk})
  
  class Meta:
    verbose_name = 'Scheda informativa'
    verbose_name_plural = 'Schede informative'

class Report(models.Model):
  name = models.CharField(max_length=80, verbose_name="nome report")
  description = models.CharField(max_length=150, verbose_name="descrizione report", default='-')
  specification = models.ForeignKey(BimSpecification, on_delete=models.SET_DEFAULT, related_name='reports', verbose_name="specifica coordinamento/verifica", default=1)
  
  info_sheet = models.ForeignKey(InfoSheet, on_delete=models.CASCADE, related_name='reports')

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('manage_report', kwargs={'pk': self.pk})
  
  class Meta:
    verbose_name = 'Report'
    verbose_name_plural = 'Reports'

class ClashTest(models.Model):
  date = models.DateTimeField(auto_now_add=True, verbose_name="data")
  comments = models.CharField(max_length=150, verbose_name="commenti", default='-')
  clash_new = models.PositiveIntegerField(verbose_name="interferenze nuove")
  clash_active = models.PositiveIntegerField(verbose_name="interferenze attive")
  clash_reviewed = models.PositiveIntegerField(verbose_name="interferenze riviste")
  clash_approved = models.PositiveIntegerField(verbose_name="interferenze approvate")
  clash_resolved = models.PositiveIntegerField(verbose_name="interferenze risolte")
  report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='clash_tests')

  def __str__(self):
    return f'{self.report.name} - {self.date}'
  
  class Meta:
    verbose_name = 'Test interferenze'
    verbose_name_plural = 'Tests interferenze'

class ValidationTest(models.Model):
  date = models.DateTimeField(auto_now_add=True, verbose_name="data")
  comments = models.CharField(max_length=150, verbose_name="commenti", default='-')
  issues = models.PositiveIntegerField(verbose_name="difformità riscontrate")
  report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='validation_tests')

  def __str__(self):
    return f'{self.report.name} - {self.date}'
  
  class Meta:
    verbose_name = 'Test verifica'
    verbose_name_plural = 'Tests verifica'

