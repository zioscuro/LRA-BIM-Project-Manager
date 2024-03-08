from django.http import HttpResponse
from .models import InfoSheet, Report

def create_model_register(project):
  bim_models = project.bim_models.all()

  response = HttpResponse(content_type='text/plain')  
  response['Content-Disposition'] = f'attachment; filename="Model_Register_{project.name}.txt"'  
  response.write(f'Registro modelli - Progetto: {project.name}\n')
  response.write(f'n. - Nome - Disciplina - Progettista\n')

  for count, model in enumerate(bim_models):
    response.write(f'{count+1} - {model.name} - {model.discipline} - {model.designer}\n')

  return response

def create_project_info_sheets(project):
  bim_models = project.bim_models.all()

  response = HttpResponse(content_type='text/plain')  
  response['Content-Disposition'] = f'attachment; filename="Project_Info_Sheets_{project.name}.txt"'
  response.write(f'Schede informative - Progetto: {project.name}')

  for count, model in enumerate(bim_models):
    response.write(f'Modello n.{count+1} - {model.name} - {model.discipline} - {model.designer}\n')

    info_sheets = model.info_sheets.all()

    for count, sheet in enumerate(info_sheets):
      response.write(f'\tScheda n.{count+1} - {sheet.name} - {sheet.description} - {sheet.sheet_type}\n')   

  return response

def create_model_info_sheets(model):
  info_sheets = model.info_sheets.all()

  response = HttpResponse(content_type='text/plain')  
  response['Content-Disposition'] = f'attachment; filename="{model.name}_Info_Sheets.txt"'
  response.write(f'Schede informative - Modello: {model.name}')

  for count, sheet in enumerate(info_sheets):
    response.write(f'Scheda n.{count+1} - {sheet.name} - {sheet.description} - {sheet.sheet_type}\n')
    
    reports = sheet.reports.all()
    
    for count, report in enumerate(reports):
      response.write(f'\tReport n.{count+1} - {report.name} - {report.description} - {sheet.sheet_type}\n')

      if sheet.sheet_type == 'coordination':
        tests = report.clash_tests.all()
        response.write('\t\tTest Interferenze\n')
        response.write('\t\tData - Commenti - Nuove - Attive - Revisionate - Approvate - Risolte\n')

        for test in tests:
          response.write(f'\t\t{test.date.strftime("%m/%d/%Y")} - {test.comments} - {test.clash_new} - {test.clash_active} - {test.clash_reviewed} - {test.clash_approved} - {test.clash_resolved}\n')

      if sheet.sheet_type == 'validation':
        tests = report.validation_tests.all()
        response.write('\t\tTest Verifica\n')
        response.write('\t\tData - Commenti - Specifica - Difformità\n')

        for test in tests:
          response.write(f'\t\t{test.date.strftime("%m/%d/%Y")} - {test.comments} - {test.specification} - {test.issues}\n')

  return response

def set_default_coordination(model):
  sheet_LC1 = InfoSheet(
    sheet_type = 'coordination',
    name = 'LC1',
    description = 'default coordinamento',
    bim_model = model
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
  

def set_default_validation(model):
  sheet_LV1 = InfoSheet(
    sheet_type ='validation',
    name = 'LV1',
    description = 'default verifica',
    bim_model = model
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


