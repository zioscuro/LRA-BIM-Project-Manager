from django.contrib import admin
from .models import ProjectPhase, Discipline, AuthoringSoftware, LodReference, BimSpecification, BimExpert

# Register your models here.

admin.site.register(ProjectPhase)
admin.site.register(Discipline)
admin.site.register(AuthoringSoftware)
admin.site.register(LodReference)
admin.site.register(BimSpecification)
admin.site.register(BimExpert)