from django.contrib import admin
from .models import Project, BimModel, InfoSheet, Report, ClashTest, ValidationTest

# Register your models here.

admin.site .register(Project)
admin.site .register(BimModel)
admin.site .register(InfoSheet)
admin.site .register(Report)
admin.site .register(ClashTest)
admin.site .register(ValidationTest)