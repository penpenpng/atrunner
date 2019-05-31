from dataclasses import dataclass
from typing import List

from . import errors
from .soup import get_soup_from_url


@dataclass(frozen=True)
class TestCase:
    no: int
    input: str
    output: str


def create_url_from_problem_id(problem_id: str) -> str:
    contest_id = "_".join(problem_id.split("_")[:-1])
    return f"https://atcoder.jp/contests/{contest_id}/tasks/{problem_id}"


def fetch_test_cases(url: str) -> List[TestCase]:
    soup = get_soup_from_url(url)

    samples = [
        pre.text.replace("\r", "")
        for pre
        in soup.select("span.lang-ja h3 + pre")
    ]

    if len(samples) == 0 or len(samples) % 2 != 0:
        raise errors.AtCoderHtmlStructureError(url)

    test_cases = []
    no = 0
    while len(samples) > 0:
        no += 1
        input, output, *samples = samples
        test_cases.append(TestCase(no, input, output))

    return test_cases
