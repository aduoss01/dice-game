from util.json_io import dict_to_json_file, json_file_to_dict

def rank() -> dict:
    # 저장된 사용자 정보 딕셔너리를 불러옴
    user_info_dict = json_file_to_dict()
    sorted_list = []

    # 사용자 정보 딕셔너리에서 각 사용자 정보를 리스트에 추가
    for key, value in user_info_dict.items():
        dict_value = dict(value)
        dict_value.update({'id': key})
        sorted_list.append(dict_value)

    # 사용자 정보를 포인트 기준으로 내림차순 정렬
    sorted_list.sort(key=lambda x: x['point'], reverse=True)

    # 정렬된 사용자 정보를 다시 파일에 저장
    dict_to_json_file(user_info_dict)

    ranker_list = []

    # 상위 3명의 사용자 정보를 ranker_list에 추가
    for ranker in sorted_list[:3]:
        ranker_list.append({'name': ranker['id'], 'point': ranker['point']})

    # 랭킹 정보를 딕셔너리 형태로 반환
    return {"ranker": ranker_list}