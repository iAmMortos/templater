
def get_value(obj, attr):
  attrs = []
  if type(attr) is list:
    attrs = attr
  elif type(attr) is str:
    attrs = attr.split('.')
    
  nxt = attrs[0]
  if nxt not in vars(obj):
    return None
    
  if len(attrs) == 1:
    return vars(obj)[nxt]
  else:
    o = vars(obj)[nxt]
    return get_value(o, attrs[1:])
  
