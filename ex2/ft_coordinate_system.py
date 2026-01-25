import math


def ft_coordinate_system() -> None:
    print("=== Game Coordinate System ===")
    pos: tuple = (10, 20, 5)
    zero_pos: tuple = (0, 0, 0)
    print(f"\nPosition created: {pos}")
    try:
        dist: float = calculate_dist(zero_pos, pos)
        print(f"Distance between {zero_pos} and {pos}: {dist:.2f}")
    except ValueError as e:
        print(e)

    data: str = "3,4,0"
    print(f"\nParsing coordinates: \"{data}\"")
    try:
        pos = parsing_coordinates(data)
        print(f"Parsed position: {pos}")
        dist = calculate_dist(zero_pos, pos)
        print(f"Distance between {zero_pos} and {pos}: {dist:.2f}")
    except ValueError as e:
        print(e)

    invalid_data: str = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{invalid_data}\"")
    try:
        parsing_coordinates(invalid_data)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")

    print("\nUnpacking demonstration:")
    pos = (3, 4, 0)
    print(f"Player at x={pos[0]}, y={pos[1]}, z={pos[2]}")
    x, y, z = pos
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def parsing_coordinates(data: str) -> tuple:
    strings: list[str] = data.split(",")
    if len(strings) != 3:
        raise ValueError("Expected 3 coordinates")
    return (int(strings[0]), int(strings[1]), int(strings[2]))


def calculate_dist(pos1: tuple, pos2: tuple) -> float:
    dist: float = math.sqrt((pos2[0] - pos1[0]) ** 2 +
                            (pos2[1] - pos1[1]) ** 2 +
                            (pos2[2] - pos1[2]) ** 2)
    return dist


if __name__ == "__main__":
    ft_coordinate_system()
