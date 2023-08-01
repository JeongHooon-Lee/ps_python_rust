# https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    player_key = {player: i for i, player in enumerate(players)}
    for call in callings:
        get_order = player_key[call]

        player_key[players[get_order - 1]
                   ], player_key[call] = get_order, get_order - 1
        players[get_order], players[get_order -
                                    1] = players[get_order - 1], players[get_order]
    return players


print(solution(["mumu", "soe", "poe", "kai", "mine"],
      ["kai", "kai", "mine", "mine"]))
