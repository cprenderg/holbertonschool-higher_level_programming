#!/usr/bin/env python3
"""
Creates a local HTTP server
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    # Handle HTTP GET requests
    def do_GET(self):
        if self.path == '/data':
            # Dataset
            payload = {"name": "John", "age": 30, "city": "New York"}

            # Standard headers for JSON
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Writes payload to stream
            self.wfile.write(json.dumps(payload).encode('utf-8'))
        
        elif self.path == '/info':
            info_payload = {
                "version": "1.0", 
                "description": "A simple API built with http.server"
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(info_payload).encode('utf-8'))
        
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()

            # Text response
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Endpoint not found".encode('utf-8'))
        



def run(port=8000):
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    print(f"Starting server on http://localhost:{port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
        httpd.server_close()

if __name__ == "__main__":
    run()