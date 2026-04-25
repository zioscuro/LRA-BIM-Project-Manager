from django.contrib import admin
from .models import BimProject, BimModel, InfoSheet, Report, ClashTest, ValidationTest

# Register your models here.

admin.site.register(BimProject)
admin.site.register(BimModel)
admin.site.register(InfoSheet)
admin.site.register(Report)
admin.site.register(ClashTest)
admin.site.register(ValidationTest)