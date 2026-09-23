import sys
if len(sys.argv) > 1:
    print("parameters:", len(sys.argv) - 1)
    for arg in sys.argv[1:]:
        print(arg + ":", len(arg))
else:
    print("none")