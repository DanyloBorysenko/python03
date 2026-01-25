class Player():
    def __init__(self, name: str, achievements: set[str]):
        self.name = name
        self.achievements = achievements


def ft_achievement_tracker(players: set[Player]) -> None:
    print("=== Achievement Tracker System ===\n")
    for player in players:
        print(f"Player {player.name} achievements: {player.achievements}")

    print("\n=== Achievement Analytics ===\n")
    unique: set[str] = set()
    for player in players:
        unique = unique.union(player.achievements)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}\n")

    print(f"Common to all players: {get_common_achievements(players)}")

    shared: set[str] = set()
    for player1 in players:
        for player2 in players:
            if player1 != player2:
                shared = shared.union(
                    player1.achievements.intersection(player2.achievements))
    print(f"Rare achievements (1 player): {unique.difference(shared)}\n")


def get_common_achievements(players: set[Player]) -> set[str]:
    common: set[str]
    counter: int = 1
    for player in players:
        if counter == 1:
            common = player.achievements
            counter += 1
            continue
        common = common.intersection(player.achievements)
        counter += 1
    return common


def compare_two_players(player1: Player, player2: Player) -> None:
    common: set[str] = get_common_achievements({player1, player2})
    print(f"{player1.name} vs {player2.name} common: {common}")
    print(f"{player1.name} unique: {player1.achievements.difference(common)}")
    print(f"{player2.name} unique: {player2.achievements.difference(common)}")


if __name__ == "__main__":
    alice: Player = Player("alice", {'first_kill', 'level_10',
                                     'treasure_hunter', 'speed_demon'})
    bob: Player = Player("bob", {'first_kill', 'level_10',
                                 'boss_slayer', 'collector'})
    charlie: Player = Player("charlie",
                             {'level_10', 'treasure_hunter', 'boss_slayer',
                              'speed_demon', 'perfectionist'})
    ft_achievement_tracker({alice, bob, charlie})
    compare_two_players(alice, bob)
