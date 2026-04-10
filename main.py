from controllers import GameController
from validators import validate_retry_command
from views import InputView, OutputView
from exceptions import InvalidInputError


class Application:
    def run(self) -> None:
        OutputView.print_start()

        while True:
            GameController().run()

            try:
                command = validate_retry_command(InputView.read_retry_command())
            except InvalidInputError as e:
                OutputView.print_error(str(e))
                continue

            if command == "2":
                break


if __name__ == "__main__":
    Application().run()
