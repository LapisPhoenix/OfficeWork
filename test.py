import curses
import re

def setup_true_color(stdscr):
    # Enable true color if supported
    if curses.can_change_color() and hasattr(curses, 'COLORS') and curses.COLORS >= 16777216:
        curses.use_default_colors()

    # If color changing isn't supported, we'll use color pairs
    if not hasattr(curses, 'COLOR_RGB'):
        print("Terminal may not support true color")

def render_ansi_to_curses(stdscr, ansi_string):
    # Split the string into color-coded segments
    # This regex matches ANSI color escape sequences
    segments = re.findall(r'(\x1b\[38;2;(\d+);(\d+);(\d+)m\x1b\[48;2;(\d+);(\d+);(\d+)m(.+?)\x1b\[0m)', ansi_string)

    y = 0
    for fg_r, fg_g, fg_b, bg_r, bg_g, bg_b, char in [(int(s[1]), int(s[2]), int(s[3]),
                                                      int(s[4]), int(s[5]), int(s[6]), s[7])
                                                     for s in segments]:
        try:
            # Initialize a color pair dynamically
            # Curses color pair index is limited, so we hash the color
            color_pair_index = hash((fg_r, fg_g, fg_b, bg_r, bg_g, bg_b)) % 256

            # Try to initialize color pair
            try:
                curses.init_pair(color_pair_index,
                                 curses.COLOR_RGB(fg_r, fg_g, fg_b),
                                 curses.COLOR_RGB(bg_r, bg_g, bg_b))
            except Exception:
                # Fallback to nearest color if true color isn't supported
                color_pair_index = 1

            # Draw the character
            stdscr.addstr(y, 0, char, curses.color_pair(color_pair_index))
        except Exception as e:
            # Handle any drawing errors
            stdscr.addstr(y, 0, f"Error: {str(e)}")

        y += 1

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Setup true color
    setup_true_color(stdscr)

    # Example ANSI-colored Unicode strings (from your previous code)
    ansi_strings = [
        "\033[38;2;255;0;0m\033[48;2;128;0;0m█\033[0m",
        "\033[38;2;0;255;0m\033[48;2;0;128;0m▓\033[0m",
        "\033[38;2;0;0;255m\033[48;2;0;0;128m░\033[0m"
    ]

    # Render the strings
    for ansi_string in ansi_strings:
        render_ansi_to_curses(stdscr, ansi_string)

    # Refresh and wait
    stdscr.refresh()
    stdscr.getch()

# Run the curses application
if __name__ == '__main__':
    curses.wrapper(main)