from django.http import HttpResponse
from .models import InfoSheet, Report
from openpyxl import Workbook
from openpyxl.styles import NamedStyle, Font, Border, Side, Alignment, PatternFill

def create_model_register_file(bim_project):
  '''
  create an excel file export with the model register with all the BIM model of a specific project
  '''
  bim_models = bim_project.bim_models.all()

  thin_line = Side(border_style="thin", color="000000")

  title_style = NamedStyle(name="title")
  title_style.font = Font(bold=True)
  title_style.alignment = Alignment(horizontal='center')
  title_style.fill = PatternFill(start_color='C0C0C0', end_color='C0C0C0', fill_type = "solid")
  title_style.border = Border(top=thin_line, left=thin_line, right=thin_line, bottom=thin_line)

  header_style = NamedStyle(name="header")
  header_style.font = Font(bold=True)
  header_style.border = Border(top=thin_line, left=thin_line, right=thin_line, bottom=thin_line)

  standard_cell_style = NamedStyle(name="standard cell")
  standard_cell_style.border = Border(top=thin_line, left=thin_line, right=thin_line, bottom=thin_line)

  wb = Workbook()
  wb.remove(wb.active)  
  ws = wb.create_sheet(title='Model-Register')

  ws.column_dimensions['A'].width = 5
  ws.column_dimensions['B'].width = 20
  ws.column_dimensions['C'].width = 15
  ws.column_dimensions['D'].width = 15
  ws.column_dimensions['E'].width = 15
  ws.column_dimensions['F'].width = 15

  ws['A1'] = f'Registro modelli - Progetto: {bim_project.name}'
  ws['A1'].style = title_style
  ws.row_dimensions[1].height = 20
  ws.merge_cells('A1:F1')

  ws['A2'] = 'n.'
  ws['A2'].style = header_style

  ws['B2'] = 'Nome modello'
  ws['B2'].style = header_style

  ws['C2'] = 'Disciplina'
  ws['C2'].style = header_style

  ws['D2'] = 'Software'
  ws['D2'].style = header_style

  ws['E2'] = 'Scheda LOD'
  ws['E2'].style = header_style

  ws['F2'] = 'Progettista'
  ws['F2'].style = header_style

  ws.row_dimensions[2].height = 20

  for count, bim_model in enumerate(bim_models):
   ws.append([count+1, bim_model.name, bim_model.discipline, bim_model.authoringSoftware, bim_model.lodReference, bim_model.designer])
   ws.row_dimensions[count+3].height = 20

   for cell in ws[ws.max_row]:
     cell.style = standard_cell_style

  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
  response['Content-Disposition'] = f'attachment; filename="Model_Register_{bim_project.name}.xlsx"'
  wb.save(response)

  return response

def create_project_info_sheets_file(bim_project):
  '''
  create an excel file export with all the info sheets of the project divided by BIM model
  '''
  bim_models = bim_project.bim_models.all()

  thin_line = Side(border_style="thin", color="000000")
  
  title_style = NamedStyle(name="title")
  title_style.font = Font(bold=True)
  title_style.alignment = Alignment(horizontal='center')
  title_style.fill = PatternFill(start_color='C0C0C0', end_color='C0C0C0', fill_type = "solid")

  header_style = NamedStyle(name="header")
  header_style.font = Font(bold=True)
  header_style.border = Border(top=thin_line, left=thin_line, right=thin_line, bottom=thin_line)

  standard_cell_style = NamedStyle(name="standard cell")
  standard_cell_style.border = Border(top=thin_line, left=thin_line, right=thin_line, bottom=thin_line)

  wb = Workbook()
  wb.remove(wb.active)

  for count, bim_model in enumerate(bim_models):    
    ws = wb.create_sheet(title=bim_model.name)

    ws.column_dimensions['A'].width = 5
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 25
    ws.column_dimensions['D'].width = 15
    
    ws['A1'] = f'Schede Informative modello: {bim_model.name}'
    ws['A1'].style = title_style
    ws.row_dimensions[1].height = 20
    ws.merge_cells('A1:D1')

    ws['A2'] = 'n.'
    ws['A2'].style = header_style

    ws['B2'] = 'Nome Scheda'
    ws['B2'].style = header_style

    ws['C2'] = 'Descrizione Scheda'
    ws['C2'].style = header_style

    ws['D2'] = 'Tipo Scheda'
    ws['D2'].style = header_style

    ws.row_dimensions[2].height = 20

    info_sheets = bim_model.info_sheets.all()
    
    for count, sheet in enumerate(info_sheets):
      ws.append([count+1, sheet.name, sheet.description, sheet.sheet_type])

      for cell in ws[ws.max_row]: 
        cell.style = standard_cell_style

  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  
  response['Content-Disposition'] = f'attachment; filename="Project_Info_Sheets_{bim_project.name}.xlsx"'
  wb.save(response)

  return response

