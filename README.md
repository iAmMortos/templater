# Python Templater
A flexible python library for turning python objects into formatted text output using customized templates.

The possible output format and templates are provided by the user, so any output format is possible.

Templates are plain-text documents that contain configurable placeholder tokens that can represent values within a given python object, repeating sections like sub-objects in a list, or even other templates.

The tokens can also be configured to use different delimiters so they don't conflict with the desired output format.

## Usage
Once our templates and configurations are in place, converting an object is as simple as the following snippet. Assume we have a python object that represents a D&D monster and we want that monster turned into a nice block of formatted Markdown text:

```py
from templater import Templater

# Specify the desired output format
tmpltr = Templater('markdown')
monster_md = tmpltr.make(monster_obj)
```