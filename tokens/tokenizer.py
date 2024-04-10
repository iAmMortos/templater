
from templater.tokens.token import Token
from templater.tokens.tokenizing_error import TokenizingError


class Tokenizer (object):
  def __init__(self, token_config):
    # The default token configuration to use
    self.token_config = token_config
    
  def tokenize(self, s, temp_token_config=None):
    # load the token configuration from the given path or default to 
    token_config = temp_token_config if temp_token_config else self.token_config
    out = []
    rs = s
    open = False
    while len(rs) > 0:
      if not open:
        i = rs.find(token_config.token_start)
        if i >= 0:
          if i > 0:
            out.append(rs[:i])
          rs = rs[i+len(token_config.token_start):]
          open = True
        else:
          out.append(rs)
          rs = ''
      else:
        i = rs.find(token_config.token_end)
        if i >= 0:
          token = self._parse_token_content(rs[:i], token_config)
          out += [token]
          rs = rs[i + len(token_config.token_end):]
          open = False
        else:
          raise TokenizingError("Unclosed Token")
    return out

  def _parse_token_content(self, s, token_config):
    parts = s.split(token_config.token_delimiter)
    value = parts[0]
    flags = {}
    for part in parts[1:]:
      if token_config.token_flag_setter in part:
        ps = part.split(token_config.token_flag_setter)
        key = ps[0]
        val = token_config.token_flag_setter.join(ps[1:])
        # TODO: will run into problems if different variations of the same key are used within one token
        #   e.g. 'regextemp' and 'rtemp'
        #   Could fix in Token object and how flag values are retrieved
        if key in flags:
          if type(flags[key] is not list):
            flags[key] = [flags[key]]
          flags[key].append(val)
        else:
          flags[key] = val
      else:
        flags[part] = None
    return Token(value, flags)

if __name__ == '__main__':
  pass
  
