#Scanner.py
#Can accept arguments: -h:help, -v:version, -b:verbose

import sys

if sys.argv[1] == "-v":
    print("Version 1.0")
elif sys.argv[1] == "-h":
    print("""
    Scanner.py <option>
    
      -s, scan
      -r, report
      -v, version
      -h, help
    """)
