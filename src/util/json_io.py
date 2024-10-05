import json
import os
from io import TextIOWrapper
from typing import Dict


def file_open(mode: str) -> TextIOWrapper:
    """파일을 열거나 생성하는 함수"""
    if os.path.exists("user_info.json"):
        return open("user_info.json", mode)
    else:
        with open("user_info.json", "w") as f:
            f.write("{}")
        return open("user_info.json", mode)


def dict_to_json_file(data: Dict) -> None:
    """딕셔너리를 JSON 파일로 저장하는 함수"""
    with file_open("w") as f:
        json.dump(data, f, ensure_ascii=False)


def dict_to_json_data(data: Dict) -> str:
    """딕셔너리를 JSON 문자열로 변환하는 함수"""
    return json.dumps(data, ensure_ascii=False)


def json_file_to_dict() -> Dict:
    """JSON 파일을 딕셔너리로 읽어오는 함수"""
    with file_open("r") as f:
        return json.load(f)


def json_data_to_dict(data: str) -> Dict:
    """JSON 문자열을 딕셔너리로 변환하는 함수"""
    return json.loads(data)
