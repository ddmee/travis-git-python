#!/usr/bin/env python3
"""
Main entry point file for this module.

Created: 2018-03-22
Author: Donal Mee
"""
# standard
import argparse
# local
from travigy.web.main import start


def main():
    print("hello ci world")

def parse_args() -> argparse.Namespace:
    """Ingests command line args"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", help="Flag, start web server", action="store_true")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    main()
    if args.w:
        start()
