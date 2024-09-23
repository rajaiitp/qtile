# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.lazy import lazy
from libqtile.widget import Spacer

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')
battery      = "BAT0"

def latest_group(qtile):
    qtile.current_screen.set_group(qtile.current_screen.previous_group)

# keys += [Key(["mod4"], "s", lazy.function(latest_group))]

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

# @lazy.function
# def float_to_front(qtile):
#     for window in qtile.currentGroup.windows:
#         if window.floating:
#             window.cmd_bring_to_front()



if False:
    vol_cur  = None
    vol_up   = "pactl set-sink-volume @DEFAULT_SINK@ +2%"
    vol_down = "pactl set-sink-volume @DEFAULT_SINK@ -2%"
    mute     = "pactl set-sink-mute @DEFAULT_SINK@ toggle"
else:
    vol_cur  = "amixer -D pulse get Master"
    vol_up   = "amixer -q -D pulse sset Master 2%+"
    vol_down = "amixer -q -D pulse sset Master 2%-"
    mute     = "amixer -q -D pulse set Master toggle"


keys = [

# Most of our keybindings are in sxhkd file - except these

# SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),


    Key([mod], "Tab", lazy.function(latest_group)),


# SUPER + SHIFT KEYS

    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),


# QTILE LAYOUT KEYS
    # Key([mod], "n", float_to_front()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    # Key([mod], "Up", lazy.layout.up()),
    # Key([mod], "Down", lazy.layout.down()),
    # Key([mod], "Left", lazy.group.prev_window()),
    # Key([mod], "Right", lazy.group.next_window()),


# RESIZE UP, DOWN, LEFT, RIGHT
    # Key([mod], "l",
    #     # lazy.layout.grow_right(),
    #     lazy.layout.grow(),
    #     # lazy.layout.increase_ratio(),
    #     # lazy.layout.delete(),
    #     ),
    #   Key([mod, "control"], "h",
    #     # lazy.layout.grow_left(),
    #     lazy.layout.shrink(),
    #     # lazy.layout.decrease_ratio(),
    #     # lazy.layout.add(),
    #     ),
    Key([mod], "equal",
        # lazy.layout.grow_up(),
        lazy.layout.shrink_main(),
        # lazy.layout.decrease_nmaster(),
        ),
    Key([mod], "minus",
        # lazy.layout.grow_down(),
        lazy.layout.grow_main(),
        # lazy.layout.increase_nmaster(),
        ),
 
    Key([mod], "comma", lazy.layout.shuffle_left()),
    Key([mod], "period", lazy.group.next_window()),

# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),

    ]



keys.extend([
    Key([mod, "shift"], "s", lazy.spawn("sxhkd -c /home/raja/.config/qtile/sxhkd/sxhkdrc")),
    Key([mod], "h", lazy.spawn("alacritty")),
    ])

# def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
#     i = qtile.screens.index(qtile.current_screen)
#     if i != 0:
#         group = qtile.screens[i - 1].group.name
#         qtile.current_window.togroup(group, switch_group=switch_group)
#         if switch_screen == True:
#             qtile.cmd_to_screen(i - 1)

# def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
#     i = qtile.screens.index(qtile.current_screen)
#     if i + 1 != len(qtile.screens):
#         group = qtile.screens[i + 1].group.name
#         qtile.current_window.togroup(group, switch_group=switch_group)
#         if switch_screen == True:
#             qtile.cmd_to_screen(i + 1)

# keys.extend([
#     # MOVE WINDOW TO NEXT SCREEN
#     Key([mod,"shift"], "Right", lazy.function(window_to_next_screen, switch_screen=True)),
#     Key([mod,"shift"], "Left", lazy.function(window_to_previous_screen, switch_screen=True)),
# ])


# FOR AZERTY KRREYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
#group_labels = ["", "", "", "", "", "", "", "", "", "",]

icons = {
    "logo": "",     # fa-redhat
    "temp": "",     # fa-fire-extinguisher
    "battery": "",  # fa-battery-three-quarters
    "light": "",    # fa-lightbulb-o
    "volume": "",   # fa-bullhorn
    "rss": "",      # fa-rss
    "sync": "",     # fa-sync-alt
    "tasks": "",    # fa-calendar-check-o
    "repeat": "",   # fa-repeat
    "email": "",    # fa-at
    "gmail": "",      # fa-google

    "chat": "",      # fa-comment-dots
    "web": "",      # fa-internet-explorer
    "terminal": "", # fa-keyboard
    "dev": "",      # fa-heart
    "doc": "",      # fa-folder
    "misc": "",     # fa-file
    "ssh": "",      # fa-hashtag
    "virtual": "", # fa-cogs
    "games": "",     # fa-playstation
    "music": "",    # fa-headphones

    "max": "",       # fa-window-maximize
    "monadtall": "", # fa-columns
    "treetab": "",   # fa-tree

    "systray": "",  # fa-fedora
}

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "o", "k", "s", "e", "y","u","g","t","p","r"]

