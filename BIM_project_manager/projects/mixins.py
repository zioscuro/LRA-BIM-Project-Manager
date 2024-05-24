from django.views.generic.edit import SingleObjectMixin

from core.mixins import StaffMixin
from projects.models import BimProject, BimModel, InfoSheet, Report, ClashTest, ValidationTest

class BimProjectViewMixin(StaffMixin, SingleObjectMixin):
    model = BimProject

class BimModelViewMixin(StaffMixin, SingleObjectMixin):
    model = BimModel

class InfoSheetViewMixin(StaffMixin, SingleObjectMixin):
    model = InfoSheet

class ReportViewMixin(StaffMixin, SingleObjectMixin):
    model = Report

class ClashTestViewMixin(StaffMixin, SingleObjectMixin):
    model = ClashTest

class ValidationViewMixin(StaffMixin, SingleObjectMixin):
    model = ValidationTest
