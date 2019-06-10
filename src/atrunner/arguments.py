import argparse
import json
import os.path
from typing import Union

from . import errors
from .atcoder import create_url_from_problem_id


class Arguments:
    def __init__(
        self,
        source_file: str,
        problem_url: Union[str, None],
    ):
        # load settings json file
        package_dir = os.path.dirname(__file__)
        settings_file = os.path.join(package_dir, "settings.json")
        if not os.path.isfile(settings_file):
            with open(settings_file, "w", encoding="utf-8") as f:
                json.dump({
                    "command": {
                        "exe": {
                            "run": "{}",
                        },
                        "c": {
                            "compile": "gcc {}",
                            "bin": "a.exe",
                            "run": "a.exe",
                        },
                        "cpp": {
                            "compile": "g++ {}",
                            "bin": "a.exe",
                            "run": "a.exe",
                        },
                        "d": {
                            "run": "rdmd {}",
                        },
                        "py": {
                            "run": "python {}",
                        },
                    }
                }, f)

        try:
            with open(settings_file, "r", encoding="utf-8") as f:
                settings = json.load(f)
        except json.JSONDecodeError:
            raise errors.InvalidSettingsFileError(
                "Failed to decode json")

        if "command" not in settings:
            settings["command"] = {}
        self.__settings = settings

        # check the existance of the source file
        if not os.path.isfile(source_file):
            raise errors.SourceFileNotFoundError(source_file)
        self.__source_file = source_file

        # generate the problem url if needed
        if problem_url is None:
            problem_url = create_url_from_problem_id(self.source_file_basename)
        self.__problem_url = problem_url

        # validation
        if self.source_file_extension not in self.settings["command"]:
            raise errors.NotSupportedLanguageError(self.source_file_extension)
        lang_settings = self.settings["command"][self.source_file_extension]
        if any([
            "compile" not in lang_settings and "bin" in lang_settings,
            "compile" in lang_settings and "bin" not in lang_settings,
        ]):
            raise errors.InvalidSettingsFileError(
                "'compile' and 'bin' fields must coexist.")
        if "run" not in lang_settings:
            raise errors.InvalidSettingsFileError(
                "'run' field is required.")

    @property
    def source_file(self) -> str:
        return self.__source_file

    @property
    def problem_url(self) -> str:
        return self.__problem_url

    @property
    def source_file_basename(self) -> str:
        if not hasattr(self, "__source_file_basename"):
            filename = os.path.basename(self.source_file)
            if "." in filename:
                basename = ".".join(filename.split(".")[:-1])
            else:
                basename = filename

            self.__source_file_basename = basename

        return self.__source_file_basename

    @property
    def source_file_extension(self) -> Union[str, None]:
        if not hasattr(self, "__source_file_extension"):
            filename = os.path.basename(self.source_file)
            if "." in filename:
                ext = filename.split(".")[-1]
            else:
                ext = None

            self.__source_file_extension = ext

        return self.__source_file_extension

    @property
    def settings(self) -> dict:
        return self.__settings

    @property
    def needs_compilation(self) -> bool:
        return self.compile_command is not None

    @property
    def compile_command(self) -> Union[str, None]:
        ext = self.source_file_extension
        src = self.source_file
        cmd = self.settings["command"][ext].get("compile")
        if cmd is not None:
            cmd = cmd.replace("{}", src)
        return cmd

    @property
    def run_command(self) -> str:
        ext = self.source_file_extension
        src = self.source_file
        return self.settings["command"][ext]["run"].replace("{}", src)

    @property
    def bin_file(self) -> Union[str, None]:
        ext = self.source_file_extension
        return self.settings["command"][ext].get("bin")


def parse() -> Arguments:
    parser = argparse.ArgumentParser(
        description="")
    parser.add_argument(
        "source_file",
        help="path to your source file")
    parser.add_argument(
        "--url", "-u",
        help="problem URL "
        "(can be omittedif the source file name is the same as problem id.)")
    args = parser.parse_args()

    return Arguments(
        args.source_file,
        args.url)
