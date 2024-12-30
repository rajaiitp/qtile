import os
import re
import subprocess
from libqtile import layout, bar, hook
from libqtile.config import Drag, Group, Key, Match, Screen
from tools.monitor import *
from libqtile.lazy import lazy
from libqtile.backend.wayland import InputConfig
import keys

mod = "mod4"
colors_1 = "#000000"
colors_2 = "#c0c5ce"
colors_3 = "#fab387"
colors_5 = "#cccccc"
colors_9 = "#555555"
keys = keys.keys
group_names = ["1", "2", "3", "4", "5", "6", "7", "8","9","0"]
group_labels = ["-1", "-2", "-3", "-4","-5", "-6","-7","-8","-9","-0"]
match = [
[""],[""],[""],[""],#1,2,3,4
["sublime_text", "Sublime_text","obsidian", "Obsidian"],[""],#5,6
["thunar", "Thunar"],#7
["google-chrome", "Google-chrome"],#8
["teams-for-linux","slack"],#9
["Alacritty","alacritty"]#0
]

layout_theme = {
    "margin":5,
    "border_focus": "#fab387",
    "border_normal": "#000000",
}
layouts = [
    layout.MonadThreeCol(**layout_theme,ratio=0.5, single_border_width=0, border_width=1),
]


groups = []
for i in range(len(group_names)):
    groups.append(Group(
        name=group_names[i],
        # layout= layout.MonadThreeCol(**layout_theme,ratio=0.5, single_border_width=0, border_width=1),
        label=group_labels[i],
        matches=[Match(wm_class=re.compile(rf"^{'|'.join(match[i])}$"))]
    ))
for index,i in enumerate(groups):
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key(["mod1"], i.name, lazy.window.togroup(i.name)),
        Key(["control"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])



def init_widgets_defaults():
    return dict(font="Noto Sans Bold",
                fontsize = 14,
                padding = 2,
                background=colors_1)

widget_defaults = init_widgets_defaults()

def init_screens():
    wall_loc = "/usr/share/backgrounds/arcolinux-dual/beautiful-morning.png"
    main_scr = [Screen(wallpaper =wall_loc, wallpaper_mode = 'fill', top=bar.Bar(widgets=init_widgets_screen_tray(), size=20, opacity=1))]
    add_scr = [Screen(wallpaper =wall_loc, wallpaper_mode = 'fill', top=bar.Bar(widgets=init_widgets_screen(), size=20, opacity=1)) for _ in range(2)]
    return main_scr+add_scr
screens = init_screens()



# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag(["mod1"], "Button1", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

@hook.subscribe.startup_once
def start_once():
    subprocess.call([os.path.expanduser('~') + '/.config/qtile/scripts/autostart.sh'])


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='archlinux-logout.py'),
    Match(wm_class='Archlinux-logout.py'),
    Match(wm_class='error'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='feh'),
    Match(wm_class='archlinux-logout'),
    Match(wm_class='pavucontrol'),
],  fullscreen_border_width = 0, border_width = 0, border_focus=colors_3)



wl_input_rules = {
    "type:keyboard": InputConfig(dwt=True, kb_variant="altgr-intl", kb_layout="us"),
    "*": InputConfig(tap=True, natural_scroll=True),
}
auto_fullscreen = False
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
focus_on_window_activation =  "focus" #"smart"
reconfigure_screens = True
auto_minimize = True
floats_kept_above = True
wmname = "LG3D"
