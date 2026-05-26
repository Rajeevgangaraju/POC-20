from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Welcome to the LIVE Python GitOps POC Application! V2</h1>")

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8080), MyHandler)
    print("Python app running on port 8080...")
    server.serve_forever()
