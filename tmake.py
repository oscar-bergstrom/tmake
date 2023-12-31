#!/usr/bin/env python3
#
# tmake
#
# Script for making life easier when using google test for unit testing
# embedded c-code
#
# Oscar Bergstrom
#

import argparse
from dataclasses import dataclass
from pathlib import Path
import re


@dataclass
class Makefile:
    """Class for represent valid data from makefiles"""
    make_inc: str

    def __init__(self):
        pass

    @classmethod
    def parse(cls, filename: Path):
        m = Makefile()

        with open(filename, "r").readall() as data:
            m.make_inc = re.findall("^TESTS_MAKE.*$", data)[-1].split("=")[-1]
        
        return m


@dataclass
class Sourcefile:
    """Class for representing options found in test source files"""
    mocks_objs = list[str]
    target_objs = list[str]

    @classmethod
    def parse(cls, filename: Path):
        s = Sourcefile()

        return s


def generate_makestub(makefile: Makefile, sourcefile: Sourcefile):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--makefile",
                        help="Makefile to use",
                        default="Makefile",
                        type=open)
    parser.add_argument("target", metavar='target', type=str, nargs='+',
                        help="Which target file to build")

    try:
        args = parser.parse_args()
    except FileNotFoundError as f:
        parser.print_usage()
        print(f)
        exit(1)

    print(args)

    print("Parsing makefile:", args.makefile)
    makefile = Makefile.parse(args.makefile)

    for target in args.target:
        print("Parsing source files:", args.target)
        s = Sourcefile.parse(target)

        print("Generating makefile stub...")
        generate_makestub(makefile, s)


if __name__ == "__main__":
    main()
