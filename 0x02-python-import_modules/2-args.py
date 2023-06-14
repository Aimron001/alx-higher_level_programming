#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) == 1):
        print("0 arguments.")
    else:
        print("{} arguements:".format(len(sys.argv)-1))
    for i in range(len(sys.argv)):
            if i == 0:
                continue
            else:
                print("{}: {}".format(i,sys.argv[i]))
