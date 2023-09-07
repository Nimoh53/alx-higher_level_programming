#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        print(f"{count}: {sys.argv[count]}")
    else:
        print("{} arguments:".format(count))
        for i, name in enumerate(sys.argv):
            if i == 0:
                continue
            print(f"{i}: {name}")
