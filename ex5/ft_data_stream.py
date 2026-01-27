class Player():
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level


class Event():
    def __init__(self, id: int, player: Player, action: str):
        self.id = id
        self.player = player
        self.action = action


def events_generator(events_count: int, players: list[Player],
                     actions: list[str]):
    action_index: int = 0
    for i in range(1, events_count + 1):
        player: Player = players[i % len(players)]
        if i % 2 == 0:
            action_index = (action_index + 1) % len(actions)
        action: str = actions[action_index]

        if action == "leveled up":
            player.level += 1
        yield Event(i, player, action)


def fibonacci_generator(number: int):
    a: int = 0
    b: int = 1
    sum: int
    for i in range(0, number):
        yield a
        sum = a + b
        a = b
        b = sum


def fibonacci_iterate(number: int) -> list[int]:
    sequence: list[int] = []
    for i in range(0, number):
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


def prime_number_generator(count: int):
    current: int = 2
    found: int = 0

    while found < count:
        is_prime: bool = True
        for i in range(2, current):
            if current % i == 0:
                is_prime = False
                break
        if is_prime is True:
            yield current
            found += 1
        current += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    events_count: int = 10
    print(f"Processing {events_count} game events...\n")
    alice: Player = Player("alice", 10)
    bob: Player = Player("bob", 5)
    charlie: Player = Player("charlie", 1)
    players: list[Player] = [alice, bob, charlie]
    actions: list[str] = ["killed monster", "found treasure", "leveled up"]
    iter_obj = events_generator(events_count, players, actions)

    total: int = 0
    high_level_players: set[str] = set()
    treasure_events_count: int = 0
    level_up_events: int = 0

    for event in iter_obj:
        if event.id < 5:
            print(f"Event{event.id}: Player {event.player.name} "
                  f"(level {event.player.level}) {event.action}")
        if event.id == events_count:
            print("...")
        total += 1

        if event.player.level >= 10:
            high_level_players.add(event.player.name)

        if event.action == "found treasure":
            treasure_events_count += 1

        if event.action == "leveled up":
            level_up_events += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {len(high_level_players)}")
    print(f"Treasure events: {treasure_events_count}")
    print(f"Level-up events: {level_up_events}")

    print("\n=== Generator Demonstration ===")
    print("fibonacci_generator")
    for nb in fibonacci_generator(5):
        print(nb, end=", ")
    print("\nfibonacci_iteration")
    for nb in fibonacci_iterate(5):
        print(nb, end=", ")
    print("\nprime_numbers_generator")
    for nb in prime_number_generator(10):
        print(nb, end=", ")
