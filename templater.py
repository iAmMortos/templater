
from templater.utils.properties_file import PropertiesFile
from templater.utils.class_utils import fully_qualified_name
from templater.template_manager import TemplateManager
from templater.tokens.tokenizer import Tokenizer
from templater.utils import obj_utils


class Templater (object):
  SELFREF = 'this'
  def __init__(self, output_type, token_config_path='templater/config/token.properties', template_config_path='templater/config/template.properties'):
    self.output_type = output_type
    self.template_manager = TemplateManager(self.output_type)
    self.tokenizer = Tokenizer(token_config_path)
    self.template_properties = PropertiesFile(template_config_path)

  def make(self, o, template_str=None):
    output = ''
    # If template_str is not provided, attempt to look up from class of given object
    template_name = template_str
    if not template_name:
      obj_clazz = fully_qualified_name(o)
      template_name = self.template_properties.get(obj_clazz)
      if not template_name:
        raise Exception(f"No valid template found for template [{template_name}]")
    template = self.template_manager.get_template(template_name)
    tokens = self.tokenizer.tokenize(template)

    pending_line_removal = False
    for token in tokens:
      if type(token) is str:  # is a raw string straight from the template
        if pending_line_removal:
          if len(output) > 0 and output.endswith('\n'):
            output = output[:-1]
        pending_line_removal = False
        output += token
      else:
            # Treat evey token as if it represents a list
        token_strs = []  # The string return value the given token represents
        
        objs = []  # represent the object(s) receieved by doing a lookup on the token's reference
        if token.valueref == Templater.SELFREF:
          objs = [o]
        else:
          ob = obj_utils.get_value(o, token.valueref)
          objs = ob if type(ob) is list else [ob]
    
        # Whether the token's value is ultimately null or not
        # (including empty lists and strings)    
        value_isnull = True
        for ob in objs:
          if ob:
            value_isnull = False
            break
        
        # Handle null value or empty lists/strings.
        if value_isnull:
          if token.nullval:
            token_strs.append(token.nullval)
          elif token.optline:
            if len(output) > 0 and output.endswith('\n'):
              output = output[:-1]
              pending_line_removal = False
            else:
              pending_line_removal = True
        elif not value_isnull and token.nonnullval:
          token_strs.append(token.nonnullval)
        # token is Token object
        # resolve the value lookup
          # determine type: simple string? object? list?
        elif token.template:
          # TODO: add support for regex templates
          for ob in objs:
            token_strs.append(self.make(ob, token.template))        
        else:
          for ob in objs:
            token_strs.append(str(ob))
                
            # determine visibility
              # if not visible, check if optline
            # determine text value
              # if template reference, recursively resolve string before continuing
              # add prefix, suffix
              # if list, use specified delimiter
    
        # Add prefix and suffix
        if len(token_strs) > 0:
          v = token.prefix.encode('utf-8').decode('unicode_escape') + token.delimiter.encode('utf-8').decode('unicode_escape').join(token_strs) + token.suffix.encode('utf-8').decode('unicode_escape')
          output += v
        # otherwise, nothing to append, continue
    return output  # obj_utils.get_value(template, o)

  '''
  o - The object from which we're pulling our values
  token - The token object from the tokenizer
  output - The string we're appending to that will be returned by the "make" function
  pending_line_removal - A boolean value to pass back and forth for this specific call of the "make" function. 
    used to support the optline feature
  '''
#   def _handle_token_obj(self, o, token, output, pending_line_removal):
        
