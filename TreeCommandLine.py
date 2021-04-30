# Directory Tree
# RetrO_13th
# github.com/RetrO-13th

import pathlib
import sys


from TreeClasses import DirectoryTree
import argparse

def parse_cli():
    parser = argparse.ArgumentParser(prog="Directory Tree", description="RetrO_13th Directory Tree", epilog="Thanks for using RetrO_13th Directory Tree")
    
    parser.version = "Directory Tree v0.1.5"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument("dir", metavar="Directory".upper(), nargs="?", default=".", help="Generate a full directory starting at [DIRECTORY]")
    parser.add_argument("-d", "--dir-only", action="store_true", help="Generate a only directory tree")
    parser.add_argument("-e", "--extention", nargs="?", help="Find files with a specific extention in a directory")

    return parser.parse_args()

def main():
    args = parse_cli()
    dir = pathlib.Path(args.dir)

    if not dir.is_dir():
        print(f"{dir} is not recognized as an internal or external command, operable program or batch file.")
        sys.exit()

    tree = DirectoryTree(dir, extention=args.extention, dir_only=args.dir_only)
    tree.show()
