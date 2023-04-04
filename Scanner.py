#python3 Scanner.py
#Can accept arguments: -h:help, -v:version, -r:report

import sys
from Function import *

n = len(sys.argv)
if n<2:
    print("No options selected")
elif sys.argv[1] == "-v":
    print("Version 1.0")
elif sys.argv[1] == "-h":
    print("""
    Scanner.py <option>
    
      -r, report
      -v, version
      -h, help
    """)
elif sys.argv[1] == "-r":
    #call scan function
    Untar("/usr/local/NCRSystemLog_2022-09-05T1658+0800.tar.gz")
else:
    print("Incorrect option selected")


