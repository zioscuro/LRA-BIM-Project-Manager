from django.db import models
from django.urls import reverse
from organization.models import ProjectPhase, BimExpert

# Create your models here.

class BimProject(models.Model):
  name = models.CharField(max_length=50, verbose_name="nome")
  description = models.CharField(max_length=150, blank=True, null=True, verbose_name="descrizione")
  customer = models.CharField(max_length=50, blank=True, null=True, verbose_name="committente")
  address = models.CharField(max_length=150, blank=True, null=True, verbose_name="indirizzo")  
  phase = models.ForeignKey(ProjectPhase, on_delete=models.SET_NULL, blank=True, null=True, related_name='projects', verbose_name="fase progettuale")
  default_designer = models.ForeignKey(BimExpert, on_delete=models.SET_NULL, blank=True, null=True, related_name='designer_role_projects', verbose_name="responsabile progetto")
  default_bim_manager = models.ForeignKey(BimExpert, on_delete=models.SET_NULL, blank=True, null=True, related_name='bim_manager_role_projects', verbose_name="bim manager progetto")
  default_bim_coordinator = models.ForeignKey(BimExpert, on_delete=models.SET_NULL, blank=True, null=True, related_name='bim_coordinator_role_projects', verbose_name="bim coordinator progetto")
  default_bim_specialist = models.ForeignKey(BimExpert, on_delete=models.SET_NULL, blank=True, null=True, related_name='bim_specialist_role_projects', verbose_name="bim specialist progetto")

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('manage_project', kwargs={'pk': self.pk})
  
  class Meta:
    verbose_name = 'Progetto'
    verbose_name_plural = 'Progetti'

class BimModel(models.Model):
  """
  a BIM model related to a Project
  each BIM model contains several Info Sheets
  """
  name = models.CharField(max_length=80, verbose_name="nome")

  DISCIPLINE_CHOICES = {
    'ARC': 'Architettonico',
    'STR': 'Strutture',
    'MEC': 'Impianti meccanici',
    'ELE': 'Impianti elettrici',
    'COO': 'Coordinamento',
  }

  discipline = models.CharField(choices=DISCIPLINE_CHOICES, max_length=50, blank=True, null=True, verbose_name="disciplina")
  designer =  models.CharField(max_length=50, blank=True, null=True, verbose_name="progettista")
  default_coordination = models.BooleanField(default=False)
  default_validation = models.BooleanField(default=False)
  authoringSoftware = models.CharField(max_length=50, blank=True, null=True, verbose_name="software di authoring")
  lodReference = models.CharField(max_length=100, blank=True, null=True, verbose_name="scheda LOD")
  project = models.ForeignKey(BimProject, on_delete=models.CASCADE, related_name='bim_models')

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('manage_bim_model', kwargs={'pk': self.pk})
  
  class Meta:
    verbose_name = 'Modello'
    verbose_name_plural = 'Modelli'

class InfoSheet(models.Model):
  """
  an Info Sheet related to a BIM Model
  each Info Sheet contains several Reports
  """
  
  SHEET_TYPE_CHOICES = {
    'Coordination': 'Coordinamento',
    'Validation': 'Verifica',
  }

  sheet_type = models.CharField(max_length=20, choices=SHEET_TYPE_CHOICES, verbose_name="tipo scheda")
  name = models.CharField(max_length=80, verbose_name="nome")
  description = models.CharField(max_length=150, blank=True, null=True, verbose_name="disciplina")
  bim_model = models.ForeignKey(BimModel, on_delete=models.CASCADE, related_name='info_sheets')

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('manage_info_sheet', kwargs={'pk': self.pk})
  
  class Meta:
    verbose_name = 'Scheda informativa'
    verbose_name_plural = 'Schede informative'

class Report(models.Model):
  """
  a Report related to a Info Sheet
  each Report contains several Tests
  """
  name = models.CharField(max_length=80, verbose_name="nome report")
  description = models.CharField(max_length=150, blank=True, null=True, verbose_name="descrizione report")
  info_sheet = models.ForeignKey(InfoSheet, on_delete=models.CASCADE, related_name='reports')

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('manage_report', kwargs={'pk': self.pk})
  
  class Meta:
    verbose_name = 'Report'
    verbose_name_plural = 'Reports'

class ClashTest(models.Model):
  """
  a Clash Test related to a Report
  """
  date = models.DateTimeField(auto_now_add=True, verbose_name="data")
  comments = models.CharField(max_length=150, blank=True, null=True, verbose_name="commenti")
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
  """
  a Validation Test related to a Report
  """
  date = models.DateTimeField(auto_now_add=True, verbose_name="data")
  comments = models.CharField(max_length=150, blank=True, null=True, verbose_name="commenti")
  specification = models.CharField(max_length=100, verbose_name="specifica di verifica")
  issues = models.PositiveIntegerField(verbose_name="difformità riscontrate")
  report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='validation_tests')

  def __str__(self):
    return f'{self.report.name} - {self.date}'
  
  class Meta:
    verbose_name = 'Test verifica'
    verbose_name_plural = 'Tests verifica'

