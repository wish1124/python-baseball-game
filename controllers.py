from models import Computer, Player, Referee
from views import InputView, OutputView
from validators import validate_retry_command
from exceptions import InvalidInputError


class GameController:
    def run(self) -> None:
        computer = Computer.generate()

        while True:
            try:
                raw = InputView.read_numbers()
                player = Player.from_input(raw)
            except InvalidInputError as e:
                OutputView.print_error(str(e))
                continue

            result = Referee.judge(computer, player)
            OutputView.print_result(result)

            if result.is_homerun():
                OutputView.print_homerun()
                break
