from util.json_io import dict_to_json_file, json_file_to_dict
from typing import Dict

def get_user_info() -> Dict[str, dict]:
    """사용자 정보 딕셔너리를 불러오는 함수"""
    return json_file_to_dict()

def save_user_info(user_info_dict: Dict[str, dict]) -> None:
    """사용자 정보 딕셔너리를 저장하는 함수"""
    dict_to_json_file(user_info_dict)

def register(new_user_info: dict) -> dict:
    """
    새로운 사용자를 등록하는 함수

    Args:
        new_user_info (dict): 새로운 사용자 정보 (id와 password 포함)

    Returns:
        dict: 등록 결과를 나타내는 딕셔너리
    """
    user_info_dict = get_user_info()
    new_user_id = new_user_info["id"]
    new_user_pw = new_user_info["password"]
    result_dict: dict = {"success": True, "id": new_user_id}

    # 이미 존재하는 사용자 ID인지 확인
    if new_user_id in user_info_dict:
        result_dict["success"] = False
    else:
        # 새로운 사용자 정보 추가
        user_info_dict[new_user_id] = {
            "password": new_user_pw,
            "level": 1,
            "point": 0,
            "rank": 0,
        }
        result_dict.update(user_info_dict[new_user_id])

    # 사용자 정보 저장
    save_user_info(user_info_dict)
    return result_dict

def login(new_user_info: dict) -> dict:
    """
    사용자 로그인 함수

    Args:
        new_user_info (dict): 로그인할 사용자 정보 (id와 password 포함)

    Returns:
        dict: 로그인 결과를 나타내는 딕셔너리
    """
    user_info_dict = get_user_info()
    new_user_id = new_user_info["id"]
    new_user_pw = new_user_info["password"]

    result_dict: dict = {"success": False, "id": new_user_id}

    # 사용자 ID와 비밀번호 확인
    if (
        new_user_id in user_info_dict
        and new_user_pw == user_info_dict[new_user_id]["password"]
    ):
        result_dict["success"] = True
        result_dict.update(user_info_dict[new_user_id])

    return result_dict