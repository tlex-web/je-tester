class colors:
    """
    bcolors class to color the output of the program
    """

    HEADER = "\033[95m"  # Purple
    OKBLUE = "\033[94m"  # Blue
    OKGREEN = "\033[92m"  # Green
    WARNING = "\033[93m"  # Yellow
    FAIL = "\033[91m"  # Red
    ENDC = "\033[0m"  # White
    BOLD = "\033[1m"  # Bold
    UNDERLINE = "\033[4m"  # Underline


def print_color(color: colors, text):
    """
    Print the text with the color specified
    """
    print(f"{color} {text} {colors.ENDC}")
