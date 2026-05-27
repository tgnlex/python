from http.server import BaseHTTPRequestHandler, HTTPServer
from logging import info
from utils import jstr
import logging

content = { 'html': "text/html", 'json': "application/json" }
headers = { 'ctype': "Content-Type" }

def configure():
    logging.basicConfig(level=logging.DEBUG)
    HOSTNAME = "127.0.0.1"
    PORT = input("Enter a host port: ")
    return (HOSTNAME, int(PORT))

class Handler(BaseHTTPRequestHandler):
    
    def _set_logger(self):  
        info("[HTTP]\nMETHOD: GET \nPATH: %s \nHEADERS: %s\n ", str(self.path), str(self.headers))
    
    def _set_response(self, ctype):
        self.send_response(200)
        self.send_header(headers['ctype'], ctype)
        self.end_headers()
    
    def _setup_html_route(self):
        self._set_logger()
        self._set_response(content['html'])
    
    def _setup_json_route(self):
    4    self._set_logger()
        self._set_response(content['json'])
    
    def do_GET(self):
        if self.path == "/api":
            self._setup_html_route()
            self.wfile.write(b"Server Root!")
        if self.path == "/api/hello":
            self._setup_json_route()
            data = {"message": "hello"}
            self.wfile.write(jstr(data))
        
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
