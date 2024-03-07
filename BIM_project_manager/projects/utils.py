from django.http import HttpResponse

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
  response = HttpResponse(content_type='text/plain')  
  response['Content-Disposition'] = f'attachment; filename="Project_Info_Sheets_{project.name}.txt"'
  response.write(f'Tutte le schede informative dei modelli per il progetto: {project.name}')
  return response

def create_model_info_sheets(model):
  response = HttpResponse(content_type='text/plain')  
  response['Content-Disposition'] = f'attachment; filename="{model.name}_Info_Sheets.txt"'
  response.write(f'Tutte le schede informative per il modello BIM: {model.name}')
  return response

