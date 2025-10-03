from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = 'localhost'
PORT = 8000

# Create a request handler
handler = SimpleHTTPRequestHandler

# Set up the server
with HTTPServer((HOST, PORT), handler) as server:
    print(f"Serving on http://{HOST}:{PORT}")
    server.serve_forever()