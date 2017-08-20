import os
import platform
import pwd
import socket
import time
from flask import Flask, jsonify, request


def my_app():
    app = Flask(__name__)

    @app.route('/')
    @app.route("/hostname", strict_slashes=False, methods=["GET"])
    def route_hostname():
        return socket.gethostname() + '\n'

    @app.route("/client", strict_slashes=False, methods=["GET"])
    def route_client():
        response = {
            'user_agent': request.headers.get('User-Agent'),
            'os_platform': request.user_agent.platform,
            'browser_type': request.user_agent.browser,
            'browser_version': request.user_agent.version,
            'client_ip': request.remote_addr
        }
        return jsonify(response)

    @app.route("/datetime", strict_slashes=False, methods=["GET"])
    @app.route("/date", strict_slashes=False, methods=["GET"])
    @app.route("/time", strict_slashes=False, methods=["GET"])
    def route_datetime():
        return jsonify(datetime=time.strftime('%Y%m%d_%H%M%S'))

    @app.route("/host", strict_slashes=False, methods=["GET"])
    def route_host():
        response = {
            'host_hostname': str(socket.gethostname()),
            'host_ip': str(socket.gethostbyname(socket.gethostname())),
            'os_platform': str(platform.platform()),
            'os_system': str(platform.system()),
            'python_version': str(platform.python_version()),
            'user_id': str(os.getuid()),
            'user_name': str(pwd.getpwuid(int(os.getuid())).pw_name),
            'pid_parent': str(os.getppid()),
            'pid_self': str(os.getpid())
        }
        return jsonify(response)

    @app.route("/ip", strict_slashes=False, methods=["GET"])
    def route_ip():
        return request.remote_addr

    @app.route('/ping', strict_slashes=False, methods=["GET"])
    def route_ping():
        return jsonify(ping='pong')

    return app


if __name__ == '__main__':
    app = my_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
