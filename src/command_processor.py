import argparse
from Enum.search_options import SearchOptions

my_parser = argparse.ArgumentParser(description='Finding files in path', usage='%(prog)s [options] path')
my_parser.add_argument("--input", "-i", help="input for search engine", type=str)
my_parser.add_argument("--current", "-c", help="specification about the scope of searching - current directory", action='store_true')
my_parser.add_argument("--full", "-f", help="specification about the scope of searching - whole system", action='store_true')
my_parser.add_argument("--disc", "-d", help="specification about the scope of searching - disc (as example --disc=D", action='store_true')
my_parser.add_argument("--directory", "-dir", help="specification about the scope of searching - disc (as example --directory=temp", action='store_true')
args = my_parser.parse_args()


def define_command():
    if args.current:
        return SearchOptions.CURRENT_DIR
    elif args.full:
        return SearchOptions.FULL
    elif args.disc:
        return SearchOptions.DISC
    elif args.directory:
        return SearchOptions.DIR

def get_input():
    return args.input
