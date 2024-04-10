

class Token (object):
  def __init__(self, valueref, flags):
    self.valueref = valueref
    self.prefix = self._set_flag(flags, ['prefix', 'pref', 'p'], '')
    self.suffix = self._set_flag(flags, ['suffix', 'suff', 's'], '')
    self.delimiter = self._set_flag(flags, ['delimiter', 'del', 'd'], ', ')
    self.template = self._set_flag(flags, ['template', 'temp', 't'])
    self.optline = self._set_bool_flag(flags, ['optline', 'o'])
    self.showif = self._set_flag(flags, ['showif', 'if'])
    self.nullval = self._set_flag(flags, ['nullval', 'nv'])
    self.nonnullval = self._set_flag(flags, ['nonnullval', 'nnv'])
    self.regextemplate = self._set_flag(flags, ['regextemplate', 'rtemp', 'rt'])

  def _set_flag(self, flags, keys, default_val=None):
    for key in keys:
      if key in flags:
        return flags[key]
    return default_val
    
  def _set_bool_flag(self, flags, keys):
    for key in keys:
      if key in flags:
        return True
    return False

  @property
  def is_visible(self):
    return self.value != ''
    
  @property
  def is_reference(self):
    return self.template or self.regextemplate
  
