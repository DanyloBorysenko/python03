import sys


def ft_command_quest() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        args: list[str] = sys.argv
        print(f"Arguments received: {len(args) - 1}")
        for i in range(1, len(args)):
            print(f"Argument {i}: {args[i]}")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
