#!flask/bin/python

from Server import socketio, server, register_blueprint
from ConfReader import check_conf_availability
import logging


def main():
    register_blueprint(server)
    socketio.run(server, host='0.0.0.0', port=5000)
    # server.run(debug=True)


if __name__ == '__main__':
    logging.basicConfig(
        filename="./debug-server.log",
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M'
    )

    console = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    logging.info("Bassa starting")
    check_conf_availability()
    main()
