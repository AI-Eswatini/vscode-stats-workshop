"""A tiny web server for the VS Code workshop.

Run it with:  python server.py
Then open:    http://localhost:8000
"""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 8000

# Try changing this message, save the file, restart the server and refresh the page!
MESSAGE = "Hello from my first web server!"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = f"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Workshop Server</title>
    <style>
      body {{ font-family: sans-serif; text-align: center; margin-top: 80px; }}
      h1 {{ color: #007acc; }}
    </style>
  </head>
  <body>
    <h1>{MESSAGE}</h1>
  </body>
</html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


if __name__ == "__main__":
    server = ThreadingHTTPServer(("localhost", PORT), Handler)
    print(f"Server running at http://localhost:{PORT}  (press Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
