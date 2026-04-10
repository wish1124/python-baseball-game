from models import GameResult


class InputView:
    @staticmethod
    def read_numbers() -> str:
        return input("숫자를 입력해주세요 : ")

    @staticmethod
    def read_retry_command() -> str:
        return input("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.\n")


class OutputView:
    @staticmethod
    def print_start() -> None:
        print("숫자 야구 게임을 시작합니다.")

    @staticmethod
    def print_result(result: GameResult) -> None:
        if result.is_nothing():
            print("낫싱")
            return
        parts = []
        if result.balls > 0:
            parts.append(f"{result.balls}볼")
        if result.strikes > 0:
            parts.append(f"{result.strikes}스트라이크")
        print(" ".join(parts))

    @staticmethod
    def print_homerun() -> None:
        print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")

    @staticmethod
    def print_error(message: str) -> None:
        print(f"[오류] {message}")
