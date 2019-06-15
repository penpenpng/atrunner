import argparse
import os
from pathlib import Path

EXT = {
    "python": "py",
    "d": "d",
}

TEMP = {
    "python": "",
    "d": """import std.algorithm;
import std.algorithm;
import std.container;
import std.conv;
import std.functional;
import std.math;
import std.random;
import std.range;
import std.stdio;
import std.string;
import std.traits;


void main() {

}

""",
}


def main():
    parser = argparse.ArgumentParser(
        description="create working directory for atcoder")
    parser.add_argument(
        "contest",
        help="contest id: like \"abc123\"")
    parser.add_argument(
        "language",
        help="d and python are supported")
    args = parser.parse_args()

    if any([
        args.language not in EXT,
        args.language not in EXT,
    ]):
        print("The language is not supported")
        return

    os.mkdir(args.contest)
    for suf in ["_a", "_b", "_c", "_d", "_e", "_f"]:
        path = Path(args.contest) / f"{args.contest}{suf}.{EXT[args.language]}"
        with open(path, "w") as f:
            f.write(TEMP[args.language])
