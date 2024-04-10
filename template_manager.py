
import os


class TemplateManager (object):
  # knows what kind of templates there are, how to find them.
  def __init__(self, template_type, template_dir='templater/templates'):
    self.template_dir = os.path.abspath(template_dir)
    self.type = template_type

  def template_for(self, o):
    type(o)

  def get_template(self, template_name, temp_type=None):
    t = temp_type if temp_type is not None else self.type
    type_dir = os.path.join(self.template_dir, t)
    templates = os.listdir(type_dir)
    for temp in templates:
      if temp.split('.')[0] == template_name:
        path = os.path.join(type_dir, temp)
        with open(path) as f:
          return f.read().strip()
    # no template found
    raise FileNotFoundError(f"No template found for output type [{t}], and template [{template_name}].")

