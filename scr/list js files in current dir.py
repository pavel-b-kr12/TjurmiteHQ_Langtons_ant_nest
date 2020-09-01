import os
import re

from os.path import dirname, abspath
for root, dirs, files in os.walk('.'):#/mydir
    for file in files:
        if file.endswith((".png",".jpg")):
            #print(root)
            if 'src' in root:
                continue
            s=os.path.basename(os.getcwd())+os.path.join(root, file)[1:]
            #re.escape(s)
            s=s.replace('\\', '\\\\')
            print("'"+s+"',")
#__file__
#os.getcwdb()
#'.'
#dirname(dirname(abspath(__file__)))
#dirname(abspath('.'))
