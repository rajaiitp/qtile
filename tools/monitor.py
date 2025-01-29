from .toolbar import *
colors_1 = "#000000"
colors_2 = "#c0c5ce"
colors_3 = "#fab387"
colors_5 = "#cccccc"
colors_9 = "#555555"


def init_widgets_screen_tray():

    # widgets_screen.append(b)
    return init_tray() + init_widgets_list_left() + init_widgets_list_right()

def init_widgets_screen():
    return init_widgets_list_left() + init_widgets_list_right()