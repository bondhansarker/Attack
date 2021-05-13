import argparse
from .password_sprayer import PasswordSprayer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "yaml",
        help="a YAML configuration file")
    args = parser.parse_args()
    password_sprayer = PasswordSprayer(args.yaml)


if __name__ == "__main__":
    main()
