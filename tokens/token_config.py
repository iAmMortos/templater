
from templater.utils.properties_file import PropertiesFile


class TokenConfig (object):
  def __init__(self, path):
    props = PropertiesFile(path)
    self.token_start = props.get('start', default='{')
    self.token_end = props.get('end', default='}')
    self.token_delimiter = props.get('delimiter', default='|')
    self.token_flag_setter = props.get('flag_setter', default=':')
    self.token_self_ref_keyword = props.get('self_ref_keyword', default='this')