def create_model_info_sheets_file(bim_model):
  '''
  create an excel file export with all the info sheets of a specific BIM model
  '''
  info_sheets = bim_model.info_sheets.all()

  thin = Side(border_style="thin", color="000000")

  model_header_style = NamedStyle(name="model header")
  model_header_style.font = Font(bold=True)
  model_header_style.fill = PatternFill(start_color='ddebf7', end_color='ddebf7', fill_type = "solid")
  model_header_style.border = Border(top=thin, left=thin, right=thin, bottom=thin) 

  info_header_style = NamedStyle(name="info header")
  info_header_style.font = Font(bold=True)
  info_header_style.fill = PatternFill(start_color='ffe699', end_color='ffe699', fill_type = "solid")
  info_header_style.border = Border(top=thin, left=thin, right=thin, bottom=thin) 

  report_header_style = NamedStyle(name="report header")
  report_header_style.font = Font(bold=True)
  report_header_style.fill = PatternFill(start_color='f8cbad', end_color='f8cbad', fill_type = "solid")
  report_header_style.border = Border(top=thin, left=thin, right=thin, bottom=thin) 
  report_header_style.alignment = Alignment(textRotation=90, wrap_text=True, horizontal='center', vertical='center')

  standard_cell_style = NamedStyle(name="standard cell")
  standard_cell_style.border = Border(top=thin, left=thin, right=thin, bottom=thin)

  wb = Workbook()
  wb.remove(wb.active)

  for sheet in info_sheets:
    ws = wb.create_sheet(sheet.name)

    ws.column_dimensions['A'].width = 5
    ws.column_dimensions['B'].width = 25
    ws.column_dimensions['C'].width = 50
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15
    ws.column_dimensions['G'].width = 15
    ws.column_dimensions['H'].width = 15

    ws['A1'] = 'DATI MODELLO'
    ws['A1'].style = model_header_style
    ws['A1'].alignment = Alignment(textRotation=90, wrap_text=True, horizontal='center', vertical='center')
    ws.merge_cells('A1:A5')

    ws['B1'] = 'Nome Modello'
    ws['B1'].style = model_header_style
    ws['C1'] = bim_model.name
    ws['C1'].style = standard_cell_style

    ws['B2'] = 'Disciplina'
    ws['B2'].style = model_header_style
    ws['C2'] = bim_model.discipline
    ws['C2'].style = standard_cell_style

    ws['B3'] = 'Progettista'
    ws['B3'].style = model_header_style
    ws['C3'] = bim_model.designer
    ws['C3'].style = standard_cell_style

    ws['B4'] = 'Software BIM Authoring'
    ws['B4'].style = model_header_style
    ws['C4'] = bim_model.authoringSoftware
    ws['C4'].style = standard_cell_style

    ws['B5'] = 'LOD di riferimento'
    ws['B5'].style = model_header_style
    ws['C5'] = bim_model.lodReference
    ws['C5'].style = standard_cell_style    

    ws['A6'] = 'DATI SCHEDA'
    ws['A6'].style = info_header_style
    ws['A6'].alignment = Alignment(textRotation=90, wrap_text=True, horizontal='center', vertical='center')
    ws.merge_cells('A6:A8')

    ws['B6'] = 'Nome Scheda Informativa'
    ws['B6'].style = info_header_style
    ws['C6'] = sheet.name
    ws['C6'].style = standard_cell_style

    ws['B7'] = 'Descrizione Scheda'
    ws['B7'].style = info_header_style
    ws['C7'] = sheet.description
    ws['C7'].style = standard_cell_style

    ws['B8'] = 'Tipo Scheda'
    ws['B8'].style = info_header_style
    ws['C8'] = sheet.sheet_type
    ws['C8'].style = standard_cell_style
    
    ws.append([])
    
    reports = sheet.reports.all()    
    for report in reports:
      if sheet.sheet_type == 'coordination':
        ws.append(['', 'Nome Report', report.name])
        for cell in ws[ws.max_row]:
          cell.style = standard_cell_style
          cell.font = Font(bold=True)
        ws.merge_cells(f'C{ws.max_row}:H{ws.max_row}')         

        ws.append(['', 'Oggetto/Specifica Report', report.description])
        for cell in ws[ws.max_row]:
          cell.style = standard_cell_style
        ws.merge_cells(f'C{ws.max_row}:H{ws.max_row}')
        
        ws.append(['', 'Data', 'Commenti', 'Nuove', 'Attive', 'Revisionate', 'Approvate', 'Risolte'])

        for cell in ws[ws.max_row]: 
          cell.style = standard_cell_style        
        
        tests = report.clash_tests.all()

        for test in tests:
          ws.append(['',test.date.strftime("%m/%d/%Y"), test.comments, test.clash_new, test.clash_active, test.clash_reviewed, test.clash_approved, test.clash_resolved])
          
          for cell in ws[ws.max_row]: 
            cell.style = standard_cell_style
        
        ws.append([])

      if sheet.sheet_type == 'validation':
        ws.append(['', 'Nome Report', report.name])
        for cell in ws[ws.max_row]:
          cell.style = standard_cell_style
          cell.font = Font(bold=True)
        ws.merge_cells(f'C{ws.max_row}:F{ws.max_row}')         

        ws.append(['', 'Oggetto/Specifica Report', report.description])
        for cell in ws[ws.max_row]:
          cell.style = standard_cell_style
        ws.merge_cells(f'C{ws.max_row}:F{ws.max_row}')

        for cell in ws[ws.max_row]: 
          cell.style = standard_cell_style
          
        tests = report.validation_tests.all()
        ws.append(['','Data', 'Commenti', 'Specifica', 'Difformità', 'Allegati'])

        for cell in ws[ws.max_row]: 
          cell.style = standard_cell_style   

        for test in tests:
          ws.append(['', test.date.strftime("%m/%d/%Y"), test.comments, test.specification, test.issues, ''])

          for cell in ws[ws.max_row]: 
            cell.style = standard_cell_style          
        
        ws.append([])

    ws['A10'] = 'ATTIVITA\' REPORT'
    ws['A10'].style = report_header_style
    ws.merge_cells(f'A10:A{ws.max_row}')    

  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  
  response['Content-Disposition'] = f'attachment; filename="{bim_model.name}_Info_Sheets.xlsx"'
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
