colors = {
    "black": "#000000",
    "white": "#FFFFFF",
    "red": "#FF0000",
    "green": "#008000",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
    "cyan": "#00FFFF",
    "magenta": "#FF00FF",
    "gray": "#808080",
    "orange": "#FFA500",
    "purple": "#800080",
    "brown": "#A52A2A",
    "pink": "#FFC0CB",
    "lime": "#00FF00",
    "teal": "#008080",
    "navy": "#000080",
    "gold": "#FFD700",
    "silver": "#C0C0C0",
    "maroon": "#800000",
    "olive": "#808000",
    "dark_gray": "#323232"
}

def get_color(color, backup="#000000"):
    return colors.get(color, backup)

BACKGROUND_COLOR = get_color("dark_gray")

WALL_COLOR = get_color("black")

MOVE_COLOR = get_color("red", "#FFFFFF")

FILL_COLOR = BACKGROUND_COLOR

