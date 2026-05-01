from django.db import models

# Create your models here.
class OrganizationEntity(models.Model):
  name = models.CharField(max_length=80, verbose_name="nome")
  description = models.CharField(max_length=150, blank=True, null=True, verbose_name="descrizione")

  def __str__(self):
    return self.name

  class Meta:
    abstract = True

class ProjectPhase(OrganizationEntity): 
  class Meta:
    verbose_name = 'Fase progetto'
    verbose_name_plural = 'Fasi progetto'

class Discipline(OrganizationEntity):
  class Meta:
    verbose_name = 'Disciplina'
    verbose_name_plural = 'Discipline'

class AuthoringSoftware(OrganizationEntity): 
  class Meta:
    verbose_name = 'Software di Authoring'
    verbose_name_plural = 'Software di Authoring'

class LodReference(OrganizationEntity):
  class Meta:
    verbose_name = 'Scheda LOD'
    verbose_name_plural = 'Schede LOD'

class BimSpecification(OrganizationEntity): 
  class Meta:
    verbose_name = 'Specifica coordinamento/verifica'
    verbose_name_plural = 'Specifiche coordinamento/verifica'

class BimExpert(OrganizationEntity): 
  class Meta:
    verbose_name = 'Professionista'
    verbose_name_plural = 'Professionisti'