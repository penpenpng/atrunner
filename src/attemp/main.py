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

    template = load_template(args.extension)
    os.mkdir(args.contest)
    for suf in ["_a", "_b", "_c", "_d", "_e", "_f"]:
        path = Path(args.contest) / f"{args.contest}{suf}.{args.extension}"
        with open(path, "w", encoding="utf_8") as f:
            f.write(template)


def load_template(ext):
    template_dir = Path(__file__).parent / "temp"
    template_file = template_dir / ext
    if not template_dir.exists():
        os.mkdir(template_dir)
    if template_file.is_file():
        with open(template_file, "r", encoding="utf_8") as f:
            return f.read()
    return ""
