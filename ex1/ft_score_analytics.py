import sys


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(("No scores provided. "
               "Usage: python3 ft_score_analytics.py <score1> <score2> ..."))
        return
    args: list[str] = sys.argv[1:]
    scores: list[int] = []
    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Argument '{arg}' must be a number")
    total_players: int = len(scores)
    if total_players == 0:
        print("No valid scores provided. Please enter numeric values.")
        return
    total_score: int = sum(scores)
    max_score: int = max(scores)
    min_score: int = min(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {(total_score / total_players):.2f}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {max_score - min_score}")


if __name__ == "__main__":
    ft_score_analytics()
