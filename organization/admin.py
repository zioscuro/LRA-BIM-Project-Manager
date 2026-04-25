from django.contrib import admin
from .models import  AuthoringSoftware, BimExpert, BimSpecification, Discipline, LodReference, ProjectPhase

# Register your models here.

admin.site.register(ProjectPhase)
admin.site.register(Discipline)
admin.site.register(AuthoringSoftware)
admin.site.register(LodReference)
admin.site.register(BimSpecification)
admin.site.register(BimExpert)