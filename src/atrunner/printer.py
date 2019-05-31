from .atcoder import TestCase
from .process import ProcessResult


def print_compile_log(command: str, res: ProcessResult):
    print(f"Run '{command}'")
    if res.stdout != "":
        print(res.stdout)
    if res.stderr != "":
        print(res.stdout)
    print()


def print_ac_info(case: TestCase):
    print(f"* [AC] Test #{case.no}")


def print_failed_case_info(case: TestCase, out: str):
    print(f"| input:")
    for line in case.input.split("\n"):
        print(f"|  {line}")
    print(f"| expected output:")
    for line in case.output.split("\n"):
        print(f"|  {line}")
    print(f"| but got:")
    if out == "":
        print("|  (NO OUTPUT)")
    else:
        for line in out.split("\n"):
            print(f"|  {line}")
    print()


def print_wa_info(case: TestCase, stdout: str):
    print(f"* [WA] Test #{case.no}")
    print_failed_case_info(case, stdout)


def print_re_info(case: TestCase, stderr: str):
    print(f"* [RE] Test #{case.no}")
    print_failed_case_info(case, stderr)


def print_all_info(all_cases: int, passed_cases: int):
    print(f"Passed cases: {passed_cases}/{all_cases}")
