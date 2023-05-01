"""
Super Simple HTTP Server in Python .. not for production just for learning and fun
Author: Wolf Paulus (https://wolfpaulus.com)
Modified by: Taylor Hancock
Notes: Copilot used for text autocompletion. Method to handle application JSON found after a bit of scrounging around
       in the docs for http.server (https://docs.python.org/3/library/http.server.html) (plus some StackOverflow as a
       sanity check)
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import asctime
from main import distance_string
import json

hostName = "0.0.0.0"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        content_type = "text/html"  # default content type
        if self.path == "/health":
            status = 200

            # handle JSON requests (get if it accepts JSON first - if not, return text)
            if self.headers.get('accept') == "application/json":
                content_type = "application/json"
                content = json.dumps({"status": status, "health": "OK"})
            else:
                content = "OK"
        elif self.path == "/" or self.path.startswith("/?number="):
            status = 200

            # calculations
            number = self.path.split("=")[1] if self.path.startswith("/?number=") else ""
            result = distance_string(number, "")  # Leave error message blank

            if self.headers.get('accept') == "application/json":
                content_type = "application/json"
                content = json.dumps({"status": status, "number": number, "result": result})
            else:
                with open('./src/response.html', 'r') as f:
                    # read the html template and fill in the parameters: path, time and result
                    content = f.read().format(path=self.path, time=asctime(), result=result)
        elif self.path == "/teapot":
            status = 418

            if self.headers.get('accept') == "application/json":
                content_type = "application/json"
                content = json.dumps({"status": status, "error": "I'm a Little Teapot, Short and Stout, "
                                                                 "Tip Me Over and Pour Me Out"})
            else:
                content = "<html>" \
                          "<head>" \
                          "<link rel='preconnect' href='https://fonts.googleapis.com'>" \
                          "<link rel='preconnect' href='https://fonts.gstatic.com' crossorigin>" \
                          "<link href='https://fonts.googleapis.com/css2?family=Castoro+Titling&display=swap'" \
                          "rel='stylesheet'>" \
                          "<style>" \
                          "h1 {text-align: center; font-family: 'Castoro Titling', cursive;}" \
                          "</style>" \
                          "</head>" \
                          "<body>" \
                          "<h1>ERROR 418:<br>" \
                          "I'm a Little Teapot,<br>" \
                          "Short and Stout,<br>" \
                          "Tip Me Over<br>and Pour Me Out</h1>" \
                          "</body>" \
                          "</html>"
        else:
            status = 404

            if self.headers.get('accept') == "application/json":
                content = json.dumps({"status": status, "error": "Not Found"})
            else:
                content = "Not Found"

        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.end_headers()
        self.wfile.write(bytes(content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
