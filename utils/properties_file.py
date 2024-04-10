
import os


class PropertiesFile (object):
  def __init__(self, path):
    DEFAULT_NAME = 'application.properties'
    self.properties = {}
    self.path = os.path.abspath(path)
    self.file = None
    if os.path.exists(self.path):
      if os.path.isdir(self.path):
        self.path = f'{self.path}{os.sep}{DEFAULT_NAME}'
        if not os.path.exists(self.path):
          with open(self.path, 'w') as f:
            f.write('')
      elif not os.path.isfile(self.path):
        raise Exception(f'given path [{self.path}] must terminate at a file.')
    else:
      pdir = os.path.dirname(self.path)
      pbase = os.path.basename(self.path)
      if '.' not in pbase:
        pdir = f'{pdir}{os.sep}{pbase}'
        pbase = DEFAULT_NAME
      self.path = f'{pdir}{os.sep}{pbase}'
      os.makedirs(pdir)
      if not os.path.exists(self.path):
        with open(self.path, 'w') as f:
          f.write('')

    with open(self.path) as f:
      lines = f.read().split('\n')
    for line in lines:
      if not line.strip().startswith('#') and not line.strip() == '':
        if '=' not in line:
          raise Exception(f"Improperly formatted property line: [{line}]")
        parts = line.split('=')
        key = parts[0]
        value = '='.join(parts[1:])
        self.properties[key] = value

  def get(self, key):
    if key in self.properties:
      return self.properties[key]
    else:
      return None

  def set(self, key, value):
    self.properties[key] = value
    self._write()

  def _write(self):
    with open(self.path, 'w') as f:
      f.write(str(self))
      
  def __repr__(self):
    return '\n'.join([f'{k}={self.properties[k]}' for k in self.properties.keys()])
    

