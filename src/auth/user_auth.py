from json_util.json_io import dict_to_json_file, json_file_to_dict


def register(new_user_info: dict) -> dict:
    user_info_dict = json_file_to_dict()
    new_user_id = new_user_info["id"]
    new_user_pw = new_user_info["password"]
    result_dict: dict = {"success": True, "id": new_user_id}

    if new_user_id in user_info_dict:
        result_dict["success"] = False
    else:
        user_info_dict[new_user_id] = {
            "password": new_user_pw,
            "level": 1,
            "point": 0,
            "rank": 0,
        }
        result_dict.update(user_info_dict[new_user_id])

    dict_to_json_file(user_info_dict)
    return result_dict


def login(new_user_info: dict) -> dict:
    user_info_dict = json_file_to_dict()

    new_user_id = new_user_info["id"]
    new_user_pw = new_user_info["password"]

    result_dict: dict = {"success": False, "id": new_user_id}

    if (
        new_user_id in user_info_dict
        and new_user_pw == user_info_dict[new_user_id]["password"]
    ):
        result_dict["success"] = True
        result_dict.update({"level": 1, "point": 0, "rank": 0})

    return result_dict
