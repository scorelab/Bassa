#!flask/bin/python
from REST import *
from Worker import *


def main():
    server.run(debug=True)


if __name__ == '__main__':
    main()

