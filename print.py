from colorama import init, Fore, Style
init(autoreset=True)
def print_color(text, color="white"):
    color_map = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
    }
    print(f"{color_map.get(color, Fore.WHITE)}{text}{Style.RESET_ALL}",end=" ")
