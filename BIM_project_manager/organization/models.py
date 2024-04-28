from django.db import models

# Create your models here.

class ProjectPhase(models.Model):
  name = models.CharField(max_length=80, verbose_name="nome")
  description = models.CharField(max_length=150, blank=True, null=True, verbose_name="descrizione")

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Fase progetto'
    verbose_name_plural = 'Fasi progetto'

class Discipline(models.Model):
  name = models.CharField(max_length=80, verbose_name="nome")
  description = models.CharField(max_length=150, blank=True, null=True, verbose_name="descrizione")
  code = models.CharField(max_length=3, blank=True, null=True, verbose_name="codice disiplina")

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Disciplina'
    verbose_name_plural = 'Discipline'

class AuthoringSoftware(models.Model):
  name = models.CharField(max_length=80, verbose_name="nome")
  version = models.CharField(max_length=150, blank=True, null=True, verbose_name="versione")

  def __str__(self):
    return f'{self.name} - {self.version}'
  
  class Meta:
    verbose_name = 'Software di Authoring'
    verbose_name_plural = 'Software di Authoring'

class LodReference(models.Model):
  name = models.CharField(max_length=80, verbose_name="nome")
  description = models.CharField(max_length=150, blank=True, null=True, verbose_name="descrizione")

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Scheda LOD'
    verbose_name_plural = 'Schede LOD'

class BimSpecification(models.Model):
  name = models.CharField(max_length=80, verbose_name="nome")
  description = models.CharField(max_length=150, blank=True, null=True, verbose_name="descrizione")

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Specifica coordinamento/verifica'
    verbose_name_plural = 'Specifiche coordinamento/verifica'

class BimExpert(models.Model):
  name = models.CharField(max_length=80, verbose_name="nome")
  position = models.CharField(max_length=80, blank=True, null=True, verbose_name="qualifica")

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Professionista'
    verbose_name_plural = 'Professionisti'