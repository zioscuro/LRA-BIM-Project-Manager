from django.db import models

# Create your models here.

class Project(models.Model):
  """ 
  a project in the domain model 
  each project contains several BIM models
  """
  name = models.CharField(max_length=80)
  description = models.CharField(max_length=150, blank=True, null=True)
  logo_img = models.ImageField(blank=True, null=True)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Progetto'
    verbose_name_plural = 'Progetti'


class BimModel(models.Model):
  """
  a BIM model related to a Project
  each BIM model contains several Info Sheets
  """
  name = models.CharField(max_length=80)
  discipline = models.CharField(max_length=50, blank=True, null=True)
  designer =  models.CharField(max_length=50, blank=True, null=True)
  project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bim_models')

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Modello'
    verbose_name_plural = 'Modelli'

class InfoSheet(models.Model):
  """
  an Info Sheet related to a BIM Model
  each Info Sheet contains several Reports
  """
  name = models.CharField(max_length=80)
  description = models.CharField(max_length=150, blank=True, null=True)
  bim_model = models.ForeignKey(BimModel, on_delete=models.CASCADE, related_name='info_sheets')

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Scheda informativa'
    verbose_name_plural = 'Schede informative'

class Report(models.Model):
  """
  a Report related to a Info Sheet
  each Report contains several Tests
  """
  name = models.CharField(max_length=80)
  description = models.CharField(max_length=150, blank=True, null=True)
  info_sheet = models.ForeignKey(InfoSheet, on_delete=models.CASCADE, related_name='reports')

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Report'
    verbose_name_plural = 'Reports'

class ClashTest(models.Model):
  """
  a Clash Test related to a Report
  """
  date = models.DateTimeField(auto_now_add=True)
  comments = models.CharField(max_length=150, blank=True, null=True)
  clash_new = models.PositiveIntegerField()
  clash_active = models.PositiveIntegerField()
  clash_reviewed = models.PositiveIntegerField()
  clash_approved = models.PositiveIntegerField()
  clash_resolved = models.PositiveIntegerField()
  report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='clash_tests')

  def __str__(self):
    return f'{self.report.name} - {self.date}'
  
  class Meta:
    verbose_name = 'Clash Test'
    verbose_name_plural = 'Clash Tests'

class ValidationTest(models.Model):
  """
  a Validation Test related to a Report
  """
  date = models.DateTimeField(auto_now_add=True)
  comments = models.CharField(max_length=150, blank=True, null=True)
  specification = models.CharField(max_length=100, blank=True, null=True)
  issues = models.PositiveIntegerField()
  report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='validation_tests')

  def __str__(self):
    return f'{self.report.name} - {self.date}'
  
  class Meta:
    verbose_name = 'Validation Test'
    verbose_name_plural = 'Validation Tests'

