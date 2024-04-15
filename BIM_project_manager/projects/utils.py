from django.http import HttpResponse
from .models import InfoSheet, Report
from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font

def create_model_register_file(bim_project):
  '''
  create an excel file export with the model register with all the BIM model of a specific project
  '''
  bim_models = bim_project.bim_models.all()

  wb = Workbook()
  wb.remove(wb.active)  
  ws = wb.create_sheet(title='Model-Register')

  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
  response['Content-Disposition'] = f'attachment; filename="Model_Register_{bim_project.name}.xlsx"'

  ws.append([f'Registro modelli - Progetto: {bim_project.name}'])
  ws.append(['n.', 'Nome modello', 'Disciplina', 'Progettista'])

  for count, model in enumerate(bim_models):
   ws.append([count+1, model.name, model.discipline, model.designer])

  wb.save(response)

  return response

def create_project_info_sheets_file(bim_project):
  '''
  create an excel file export with all the info sheets of the project divided by BIM model
  '''
  bim_models = bim_project.bim_models.all()

  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  
  response['Content-Disposition'] = f'attachment; filename="Project_Info_Sheets_{bim_project.name}.xlsx"'

  wb = Workbook(write_only=True)  
  for count, model in enumerate(bim_models):    
    ws = wb.create_sheet(model.name)
    ws.append([f'Schede Informative Modello: {model.name}'])
    ws.append(['n.','Nome Scheda', 'Descrizione Scheda', 'Tipo Scheda'])

    info_sheets = model.info_sheets.all()
    for count, sheet in enumerate(info_sheets):
      ws.append([count+1, sheet.name, sheet.description, sheet.sheet_type])   

  wb.save(response)

  return response

def create_model_info_sheets_file(bim_model):
  '''
  create an excel file export with all the info sheets of a specific BIM model
  '''
  info_sheets = bim_model.info_sheets.all()

  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  
  response['Content-Disposition'] = f'attachment; filename="{bim_model.name}_Info_Sheets.xlsx"'
  
  wb = Workbook(write_only=True)  

  for count, sheet in enumerate(info_sheets):
    ws = wb.create_sheet(sheet.name)

    ws.append(['DATI MODELLO BIM'])
    ws.append(['nome modello', bim_model.name])
    ws.append(['disciplina', bim_model.discipline])
    ws.append(['Autore', bim_model.designer])
    ws.append(['Software', bim_model.authoringSoftware])
    ws.append(['Scheda LOD', bim_model.lodReference])
    ws.append([])
    ws.append(['DATI SCHEDA INFORMATIVA'])
    ws.append(['nome scheda', sheet.name])
    ws.append(['descrizione scheda', sheet.description])
    ws.append(['tipo scheda', sheet.sheet_type])
    ws.append([])
    
    reports = sheet.reports.all()    
    for count, report in enumerate(reports):
      ws.append([f'Report n.{count+1} - {report.name} - {report.description}'])

      if sheet.sheet_type == 'coordination':
        tests = report.clash_tests.all()
        ws.append(['Data', 'Commenti', 'Nuove', 'Attive', 'Revisionate', 'Approvate', 'Risolte'])

        for test in tests:
          ws.append([test.date.strftime("%m/%d/%Y"), test.comments, test.clash_new, test.clash_active, test.clash_reviewed, test.clash_approved, test.clash_resolved])

      if sheet.sheet_type == 'validation':
        tests = report.validation_tests.all()
        ws.append(['Data', 'Commenti', 'Specifica', 'Difformità'])

        for test in tests:
          ws.append([test.date.strftime("%m/%d/%Y"), test.comments, test.specification, test.issues])

  wb.save(response)
  
  return response

def set_default_coordination(bim_model):
  '''
  create in a specific BIM model a default set of coordination info sheets ad related reports
  '''
  sheet_LC1 = InfoSheet(
    sheet_type = 'coordination',
    name = 'LC1',
    description = 'default coordinamento',
    bim_model = bim_model
  )
  sheet_LC1.save()

  duplicates_report = Report(
    name = 'duplicati',
    description = 'default report elementi duplicati',
    info_sheet = sheet_LC1,
  )
  duplicates_report.save()

  intersections_report = Report(
    name = 'intersezioni',
    description = 'default report elementi intersecanti',
    info_sheet = sheet_LC1,
  )
  intersections_report.save()

def set_default_validation(bim_model):
  '''
  create in a specific BIM model a default set of validation info sheets ad related reports
  '''
  sheet_LV1 = InfoSheet(
    sheet_type ='validation',
    name = 'LV1',
    description = 'default verifica',
    bim_model = bim_model
  )
  sheet_LV1.save()

  file_name_report = Report(
    name = 'nomenclatura file modello',
    description = 'default report nomenclatura file',
    info_sheet = sheet_LV1,
  )
  file_name_report.save()

  objects_name_report = Report(
    name = 'nomenclatura oggetti',
    description = 'default report nomenclatura oggetti nel modello',
    info_sheet = sheet_LV1,
  )
  objects_name_report.save()
