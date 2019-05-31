class AtRunnerError(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.message = self._create_message(*args)

    def _create_message(self, *args):
        raise NotImplementedError


class SourceFileNotFoundError(AtRunnerError):
    def _create_message(self, source_file: str):
        return f"Source file '{source_file}' is not found."


class SettingsFileNotFoundError(AtRunnerError):
    def _create_message(self, settings_file: str):
        return f"Settings json file '{settings_file}' is not found."


class InvalidSettingsFileError(AtRunnerError):
    def _create_message(self, reason: str):
        return f"Settings json file has invalid format: {reason}"


class NotSupportedLanguageError(AtRunnerError):
    def _create_message(self, ext: str):
        return f"No configuration for '.{ext}' file. Edit your settings file."


class HttpResponseError(AtRunnerError):
    def _create_message(self, url: str, status_code: str):
        return f"""Returned status code {status_code} from '{url}'.
        Confirm whether the url is correct or not."""


class AtCoderHtmlStructureError(AtRunnerError):
    def _create_message(self, url: str):
        return f"""Couldn't find test cases in the problem page: {url}
        Confirm whether the url is correct or not."""


class CompileError(AtRunnerError):
    def _create_message(self):
        return "Couldn't compile the source file."
