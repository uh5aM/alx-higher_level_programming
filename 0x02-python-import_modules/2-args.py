#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1
    if i==0:
        print("{} argumant.".format(i))
    elif i==1:
        print("{} argument:".format(i))
    else:
        print("{} argument:".format(i))

        if i >=0:
            i=0
            for arg insys.argv:
                if i !=0:
                    print("{}: {}".format(i, arg))
                i += 1
