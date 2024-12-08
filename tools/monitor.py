from .toolbar import *
colors_1 = "#000000"
colors_2 = "#c0c5ce"
colors_3 = "#fab387"
colors_5 = "#cccccc"
colors_9 = "#555555"


def init_widgets_screen_bar():
    widgets_screen = init_widgets_list()
    tray=widget.Systray(
        background=colors_1,
        icon_size=20,
        padding = 15,
        )
    # tray = widget.StatusNotifier(
    #     background=colors_1,
    #     icon_size=20,
    #     padding = 15,)
    # b=widget.Sep(**sep)
    widgets_screen.append(tray)
    # widgets_screen.append(b)
    return widgets_screen

def init_widgets_screen():
    return init_widgets_list()