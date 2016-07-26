#!flask/bin/python

from REST import *
from ConfReader import check_conf_availability
import logging


def main():
    socketio.run(server)
    # server.run(debug=True)


if __name__ == '__main__':
    logging.basicConfig(filename="./debug-server.log", level=logging.DEBUG)
    logging.warning("INFO: Bassa starting")
    check_conf_availability()
    main()
