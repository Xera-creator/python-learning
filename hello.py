"""A simple hello world script to get started with Python."""


def greet(name="World"):
    """Return a greeting message."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
