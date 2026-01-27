class Game_Analytics_Dashboard():
    def __init__(self):
        print("=== Game Analytics Dashboard ===")

    def list_comprehension_examples(self, data: list[dict],
                                    high_score: int) -> None:
        print("=== List Comprehension Examples ===")

        high_score_players: list[str]
        high_score_players = [dictionary["name"] for dictionary in data
                              if dictionary.get("score") > high_score]
        print(f"High scorers (>{high_score}): {high_score_players}")

        score_doubled: list[int]
        score_doubled = [dictionary["score"] * 2 for dictionary in data]
        print(f"Scores doubled: {score_doubled}")

    def dict_comprehensions_examples(self, data: list[dict]) -> None:
        print("\n=== Dict Comprehension Examples ===")
        players_score: dict[str, int]
        players_score = {dictionary["name"]: dictionary["score"] for dictionary in data}
        print(f"Player scores: {players_score}")

        score_category: dict[str, list[str]] = {}
        score_category.update({"Low": [dictionary["name"] for dictionary in data if dictionary["level"] == 1]})
        score_category.update({"Medium": [dictionary["name"] for dictionary in data if 1 < dictionary["level"] < 10]})
        score_category.update({"High": [dictionary["name"] for dictionary in data if dictionary["level"] == 10]})
        print(f"{score_category}")


if __name__ == "__main__":
    dashboard = Game_Analytics_Dashboard()

    alice: dict = {"name": "alice",
                   "score": 2000,
                   "level": 2,
                   "achievments": {"level_2", "first_kill"}}
    bob: dict = {"name": "bob",
                 "score": 3000,
                 "level": 3,
                 "achievments": {"level_2", "level_3",
                                 "first_kill", "boss_slayer"}}
    charlie: dict = {"name": "charlie",
                     "score": 1000,
                     "level": 1,
                     "achievments": set()}

    din: dict = {"name": "din",
                 "score": 5000,
                 "level": 10,
                 "achievments": {"level_2", "level_3",
                                 "level_4", "level_5",
                                 "first_kill", "boss_slayer", "winner"}}

    data: list[dict] = [alice, bob, charlie, din]
    high_score: int = 2000
    dashboard.list_comprehension_examples(data, high_score)
    dashboard.dict_comprehensions_examples(data)
