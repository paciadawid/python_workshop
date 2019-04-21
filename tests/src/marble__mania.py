
def marble_game(num_of_players, last_marble):
    last_marble, high_score = last_marble, 0

    marble_list = [0]
    target_position = 0
    players_score = {}

    for i in range(1, last_marble + 1):
            if i % 23:
                target_position = (target_position + 1) % len(marble_list) + 1
                marble_list.insert(target_position, i)
            else:
                target_position = target_position - 7
                player_id = ((i - 1) % num_of_players + 1)
                try:
                    players_score[str(player_id)] += i + marble_list[target_position]
                except KeyError:
                    players_score[str(player_id)] = i + marble_list[target_position]
                marble_list.remove(marble_list[target_position])
    for key, value in players_score.items():
        if value > high_score:
            high_score = value
    return {"last_marble": last_marble, "high_score": high_score}