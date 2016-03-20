#!flask/bin/python
from REST import *
import logging


def main():
    server.run(debug=True)


if __name__ == '__main__':
    logging.basicConfig(filename="./debug-server.log", level=logging.DEBUG)
    logging.warning("INFO: Bassa starting")
    main()
