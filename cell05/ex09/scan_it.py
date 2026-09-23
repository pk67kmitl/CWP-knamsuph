import sys
import re
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    string = sys.argv[2]
    result = re.findall(keyword, string)
    if len(result) > 0:
        print(len(result))
    else:
        print("none")
else:
    print("none")