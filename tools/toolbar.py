from libqtile import widget



def textfilter(text):
    return " "

colors_1 = "#000000"
colors_2 = "#c0c5ce"
colors_3 = "#fab387"
colors_5 = "#cccccc"
colors_9 = "#555555"

sep = {
    "padding": 25,
    "foreground" : colors_1
}

style = {
    "padding": 5,
}

vol_cur  = "amixer"

def init_widgets_list_left():
    widgets_list = [


            widget.Sep(**sep),


            widget.TaskList(
                max_title_width=45,
                parse_text=textfilter,
                icon_size=20,
                font="Inter Medium",
                background=colors_1,
                foreground=colors_3,
                padding_x = 10,
                fontsize = 17,
                margin_x = 40,
                margin_y= -2,
                txt_minimized="",
                highlight_method="block",
                rounded = False,
                border="#777777",
                urgent_border="#ff0000",
                title_width_method="uniform",
                theme_mode = 'preferred',
                theme_path = '/usr/share/icons/hicolor',
                icons_only=True
            ),

            widget.GroupBox(
                    text="",
                    font="Inter Medium",
                    fontsize = 17,
                    margin_y = 3,
                    margin_x = 0,
                    padding_x = 20,
                    borderwidth = 0,
                    disable_drag = True,
                    active = colors_3,
                    inactive = colors_9,
                    # rounded = False,
                    highlight_method = "block",
                    center_aligned=True,
                    this_current_screen_border = "#777777",
                    foreground = colors_2,
                    background = colors_1,
                    padding = 10,

                    ),

            widget.TaskList(
                max_title_width=25,
                parse_text=textfilter,
                icon_size=0,
                font="Inter Medium",
                border="#000000",
            ),
        ]
    return widgets_list


def init_widgets_list_right():
    widgets_list = [


            # Volume
            widget.TextBox(
                text="",
                foreground=colors_3,
                font="Font Awesome",
                fontsize = 17,
            ),
            widget.Volume(
                get_volume_command=vol_cur, # "amixer -D pulse get Master | grep 'Right:' | awk -F'[][]' '{ print $2 }'",
                foreground=colors_5,
                font="Inter Medium",
            ),
            widget.Sep(**sep),
            
            # Battery
            widget.TextBox(
                text="",
                foreground=colors_3,
                font="Font Awesome",
                fontsize = 17,
            ),
            widget.Battery(
                battery_name="BAT0",
                font="Inter Medium",
                foreground=colors_5,
                format="{percent:2.0%}",
                low_foreground="#ff0000",
            ),
            widget.Sep(**sep),


            widget.TextBox(
                text="",
                foreground=colors_3,
                font="Font Awesome",
                fontsize = 17,
                ),


            widget.Clock(
                font="Inter Medium",
                foreground = colors_5,
                format="%H:%M "
                ),

            widget.Sep(**sep),


            widget.TextBox(
                text="",
                foreground=colors_3,
                font="Font Awesome",
                fontsize = 17,
                ),

            widget.Clock(
                font="Inter Medium",
                foreground = colors_5,
                format="%a %b %d ",
                ),

            widget.Sep(**sep),



            


        ]

    return widgets_list




def init_tray():
    widgets_list = [

        widget.Systray(
            background=colors_1,
            icon_size=20,
            padding = 25,
            ),
        # tray = widget.StatusNotifier(
        #     background=colors_1,
        #     icon_size=20,
        #     padding = 15,)
        # b=widget.Sep(**sep)
        widget.Sep(**sep),

    ]           

    return widgets_list
