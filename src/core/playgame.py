from random import Random
from time import time

from json_util.json_io import dict_to_json_file, json_file_to_dict

initial_win_probability = 5 / 12
initial_defeat_probability = 5 / 12
initial_draw_probability = 1 / 6


def play(user_id: str) -> dict:
    random = Random(time())
    user_info_dict = json_file_to_dict()

    player_info = user_info_dict[user_id]
    player_level = player_info["level"]
    player_point = player_info["point"]
    result = dict({"result": "win"})

    win_probability = initial_win_probability + (player_level * 1 / 100)
    defeat_probability = initial_defeat_probability - (0.5 * player_level * 1 / 100)
    draw_probability = initial_draw_probability - (0.5 * player_level * 1 / 100)

    win_defeat_draw = random.choices(
        ["win", "defeat", "draw"],
        [win_probability, defeat_probability, draw_probability],
    )[0]

    player_roll = 0
    computer_roll = 0

    if win_defeat_draw == "win":
        result.update({"result": "win"})

        while player_roll <= computer_roll:
            player_roll += random.randint(2, 6)
            computer_roll += random.randint(1, player_roll - 1)
    elif win_defeat_draw == "defeat":
        result.update({"result": "defeat"})

        while computer_roll <= player_roll:
            computer_roll += random.randint(2, 6)
            player_roll += random.randint(1, computer_roll - 1)
    else:
        result.update({"result": "draw"})
        player_roll = random.randint(1, 6)
        computer_roll = player_roll

    if win_defeat_draw == "win":
        player_info["point"] = player_point + 10

        if (player_point + 10) % 100 == 0:
            if player_info["level"] < 25:
                player_info["level"] = player_level + 1

    user_info_dict[user_id].update(player_info)
    result.update(
        {
            "player": player_roll,
            "computer": computer_roll,
            "point": player_info["point"],
            "level": player_info["level"],
        }
    )

    test_probability([win_probability, defeat_probability, draw_probability])

    dict_to_json_file(user_info_dict)
    return result


def test_probability(probabilities: list):
    random = Random(time())
    num_of_test = 100000
    count: dict = {"win": 0, "defeat": 0, "draw": 0}
    for _ in range(num_of_test):
        choice_one = random.choices(["win", "defeat", "draw"], probabilities)
        count[choice_one[0]] += 1

    print(
        f"이론적 승리 확률 : {round(probabilities[0], 3)} "
        + f"통계적 승리 확률 : {count['win'] / 100000}"
    )
    print(
        f"이론적 패배 확률 : {round(probabilities[1], 3)} "
        + f"통계적 패배 확률 : {count['defeat'] / 100000}"
    )
    print(
        f"이론적 무승부 확률 : {round(probabilities[2], 3)} "
        + f"통계적 무승부 확률 : {count['draw'] / 100000}"
    )
