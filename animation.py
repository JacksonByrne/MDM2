import curses
import math
import time


def main(stdscr):
    curses.curs_set(0)          # Hide cursor
    stdscr.nodelay(True)        # Non-blocking input
    stdscr.timeout(0)

    t = 0.0
    speed = 0.15                # Smaller = slower
    amplitude = 10
    wavelength = 15

    while True:
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()

        # Draw animated sine wave across the screen
        for x in range(max_x):
            y = int(
                max_y / 2
                + amplitude * math.sin((x / wavelength) + t)
            )

            # Stay inside 0..max_y-1 and 0..max_x-2 (avoid bottom-right corner)
            if 0 <= y < max_y and 0 <= x < max_x - 1:
                try:
                    stdscr.addch(y, x, "*")
                except curses.error:
                    pass


        stdscr.addstr(0, 0, "Press 'q' to quit")

        stdscr.refresh()
        time.sleep(0.03)
        t += speed

        # Quit on 'q'
        ch = stdscr.getch()
        if ch == ord('q'):
            break


if __name__ == "__main__":
    curses.wrapper(main)
