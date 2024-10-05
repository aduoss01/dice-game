from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from auth.user_auth import login, register
from core.play_game import play
from core.rank import rank
from util.json_io import dict_to_json_data, json_data_to_dict


class Main(BaseHTTPRequestHandler):
    # JSON 응답 헤더를 설정하는 메서드
    def send_json_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    # 요청 경로를 파싱하여 서비스 이름과 쿼리 파라미터를 반환하는 메서드
    def parse_request_path(self) -> tuple:
        service_with_query_params = self.path
        service_name = urlparse(service_with_query_params).path
        query_params = parse_qs(urlparse(service_with_query_params).query)
        return service_name, query_params

    # 결과를 JSON으로 변환하여 응답으로 쓰는 메서드
    def write_json_response(self, result):
        if result:
            result_data = dict_to_json_data(result)
            self.wfile.write(result_data.encode("utf-8"))

    # GET 요청을 처리하는 메서드
    def do_GET(self):
        self.send_json_headers()
        service_name, query_params = self.parse_request_path()
        result = {}

        # 서비스 이름에 따라 적절한 함수를 호출하여 결과를 얻음
        if service_name == "/playgame":
            player_id = query_params["id"][0]
            result = play(player_id)
        elif service_name == "/ranking":
            result = rank()

        # 결과를 JSON 응답으로 전송
        self.write_json_response(result)

    # POST 요청을 처리하는 메서드
    def do_POST(self):
        self.send_json_headers()
        service_name, _ = self.parse_request_path()

        # 요청 본문에서 JSON 데이터를 읽어와 파싱
        json_data = self.rfile.read(int(self.headers["Content-Length"])).decode("utf-8")
        dict_data = json_data_to_dict(json_data)
        result = {}

        # 서비스 이름에 따라 적절한 함수를 호출하여 결과를 얻음
        if service_name == "/register":
            result = register(dict_data)
        elif service_name == "/login":
            result = login(dict_data)

        # 결과를 JSON 응답으로 전송
        self.write_json_response(result)


# 서버 설정 및 실행
server_address = ("localhost", 8080)
httpd = HTTPServer(server_address, Main)
httpd.serve_forever()
