import sys

def main():
    a = []
    a.append(2)
    a.append(3)
    call(a)
    print a

def call(b):
    b.append(5)

if __name__ == '__main__':
    main()