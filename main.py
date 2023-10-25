import sys
import time


def sim_bar(iteration: int, total: list, bar_length: int = 50) -> None:
    """Функция для вывода прогресс-бара"""
    progress = (iteration / total)
    arrow = '*' * int(round(bar_length * progress))
    spaces = ' ' * (bar_length - len(arrow))
    sys.stdout.write(f'\r[{arrow}{spaces}] {int(progress * 100)}%')
    sys.stdout.flush()


num_list = [_ for _ in range(1, 101)]

for _, num in enumerate(num_list):
    sim_bar(_ + 1, len(num_list), bar_length=25)
    time.sleep(0.1)
    print(f" [✅️] {num} завершена")
    
