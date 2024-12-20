#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        csp_policy = "default-src 'self'; font-src 'self'; style-src 'self'; script-src 'self';"
        self.send_header('Content-Security-Policy', csp_policy)
        SimpleHTTPRequestHandler.end_headers(self)
        

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
