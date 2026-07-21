#!/usr/bin/env python

import os; import nbformat; import sys

filename = sys.argv[-1]

assert os.path.exists(filename)
txt = ''
with open(filename, 'rb') as nb_file:
  txt = nb_file.read()

nb_node = nbformat.reads(txt, nbformat.NO_CONVERT)

for cell in nb_node['cells']:
  if 'code' == cell['cell_type']:
    if 'execution_count' in cell:
      cell['execution_count'] = None
    if 'outputs' in cell:
      outputs = cell['outputs']
      for i, output in enumerate(outputs):
        if 'name' in outputs[i]:
          if 'stderr' == outputs[i]['name']:
            if 'text' in outputs[i]:
              del cell['outputs'][i]

nbformat.write(nb_node, filename)







