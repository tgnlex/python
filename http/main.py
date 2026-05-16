from http.server import BaseHTTPRequestHandler, HTTPServer
from logging import info
import logging

content = { 'html': "text/html", 'json': "application/json" }
headers = { 'ctype': "Content-Type" }


def configure():
    logging.basicConfig(level=logging.DEBUG)
    HOSTNAME = "127.0.0.1"
    PORT = input("Enter a host port: ")
    return (HOSTNAME, int(PORT))

class Handler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header(headers['ctype'], content['html'])
        self.end_headers()
    def do_GET(self):
        logging.info("[HTTP]\nMETHOD: GET \nPATH: %s \nHEADERS: %s\n ", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write(b"Hello World!")


def start():
    address = configure()
    info('[HTTP] Serving on http://{}:{}'.format(address[0], address[1]))
    server = HTTPServer(address, Handler)
    try: 
        server.serve_forever()
    except KeyboardInterrupt:
        pass 
    server.server_close()
    info('[HTTP] Shutting down server...')
    

start()
