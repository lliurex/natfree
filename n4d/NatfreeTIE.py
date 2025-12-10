import n4d.responses
import socket


class NatfreeTIE:

    def __init__(self):
        pass

    def check_server(self):
        try:
            socket.gethostbyname("server")
            return n4d.responses.build_successful_call_response(True)
        except socket.gaierror:
            return n4d.responses.build_successful_call_response(False)
