from json_util.json_io import dict_to_json_file, json_file_to_dict

"""
    랭킹을 반환하는 메소드

    reply -> 딕셔너리가 리스트로 있는 형태
    {   
        'ranker' : [
            {'name' : 'user1', 'point' : 100},
            {'name' : 'user2', 'point' : 90},
            {'name' : 'user3', 'point' : 80}
        ]
    }
"""


def ranking() -> dict:
    # 저장된 user_info.json으로부터 딕셔너리를 불러온다.
    user_info_dict = json_file_to_dict()
    sorted_list = []

    # user_info_dict는 {id : {'point' : point, 'rank' : rank ... }}의 형태이므로, value만을 리스트에 추가한다.
    for key, value in user_info_dict.items():
        dict_value = dict(value)
        dict_value.update({'id': key})
        sorted_list.append(dict_value)

    ###################작성필요########################
    # 힌트 : sorted_list = [{'id' : 'user1', 'point' : 100, 'rank' : 1}, {'id' : 'user2', 'point' : 90, 'rank' : 2}, ...]와 같은 형태로 저장되어 있다.
    #        삽입 정렬, 버블 정렬, 선택 정렬 등을 활용하여 정렬한다.
    ##################################################

    # 정렬된 결과 json 파일에 다시 저장
    dict_to_json_file(user_info_dict)

    ranker_list = []
    """
    { 
     'ranker' : [
        {'name' : 'user1', 'point' : 100},
        {'name' : 'user2', 'point' : 90},
        {'name' : 'user3', 'point' : 80} 
     ]
    } 의 형태로 저장한다.
    """
    ###################작성필요########################
    # 힌트 : sorted_list를 활용하여, ranker_list에 최대 3명까지 추가한다.
    ##################################################

    return {"ranker": ranker_list}
