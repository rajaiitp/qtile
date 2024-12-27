from libqtile import widget

colors_1 = "#000000"
colors_2 = "#c0c5ce"
colors_3 = "#fab387"
colors_5 = "#cccccc"
colors_9 = "#555555"

sep = {
    "padding": 20,
    "foreground" : colors_1
}

style = {
    "padding": 5,
}

vol_cur  = "amixer"

def init_widgets_list_left():
    widgets_list = [
            widget.GroupBox(
                    text="",
                    font="Font Awesome",
                    fontsize = 14,
                    margin_y = 5,
                    margin_x = 0,
                    padding_x = 15,
                    borderwidth = 0,
                    # disable_drag = True,
                    active = colors_3,
                    inactive = colors_9,
                    # rounded = False,
                    highlight_method = "block",
                    this_current_screen_border = "#777777",
                    foreground = colors_2,
                    background = colors_1,
                    padding = 10,
                    ),
            widget.Sep(
                    linewidth = 0,
                    padding = 30,
                    foreground = colors_2,
                    background = colors_1
                    ),

            widget.Sep(**sep),


            widget.TaskList(
                max_title_width=250,
                icon_size=0,
                background=colors_1,
                foreground=colors_3,
                padding_x = 20,
                fontsize = 12,
                highlight_method="block",
                border="#777777",
                urgent_border="#ff0000",
            ),

        ]
    return widgets_list


def init_widgets_list_right():
    widgets_list = [

            widget.TextBox(
                text="",
                foreground=colors_3,
                font="Font Awesome",
                fontsize = 14,
                ),


            widget.Clock(
                font="Noto Sans Bold",
                foreground = colors_5,
                format="%H:%M "
                ),

            widget.Sep(**sep),


            widget.TextBox(
                text="",
                foreground=colors_3,
                font="Font Awesome",
                fontsize = 14,
                ),

            widget.Clock(
                foreground = colors_5,
                format="%a %b %d ",
                ),

            widget.Sep(**sep),



            # Battery
            widget.TextBox(
                text="",
                foreground=colors_3,
                font="Font Awesome",
                fontsize = 14,
            ),
            widget.Battery(
                battery_name="BAT0",
                foreground=colors_5,
                format="{percent:2.0%}",
                low_foreground="#ff0000",
            ),
            widget.Sep(**sep),


            # Volume
            widget.TextBox(
                text="",
                foreground=colors_3,
                font="Font Awesome",
                fontsize = 14,
            ),
            widget.Volume(
                get_volume_command=vol_cur, # "amixer -D pulse get Master | grep 'Right:' | awk -F'[][]' '{ print $2 }'",
                foreground=colors_5,
                fontsize = 14,
            ),
            widget.Sep(**sep),
        ]

    return widgets_list




def init_tray():
    widgets_list = [

        widget.Systray(
            background=colors_1,
            icon_size=20,
            padding = 15,
            ),
        # tray = widget.StatusNotifier(
        #     background=colors_1,
        #     icon_size=20,
        #     padding = 15,)
        # b=widget.Sep(**sep)
        widget.Sep(**sep),

    ]           

    return widgets_list