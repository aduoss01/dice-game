from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from auth.user_auth import login, register
from core.playgame import play
from core.ranking import ranking
from json_util.json_io import dict_to_json_data, json_data_to_dict


class DicegameServer(BaseHTTPRequestHandler):
    def make_header(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def divide_path(self) -> tuple:
        service_with_query_params = self.path

        servie_name = urlparse(service_with_query_params).path
        query_params = parse_qs(urlparse(service_with_query_params).query)

        return servie_name, query_params

    def do_GET(self):
        self.make_header()
        service_name, query_params = self.divide_path()
        result = {}

        if service_name == "/playgame":
            player_id = query_params["id"][0]
            result = play(player_id)
        elif service_name == "/ranking":
            result = ranking()

        if result:
            result_data = dict_to_json_data(result)
            self.wfile.write(result_data.encode("utf-8"))

    def do_POST(self):
        self.make_header()
        service_name, _ = self.divide_path()

        json_data = self.rfile.read(int(self.headers["Content-Length"])).decode("utf-8")
        dict_data = json_data_to_dict(json_data)
        result = {}

        if service_name == "/register":
            result = register(dict_data)
        elif service_name == "/login":
            result = login(dict_data)

        if result:
            result_data = dict_to_json_data(result)
            self.wfile.write(result_data.encode("utf-8"))


server_address = ("localhost", 8080)
httpd = HTTPServer(server_address, DicegameServer)
httpd.serve_forever()
