import sys

if len(sys.argv) >= 3:
    for arg in sys.argv[:0:-1]:
        print(arg)
else:
    print("none")