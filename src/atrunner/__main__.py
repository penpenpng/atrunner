from . import errors
from .main import main


if __name__ == "__main__":
    try:
        main()
    except errors.AtRunnerError as e:
        print(f"ERROR: {e.message}")
