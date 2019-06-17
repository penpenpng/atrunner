import argparse
import os
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="create working directory for atcoder")
    parser.add_argument(
        "contest",
        help="contest id: like \"abc123\"")
    parser.add_argument(
        "extension",
        help="extension of source files excluding period: like \"cpp\"")
    args = parser.parse_args()

    template = load_templates(args.extension)
    os.mkdir(args.contest)
    for suf in ["_a", "_b", "_c", "_d", "_e", "_f"]:
        path = Path(args.contest) / f"{args.contest}{suf}.{args.extension}"
        if template is not None:
            with open(path, "w", encoding="utf_8") as f:
                f.write(template)


def load_templates(ext):
    template_file = Path(__file__).parent / "temp" / ext
    if template_file.is_file():
        with open(template_file, "r", encoding="utf_8") as f:
            return f.read()
