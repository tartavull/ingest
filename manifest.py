import json
import os
with open('./tmp/0-1024_0-1024_0-100.npz.manifest.json') as f:
  ids = json.load(f)

for _id in ids:

  filepath = os.path.join('./tmp/{}:0'.format(_id))
  fragjson =  json.dumps({ 
    "fragments": ['{}:{}:{}'.format(_id, 0, '0-1024_0-1024_0-100.npz')],
  })

  with open(filepath, 'w') as f:
    f.write(fragjson) 