group_labels = ["-1", "-2", "-3", "-4", "-5","-6","-O", "-K", "-S", "-E","-Y","-U","-G","-T","-P","-R"]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]


match = [
[""],
#1
[""],
#2
[""],
#3
[""],
#4
[""],
#5
[],
#6
["obsidian", "Obsidian"],
#7
["teams","slack"],
#8
["subl"],
#9
["thunar", "Thunar"], 
#10
["telegram-desktop", "TelegramDesktop","signal", "Signal"],
#11
["spotify", "Spotify"],
#12
["google-chrome", "Google-chrome"],
#13
["teams","microsoft teams - preview", "Microsoft Teams - Preview"],
#14
["Steam","steam"],

["Alacritty"]
]
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout="monadtall".lower(),
            label=group_labels[i],
            matches=[Match(wm_class=re.compile(r"^(match[i])$"))]

        ))

for index,i in enumerate(groups):
    if index < 6:

        keys.extend([
            Key([mod], i.name, lazy.group[i.name].toscreen()),
        ])

    keys.extend([
        # Key([mod], "Tab", lazy.screen.next_group()),
        # Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        # Key(["mod1"], "Tab", lazy.screen.next_group()),
        # Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
        # Key([mod], i.name, lazy.group[i.name].toscreen()),


# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key(["mod1", "control"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key(["mod1"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


def init_layout_theme():
    return {"margin":5,
            "border_focus": "#fab387",
            # "border_focus": "#cf4d0a",

            
            "border_normal": "#000000",
            }

layout_theme = init_layout_theme()

style = {
    "padding": 5,
}

layouts = [
    layout.MonadThreeCol(**layout_theme,ratio=0.5, single_border_width=0, border_width=1),
    # layout.MonadTall(**layout_theme),
    #layout.MonadWide(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    # layout.MonadWide(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.Floating(**layout_theme),
    # layout.Max(**layout_theme, border_width=0)
    # layout.RatioTile(**layout_theme),
]

# COLORS FOR THE BAR
#Theme name : ArcoLinux Default
def init_colors():
    return [["#000000", "#000000"], # color 0
            ["#000000", "#000000"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#fab387", "#fab387"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#cccccc", "#cccccc"], # color 5
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#6790eb", "#6790eb"], # color 8
            ["#555555", "#555555"]] # color 9


colors = init_colors()
sep = {
    "padding": 15,
    "foreground" : colors[1]
}

# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sans Bold",
                fontsize = 12,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [

                widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.GroupBox(
                        text=icons["logo"],
                        font="Bold Font Awesome",
                        fontsize = 17,
                        margin_y = 5,
                        margin_x = 0,
                        padding_x = 10,
                        borderwidth = 0,
                        disable_drag = True,
                        active = colors[3],
                        inactive = colors[9],
                        rounded = False,
                        highlight_method = "block",
                        this_current_screen_border = "#777777",
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 0,
                        padding = 30,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               # widget.CurrentLayout(
               #          font = "Noto Sans Bold",
               #          foreground = colors[5],
               #          background = colors[1]
               #          ),
               # widget.Sep(
               #          linewidth = 0,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.WindowName(font="Noto Sans",
               #          fontsize = 12,
               #          foreground = colors[3],
               #          background = colors[1],
               #          ),

            widget.Sep(**sep),


            widget.TaskList(
                max_title_width=250,
                icon_size=0,
                background=colors[1],
                foreground="#888888",

                highlight_method="text",
                border=colors[3],
                urgent_border="#ff0000",
            ),



                            #     text=icons["gmail"],
            #     foreground=base16_chalk["green"],
            #     **style
            # ),
            # Mu(
            #     "/home/jkadlcik/Mail",
            #     "/gmail/*",
            #     "jakub.kadlcik@gmail.com",
            #     foreground=base16_chalk["green"],
            #     **style
            # ),
            # widget.Sep(**sep),


            # Temp



            widget.TextBox(
                text="",
                foreground=colors[3],
                font="Font Awesome",
                fontsize = 14,
                **style
                ),

            widget.Clock(
                        font="Noto Sans Bold",
                        foreground = colors[5],
                                                fontsize = 14,

                        format="%H:%M "
                ),

            widget.Sep(**sep),


            widget.TextBox(
                text="",
                foreground=colors[3],
                font="Font Awesome",
                fontsize = 14,
                **style
                ),

            widget.Clock(
                        font="Noto Sans Bold",
                        foreground = colors[5],
                        format="%a %b %d ",
                                        fontsize = 14,
                ),

            widget.Sep(**sep),



            # Battery
            widget.TextBox(
                text=icons["battery"],
                foreground=colors[3],
                font="Font Awesome",
                                fontsize = 14,
                **style
            ),
            widget.Battery(
                battery_name=battery,
                foreground=colors[5],
                format="{percent:2.0%}",
                low_foreground="#ff0000",
                                fontsize = 14,
                **style
            ),
            widget.Sep(**sep),





            # Volume
            widget.TextBox(
                text=icons["volume"],
                foreground=colors[3],
                font="Font Awesome",
                                fontsize = 14,
                **style
            ),
            widget.Volume(
                get_volume_command=(vol_cur.split() if vol_cur else None),
                foreground=colors[5],
                                fontsize = 14,
                **style
            ),
            widget.Sep(**sep),


            # # Light
            # widget.TextBox(
            #     text=icons["light"],
            #     foreground=colors[3],
            #     font="Font Awesome",
            #                     fontsize = 14,
            #     **style
            # ),
            # widget.Backlight(
            #     brightness_file="/sys/class/backlight/intel_backlight/actual_brightness",
            #     max_brightness_file="/sys/class/backlight/intel_backlight/max_brightness",
            #     foreground=colors[5],
            #                     fontsize = 14,
            #     **style
            # ),
            # widget.Sep(**sep),



            # widget.TextBox(
            #     text=icons["temp"],
            #     foreground=colors[3],
            #     font="Font Awesome",
            #                     fontsize = 14,
            #     **style
            # ),
            # widget.ThermalSensor(
            #     threshold=65,
            #     foreground=colors[5],
            #     foreground_alert="#f2777a",
            #                     fontsize = 14,
            #     **style
            # ),





                # arcobattery.BatteryIcon(
                #         padding=0,
                #         scale=0.7,
                #         y_poss=2,
                #         theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
                #         update_interval = 5,
                #         background = colors[1]
                #         ),

               # widget.Sep(
               #          linewidth = 1,
               #          padding = 10,
               #          foreground = colors[2],
               #          background = colors[1]
               #          ),
               # widget.Systray(
               #          background=colors[1],
               #          icon_size=20,
               #          padding = 15,
               #          ),
               #             widget.Sep(**sep),


              ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    a=widget.Systray(
        background=colors[1],
        icon_size=20,
        padding = 15,
        )
    b=widget.Sep(**sep)
    widgets_screen1.append(a)
    widgets_screen1.append(b)
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

def init_widgets_screen3():
    widgets_screen3 = init_widgets_list()
    return widgets_screen3

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()
widgets_screen3 = init_widgets_screen3()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=1)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=1)),
            Screen(top=bar.Bar(widgets=init_widgets_screen3(), size=20, opacity=1))]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod1], "Button1", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]


