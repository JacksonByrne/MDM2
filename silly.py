import os
import time

def clear():
    # Works on Windows, macOS, Linux
    os.system("cls" if os.name == "nt" else "clear")

def bouncing_text(width=30, cycles=3, delay=0.05):
    text = "Hello VS Code!"
    pos = 0
    direction = 1  # 1 = right, -1 = left
    steps = cycles * (width - len(text)) * 2

    for _ in range(steps):
        clear()
        print(" " * pos + text)
        time.sleep(delay)

        pos += direction
        if pos <= 0 or pos >= width - len(text):
            direction *= -1

if __name__ == "__main__":
    bouncing_text()
