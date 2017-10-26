import sys

def main():
    print('first module name: {}'.format(__name__))
    sys.platform

if __name__ == '__main__':
    main()