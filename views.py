from models import GameResult


class InputView:
    @staticmethod
    def read_numbers() -> str:
        pass

    @staticmethod
    def read_retry_command() -> str:
        pass


class OutputView:
    @staticmethod
    def print_start() -> None:
        pass

    @staticmethod
    def print_result(result: GameResult) -> None:
        pass

    @staticmethod
    def print_homerun() -> None:
        pass

    @staticmethod
    def print_error(message: str) -> None:
        pass
