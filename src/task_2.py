import matplotlib.pyplot as plt
import numpy as np


def draw_branch(x, y, length, angle, depth):
    if depth == 0:
        return

    # Реалізація логіки візуалізації фракталу
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    LINE_WIDTH = 1.5

    plt.plot([x, x_end], [y, y_end], color="brown", linewidth=LINE_WIDTH)

    new_length = length * 0.7
    angle_delta = np.pi / 6

    # Ліва гілка
    draw_branch(
        x_end,
        y_end,
        new_length,
        angle + angle_delta,
        depth - 1,
    )

    # Права гілка
    draw_branch(
        x_end,
        y_end,
        new_length,
        angle - angle_delta,
        depth - 1,
    )


if __name__ == "__main__":
    depth = int(input("Введіть рівень рекурсії (наприклад 8–12): "))

    # Налаштування вікна для малювання
    plt.figure(figsize=(8, 8))
    plt.axis("off")
    plt.title("Фрактал: дерево Піфагора")

    draw_branch(
        x=0.0,
        y=0.0,
        length=1.0,
        angle=np.pi / 2,
        depth=depth,
    )

    plt.show()
