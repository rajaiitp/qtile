from libqtile.lazy import lazy
from libqtile.config import Key
from libqtile.log_utils import logger
import time
from libqtile.config import Match
mod = "mod4"

def latest_group(qtile):
    qtile.current_screen.set_group(qtile.current_screen.previous_group)

def find_or_run(app, wm_class):
       
    def __inner(qtile):

        # Get the window objects from windows_map
        for window in qtile.windows_map.values():


            # Check if the window matches your desired class
            if hasattr(window, "match") and window.match(Match(wm_class=wm_class)):

                # Switch to the group where the window is
                qtile.current_screen.set_group(window.group)

                # Focus the window
                window.focus(False)

                # Exit the function
                return

        # If we're here, the app wasn't found so we launch it
        qtile.spawn(app)

    return __inner


keys = [
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "Tab", lazy.function(latest_group)),
    # Key([mod, "shift"], "r", lazy.restart()),
    Key([mod], "Equal",lazy.layout.shrink_main()),
    Key([mod], "Minus",lazy.layout.grow_main()),
    Key([mod], "Space", lazy.layout.swap_main()),
    Key([mod], "Left", lazy.group.next_window()),
    Key([mod], "Right", lazy.group.prev_window()),
    Key([mod], "Up", lazy.window.toggle_maximize()),  
    Key([mod], "Down", lazy.window.toggle_minimize()),  
    Key([mod, "shift"], "Space", lazy.window.toggle_floating()),
    Key(["control"], "Up", lazy.spawn("amixer set Master 5%+")),
    Key(["control"], "Down", lazy.spawn("amixer set Master 5%-")),
    ]


#launcher short-keys
keys.extend([
    Key([mod], "r", lazy.function(find_or_run("alacritty","Alacritty"))),
    Key([mod], "a", lazy.spawn("flameshot gui")),
    # Key([mod], "a", lazy.spawn('grim -g "$(slurp)" - | wl-copy', shell=True) ),
    # Key([mod, "shift"], "a", lazy.spawn('grim -g "$(slurp)" - | swappy -f -', shell=True) ),

    Key([mod], "v", lazy.spawn("pavucontrol")),
    Key([mod], "Escape", lazy.spawn("xkill")),
    Key([mod], "i", lazy.spawn("firefox --private-window")),
    Key([mod], "b", lazy.spawn("firefox")),
    Key([mod], "e", lazy.function(find_or_run("thunar","thunar"))),
    Key([mod], "k", lazy.function(find_or_run("slack","slack"))),
    Key([mod], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
    Key([mod], "s", lazy.spawn("subl")),
    Key([mod], "t", lazy.spawn("teams-for-linux")),
    Key([mod], "o", lazy.function(find_or_run("obsidian","obsidian"))),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod, "shift"], "r", lazy.spawn("qtile cmd-obj -o cmd -f reload_config")),
    Key([mod], "g", lazy.spawn("google-chrome-stable")),
    Key([mod, "shift"], "l", lazy.spawn("i3lock -i /usr/share/backgrounds/arcolinux-dual/beautiful-morning.png --nofork ")),
    Key([mod, "shift"], "s", lazy.spawn("systemctl suspend")),
    Key([mod, "shift"], "h", lazy.spawn("systemctl hibernate")),


])


#setting up the function keys
keys.extend([
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")), 
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")), 
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5+%")), 
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5-%")), 


    # Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")), 
    # Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")), 
])




keys.extend([
    Key(["control","mod1"], "d", lazy.spawn("/home/raja/.screenlayout/desktop.sh")),
    Key(["control","mod1"], "l", lazy.spawn("/home/raja/.screenlayout/laptop.sh")),
    Key(["control","mod1"], "p", lazy.spawn("/home/raja/.screenlayout/pasqal.sh")),

])
