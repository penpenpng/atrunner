import subprocess
from dataclasses import dataclass


@dataclass(frozen=True)
class ProcessResult:
    stdout: str
    stderr: str


def run(command, input=None) -> ProcessResult:
    proc = subprocess.run(
        command.split(),
        text=True,
        input=input,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    return ProcessResult(proc.stdout, proc.stderr)