# def latest_group(qtile):
#     qtile.current_screen.set_group(qtile.current_screen.previous_group)

# keys += [Key(["mod4"], "s", lazy.function(latest_group))]




dgroups_key_binder = None
dgroups_app_rules = []


# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

#########################################################
################ assgin apps to groups ##################
#########################################################
# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #####################################################################################
#     ### Use xprop fo find  the value of WM_CLASS(STRING) -> First field is sufficient ###
#     #####################################################################################
#     d[group_names[0]] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d[group_names[1]] = [ "Atom", "Subl", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                "atom", "subl", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d[group_names[2]] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d[group_names[3]] = ["Gimp", "gimp" ]
#     d[group_names[4]] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d[group_names[5]] = ["Vlc","vlc", "Mpv", "mpv" ]
#     d[group_names[6]] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
#               "virtualbox manager", "virtualbox machine", "vmplayer", ]
#     d[group_names[7]] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#               "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d[group_names[8]] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d[group_names[9]] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
#               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
#     ######################################################################################
#
# wm_class = client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen(toggle=False)

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME



main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='Arcolinux-welcome-app.py'),
    Match(wm_class='Arcolinux-calamares-tool.py'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='archlinux-logout.py'),
    Match(wm_class='Archlinux-logout.py'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='archlinux-logout'),
    Match(wm_class='xfce4-terminal'),
    Match(wm_class='Pavucontrol'),
],  fullscreen_border_width = 0, border_width = 1, border_focus=colors[3])
auto_fullscreen = False

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
