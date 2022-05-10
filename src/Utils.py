from pathlib import Path

def get_project_root() -> Path:
  return Path(__file__).parent.parent

def null(input):
  if type(input) == str:
    if input:
      return f'\'{input}\''
    else:
      return 'NULL'
  if type(input) == int:
    return input or 'NULL'