import os

from . import arguments, atcoder, errors, printer, process


def main():
    args = arguments.parse()

    if args.needs_compilation:
        compile_source(args)

    cases = atcoder.fetch_test_cases(args.problem_url)

    passed_cases = 0
    for case in cases:
        res = process.run(args.run_command, input=case.input)

        if res.stdout == case.output:
            passed_cases += 1
            printer.print_ac_info(case)
        elif res.stderr != "":
            printer.print_re_info(case, res.stderr)
        else:
            printer.print_wa_info(case, res.stdout)

    printer.printer_all_info(len(cases), passed_cases)


def compile_source(args: arguments.Arguments):
    if os.path.exists(args.bin_file):
        os.remove(args.bin_file)

    res = process.run(args.compile_command)

    printer.print_compile_log(args.compile_command, res)

    if not os.path.exists(args.bin_file):
        raise errors.CompileError
