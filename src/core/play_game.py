from random import Random
from time import time
from typing import Dict

from util.json_io import dict_to_json_file, json_file_to_dict

# 초기 승리, 패배, 무승부 확률 설정
initial_win_probability = 5 / 12
initial_defeat_probability = 5 / 12
initial_draw_probability = 1 / 6


def roll_dice(random: Random, win_defeat_draw: str) -> tuple:
    player_roll = 0
    computer_roll = 0

    if win_defeat_draw == "win":
        while player_roll <= computer_roll:
            player_roll += random.randint(2, 6)
            computer_roll += random.randint(1, player_roll - 1)
    elif win_defeat_draw == "defeat":
        while computer_roll <= player_roll:
            computer_roll += random.randint(2, 6)
            player_roll += random.randint(1, computer_roll - 1)
    else:
        player_roll = random.randint(1, 6)
        computer_roll = player_roll

    return player_roll, computer_roll


def update_player_info(player_info: Dict[str, int], win_defeat_draw: str) -> None:
    if win_defeat_draw == "win":
        player_info["point"] += 10
        if player_info["point"] % 100 == 0 and player_info["level"] < 25:
            player_info["level"] += 1


def play(user_id: str) -> Dict[str, int]:
    # 랜덤 객체 생성
    random = Random(time())
    # 사용자 정보 딕셔너리 불러오기
    user_info_dict = json_file_to_dict()

    # 사용자 정보 가져오기
    player_info = user_info_dict[user_id]
    player_level = player_info["level"]

    # 사용자 레벨에 따른 승리, 패배, 무승부 확률 계산
    win_probability = initial_win_probability + (player_level * 1 / 100)
    defeat_probability = initial_defeat_probability - (0.5 * player_level * 1 / 100)
    draw_probability = initial_draw_probability - (0.5 * player_level * 1 / 100)

    # 승리, 패배, 무승부 중 하나를 랜덤으로 선택
    win_defeat_draw = random.choices(
        ["win", "defeat", "draw"],
        [win_probability, defeat_probability, draw_probability],
    )[0]

    # 주사위 굴리기
    player_roll, computer_roll = roll_dice(random, win_defeat_draw)

    # 사용자 정보 업데이트
    update_player_info(player_info, win_defeat_draw)
    user_info_dict[user_id].update(player_info)

    result = {
        "result": win_defeat_draw,
        "player": player_roll,
        "computer": computer_roll,
        "point": player_info["point"],
        "level": player_info["level"],
    }

    # 업데이트된 사용자 정보를 파일에 저장
    dict_to_json_file(user_info_dict)
    return result
