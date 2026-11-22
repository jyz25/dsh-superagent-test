import sys


def greet(name):
    if not name:
        return "hello, world"
    return f"hello, {name}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python3 greet.py <name>", file=sys.stderr)
        raise SystemExit(2)
    print(greet(sys.argv[1]))
