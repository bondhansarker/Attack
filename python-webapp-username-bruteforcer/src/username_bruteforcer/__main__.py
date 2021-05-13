import argparse
from .username_bruteforcer import UsernameBruteforcer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "yaml",
        help="a YAML configuration file")
    args = parser.parse_args()
    username_bruteforcer = UsernameBruteforcer(args.yaml)

if __name__ == "__main__":
    main()
