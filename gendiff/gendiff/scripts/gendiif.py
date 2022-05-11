#!/usr/bin/env python
"""Parse generate diff."""

import argparse


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT', help='set format of output')
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
