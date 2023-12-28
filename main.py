import sys
import time


def sim_bar(iteration: int, total: list, bar_length: int = 50, symbol: str = "🟦") -> None:
    """Функция для вывода прогресс-бара"""
    total = len(total)
    progress = ((iteration + 1) / total)
    arrow = symbol * int(round(bar_length * progress))
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write(f'\r[{arrow}{spaces}] {int(progress * 100)}%')
    sys.stdout.flush()


if __name__ == "__main__":
    num_list = [_ for _ in range(1, 101)]

    for _, num in enumerate(num_list):
        sim_bar(_, num_list, bar_length=25)
        time.sleep(0.1)
        print(f" [✅️] {num} завершена")
    
